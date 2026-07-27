import os
from pathlib import Path

from dotenv import load_dotenv

# ====================================================
# Load Environment Variables
# ====================================================

load_dotenv()

# ====================================================
# Project Paths
# ====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw_papers"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CHROMA_DB_DIR = DATA_DIR / "chroma_db"

# Create required directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
RAW_DATA_DIR.mkdir(exist_ok=True)
PROCESSED_DATA_DIR.mkdir(exist_ok=True)
CHROMA_DB_DIR.mkdir(exist_ok=True)

# ====================================================
# API Keys
# ====================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-flash-latest")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found.\n"
        "Please add it to your .env file."
    )

# ====================================================
# Gemini Configuration
# ====================================================

TEMPERATURE = 0.2

MAX_OUTPUT_TOKENS = 1024

MAX_RETRIES = 3

INITIAL_RETRY_DELAY = 1

# ====================================================
# Embedding Model Configuration
# ====================================================

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

AVAILABLE_EMBEDDING_MODELS = {
    "bge_small": "BAAI/bge-small-en-v1.5",
    "bge_m3": "BAAI/bge-m3",
}

# ====================================================
# Text Chunking
# ====================================================

CHUNK_SIZE = 600

CHUNK_OVERLAP = 75

# ====================================================
# Retrieval Configuration
# ====================================================

TOP_K = 5

FINAL_TOP_K = 3

FETCH_K = 10

MMR_LAMBDA = 0.85

# Retrieval Confidence Threshold
MIN_RELEVANCE_SCORE = 0.60

# ====================================================
# Retrieval Strategy
# ====================================================

SIMILARITY = "similarity"

MMR = "mmr"

RETRIEVAL_STRATEGY = MMR

# ====================================================
# Evaluation Queries
# ====================================================

EVALUATION_QUERIES = [
    "What is Retrieval-Augmented Generation?",
    "Explain Chain-of-Thought Prompting.",
    "Compare RAG and Self-RAG.",
    "Explain the BERT architecture.",
    "What is ReAct?",
]

# ====================================================
# Application Metadata
# ====================================================

APP_NAME = "Research Paper Answer Bot"

APP_VERSION = "1.0.0"

AUTHOR = "Sanjai S"

# ====================================================
# Utility
# ====================================================

def print_config():
    """Print the current application configuration."""

    print("=" * 60)
    print(APP_NAME)
    print("=" * 60)
    print(f"Version              : {APP_VERSION}")
    print(f"Gemini Model         : {MODEL_NAME}")
    print(f"Embedding Model      : {EMBEDDING_MODEL}")
    print(f"Chunk Size           : {CHUNK_SIZE}")
    print(f"Chunk Overlap        : {CHUNK_OVERLAP}")
    print(f"Retrieval Strategy   : {RETRIEVAL_STRATEGY}")
    print(f"TOP_K                : {TOP_K}")
    print(f"FINAL_TOP_K          : {FINAL_TOP_K}")
    print(f"FETCH_K              : {FETCH_K}")
    print(f"MMR Lambda           : {MMR_LAMBDA}")
    print("=" * 60)
