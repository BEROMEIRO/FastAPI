from typing import List
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://gabriel:romeirosato@127.0.0.1:5432/faculdade3"
    DBBaseModel = declarative_base

    JWT_SECRET: str = ''
    '''
    import secrets
    token: str = secrets.token_urlsafe(32)
    '''
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


    class Config:
        case_sensitive = True


settings: Settings = Settings()

