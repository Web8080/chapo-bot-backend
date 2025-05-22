import random

CORE_CONVERSATION_RESPONSES = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?",
        "Hey! Ready to chat whenever you are."
    ],
    "goodbye": [
        "Goodbye! Talk soon!",
        "See you later! Stay safe.",
        "Take care! I'm always here if you need me."
    ],
    "how_are_you": [
        "I'm just a bunch of code, but I'm doing great!",
        "Feeling fantastic and ready to assist!",
        "Running smoothly—thanks for asking!"
    ],
    "bot_feelings": [
        "I don't have feelings, but I enjoy helping you!",
        "I'm all logic, no emotion—but I'm happy when you are!",
        "I'm always calm, collected, and here for you."
    ],
    "tell_me_about_you": [
        "I'm Chapo, your personal assistant. I can help with reminders, music, smart home devices, and more!",
        "I’m your AI companion—trained to assist, chat, and be helpful!",
        "I'm here to make your day easier, one task at a time."
    ],
    "smart_greetings": [
        "Top of the morning to you!",
        "Hope you're having a great day!",
        "Good to see you! How can I assist?"
    ]
}

# ✅ Updated to accept user_input as the second argument
def handle_core_conversation(intent, user_input=None):
    responses = CORE_CONVERSATION_RESPONSES.get(intent, [])
    if responses:
        return random.choice(responses)
    return "I'm not sure how to respond to that, but I'm learning!"
