import requests
import logging
from config.keys import WIT_TOKEN
from config.settings import WIT_API_URL

def get_intent(text: str) -> dict:
    headers = {"Authorization": f"Bearer {WIT_TOKEN}"}
    params = {"q": text}
    try:
        response = requests.get(WIT_API_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"[WitClient] Failed to fetch intent: {e}")
        return {"intents": [], "entities": {}, "error": str(e)}
