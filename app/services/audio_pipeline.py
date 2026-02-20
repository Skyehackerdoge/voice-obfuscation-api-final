import librosa
import soundfile as sf
import logging
import time
from app.services.voice_transform import VoiceTransformer
from app.services.security import validate_duration
from app.config import settings

logger = logging.getLogger(__name__)

class AudioPipeline:

    def __init__(self):
        self.transformer = VoiceTransformer(settings.SAMPLE_RATE)

    def process(self, input_path: str, output_path: str):
        start_time = time.time()

        logger.info("Loading audio file")
        y, sr = librosa.load(input_path, sr=settings.SAMPLE_RATE)

        duration = len(y) / sr
        validate_duration(duration)
        logger.info(f"Duration: {duration:.2f} seconds")

        logger.info("Applying voice transformations")
        y_transformed = self.transformer.transform(y)

        logger.info("Saving processed audio")
        sf.write(output_path, y_transformed, sr)

        processing_time = time.time() - start_time
        logger.info(f"Processing took {processing_time:.2f} seconds")

