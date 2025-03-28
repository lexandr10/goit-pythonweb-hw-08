from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    DB_URL: str = "postgres+asyncpg://postgres:alexandrenko2707@localhost:5432/contacts_db"

    model_config = ConfigDict( env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore")


settings = Settings()