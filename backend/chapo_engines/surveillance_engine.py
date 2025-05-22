# surveillance_engine.py

def handle_surveillance_intent(intent, user_input, memory=None):
    if intent == "camera_stream":
        return "📷 Starting live camera stream..."

    elif intent == "stream_cam":
        return "📹 Streaming camera feed now."

    elif intent == "take_photo":
        return "📸 Capturing a photo now..."

    elif intent == "record_video":
        return "🎬 Recording video... say cheese!"

    elif intent == "remote_monitoring":
        return "🌐 Activating remote monitoring systems..."

    elif intent == "surveillance_patrol":
        return "🚨 Initiating surveillance patrol route..."

    else:
        return "🔍 I'm not yet sure how to handle that surveillance task."
