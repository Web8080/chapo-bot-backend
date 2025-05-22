import os
import glob
import pandas as pd
import requests
import json
from difflib import SequenceMatcher

# ✅ Your Wit.ai Server Access Token
ACCESS_TOKEN = "SSMMM332R3XF3LMATF5LZ55QEU33NYL4"

# ✅ Headers and API URLs
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
INTENT_URL = "https://api.wit.ai/intents?v=20230204"
UTTERANCE_URL = "https://api.wit.ai/utterances?v=20230204"
ENTITY_URL = "https://api.wit.ai/entities?v=20230204"

# ✅ Path to your CSV files
batch_folder = "new_batch"
csv_files = sorted(glob.glob(os.path.join(batch_folder, "*.csv")))

# 🧠 Track created intents and entities to avoid duplication
created_intents = set()
created_entities = set()

# 🔍 Helper: fuzzy match threshold
def fuzzy_match(value, text, threshold=0.8):
    best_match = None
    best_ratio = 0
    value_lower = value.lower()
    text_lower = text.lower()
    for i in range(len(text) - len(value) + 1):
        window = text_lower[i:i+len(value)]
        ratio = SequenceMatcher(None, value_lower, window).ratio()
        if ratio > best_ratio and ratio >= threshold:
            best_ratio = ratio
            best_match = (i, i + len(value))
    return best_match

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

    # 🧠 Extract and create unique entities
    for entity_json in df['entities']:
        try:
            parsed = json.loads(entity_json)
            for entity in parsed:
                if entity not in created_entities:
                    # ✅ FIXED: Proper payload for entity creation
                    res = requests.post(ENTITY_URL, headers=HEADERS,
                                        json={"name": entity, "roles": [{"name": entity}]})
                    if res.status_code == 200:
                        print(f"✅ Created entity: {entity}")
                    elif "already exists" in res.text:
                        print(f"🔁 Entity exists: {entity}")
                    else:
                        print(f"❌ Failed to create entity {entity}: {res.text}")
                    created_entities.add(entity)
        except Exception as e:
            print(f"⚠️ Failed to parse entity JSON: {entity_json} → {e}")

    # 🗣 Upload utterances with valid or fallback entity labels
    for i, row in df.iterrows():
        text = row.get("uttrance", row.get("text", "")).strip()
        intent = row["intent"].strip()
        entity_str = row.get("entities", "{}")

        if not text:
            print(f"⚠️ Skipping empty text on row {i+1}")
            continue

        try:
            parsed_entities = json.loads(entity_str)
            entities = []
            for key, value in parsed_entities.items():
                value_str = str(value).strip()
                match = fuzzy_match(value_str, text)
                if match:
                    start, end = match
                    entities.append({
                        "entity": key,
                        "value": value_str,
                        "start": start,
                        "end": end,
                        "body": text[start:end]
                    })
                else:
                    print(f"⚠️ '{value_str}' not found (even fuzzily) in \"{text}\" for entity '{key}' — will upload without it")
        except Exception as e:
            print(f"⚠️ Failed to parse entities on row {i+1}: {e}")
            entities = []

        utterance = {
            "text": text,
            "intent": intent,
            "entities": entities,
            "traits": {}
        }

        res = requests.post(UTTERANCE_URL, headers=HEADERS, json=[utterance])
        if res.status_code == 200:
            print(f"✅ Uploaded {i+1}: \"{text}\"")
        else:
            print(f"❌ Failed {i+1}: {res.status_code} - {res.text}")
