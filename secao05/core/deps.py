# São as dependências do projeto, que serão injetadas nas classes
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from core.database import Session

# Depois do -> retorna um generator assíncrono
# AsyncGenerator é um tipo de generator assíncrono
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()