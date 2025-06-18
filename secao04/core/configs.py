# Configurações gerais do projeto
from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

# usuário: gabriel senha: romeirosato

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://gabriel:romeirosato@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()