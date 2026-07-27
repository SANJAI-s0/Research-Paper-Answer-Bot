# Changelog

All notable changes to this project are documented in this file.

The format is based on **Keep a Changelog** (https://keepachangelog.com/en/1.1.0/)
and this project follows **Semantic Versioning** (https://semver.org/).

---

# [1.0.0] - 2026-07-27

## Initial Release

This is the first stable release of the **Research Paper Answer Bot**.

### Added

- Retrieval-Augmented Generation (RAG) architecture
- Streamlit-based interactive web application
- PDF document loading and preprocessing
- Automatic text chunking for research papers
- ChromaDB vector database integration
- HuggingFace BGE embedding model support
- Google Gemini integration for answer generation
- Similarity-based document retrieval
- Max Marginal Relevance (MMR) retrieval
- Configurable retrieval strategy
- Retrieval confidence threshold
- Confidence-based answer validation
- Supporting evidence viewer
- Source paper grouping
- Response time display
- Debug retrieval statistics
- Research paper evaluation utilities
- Embedding comparison utility
- Vector database builder
- Environment variable configuration
- Example configuration file
- Modular project architecture
- Testing utilities for loader, chunking, retriever, and RAG pipeline

### Improved

- Cleaner retrieval pipeline
- Improved supporting evidence display
- Better duplicate chunk removal
- Enhanced preview text cleaning
- Improved PDF artifact removal
- More informative retrieval statistics
- Better prompt design for grounded answers
- Improved fallback handling for out-of-domain questions
- Better Gemini retry mechanism
- Cleaner Streamlit interface
- Organized project structure
- Improved code modularity
- Improved maintainability and readability

### Fixed

- Removed duplicate retrieved passages
- Prevented low-confidence evidence from being displayed
- Reduced hallucinations through confidence filtering
- Fixed PDF preview formatting artifacts
- Improved Unicode text cleanup
- Improved source grouping
- Improved retrieval consistency
- Better handling of temporary Gemini API failures
- Better exception handling for API quota and timeout issues

---

# Future Roadmap

The following features are planned for future releases.

## Planned

- Conversation memory
- Citation highlighting inside answers
- Hybrid search (BM25 + Vector Search)
- Multi-document comparison
- PDF upload through the web interface
- Support for additional embedding models
- Export answers as PDF
- User authentication
- Usage analytics dashboard
- Docker support
- REST API
- Cloud deployment templates
- Continuous Integration (CI)
- Automated evaluation reports
- Performance benchmarking dashboard

---

## Version History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Stable | Initial public release of the Research Paper Answer Bot |

---

## Notes

Version **1.0.0** represents the first stable release of the project, featuring a complete Retrieval-Augmented Generation pipeline, configurable retrieval strategies, confidence-aware answer generation, supporting evidence visualization, and a modular architecture designed for future enhancements.
