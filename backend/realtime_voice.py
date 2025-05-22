import whisper
import requests
import os
import pyaudio
import wave
import pyttsx3
import uuid
from backend.intent.intent_router import route_intent, extract_spacy_entities

from backend.services.nlp import get_intent_from_wit

# Voice settings
SAMPLE_RATE = 16000
DURATION = 5  # seconds
AUDIO_FILENAME = "voice_input.wav"
session_id = f"session_{uuid.uuid4().hex[:8]}"

# TTS
def speak(text):
    print(f"🗣️ Chapo: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Record voice
def record_audio(filename=AUDIO_FILENAME, duration=DURATION, rate=SAMPLE_RATE):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=rate,
                    input=True,
                    frames_per_buffer=1024)
    print("🎤 Speak now...")
    frames = []
    for _ in range(0, int(rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    return filename

# Transcribe with Whisper
def transcribe_audio(file):
    model = whisper.load_model("base")
    result = model.transcribe(file)
    return result.get("text", "").strip()

# Real-time loop
def run_voice_assistant():
    print("🎙️ Real-time Voice Mode: Say 'exit' to stop.\n")
    while True:
        audio_path = record_audio()
        text = transcribe_audio(audio_path)

        if not text:
            print("❌ No speech detected.")
            continue

        if "exit" in text.lower():
            speak("Goodbye!")
            break

        print(f"🧠 You said: {text}")

        intent, confidence, wit_entities = get_intent_from_wit(text)

        # Normalize intent
        if intent and intent.startswith("wit$"):
            intent = intent.replace("wit$", "")

        response = route_intent(intent or "unknown", wit_entities, text, session_id)
        speak(response)

if __name__ == "__main__":
    run_voice_assistant()
