"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224464
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
    semantic_id="pit_v1.0.0_sun_trine_jupiter__流年太阳拱本命木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunTrineJupiter流年太阳拱本命木星(SemanticEntry):
    """
    **Source Text** (Lines 2754-2765):
> According to tradition and modern experience, one of the most p...
    """
    
    original_text: str = """**Source Text** (Lines 2754-2765):
> According to tradition and modern experience, one of the most positive transits. Unless powerful negative influence, assures good feelings, peace and harmony with others. But you should use energy to accomplish something good—temptation is to enjoy good feelings and let day slip by. Can indicate lazy feelings, but to sleep through it would be a waste. Enthusiasm, optimism and buoyancy will enable you to project energies that help your affairs work out.

**English Paraphrase**: One of most positive transits—good feelings, peace, harmony. Use energy to accomplish something. Temptation: enjoy and let day slip by. Can be lazy but sleeping through it is waste. Enthusiasm and optimism help affairs work out.

**Complete Chinese Interpretation**: 最积极的行运之一——美好感觉、平和、和谐。用能量完成事情。诱惑：享受并让一天溜走。可能懒惰但睡过去是浪费。热情和乐观帮助事务顺利。

**Narrative Snippets**:
- `[ns_pit_096]` `[trigger: transit_sun_trine_natal_jupiter]` `[factor_trigger: astro_transit_sun TRINE natal_jupiter]` `[role: 主干]` One of most positive transits—good feelings, peace, harmony. Use energy to accomplish something. → PIT Ch4 Sun△Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Trine Jupiter (流年太阳拱本命木星)"
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
        l1_anchor="pit_v1.0.0_sun_trine_jupiter__流年太阳拱本命木星_001_L1",
    )
    version: str = "1.0.0"
