from typing import Dict, List, Optional, Tuple

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config import (
    CHROMA_DB_DIR,
    EMBEDDING_MODEL,
    FETCH_K,
    MIN_RELEVANCE_SCORE,
    MMR_LAMBDA,
    RETRIEVAL_STRATEGY,
    TOP_K,
)
from app.embeddings import get_embedding_model

# =====================================================
# Cached Objects
# =====================================================

_vector_db = None
_similarity_retriever = None
_mmr_retriever = None


# =====================================================
# Vector Database
# =====================================================

def get_vector_db() -> Chroma:
    """
    Load the Chroma vector database only once.
    """

    global _vector_db

    if _vector_db is None:

        print("\nLoading Chroma Vector Database...")

        _vector_db = Chroma(
            persist_directory=str(CHROMA_DB_DIR),
            embedding_function=get_embedding_model(),
        )

        print("✓ Vector database loaded successfully.")

    return _vector_db


# =====================================================
# Similarity Retriever
# =====================================================

def get_similarity_retriever():

    global _similarity_retriever

    if _similarity_retriever is None:

        _similarity_retriever = get_vector_db().as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": TOP_K,
            },
        )

    return _similarity_retriever


# =====================================================
# MMR Retriever
# =====================================================

def get_mmr_retriever():

    global _mmr_retriever

    if _mmr_retriever is None:

        _mmr_retriever = get_vector_db().as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": TOP_K,
                "fetch_k": FETCH_K,
                "lambda_mult": MMR_LAMBDA,
            },
        )

    return _mmr_retriever


# =====================================================
# Default Retriever
# =====================================================

def get_retriever(strategy: Optional[str] = None):

    strategy = (
        strategy or RETRIEVAL_STRATEGY
    ).lower()

    if strategy == "mmr":
        return get_mmr_retriever()

    return get_similarity_retriever()


# =====================================================
# Basic Search
# =====================================================

def search(
    query: str,
    strategy: Optional[str] = None,
):
    """
    Standard retrieval without scores.
    """

    return get_retriever(
        strategy
    ).invoke(query)


# =====================================================
# Internal Helper
# =====================================================

def _filter_results(
    results: List[Tuple[Document, float]],
    min_score: float,
) -> List[Tuple[Document, float]]:
    """
    Apply confidence threshold.
    """

    if min_score < 0:
        min_score = 0

    if min_score > 1:
        min_score = 1

    return [
        (doc, score)
        for doc, score in results
        if score >= min_score
    ]


# =====================================================
# Similarity Search
# =====================================================

def search_with_scores(
    query: str,
    min_score: float = MIN_RELEVANCE_SCORE,
) -> List[Tuple[Document, float]]:
    """
    Similarity retrieval with confidence filtering.
    """

    db = get_vector_db()

    results = db.similarity_search_with_relevance_scores(
        query=query,
        k=TOP_K,
    )

    return _filter_results(
        results,
        min_score,
    )


# =====================================================
# MMR Search
# =====================================================

def mmr_search_with_scores(
    query: str,
    min_score: float = MIN_RELEVANCE_SCORE,
) -> List[Tuple[Document, float]]:
    """
    MMR retrieval combined with similarity confidence.
    """

    mmr_docs = get_mmr_retriever().invoke(
        query
    )

    similarity_results = search_with_scores(
        query,
        min_score=0.0,
    )

    similarity_lookup: Dict[
        str,
        float,
    ] = {
        doc.page_content: score
        for doc, score in similarity_results
    }

    merged = []

    for doc in mmr_docs:

        score = similarity_lookup.get(
            doc.page_content,
            0.0,
        )

        merged.append(
            (
                doc,
                score,
            )
        )

    return _filter_results(
        merged,
        min_score,
    )


# =====================================================
# Debug Utility
# =====================================================

def inspect_query(
    query: str,
    min_score: float = 0.0,
):
    """
    Print retrieval scores.
    """

    print("\nQuery:", query)
    print("-" * 70)

    results = search_with_scores(
        query,
        min_score=min_score,
    )

    if not results:

        print("No matching chunks.")
        return

    for i, (doc, score) in enumerate(
        results,
        start=1,
    ):

        title = doc.metadata.get(
            "paper_title",
            "Unknown",
        )

        page = doc.metadata.get(
            "page",
            "-",
        )

        print(
            f"{i:02d}. "
            f"Score={score:.3f} | "
            f"{title} | "
            f"Page {page}"
        )


# =====================================================
# Retriever Information
# =====================================================

def print_retriever_info():

    print("\nRetriever Configuration")
    print("-" * 50)

    print(
        f"Embedding Model : {EMBEDDING_MODEL}"
    )

    print(
        f"Strategy        : {RETRIEVAL_STRATEGY}"
    )

    print(
        f"Top K           : {TOP_K}"
    )

    print(
        f"Fetch K         : {FETCH_K}"
    )

    print(
        f"MMR Lambda      : {MMR_LAMBDA}"
    )

    print(
        f"Confidence Cutoff : {MIN_RELEVANCE_SCORE}"
    )
