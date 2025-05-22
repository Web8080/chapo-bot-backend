import cv2
import numpy as np
import os
from datetime import datetime
from pymongo import MongoClient
from fer import FER  # Facial Expression Recognition library

# ===== MongoDB Setup =====
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri) if mongo_uri else None

try:
    db = client.get_default_database() if client else None
except Exception as e:
    db = None
    print(f"❌ Failed to connect to MongoDB: {e}")

# ===== Initialize Webcam =====
cap = cv2.VideoCapture(0)
detector = FER(mtcnn=False)

print("📸 Starting real-time face & emotion detection... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Detect emotion and face
    results = detector.detect_emotions(frame)

    for result in results:
        (x, y, w, h) = result["box"]
        emotions = result["emotions"]
        dominant_emotion = max(emotions, key=emotions.get)
        confidence = emotions[dominant_emotion]

        # Draw box and label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        label = f"{dominant_emotion} ({confidence:.2f})"
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        # MongoDB Logging
        if db is not None:
            try:
                db.emotions.insert_one({
                    "timestamp": datetime.utcnow(),
                    "emotion": dominant_emotion,
                    "confidence": confidence,
                    "box": result["box"]
                })
            except Exception as e:
                print(f"❌ MongoDB logging error: {e}")

    # Show frame
    cv2.imshow("Chapo - Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("👋 Goodbye!")
