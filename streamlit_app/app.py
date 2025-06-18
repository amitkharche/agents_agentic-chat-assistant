"""
Streamlit frontend for Agentic AI Chat Assistant using LangChain
"""

import os
import sys
import streamlit as st
from dotenv import load_dotenv

# 🧩 Set up imports from src if needed
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

# ✅ Load OpenAI key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ If not found, ask user to enter it
if not api_key:
    st.warning("🔐 Please enter your OpenAI API Key to proceed.")
    api_key = st.text_input("Enter OpenAI API Key:", type="password")

# ✅ Proceed only if API key is available
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

    from src.langchain_agent import get_agentic_response

    # ✅ Streamlit page setup
    st.set_page_config(page_title="💬 AI Chat Assistant", layout="wide")
    st.title("💬 AI Chat Assistant (LangChain Enhanced)")

    # ✅ Initialize session history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # ✅ User input
    user_input = st.text_input("You:", key="user_input")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("🤖 Thinking..."):
            response = get_agentic_response(user_input)

        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.text_area("Assistant:", value=response, height=150)

    # ✅ Chat history display
    st.markdown("---")
    st.subheader("🗂 Chat History")
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**🧑 You:** {msg['content']}")
        else:
            st.markdown(f"**🤖 Assistant:** {msg['content']}")
else:
    st.stop()
