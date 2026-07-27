import shutil
from pathlib import Path

from langchain_chroma import Chroma

from app.config import CHROMA_DB_DIR
from app.embeddings import get_embedding_model


def create_vector_store(chunks):
    """
    Create a fresh ChromaDB vector store.

    Existing database will be deleted to prevent duplicate vectors.

    Args:
        chunks: List of LangChain Document chunks.

    Returns:
        Chroma: Persisted vector database.
    """

    db_path = Path(CHROMA_DB_DIR)

    # Remove existing database
    if db_path.exists():
        print("\nRemoving existing vector database...")
        shutil.rmtree(db_path)

    db_path.mkdir(parents=True, exist_ok=True)

    embeddings = get_embedding_model()

    print("\nCreating new vector database...")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DB_DIR),
    )

    print("✓ Vector database created successfully!")
    print(f"✓ Total vectors stored: {vector_db._collection.count()}")

    return vector_db


def load_vector_store():
    """
    Load an existing ChromaDB vector database.

    Returns:
        Chroma: Loaded vector database.

    Raises:
        FileNotFoundError: If the vector database does not exist.
    """

    db_path = Path(CHROMA_DB_DIR)

    if not db_path.exists():
        raise FileNotFoundError(
            "Vector database not found.\n"
            "Run 'python build_vector_db.py' first."
        )

    embeddings = get_embedding_model()

    return Chroma(
        persist_directory=str(CHROMA_DB_DIR),
        embedding_function=embeddings,
    )
