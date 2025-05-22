import json
from core.wit_client import get_intent
from core.intent_handler import handle_intent

with open("data/test.json") as f:
    utterances = json.load(f)

for text in utterances:
    wit_data = get_intent(text)
    print(f"User: {text}")
    print("Chapo:", handle_intent(wit_data, text))
    print("-" * 40)
