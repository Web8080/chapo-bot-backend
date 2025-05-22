import json
import os
from datetime import datetime

# JSON file to track medication
MEDICATION_FILE = "medication_schedule.json"

# Load existing medication data
def load_medications():
    if not os.path.exists(MEDICATION_FILE):
        return []
    try:
        with open(MEDICATION_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Save updated medication list
def save_medications(data):
    with open(MEDICATION_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Add medication to schedule
def add_medication(name, time):
    schedule = load_medications()
    schedule.append({"name": name, "time": time, "timestamp": datetime.utcnow().isoformat()})
    save_medications(schedule)
    return f"💊 Scheduled {name} at {time}."

# Check upcoming meds
def get_medication_schedule():
    schedule = load_medications()
    if not schedule:
        return "🗂️ No medications scheduled."
    formatted = [f"- {m['name']} at {m['time']}" for m in schedule]
    return "🕒 Your current medication schedule:\n" + "\n".join(formatted)

# Main intent handler
def handle_medication(intent, user_input, memory):
    memory = memory or {}

    if intent == "track_medication":
        return get_medication_schedule()

    if intent == "detect_med_chart":
        return "📸 I'm ready to visually scan your chart. Please show the medication chart to my camera (feature in progress)."

    if intent == "medication_reminder":
        memory['expecting_med_name'] = True
        return "📝 What medication should I remind you about?"

    if memory.get("expecting_med_name"):
        memory['med_name'] = user_input
        memory['expecting_med_name'] = False
        memory['expecting_med_time'] = True
        return f"⏰ Got it. When should I remind you to take {user_input}?"

    if memory.get("expecting_med_time"):
        name = memory.pop("med_name")
        time = user_input
        memory['expecting_med_time'] = False
        return add_medication(name, time)

    return "❓ I couldn't understand your medication request."
