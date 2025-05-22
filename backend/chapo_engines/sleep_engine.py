import random
from datetime import datetime

# Sample sleep tips and routines
SLEEP_TIPS = [
    "Avoid screens at least 30 minutes before bed.",
    "Try a warm shower to relax your body.",
    "Use deep breathing to slow your heart rate.",
    "Keep your bedroom cool and dark.",
    "Avoid caffeine after 3 PM."
]

SLEEP_SOUNDS = [
    "https://noisli.com/sounds/ocean",
    "https://noisli.com/sounds/rain",
    "https://noisli.com/sounds/forest",
    "https://noisli.com/sounds/wind",
    "https://noisli.com/sounds/night"
]

# Intent handler for sleep-related requests
def handle_sleep(intent, user_input, memory):
    memory = memory or {}

    if intent == "help_sleep":
        tip = random.choice(SLEEP_TIPS)
        return f"😴 To improve sleep, try this tip: {tip}"

    if intent == "sleep_support":
        memory['expecting_sleep_issue'] = True
        return "🛌 Are you having trouble falling asleep, staying asleep, or waking too early?"

    if memory.get("expecting_sleep_issue"):
        memory['expecting_sleep_issue'] = False
        return f"💡 Noted. Here’s something soothing to help: {random.choice(SLEEP_SOUNDS)}"

    if intent == "bedtime_routine":
        return ("🕯️ Let's begin your bedtime routine:\n"
                "1. Dim the lights\n"
                "2. Play calming music\n"
                "3. Breathe deeply for 2 minutes\n"
                "4. No screens from now\n"
                f"5. Soundscape: {random.choice(SLEEP_SOUNDS)}")

    return "❓ I’m not sure how to help with that sleep request."
