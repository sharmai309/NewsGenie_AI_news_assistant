# 📰 NewsGenie — AI News Assistant

An intelligent, conversational news assistant powered by AI. NewsGenie fetches the latest news and lets you interact with it through a natural language chatbot interface.

---

## 🚀 Features

- 🔍 **Automated News Fetching** — Pulls the latest articles from news sources in real time
- 🤖 **AI Chatbot Interface** — Ask questions about current events in plain English
- ⚙️ **Modular Workflow** — Clean separation of concerns across fetch, process, and chat layers
- 🧠 **Context-Aware Responses** — The assistant understands follow-up questions within a session

---

## 🗂️ Project Structure

```
NewsGenie_AI_news_assistant/
│
├── app.py            # Entry point — launches the application
├── chatbot.py        # AI chatbot logic and conversation handling
├── news_fetcher.py   # Fetches and parses news articles
└── workflow.py       # Orchestrates the end-to-end pipeline
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/sharmai309/NewsGenie_AI_news_assistant.git
cd NewsGenie_AI_news_assistant

# Install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
python app.py
```

---

## 💬 Usage

Once the app is running, simply type your news-related question in the terminal or UI:

```
You: What's happening in tech today?
NewsGenie: Here's a summary of today's top tech stories...
```

---

## 📦 Dependencies

| Package | Purpose |
|--------|---------|
| `requests` | Fetching news from APIs |
| `openai` / `anthropic` | AI language model integration |
| `beautifulsoup4` | HTML parsing (if scraping) |

> **Note:** A full `requirements.txt` will be added soon.

---

## 🔧 Configuration

Set the following environment variables before running:

```bash
export NEWS_API_KEY=your_news_api_key
export OPENAI_API_KEY=your_openai_api_key   # or ANTHROPIC_API_KEY
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👩‍💻 Author

**Isha Sharma** — [@sharmai309](https://github.com/sharmai309)

---

## 📄 License

This project is currently unlicensed. Feel free to reach out for collaboration or usage rights.
