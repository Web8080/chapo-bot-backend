import random
from datetime import datetime

# Sample workouts by type and duration
WORKOUTS = {
    "stretch": [
        "Neck rolls for 30 seconds.",
        "Shoulder rolls for 30 seconds.",
        "Side stretches for 1 minute.",
        "Hamstring stretch for 30 seconds each leg."
    ],
    "cardio": [
        "Jumping jacks – 1 minute.",
        "High knees – 30 seconds.",
        "Burpees – 10 reps.",
        "Mountain climbers – 45 seconds."
    ],
    "strength": [
        "Push-ups – 10 reps.",
        "Bodyweight squats – 15 reps.",
        "Plank – Hold for 1 minute.",
        "Lunges – 10 each leg."
    ]
}

# Track user sessions
fitness_sessions = {}

# Generate a workout routine
def start_fitness_routine(user_id, memory):
    now = datetime.now().strftime("%I:%M %p")
    memory[user_id] = {"routine_started": now}
    
    stretch = random.choice(WORKOUTS["stretch"])
    cardio = random.choice(WORKOUTS["cardio"])
    strength = random.choice(WORKOUTS["strength"])

    return (
        f"🏋️ Starting your home fitness routine ({now}):\n"
        f"1. {stretch}\n2. {cardio}\n3. {strength}\n"
        f"Let me know when you're done to log this session."
    )

# Log workout completion
def log_fitness_completion(user_id, memory):
    session = memory.pop(user_id, None)
    if session and session.get("routine_started"):
        return f"✅ Great job! Workout started at {session['routine_started']} logged successfully. 💪"
    else:
        return "🤔 I don’t have a workout session recorded. Say 'Start a workout' to begin."

# Unified handler

def handle_fitness(intent, user_input, memory):
    user_id = memory.get("session_id", "default_user")

    if intent in ["start_workout", "home_fitness"]:
        return start_fitness_routine(user_id, memory)

    if intent == "fitness_reminder" or "done" in user_input.lower():
        return log_fitness_completion(user_id, memory)

    return "❓ Not sure what you meant. Say 'Start a workout' to begin your routine."
