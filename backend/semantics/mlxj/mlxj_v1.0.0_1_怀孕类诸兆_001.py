"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.801352
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
    semantic_id="mlxj_v1.0.0_1_怀孕类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1怀孕类诸兆(SemanticEntry):
    """
    #### 原文摘要

气从胎中生，胎从伏气中得，阳气动，动极而静，静而生阴。巽、离、兑，其胎为女；阴气静，静极而动，动而生阳。震、坎、艮，其胎为男。阳气生木，木属肝，肝主血，血主于胎而为女；会气生水，...
    """
    
    original_text: str = """#### 原文摘要

气从胎中生，胎从伏气中得，阳气动，动极而静，静而生阴。巽、离、兑，其胎为女；阴气静，静极而动，动而生阳。震、坎、艮，其胎为男。阳气生木，木属肝，肝主血，血主于胎而为女；会气生水，水属肾，肾主精，精主于胎而为男。阴阳合闭而生金，金属肺，肺主气，气会而成胎。怀胎四千九百刻，而分娩。

#### 怀孕梦象汇总

**吉类**：
- 梦妇怀孕：主有财
- 梦见妊妇：主事成
- 张司直典故：梦身怀孕，壬辰日愈

**凶类**：
- 梦妻孕：主外私

#### 胎象与八卦对应

| 八卦 | 阴阳 | 胎性 |
|------|------|------|
| 巽离兑 | 阳极生阴 | 女胎 |
| 震坎艮 | 阴极生阳 | 男胎 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 怀孕类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_怀孕类诸兆_001_L1",
    )
    version: str = "1.0.0"
