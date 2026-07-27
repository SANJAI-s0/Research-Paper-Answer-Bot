# Overall Project Structure

```tree
Research-Paper-Answer-Bot/
│
├── .git/                                 # Git version control metadata (auto-generated)
├── .github/                              # GitHub workflows, issue templates, and CI (optional)
│
├── app/                                  # Core application source code
│   ├── __init__.py                       # Marks 'app' as a Python package
│   ├── chunking.py                       # Splits research papers into semantic chunks
│   ├── config.py                         # Stores project configuration, constants, and API settings
│   ├── embeddings.py                     # Loads and manages HuggingFace embedding models
│   ├── evaluation.py                     # Evaluation helper functions for retrieval and answers
│   ├── llm.py                            # Handles Gemini API communication and answer generation
│   ├── loader.py                         # Loads PDF files and extracts document text
│   ├── prompt.py                         # Stores prompt templates for the language model
│   ├── rag_chain.py                      # Implements the complete Retrieval-Augmented Generation pipeline
│   ├── retriever.py                      # Retrieves relevant document chunks from ChromaDB
│   ├── utils.py                          # Common helper and utility functions
│   ├── vector_store.py                   # Creates and manages the Chroma vector database
│   └── __pycache__/                      # Python bytecode cache (ignored by Git)
│
├── data/                                 # Project datasets and vector database
│   ├── raw_papers/                       # Original research paper PDF files
│   ├── processed/                        # Processed intermediate files (optional)
│   └── chroma_db/                        # Persistent ChromaDB vector database (excluded from Git)
│
├── docs/                                 # Project documentation
│   ├── screenshots/                      # Application screenshots for README and report
│   ├── Flow/architecture.png             # High-level system architecture diagram
│   ├── Flow/workflow.png                 # RAG workflow diagram
│   ├── Flow/architecture_workflow.svg    # High-Level Overall Architecture and Work Flow Diagram
│   ├── deployment.md                     # Deployment guide
│   ├── evaluation.md                     # Evaluation methodology and results
│   └── user_manual.md                    # End-user guide
│
├── experiments/                          # Experimental results and benchmarking
│   ├── experiment_log.csv                # Experiment logs
│   ├── embedding_comparison.csv          # Embedding model comparison results (recommended)
│   └── evaluation_results.csv            # Final evaluation metrics (recommended)
│
├── notebooks/                            # Development notebooks
│   └── Research_Paper_Answer_Bot.ipynb   # Research, experiments, and prototype notebook
│
├── tests/                                # Testing scripts
│   ├── test_loader.py                    # Tests PDF loading
│   ├── test_chunking.py                  # Tests text chunking
│   ├── test_retriever.py                 # Tests retrieval quality
│   ├── test_rag.py                       # End-to-end RAG pipeline tests
│   ├── list_models.py                    # Lists available embedding and LLM models
│   └── quota_checking.py                 # Checks Gemini API quota
│
├── .streamlit/                           # Streamlit configuration
│   └── config.toml                       # Streamlit theme and server configuration
│
├── .env                                 # Environment variables (never commit)
├── .env.example                         # Example environment variable template
├── .gitignore                           # Files and folders ignored by Git
├── LICENSE                              # Open-source license (MIT recommended)
├── CHANGELOG.md                         # Project version history
├── CONTRIBUTING.md                      # Contribution guidelines
├── CODE_OF_CONDUCT.md                   # Community code of conduct (optional)
├── README.md                            # Project overview and setup guide
├── structure.md                         # Explains the project folder structure
├── requirements.txt                     # Python dependencies
├── build_vector_db.py                   # Builds ChromaDB from PDF documents
├── compare_embeddings.py                # Compares embedding model performance
├── evaluate_rag.py                      # Evaluates the complete RAG system
├── streamlit_app.py                     # Main Streamlit application
└── run.py                               # Optional launcher script for the application
```