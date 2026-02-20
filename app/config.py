from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Voice Obfuscation API"
    MAX_FILE_SIZE_MB: int = 25
    SAMPLE_RATE: int = 16000
    MAX_DURATION_SECONDS: int = 600

    class Config:
        env_file = ".env"

settings = Settings()
