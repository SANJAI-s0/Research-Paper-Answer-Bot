# Deployment Guide

# Research Paper Answer Bot

**Version:** 1.0.0

---

# Table of Contents

1. Introduction
2. Deployment Requirements
3. Local Deployment
4. Environment Configuration
5. Building the Vector Database
6. Running the Application
7. Deploying on Streamlit Community Cloud
8. Deploying on Render (Optional)
9. Deploying with Docker (Future)
10. Updating the Application
11. Troubleshooting
12. Conclusion

---

# 1. Introduction

This document explains how to deploy the **Research Paper Answer Bot** locally and on cloud platforms.

The application is built using:

- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Google Gemini API

Deployment requires only Python, the required packages, and a valid Gemini API key.

---

# 2. Deployment Requirements

## Operating System

- Windows 10 / 11
- Ubuntu 20.04+
- macOS

---

## Software

- Python 3.11 or later
- Git
- Visual Studio Code (recommended)

---

## Required Accounts

For cloud deployment:

- GitHub
- Streamlit Community Cloud
- Google AI Studio (Gemini API)

---

# 3. Local Deployment

## Step 1

Clone the repository.

```bash
git clone <repository-url>
```

---

## Step 2

Open the project folder.

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

Activate the virtual environment.

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

Install all dependencies.

```bash
pip install -r requirements.txt
```

---

# 4. Environment Configuration

Create a `.env` file in the project root.

Example:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
MODEL_NAME=gemini-2.5-flash
```

Replace:

```
YOUR_GOOGLE_GEMINI_API_KEY
```

with your own API key.

---

# 5. Building the Vector Database

Before starting the application, build the ChromaDB database.

```bash
python build_vector_db.py
```

This process:

- Loads research papers
- Extracts text
- Splits documents into chunks
- Creates embeddings
- Stores vectors in ChromaDB

This step only needs to be repeated after adding or modifying research papers.

---

# 6. Running the Application

Start the Streamlit application.

```bash
streamlit run streamlit_app.py
```

Open your browser and navigate to:

```
http://localhost:8501
```

The application is now ready to use.

---

# 7. Deploying on Streamlit Community Cloud

Streamlit Community Cloud provides a free and simple deployment platform for Streamlit applications.

---

## Step 1

Push the complete project to GitHub.

Example:

```
Research-Paper-Answer-Bot/
```

Ensure the repository includes:

- streamlit_app.py
- requirements.txt
- app/
- data/raw_papers/
- docs/
- .env.example

Do **not** upload:

- .env
- data/chroma_db/
- __pycache__/
- *.pyc

---

## Step 2

Sign in to:

https://share.streamlit.io/

using your GitHub account.

---

## Step 3

Click

```
New App
```

---

## Step 4

Select:

Repository

```
Research-Paper-Answer-Bot
```

Branch

```
main
```

Main file

```
streamlit_app.py
```

---

## Step 5

Add your secrets.

Open

```
Settings
```

↓

```
Secrets
```

Add:

```toml
GOOGLE_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
MODEL_NAME="gemini-2.5-flash"
```

---

## Step 6

Deploy the application.

The deployment may take a few minutes during the first build.

---

## Step 7

Once deployment is complete, Streamlit will provide a public application URL.

Example:

```
https://research-paper-answer-bot.streamlit.app
```

---

# 8. Deploying on Render (Optional)

Render can also host the application.

General steps:

1. Connect GitHub repository.
2. Create a new Web Service.
3. Install dependencies using:

```bash
pip install -r requirements.txt
```

4. Configure environment variables.
5. Start the application using:

```bash
streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
```

---

# 9. Docker Deployment (Future Enhancement)

A future version may include Docker support.

Example commands:

Build:

```bash
docker build -t research-paper-answer-bot .
```

Run:

```bash
docker run -p 8501:8501 research-paper-answer-bot
```

---

# 10. Updating the Application

Whenever research papers are added:

1. Place PDFs inside:

```
data/raw_papers/
```

2. Rebuild the vector database.

```bash
python build_vector_db.py
```

3. Restart the Streamlit application.

---

# 11. Troubleshooting

## ModuleNotFoundError

Install dependencies again.

```bash
pip install -r requirements.txt
```

---

## Missing API Key

Verify the `.env` file exists and contains a valid Google Gemini API key.

---

## Chroma Database Missing

Run:

```bash
python build_vector_db.py
```

---

## Streamlit Does Not Start

Ensure the virtual environment is activated.

---

## Port Already in Use

Specify another port.

```bash
streamlit run streamlit_app.py --server.port 8502
```

---

## Slow First Response

The embedding model and vector database are loaded into memory during the first query.

Subsequent responses are faster.

---

## API Quota Exceeded

Wait for your quota to reset or use another valid API key.

---

# 12. Deployment Checklist

Before deployment, verify the following:

- Python is installed.
- Virtual environment is activated.
- All dependencies are installed.
- `.env` file is configured.
- Research papers are available.
- Vector database has been built.
- Application runs locally.
- Repository is pushed to GitHub.
- Secrets are configured for cloud deployment.

---

# 13. Conclusion

The Research Paper Answer Bot can be deployed locally for development or on Streamlit Community Cloud for public access.

The deployment process is straightforward and requires only a valid Gemini API key, Python environment, and the indexed research paper dataset.

Following the steps in this guide ensures a successful deployment and a reproducible setup across different environments.

---

# End of Deployment Guide
