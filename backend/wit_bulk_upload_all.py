# create_wit_intents.py

import os
import glob
import pandas as pd
import requests

ACCESS_TOKEN = "KMTQWKBOXWTGAWTRKLUH6UGGY4HJHYX6"
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
INTENT_URL = "https://api.wit.ai/intents?v=20230204"
batch_folder = "batches"
csv_files = sorted(glob.glob(os.path.join(batch_folder, "*.csv")))

all_intents = set()

for file in csv_files:
    df = pd.read_csv(file)
    if 'intent' in df.columns:
        all_intents.update(df['intent'].dropna().unique())

for intent in sorted(all_intents):
    payload = { "name": intent }
    response = requests.post(INTENT_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"✅ Created intent: {intent}")
    elif "already exists" in response.text:
        print(f"🔁 Intent exists: {intent}")
    else:
        print(f"❌ Failed to create intent: {intent} => {response.text}")
