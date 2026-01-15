"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044574
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
    semantic_id="bot_v1.0.0_atu_iii__the_empress__皇后_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuIiiTheEmpress皇后(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Daleth (ד) | Hebrew letter "Door" | Gateway of manifestation |
| Venus | Planet of love/beauty | Creative fertility |
| Salt (Alchemy) | Passive stabilizing principle | Requires Sulphur activation |
| Pelican | Self-sacrificing bird | Maternal love symbol |

**Source Text**:
> "This card is attributed to the letter Daleth, which means a Door... It is impossible to summarize the meanings of the symbol of the Woman... She combines the highest spiritual with the lowest material qualities. For this reason, she is fitted to represent one of the three alchemical forms of energy, Salt... She represents a woman with the imperial crown and vestments, seated upon a throne... In her right hand she bears the lotus of Isis... About her, for a girdle, is the Zodiac." (Book of Thoth, The Empress)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Daleth (ד, value 4) - "Door"
- **Path**: Connects Chokmah (Wisdom) to Binah (Understanding) - The 14th Path
- **Planet**: Venus ♀
- **Element**: Earth
- **Alchemical**: Salt (the passive principle requiring activation)

**English Paraphrase**:
The Empress is the archetype of **Creative Manifestation** and **Fertile Love**, representing Venus in her full maternal power. Unlike the virginal High Priestess who embodies pure potential, the Empress is the **Mother actively creating**—pregnant, abundant, and nurturing. The **Door** (Daleth) symbolizes the gateway through which spirit becomes matter, the threshold of manifestation. She sits enthroned in lush nature, crowned and robed in imperial splendor, holding the **Lotus of Isis** (the Holy Grail sanctified by solar energy). Around her waist is the Zodiac, indicating her dominion over the cycle of time and seasons. The **Pelican** (feeding young with her own blood) represents self-sacrificing love and the continuity of life. The **White Eagle** corresponds to the alchemical White Tincture (lunar, silver). She is alchemical **Salt**—the passive, stable substance that must be energized by Sulphur (the Emperor) to maintain cosmic equilibrium.

**完整中文诠释**:
皇后（The Empress）是**创造性显化**与**多产之爱**的原型，代表着金星（Venus）在其完整母性力量中的展现。与体现纯粹潜能的童贞女祭司不同，皇后是**主动创造的母亲**——孕育、丰盛、滋养。**门**（Daleth）象征着灵性转化为物质的门户，显化的门槛。她端坐于郁郁葱葱的自然之中，头戴王冠、身披帝王华服，手持**伊西斯之莲**（Lotus of Isis，被太阳能量圣化的圣杯）。她腰间环绕着黄道十二宫，表明她掌管着时间与季节的循环。**鹈鹕**（Pelican，以自己的血喂养幼雏）代表着自我牺牲的爱以及生命的延续性。**白鹰**（White Eagle）对应着炼金术中的白色药剂（月性、银质）。她是炼金术中的**盐**（Salt）——被动的、稳定的物质，必须被硫磺（Sulphur，即皇帝）激活才能维持宇宙的平衡。

**Core Points**:
- **Manifestation Gateway**: The Door (Daleth) through which spirit enters matter
- **Fertile Creation**: Active maternal love bringing forth tangible forms
- **Alchemical Salt**: Passive principle requiring Sulphur (Emperor) for activation
- **Universal Love**: Venus as the fundamental formula of the universe

**Detailed Explanation**:
The Empress path connects Chokmah (Father/Wisdom) to Binah (Mother/Understanding), completing the Supernal Triangle. Her alchemical symbol of Venus uniquely encompasses all ten Sephiroth on the Tree of Life, indicating love as the cosmic binding force. The symbols on her robe—bees (industry, sweetness), dominos (fate/games), spirals (continuous generation)—all point to creative abundance. The fleurs-de-lys and fishes at her feet adore the Secret Rose (womb, center of creation). She is both Isis (highest spiritual) and the material earth, demonstrating that the sacred and profane are one.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: The Empress represents Venus in full maternal power, distinct from the virginal Priestess. Daleth (Door) indicates spirit entering matter. She is alchemical Salt requiring Emperor's Sulphur. Harris depicts abundance through nature imagery, pelican, and Zodiac belt.
- **中文**: 皇后代表金星完整母性力量，与童贞女祭司不同。Daleth（门）表示灵进入物质。她是炼金术的盐，需要皇帝的硫磺。Harris通过自然意象、鹈鹐和黄道带描绘丰盛。

**Narrative Snippets**:
- `[ns_thoth_039]` `[trigger: empress_door_manifestation]` `[factor_trigger: tarot_daleth AND tarot_manifestation]` `[role: 主干]` Daleth, the Door, marks the gateway where formless spirit enters matter—the Empress as portal of manifestation. → English Paraphrase
- `[ns_thoth_040]` `[trigger: empress_venus_mother]` `[factor_trigger: tarot_empress AND tarot_venus]` `[role: 主干依赖]` The Empress is Venus in full maternal power—creative love that conceives, nurtures, and beautifies the world. → English Paraphrase
- `[ns_thoth_041]` `[trigger: pelican_maternal_love]` `[factor_trigger: tarot_pelican AND tarot_sacrifice]` `[role: 主干依赖]` The pelican feeding her young with her own blood symbolizes self‑sacrificing maternal love and continuity of life. → English Paraphrase
- `[ns_thoth_042]` `[trigger: alchemical_salt]` `[factor_trigger: tarot_salt AND tarot_alchemy]` `[role: 总结]` Alchemically, the Empress is Salt—the passive, stable substance that must be energized by the Emperor’s Sulphur to sustain cosmic balance. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU III: The Empress (皇后)"
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_atu_iii__the_empress__皇后_001_L1",
    )
    version: str = "1.0.0"
