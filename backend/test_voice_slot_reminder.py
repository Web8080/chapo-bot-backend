import whisper
import requests
import os
import pyaudio
import wave
import pyttsx3
import json
import random
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse

# ---------- CONFIG ----------
WIT_TOKEN = "Bearer KMTQWKBOXWTGAWTRKLUH6UGGY4HJHYX6"  # Replace with your Wit.ai token
WIT_API_URL = "https://api.wit.ai/message?v=20230228"
LOG_FILE = "session_logs.json"
session_memory = {}

# Memory expiry config
SESSION_TTL_MINUTES = 15

# ---------- TTS ----------
def speak(text):
    print(f"🗣️ Chapo: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ---------- RECORD AUDIO ----------
def record_audio(filename="test.wav", duration=5, rate=16000):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=rate,
                    input=True,
                    frames_per_buffer=1024)
    print("🎤 Speak now...")
    frames = []
    for _ in range(0, int(rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    return filename

# ---------- TRANSCRIBE ----------
def transcribe_whisper(filename):
    print("🔍 Transcribing with Whisper...")
    model = whisper.load_model("base")
    result = model.transcribe(filename, language='en')  # Ensures English language transcription
    text = result['text'].strip()
    print(f"[You said]: {text if text else '[Nothing detected]'}")
    return text

# ---------- WIT.AI ----------
def get_intent_from_wit(text):
    if not text:
        return None, 0.0, {}
    headers = {"Authorization": WIT_TOKEN}
    params = {"q": text}
    response = requests.get(WIT_API_URL, headers=headers, params=params)
    if not response.ok:
        print("❌ Wit.ai error:", response.text)
        return None, 0.0, {}
    data = response.json()
    intents = data.get("intents", [])
    entities = data.get("entities", {})
    if intents:
        intent = intents[0]['name']
        confidence = intents[0]['confidence']
        print(f"✅ Detected intent: {intent} (Confidence: {confidence:.2f})")
        return intent, confidence, entities
    return None, 0.0, entities

# ---------- FALLBACK ----------
def fallback_with_free_gpt(user_input, memory=None):
    print("⚠️ Using free GPT fallback (mocked)...")
    return f"I'm not sure how to respond perfectly, can you say that differently?"

# ---------- SLOT-FILLING / REMINDER FLOW ----------
def handle_reminder_flow(session_id, entities):
    memory = session_memory.get(session_id, {}).get("data", {})
    print("📦 Raw Wit Entities:", json.dumps(entities, indent=2))
    task_key = next((k for k in entities if "task" in k), None)
    if task_key:
        task_values = [ent.get("value") or ent.get("body") for ent in entities[task_key] if ent.get("value") or ent.get("body")]
        if task_values:
            memory["task"] = max(task_values, key=len)
    datetime_key = next((k for k in entities if "datetime" in k), None)
    if datetime_key:
        memory["datetime"] = entities[datetime_key][0].get("value")
    session_memory[session_id] = {"data": memory, "last_updated": datetime.now(timezone.utc)}
    task = memory.get("task")
    time = memory.get("datetime")
    if task and time:
        session_memory.pop(session_id, None)
        pretty_time = parse(time).strftime("%A at %I:%M %p") if time else time
        return f"✅ Reminder set: I’ll remind you to {task} on {pretty_time}."
    elif not task:
        return "📝 What should I remind you about?"
    elif not time:
        return "⏰ What time should I remind you?"

# ---------- WEATHER API INTEGRATION ----------
import requests

# ---------- WEATHER API INTEGRATION ----------
def get_weather(city_name):
    weather_api_key = '9da4a523b41c453ab6f91434251604'  # WeatherAPI key
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city_name}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temp_c']
        description = data['current']['condition']['text']
        return f"The weather in {city_name} is {description} with a temperature of {temp}°C."
    else:
        return "Sorry, I couldn't fetch the weather for that city. Please try again later."

# ---------- PLAY MUSIC API INTEGRATION ----------
def play_music(song_name):
    token = get_spotify_token("client_id", "client_secret")  # Get Spotify token
    if token:
        # Search for the song name and fetch its details
        search_url = f"https://api.spotify.com/v1/search?q={song_name}&type=track&limit=1"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(search_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            track = data['tracks']['items'][0]
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            return f"Now playing {track_name} by {artist_name}."
        else:
            return "I couldn't find that song. Can you try a different one?"
    else:
        return "Sorry, I couldn't fetch the Spotify token."

# ---------- INTENT RESPONSES ----------
# ---------- INTENT RESPONSES ----------
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
        lambda: f"It’s now {datetime.now().strftime('%H:%M')}.",
        lambda: f"Right now, it's {datetime.now().strftime('%I:%M %p')}.",
        lambda: f"The time here is {datetime.now().strftime('%I:%M %p')}."
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


# ---------- RESPONSE ----------
import re

# ---------- MEMORY PRUNE ----------
def prune_memory(session_id):
    record = session_memory.get(session_id)
    if record:
        last_updated = record.get("last_updated")
        if datetime.now(timezone.utc) - last_updated > timedelta(minutes=SESSION_TTL_MINUTES):
            del session_memory[session_id]

def respond(intent, entities, session_id, user_input):
    prune_memory(session_id)
    memory = session_memory.get(session_id, {}).get("data", {})
    memory.update(entities)
    session_memory[session_id] = {"data": memory, "last_updated": datetime.now(timezone.utc)}

    # === Reminder handling ===
    if intent == "set_reminder":
        return handle_reminder_flow(session_id, entities)

    # === Time intent handling ===
    if intent == "time_now":
        return random.choice(INTENT_RESPONSES["time_now"])()

    # === Weather intent handling ===
    if intent == "get_weather" or intent == "wit$get_weather":
        city = None
        if "wit$location" in entities:
            city = entities["wit$location"][0].get("value")
        if not city:
            possible_cities = re.findall(r"(?:in|for)\s+([A-Za-z\s,]+)", user_input, re.IGNORECASE)
            if possible_cities:
                city = possible_cities[0].strip(" ?,")
        return get_weather(city) if city else "I couldn't find the city. Try asking again with a location."

    # === Music intent ===
    if intent == "play_music":
        song_name = entities.get("song", [{}])[0].get("value")
        return play_music(song_name) if song_name else "Sorry, I couldn't detect the song name."

    # ✅ === Direct Match: INTENT_RESPONSES ===
    if intent in INTENT_RESPONSES:
        responses = INTENT_RESPONSES[intent]
        return random.choice(responses) if isinstance(responses, list) else responses

    # === Fallback for known but low-confidence ===
    return "I didn't quite understand that. Can you say that differently?"

# ---------- LOGGING ----------
def log_session(session_id, user_input, intent, confidence, response, memory):
    log = {
        "session_id": session_id,
        "user_input": user_input,
        "intent": intent,
        "confidence": confidence,
        "response": response,
        "memory": memory,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log) + "\n")

# ---------- MAIN LOOP ----------
if __name__ == "__main__":
    print("🤖 Chapo is ready. Say 'exit' to quit.\n")
    session_id = "user_001"

    while True:
        audio_file = record_audio()
        transcribed_text = transcribe_whisper(audio_file)

        if "exit" in transcribed_text.lower():
            speak("Goodbye!")
            break

        intent, confidence, entities = get_intent_from_wit(transcribed_text)

        # Normalize intent name (remove Wit.ai prefix like 'wit$')
        if intent:
            intent = intent.replace("wit$", "")

        if not intent or confidence < 0.75:
            reply = fallback_with_free_gpt(transcribed_text, session_memory.get(session_id))
        else:
            reply = respond(intent, entities, session_id, transcribed_text)

        speak(reply)

        log_session(session_id, transcribed_text, intent, confidence, reply,
                    session_memory.get(session_id, {}).get("data", {}))
