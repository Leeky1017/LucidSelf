"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147294
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
    semantic_id="ca_v1.0.0_house_system___twelve_life_are_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class HouseSystemTwelveLifeAre(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| Angular houses | Domus Angulares | Houses 1/4/7/10 on angles | Strongest power, quick manifestation |
| Succedent houses | Domus Succedentes | Houses 2/5/8/11 following angles | Moderate power, steady development |
| Cadent houses | Domus Cadentes | Houses 3/6/9/12 falling away | Weakest power, unstable matters |
| Derived houses | Turned houses | Houses counted from another house | Relationship analysis technique |

#### Source Text

"The twelve Houses do represent the whole Universe, and are distinguished by the twelve Signs of the Zodiack. The first House beginneth from the Cusp of the Ascendent, and containeth all that part of Heaven from the Ascendent to the second House-cusp. Every House hath particular signification assigned unto it: the First signifieth Life and Body; the Second, Substance and Wealth; the Third, Brethren and short journeys; and so forth through all twelve."

#### English Paraphrase (Primary Language)

The **twelve houses** divide the celestial sphere into **life areas**, each governing specific matters querent might ask about. Understanding house meanings is **essential to horary**—you must know which house governs the questioned matter to identify correct significator.

**House meanings** (Lilly's classical attributions):

**Angular Houses** (1, 4, 7, 10 - most powerful):
- **1st House**: Querent, body, life, health, appearance, general state
- **4th House**: Father, land, property, endings, hidden things, agriculture, graves
- **7th House**: Spouse, partners, open enemies, lawsuits, contracts, "other person"
- **10th House**: Career, honors, authority, mother, kings, reputation, success

**Succedent Houses** (2, 5, 8, 11 - moderate power):
- **2nd House**: Money, moveable property, profit, possessions, personal resources
- **5th House**: Children, pleasure, gambling, taverns, entertainment, creative works
- **8th House**: Death, inheritance, partner's money, fear, surgery, transformation
- **11th House**: Friends, hopes, wishes, benefits from authority, support networks

**Cadent Houses** (3, 6, 9, 12 - weakest, most unstable):
- **3rd House**: Siblings, short journeys, writing, communication, neighbors, rumors
- **6th House**: Illness, servants, small animals, daily work, employees, uncles/aunts
- **9th House**: Long journeys, religion, higher learning, foreign lands, dreams, law
- **12th House**: Secret enemies, imprisonment, large animals (horses), self-undoing, isolation

**Derived houses** (houses from houses): Count from any house to find related matters:
- **2nd from 7th** (8th house): Partner's money
- **7th from 7th** (1st house): Opponent's opponent (your ally)
- **10th from 10th** (7th house): Career's outcome
- **5th from 5th** (9th house): Grandchildren

**House strength hierarchy**:
1. **Angular**: Strongest, matters manifest quickly, visibility, power
2. **Succedent**: Moderate, matters develop steadily, resources, stability  
3. **Cadent**: Weakest, matters unstable, often fail, communication, thought

**Practical application**: "Will I get the job?"
- **10th house** governs career → 10th house ruler = the job
- **Querent** (1st house ruler) applying to 10th house ruler → YES
- If querent in 10th house → You're already close to position
- If 10th ruler in 6th house → Job involves service/health, or brings illness

#### Complete Chinese Interpretation (Secondary Language)

**十二宫位**划分生活领域，每宫管特定事项。**角宫**(Angular: 1/4/7/10)最强；**续宫**(Succedent: 2/5/8/11)中等；**果宫**(Cadent: 3/6/9/12)最弱。每宫代表：第1宫=问卜者自身；第2宫=金钱/财产；第3宫=兄弟/沟通/短途；第4宫=家园/父亲/房产/事物结局；第5宫=子女/娱乐/怀孕；第6宫=仆人/疾病/小动物；第7宫=配偶/伴侣/对手/诉讼；第8宫=死亡/遗产/他人金钱；第9宫=长途旅行/宗教/智慧；第10宫=事业/荣誉/母亲；第11宫=朋友/希望/团体；第12宫=敌人/监禁/大动物/自毁。行星在角宫有力量迅速行动；在续宫延迟但最终成功；在果宫软弱难以完成事项。宫位守护星成为相关事项的征象星。

#### Core Points

- **Twelve life areas**: Each house governs specific matters querent asks about
- **Angular strongest**: 1/4/7/10 houses most powerful, matters manifest
- **Succedent moderate**: 2/5/8/11 houses stable, resource-oriented
- **Cadent weakest**: 3/6/9/12 houses unstable, often fail
- **Derived houses**: Count from any house for related matters
- **House identification**: Determines correct quesited significator
- **House strength**: Affects speed and success of manifestation

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly's house meanings largely follow Ptolemy and Arabic sources, but with expanded practical detail. The "angular/succedent/cadent" terminology derives from Greek (kentron/epanaphora/apoklima). Some medieval variations exist—e.g., 9th house as "God's house" (dreams, prophecy) in Arabic texts. The derived house technique ("turned houses") became especially important in horary for relationship questions.
- **中文**: Lilly的宫位意义大体遵循托勒密和阿拉伯来源，但有更详细的实践细节。"角宫/续宫/果宫"术语源自希腊语(kentron/epanaphora/apoklima)。中世纪存在一些变体——如阿拉伯文本中第9宫作为"神之宫"（梦、预言）。衍生宫位技术（"转宫"）在关系问题的卜卦中尤为重要。

**Narrative Snippets**:
- `[ns_lilly_011]` `[trigger: twelve_houses]` `[factor_trigger: astro_houses AND astro_universe AND astro_life_division]` `[role: 主干]` The twelve Houses do represent the whole Universe, distinguished by the twelve Signs of the Zodiack. → Source Text
- `[ns_lilly_012]` `[trigger: house_meanings]` `[factor_trigger: astro_house AND astro_signification AND astro_matter_category AND astro_wealth_level]` `[role: 主干依赖]` Every House hath particular signification: the First signifieth Life and Body; the Second, Substance and Wealth; the Third, Brethren and short journeys. → Source Text
- `[ns_lilly_013]` `[trigger: angular_power]` `[factor_trigger: astro_angular AND astro_strength AND astro_manifestation_power]` `[role: 条件分支]` Angular houses (1/4/7/10) are strongest—matters manifest quickly; succedent moderate; cadent weakest, often fail. → English Paraphrase
- `[ns_lilly_014]` `[trigger: derived_houses]` `[factor_trigger: astro_derived AND astro_counting AND astro_related_matter]` `[role: 总结]` Derived houses: count from any house for related matters—e.g., 2nd from 7th (8th house) = partner's money. → English Paraphrase
- `[ns_lilly_015]` `[trigger: career_house]` `[factor_trigger: astro_career_house]` `[role: 主干依赖]` The 10th house signifies career, honors, authority, mother, reputation, success—matters of public standing. → English Paraphrase
- `[ns_lilly_016]` `[trigger: disease_house]` `[factor_trigger: astro_disease_house]` `[role: 条件分支]` The 6th house signifies illness, servants, small animals, daily work, employees—matters of health and service. → English Paraphrase
- `[ns_lilly_017]` `[trigger: life_vitality]` `[factor_trigger: astro_life_vitality]` `[role: 主干依赖]` The 1st house signifies life and body—querent's vitality, health, appearance, general condition. → English Paraphrase
- `[ns_lilly_018]` `[trigger: marriage_axis]` `[factor_trigger: astro_marriage_axis]` `[role: 条件分支]` The 7th house signifies spouse, partners, open enemies, lawsuits, contracts—the "other person" axis. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "House System - Twelve Life Areas"
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
        l1_anchor="ca_v1.0.0_house_system___twelve_life_are_001_L1",
    )
    version: str = "1.0.0"
