from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    app_name: str = "Todo App"
    debug: bool = False

    # Database
    database_url: str = "sqlite:///./todos.db"

    # JWT
    secret_key: str = "your-secret-key-change-this"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS
    cors_origins: list = ["http://localhost:3000", "http://localhost:8000"]

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
