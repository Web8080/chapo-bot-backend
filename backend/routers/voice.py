from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.voice_handler import process_voice_file
from starlette.status import HTTP_400_BAD_REQUEST
import logging

router = APIRouter(prefix="/voice", tags=["Voice Input"])

@router.post("/")
async def handle_voice(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".mp3", ".wav", ".m4a")):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Unsupported file format. Please upload .mp3, .wav, or .m4a."
        )
    try:
        logging.info(f"📥 Received voice file: {file.filename}")
        return await process_voice_file(file)
    except Exception as e:
        logging.error(f"❌ Error in /voice/: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
