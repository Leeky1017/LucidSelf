"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147278
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
    semantic_id="ca_v1.0.0_significators___representative_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class SignificatorsRepresentative(SemanticEntry):
    """
    #### Source Text

"The Significator of him or her that propounds the Question, is always the Lord of...
    """
    
    original_text: str = """#### Source Text

"The Significator of him or her that propounds the Question, is always the Lord of the houre wherein the Question is asked, viz. the Lord of the Ascendent; and therefore you must erect your Figure exactly for that time wherein you perfectly understood the Question. The Moon is generally a co-Significator with the Lord of the Ascendent, and in every Question may be so used. The Significator of the thing demanded, is the Lord of that House which signifies the thing demanded."

#### Key Term Analysis

- **Lord of the Ascendent**: The planet ruling the sign on the 1st house cusp; traditional rulerships only (Mars for Scorpio, not Pluto)
- **Co-Significator**: Secondary planet sharing signification; Moon always co-signifies querent alongside Ascendant ruler
- **Thing Demanded**: The quesited—whatever matter the querent asks about (marriage, money, job, etc.)
- **Lord of that House**: The planet ruling the sign on the cusp of the relevant house (e.g., 7th for marriage)

#### English Paraphrase (Primary Language)

**Significators** are the planets assigned to represent the **main actors or elements** in the question. Proper significator assignment is **foundation of judgment**—if you misidentify significators, entire reading collapses.

**The two essential significators**:

**1. Querent (问卜者)** - The Questioner:
- **Primary**: Ruler of Ascendant (1st house cusp sign's traditional ruler)
  - Example: Ascendant in Leo → Sun represents querent
  - Example: Ascendant in Scorpio → Mars represents querent (traditional, not Pluto)
- **Secondary**: Moon (universal co-significator)
  - Moon shows querent's emotional state, changeability, immediate concerns
  - When querent's ruler badly placed, Moon often provides backup testimony

**2. Quesited (被询之物)** - Thing Asked About:
- **Determined by house**: Ruler of house governing questioned matter
  - 7th house (partners, lawsuits, enemies) → 7th house ruler
  - 2nd house (money, possessions, debt) → 2nd house ruler
  - 10th house (career, reputation, authority) → 10th house ruler
  - 4th house (property, father, endings) → 4th house ruler

**Additional significators**:
- **Natural rulers**: Some planets inherently signify certain things:
  - **Venus**: Women (traditional), beauty, pleasure, marriage
  - **Mars**: Men (traditional), conflict, speed, violence
  - **Mercury**: Communication, young people, thieves, merchants
  - **Jupiter**: Wealth, judges, clergy, expansion
  - **Saturn**: Elderly, land, agriculture, delays, death
  - **Sun**: Authority figures, kings, fathers, vitality
  - **Moon**: Mothers, common people, fluctuation, women

**Judgment principle**: **Relationship between querent's significator and quesited's significator determines outcome**.

**Aspect types**:
- **Applying** (入相位): Planets moving toward exact aspect → YES, matter perfects
- **Separating** (出相位): Planets moving apart after aspect → NO, opportunity past
- **No aspect**: Matter unlikely unless **translated by third planet** or **collection of light**

**Reception** (接纳): When one planet in dignity of another:
- **Mutual reception**: Both planets in each other's dignity → strong connection, matter succeeds despite obstacles
- **Single reception**: Quesited receives querent → they welcome you
- **No reception**: Indifference or rejection

**Example**: "Will I marry John?"
- Querent: Ascendant ruler (represents you)
- Quesited: 7th house ruler (represents John/marriage)
- If querent's ruler applies to 7th ruler by trine with mutual reception → YES, marriage likely
- If querent's ruler separates from 7th ruler → NO, relationship already cooling
- If no aspect but Moon translates light between them → Maybe, through intermediary

#### Complete Chinese Interpretation (Secondary Language)

**征象星**(Significators)是指派代表问题主要行动者的行星。**问卜者**由上升守护星代表(+月亮作为共同征象星)。**被询之物**(quesited)由相关宫位守护星代表——第7宫守护星=伴侣/对手，第2宫守护星=金钱/财产，第10宫守护星=工作/荣誉，依此类推。**自然守护星**：某些行星固有地象征特定事物——金星(女性、美、婚姻)，火星(男性、冲突、速度)，水星(沟通、年轻人、商人)，木星(财富、法官、神职)，土星(老年、土地、延迟、死亡)，太阳(权威人物、父亲)，月亮(母亲、平民、波动)。**判断原则**：**问卜者征象星与被询之物征象星之间的关系决定结果**。相位类型：**入相**(applying，行星向精确相位移动)→是，事项完成；**出相**(separating，行星在相位后分离)→否，机会已过；**无相位**：事项不太可能，除非**第三行星传递**或**汇光**。

#### Core Points

- **Querent significator**: Ascendant ruler (primary) + Moon (secondary)
- **Quesited significator**: Ruler of house governing questioned matter
- **Natural rulers**: Planets inherently signifying certain things (Venus=women, Mars=men, etc.)
- **Applying aspect**: Significators moving toward each other = YES/completion
- **Separating aspect**: Significators moving apart = NO/past opportunity
- **Reception**: Planet in another's dignity = welcome, connection strength
- **No aspect**: Matter unlikely without translation or collection of light

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly's significator system derives from Arabic sources (esp. Masha'allah, Sahl ibn Bishr) via medieval Latin translations. The "Lord of the Hour" mentioned in source was originally a separate technique (planetary hours) but Lilly prioritizes Ascendant ruler. Traditional rulerships are essential—modern outer planets (Uranus, Neptune, Pluto) are debated among contemporary horary practitioners.
- **中文**: Lilly的征象星系统源自阿拉伯来源（尤其是Masha'allah、Sahl ibn Bishr），通过中世纪拉丁译本传播。原文提到的"时主星"原本是单独技术（行星时），但Lilly优先使用上升守护星。传统守护星是必需的——现代外行星（天王、海王、冥王）在当代占星师中有争议。

**Narrative Snippets**:
- `[ns_lilly_007]` `[trigger: querent_significator]` `[factor_trigger: astro_querent AND astro_significator AND astro_ascendant_ruler]` `[role: 主干]` The significator of the querent is always the Lord of the Ascendent; the Moon is generally a co-significator. → Source Text
- `[ns_lilly_008]` `[trigger: quesited_significator]` `[factor_trigger: astro_quesited AND astro_house_lord AND astro_matter_ruler]` `[role: 主干依赖]` The significator of the thing demanded is the Lord of that House which signifies the thing demanded. → Source Text
- `[ns_lilly_009]` `[trigger: applying_aspect]` `[factor_trigger: astro_applying AND astro_perfection AND astro_matter_completes AND astro_matter_fails]` `[role: 条件分支]` Applying aspect between significators = YES, matter perfects; separating = NO, opportunity past. → English Paraphrase
- `[ns_lilly_010]` `[trigger: reception]` `[factor_trigger: astro_reception AND astro_dignity AND astro_connection_strength]` `[role: 总结]` Reception (planet in another's dignity) indicates welcome, connection strength; mutual reception = strong success despite obstacles. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Significators - Representative Planets"
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_significators___representative_001_L1",
    )
    version: str = "1.0.0"
