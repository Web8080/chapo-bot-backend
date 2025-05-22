# backend/services/memory.py

from collections import defaultdict
import threading

# Thread-safe in-memory session storage
session_store = defaultdict(list)
lock = threading.Lock()

def session_memory(session_id: str, message: dict):
    """
    Store a message or interaction in session memory for a given session_id.
    """
    with lock:
        session_store[session_id].append(message)

def prune_memory(session_id: str, max_length: int = 50):
    """
    Prune session memory for a session_id to keep it within max_length.
    Removes oldest messages if above limit.
    """
    with lock:
        if session_id in session_store and len(session_store[session_id]) > max_length:
            session_store[session_id] = session_store[session_id][-max_length:]
