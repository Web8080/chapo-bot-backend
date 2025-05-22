def handle_battery_status(user_input, entities):
    # Simulate checking battery level
    battery_level = 76  # You can replace with real API/hardware call
    if battery_level > 80:
        return "🔋 Your battery level is high at 76%. You're good to go!"
    elif battery_level > 40:
        return "🔋 Your battery is at a moderate level: 76%. Consider charging soon."
    else:
        return "⚠️ Your battery is low at 76%. Please charge immediately."

def handle_battery_alerts(user_input, entities):
    # Simulate battery warning or trigger
    return "🚨 Battery alert triggered! Power levels are critically low. Entering power-saving mode."
