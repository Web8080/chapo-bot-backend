# security_engine.py

def handle_security(intent, user_input, entities=None):
    if intent == "lock_doors":
        return "🔒 All doors have been securely locked."

    elif intent == "unlock_doors":
        return "🔓 Doors have been unlocked. Please ensure safety."

    elif intent == "open_garage":
        return "🚗 Opening the garage door now..."

    elif intent == "face_authentication":
        return "🧑‍💻 Verifying your face... Access granted."

    elif intent == "voice_authentication":
        return "🗣️ Voice recognized successfully. You're logged in."

    elif intent == "recognize_face":
        return "🖼️ Face recognized. Hello again!"

    elif intent == "access_logs":
        return "📜 Here are your most recent access logs. [Mocked for demo]"

    else:
        return "❗ I’m not sure how to handle that security task yet."

def security_engine_dispatcher(intent, user_input, entities=None):
    return handle_security(intent, user_input, entities)
