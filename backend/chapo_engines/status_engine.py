# status_engine.py

def handle_status(intent, user_input, memory=None):
    if intent == "sensor_status":
        return "📟 All sensors are functioning properly."

    elif intent == "get_device_status":
        return "🔍 Fetching device status... Everything looks normal."

    elif intent == "show_home_status":
        return "🏠 Home status dashboard: No alerts. All systems nominal."

    else:
        return "📊 I’m unsure how to report that status yet."
