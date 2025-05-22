import random
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse
import re
from backend.services.memory import session_memory, prune_memory
from backend.services.music import play_music
from backend.services.weather import get_weather
from backend.services.reminder import handle_reminder
from backend.services.news import get_news
from backend.services import shopping_list_service

# Central dictionary for canned responses
INTENT_RESPONSES = {
    "calendar_event": [
        "Got it. I've added that event to your calendar.",
        "Okay, it’s been added.",
        "Your calendar event is scheduled!",
        "Done! It’s on your calendar."
    ],
    "calendar_integration": [
        "Your calendar is synced and up to date.",
        "Integration complete — calendar is ready.",
        "Calendar synced without issues.",
        "All set with your calendar."
    ],
    "camera_stream": [
        "Streaming camera footage now.",
        "Pulling up your camera stream.",
        "Accessing live video feed.",
        "Here comes the camera footage."
    ],
    "casual_checkin": [
        "Hey there! I'm functioning perfectly! How can I help?",
        "All systems go! How’s your day?",
        "Doing awesome. You?",
        "Hey! I'm good. What can I do for you today?"
    ],
    "chat_emotion": [
        "I’m always here for you. Emotions matter.",
        "You can share anything with me.",
        "Tell me how you're feeling.",
        "I'm listening — how can I support you?"
    ],
    "emergency_alert": [
        "🚨 Alert triggered! Help is on the way.",
        "Emergency mode activated. Stay calm.",
        "I'm calling for help immediately.",
        "Panic button hit. Help is en route."
    ],
    "get_weather": [
        "Sure, let me fetch the weather for you.",
        "Getting the weather update now.",
        "Just a second, checking the forecast.",
        "Here’s what the skies are saying."
    ],
    "health_check": [
        "Checking your health stats now.",
        "Health systems scanning…",
        "Pulling up your wellness data.",
        "Monitoring your vitals now."
    ],
    "how_are_you": [
        "I'm functioning perfectly! How about you?",
        "Better now that we’re chatting!",
        "I’m great! What’s on your mind?",
        "Feeling sharp as ever!"
    ],
    "media_control": [
        "Media updated accordingly.",
        "Volume adjusted and media settings saved.",
        "The playback settings are updated.",
        "Media is all set!"
    ],
    "mental_checkin": [
        "Noted. Let’s take a deep breath together.",
        "Taking a moment for mindfulness.",
        "Logging your mental state.",
        "It’s good to check in with yourself."
    ],
    "play_music": [
        "Playing your requested song now.",
        "Here comes the vibe!",
        "Your playlist is loading.",
        "Enjoy your music 🎵"
    ],
    "sensor_status": [
        "Let me check the status of your home sensors.",
        "Scanning all connected sensors.",
        "Sensor data coming up.",
        "Everything seems in order — want the report?"
    ],
    "sentiment_report": [
        "Logging that. Your mood matters!",
        "Sentiment tracked and stored.",
        "Got it. I’ve saved your current mood.",
        "Thanks for sharing how you feel."
    ],
    "set_reminder": [
        "Reminder has been saved. I won’t let you forget.",
        "Got it — I’ll remind you.",
        "Noted. You’ll get a heads-up!",
        "I’ve locked it in your memory queue."
    ],
    "smart_kitchen": [
        "Smart kitchen activated.",
        "All systems in the kitchen are online.",
        "Turning on kitchen assistance.",
        "Chef mode: engaged."
    ],
    "tell_joke": [
        "What do you get when you cross AI and humor? Me!",
        "Why was the computer cold? It left its Windows open!",
        "I'd tell you a joke about UDP... but you might not get it.",
        "Knock knock. Who’s there? AI. AI who? AI’m here to make you laugh!"
    ],
    "time_now": [
        lambda: f"The current time is {datetime.now().strftime('%I:%M %p')}",
        lambda: f"It’s now {datetime.now().strftime('%H:%M')}",
        lambda: f"Right now, it's {datetime.now().strftime('%I:%M %p')}",
        lambda: f"The time here is {datetime.now().strftime('%I:%M %p')}"
    ],
    "turn_off_lights": [
        "Turning the lights off now.",
        "Lights out. Enjoy the dark.",
        "Off they go. Night mode activated.",
        "Done. The room is now dark."
    ],
    "turn_on_lights": [
        "Lights turned on. Let there be light!",
        "Bringing brightness to the room!",
        "The lights are on now.",
        "Light mode: activated."
    ]
}

def respond(intent, entities, session_id, user_input):
    prune_memory(session_id)
    memory = session_memory.get(session_id, {}).get("data", {})
    memory.update(entities)
    session_memory[session_id] = {"data": memory, "last_updated": datetime.now(timezone.utc)}

    if intent == "set_reminder":
        return handle_reminder_flow(session_id, entities)

    if intent == "time_now":
        return random.choice(INTENT_RESPONSES["time_now"])()

    if intent == "get_weather" or intent == "wit$get_weather":
        city = None
        if "wit$location" in entities:
            city = entities["wit$location"][0].get("value")
        if not city:
            possible_cities = re.findall(r"(?:in|for)\\s+([A-Za-z\\s,]+)", user_input, re.IGNORECASE)
            if possible_cities:
                city = possible_cities[0].strip(" ?,")
        return get_weather(city) if city else "I couldn't find the city. Try asking again with a location."

    if intent == "play_music":
        song_name = entities.get("song", [{}])[0].get("value")
        return play_music(song_name) if song_name else "Sorry, I couldn't detect the song name."

    if intent in INTENT_RESPONSES:
        responses = INTENT_RESPONSES[intent]
        return random.choice(responses) if isinstance(responses, list) else responses

    return "I didn't quite understand that. Can you say that differently?"
