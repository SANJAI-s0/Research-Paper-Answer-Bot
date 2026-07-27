# User Manual

# Research Paper Answer Bot

**Version:** 1.0.0

---

# Table of Contents

1. Introduction
2. System Requirements
3. Installation
4. Configuration
5. Running the Application
6. User Interface Overview
7. Using the Application
8. Example Questions
9. Understanding the Results
10. Troubleshooting
11. Frequently Asked Questions (FAQ)
12. Limitations
13. Future Enhancements
14. Contact

---

# 1. Introduction

The **Research Paper Answer Bot** is an AI-powered question-answering system that uses **Retrieval-Augmented Generation (RAG)** to answer questions from a collection of indexed research papers.

Instead of relying solely on a language model, the application first retrieves relevant information from research papers stored in a vector database and then generates an answer grounded in those retrieved passages.

This helps improve answer accuracy and reduces hallucinations.

---

# 2. System Requirements

## Operating System

- Windows 10/11
- Ubuntu 20.04+
- macOS 12+

---

## Python

Python 3.11 or later is recommended.

---

## Internet Connection

An active internet connection is required because the application uses the Google Gemini API.

---

## Required Software

- Python
- Git (optional)
- Visual Studio Code (recommended)

---

# 3. Installation

## Step 1

Clone the repository.

```bash
git clone <repository-url>
```

---

## Step 2

Navigate to the project folder.

```bash
cd Research-Paper-Answer-Bot
```

---

## Step 3

Create a virtual environment.

Windows

```bash
python -m venv venv
```

Linux/macOS

```bash
python3 -m venv venv
```

---

## Step 4

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

## Step 5

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 4. Configuration

Create a `.env` file.

Example:

```env
GOOGLE_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.5-flash
```

Replace `YOUR_API_KEY` with your Google Gemini API key.

---

# 5. Build the Vector Database

Before running the application, create the vector database.

```bash
python build_vector_db.py
```

This process:

- Loads all research papers
- Splits documents into chunks
- Creates embeddings
- Stores vectors in ChromaDB

This only needs to be performed once unless new research papers are added.

---

# 6. Running the Application

Start the Streamlit application.

```bash
streamlit run streamlit_app.py
```

After the server starts, open:

```
http://localhost:8501
```

The application homepage will appear.

---

# 7. User Interface Overview

The application contains the following sections.

---

## Sidebar

The sidebar displays:

- Project information
- Knowledge base statistics
- Example questions
- Debug option
- Clear Chat button

---

## Chat Window

The main interface allows users to:

- Ask research-related questions
- View generated answers
- View supporting evidence
- View referenced papers

---

## Retrieved Supporting Evidence

Displays the document passages used to generate the answer.

Each passage contains:

- Paper name
- Page number
- Relevance score
- Retrieved content

---

## Sources

Displays the research papers used to answer the question.

---

# 8. Using the Application

## Step 1

Launch the application.

---

## Step 2

Type a question into the chat box.

Example:

```
What is Retrieval-Augmented Generation?
```

---

## Step 3

Press Enter.

The system will:

1. Search the research papers.
2. Retrieve relevant passages.
3. Generate an answer.
4. Display supporting evidence.

---

# 9. Example Questions

The following questions can be asked.

```
What is Retrieval-Augmented Generation?

Explain Chain-of-Thought Prompting.

Compare RAG and Self-RAG.

Explain the BERT architecture.

What is ReAct?

What are the advantages of Instruction Tuning?

Explain LLaMA 2.
```

---

# 10. Understanding the Results

The generated response consists of multiple sections.

---

## Answer

A concise explanation generated from the retrieved research papers.

---

## Supporting Evidence

Displays the retrieved passages used during answer generation.

---

## Sources

Lists the research papers that contributed to the answer.

---

## Retrieval Statistics (Debug Mode)

When enabled, the application displays:

- Retrieved Chunks
- Papers Used
- Top Retrieval Score
- Average Retrieval Score
- Retrieval Strategy

These statistics help evaluate retrieval quality.

---

# 11. Confidence Filtering

The system evaluates retrieval confidence before generating an answer.

If sufficient evidence exists:

- An answer is generated.
- Supporting evidence is shown.

If confidence is too low:

The system returns:

> "I couldn't find sufficient evidence in the indexed research papers to answer this question confidently."

No supporting evidence is displayed.

---

# 12. Troubleshooting

## Application does not start

Ensure all required packages are installed.

```bash
pip install -r requirements.txt
```

---

## Missing API Key

Verify that the `.env` file contains a valid Google Gemini API key.

---

## Vector Database Missing

Run:

```bash
python build_vector_db.py
```

---

## Slow Responses

The first query may take longer because the embedding model and vector database are loaded into memory.

Subsequent queries are significantly faster.

---

## Gemini API Quota Exceeded

Wait until your quota resets or use another valid API key.

---

# 13. Frequently Asked Questions (FAQ)

## Can I add more research papers?

Yes.

Place the PDF files inside:

```
data/raw_papers/
```

Then rebuild the vector database.

```bash
python build_vector_db.py
```

---

## Can I change the embedding model?

Yes.

Modify the embedding model configuration in:

```
app/config.py
```

Rebuild the vector database afterward.

---

## Can I change the language model?

Yes.

Update the model name in the configuration file.

---

## Does the chatbot use internet search?

No.

It answers only from the indexed research papers stored in the vector database.

---

# 14. Limitations

Current limitations include:

- Answers are limited to the indexed research papers.
- Internet search is not supported.
- Image-based PDF understanding is not available.
- Tables and figures are processed as extracted text.
- Performance depends on retrieval quality.

---

# 15. Future Enhancements

Planned improvements include:

- PDF upload through the web interface
- Hybrid search
- Citation highlighting
- Conversation memory
- Multi-document comparison
- REST API
- Docker deployment
- Authentication
- Cloud deployment

---

# 16. Contact

Project Name:

**Research Paper Answer Bot**

Version:

**1.0.0**

For bug reports, feature requests, or improvements, please create an issue in the project repository.

---

# End of User Manual
