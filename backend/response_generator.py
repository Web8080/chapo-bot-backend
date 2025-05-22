from multi_turn_manager import MultiTurnManager
from emotion_detector import detect_emotion

multi_turn = MultiTurnManager()

def generate_response(session_id, intent, entities, user_input):
    context = multi_turn.get_context(session_id)
    
    # If missing key information
    if intent == "set_reminder" and not any("task" in k for k in entities):
        return "What should I remind you about?"

    if intent == "set_reminder" and not any("datetime" in k for k in entities):
        return "When should I remind you?"

    if intent == "play_music" and not any(entities.values()):
        return "What song would you like to hear?"

    if intent == "get_weather" and not any("wit$location" in k for k in entities):
        return "Which city's weather would you like to know about?"

    # Emotionally adjust based on user input
    emotion = detect_emotion(user_input)
    if emotion == "sad":
        return "I'm here for you. What can I help you with right now?"
    
    return None  # Otherwise let normal flow handle
