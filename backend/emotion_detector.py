# emotion_detector.py

import random

class EmotionDetector:
    def __init__(self):
        self.current_emotion = "neutral"
        self.emotion_history = []

    def detect_emotion(self, text):
        """Simple text-based emotion detection using keywords."""
        text = text.lower()
        emotion = "neutral"

        if any(word in text for word in ["sad", "depressed", "unhappy", "lonely"]):
            emotion = "sad"
        elif any(word in text for word in ["happy", "excited", "glad", "joyful"]):
            emotion = "happy"
        elif any(word in text for word in ["angry", "mad", "furious", "upset"]):
            emotion = "angry"
        elif any(word in text for word in ["tired", "sleepy", "exhausted"]):
            emotion = "tired"
        elif any(word in text for word in ["anxious", "worried", "nervous"]):
            emotion = "anxious"

        self.update_emotion(emotion)
        return emotion

    def update_emotion(self, new_emotion):
        """Update Chapo's memory about user's current mood."""
        self.emotion_history.append(new_emotion)
        if len(self.emotion_history) > 5:
            self.emotion_history.pop(0)  # Keep history small
        self.current_emotion = new_emotion

    def generate_emotion_response(self):
        """Generate a conversational reaction based on current mood."""
        if self.current_emotion == "sad":
            return random.choice([
                "I'm here for you. Want me to play something cheerful?",
                "I'm sending you a big virtual hug. Do you want to hear a joke?",
                "I'm always around if you need someone to talk to."
            ])
        elif self.current_emotion == "happy":
            return random.choice([
                "I love seeing you in high spirits!",
                "That's awesome! Want to celebrate with some music?",
                "Yay, your happiness makes my circuits buzz!"
            ])
        elif self.current_emotion == "angry":
            return random.choice([
                "That sounds frustrating. Want me to help you calm down with some breathing music?",
                "I'm here to listen if you want to vent a little.",
                "Maybe a calming song could help. Should I play one?"
            ])
        elif self.current_emotion == "tired":
            return random.choice([
                "Sounds like you need a recharge. Maybe a meditation session?",
                "You deserve a break. Should I suggest a relaxation playlist?",
                "Rest is important. I'm happy to keep things quiet if you want."
            ])
        elif self.current_emotion == "anxious":
            return random.choice([
                "Let's take a deep breath together. In and out.",
                "I'm right here with you. Maybe a calming playlist will help?",
                "You are stronger than you feel right now."
            ])
        else:
            return random.choice([
                "I'm here whenever you need me.",
                "Let me know if you'd like to chat or listen to music.",
                "How can I make your day better?"
            ])
