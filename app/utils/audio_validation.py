def validate_content_type(content_type: str):
    if content_type not in ["audio/wav", "audio/mpeg"]:
        raise ValueError("Unsupported audio format. Only WAV and MP3 allowed.")
