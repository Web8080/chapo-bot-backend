## this will handle things like definitions, facts, trivia, Q&A
# knowledge_engine.py

import random

def handle_knowledge(intent, user_input, memory=None):
    if intent == "define_term":
        # TODO: Hook to dictionary or language model
        return "📘 Let me look up the definition for you..."

    elif intent == "general_knowledge_question":
        return "🧠 Interesting question! Let me find the best answer..."

    elif intent == "trivia_question":
        trivia_facts = [
            "🐘 Elephants are the only mammals that can't jump.",
            "🌎 A day on Venus is longer than a year on Venus.",
            "🍯 Honey never spoils. Archaeologists have found edible honey in ancient tombs!"
        ]
        return f"🤓 Did you know? {random.choice(trivia_facts)}"

    elif intent == "math_question":
        return "🧮 I'm crunching the numbers for you..."

    elif intent == "language_practice":
        return "🗣️ Let's practice some vocabulary. Say a word, and I’ll translate or repeat it."

    else:
        return "📚 I'm still learning how to answer that. Want to ask me a fun fact?"
