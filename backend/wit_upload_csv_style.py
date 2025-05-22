import os
import glob
import pandas as pd
import requests
import json

# ✅ Your Wit.ai Server Access Token
ACCESS_TOKEN = "KMTQWKBOXWTGAWTRKLUH6UGGY4HJHYX6"  # <-- Replace this!

# ✅ Headers and API URLs
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
INTENT_URL = "https://api.wit.ai/intents?v=20230204"
UTTERANCE_URL = "https://api.wit.ai/utterances?v=20230204"

# ✅ Path to your CSV files
batch_folder = "new_batch"
csv_files = sorted(glob.glob(os.path.join(batch_folder, "*.csv")))

# 🧠 Track created intents to avoid duplication
created_intents = set()

for file in csv_files:
    print(f"\n📤 Processing: {file}")
    df = pd.read_csv(file)

    # 🧠 Create any missing intents
    for intent in df['intent'].unique():
        if intent not in created_intents:
            res = requests.post(INTENT_URL, headers=HEADERS, json={"name": intent})
            if res.status_code == 200:
                print(f"✅ Created intent: {intent}")
            elif "already exists" in res.text:
                print(f"🔁 Intent exists: {intent}")
            else:
                print(f"❌ Failed to create intent {intent}: {res.text}")
            created_intents.add(intent)

    # 🗣 Upload utterances (entity labels skipped, just used for training)
    for i, row in df.iterrows():
        text = row.get("uttrance", row.get("text", "")).strip()
        intent = row["intent"].strip()

        if not text:
            print(f"⚠️ Skipping empty text on row {i+1}")
            continue

        utterance = {
            "text": text,
            "intent": intent,
            "entities": [],  # Skip entity positions; train later in Wit UI
            "traits": {}
        }

        res = requests.post(UTTERANCE_URL, headers=HEADERS, json=[utterance])
        if res.status_code == 200:
            print(f"✅ Uploaded {i+1}: \"{text}\"")
        else:
            print(f"❌ Failed {i+1}: {res.status_code} - {res.text}")
