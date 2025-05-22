from fastapi import APIRouter
from backend.db.mongo import db
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.get("/interactions")
def get_interactions():
    interactions = db["interactions"].find().sort("timestamp", -1)
    result = []
    for doc in interactions:
        result.append({
            "id": str(doc["_id"]),
            "text": doc.get("text", ""),
            "intent": doc.get("intent", ""),
            "confidence": doc.get("confidence", 0),
            "timestamp": str(doc.get("timestamp", datetime.now()))
        })
    return result
