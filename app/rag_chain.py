import re
import unicodedata
from typing import Dict, List, Optional, Tuple

from langchain_core.documents import Document

from app.config import (
    FINAL_TOP_K,
    MIN_RELEVANCE_SCORE,
    RETRIEVAL_STRATEGY,
)
from app.llm import generate_answer
from app.retriever import (
    mmr_search_with_scores,
    search_with_scores,
)

# =====================================================
# Constants
# =====================================================

FALLBACK_MESSAGE = (
    "I couldn't find sufficient evidence in the indexed "
    "research papers to answer this question confidently."
)

MAX_PREVIEW_LENGTH = 350

MIN_AVG_CONFIDENCE = max(
    MIN_RELEVANCE_SCORE,
    0.65,
)

# =====================================================
# Preview Cleaning
# =====================================================

def clean_preview(text: str) -> str:
    """
    Clean retrieved text for UI display only.

    The original chunk sent to the LLM is NOT modified.
    """

    if not text:
        return ""

    text = unicodedata.normalize("NFKC", text)

    replacements = {
        "[CLS]": "",
        "[SEP]": "",
        "##": "",
        "Â": "",
        "Ã": "",
        "�": "",
        "\u00A0": " ",   # Non-breaking space
        "\u200B": "",    # Zero-width space
        "\u200C": "",
        "\u200D": "",
        "\ufeff": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Collapse repeated punctuation
    text = re.sub(r"\.{3,}", "...", text)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    if len(text) > MAX_PREVIEW_LENGTH:
        text = text[:MAX_PREVIEW_LENGTH].rstrip() + "..."

    return text


# =====================================================
# Duplicate Removal
# =====================================================

def remove_duplicate_chunks(
    scored_docs: List[Tuple[Document, float]]
) -> List[Tuple[Document, float]]:
    """
    Remove duplicate retrieved chunks while
    preserving their retrieval scores.
    """

    unique = []
    seen = set()

    for doc, score in scored_docs:

        key = doc.page_content.strip()

        if key not in seen:
            seen.add(key)
            unique.append((doc, score))

    return unique


# =====================================================
# Sources
# =====================================================

def build_sources(
    docs: List[Document],
) -> Dict[str, List[int]]:
    """
    Group retrieved pages by paper title.
    """

    grouped = {}

    for doc in docs:

        paper = doc.metadata.get(
            "paper_title",
            "Unknown",
        )

        page = doc.metadata.get(
            "page",
            "-",
        )

        grouped.setdefault(
            paper,
            set(),
        ).add(page)

    return {
        paper: sorted(pages)
        for paper, pages in grouped.items()
    }


# =====================================================
# Supporting Passages
# =====================================================

def build_passages(
    scored_docs: List[Tuple[Document, float]]
):
    """
    Prepare passages for Streamlit UI.
    """

    passages = []

    for doc, score in scored_docs:

        passages.append(
            {
                "paper": doc.metadata.get(
                    "paper_title",
                    "Unknown",
                ),
                "page": doc.metadata.get(
                    "page",
                    "-",
                ),
                "score": round(score, 3),
                "content": clean_preview(
                    doc.page_content
                ),
            }
        )

    return passages


# =====================================================
# Confidence
# =====================================================

def has_sufficient_confidence(
    scored_docs: List[Tuple[Document, float]]
) -> bool:
    """
    Determine whether retrieved evidence is
    sufficiently reliable.
    """

    if not scored_docs:
        return False

    avg_score = (
        sum(score for _, score in scored_docs)
        / len(scored_docs)
    )

    return avg_score >= MIN_AVG_CONFIDENCE


# =====================================================
# Statistics
# =====================================================

def build_stats(
    question: str,
    retrieval_mode: str,
    scored_docs: List[Tuple[Document, float]],
    papers_used: int,
    confidence_passed: bool,
):
    """
    Build retrieval statistics.
    """

    if scored_docs:

        scores = [
            score
            for _, score in scored_docs
        ]

        avg_score = round(
            sum(scores) / len(scores),
            3,
        )

        top_score = round(
            max(scores),
            3,
        )

    else:

        avg_score = 0.0
        top_score = 0.0

    return {
        "query": question,
        "retrieved_chunks": len(scored_docs),
        "papers_used": papers_used,
        "avg_score": avg_score,
        "top_score": top_score,
        "retrieval_mode": retrieval_mode.upper(),
        "confidence_passed": confidence_passed,
    }


# =====================================================
# Main RAG Pipeline
# =====================================================

def ask(
    question: str,
    strategy: Optional[str] = None,
):

    retrieval_mode = (
        strategy or RETRIEVAL_STRATEGY
    ).lower()

    # -------------------------------------------------
    # Retrieve
    # -------------------------------------------------

    if retrieval_mode == "similarity":

        scored_docs = search_with_scores(
            question
        )

    else:

        retrieval_mode = "mmr"

        scored_docs = mmr_search_with_scores(
            question
        )

    # -------------------------------------------------
    # Remove duplicates
    # -------------------------------------------------

    scored_docs = remove_duplicate_chunks(
        scored_docs
    )

    scored_docs = scored_docs[:FINAL_TOP_K]

    # -------------------------------------------------
    # Confidence check
    # -------------------------------------------------

    if not has_sufficient_confidence(
        scored_docs
    ):

        return {
            "answer": FALLBACK_MESSAGE,
            "sources": {},
            "retrieved_passages": [],
            "stats": build_stats(
                question=question,
                retrieval_mode=retrieval_mode,
                scored_docs=scored_docs,
                papers_used=0,
                confidence_passed=False,
            ),
        }

    docs = [
        doc
        for doc, _ in scored_docs
    ]

    # -------------------------------------------------
    # Build Context
    # -------------------------------------------------

    context = "\n\n".join(
        doc.page_content.strip()
        for doc in docs
    )

    # -------------------------------------------------
    # Generate Answer
    # -------------------------------------------------

    answer = generate_answer(
        question,
        context,
    )

    # -------------------------------------------------
    # Sources
    # -------------------------------------------------

    grouped_sources = build_sources(
        docs
    )

    # -------------------------------------------------
    # Passages
    # -------------------------------------------------

    retrieved_passages = build_passages(
        scored_docs
    )

    # -------------------------------------------------
    # Return
    # -------------------------------------------------

    return {
        "answer": answer,
        "sources": grouped_sources,
        "retrieved_passages": retrieved_passages,
        "stats": build_stats(
            question=question,
            retrieval_mode=retrieval_mode,
            scored_docs=scored_docs,
            papers_used=len(grouped_sources),
            confidence_passed=True,
        ),
    }
