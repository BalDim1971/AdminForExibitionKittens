from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker,
                                    AsyncSession, AsyncAttrs)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///kittens.sqlite'
engine = create_async_engine(url=SQLALCHEMY_DATABASE_URL)
SessionLocal = async_sessionmaker(engine, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(),
                                                 onupdate=func.now())
