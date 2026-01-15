"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224408
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
    semantic_id="pit_v1.0.0_sun_trine_mars__流年太阳拱本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunTrineMars流年太阳拱本命火星(SemanticEntry):
    """
    **Source Text** (Lines 2618-2640):
> Today easy to be yourself. Should work alone and for your own b...
    """
    
    original_text: str = """**Source Text** (Lines 2618-2640):
> Today easy to be yourself. Should work alone and for your own benefit—not hostile, just don't want to be dependent on others. Physically vigorous—physical activity recommended for body, mind and spirit. Good time to take stock of projects, examine their state. What motivates you? In near future you'll have confrontations—understand what you're doing. Strive not only to be yourself, but to know who "yourself" is.

**English Paraphrase**: Easy to be yourself. Work alone for own benefit—no hostility, just independence. Physically vigorous—activity recommended. Take stock of projects. What motivates you? Confrontations coming—understand yourself. Be yourself AND astro_know who you are.

**Complete Chinese Interpretation**: 容易做自己。为自己利益独自工作——无敌意，只是独立。体力旺盛——推荐活动。盘点项目。什么激励你？即将面临对抗——理解自己。做自己并知道自己是谁。

**Narrative Snippets**:
- `[ns_pit_087]` `[trigger: transit_sun_trine_natal_mars]` `[factor_trigger: astro_transit_sun TRINE natal_mars]` `[role: 主干]` Easy to be yourself—work alone for own benefit, physically vigorous. Take stock of projects. → PIT Ch4 Sun△Mars
- `[ns_pit_088]` `[trigger: transit_sun_trine_natal_mars]` `[factor_trigger: astro_transit_sun TRINE natal_mars]` `[role: 总结]` Confrontations coming—understand what motivates you. Be yourself AND astro_know who you are. → PIT Ch4 Sun△Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Trine Mars (流年太阳拱本命火星)"
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
        l1_anchor="pit_v1.0.0_sun_trine_mars__流年太阳拱本命火星_001_L1",
    )
    version: str = "1.0.0"
