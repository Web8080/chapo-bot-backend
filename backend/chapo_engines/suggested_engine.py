# suggested_engine.py
##this will handle proactive suggestions, context awareness, and smart predictions

def handle_suggested_features(intent, user_input, memory=None):
    if intent == "suggest_tip":
        return "💡 Here's a tip: You can say 'Remind me to drink water every 2 hours' to stay hydrated!"

    elif intent == "context_aware_suggestion":
        return "🔍 Based on your past queries, would you like to check the weather again?"

    elif intent == "proactive_offer":
        return "🤖 I noticed it's been a long day. Want to hear something calming or play music?"

    elif intent == "smart_recommendation":
        return "🧠 Here's a smart suggestion: Enable morning summary to get a daily update on weather, schedule, and news."

    elif intent == "pattern_insight":
        return "📊 You usually set reminders around 8pm. Want me to prepare a nightly routine?"

    else:
        return "🤔 I'm still learning how to assist better. Thanks for your patience!"
