"""Configuration."""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ENVIRONMENT: str = "production"
    LOG_LEVEL: str = "INFO"
    OPENAI_API_KEY: str
    DATABASE_URL: str = "postgresql://user:pass@localhost/rag_db"
    REDIS_URL: str = "redis://localhost:6379"
    PINECONE_API_KEY: str = ""
    MAX_CHUNK_SIZE: int = 1024
    CACHE_TTL_MINUTES: int = 60
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()