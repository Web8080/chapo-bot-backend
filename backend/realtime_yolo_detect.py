import cv2
from ultralytics import YOLO
import os
from datetime import datetime
from pymongo import MongoClient
import logging

# Load YOLOv5 model (auto-downloads if not present)
model = YOLO("yolov5s.pt")

# MongoDB setup (optional)
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri) if mongo_uri else None
db = client.get_default_database() if client else None

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Could not access the webcam.")
    exit()

print("📸 Real-time object detection started — Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to capture frame.")
        break

    # Run YOLOv5 object detection
    results = model.predict(frame, imgsz=640, conf=0.4)[0]

    # Draw results
    annotated = results.plot()

    # Log results
    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])
        detections.append({"label": label, "confidence": round(conf, 2)})

    if db is not None:
        try:
            db.yolo_detections.insert_one({
                "timestamp": datetime.utcnow(),
                "detections": detections
            })
        except Exception as e:
            logging.error(f"❌ MongoDB logging failed: {e}")

    # Display
    cv2.imshow("Chapo - YOLOv5 Object Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("👋 Session ended.")
