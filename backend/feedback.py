import json
from datetime import datetime

def log_user_feedback(session_id, intent, response, feedback=None, file="feedback_logs.json"):
    log = {
        "session_id": session_id,
        "intent": intent,
        "response": response,
        "feedback": feedback or "neutral",  # default to neutral if no input yet
        "timestamp": datetime.utcnow().isoformat()
    }
    with open(file, "a") as f:
        f.write(json.dumps(log) + "\n")
