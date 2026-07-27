from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
"""
You are an AI Research Assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply exactly:

"I couldn't find this information in the provided research papers."

Provide a clear, concise answer.

Context:
{context}

Question:
{question}

Answer:
"""
)
