import requests
import pandas as pd
import glob
import os

# Your Wit.ai Token
ACCESS_TOKEN = "U7I2QUYBD2R2ZAZQYQZZ36R4YULPHOKI"
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# URLs
INTENT_URL = "https://api.wit.ai/intents?v=20230204"
UTTERANCE_URL = "https://api.wit.ai/utterances?v=20230204"

# Point to CSV batch folder
batch_folder = "batches"
csv_files = sorted(glob.glob(os.path.join(batch_folder, "*.csv")))

# Track created intents
created_intents = set()

for file in csv_files:
    print(f"📤 Processing: {file}")
    df = pd.read_csv(file)

    # Create missing intents first
    for intent in df['intent'].unique():
        if intent not in created_intents:
            r = requests.post(INTENT_URL, headers=HEADERS, json={"name": intent})
            if r.status_code == 200:
                print(f"✅ Created intent: {intent}")
            elif "already exists" in r.text:
                print(f"🔁 Intent exists: {intent}")
            else:
                print(f"❌ Failed to create intent {intent}: {r.text}")
            created_intents.add(intent)

    # Upload utterances
    data = []
    for _, row in df.iterrows():
        data.append({
            "text": row["utterance"],
            "intent": row["intent"],
            "entities": [],
            "traits": {}
        })

    response = requests.post(UTTERANCE_URL, headers=HEADERS, json=data)
    try:
        print(f"✅ Uploaded {os.path.basename(file)}: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"❌ Upload error for {file}: {e}")