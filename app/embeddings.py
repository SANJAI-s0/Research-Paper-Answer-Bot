from langchain_huggingface import HuggingFaceEmbeddings

from app.config import EMBEDDING_MODEL


# ====================================================
# Singleton Embedding Model
# ====================================================

_embedding_model = None


def get_embedding_model():
    """
    Load the Hugging Face embedding model only once.

    Returns
    -------
    HuggingFaceEmbeddings
        Cached embedding model instance.
    """

    global _embedding_model

    if _embedding_model is None:

        print("\n" + "=" * 60)
        print("Loading Embedding Model")
        print(f"Model : {EMBEDDING_MODEL}")
        print("=" * 60)

        _embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu",
            },
            encode_kwargs={
                "normalize_embeddings": True,
            },
        )

        print("✓ Embedding model loaded successfully.")

    return _embedding_model


def get_embedding_model_name():
    """
    Return the name of the configured embedding model.
    """

    return EMBEDDING_MODEL


def reset_embedding_model():
    """
    Reset the cached embedding model.

    Useful when changing EMBEDDING_MODEL during
    experiments without restarting the application.
    """

    global _embedding_model

    _embedding_model = None

    print("✓ Cached embedding model has been reset.")
