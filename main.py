import streamlit as st
from chatbot_backend import get_bot_response

st.set_page_config(page_title="Insurance Policy Chatbot")
st.title("🤖 AI-Powered Insurance Chatbot")

st.markdown("Ask me anything about insurance policies: health, auto, home, or life.")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Your question", key="input")

if query:
    with st.spinner("Thinking..."):
        response = get_bot_response(query)
        st.session_state.chat_history.append((query, response))

for q, r in reversed(st.session_state.chat_history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {r}")
