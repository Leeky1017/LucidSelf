"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224398
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
    semantic_id="pit_v1.0.0_sun_square_mars__流年太阳刑本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSquareMars流年太阳刑本命火星(SemanticEntry):
    """
    **Source Text** (Lines 2585-2617):
> Must be very conscious of yourself and motivations. Likely to h...
    """
    
    original_text: str = """**Source Text** (Lines 2585-2617):
> Must be very conscious of yourself and motivations. Likely to have serious ego conflicts. Tests validity of positions taken six months ago. Circumstances and people will look for chinks in your armor. Energy level high—perhaps too high. Watch irritable impatience when things don't go as planned. Be assertive only when situation calls for it. Watch baseless conflicts—effects may be projected. Be particularly careful of conflicts with authorities. Frustrated energies can lead to illness or accidents.

**English Paraphrase**: Be conscious of motivations—likely ego conflicts. Tests positions from six months ago. Others seek flaws. High energy—watch impatience. Assert only when necessary. Conflicts may be projected. Careful with authorities. Frustrated energy → illness/accidents.

**Complete Chinese Interpretation**: 意识到动机——可能有自我冲突。测试六个月前的立场。他人寻找缺陷。高能量——注意不耐烦。只在必要时主张。冲突可能被投射。小心与权威的冲突。受挫能量→疾病/事故。

**Narrative Snippets**:
- `[ns_pit_085]` `[trigger: transit_sun_square_natal_mars]` `[factor_trigger: astro_transit_sun SQUARE natal_mars]` `[role: 主干]` Be conscious of motivations—ego conflicts likely. Tests positions from six months ago. High energy. → PIT Ch4 Sun□Mars
- `[ns_pit_086]` `[trigger: transit_sun_square_natal_mars]` `[factor_trigger: astro_transit_sun SQUARE natal_mars]` `[role: 条件分支]` Assert only when necessary. Careful with authorities. Frustrated energy can lead to illness or accidents. → PIT Ch4 Sun□Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Square Mars (流年太阳刑本命火星)"
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
        l1_anchor="pit_v1.0.0_sun_square_mars__流年太阳刑本命火星_001_L1",
    )
    version: str = "1.0.0"
