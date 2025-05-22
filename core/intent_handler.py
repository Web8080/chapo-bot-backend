from core.gpt_responder import generate_response

INTENT_CONFIDENCE_THRESHOLD = 0.7  # Could be made configurable

def handle_intent(wit_data: dict, original_input: str) -> str:
    intents = wit_data.get("intents", [])
    if not intents:
        return fallback_to_gpt(original_input)

    top_intent = intents[0]
    if top_intent.get("confidence", 0) < INTENT_CONFIDENCE_THRESHOLD:
        return fallback_to_gpt(original_input)

    return f"Intent '{top_intent['name']}' detected with confidence {top_intent['confidence']:.2f}."

def fallback_to_gpt(user_input: str) -> str:
    return generate_response(f"User said: {user_input}")
