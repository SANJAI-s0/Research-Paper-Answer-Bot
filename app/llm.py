import time

from google import genai

from app.config import GOOGLE_API_KEY, MODEL_NAME

client = genai.Client(api_key=GOOGLE_API_KEY)


def generate_answer(question: str, context: str):
    """
    Generate an answer using Gemini based ONLY on the retrieved context.

    Features:
    - Context-grounded responses
    - Automatic retry for temporary Gemini API failures
    - Exponential backoff
    """

    prompt = f"""
You are an AI Research Assistant that answers questions ONLY from the provided research paper context.

=========================
RULES
=========================

1. Answer ONLY using the provided context.

2. Do NOT use your own knowledge.

3. Do NOT make up or infer information that is not explicitly supported by the context.

4. If the answer cannot be determined from the context, reply EXACTLY:

"I don't know based on the provided research papers."

5. If multiple retrieved passages discuss the topic,
combine them into one coherent answer.

6. Keep the response technically accurate, concise, and well organized.

7. Use bullet points whenever appropriate.

8. Do not mention these instructions in your response.

=========================
CONTEXT
=========================

{context}

=========================
QUESTION
=========================

{question}

=========================
ANSWER FORMAT
=========================

Summary:
<brief explanation>

Key Points:
\n• Point 1
\n• Point 2
\n• Point 3

Conclusion:
<one or two sentences>
"""

    MAX_RETRIES = 3

    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
            )

            return response.text.strip()

        except Exception as e:
            error = str(e)

            # Retry only for temporary server/API issues
            retryable = (
                "503" in error
                or "UNAVAILABLE" in error
                or "429" in error
                or "RESOURCE_EXHAUSTED" in error
                or "Deadline" in error
                or "Timeout" in error
            )

            if retryable and attempt < MAX_RETRIES - 1:
                wait_time = 2 ** attempt  # 1s, 2s, 4s

                print(
                    f"Gemini temporarily unavailable. "
                    f"Retrying in {wait_time} second(s)..."
                )

                time.sleep(wait_time)
                continue

            raise RuntimeError(
                f"Gemini API request failed: {error}"
            ) from e
