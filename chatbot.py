import os
from anthropic import Anthropic

client = Anthropic()

SYSTEM_PROMPT = """You are NewsGenie, an AI news and information assistant.
- For news requests: tell the user you are fetching live headlines for them.
- For general questions: answer helpfully and concisely.
- Always be factual, neutral, and cite uncertainty when unsure.
- Keep responses under 150 words unless asked for detail."""

def chat(messages: list) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return "⚠️ ANTHROPIC_API_KEY is missing. Please add it to your .env file."
    try:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=messages
        )
        return response.content[0].text
    except Exception as e:
        return f"⚠️ AI error: {str(e)}"