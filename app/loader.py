from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

from app.config import RAW_DATA_DIR


# Mapping of PDF filename -> Actual Research Paper Title
PAPER_TITLES = {
    "attention": "Attention Is All You Need",
    "bert": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "gpt3": "Language Models are Few-Shot Learners",
    "rag": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "instructgpt": "Training Language Models to Follow Instructions with Human Feedback",
    "llama": "LLaMA: Open and Efficient Foundation Language Models",
    "llama2": "Llama 2: Open Foundation and Fine-Tuned Chat Models",
    "cot": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
    "react": "ReAct: Synergizing Reasoning and Acting in Language Models",
    "selfrag": "Self-RAG: Learning to Retrieve, Generate and Critique",
}


def load_documents() -> List[Document]:
    """
    Load all research papers from the raw_papers directory.

    Returns:
        List[Document]: LangChain Document objects with enriched metadata.
    """

    documents: List[Document] = []

    pdf_files = sorted(Path(RAW_DATA_DIR).glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in: {RAW_DATA_DIR}"
        )

    print("\n" + "=" * 60)
    print(f"Found {len(pdf_files)} research papers")
    print("=" * 60)

    total_pages = 0

    for pdf in pdf_files:

        print(f"\nLoading: {pdf.name}")

        loader = PyPDFLoader(str(pdf))
        pages = loader.load()

        paper_key = pdf.stem.lower()

        paper_title = PAPER_TITLES.get(
            paper_key,
            pdf.stem.replace("_", " ").title()
        )

        for page in pages:
            page.metadata.update(
                {
                    "source": pdf.name,
                    "paper_id": paper_key,
                    "paper_title": paper_title,
                    "file_name": pdf.name,
                    "page_number": page.metadata.get("page", 0),
                }
            )

        documents.extend(pages)

        total_pages += len(pages)

        print(f"   ✓ {len(pages)} pages loaded")

    print("\n" + "=" * 60)
    print("Document Loading Completed")
    print("=" * 60)
    print(f"Research Papers : {len(pdf_files)}")
    print(f"Total Pages     : {total_pages}")
    print(f"Documents       : {len(documents)}")
    print("=" * 60)

    return documents
