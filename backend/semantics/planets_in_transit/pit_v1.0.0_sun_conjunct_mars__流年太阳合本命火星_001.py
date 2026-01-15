"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224377
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
    semantic_id="pit_v1.0.0_sun_conjunct_mars__流年太阳合本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctMars流年太阳合本命火星(SemanticEntry):
    """
    **Source Text** (Lines 2537-2563):
> Excellent day for starting new projects, especially working alo...
    """
    
    original_text: str = """**Source Text** (Lines 2537-2563):
> Excellent day for starting new projects, especially working alone without taking orders. Feel vigorous—high physical energy—really need to be physically active. Worst way: work quietly at desk—become itchy and irritable. Must identify with what you do—ego energies high—demand recognition as individual. If not recognized, become angry and involved in disputes. This energy can be used for creative expression. Watch for accidents—inflammations, infections, fevers. Be careful of sharp objects and machinery.

**English Paraphrase**: Excellent for new projects, especially solo work. High physical energy—must be active. Desk work = itchy and irritable. Need recognition; if denied, anger and disputes. Energy for creative expression. Watch accidents—inflammations, fevers. Careful with sharp objects.

**Complete Chinese Interpretation**: 对新项目极好，尤其是独自工作。高体力能量——必须活跃。桌面工作=烦躁不安。需要认可；如被拒绝，愤怒和争执。能量用于创意表达。注意事故——炎症、发烧。小心锋利物品。

**Narrative Snippets**:
- `[ns_pit_082]` `[trigger: transit_sun_conjunct_natal_mars]` `[factor_trigger: astro_transit_sun CONJUNCT natal_mars]` `[role: 主干]` Excellent for starting new projects—high physical energy, must be active. Ego energies demand recognition. → PIT Ch4 Sun☌Mars
- `[ns_pit_083]` `[trigger: transit_sun_conjunct_natal_mars]` `[factor_trigger: astro_transit_sun CONJUNCT natal_mars]` `[role: 条件分支]` If not recognized: anger and disputes. Watch accidents—inflammations, fevers. Careful with sharp objects. → PIT Ch4 Sun☌Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Mars (流年太阳合本命火星)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_mars__流年太阳合本命火星_001_L1",
    )
    version: str = "1.0.0"
