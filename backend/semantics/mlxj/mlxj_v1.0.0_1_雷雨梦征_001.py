"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.783957
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
    semantic_id="mlxj_v1.0.0_1_雷雨梦征_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1雷雨梦征(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 齐 | 窦母 | 雷电耀目 | 生泰 |
| 宋 | 宗母 | 雷电烛...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 齐 | 窦母 | 雷电耀目 | 生泰 |
| 宋 | 宗母 | 雷电烛身 | 生泽 |
| - | 某人 | 雨中戴帽 | 未沾一命 |
| - | 某人 | 江上逢雷 | 膺百里宰 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 雷雨梦征"
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
        l1_anchor="mlxj_v1.0.0_1_雷雨梦征_001_L1",
    )
    version: str = "1.0.0"
