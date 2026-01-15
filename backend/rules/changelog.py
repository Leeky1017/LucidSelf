"""
Rule Change Logger

规则变更日志记录器。

对照 Task 23.4: Implement RuleChangeLogger
对照 Requirement 15.10
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class RuleChangeLogger:
    """
    规则变更日志记录器
    
    记录所有规则的创建、更新、删除操作。
    """
    
    DEFAULT_LOG_PATH = Path("data/rules/rule_change_log.jsonl")
    
    def __init__(self, log_path: Optional[Path] = None):
        """初始化日志记录器"""
        self.log_path = Path(log_path or self.DEFAULT_LOG_PATH)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
    
    def log_change(
        self,
        action: str,
        rule_id: str,
        system: str,
        details: Optional[Dict[str, Any]] = None,
        user: Optional[str] = None,
    ) -> None:
        """
        记录规则变更
        
        Args:
            action: 操作类型 (create, update, delete, status_change)
            rule_id: 规则 ID
            system: 体系名称
            details: 变更详情
            user: 操作用户
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "rule_id": rule_id,
            "system": system,
            "details": details or {},
            "user": user or "system",
        }
        
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        
        logger.info(f"Rule change logged: {action} {rule_id}")
    
    def log_create(
        self,
        rule_id: str,
        system: str,
        version: str = "1.0.0",
        user: Optional[str] = None,
    ) -> None:
        """记录规则创建"""
        self.log_change(
            action="create",
            rule_id=rule_id,
            system=system,
            details={"version": version},
            user=user,
        )
    
    def log_update(
        self,
        rule_id: str,
        system: str,
        old_version: str,
        new_version: str,
        changes: Optional[List[str]] = None,
        user: Optional[str] = None,
    ) -> None:
        """记录规则更新"""
        self.log_change(
            action="update",
            rule_id=rule_id,
            system=system,
            details={
                "old_version": old_version,
                "new_version": new_version,
                "changes": changes or [],
            },
            user=user,
        )
    
    def log_status_change(
        self,
        rule_id: str,
        system: str,
        old_status: str,
        new_status: str,
        user: Optional[str] = None,
    ) -> None:
        """记录规则状态变更"""
        self.log_change(
            action="status_change",
            rule_id=rule_id,
            system=system,
            details={
                "old_status": old_status,
                "new_status": new_status,
            },
            user=user,
        )
    
    def log_delete(
        self,
        rule_id: str,
        system: str,
        reason: Optional[str] = None,
        user: Optional[str] = None,
    ) -> None:
        """记录规则删除"""
        self.log_change(
            action="delete",
            rule_id=rule_id,
            system=system,
            details={"reason": reason},
            user=user,
        )
    
    def get_history(
        self,
        rule_id: Optional[str] = None,
        system: Optional[str] = None,
        action: Optional[str] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """
        获取变更历史
        
        Args:
            rule_id: 过滤规则 ID
            system: 过滤体系
            action: 过滤操作类型
            limit: 最大返回数量
        
        Returns:
            变更记录列表
        """
        if not self.log_path.exists():
            return []
        
        entries = []
        with open(self.log_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    entry = json.loads(line)
                    
                    # 过滤
                    if rule_id and entry.get("rule_id") != rule_id:
                        continue
                    if system and entry.get("system") != system:
                        continue
                    if action and entry.get("action") != action:
                        continue
                    
                    entries.append(entry)
                except json.JSONDecodeError:
                    continue
        
        # 按时间倒序
        entries.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        
        return entries[:limit]


# 单例实例
_logger: Optional[RuleChangeLogger] = None


def get_change_logger() -> RuleChangeLogger:
    """获取变更日志记录器单例"""
    global _logger
    if _logger is None:
        _logger = RuleChangeLogger()
    return _logger
