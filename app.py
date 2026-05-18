import streamlit as st
from dotenv import load_dotenv
from workflow import process_query
from news_fetcher import fetch_news, CATEGORIES

load_dotenv()

st.set_page_config(page_title="NewsGenie", page_icon="📰", layout="wide")
st.title("📰 NewsGenie — AI News Assistant")
st.caption("Real-time news + AI chat, powered by Claude & LangGraph")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    category = st.selectbox("News Category", list(CATEGORIES.keys()))
    if st.button("🔄 Fetch Latest Headlines"):
        with st.spinner("Fetching news..."):
            articles, error = fetch_news(CATEGORIES[category])
        if error:
            st.warning(error)
        for a in articles:
            st.markdown(f"**{a['title']}**  \n*{a['source']['name']}*")
            if a.get("description"):
                st.caption(a["description"])
            st.divider()
    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat_history = []
        st.rerun()

# Chat history display
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything or request news headlines…"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            result = process_query(prompt, category, st.session_state.messages)
        response = result["response"]
        st.markdown(response)
        st.session_state.messages = result["messages"]
        st.session_state.chat_history.append({"role": "assistant", "content": response})