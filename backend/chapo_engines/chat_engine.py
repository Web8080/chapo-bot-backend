# chapo_engines/chat_engine.py

import random
import json

class ChatEngine:
    def __init__(self, memory):
        self.memory = memory  # Dictionary shared across all sessions
        self.turn_count = 0
        self.intent = "chat_emotion"
        self.context = {}

    def reset(self):
        self.turn_count = 0
        self.context = {}

    def handle_input(self, user_input):
        self.turn_count += 1

        mood_keywords = {
            "happy": ["happy", "great", "awesome", "fantastic"],
            "sad": ["sad", "down", "bad", "lonely"],
            "tired": ["tired", "exhausted", "sleepy"],
            "anxious": ["anxious", "worried", "nervous"]
        }

        for mood, keywords in mood_keywords.items():
            if any(word in user_input.lower() for word in keywords):
                self.context["user_mood"] = mood
                break

        # Branch responses by turn and context
        if self.turn_count == 1:
            return "How are you feeling today?"

        if "user_mood" in self.context:
            mood = self.context["user_mood"]
            if mood == "happy":
                return random.choice([
                    "That's wonderful to hear! Should I play something upbeat?",
                    "Yay! Would you like a fun trivia question to keep the mood going?"
                ])
            elif mood == "sad":
                return random.choice([
                    "I'm here for you. Would you like me to play something comforting?",
                    "Sad days happen. Want me to suggest a calming activity?"
                ])
            elif mood == "tired":
                return random.choice([
                    "You’ve earned a break. Would a meditation session help?",
                    "Sounds like nap time. Want me to lower the lights or play white noise?"
                ])
            elif mood == "anxious":
                return random.choice([
                    "Let's take a deep breath together. Want me to play a calm playlist?",
                    "You're not alone. Would a breathing session or nature sounds help?"
                ])

        return random.choice([
            "Want to talk about something specific?",
            "I'm here to chat or help however you like."
        ])


# Example usage:
# memory = {}
# chat = ChatEngine(memory)
# response = chat.handle_input("I'm feeling down today")
# print(response)
