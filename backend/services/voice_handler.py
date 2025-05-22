import whisper
import os
import tempfile
import logging
from fastapi import UploadFile
from backend.services.nlp import get_intent_from_wit
from backend.intent.intent_router import route_intent
from backend.db.mongo import save_interaction
from datetime import datetime

# Load Whisper model once at module level
whisper_model = whisper.load_model("base")

async def process_voice_file(file: UploadFile):
    try:
        # Save uploaded audio to temp file
        suffix = os.path.splitext(file.filename)[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        logging.info(f"🎤 Received voice file: {file.filename}")

        # Transcribe with Whisper
        result = whisper_model.transcribe(tmp_path, language='en')
        transcribed_text = result['text'].strip()

        logging.info(f"📝 Transcribed: {transcribed_text}")

        # Query Wit.ai
        intent, confidence, entities = get_intent_from_wit(transcribed_text)

        # Fallback or route based on intent
        if not intent or confidence < 0.75:
            response = "🤖 I'm not sure how to respond to that. Could you rephrase?"
        else:
            response = route_intent(intent, entities, user_input=transcribed_text)

        # Log interaction
        log = {
            "input": transcribed_text,
            "intent": intent,
            "confidence": confidence,
            "entities": entities,
            "response": response,
            "source": "voice",
            "timestamp": datetime.utcnow()
        }
        save_interaction(log)

        return log

    except Exception as e:
        logging.error(f"Voice processing failed: {e}")
        return {
            "input": "",
            "intent": "error",
            "response": f"Voice processing error: {str(e)}"
        }
