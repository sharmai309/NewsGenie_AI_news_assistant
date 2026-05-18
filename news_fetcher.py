import requests
import os

CATEGORIES = {
    "Technology": "technology",
    "Finance": "business",
    "Sports": "sports"
}

FALLBACK = {
    "technology": [{"title": "AI advances continue in 2025", "description": "Latest developments in artificial intelligence.", "source": {"name": "TechNews"}, "url": "#"}],
    "business":   [{"title": "Markets steady amid global uncertainty", "description": "Stock markets hold firm.", "source": {"name": "FinanceDaily"}, "url": "#"}],
    "sports":     [{"title": "Championship finals this weekend", "description": "Top teams compete for the title.", "source": {"name": "SportsCentral"}, "url": "#"}],
}

def fetch_news(category: str = "technology", page_size: int = 5):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return FALLBACK.get(category, []), "⚠️ NEWS_API_KEY missing — showing cached headlines."
    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {"category": category, "language": "en", "pageSize": page_size, "apiKey": api_key}
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()
        articles = r.json().get("articles", [])
        if not articles:
            return FALLBACK.get(category, []), "No articles found — showing cached headlines."
        return articles, None
    except requests.exceptions.Timeout:
        return FALLBACK.get(category, []), "⚠️ News API timed out — showing cached headlines."
    except Exception as e:
        return FALLBACK.get(category, []), f"⚠️ News API error: {str(e)}"