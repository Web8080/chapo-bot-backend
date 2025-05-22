import random

# Mock list of user contacts
CONTACTS = [
    "Mom", "Dad", "Alex", "Sarah", "James", "Grandma"
]

# Memory of current call state
call_sessions = {}

# Start a video call with a known contact
def start_video_call(contact_name):
    if contact_name in CONTACTS:
        return f"📹 Starting a video call with {contact_name}... Connecting now."
    else:
        return f"❗ I couldn't find {contact_name} in your contacts. Try someone else?"

# Join an ongoing group call (mocked)
def join_group_call():
    group_name = random.choice(["family", "friends", "team meeting"])
    return f"👥 Joining the {group_name} group call now."

# Handle video call-related intents
def handle_video_call(intent, user_input, memory):
    user_id = memory.get("session_id", "default_user")

    if intent == "video_call_friend":
        for name in CONTACTS:
            if name.lower() in user_input.lower():
                return start_video_call(name)
        return "👤 Who would you like to call? Try saying 'Call Sarah on video'."

    if intent == "start_video_call":
        return "📞 Starting a new video call. Who should I connect you to?"

    if intent == "join_video_call":
        return join_group_call()

    return "❓ I didn't catch who to call. Please say 'Start a call with [Name]'."
