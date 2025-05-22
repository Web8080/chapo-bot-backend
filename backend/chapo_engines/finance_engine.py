# finance_engine.py
##handle things like logging expenses, budget summaries

def handle_finance(intent, user_input, memory=None):
    if intent == "log_expense":
        # Simple mocked logic for expense logging
        return "🧾 Your expense has been logged successfully."

    elif intent == "budget_summary":
        return "📊 Here's your current budget summary:\n- Food: $120\n- Bills: $250\n- Entertainment: $80"

    elif intent == "track_expenses":
        return "📈 You've spent $450 this month across 3 categories."

    elif intent == "set_budget_goal":
        return "✅ Budget goal set. I'll help you stay on track."

    elif intent == "investment_tips":
        return "💹 Here's a tip: Diversify your portfolio and review your risk tolerance regularly."

    else:
        return "❗ I couldn’t understand that finance request."
