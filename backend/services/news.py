import os
import requests

def get_news(category: str = None) -> str:
    news_api_key = os.getenv("NEWS_API_KEY")
    if not news_api_key:
        return "News API key not found. Please set it in .env."

    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": news_api_key
    }
    if category:
        params["category"] = category.lower()

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        if not articles:
            return f"Sorry, I couldn't find any {category or 'general'} news right now."

        top_headlines = [article['title'] for article in articles[:3]]
        return f"🗞️ Here are the latest {category or 'general'} headlines: " + " | ".join(top_headlines)
    else:
        return "Sorry, I couldn't fetch the news at this time."
