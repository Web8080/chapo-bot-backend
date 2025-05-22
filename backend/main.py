from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import voice, text, interactions
from backend.db.mongo import connect_db
import logging
from backend.api.shopping_list_routes import router as shopping_list_router


app = FastAPI(title="Chapo Bot Backend")

# Register the shopping list routes
app.include_router(shopping_list_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or set your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    try:
        connect_db()
        logging.info("✅ MongoDB connected.")
    except Exception as e:
        logging.error(f"❌ MongoDB startup error: {e}")

app.include_router(voice.router)
app.include_router(text.router)
app.include_router(interactions.router)