"""
R-09: Alembic 环境配置
WP-08: 数据库迁移基础设施
P1-2: 支持任意目录执行
"""

import os
import sys
from pathlib import Path
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# P1-2: 基于 env.py 位置计算项目根路径并注入 sys.path
# env.py 位于 backend/alembic/env.py，项目根在 ../..
_env_file = Path(__file__).resolve()
_project_root = _env_file.parents[2]  # /home/.../LucidSelf
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

# Alembic Config 对象
config = context.config

# 日志配置
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# P1-2: 使用 importlib 直接加载 base.py 模块，绕过 db/__init__.py
# 避免触发 session.py 的引擎创建
import importlib.util
_base_path = _project_root / "backend" / "db" / "base.py"
_spec = importlib.util.spec_from_file_location("backend_db_base", _base_path)
_base_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base_module)
Base = _base_module.Base

# 导入模型模块以注册 SQLAlchemy models（同样绕过 __init__.py）
_memory_path = _project_root / "backend" / "models" / "memory.py"
if _memory_path.exists():
    _spec2 = importlib.util.spec_from_file_location("backend_models_memory", _memory_path)
    _memory_module = importlib.util.module_from_spec(_spec2)
    try:
        _spec2.loader.exec_module(_memory_module)
    except Exception:
        pass  # 模型可能依赖其他模块，但 Base.metadata 已包含已定义的表

target_metadata = Base.metadata


def get_url():
    """从环境变量获取数据库 URL"""
    return os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://localhost:5432/lucidself"
    )


def run_migrations_offline() -> None:
    """
    离线模式运行迁移
    
    不需要数据库连接，只生成 SQL 脚本。
    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    在线模式运行迁移
    
    需要数据库连接。
    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
