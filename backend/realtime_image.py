import torch
from torchvision import models, transforms
from PIL import Image
import requests
import os

# Download ImageNet labels if needed
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
LABELS_PATH = "imagenet_classes.txt"

if not os.path.exists(LABELS_PATH):
    labels = requests.get(LABELS_URL).text
    with open(LABELS_PATH, "w") as f:
        f.write(labels)

with open(LABELS_PATH, "r") as f:
    categories = [s.strip() for s in f.readlines()]

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Load pre-trained model
model = models.mobilenet_v2(pretrained=True)
model.eval()

# Image classification
def classify_image(image_path):
    image = Image.open(image_path).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = outputs.max(1)
        return categories[predicted.item()]

# === Run ===
if __name__ == "__main__":
    test_image = input("📸 Enter path to image (e.g., cat.png or /full/path/to/image.jpg): ").strip()
    if os.path.exists(test_image):
        prediction = classify_image(test_image)
        print(f"🔍 I see: {prediction}")
    else:
        print("❌ Image not found. Make sure the path is correct.")
