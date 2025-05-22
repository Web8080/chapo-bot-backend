# tv_engine.py

def handle_tv(intent, user_input, memory=None):
    if intent == "media_playback":
        return "📺 Playing media on your smart TV."

    elif intent == "media_sharing":
        return "🔗 Sharing media to your smart display."

    else:
        return "📡 I’m not sure how to control that TV or display media request yet."
