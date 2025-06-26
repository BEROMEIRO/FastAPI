# Pega informações do banco de dados
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

# Isso parece uma Classe, por isso o nome começa com letra maiúscula
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

