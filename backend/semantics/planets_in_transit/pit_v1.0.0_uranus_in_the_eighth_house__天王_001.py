"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206811
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
    semantic_id="pit_v1.0.0_uranus_in_the_eighth_house__天王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheEighthHouse天王(SemanticEntry):
    """
    **Source Text** (Lines 14664-14699):
> Gradually aware of powerful subconscious forces bringing grea...
    """
    
    original_text: str = """**Source Text** (Lines 14664-14699):
> Gradually aware of powerful subconscious forces bringing great changes. Changes not gradual but sudden unexpected events of intense, fateful quality. Old order passing away, new one coming. Someone may die connected with past life—signal to begin new era. Restrictions become intolerable—forced to break away. What was gradual evolution must become revolution. Also house of joint finances and shared resources—unexpected events. Partner's income may change suddenly. Wise to avoid becoming dependent on anyone else's money. May become impatient with duties of sharing property or debt—trying to break away could cause trouble. Ninth can indicate new sexual relationship quite different from any before—don't count on it lasting. Avoid new long-range commitments. Even existing relationships must change.

**English Paraphrase**: Subconscious forces bring sudden intense changes. Old order passing. May signal death of someone connected to past. Restrictions intolerable—break away. Joint finances/resources unstable. Avoid dependence on others' money. New sexual relationship possible but may not last. Avoid long-term commitments.

**Complete Chinese Interpretation**: 潜意识力量带来突然的强烈变化。旧秩序消逝。可能预示与过去有关的人死亡。限制变得无法忍受——挣脱。共同财务/资源不稳定。避免依赖他人的钱。可能有新的性关系但可能不会持久。避免长期承诺。

**Narrative Snippets**:
- `[ns_pit_ur008]` `[trigger: uranus_transit_house_8]` `[factor_trigger: astro_transit_uranus AND astro_house_8]` `[role: 主干]` Sudden intense changes. Old order passing. Joint finances unstable. Avoid long-term commitments. → PIT Ch11 Uranus-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Eighth House (天王星过境第八宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_eighth_house__天王_001_L1",
    )
    version: str = "1.0.0"
