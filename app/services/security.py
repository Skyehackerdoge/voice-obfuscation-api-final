from app.config import settings

def validate_file_size(file_bytes: bytes):
    size_mb = len(file_bytes) / (1024 * 1024)
    if size_mb > settings.MAX_FILE_SIZE_MB:
        raise ValueError("File exceeds maximum size limit.")

def validate_duration(duration: float):
    if duration > settings.MAX_DURATION_SECONDS:
        raise ValueError("Audio exceeds maximum allowed duration.")
