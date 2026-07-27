import time
import streamlit as st

from app.rag_chain import ask

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Research Paper Answer Bot",
    page_icon="📚",
    layout="wide",
)

# ----------------------------------------------------
# UI Helper Functions
# ----------------------------------------------------

def render_retrieved_passages(passages):
    """
    Display supporting evidence.
    """

    if not passages:
        return

    st.subheader("📑 Retrieved Supporting Evidence")

    st.caption(
        "Top retrieved passages used to generate the answer."
    )

    for passage in passages:

        title = (
            f"📄 {passage['paper']} "
            f"(Page {passage['page']})"
        )

        with st.expander(title):

            score = passage.get("score")

            if score is not None:

                st.caption(
                    f"Relevance Score: {score:.3f}"
                )

            st.write(
                passage["content"]
            )


def render_sources(sources):
    """
    Display grouped source papers.
    """

    if not sources:
        return

    st.subheader("📚 Sources")

    for paper, pages in sources.items():

        with st.expander(
            f"📄 {paper}"
        ):

            st.write(
                f"📄 Pages: {', '.join(map(str, pages))}"
            )


def render_stats(stats):
    """
    Display retrieval statistics.

    Visible only when Debug Mode is enabled.
    """

    if not st.session_state.get(
        "debug_mode",
        False,
    ):
        return

    st.subheader("📊 Retrieval Statistics")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Chunks",
        stats.get(
            "retrieved_chunks",
            0,
        ),
    )

    col2.metric(
        "Papers",
        stats.get(
            "papers_used",
            0,
        ),
    )

    col3.metric(
        "Top Score",
        f"{stats.get('top_score',0):.3f}",
    )

    col4.metric(
        "Avg Score",
        f"{stats.get('avg_score',0):.3f}",
    )

    col5.metric(
        "Mode",
        stats.get(
            "retrieval_mode",
            "-",
        ),
    )

    query = stats.get("query")

    if query:

        st.caption(
            f"Query: {query}"
        )


def render_response_time(elapsed):

    st.caption(
        f"⏱️ Response Time: {elapsed:.2f} seconds"
    )


def render_assistant_response(message):

    st.markdown(
        message["content"]
    )

    stats = message.get(
        "stats",
        {},
    )

    confidence = stats.get(
        "confidence_passed",
        True,
    )

    if confidence:

        render_retrieved_passages(
            message.get(
                "retrieved_passages",
                [],
            )
        )

        render_sources(
            message.get(
                "sources",
                {},
            )
        )

    else:

        st.info(
            "No sufficiently relevant supporting evidence was found."
        )

    render_stats(stats)

    if "time" in message:

        render_response_time(
            message["time"]
        )


# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "debug_mode" not in st.session_state:
    st.session_state.debug_mode = False

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.title(
        "📚 Research Paper Answer Bot"
    )

    st.markdown("---")

    st.markdown(
        """
### 📖 About

This chatbot answers questions using **Retrieval-Augmented Generation (RAG)** over an indexed collection of research papers.

### 📚 Knowledge Base

- Research Papers: **10**
- Total Pages: **403**
- Chunks: **1992**

### ⚙️ Tech Stack

- Google Gemini
- LangChain
- ChromaDB
- BGE Embeddings
- Streamlit
"""
    )

    st.markdown("---")

    st.markdown(
        "### 💡 Example Questions"
    )

    st.markdown(
        """
- What is Retrieval-Augmented Generation?
- Explain ReAct.
- Compare RAG and Self-RAG.
- Explain BERT.
- What is Chain-of-Thought Prompting?
"""
    )

    st.markdown("---")

    st.session_state.debug_mode = st.checkbox(
        "Show Retrieval Statistics",
        value=False,
    )

    st.markdown("---")

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True,
    ):

        st.session_state.messages = []

        st.rerun()

# ----------------------------------------------------
# Main Page
# ----------------------------------------------------

st.title(
    "📚 Research Paper Answer Bot"
)

st.caption(
    "Ask questions about your indexed research papers."
)

# ----------------------------------------------------
# Chat History
# ----------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        if message["role"] == "assistant":

            render_assistant_response(
                message
            )

        else:

            st.markdown(
                message["content"]
            )

# ----------------------------------------------------
# Chat Input
# ----------------------------------------------------

prompt = st.chat_input(
    "Ask anything about your research papers..."
)

if prompt:

    with st.chat_message("user"):

        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Searching research papers..."
        ):

            start = time.time()

            try:

                result = ask(prompt)

                elapsed = (
                    time.time() - start
                )

                assistant_message = {
                    "role": "assistant",
                    "content": result.get(
                        "answer",
                        "",
                    ),
                    "sources": result.get(
                        "sources",
                        {},
                    ),
                    "retrieved_passages": result.get(
                        "retrieved_passages",
                        [],
                    ),
                    "stats": result.get(
                        "stats",
                        {},
                    ),
                    "time": elapsed,
                }

                render_assistant_response(
                    assistant_message
                )

                st.session_state.messages.append(
                    assistant_message
                )

            except Exception as e:

                error = str(e)

                if (
                    "503" in error
                    or "UNAVAILABLE" in error
                ):

                    st.warning(
                        "⚠️ Gemini is temporarily unavailable. Please try again in a few moments."
                    )

                elif (
                    "429" in error
                    or "RESOURCE_EXHAUSTED" in error
                ):

                    st.warning(
                        "⚠️ Gemini API quota has been reached. Please try again later."
                    )

                elif (
                    "Timeout" in error
                    or "Deadline" in error
                ):

                    st.warning(
                        "⚠️ The request timed out. Please try again."
                    )

                else:

                    st.error(
                        f"❌ {error}"
                    )

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.markdown("---")

st.caption(
    "📚 Research Paper Answer Bot • Powered by Gemini • LangChain • ChromaDB • BGE Embeddings"
)
