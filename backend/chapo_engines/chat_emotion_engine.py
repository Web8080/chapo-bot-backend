# chat_emotion_engine.py

import random
from datetime import datetime
import json
from elevenlabs import VoiceSettings

# Sample emotion response bank
EMOTION_RESPONSES = {
    "anxious": [
        "It's okay to feel anxious sometimes. Would you like me to play something calming?",
        "You're not alone. Want to try a quick meditation session?",
        "Let’s take a few deep breaths together. I'm right here."
    ],
    "sad": [
        "That sounds tough. I'm here for you.",
        "Would you like me to tell you a joke or play something relaxing?",
        "Sometimes talking helps. Want to hear some music or try a breathing exercise?"
    ],
    "lonely": [
        "I'm always around. Would you like to chat a bit more?",
        "Want to play a game or listen to a podcast together?",
        "You matter. How can I make you feel more connected right now?"
    ],
    "neutral": [
        "How are you really feeling today?",
        "I’m here for whatever you want to talk about.",
        "Would you like to do something uplifting together?"
    ]
}

# Optional: Save sessions for memory
def log_emotion_session(emotion, user_text):
    timestamp = datetime.now().isoformat()
    log_entry = {"timestamp": timestamp, "emotion": emotion, "input": user_text}
    try:
        with open("logs/chat_emotion_log.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"Error logging emotion: {e}")

# Handle emotion chat
def handle_chat_emotion(user_text, detected_emotion="neutral"):
    responses = EMOTION_RESPONSES.get(detected_emotion, EMOTION_RESPONSES["neutral"])
    selected = random.choice(responses)
    log_emotion_session(detected_emotion, user_text)
    return selected
