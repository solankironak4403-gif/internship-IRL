import logging
import streamlit as st

from rag.pipeline import get_rag_pipeline, process_query, RAGResponse
from utils.config import get_config

# ------------------ CONFIG ------------------ #
st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖",
    layout="wide"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ------------------ CUSTOM CSS ------------------ #
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
.stTextArea textarea {
    border-radius: 10px;
}
.chat-user {
    background: #1e293b;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.chat-bot {
    background: #020617;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #38bdf8;
    margin-bottom: 15px;
}
.small-text {
    color: gray;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION ------------------ #
def init_session():
    if "config" not in st.session_state:
        st.session_state.config = get_config()

    if "pipeline" not in st.session_state:
        st.session_state.pipeline = get_rag_pipeline()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


# ------------------ SIDEBAR ------------------ #
def sidebar():
    with st.sidebar:
        st.title("⚙️ Settings")

        config = st.session_state.config

        st.markdown("### Model")
        st.info(config.model_id.split("/")[-1])

        st.markdown("### Retrieval")
        top_k = st.slider("Top K", 1, 10, config.top_k)

        st.markdown("### Generation")
        temp = st.slider("Temperature", 0.0, 1.0, config.temperature)

        st.divider()

        if st.button("🧹 Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

        st.markdown("---")
        st.caption("🚀 Powered by Amazon Bedrock")


# ------------------ CHAT UI ------------------ #
def chat_ui():
    st.title("🤖 Enterprise AI Assistant")
    st.caption("Ask anything about your company knowledge base")

    # Display chat history
    for chat in st.session_state.chat_history:
        st.markdown(f"<div class='chat-user'>🧑 {chat['question']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-bot'>🤖 {chat['answer']}</div>", unsafe_allow_html=True)

    # Input box
    user_query = st.chat_input("Ask your question...")

    if user_query:
        # Show user message instantly
        st.session_state.chat_history.append({
            "question": user_query,
            "answer": "⏳ Thinking..."
        })

        with st.spinner("Processing..."):
            try:
                response = process_query(
                    query=user_query,
                    top_k=st.session_state.config.top_k
                )

                # Replace last answer
                st.session_state.chat_history[-1]["answer"] = response.answer

                # Show response
                st.rerun()

            except Exception as e:
                st.session_state.chat_history[-1]["answer"] = f"❌ Error: {str(e)}"
                logger.error(e)
                st.rerun()


# ------------------ CITATIONS ------------------ #
def show_details():
    if not st.session_state.chat_history:
        return

    last = st.session_state.chat_history[-1]

    if "response" in last:
        response = last["response"]

        with st.expander("📚 Citations"):
            for c in response.citations:
                st.markdown(f"**[{c['index']}] {c.get('title', '')}**")

        with st.expander("📄 Source Docs"):
            for doc in response.source_documents[:3]:
                st.code(doc.content[:300])


# ------------------ MAIN ------------------ #
def main():
    init_session()
    sidebar()
    chat_ui()

    st.divider()
    st.caption("Enterprise Knowledge Base System © 2026")


if __name__ == "__main__":
    main()