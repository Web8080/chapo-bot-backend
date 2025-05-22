# personality_engine.py

def handle_personality(intent, user_input, memory=None):
    if intent == "personalization_engine":
        return "✨ I've adjusted my personality to better match your preferences."

    elif intent == "empathetic_response_generator":
        return "💬 I'm here for you. That sounds tough—want to talk more about it?"

    elif intent == "conversation_engagement":
        return "🤝 I'm listening. Tell me more about what you're thinking."

    else:
        return "🧠 I'm still learning how to handle that personality-related request."
