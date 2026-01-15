"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850628
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
    semantic_id="mlxj_v1.0.0_条目十一_梦无昼夜_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目十一梦无昼夜(SemanticEntry):
    """
    ### 原文（source_text）

梦无昼夜，必有吉凶。凡人觉而兴也形役，寐而寝也神游。形有兴寝，神有敛触，敛则无梦，触则梦成。古今一昼夜也，昼夜一息也，固有辨乎形神，必无分于昼夜。占梦者勿异视...
    """
    
    original_text: str = """### 原文（source_text）

梦无昼夜，必有吉凶。凡人觉而兴也形役，寐而寝也神游。形有兴寝，神有敛触，敛则无梦，触则梦成。古今一昼夜也，昼夜一息也，固有辨乎形神，必无分于昼夜。占梦者勿异视焉。

### 规范化释义（primary_lang_explained）

占梦的第十一条核心原则是「梦无昼夜」——梦不分白天黑夜，都有吉凶之兆。

人醒着时，形体被役使；睡着时，精神在游走。形体有醒与睡的区别，精神有收敛与触发的区别：收敛则无梦，触发则成梦。

从古至今昼夜循环是一体的，昼夜之间不过一息之隔。虽然形神有分别，但昼夜并无本质差异。占梦者不应区别对待白天的梦与夜晚的梦。

### 核心要点

- 梦无昼夜是占梦第十一核心原则
- 昼梦夜梦皆有吉凶
- 形有兴寝，神有敛触
- 敛则无梦，触则梦成
- 昼夜无分，不可异视

### 叙事素材（narrative_snippets）

- `[ns_mlxj_027]` `[trigger: 梦境时间]` `[factor_trigger: dream_time_of_day]` `[role: 否定因素]` 梦无昼夜，必有吉凶。占梦者勿异视焉。 → 《梦林玄解·卷之首》#梦无昼夜"""
    normalized_text_zh: str = """"""
    subject: str = "条目十一：梦无昼夜"
    factor_refs: list = []
    
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
        l1_anchor="mlxj_v1.0.0_条目十一_梦无昼夜_001_L1",
    )
    version: str = "1.0.0"
