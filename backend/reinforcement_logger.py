import json
from datetime import datetime

def log_feedback(session_id, user_input, intent, response, emotion):
    log_entry = {
        "session_id": session_id,
        "timestamp": datetime.utcnow().isoformat(),
        "user_input": user_input,
        "intent": intent,
        "response": response,
        "emotion": emotion
    }
    with open("reinforcement_logs.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
