import random
import re
import os
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse
import logging
import requests
import spacy
from pymongo import MongoClient

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# MongoDB logging
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri) if mongo_uri else None
try:
    db = client.get_default_database() if client else None
except Exception:
    db = None

# In-memory session data
session_memory = {}
SESSION_TTL_MINUTES = 15

# Intent response templates
INTENT_RESPONSES = {
    "how_are_you": [
        "I'm functioning perfectly! How about you?",
        "Better now that we’re chatting!",
        "I’m great! What’s on your mind?",
        "Feeling sharp as ever!"
    ],
    "set_reminder": [
        "Reminder saved! I won’t let you forget.",
        "Got it — I’ll remind you.",
        "Noted. You’ll get a heads-up!",
        "I’ve locked it in your memory queue."
    ],
    "turn_on_lights": [
        "Lights turned on. Let there be light!",
        "Bringing brightness to the room!",
        "The lights are on now.",
        "Light mode: activated."
    ],
    "turn_off_lights": [
        "Turning the lights off now.",
        "Lights out. Enjoy the dark.",
        "Off they go. Night mode activated.",
        "Done. The room is now dark."
    ],
    "time_now": [
        lambda: f"The current time is {datetime.now().strftime('%I:%M %p')}",
        lambda: f"It’s now {datetime.now().strftime('%H:%M')}",
        lambda: f"Right now, it's {datetime.now().strftime('%I:%M %p')}",
        lambda: f"The time here is {datetime.now().strftime('%I:%M %p')}"
    ]
}

# Reminder flow handler
def handle_reminder_flow(session_id, entities):
    memory = session_memory.get(session_id, {}).get("data", {})
    logging.info(f"📦 Wit Entities: {entities}")

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

# Weather fetcher
def get_weather(city_name):
    api_key = os.getenv("WEATHER_API_KEY", "9da4a523b41c453ab6f91434251604")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"The weather in {city_name} is {data['current']['condition']['text']} with {data['current']['temp_c']} °C."
    return "Sorry, couldn't fetch weather info."

# Cleanup expired memory
def prune_memory(session_id):
    record = session_memory.get(session_id)
    if record and datetime.now(timezone.utc) - record.get("last_updated") > timedelta(minutes=SESSION_TTL_MINUTES):
        session_memory.pop(session_id, None)

# Local entity enhancement using spaCy
def extract_spacy_entities(text: str):
    doc = nlp(text)
    spacy_ents = {}
    for ent in doc.ents:
        label = ent.label_.lower()
        spacy_ents.setdefault(label, []).append(ent.text)
    return spacy_ents

# MongoDB logging
def log_to_mongo(session_id, user_input, intent, response):
    if db is not None:
        try:
            db.logs.insert_one({
                "session_id": session_id,
                "user_input": user_input,
                "intent": intent,
                "response": response,
                "timestamp": datetime.utcnow()
            })
        except Exception as e:
            logging.error(f"❌ MongoDB logging error: {e}")

# Main intent router
def route_intent(intent: str, entities: dict, user_input: str, session_id="default"):
    prune_memory(session_id)

    # spaCy entity fallback
    spacy_entities = extract_spacy_entities(user_input)
    if spacy_entities:
        logging.info(f"🔍 spaCy NER fallback: {spacy_entities}")

    if intent == "set_reminder":
        response = handle_reminder_flow(session_id, entities)
    elif intent == "time_now":
        response = random.choice(INTENT_RESPONSES["time_now"])()
    elif intent == "get_weather":
        city = None
        if "wit$location" in entities:
            city = entities["wit$location"][0].get("value")
        if not city:
            match = re.search(r"(?:in|for)\s+([A-Za-z\s,]+)", user_input)
            if match:
                city = match.group(1).strip(" ?,")
        response = get_weather(city) if city else "Please provide a location to get the weather."
    elif intent in INTENT_RESPONSES:
        responses = INTENT_RESPONSES[intent]
        response = random.choice(responses) if isinstance(responses, list) else responses
    else:
        response = "🤔 I'm not sure how to handle that yet."

    log_to_mongo(session_id, user_input, intent, response)
    return response