"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147382
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
    semantic_id="ca_v1.0.0_5d__fourth_house_questions___p_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class 5dFourthHouseQuestionsP(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 4th House | Imum Coeli (IC) | House of father, land, endings | Property and inheritance |
| Lord of 4th | Dominus 4 | Ruler of 4th house cusp | Father/property significator |
| End of matter | Finis rei | Outcome of any question | 4th shows conclusions |

**Source Text** (Synthesized from Lilly Book II, Ch. 4):
> Of buying and selling Lands, Houses, Farms: The 4th house signifies the Land or House itself; its Lord shows the quality thereof. If L4 be well dignified, the purchase is good; if afflicted or in Cadent house, there are hidden defects. To find a thing hid or mislaid: Consider the 4th house and its Lord, also the Moon. The sign on 4th cusp describes the place; L4 position shows where it lies.

**English Paraphrase (Primary Language)**:

**Fourth House Questions** address father, real estate, hidden things, and endings:

| Question Type | Judgment Method |
|---------------|-----------------|
| Should I buy property? | L4 dignified = good property; L4 afflicted = defects |
| Is father well? | L4 condition shows father's state |
| Where is hidden thing? | 4th sign = place type; L4 position = specific location |
| What is the end? | 4th house condition shows final outcome |

**完整中文诠释**：第四宫问题涉及父亲、不动产、隐藏物和结局。买房产：L4有尊贵=好房产；L4受克=有缺陷。父亲状况：L4状态显示父亲状态。隐藏物位置：4宫星座=地点类型；L4位置=具体位置。结局：4宫状态显示最终结果。

#### Core Points

- **Property questions**: L4 dignity indicates property quality
- **Father questions**: L4 condition shows father's wellbeing
- **Hidden things**: 4th sign describes location type
- **Endings**: 4th house shows final outcome of any matter

**Narrative Snippets**:
- `[ns_lilly_4th_001]` `[trigger: property_quality]` `[factor_trigger: L4_dignity AND astro_property_quality]` `[role: 主干]` L4 well dignified = good purchase; L4 afflicted = hidden defects in property. → Christian Astrology 4th House
- `[ns_lilly_4th_002]` `[trigger: hidden_location]` `[factor_trigger: 4th_sign AND astro_hidden_location]` `[role: 主干依赖]` Sign on 4th cusp describes the place; L4 position shows where the hidden thing lies. → Christian Astrology 4th House"""
    normalized_text_zh: str = """"""
    subject: str = "5D. Fourth House Questions – Parents, Property, Hidden Things"
    factor_refs: list = ['property_question', 'hidden_thing', 'end_of_matter']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_5d__fourth_house_questions___p_001_L1",
    )
    version: str = "1.0.0"
