import streamlit as st
import os
from dotenv import load_dotenv
from langchain_agent import get_agentic_response

# Try loading from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# If .env is not present or key is missing, ask user
if not api_key:
    st.warning("🔐 Please enter your OpenAI API Key to proceed.")
    api_key = st.text_input("Enter OpenAI API Key:", type="password")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

    st.set_page_config(page_title="AI Chat Assistant", layout="wide")
    st.title("💬 AI Chat Assistant (LangChain Enhanced)")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="user_input")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        response = get_agentic_response(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.text_area("Assistant:", value=response, height=150)

    st.markdown("---")
    st.subheader("🗂 Chat History")
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**🧑 You:** {msg['content']}")
        else:
            st.markdown(f"**🤖 Assistant:** {msg['content']}")
else:
    st.stop()
