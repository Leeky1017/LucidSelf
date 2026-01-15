"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192803
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
    semantic_id="tb_v1.0.0_hurts__injuries__and_diseases__001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class HurtsInjuriesAndDiseases(SemanticEntry):
    """
    **Source Text** (Lines 6376-6567):
> For the investigation of these circumstances, the two angles on...
    """
    
    original_text: str = """**Source Text** (Lines 6376-6567):
> For the investigation of these circumstances, the two angles on the horizon, both the ascendant and the western, must in all cases be remarked... if both the malefics, or even if one of them, should be stationed bodily on any of the successive degrees composing the said angles, or be configurated with such degrees in quartile or in opposition, some bodily disorders or injuries will attach to the native.

**English Paraphrase (Primary Language)**:
**Bodily afflictions** are indicated by:
- **Malefics on angles** (especially ASC/DSC and 6th house)
- **Malefics in quartile/opposition to angles**
- **Luminaries angularly posited with malefics**

**Planetary body rulerships**:
- Saturn: Right ear, spleen, bladder, phlegm, bones
- Jupiter: Hand, lungs, arteries, seed
- Mars: Left ear, kidneys, veins, privities
- Sun: Eyes, brain, heart, nerves, right side
- Venus: Nostrils, liver, flesh
- Mercury: Speech, understanding, bile, tongue
- Moon: Palate, throat, stomach, belly, womb, left side

**Saturn diseases**: Cold, consumption, rheumatism, decay, dropsy
**Mars diseases**: Fevers, wounds, hemorrhage, inflammation, burns
**Benefics mitigate**: Jupiter through human aid (wealth); Venus through divine aid (oracles)

**Complete Chinese Interpretation (Secondary Language)**:
**身体疾病**由以下指示：
- **凶星在角宫**（尤其是上升/下降和第6宫）
- **凶星与角宫四分/对分**
- **发光体与凶星角宫配置**

**行星身体主宰**：
- 土星：右耳、脾、膀胱、痰、骨骼
- 木星：手、肺、动脉、精液
- 火星：左耳、肾、静脉、私处
- 太阳：眼、脑、心、神经、右侧
- 金星：鼻孔、肝、肉
- 水星：言语、理解、胆汁、舌
- 月亮：上颚、喉、胃、腹、子宫、左侧

**Core Points**:
- Malefics on ASC/DSC/6th = bodily afflictions
- Each planet rules specific body parts
- Saturn = cold diseases; Mars = hot diseases
- Occidental malefics = disease; Oriental = injury
- Benefics in elevation mitigate afflictions

**Narrative Snippets**:
- `[ns_tetra_iii019]` `[trigger: bodily_disease]` `[factor_trigger: astro_malefic_angular]` `[role: 主干]` Bodily diseases arise when malefics occupy or aspect the horizon angles. → Source Text III.17
- `[ns_tetra_iii020]` `[trigger: body_rulership]` `[factor_trigger: astro_planet_body_part]` `[role: 条件分支]` Each planet rules specific body parts—Saturn bones, Mars blood, Mercury speech, etc. → Source Text III.17
- `[ns_tetra_iii_ba]` `[trigger: bodily_affliction]` `[factor_trigger: bodily_affliction]` `[role: 效果]` Bodily affliction (disease, injury, defect) indicated by malefics on or aspecting horizon angles—severity depends on malefic nature. → Source Text III.17"""
    normalized_text_zh: str = """"""
    subject: str = "Hurts, Injuries, and Diseases of the Body (Chapter XVII)"
    factor_refs: list = ['bodily_affliction']
    
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
        l1_anchor="tb_v1.0.0_hurts__injuries__and_diseases__001_L1",
    )
    version: str = "1.0.0"
