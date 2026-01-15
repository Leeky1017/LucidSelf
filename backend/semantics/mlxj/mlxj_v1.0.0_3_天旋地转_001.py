"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793422
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
    semantic_id="mlxj_v1.0.0_3_天旋地转_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3天旋地转(SemanticEntry):
    """
    #### 原文（source_text）

天旋地转吉。天运回，地候返，人事新也。此为气运交亨之兆。文人梦之指日登云步月，平人梦之利于营谋作事，日攺业迁图。

#### 规范化释义（primary_l...
    """
    
    original_text: str = """#### 原文（source_text）

天旋地转吉。天运回，地候返，人事新也。此为气运交亨之兆。文人梦之指日登云步月，平人梦之利于营谋作事，日攺业迁图。

#### 规范化释义（primary_lang_explained）

梦见天旋地转，吉。天运回转，地候更替，人事更新。此为气运交亨之兆。文人梦此，主指日可登云步月（功名将至）；平人梦此，利于营谋作事，主改业迁移。

#### 核心要点

- **梦象**：天旋地转
- **吉凶**：吉
- **象义**：气运交亨、人事更新
- **人群分占**：文人主功名；平人主改业迁图"""
    normalized_text_zh: str = """"""
    subject: str = "3 天旋地转"
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
        l1_anchor="mlxj_v1.0.0_3_天旋地转_001_L1",
    )
    version: str = "1.0.0"
