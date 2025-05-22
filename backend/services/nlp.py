import requests
import os
import logging

WIT_API_URL = "https://api.wit.ai/message?v=20230228"
WIT_TOKEN = os.getenv("WIT_TOKEN", "Bearer your-wit-token")

def get_intent_from_wit(text: str):
    if not text:
        return None, 0.0, {}
    headers = {"Authorization": WIT_TOKEN}
    params = {"q": text}
    try:
        response = requests.get(WIT_API_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        intents = data.get("intents", [])
        entities = data.get("entities", {})
        if intents:
            intent = intents[0]["name"]
            confidence = intents[0]["confidence"]
            logging.info(f"✅ Wit.ai intent: {intent} ({confidence:.2f})")
            return intent, confidence, entities
        return None, 0.0, entities
    except Exception as e:
        logging.error(f"Wit.ai API error: {e}")
        return None, 0.0, {}
