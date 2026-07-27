import shutil
import time

from app.chunking import chunk_documents
from app.config import (
    CHROMA_DB_DIR,
    EVALUATION_QUERIES,
)
from app.embeddings import (
    get_embedding_model_name,
    reset_embedding_model,
)
from app.loader import load_documents
from app.retriever import (
    get_retriever,
    print_retriever_info,
)
from app.vector_store import create_vector_store


# =====================================================
# Build Vector Database
# =====================================================

def rebuild_database():
    """
    Rebuild the Chroma vector database using the
    currently configured embedding model.
    """

    print("\n" + "=" * 80)
    print("BUILDING VECTOR DATABASE")
    print("=" * 80)

    reset_embedding_model()

    if CHROMA_DB_DIR.exists():
        print("\nRemoving existing vector database...")
        shutil.rmtree(CHROMA_DB_DIR)

    start = time.perf_counter()

    documents = load_documents()

    chunks = chunk_documents(documents)

    print(f"\nTotal Chunks Created : {len(chunks)}")

    create_vector_store(chunks)

    build_time = time.perf_counter() - start

    return documents, chunks, build_time


# =====================================================
# Evaluate Retriever
# =====================================================

def evaluate(strategy="similarity"):
    """
    Evaluate a retrieval strategy.
    """

    retriever = get_retriever(strategy)

    total_time = 0

    print("\n" + "=" * 80)
    print(f"RETRIEVAL STRATEGY : {strategy.upper()}")
    print("=" * 80)

    for index, query in enumerate(EVALUATION_QUERIES, start=1):

        print(f"\n[{index}] {query}")

        start = time.perf_counter()

        docs = retriever.invoke(query)

        retrieval_time = time.perf_counter() - start

        total_time += retrieval_time

        print(f"Retrieval Time : {retrieval_time:.3f} sec")

        print("-" * 80)

        for i, doc in enumerate(docs[:3], start=1):

            title = doc.metadata.get("paper_title", "Unknown")

            page = doc.metadata.get("page", "-")

            preview = (
                doc.page_content[:220]
                .replace("\n", " ")
                .strip()
            )

            print(f"{i}. {title}")
            print(f"   Page : {page}")
            print(f"   Preview : {preview}...")
            print()

    avg_time = total_time / len(EVALUATION_QUERIES)

    print("=" * 80)
    print(f"Average Retrieval Time ({strategy}) : {avg_time:.3f} sec")
    print("=" * 80)

    return avg_time


# =====================================================
# Main
# =====================================================

def main():

    print("=" * 80)
    print("EMBEDDING MODEL COMPARISON")
    print("=" * 80)

    print(f"\nEmbedding Model : {get_embedding_model_name()}")

    documents, chunks, build_time = rebuild_database()

    print("\n" + "=" * 80)
    print("DATABASE SUMMARY")
    print("=" * 80)

    print(f"Documents     : {len(documents)}")
    print(f"Chunks        : {len(chunks)}")
    print(f"Build Time    : {build_time:.2f} sec")

    print_retriever_info()

    similarity_time = evaluate("similarity")

    mmr_time = evaluate("mmr")

    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)

    print(f"Embedding Model       : {get_embedding_model_name()}")
    print(f"Index Build Time      : {build_time:.2f} sec")
    print(f"Similarity Avg Time   : {similarity_time:.3f} sec")
    print(f"MMR Avg Time          : {mmr_time:.3f} sec")

    print("=" * 80)


if __name__ == "__main__":
    main()
