import contextlib
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.conf.config import database_config


class DatabaseSessionManager:
    """Керує асинхронним підключенням і сесіями бази даних."""

    def __init__(self, database_url: str) -> None:
        self._engine: AsyncEngine = create_async_engine(database_url)
        self._session_factory: async_sessionmaker[AsyncSession] = (
            async_sessionmaker(
                bind=self._engine,
                autoflush=False,
                autocommit=False,
                expire_on_commit=False,
            )
        )

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        """Створює сесію та закриває її після завершення роботи."""

        if self._session_factory is None:
            raise RuntimeError("Session factory is not initialized")

        database_session = self._session_factory()

        try:
            yield database_session
        except Exception as error:
            print(error)
            await database_session.rollback()
            raise error
        finally:
            await database_session.close()


session_manager = DatabaseSessionManager(database_config.DATABASE_URL)


async def get_db() -> AsyncIterator[AsyncSession]:
    """Надає сесію бази даних як залежність FastAPI."""

    async with session_manager.session() as database_session:
        yield database_session