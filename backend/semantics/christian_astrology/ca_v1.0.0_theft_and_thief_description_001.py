"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147496
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
    semantic_id="ca_v1.0.0_theft_and_thief_description_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class TheftAndThiefDescription(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 7th House | Fur/Thief | House of the thief | Thief significator |
| Lord of 7th | Dominus 7 | Ruler of 7th house | Thief's description |
| 2nd House | Substantia | Querent's goods | Stolen property |
| Peregrine planet | Peregrinus | Planet without dignity | Thief indicator |

**Source Text** (Synthesized from Lilly Book II, pp. 319-366):
> Of Theft: The 7th house and his Lord signifies the Thief. The 2nd house signifies the thing stolen. A Peregrine Planet in an angle, especially in the Ascendant or 7th, often describes the Thief. Consider the Lord of the 7th his sign, house, and aspects for description of Thief. Fire signs = ruddy complexion; Earth = swarthy; Air = fair; Water = pale.

**English Paraphrase (Primary Language)**:

**Theft Questions** use specific significator assignments:

| Element | Significator |
|---------|--------------|
| Thief | 7th house + L7 |
| Stolen goods | 2nd house + L2 |
| Thief description | L7 sign, house, aspects |
| Recovery | Moon applying to L2 |

**Physical Description by Element**:
| Sign Element | Complexion |
|--------------|------------|
| Fire (Aries, Leo, Sagittarius) | Ruddy, red |
| Earth (Taurus, Virgo, Capricorn) | Swarthy, dark |
| Air (Gemini, Libra, Aquarius) | Fair, light |
| Water (Cancer, Scorpio, Pisces) | Pale, watery |

**完整中文诠释**：盗窃问题使用特定象征星分配。盗贼=第7宫+L7；失物=第2宫+L2；盗贼描述=L7星座/宫位/相位；找回=月亮趋近L2。元素描述面貌：火象（白羊/狮子/射手）=红润；土象（金牛/处女/摩羯）=黝黑；风象（双子/天秤/水瓶）=白皙；水象（巨蟹/天蝎/双鱼）=苍白。

#### Core Points

- **Thief = 7th house**: Open enemy in theft context
- **Peregrine planet**: Often indicates thief (homeless = vagrant)
- **Elemental complexion**: Sign element describes appearance
- **Recovery**: Moon-L2 application shows return

**Narrative Snippets**:
- `[ns_lilly_theft_001]` `[trigger: thief_significator]` `[factor_trigger: L7_thief AND astro_thief_significator]` `[role: 主干]` The 7th house and its Lord signifies the Thief. Peregrine planet in angle often describes thief. → Christian Astrology Theft
- `[ns_lilly_theft_002]` `[trigger: thief_description]` `[factor_trigger: L7_sign_element AND astro_thief_appearance]` `[role: 主干依赖]` Fire signs = ruddy; Earth = swarthy; Air = fair; Water = pale complexion. → Christian Astrology Theft
- `[ns_lilly_theft_003]` `[trigger: recovery_indicator]` `[factor_trigger: Moon_L2_apply AND astro_goods_recovery]` `[role: 条件分支]` Moon applying to L2 or dispositor of L2 = goods shall be recovered. → Christian Astrology Theft

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Theft horary was major practice in Lilly's time. He accurately predicted thief characteristics in documented cases. The peregrine planet technique is unique to horary. Modern ethics questions using astrology to identify thieves.
- **中文**: 盗窃卜卦在Lilly时代是主要实践。他在记录案例中准确预测盗贼特征。游魂行星技术是卜卦独有。现代伦理对用占星识别盗贼有疑问。"""
    normalized_text_zh: str = """"""
    subject: str = "Theft and Thief Description"
    factor_refs: list = ['thief_significator', 'elemental_complexion', 'peregrine_thief']
    
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
        l1_anchor="ca_v1.0.0_theft_and_thief_description_001_L1",
    )
    version: str = "1.0.0"
