import json
import random
import os

TRIVIA_FILE = "trivia_questions.json"

# Load all trivia questions from file
def load_trivia_questions():
    if not os.path.exists(TRIVIA_FILE):
        return []
    with open(TRIVIA_FILE, "r") as f:
        return json.load(f)

# Return a nicely formatted question
def format_trivia_question(question):
    options_text = "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(question["options"])] )
    return f"🤔 {question['question']}\n{options_text}"

# Get and store a question for the user
def get_random_trivia(user_id, session_memory):
    questions = load_trivia_questions()
    question = random.choice(questions)
    session_memory[user_id] = {"current_trivia": question}
    return format_trivia_question(question)

# Check the user's answer and give feedback
def handle_trivia_answer(user_id, user_input, session_memory):
    memory = session_memory.get(user_id, {})
    current = memory.get("current_trivia")

    if not current:
        return "❗ No trivia question has been asked yet. Say 'Let's play trivia' to start."

    correct = current["answer"].lower()
    user_ans = user_input.strip().lower()

    session_memory.pop(user_id, None)
    if correct in user_ans or any(correct == opt.lower() for opt in current["options"] if user_ans in opt.lower()):
        return "🎉 Correct! Well done. Want another question?"
    else:
        return f"❌ Oops, the correct answer was '{current['answer']}'. Try another one?"

# Unified handler function
def handle_trivia(intent, user_input, memory):
    user_id = memory.get("session_id", "default_user")

    if intent in ["play_trivia", "trivia_question"]:
        return get_random_trivia(user_id, memory)

    if intent == "answer_trivia":
        return handle_trivia_answer(user_id, user_input, memory)

    return "❓ I'm not sure what you meant. Want to play trivia?"