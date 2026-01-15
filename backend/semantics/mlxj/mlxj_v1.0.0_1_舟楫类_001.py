"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.812652
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="mlxj_v1.0.0_1_舟楫类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1舟楫类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 宋 | 叶逢 | 乘船赴任入石窟 | 覆舟死 |
| 明 | 八扬王 ...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 宋 | 叶逢 | 乘船赴任入石窟 | 覆舟死 |
| 明 | 八扬王 | 百舟来载汝 | 获救归乡 |
| 明 | 车宁刘观 | 僚友并舟入广 | 并舟而还 |
| 明 | 孙本 | 登舟 | 中乡榜 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 舟楫类"
    factor_refs: list = ['source_ref']
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_舟楫类_001_L1",
    )
    version: str = "1.0.0"
