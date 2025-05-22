# vision_engine.py

def handle_vision_intent(intent, user_input, memory=None):
    if intent == "detect_object":
        return "🔍 Detecting objects in your environment..."

    elif intent == "detect_motion":
        return "🎥 Motion detection activated. Scanning for movement..."

    elif intent == "detect_person":
        return "🧍 Detecting humans in the frame..."

    elif intent == "detect_pet":
        return "🐾 Looking for your pet... Hold still, scanning."

    elif intent == "detect_signs_of_life":
        return "❤️ Scanning for vital signs or movement..."

    elif intent == "vision_detect_objects":
        return "👁️ Running object detection algorithm..."

    else:
        return "🧠 I'm still learning how to process that visual request."
