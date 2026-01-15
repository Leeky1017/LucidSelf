"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301163
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
    semantic_id="pit_v1.0.0_moon_opposition_sun__流年月亮冲本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonOppositionSun流年月亮冲本命太阳(SemanticEntry):
    """
    **Source Text** (estimated from pattern):
> This is your personal "full Moon"—a time of culmination ...
    """
    
    original_text: str = """**Source Text** (estimated from pattern):
> This is your personal "full Moon"—a time of culmination and maximum tension between conscious will and emotional needs. Events reveal how well you've integrated these two sides of yourself. May feel pulled in two directions—duty vs personal needs. Relations with others, especially opposite sex, may be strained. This is a time of maximum awareness—use it to see yourself clearly. What you've been building reaches a test point.

**English Paraphrase**: Personal "full Moon"—culmination, tension between will and emotions. Events reveal integration level. Pulled in two directions—duty vs needs. Relations may be strained. Maximum awareness—see yourself clearly. Test point for what you've built.

**Complete Chinese Interpretation**: 个人"满月"——顶点，意志与情感之间的紧张。事件揭示整合水平。被拉向两个方向——责任vs需求。关系可能紧张。最大意识——清楚地看到自己。你建立的东西的测试点。

**Narrative Snippets**:
- `[ns_pit_m030]` `[trigger: transit_moon_opposition_natal_sun]` `[factor_trigger: astro_transit_moon OPPOSITION natal_sun]` `[role: 主干]` Personal "full Moon"—culmination, tension between conscious will and emotional needs. → PIT Ch5 Moon☍Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Opposition Sun (流年月亮冲本命太阳)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_moon_opposition_sun__流年月亮冲本命太阳_001_L1",
    )
    version: str = "1.0.0"
