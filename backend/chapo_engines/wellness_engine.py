# wellness_engine.py

def handle_wellness(intent, user_input, memory=None):
    if intent == "guided_meditation":
        return "🧘 Starting a 5-minute guided meditation. Close your eyes and take a deep breath..."

    elif intent == "hydration_reminder":
        return "💧 Don’t forget to drink some water! Staying hydrated is important."

    elif intent == "mood_support":
        return "🌈 I'm here for you. Want to talk about what’s been bothering you?"

    elif intent == "daily_checkin":
        return "📋 How are you feeling today on a scale from 1 to 10?"

    elif intent == "self_care_tips":
        return "💡 Here's a tip: Take 10 minutes today to do something just for yourself—read, stretch, or listen to your favorite song."

    elif intent in ["mental_checkin", "mental_health_checkin"]:
        return "🧠 Let’s take a quick mental check-in. How are you feeling today?"

    elif intent == "mood_detection":
        return "📊 Detecting mood now. Please describe how you’re feeling in a few words."

    elif intent == "meditation":
        return "🌿 Let's begin a short meditation session to help you relax."

    elif intent == "journal_thoughts":
        return "📓 Would you like me to save this thought in your wellness journal?"

    else:
        return "🧠 I'm still learning how to help with that wellness request."
