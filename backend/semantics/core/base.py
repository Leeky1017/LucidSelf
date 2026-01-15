"""
Semantic Layer Core - Base Classes

语义层核心基类。

对照架构文档:
- docs/ls_engine_architecture_v3.md §4.2 Layer 2: 语义知识层
- docs/数据契约_Schema定义规范_v1.md §1.1-1.5

核心类:
- SemanticEntry: 语义条目基类
- SemanticRegistry: 语义注册中心（单例）
- NarrativeSnippetExtended: 扩展叙事片段
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Dict, List, Optional, Set, Type, ClassVar

from pydantic import BaseModel, Field

from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
)

logger = logging.getLogger(__name__)


class SemanticEntry(BaseModel):
    """
    语义条目基类
    
    对照架构v3 §4.2:
    - 直接从典籍Markdown生成
    - 支持上下文敏感的含义查询
    - 作为Codegen产物的基类
    """
    # 基本标识
    original_text: str = Field(default="", description="原文")
    normalized_text_zh: str = Field(default="", description="标准化中文文本")
    normalized_text_en: Optional[str] = Field(default=None, description="标准化英文文本")
    
    # 主题与属性
    subject: str = Field(default="", description="主题")
    natural_attributes: Dict[str, Any] = Field(default_factory=dict)
    
    # 因子关联
    factor_refs: List[str] = Field(default_factory=list, description="关联因子ID列表")
    
    # 术语表
    terms: List[Dict[str, str]] = Field(default_factory=list)
    
    # 跨域引用
    cross_domain_refs: Dict[str, List[str]] = Field(default_factory=dict)
    
    # L2.5 扩展 (对照数据契约 §1.5)
    relations: List[ConfigRelation] = Field(default_factory=list)
    evidence_chains: List[EvidenceChainEntry] = Field(default_factory=list)
    
    def get_contextual_meaning(self, context: Dict[str, Any]) -> str:
        """
        根据上下文返回具体含义 (架构v3要求)
        
        Args:
            context: 上下文信息（因子值、用户偏好等）
            
        Returns:
            上下文相关的含义文本
        """
        return self.normalized_text_zh or self.original_text
    
    class Config:
        extra = "allow"  # 允许额外字段（Codegen生成的子类可能有更多字段）


class NarrativeSnippetExtended(BaseModel):
    """
    扩展叙事片段
    
    对照数据契约 §3.4 NarrativeSnippet
    """
    snippet_id: str = Field(default="", description="叙事片段ID")
    trigger_condition: str = Field(default="", description="触发条件")
    role: SnippetRole = Field(default=SnippetRole.MAIN, description="逻辑角色")
    snippet_text: str = Field(default="", description="片段文本")
    source_ref: str = Field(default="", description="来源引用")
    related_factors: List[str] = Field(default_factory=list)
    related_rules: List[str] = Field(default_factory=list)
    
    class Config:
        extra = "allow"


class SemanticRegistry:
    """
    语义注册中心 - 全局单例
    
    功能:
    - 按 semantic_id 查询
    - 按 book_id 批量查询
    - 按 factor_refs 查询关联语义
    - 支持 @register 装饰器自动注册
    
    对照架构v3 §4.2:
    - O(1) 按ID查找
    - 按因子索引支持RuleEngine查询
    """
    
    # 类变量 - 全局注册表
    _entries: ClassVar[Dict[str, SemanticEntry]] = {}
    _by_book: ClassVar[Dict[str, Set[str]]] = {}  # book_id -> set of semantic_ids
    _by_factor: ClassVar[Dict[str, Set[str]]] = {}  # factor_id -> set of semantic_ids
    _by_engine: ClassVar[Dict[str, Set[str]]] = {}  # engine_id -> set of semantic_ids
    _classes: ClassVar[Dict[str, Type[SemanticEntry]]] = {}  # semantic_id -> class
    
    @classmethod
    def register(
        cls,
        semantic_id: str,
        book_id: str,
        engine_id: str = "unknown",
    ) -> Callable[[Type[SemanticEntry]], Type[SemanticEntry]]:
        """
        装饰器: 注册语义条目类
        
        使用示例:
        ```python
        @SemanticRegistry.register(
            semantic_id="dts_v1_jia_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class JiaMuEntry(SemanticEntry):
            original_text = "甲木参天..."
        ```
        
        Args:
            semantic_id: 语义ID
            book_id: 书籍ID
            engine_id: 引擎ID
            
        Returns:
            装饰器函数
        """
        def decorator(entry_class: Type[SemanticEntry]) -> Type[SemanticEntry]:
            # 实例化并注册
            try:
                entry = entry_class()
            except Exception as e:
                logger.warning(f"Failed to instantiate {semantic_id}: {e}")
                entry = SemanticEntry()
            
            # 注册到主索引
            cls._entries[semantic_id] = entry
            cls._classes[semantic_id] = entry_class
            
            # 注册到 book_id 索引
            if book_id not in cls._by_book:
                cls._by_book[book_id] = set()
            cls._by_book[book_id].add(semantic_id)
            
            # 注册到 engine_id 索引
            if engine_id not in cls._by_engine:
                cls._by_engine[engine_id] = set()
            cls._by_engine[engine_id].add(semantic_id)
            
            # 注册到 factor_refs 索引
            for factor_id in entry.factor_refs:
                if factor_id not in cls._by_factor:
                    cls._by_factor[factor_id] = set()
                cls._by_factor[factor_id].add(semantic_id)
            
            return entry_class
        
        return decorator
    
    @classmethod
    def get(cls, semantic_id: str) -> Optional[SemanticEntry]:
        """
        按ID获取单个语义条目
        
        Args:
            semantic_id: 语义ID
            
        Returns:
            语义条目实例，不存在返回None
        """
        return cls._entries.get(semantic_id)
    
    @classmethod
    def get_class(cls, semantic_id: str) -> Optional[Type[SemanticEntry]]:
        """获取语义条目类"""
        return cls._classes.get(semantic_id)
    
    @classmethod
    def get_by_book(cls, book_id: str) -> List[SemanticEntry]:
        """
        获取某本书的全部语义条目
        
        Args:
            book_id: 书籍ID
            
        Returns:
            语义条目列表
        """
        ids = cls._by_book.get(book_id, set())
        return [cls._entries[sid] for sid in ids if sid in cls._entries]
    
    @classmethod
    def get_by_engine(cls, engine_id: str) -> List[SemanticEntry]:
        """
        获取某引擎的全部语义条目
        
        Args:
            engine_id: 引擎ID
            
        Returns:
            语义条目列表
        """
        ids = cls._by_engine.get(engine_id, set())
        return [cls._entries[sid] for sid in ids if sid in cls._entries]
    
    @classmethod
    def query_by_factors(cls, factor_ids: List[str]) -> List[SemanticEntry]:
        """
        按因子ID查询关联语义 (架构v3要求)
        
        Args:
            factor_ids: 因子ID列表
            
        Returns:
            关联的语义条目列表
        """
        result_ids: Set[str] = set()
        for fid in factor_ids:
            result_ids.update(cls._by_factor.get(fid, set()))
        return [cls._entries[sid] for sid in result_ids if sid in cls._entries]
    
    @classmethod
    def count(cls) -> int:
        """获取已注册语义条目总数"""
        return len(cls._entries)
    
    @classmethod
    def count_by_book(cls) -> Dict[str, int]:
        """获取按书籍分组的计数"""
        return {book_id: len(ids) for book_id, ids in cls._by_book.items()}
    
    @classmethod
    def count_by_engine(cls) -> Dict[str, int]:
        """获取按引擎分组的计数"""
        return {engine_id: len(ids) for engine_id, ids in cls._by_engine.items()}
    
    @classmethod
    def list_books(cls) -> List[str]:
        """列出所有已注册的书籍ID"""
        return list(cls._by_book.keys())
    
    @classmethod
    def list_engines(cls) -> List[str]:
        """列出所有已注册的引擎ID"""
        return list(cls._by_engine.keys())
    
    @classmethod
    def clear(cls) -> None:
        """清空注册表（仅用于测试）"""
        cls._entries.clear()
        cls._by_book.clear()
        cls._by_factor.clear()
        cls._by_engine.clear()
        cls._classes.clear()
