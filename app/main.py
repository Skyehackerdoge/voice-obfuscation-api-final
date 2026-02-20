from fastapi import FastAPI
from app.routers import obfuscation
from app.utils.logging import configure_logging

# Configure logging once when the app starts
configure_logging()

app = FastAPI(title="Voice Obfuscation API")

# Attach routes
app.include_router(obfuscation.router)
