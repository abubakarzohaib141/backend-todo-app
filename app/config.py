from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    app_name: str = "Todo App"
    debug: bool = False

    # Database
    database_url: str = "sqlite:///./todos.db"

    # JWT
    secret_key: str = Field(default="your-secret-key-change-this", alias="SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS
    cors_origins: list = ["http://localhost:3000", "http://localhost:8000"]

    class Config:
        env_file = ".env"
        case_sensitive = False
        populate_by_name = True


settings = Settings()
