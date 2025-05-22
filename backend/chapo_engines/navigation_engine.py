# navigation_engine.py

def handle_autonomous_navigation(user_input, entities=None):
    """
    Handles requests related to autonomous pathfinding or general navigation.
    """
    location = None
    if entities and "wit$location" in entities:
        location = entities["wit$location"][0].get("value")

    if location:
        return f"🗺️ Initiating autonomous navigation to {location}. Navigating now..."
    return "🗺️ Where would you like to go? Please specify a destination."

def handle_safe_path_planning(user_input, entities=None):
    """
    Calculates or confirms a safe path based on context.
    """
    destination = None
    if entities and "wit$location" in entities:
        destination = entities["wit$location"][0].get("value")

    if destination:
        return f"🚦 Calculating safest path to {destination}... Route locked in."
    return "🚦 Please specify where you're headed so I can plan a safe path."

def handle_multi_floor_support(user_input, entities=None):
    """
    Responds to multi-floor navigation and elevator access.
    """
    return "🏢 Multi-floor support enabled. Directing you to the appropriate floor."

def handle_get_directions(user_input, entities=None):
    location = None
    if entities and "wit$location" in entities:
        location = entities["wit$location"][0].get("value")

    if location:
        return f"🗺️ Getting directions to {location}... Estimated travel time is 12 minutes."
    return "🗺️ Please tell me where you want directions to."

def handle_estimate_arrival(user_input, entities=None):
    location = None
    if entities and "wit$location" in entities:
        location = entities["wit$location"][0].get("value")

    if location:
        return f"🚗 Estimating arrival time to {location}... You'll arrive in about 15 minutes."
    return "🚗 Where are you headed? I can estimate your arrival time."

def handle_find_place(user_input, entities=None):
    place = None
    if entities and "wit$location" in entities:
        place = entities["wit$location"][0].get("value")

    if place:
        return f"🔍 Looking for {place} nearby... Found a match 5 minutes away."
    return "🔍 What place are you trying to find?"

def handle_get_nearby_places(user_input, entities=None):
    return "📍 Here are some nearby places: coffee shop, pharmacy, and grocery store."

def handle_room_transition(user_input, entities=None):
    return "🚪 Transitioning to the next room... Sensors adjusted and path confirmed."
