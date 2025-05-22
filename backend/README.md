 README.md for Chapo Bot 
# 🤖 Chapo Bot - Voice-Controlled Home Assistant

Chapo is an intelligent, voice-controlled home assistant designed for real-time interaction, environmental awareness, and personalized response generation. Built with Whisper, GPT, Wit.ai, and modular intent engines, Chapo aims to become a fully autonomous and emotionally-aware smart companion.

---

## 📦 Features

### ✅ Core Features (Implemented)
- 🎙️ Real-time voice recognition with Whisper
- 🧠 Intent detection using Wit.ai and HuggingFace
- 🤖 GPT fallback for open-ended queries
- 😊 Emotion detection via facial expression analysis
- 📊 MongoDB logging for all user interactions and metrics
- 🛍️ Shopping list handler with persistent JSON storage

### 🔧 Planned Integrations
- 🏠 IoT device control via Home Assistant
- 📅 Google Calendar API for reminders & events
- 🗺️ Google Maps API for location-based queries
- 🎵 Spotify integration (currently broken)
- 👁️ YOLOv8 for real-time object detection
- 📈 Streamlit dashboard for real-time insights

---

## 🧠 System Architecture

```mermaid
graph TD
    UserVoice[🎤 User Voice Input]
    Whisper[🧠 Whisper STT]
    Wit[🔍 Wit.ai Intent Detection]
    GPT[🤖 GPT Fallback]
    Router[🛠️ Intent Router]
    Engines[⚙️ Chapo Engines]
    DB[🗂️ MongoDB Logs]
    Camera[📸 Real-time Vision]
    Emotion[😊 Emotion Detector]

    UserVoice --> Whisper
    Whisper --> Wit
    Wit --> Router
    Router --> Engines
    Router --> GPT
    Engines --> DB
    Camera --> Emotion
    Emotion --> Router

🧰 Tech Stack
Category	Technology
Language	Python 3.10+
Backend	FastAPI
NLP	Whisper, Wit.ai, OpenAI GPT, HuggingFace
Voice I/O	PyAudio, gTTS, pyttsx3
Data Storage	MongoDB, JSON
Vision	OpenCV, YOLOv8, ONNX
Dashboard (planned)	Streamlit, Dash, Flask
Dev Tools	dotenv, logging, asyncio
📂 Folder Structure
backend/
├── app.py / main.py                  # Entry points for running the FastAPI app (if web/API interface is enabled)
├── test_voice.py                     # 🎙️ Main voice loop: handles input, transcription, intent detection, response
├── realtime_voice.py                 # Handles streaming or continuous voice capture
├── response_generator.py             # 🧠 Generates dynamic responses using multi-turn logic or GPT fallback
├── emotion_detector.py               # 😊 Detects user emotion from speech or facial cues
├── realtime_emotion_detect.py        # Real-time webcam-based emotion recognition using FER
├── realtime_object_detect.py         # Real-time object detection using YOLOv8 + OpenCV
├── spotify_handler.py                # Spotify helper functions (auth, playback), used in integration
├── feedback.py                       # Collects and logs user feedback on responses
├── multi_turn_manager.py             # Tracks context for multi-turn conversations
├── evaluate_model.py / eval_metrics.py # 📊 Evaluate accuracy of intent predictions (Wit.ai / HuggingFace)
├── db/mongo.py                            # Connects to MongoDB, stores logs & evaluation metrics
├── download_yolo_files.py            # Downloads YOLO model weights and files
├── requirements.txt                  # List of Python dependencies

# ✅ NLP / Wit.ai Integration
├── wit_bulk_upload.py                # Uploads multiple intents/utterances to Wit.ai
├── wit_upload_csv_style.py           # Uploads utterances from CSV-formatted structure
├── wit.ai_upload_new.py              # Alternative Wit.ai uploader script

# 📁 Routers
├── routers/
│   ├── voice.py                      # Handles API routes for voice commands
│   ├── text.py                       # Handles routes for text queries
│   ├── interactions.py               # Route logic for interactions with users or modules

# 🧠 Intelligence Engines (modular)
├── chapo_engines/
│   ├── core_conversation_engine.py   # Central dispatch logic to other engines
│   ├── reminder_engine.py            # Reminders, alarms, scheduling
│   ├── shopping_list_engine.py       # JSON-based shopping list manager
│   ├── fitness_engine.py             # Fitness prompts, suggestions, logs
│   ├── knowledge_engine.py           # Trivia, facts, and question answering
│   ├── wellness_engine.py            # Mood check-ins, journaling, meditation
│   ├── gp_engine.py                  # Health data interaction engine
│   ├── sleep_engine.py               # Sleep routines or logging
│   ├── entertainment_engine.py       # Music, games, storytelling
│   ├── security_engine.py            # Home surveillance or threat detection
│   ├── tv_engine.py                  # Smart TV control or suggestions
│   └── ... (20+ total engines)       # Each handling a narrow, modular domain

# 🧾 JSON Data Logs & Training Files
├── session_logs.json                # Stores all conversation sessions
├── feedback_logs.json               # Records user thumbs-up/down feedback
├── shopping_list.json               # 🛒 Persistent local shopping list store
├── trivia_questions.json            # Dataset of trivia questions
├── utterance_to_response.json       # Maps common utterances to canned replies
├── intent_to_utterances.json        # Maps intents to example phrases for training
├── gp_reports.json / training.json  # Medical report storage or dummy data
├── medication_schedule.json         # Medication reminders and logs
├── witai_utterances_formatted.json  # Formatted data for Wit.ai bulk training
|---- alarms.json

# ⚙️ Model Weights
├── yolov8n.pt                       # YOLOv8 object detection model
├── yolov5su.pt                      # Alternative or older YOLOv5 model
├── imagenet_classes.txt             # Object labels for model predictions

# 🔈 Audio & Media
├── test.wav                         # Example user input
├── voice_input.wav                  # Temporary raw recording
├── cat.png                          # Test image for visual functions

# 🔬 Evaluation & Logging
├── eval_log.csv / eval_log_new.csv # Logs of model evaluation metrics

🚀 Getting Started
🔧 Installation
# Clone the repository
git clone https://github.com/yourusername/chapo-bot.git
cd chapo-bot/backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

🔑 Environment Variables
Create a .env file in the backend/ directory with the following:
MONGODB_URI=your_mongodb_connection_string
WIT_AI_TOKEN=your_wit_ai_token
OPENAI_API_KEY=your_openai_key

🗣️ Usage
python test_voice.py
Speak to Chapo and receive intelligent, emotional, or GPT-based responses with intent-aware functionality.

📈 Roadmap
* Add Home Assistant integration
* Google Calendar support for reminders/events
* Reactivate and stabilize Spotify module
* Improve fallback routing from GPT → core logic
* Add persistent JSON storage for tasks/alarms
* Create a visual dashboard using Streamlit/Dash
* Enhance object recognition via camera input

🧠 Challenges Faced
* ❗ Asynchronous race conditions with shopping list updates
* ❗ Overlapping intents in multi-action commands (e.g., “Add milk and remind me tomorrow”)
* ❗ Spotify authentication & token refresh bugs
* ❗ GPT fallback generating good responses but not triggering actions
* ❗ Lack of visual UI made debugging interaction flows slow
* ❗ Natural language date/time parsing for reminders was unreliable

🧪 Testing
To evaluate intent prediction accuracy:
python evaluate_model.py
Check eval_metrics.py for metrics such as precision, recall, and F1-score.

🧙 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

🪪 License
MIT © 2025 — Islington Robotica Team

---
