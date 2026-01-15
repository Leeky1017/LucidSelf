"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162827
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
    semantic_id="tb_v1.0.0_quality_and_nature_of_the_effe_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class QualityAndNatureOfTheEffe(SemanticEntry):
    """
    **Source Text** (Lines 3700-3800):
> The quality of the predicted event is to be understood from the...
    """
    
    original_text: str = """**Source Text** (Lines 3700-3800):
> The quality of the predicted event is to be understood from the properties of those planets which bear chief dominion over the places of the eclipse and the angles... Saturn causes destruction by cold, long illnesses, consumption, decay; Jupiter causes abundance, peace, prosperity, honors; Mars causes wars, seditions, drought, fevers, murders; Venus causes plenty, fertility, pleasures; Mercury causes seditions, robberies, failures of commerce.

**English Paraphrase (Primary Language)**:
The **nature of eclipse effects** is determined by the planets dominating the eclipse:

| Planet | Effects |
|--------|---------|
| Saturn | Cold destruction, long illness, consumption, decay, poverty, exile |
| Jupiter | Abundance, peace, prosperity, honors, fertility |
| Mars | Wars, seditions, drought, fevers, sudden deaths, murders |
| Venus | Plenty, fertility, pleasures, prosperity, good marriages |
| Mercury | Seditions, robberies, commerce failures, religious disputes |

Multiple planets blend their effects. Benefics mitigate; malefics intensify harm. The sign's nature (hot/cold, human/animal) further modifies outcomes.

**Complete Chinese Interpretation (Secondary Language)**:
**日食效应的性质**由主宰日食的行星决定：

| 行星 | 效应 |
|------|------|
| 土星 | 寒冷破坏、长期疾病、消耗、衰败、贫困、流放 |
| 木星 | 丰富、和平、繁荣、荣誉、生育力 |
| 火星 | 战争、叛乱、干旱、发烧、突然死亡、谋杀 |
| 金星 | 丰饶、生育力、快乐、繁荣、美满婚姻 |
| 水星 | 叛乱、抢劫、商业失败、宗教争端 |

**Core Points**:
- Saturn = cold destruction, illness, poverty
- Jupiter = abundance, peace, prosperity
- Mars = war, drought, sudden death
- Venus = fertility, pleasure, prosperity
- Mercury = sedition, commerce problems
- Multiple planets blend effects

**Narrative Snippets**:
- `[ns_tetra_ii007]` `[trigger: eclipse_effect_nature]` `[factor_trigger: astro_planet_eclipse_ruler]` `[role: 主干]` Eclipse effects depend on ruling planet: Saturn=destruction, Jupiter=prosperity, Mars=war, Venus=fertility, Mercury=sedition. → Source Text II.9
- `[ns_tetra_ii021]` `[trigger: saturn_mundane]` `[factor_trigger: astro_saturn AND astro_mundane]` `[role: 条件分支]` Saturn causes destruction by cold, long illnesses, consumption, decay, poverty, and exile. → Saturn
- `[ns_tetra_ii022]` `[trigger: mars_mundane]` `[factor_trigger: astro_mars AND astro_mundane]` `[role: 条件分支]` Mars causes wars, seditions, drought, fevers, sudden deaths, and murders. → Mars
- `[ns_tetra_ii_sm]` `[trigger: saturn_mundane]` `[factor_trigger: saturn_mundane]` `[role: 条件分支]` Saturn mundane effects: destruction by cold, long illnesses, consumption, decay, poverty, exile, and death of the elderly. → Source Text II.9
- `[ns_tetra_ii_ee]` `[trigger: eclipse_effect]` `[factor_trigger: eclipse_effect]` `[role: 效果]` Eclipse effect nature determined by ruling planet: Saturn=destruction, Jupiter=prosperity, Mars=war, Venus=fertility, Mercury=sedition. → Source Text II.9"""
    normalized_text_zh: str = """"""
    subject: str = "Quality and Nature of the Effect (Chapter IX)"
    factor_refs: list = ['eclipse_ruler_effects']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_quality_and_nature_of_the_effe_001_L1",
    )
    version: str = "1.0.0"
