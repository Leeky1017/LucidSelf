"""
LucidSelf API Main Application

FastAPI 应用入口。

对照 design.md 2.5, tasks.md 13.2:
- Requirements: 6.3.4
"""

# 在最开始加载环境变量
from pathlib import Path
from dotenv import load_dotenv

# 优先加载 backend/.env，其次根目录 .env
backend_env = Path(__file__).parent.parent / ".env"
root_env = Path(__file__).parent.parent.parent / ".env"
if backend_env.exists():
    load_dotenv(backend_env)
elif root_env.exists():
    load_dotenv(root_env)
else:
    load_dotenv()  # 默认行为

import logging
import os
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import (
    health_router,
    metrics_router,
    analyze_router,
    interpret_router,
    playbook_router,
    dream_router,
    user_router,
    timeline_router,
    patterns_router,
    insights_router,
    geocoding_router,
    auth_router,
    todo_router,
    subscription_router,
    scheduler_router,
)
from backend.api.middleware.metrics import MetricsMiddleware
from backend.api.middleware.request_logging import RequestLoggingMiddleware
from backend.core.boot.checks import get_boot_requirements, run_boot_checks
from backend.core.audit import create_audit_event, write_audit_event_async

logger = logging.getLogger(__name__)

# 版本信息
VERSION = os.getenv("APP_VERSION", "1.0.0")
API_TITLE = "LucidSelf API"
API_DESCRIPTION = """
LucidSelf 命理分析 API

## 功能

- **分析** (`/analyze`): 综合命理分析
- **解读** (`/interpret`): 生成叙事解读
- **健康检查** (`/health`, `/ready`, `/live`)

## 认证

使用 `X-API-Key` header 进行认证。

## 限流

- 全局: 100 请求/秒
- 用户: 10 请求/秒
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # Startup
    logger.info("LucidSelf API starting up...")
    logger.info(f"Version: {VERSION}")

    # Bootability hard checks (fail-fast in strict mode)
    requirements = get_boot_requirements()
    ready, checks, startup_checks = await run_boot_checks(requirements=requirements)
    if not ready:
        logger.warning("Boot checks failed: %s", checks)
        try:
            await write_audit_event_async(
                create_audit_event(
                    event_type="STARTUP_CHECK",
                    result="BLOCK",
                    capability="bootability-and-regression-baseline",
                    rejection_reason_code="STARTUP_CHECK_FAILED",
                    summary="boot checks failed",
                )
            )
        except Exception:
            pass
        if requirements.strict_boot:
            raise RuntimeError("Boot checks failed (STRICT_BOOT=true)")
    
    # 初始化数据库
    try:
        from backend.db.session import init_db, close_db
        await init_db()
        logger.info("Database initialized")
    except Exception as e:
        logger.warning(f"Database init failed (will use in-memory): {e}")
    
    # 初始化调度器
    try:
        from backend.scheduler import init_scheduler, register_all_jobs
        from backend.scheduler.base import start_scheduler
        init_scheduler()
        register_all_jobs()
        start_scheduler()
        logger.info("Scheduler initialized and started")
    except Exception as e:
        logger.warning(f"Scheduler init failed: {e}")
    
    yield
    
    # Shutdown
    logger.info("LucidSelf API shutting down...")
    
    # 关闭调度器
    try:
        from backend.scheduler import shutdown_scheduler
        shutdown_scheduler()
    except Exception:
        pass
    
    # 关闭数据库
    try:
        from backend.db.session import close_db
        await close_db()
    except Exception:
        pass


def create_app(
    debug: bool = False,
    enable_auth: bool = True,
    enable_rate_limit: bool = True,
) -> FastAPI:
    """
    创建 FastAPI 应用
    
    Args:
        debug: 调试模式
        enable_auth: 启用认证
        enable_rate_limit: 启用限流
        
    Returns:
        FastAPI 应用实例
    """
    app = FastAPI(
        title=API_TITLE,
        description=API_DESCRIPTION,
        version=VERSION,
        lifespan=lifespan,
        debug=debug,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    
    # CORS 配置
    # 开发模式下允许任意 localhost 端口
    cors_origins = os.getenv("CORS_ORIGINS", "*").split(",")
    allow_origin_regex = None
    if debug or os.getenv("CORS_ALLOW_LOCALHOST", "true").lower() == "true":
        # 匹配 http://localhost:任意端口 和 http://127.0.0.1:任意端口
        allow_origin_regex = r"https?://(localhost|127\.0\.0\.1)(:\d+)?"
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins if not allow_origin_regex else [],
        allow_origin_regex=allow_origin_regex,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # 限流中间件 (可选)
    if enable_rate_limit:
        from backend.api.middleware.rate_limit import RateLimitMiddleware
        app.add_middleware(RateLimitMiddleware, rate=100.0, capacity=200.0)

    # 请求日志中间件（放在限流外层，确保 4xx/429 等也可关联到 request_id/trace_id）
    app.add_middleware(RequestLoggingMiddleware)

    # 指标中间件（最外层，覆盖所有请求路径）
    app.add_middleware(MetricsMiddleware)
    
    # 认证中间件 (可选)
    # 注: 对于细粒度控制，建议在路由中使用 Depends(api_key_auth)
    # if enable_auth:
    #     from backend.api.middleware.auth import AuthMiddleware
    #     app.add_middleware(AuthMiddleware)
    
    # 注册路由
    app.include_router(health_router)
    app.include_router(metrics_router)
    app.include_router(analyze_router, prefix="/api/v1")
    app.include_router(interpret_router, prefix="/api/v1")
    app.include_router(playbook_router, prefix="/api/v1")
    app.include_router(dream_router, prefix="/api/v1")
    app.include_router(user_router, prefix="/api/v1")
    app.include_router(timeline_router, prefix="/api/v1")
    app.include_router(patterns_router, prefix="/api/v1")
    app.include_router(insights_router, prefix="/api/v1")
    app.include_router(geocoding_router, prefix="/api/v1")
    app.include_router(auth_router, prefix="/api/v1")
    app.include_router(todo_router, prefix="/api/v1")
    app.include_router(subscription_router, prefix="/api/v1")
    app.include_router(scheduler_router, prefix="/api/v1")
    
    # 根路由
    @app.get("/", tags=["Root"])
    async def root():
        return {
            "name": API_TITLE,
            "version": VERSION,
            "docs": "/docs",
        }
    
    return app


# 默认应用实例
app = create_app(
    debug=os.getenv("DEBUG", "false").lower() == "true",
    enable_auth=os.getenv("ENABLE_AUTH", "true").lower() == "true",
    enable_rate_limit=os.getenv("ENABLE_RATE_LIMIT", "true").lower() == "true",
)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "backend.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
