# appliance_engine.py

def handle_appliance(intent, user_input, memory=None):
    if intent == "control_appliance":
        return "🧺 Appliance has been turned on/off as requested."

    elif intent == "smart_appliance_management":
        return "📲 Managing smart appliances now. Everything looks good."

    elif intent == "turn_on_tv":
        return "📺 Turning on the TV for you. Enjoy your show!"

    elif intent == "screen_control":
        return "🖥️ Adjusting screen settings based on your preferences."

    else:
        return "🤖 I’m not sure how to handle that appliance request yet."
