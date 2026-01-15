# backend/db/timescale.py
"""
TimescaleDB Integration

TimescaleDB 扩展集成，用于时序数据优化。

TimescaleDB 是 PostgreSQL 扩展，无需独立数据库。
支持:
- 自动时间分区 (hypertable)
- 连续聚合 (continuous aggregates)
- 数据保留策略 (retention policies)
- 压缩 (compression)

Usage:
    from backend.db.timescale import init_timescale, create_hypertable
    
    # 初始化 TimescaleDB
    await init_timescale()
    
    # 将表转为超表
    await create_hypertable('memory_events', 'created_at')
"""

import logging
from typing import Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.session import async_session_maker, engine

logger = logging.getLogger(__name__)


async def init_timescale() -> bool:
    """
    初始化 TimescaleDB 扩展
    
    Returns:
        是否成功初始化
    """
    try:
        async with engine.begin() as conn:
            # 创建扩展 (如果不存在)
            await conn.execute(text("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"))
            
            # 检查版本
            result = await conn.execute(text("SELECT extversion FROM pg_extension WHERE extname = 'timescaledb';"))
            row = result.fetchone()
            
            if row:
                logger.info(f"TimescaleDB initialized: version {row[0]}")
                return True
            else:
                logger.warning("TimescaleDB extension not available")
                return False
                
    except Exception as e:
        logger.error(f"Failed to initialize TimescaleDB: {e}")
        return False


async def create_hypertable(
    table_name: str,
    time_column: str = "created_at",
    chunk_interval: str = "7 days",
    if_not_exists: bool = True,
) -> bool:
    """
    将普通表转为超表 (hypertable)
    
    超表自动按时间分区，提升大规模时序数据查询性能。
    
    Args:
        table_name: 表名
        time_column: 时间列名
        chunk_interval: 分区间隔 (默认 7 天)
        if_not_exists: 如果已是超表则跳过
        
    Returns:
        是否成功
    """
    try:
        async with async_session_maker() as session:
            # 检查是否已是超表
            check_sql = text("""
                SELECT EXISTS (
                    SELECT 1 FROM timescaledb_information.hypertables 
                    WHERE hypertable_name = :table_name
                );
            """)
            result = await session.execute(check_sql, {"table_name": table_name})
            is_hypertable = result.scalar()
            
            if is_hypertable:
                if if_not_exists:
                    logger.info(f"Table {table_name} is already a hypertable, skipping")
                    return True
                else:
                    logger.warning(f"Table {table_name} is already a hypertable")
                    return False
            
            # 转为超表
            create_sql = text(f"""
                SELECT create_hypertable(
                    :table_name, 
                    :time_column,
                    chunk_time_interval => INTERVAL '{chunk_interval}',
                    if_not_exists => TRUE
                );
            """)
            await session.execute(create_sql, {
                "table_name": table_name,
                "time_column": time_column,
            })
            await session.commit()
            
            logger.info(f"Created hypertable: {table_name} (time_column={time_column}, interval={chunk_interval})")
            return True
            
    except Exception as e:
        logger.error(f"Failed to create hypertable {table_name}: {e}")
        return False


async def add_retention_policy(
    table_name: str,
    drop_after: str = "90 days",
) -> bool:
    """
    添加数据保留策略
    
    自动删除超过指定时间的旧数据。
    
    Args:
        table_name: 超表名
        drop_after: 保留时间 (默认 90 天)
        
    Returns:
        是否成功
    """
    try:
        async with async_session_maker() as session:
            sql = text(f"""
                SELECT add_retention_policy(
                    :table_name, 
                    INTERVAL '{drop_after}',
                    if_not_exists => TRUE
                );
            """)
            await session.execute(sql, {"table_name": table_name})
            await session.commit()
            
            logger.info(f"Added retention policy: {table_name} (drop_after={drop_after})")
            return True
            
    except Exception as e:
        logger.error(f"Failed to add retention policy for {table_name}: {e}")
        return False


async def enable_compression(
    table_name: str,
    segment_by: str = "user_id",
    order_by: str = "created_at DESC",
    compress_after: str = "7 days",
) -> bool:
    """
    启用自动压缩
    
    对旧数据进行压缩以节省存储空间。
    
    Args:
        table_name: 超表名
        segment_by: 分段列 (通常是 user_id)
        order_by: 排序列
        compress_after: 多久后压缩
        
    Returns:
        是否成功
    """
    try:
        async with async_session_maker() as session:
            # 设置压缩选项
            alter_sql = text(f"""
                ALTER TABLE {table_name} SET (
                    timescaledb.compress,
                    timescaledb.compress_segmentby = '{segment_by}',
                    timescaledb.compress_orderby = '{order_by}'
                );
            """)
            await session.execute(alter_sql)
            
            # 添加压缩策略
            policy_sql = text(f"""
                SELECT add_compression_policy(
                    :table_name,
                    INTERVAL '{compress_after}',
                    if_not_exists => TRUE
                );
            """)
            await session.execute(policy_sql, {"table_name": table_name})
            await session.commit()
            
            logger.info(f"Enabled compression: {table_name} (segment_by={segment_by}, after={compress_after})")
            return True
            
    except Exception as e:
        logger.error(f"Failed to enable compression for {table_name}: {e}")
        return False


async def setup_timescale_for_memory() -> dict:
    """
    为记忆层表配置 TimescaleDB
    
    配置:
    - memory_events: 7天分区，90天保留，7天后压缩
    - memory_insights: 30天分区，永久保留，30天后压缩
    
    Returns:
        配置结果报告
    """
    report = {
        "timescale_init": False,
        "memory_events": {"hypertable": False, "retention": False, "compression": False},
        "memory_insights": {"hypertable": False, "compression": False},
    }
    
    # 1. 初始化 TimescaleDB
    report["timescale_init"] = await init_timescale()
    if not report["timescale_init"]:
        logger.warning("TimescaleDB not available, skipping hypertable setup")
        return report
    
    # 2. memory_events - 事件表 (高频写入，短期保留)
    report["memory_events"]["hypertable"] = await create_hypertable(
        "memory_events", 
        "created_at",
        chunk_interval="7 days"
    )
    if report["memory_events"]["hypertable"]:
        report["memory_events"]["retention"] = await add_retention_policy(
            "memory_events",
            drop_after="90 days"
        )
        report["memory_events"]["compression"] = await enable_compression(
            "memory_events",
            segment_by="user_id",
            compress_after="7 days"
        )
    
    # 3. memory_insights - 洞察表 (低频写入，长期保留)
    report["memory_insights"]["hypertable"] = await create_hypertable(
        "memory_insights",
        "created_at", 
        chunk_interval="30 days"
    )
    if report["memory_insights"]["hypertable"]:
        # 洞察不设保留策略 (永久保留)
        report["memory_insights"]["compression"] = await enable_compression(
            "memory_insights",
            segment_by="user_id",
            compress_after="30 days"
        )
    
    logger.info(f"TimescaleDB setup complete: {report}")
    return report


# =============================================================================
# 便捷函数
# =============================================================================

async def is_timescale_available() -> bool:
    """检查 TimescaleDB 是否可用"""
    try:
        async with engine.begin() as conn:
            result = await conn.execute(text(
                "SELECT EXISTS (SELECT 1 FROM pg_extension WHERE extname = 'timescaledb');"
            ))
            return result.scalar() or False
    except Exception:
        return False
