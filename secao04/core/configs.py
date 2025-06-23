# Configurações gerais do projeto
from typing import ClassVar
from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

# usuário: gabriel senha: romeirosato
# faculdade: banco de dados


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://gabriel:romeirosato@127.0.0.1:5432/faculdade"

    DBBaseModel: ClassVar = declarative_base()
    
    class Config:
        case_sensitive = True

settings = Settings()