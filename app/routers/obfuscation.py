import os
import uuid
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import logging

from app.services.audio_pipeline import AudioPipeline
from app.services.security import validate_file_size
from app.utils.audio_validation import validate_content_type

router = APIRouter()
pipeline = AudioPipeline()

TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.post("/obfuscate")
async def obfuscate_audio(file: UploadFile = File(...)):

    try:
        validate_content_type(file.content_type)

        contents = await file.read()
        validate_file_size(contents)

        input_path = TEMP_DIR / f"{uuid.uuid4()}.wav"
        output_path = TEMP_DIR / f"{uuid.uuid4()}_obfuscated.wav"

        with open(input_path, "wb") as f:
            f.write(contents)

        pipeline.process(str(input_path), str(output_path))

        os.remove(input_path)

        return FileResponse(
            path=str(output_path),
            media_type="audio/wav",
            filename="obfuscated.wav"
        )

    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))
