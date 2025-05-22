class MultiTurnManager:
    def __init__(self):
        self.sessions = {}

    def update_context(self, session_id, intent, entities):
        if session_id not in self.sessions:
            self.sessions[session_id] = {"history": []}
        self.sessions[session_id]["last_intent"] = intent
        self.sessions[session_id]["last_entities"] = entities
        self.sessions[session_id]["history"].append({"intent": intent, "entities": entities})

    def get_context(self, session_id):
        return self.sessions.get(session_id, {})
    
    def clear_context(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
