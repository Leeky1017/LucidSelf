"""
Database Session

异步数据库连接和会话管理。
"""

import logging
import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from backend.db.base import Base

logger = logging.getLogger(__name__)

# 数据库URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://lucidself:lucidself_dev_password@localhost:5432/lucidself"
)

# 如果是同步URL，转换为异步
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# 创建异步引擎
engine = create_async_engine(
    DATABASE_URL,
    echo=os.getenv("DEBUG", "false").lower() == "true",
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
)

# 创建异步会话工厂
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    获取数据库会话（依赖注入）
    
    Usage:
        @router.get("/items")
        async def get_items(db: AsyncSession = Depends(get_db)):
            ...
    """
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db() -> None:
    """初始化数据库（创建表）"""
    async with engine.begin() as conn:
        # 导入所有模型以确保它们被注册
        from backend.models import auth, dream, user  # noqa: F401
        
        # 创建所有表
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Database tables created (including auth tables)")


async def close_db() -> None:
    """关闭数据库连接"""
    await engine.dispose()
    logger.info("Database connection closed")
