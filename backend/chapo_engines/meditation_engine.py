import random

# Session memory dictionary
session_memory = {}

# Predefined ambient sound options (using royalty-free demo audio)
SOUND_STREAMS = {
    "ocean waves": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "rainforest": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "wind breeze": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "fireplace": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    "night crickets": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
}


def handle_guided_meditation(intent, user_input, memory):
    memory = memory or {}

    if intent == "guided_meditation":
        memory['expecting_meditation_type'] = True
        return ("🧘 Would you prefer a breathing exercise or some ambient sounds? "
                "You can say things like 'play ocean waves' or 'start a meditation session.'")

    elif intent == "play_calm_audio":
        choice = extract_sound_type(user_input)
        if choice:
            memory.pop('expecting_meditation_type', None)
            url = SOUND_STREAMS.get(choice)
            if url:
                return f"🔊 Streaming '{choice.title()}'... You can open this link in your browser to listen: {url}"
            else:
                return "❌ I couldn't find that sound. Try 'ocean waves' or 'fireplace'."

        if memory.get('expecting_meditation_type'):
            return ("🌿 Please choose a sound type. For example: 'Play rain sounds', 'Start wind breeze', or 'Fireplace noise'.")

        return "❓ What kind of calm sound would you like to hear?"

    return "❌ Guided meditation request not recognized."


def extract_sound_type(text):
    for key in SOUND_STREAMS:
        if key in text.lower():
            return key
    return None
