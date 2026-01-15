"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224423
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
    semantic_id="pit_v1.0.0_sun_opposition_mars__流年太阳冲本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionMars流年太阳冲本命火星(SemanticEntry):
    """
    **Source Text** (Lines 2642-2674):
> Time of critical culminations—many activities come to climax. C...
    """
    
    original_text: str = """**Source Text** (Lines 2642-2674):
> Time of critical culminations—many activities come to climax. Clear whether you've conducted them skillfully. Mars-Sun transit most disruptive when ego energies operate unconsciously—blindly self-assertive, arouses opposition. Even under best circumstances, you will confront others—teammates or opponents. Any position or "ego-statement" will be sharpened, refined, or invalidated.
> 
> Whatever makes you angry today is something you've identified your ego with. Notice your anger and ask what it tells about your attitudes. Close personal relationships most likely to experience negative effects. Do not suppress hostility—can turn inward causing self-destructive behavior or illness.

**English Paraphrase**: Critical culminations—activities climax. Shows if you acted skillfully. Most disruptive if unconscious—arouses opposition. Will confront teammates or opponents. Positions sharpened or invalidated. Anger reveals ego identifications. Close relationships most affected. Don't suppress hostility—can cause illness.

**Complete Chinese Interpretation**: 关键顶点——活动达到高潮。显示你是否行动得当。如果无意识则最具破坏性——引起反对。将面对队友或对手。立场被强化或无效化。愤怒揭示自我认同。亲密关系最受影响。不要压抑敌意——可能导致疾病。

**Narrative Snippets**:
- `[ns_pit_089]` `[trigger: transit_sun_opposition_natal_mars]` `[factor_trigger: astro_transit_sun OPPOSITION natal_mars]` `[role: 主干]` Critical culminations—activities climax. Most disruptive if ego operates unconsciously. Will confront others. → PIT Ch4 Sun☍Mars
- `[ns_pit_090]` `[trigger: transit_sun_opposition_natal_mars]` `[factor_trigger: astro_transit_sun OPPOSITION natal_mars]` `[role: 条件分支]` Anger reveals ego identifications. Close relationships most affected. Don't suppress hostility—can cause illness. → PIT Ch4 Sun☍Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Mars (流年太阳冲本命火星)"
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
        l1_anchor="pit_v1.0.0_sun_opposition_mars__流年太阳冲本命火星_001_L1",
    )
    version: str = "1.0.0"
