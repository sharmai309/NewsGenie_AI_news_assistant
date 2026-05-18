from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional
from news_fetcher import fetch_news, CATEGORIES
from chatbot import chat

class QueryState(TypedDict):
    user_input: str
    category: str
    messages: list
    response: str
    news_articles: list
    error: Optional[str]
    query_type: str

NEWS_KEYWORDS = ["news", "headline", "latest", "update", "today", "happening", "market", "score", "result"]

def classify_query(state: QueryState) -> QueryState:
    text = state["user_input"].lower()
    if any(kw in text for kw in NEWS_KEYWORDS):
        state["query_type"] = "news"
    else:
        state["query_type"] = "chat"
    return state

def news_node(state: QueryState) -> QueryState:
    cat_key = CATEGORIES.get(state["category"], "technology")
    articles, error = fetch_news(cat_key)
    state["news_articles"] = articles
    state["error"] = error
    headlines = "\n".join([f"• {a['title']} ({a['source']['name']})" for a in articles])
    state["response"] = f"📰 **Top {state['category']} Headlines:**\n\n{headlines}"
    if error:
        state["response"] += f"\n\n{error}"
    return state

def chat_node(state: QueryState) -> QueryState:
    state["messages"].append({"role": "user", "content": state["user_input"]})
    reply = chat(state["messages"])
    state["messages"].append({"role": "assistant", "content": reply})
    state["response"] = reply
    return state

def verify_response(state: QueryState) -> QueryState:
    if not state.get("response"):
        state["response"] = "⚠️ No response generated. Please try again."
    return state

def route(state: QueryState) -> str:
    return state["query_type"]

def build_graph():
    g = StateGraph(QueryState)
    g.add_node("classify", classify_query)
    g.add_node("news_node", news_node)
    g.add_node("chat_node", chat_node)
    g.add_node("verify", verify_response)
    g.set_entry_point("classify")
    g.add_conditional_edges("classify", route, {"news": "news_node", "chat": "chat_node"})
    g.add_edge("news_node", "verify")
    g.add_edge("chat_node", "verify")
    g.add_edge("verify", END)
    return g.compile()

graph = build_graph()

def process_query(user_input: str, category: str, messages: list) -> dict:
    state = QueryState(
        user_input=user_input,
        category=category,
        messages=messages.copy(),
        response="",
        news_articles=[],
        error=None,
        query_type="chat"
    )
    result = graph.invoke(state)
    return result