import os
import urllib.request

YOLO_DIR = "yolo"
os.makedirs(YOLO_DIR, exist_ok=True)

YOLO_FILES = {
    "yolov3-tiny.cfg": "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg",
    "yolov3-tiny.weights": "https://pjreddie.com/media/files/yolov3-tiny.weights",
    "coco.names": "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
}

def download_yolo_files():
    for filename, url in YOLO_FILES.items():
        filepath = os.path.join(YOLO_DIR, filename)
        if not os.path.exists(filepath):
            print(f"⬇️ Downloading {filename}...")
            try:
                req = urllib.request.Request(
                    url,
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
                print(f"✅ Saved to {filepath}")
            except Exception as e:
                print(f"❌ Failed to download {filename}: {e}")
        else:
            print(f"✅ {filename} already exists.")

if __name__ == "__main__":
    download_yolo_files()
