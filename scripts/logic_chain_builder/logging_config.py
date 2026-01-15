"""
Logging Configuration - 日志配置

为Logic Chain Builder提供统一的日志配置。
"""

import logging
import sys
from pathlib import Path
from typing import Optional


def setup_logging(
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    module_name: str = "logic_chain_builder"
) -> logging.Logger:
    """
    配置日志
    
    Args:
        level: 日志级别
        log_file: 日志文件路径（可选）
        module_name: 模块名称
    
    Returns:
        配置好的Logger实例
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(level)
    
    # 避免重复添加handler
    if logger.handlers:
        return logger
    
    # 格式化器
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # 控制台handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 文件handler（可选）
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def get_logger(name: str = "logic_chain_builder") -> logging.Logger:
    """
    获取Logger实例
    
    Args:
        name: Logger名称
    
    Returns:
        Logger实例
    """
    return logging.getLogger(name)


# 默认logger
logger = get_logger()
