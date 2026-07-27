<div align="center">

# 📚 Research Paper Answer Bot

### AI-Powered Research Paper Question Answering using Retrieval-Augmented Generation (RAG)

An intelligent question-answering system that retrieves relevant information from research papers using **LangChain**, **ChromaDB**, **HuggingFace Embeddings**, and **Google Gemini**, delivered through an interactive **Streamlit** interface.

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge) ![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-6A1B9A?style=for-the-badge) ![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white) ![License](https://img.shields.io/github/license/<username>/Research-Paper-Answer-Bot?style=for-the-badge) ![Stars](https://img.shields.io/github/stars/<username>/Research-Paper-Answer-Bot?style=for-the-badge) ![Forks](https://img.shields.io/github/forks/<username>/Research-Paper-Answer-Bot?style=for-the-badge) ![Issues](https://img.shields.io/github/issues/<username>/Research-Paper-Answer-Bot?style=for-the-badge)

</div>

<div align="center">

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-success?style=for-the-badge)](YOUR_STREAMLIT_URL) [![Documentation](https://img.shields.io/badge/📖_Documentation-Available-blue?style=for-the-badge)](docs/user_manual.md) [![Evaluation](https://img.shields.io/badge/📊_Evaluation-Report-orange?style=for-the-badge)](docs/evaluation.md)

</div>

---

# 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Workflow](#-workflow)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Environment Configuration](#-environment-configuration)
- [Building the Vector Database](#-building-the-vector-database)
- [Running the Application](#-running-the-application)
- [Example Questions](#-example-questions)
- [Evaluation](#-evaluation)
- [Testing](#-testing)
- [Screenshots](#-screenshots)
- [Documentation](#-documentation)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)
- [Support](#-support)

---

## 📖 Overview

Large Language Models (LLMs) are powerful but may produce hallucinated or outdated answers when responding from their internal knowledge alone.

This project addresses that limitation by implementing a **Retrieval-Augmented Generation (RAG)** pipeline. Instead of relying only on the language model, the system first retrieves the most relevant passages from a collection of indexed research papers and then generates answers based solely on those retrieved documents.

The application is designed for researchers, students, developers, and AI enthusiasts who want reliable answers supported by research paper evidence.

---

# ✨ Features

- 📄 PDF Research Paper Loader
- ✂️ Intelligent Document Chunking
- 🔍 Semantic Search using ChromaDB
- 🤖 Google Gemini Integration
- 🧠 HuggingFace BGE Embeddings
- 📚 Retrieval-Augmented Generation (RAG)
- 🎯 Similarity & MMR Retrieval
- ✅ Confidence-based Answer Validation
- 📑 Supporting Evidence Viewer
- 📖 Referenced Research Papers
- 📊 Retrieval Statistics (Debug Mode)
- ⚡ Streamlit Interactive Interface
- 🧩 Modular Architecture
- 🔄 Easily Extendable Knowledge Base

---

# 🚀 Technologies Used

### Programming Language

- Python 3.11+

### Frameworks & Libraries

- Streamlit
- LangChain
- ChromaDB
- HuggingFace Transformers
- Sentence Transformers
- PyPDF
- Python Dotenv

### AI Models

- Google Gemini
- BAAI BGE Embedding Model

### Vector Database

- ChromaDB

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Research-Paper-Answer-Bot.git
```

---

## 2. Navigate to the Project

```bash
cd Research-Paper-Answer-Bot
```

---

## 3. Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Linux/macOS

```bash
python3 -m venv .venv
```

---

## 4. Activate the Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file in the project root.

Example:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
MODEL_NAME=gemini-2.5-flash
```

---

# 🗂️ Build the Vector Database

Before running the application, index the research papers.

```bash
python build_vector_db.py
```

This process:

- Loads PDF research papers
- Splits documents into chunks
- Creates embeddings
- Stores vectors in ChromaDB

---

# ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

Open:

```
http://localhost:8501
```

---

# 💬 Example Questions

You can ask questions such as:

```
What is Retrieval-Augmented Generation?

Explain Chain-of-Thought Prompting.

What is Self-RAG?

Compare GPT-3 and BERT.

Explain the ReAct framework.

What are the advantages of Instruction Tuning?

Explain the LLaMA 2 architecture.
```

---

# 🧠 How It Works

The application follows a Retrieval-Augmented Generation workflow.

1. User enters a question.
2. The question is converted into an embedding.
3. ChromaDB retrieves the most relevant document chunks.
4. Confidence filtering validates retrieval quality.
5. Retrieved passages are sent to Google Gemini.
6. Gemini generates a grounded response.
7. Supporting evidence and source papers are displayed.

---

# 📊 Evaluation

The project includes utilities for evaluating retrieval quality and answer generation.

Run:

```bash
python evaluate_rag.py
```

The evaluation process examines:

- Retrieval quality
- Context relevance
- Grounded answer generation
- Confidence filtering
- Retrieval consistency

---

# 🧪 Testing

Individual modules can be tested using the scripts available in the `tests` directory.

Example:

```bash
python tests/test_loader.py
```

```bash
python tests/test_chunking.py
```

```bash
python tests/test_retriever.py
```

```bash
python tests/test_rag.py
```

---

## 📈 Project Status

| Status | Version | Release |
|----------|----------|----------|
| ✅ Stable | v1.0.0 | Initial Release |

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini |
| Framework | LangChain |
| Embedding Model | HuggingFace BGE |
| Vector Database | ChromaDB |
| PDF Processing | PyPDF |
| Environment | Python Virtual Environment |

---

# 🏗️ System Architecture

<p align="center">
<img src="docs/screenshots/architecture.png" width="900">
</p>

---

# 🔄 Workflow

<p align="center">
<img src="docs/screenshots/Workflow.png" width="900">
</p>

---

# 📷 Screenshots

Application screenshots are available in the `docs/screenshots/` directory.

Included screenshots:

- System Architecture
- RAG Workflow

---

# 📚 Documentation

Additional documentation is available inside the `docs/` directory.

- User Manual
- Deployment Guide
- Evaluation Report

The project structure is documented separately in `structure.md`.

---

# ⚠️ Limitations

Current limitations include:

- Answers are limited to indexed research papers.
- Internet search is not supported.
- Performance depends on embedding quality and retrieval accuracy.
- Images and figures inside PDFs are not interpreted.

---

# 🚀 Future Enhancements

Planned improvements include:

- Hybrid Search (BM25 + Vector Search)
- Conversation Memory
- PDF Upload via UI
- Citation Highlighting
- REST API
- Docker Support
- Authentication
- Cloud Deployment Templates
- Multi-document Comparison

---

# 🤝 Contributing

Contributions are welcome.

Please read:

- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`

before submitting issues or pull requests.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# 🚀 Roadmap

- [x] PDF Loader
- [x] Text Chunking
- [x] ChromaDB Integration
- [x] Semantic Search
- [x] Google Gemini Integration
- [x] Streamlit Interface
- [x] Confidence Filtering
- [x] Supporting Evidence Viewer
- [ ] Conversation Memory
- [ ] Hybrid Search (BM25 + Vector)
- [ ] PDF Upload
- [ ] REST API
- [ ] Docker Deployment
- [ ] Authentication

---

## 📊 Repository Information

| Item | Details |
|------|---------|
| Project | Research Paper Answer Bot |
| Version | 1.0.0 |
| Language | Python |
| Architecture | Retrieval-Augmented Generation (RAG) |
| License | MIT |
| UI | Streamlit |
| Status | Stable |

---

# 🙏 Acknowledgements

This project makes use of several excellent open-source tools and technologies.

- Google Gemini
- LangChain
- ChromaDB
- HuggingFace
- Streamlit
- PyPDF

Special thanks to the open-source community for providing the tools and resources that made this project possible.

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Report issues
- 💡 Suggest new features

Your feedback and contributions are greatly appreciated.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

Made with ❤️ using Python, LangChain, ChromaDB, Google Gemini, and Streamlit.

</div>
