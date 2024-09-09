from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, \
    async_sessionmaker

from app.constants.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


class DBConnection:

    def __init__(self):
        self.engine = create_async_engine(
            url=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@"
            f"{DB_HOST}:{DB_PORT}/{DB_NAME}",
            echo=True
        )
        self.async_session_maker = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session_maker() as session:
            yield session
