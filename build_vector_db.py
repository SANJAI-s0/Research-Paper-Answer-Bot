import shutil
import time

from app.chunking import chunk_documents
from app.config import (
    CHROMA_DB_DIR,
    CHUNK_OVERLAP,
    CHUNK_SIZE,
)
from app.embeddings import get_embedding_model_name
from app.loader import load_documents
from app.vector_store import create_vector_store


def main():
    print("=" * 70)
    print("RESEARCH PAPER ANSWER BOT")
    print("Vector Database Builder")
    print("=" * 70)

    print("\nConfiguration")
    print("-" * 70)
    print(f"Embedding Model : {get_embedding_model_name()}")
    print(f"Chunk Size      : {CHUNK_SIZE}")
    print(f"Chunk Overlap   : {CHUNK_OVERLAP}")
    print(f"Vector DB       : {CHROMA_DB_DIR}")

    start_time = time.perf_counter()

    # --------------------------------------------------
    # Remove Existing Database
    # --------------------------------------------------
    if CHROMA_DB_DIR.exists():
        print("\nRemoving existing vector database...")
        shutil.rmtree(CHROMA_DB_DIR)

    # --------------------------------------------------
    # Load Documents
    # --------------------------------------------------
    print("\nLoading research papers...")
    documents = load_documents()

    # --------------------------------------------------
    # Chunk Documents
    # --------------------------------------------------
    print("\nCreating text chunks...")
    chunks = chunk_documents(documents)

    print(f"Total Chunks Created : {len(chunks)}")

    # --------------------------------------------------
    # Build Vector Store
    # --------------------------------------------------
    print("\nCreating Chroma Vector Database...")
    create_vector_store(chunks)

    elapsed = time.perf_counter() - start_time

    print("\n" + "=" * 70)
    print("VECTOR DATABASE BUILD COMPLETED")
    print("=" * 70)
    print(f"Embedding Model : {get_embedding_model_name()}")
    print(f"Documents       : {len(documents)}")
    print(f"Chunks Indexed  : {len(chunks)}")
    print(f"Build Time      : {elapsed:.2f} seconds")
    print(f"Database Path   : {CHROMA_DB_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
