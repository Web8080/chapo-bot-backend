from fastapi import APIRouter, Body, HTTPException
from backend.services.text_handler import process_text_input
from starlette.status import HTTP_400_BAD_REQUEST

router = APIRouter(prefix="/text", tags=["Text Input"])

@router.post("/")
async def handle_text(user_input: str = Body(..., embed=True)):
    if not user_input.strip():
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Input text cannot be empty.")

    try:
        return await process_text_input(user_input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
