from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine,create_async_engine

from secao06.core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncSession = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)