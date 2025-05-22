import requests

# Optional memory tracking if available from session
session_memory = {}

# Placeholder for detailed cooking guides
COOKING_GUIDES = {
    "spaghetti bolognese": [
        "Step 1: Heat oil in a large pan and sauté onions until soft.",
        "Step 2: Add minced beef and cook until browned.",
        "Step 3: Stir in tomato paste, chopped tomatoes, and seasoning.",
        "Step 4: Simmer for 30 minutes.",
        "Step 5: Meanwhile, cook spaghetti according to package instructions.",
        "Step 6: Drain spaghetti and combine with the sauce.",
        "Step 7: Serve with grated Parmesan cheese."
    ],
    "fried rice": [
        "Step 1: Heat oil in a wok and scramble eggs, then set aside.",
        "Step 2: Sauté garlic, onions, and vegetables.",
        "Step 3: Add cooked rice and mix well.",
        "Step 4: Stir in soy sauce and scrambled eggs.",
        "Step 5: Serve hot with green onions."
    ]
    # Add more meals (up to 20+) in future expansion
}

RECIPE_API_URL = "https://api.spoonacular.com/recipes/complexSearch"
RECIPE_API_KEY = "01491f086e057cb53ef4fa0f3d1e1cff05f9f3f9"  # Replace with actual key


def handle_cooking(intent, user_input, memory):
    """Handles cooking-related intents."""
    memory = memory or {}

    if intent == 'get_recipe':
        dish = memory.get("dish") or extract_dish_from_text(user_input)
        if not dish:
            memory['expecting_dish'] = True
            return generic_cooking_guide()
        memory['dish'] = dish
        memory['step'] = 1
        return fetch_recipe(dish)

    elif intent == 'step_by_step_cooking':
        if memory.get('expecting_dish'):
            dish = extract_dish_from_text(user_input)
            if dish:
                memory['dish'] = dish
                memory['step'] = 1
                memory.pop('expecting_dish')
                return f"🍽️ Great! Let's cook {dish}. {get_named_dish_step(memory, dish.lower(), 1)}"
            else:
                return "👩‍🍳 Please tell me which dish you'd like to cook."
        
        dish = memory.get("dish") or extract_dish_from_text(user_input)
        if dish and dish.lower() in COOKING_GUIDES:
            step = memory.get("step") or 1
            return get_named_dish_step(memory, dish.lower(), step)
        return "❓ Please specify a known dish so I can guide you step by step."

    elif intent == 'cooking_timer':
        duration = extract_timer_duration(user_input)
        if duration:
            memory['timer_set'] = duration
            return f"⏲️ Timer set for {duration} minutes."
        return "⏲️ How long should I set the timer for?"

    return "❓ Cooking intent not recognized."


def extract_dish_from_text(text):
    for keyword in ["for", "make", "cook", "prepare"]:
        if keyword in text.lower():
            words = text.lower().split(keyword)
            if len(words) > 1:
                return words[1].strip()
    return None


def extract_timer_duration(text):
    import re
    match = re.search(r'(\d{1,2}) ?(minutes|min)', text.lower())
    if match:
        return int(match.group(1))
    return None


def fetch_recipe(dish):
    try:
        params = {
            "query": dish,
            "number": 1,
            "apiKey": RECIPE_API_KEY
        }
        response = requests.get(RECIPE_API_URL, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])
            if results:
                title = results[0]['title']
                return f"🍽️ I found a recipe for {title}. Want to start cooking it step by step?"
            else:
                return "🍳 No recipes found for that dish."
        else:
            return "❗ Failed to fetch recipe."
    except Exception as e:
        return f"❌ Error retrieving recipe: {e}"


def get_named_dish_step(memory, dish, step):
    steps = COOKING_GUIDES.get(dish, [])
    if not steps:
        return "❗ I don’t have a cooking guide for that dish yet."
    if step <= len(steps):
        memory['step'] = step + 1
        return steps[step - 1]
    else:
        return f"✅ You’ve completed all the steps for {dish.title()}!"


def generic_cooking_guide():
    return ("👩‍🍳 You can ask me how to cook dishes like spaghetti bolognese, fried rice, or chicken curry. "
            "Try saying 'How do I cook fried rice?' or just tell me the dish you'd like help with.")