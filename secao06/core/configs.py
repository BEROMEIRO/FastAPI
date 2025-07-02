from typing import List
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://gabriel:romeirosato@127.0.0.1:5432/faculdade3"
