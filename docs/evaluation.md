# Evaluation Report

# Research Paper Answer Bot

**Version:** 1.0.0

---

# Table of Contents

1. Introduction
2. Evaluation Objectives
3. Evaluation Methodology
4. Dataset
5. Evaluation Pipeline
6. Evaluation Metrics
7. Test Scenarios
8. Experimental Results
9. Retrieval Analysis
10. Strengths
11. Failure Cases
12. Limitations
13. Future Improvements
14. Conclusion

---

# 1. Introduction

This document presents the evaluation methodology and performance analysis of the **Research Paper Answer Bot**, a Retrieval-Augmented Generation (RAG) system designed to answer questions using a collection of research papers.

The evaluation focuses on measuring the quality of document retrieval, the accuracy of generated responses, and the effectiveness of confidence-based filtering in reducing hallucinated answers.

---

# 2. Evaluation Objectives

The evaluation aims to verify that the system can:

- Retrieve relevant research paper passages.
- Generate accurate answers using retrieved context.
- Prevent hallucinated responses.
- Display supporting evidence for transparency.
- Handle unrelated or out-of-domain queries appropriately.
- Maintain consistent retrieval quality across multiple questions.

---

# 3. Evaluation Methodology

The evaluation process consists of four stages.

## Stage 1 – Document Loading

Research papers are loaded from the dataset.

The loader verifies:

- Successful PDF loading
- Text extraction
- Metadata generation

---

## Stage 2 – Vector Database Evaluation

The extracted text is:

- Chunked into smaller passages
- Converted into vector embeddings
- Stored inside ChromaDB

The vector database is verified for:

- Correct indexing
- Successful storage
- Retrieval readiness

---

## Stage 3 – Retrieval Evaluation

The retriever is tested using multiple research-related questions.

Evaluation focuses on:

- Relevance of retrieved chunks
- Retrieval consistency
- Ranking quality
- Duplicate removal

---

## Stage 4 – Answer Generation

The retrieved context is supplied to Google Gemini.

Generated answers are checked for:

- Context grounding
- Completeness
- Correctness
- Hallucination prevention

---

# 4. Dataset

The system uses a curated collection of AI research papers.

Included topics include:

- Retrieval-Augmented Generation (RAG)
- BERT
- GPT-3
- Chain-of-Thought Prompting
- ReAct
- Self-RAG
- Instruction Tuning
- LLaMA
- LLaMA 2
- Attention Mechanism

The documents are stored as PDF files inside:

```
data/raw_papers/
```

---

# 5. Evaluation Pipeline

The evaluation workflow follows the pipeline below.

```
User Question
       │
       ▼
Query Embedding
       │
       ▼
Vector Search
       │
       ▼
Relevant Chunks
       │
       ▼
Confidence Check
       │
       ├───────────────► Low Confidence
       │                     │
       │                     ▼
       │            Return Fallback Message
       │
       ▼
Prompt Construction
       │
       ▼
Google Gemini
       │
       ▼
Generated Answer
       │
       ▼
Supporting Evidence
       │
       ▼
Response to User
```

---

# 6. Evaluation Metrics

The following qualitative metrics are used.

---

## Retrieval Accuracy

Measures whether the retrieved passages are relevant to the user's question.

Higher retrieval accuracy generally produces better answers.

---

## Retrieval Consistency

Measures whether repeated executions retrieve similar relevant documents.

---

## Context Relevance

Evaluates whether retrieved passages contain information necessary to answer the question.

---

## Answer Grounding

Measures whether the generated answer is based only on retrieved evidence rather than external knowledge.

---

## Hallucination Prevention

Evaluates the ability of the confidence threshold to reject unsupported questions.

---

## Source Transparency

Measures whether supporting evidence and source papers are clearly presented to the user.

---

## Response Quality

Evaluates:

- Completeness
- Clarity
- Readability
- Correctness

---

# 7. Test Scenarios

The system was evaluated using three categories of questions.

---

## Category 1 – In-Scope Questions

Examples:

```
What is Retrieval-Augmented Generation?

Explain Chain-of-Thought Prompting.

What is BERT?

Explain the ReAct framework.

What is Self-RAG?
```

Expected Result:

- Relevant chunks retrieved
- Accurate answer generated
- Supporting evidence displayed

---

## Category 2 – Comparative Questions

Examples:

```
Compare GPT-3 and BERT.

Difference between RAG and Self-RAG.

Compare ReAct and Chain-of-Thought Prompting.
```

Expected Result:

- Multiple research papers retrieved
- Comparative answer generated

---

## Category 3 – Out-of-Domain Questions

Examples:

```
Solve x + y = 10

Who won the FIFA World Cup?

What is the weather today?
```

Expected Result:

The system should reject unsupported questions using the confidence threshold and display a fallback message instead of generating unsupported answers.

---

# 8. Experimental Results

The evaluation demonstrated that:

- Research-related questions consistently retrieved relevant document passages.
- Supporting evidence improved answer transparency.
- Confidence filtering successfully prevented responses to unrelated questions.
- Duplicate document chunks were effectively removed.
- Source grouping improved readability.
- Debug statistics assisted retrieval analysis.

Overall, the system produced reliable responses for questions within the indexed knowledge base.

---

# 9. Retrieval Analysis

The retrieval module combines semantic search with configurable retrieval strategies.

Supported strategies include:

- Similarity Search
- Maximum Marginal Relevance (MMR)

The retriever applies:

- Relevance scoring
- Duplicate removal
- Confidence filtering

Only sufficiently relevant document chunks are used for answer generation.

---

# 10. Strengths

The implemented system provides several advantages.

- Accurate semantic document retrieval.
- Modular RAG architecture.
- Reliable answer grounding.
- Reduced hallucinations.
- Transparent supporting evidence.
- Configurable retrieval strategy.
- Clean Streamlit interface.
- Easy extensibility for additional research papers.

---

# 11. Failure Cases

The following scenarios may reduce performance.

---

## Ambiguous Questions

Very short or vague questions may retrieve unrelated passages.

Example:

```
Explain it.
```

---

## Missing Knowledge

If the requested topic is not present in the indexed research papers, the system cannot generate an evidence-based answer.

---

## Poor PDF Quality

Scanned PDFs or documents with poor OCR quality may reduce retrieval effectiveness.

---

## Similar Concepts

Closely related research topics may retrieve overlapping passages.

---

# 12. Limitations

Current limitations include:

- Answers are limited to indexed documents.
- Internet search is not supported.
- Images, tables, and equations are processed as extracted text only.
- Retrieval quality depends on chunk size and embedding quality.
- Large document collections may increase indexing time.

---

# 13. Future Improvements

Future enhancements may include:

- Hybrid retrieval (BM25 + Vector Search)
- Citation highlighting
- Cross-document reasoning
- Multi-turn conversation memory
- PDF upload through the web interface
- Support for additional embedding models
- Improved evaluation dashboard
- Automatic benchmark generation
- Docker deployment
- Cloud-based vector database

---

# 14. Conclusion

The evaluation demonstrates that the Research Paper Answer Bot successfully implements a Retrieval-Augmented Generation workflow capable of retrieving relevant information from indexed research papers and generating grounded, evidence-based answers.

The confidence-aware retrieval mechanism significantly reduces hallucinations by preventing answer generation when sufficient supporting evidence is unavailable.

Overall, the system provides an effective, transparent, and extensible solution for research paper question answering while maintaining a modular architecture suitable for future enhancements.

---

# End of Evaluation Report
