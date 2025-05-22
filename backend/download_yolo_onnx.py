# download_yolo_onnx.py
import os
import requests

os.makedirs("yolo", exist_ok=True)

# ✅ Public ONNX model (yolov3-tiny)
url = "https://github.com/onnx/models/raw/main/vision/object_detection_segmentation/yolov3-tiny/model/yolov3-tiny.onnx"
save_path = "yolo/yolov3-tiny.onnx"

print("⬇️ Downloading YOLOv3-tiny ONNX model...")
try:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"✅ Saved to {save_path}")
except Exception as e:
    print(f"❌ Failed to download model: {e}")
