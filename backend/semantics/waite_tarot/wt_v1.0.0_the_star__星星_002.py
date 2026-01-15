"""
Auto-generated semantic module for waite_tarot
Generated at: 2025-12-05T13:30:19.952783
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
    semantic_id="wt_v1.0.0_the_star__星星_002",
    book_id="waite_tarot",
    engine_id="tarot"
)
class TheStar星星(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Reflected Light | Intellectual not direct | Cannot penetrate mystery |
| Nameless Tendency | Abyss horror | Lower than beast |
| Peace Be Still | Mark 4:39 | Mind calms animal |
| Imagination vs Spirit | Divorced from truth | Illusion |

**Number**: XVIII  
**Hebrew Letter**: Qoph (ק)  
**Qabalistic Path**: Netzach to Malkuth (Victory to Kingdom)  
**Element/Planet**: Pisces / Neptune/Moon

**Source Text**:
> "The distinction between this card and some of the conventional types is that the moon is increasing on what is called the side of mercy. The card represents life of the imagination apart from life of the spirit. The path between the towers is the issue into the unknown. The dog and wolf are the fears of the natural mind in the presence of that place of exit, when there is only reflected light to guide it. The intellectual light is a reflection and beyond it is the unknown mystery which it cannot shew forth. It illuminates our animal nature, types of which are represented below--the dog, the wolf and that which comes up out of the deeps, the nameless and hideous tendency which is lower than the savage beast. It strives to attain manifestation, symbolized by crawling from the abyss of water to the land, but as a rule it sinks back whence it came. The face of the mind directs a calm gaze upon the unrest below; the dew of thought falls; the message is: Peace, be still; and it may be that there shall come a calm upon the animal nature, while the abyss beneath shall cease from giving up a form."

**English Paraphrase**:
**Reflected Light & the Abyss** – Moon **increasing on side of mercy**. Key distinction: **"life of imagination apart from life of spirit"** – imagination divorced from spiritual truth. **Path between towers = issue into unknown**. **Dog and wolf = fears of natural mind** facing exit with **only reflected light** (not direct spiritual light).

Critical insight: **"The intellectual light is a reflection and beyond it is the unknown mystery which it cannot shew forth."** Intellect/reason (reflected light) cannot penetrate ultimate mystery – it only illuminates **"our animal nature"** (dog, wolf, and **"that which comes up out of the deeps, the nameless and hideous tendency which is lower than the savage beast"** – the crawfish/crayfish representing subconscious horrors).

This **"nameless tendency strives to attain manifestation"** (crawling from water abyss to land) but **"as a rule it sinks back whence it came"** – usually fails to manifest, returns to depths.

The **"face of the mind directs a calm gaze"**; **"dew of thought falls"**; message: **"Peace, be still"** (Jesus calming storm, Mark 4:39). Hope: **"there shall come a calm upon the animal nature, while the abyss beneath shall cease from giving up a form"** – mind can pacify lower nature, suppress abyss.

**Core**: **Imagination vs Spirit** – Reflected (not direct) light, fears/illusions, abyss horrors, mind must calm animal nature.

**Chinese Explanation**:
**月亮（反射之光与深渊）**——月亮**在慈悲侧增长**。关键区分：**"想象生活与灵性生活分离"**——想象脱离灵性真理。**塔间路径=进入未知的出口**。**狗与狼=自然心智的恐惧**，面对出口仅有**反射之光**（非直接灵性之光）。

关键洞察：**"智识之光是反射，其外是它无法显示的未知奥秘"**。智力/理性（反射光）无法穿透终极奥秘——它只照亮**"我们的动物本性"**（狗、狼，及**"从深处上来的，比野蛮兽更低的无名且可怕倾向"**——螯虾代表潜意识恐怖）。

这**"无名倾向努力达到显化"**（从水深渊爬向陆地）但**"通常沉回原处"**——常失败显化，回到深处。

**"心智面容投以平静凝视"**；**"思想露珠落下"**；信息：**"平静，安静"**（耶稣平静风暴，马可4:39）。希望：**"将有平静临到动物本性，而下方深渊将停止释放形体"**——心智可安抚较低本性，压制深渊。

**In Readings**: Illusion, fear, confusion, subconscious, but remember: reflected not direct light, imagination apart from spirit, mind must calm animal nature.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Waite's key distinction: "life of imagination apart from life of spirit." Intellectual light is "reflection, cannot show unknown mystery." Nameless tendency from abyss "strives to manifest, sinks back." Mind's "Peace, be still" (Mark 4:39) calms animal nature.
- **中文**: 韦特关键区分："想象生活与灵性生活分离"。智识之光是"反射，无法显示未知奥秘"。深渊无名倾向"努力显化，退回"。心智"平静，安静"(可4:39)安抚动物本性。

**Narrative Snippets**:
- `[ns_waite_046]` `[trigger: moon_reflected]` `[factor_trigger: tarot_moon AND reflected_light]` `[role: 主干]` The intellectual light is a reflection and beyond it is the unknown mystery which it cannot shew forth. → Core
- `[ns_waite_071]` `[trigger: moon_imagination]` `[factor_trigger: tarot_moon AND imagination_spirit]` `[role: 条件分支]` The card represents life of the imagination apart from life of the spirit—imagination divorced from spiritual truth. → Distinction
- `[ns_waite_072]` `[trigger: moon_abyss]` `[factor_trigger: tarot_moon AND nameless_tendency]` `[role: 条件分支]` The nameless and hideous tendency which is lower than the savage beast strives to attain manifestation but as a rule sinks back whence it came. → Shadow"""
    normalized_text_zh: str = """"""
    subject: str = "The Star (星星)"
    factor_refs: list = ['tarot_moon', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tarot_moon', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'source_ref', 'rel_waite_052', 'tarot_moon', 'opposing', 'rel_waite_053', 'tarot_moon', 'suppressed', 'rel_waite_054', 'tarot_moon', 'pacifying', 'evi_waite_035', 'tarot_moon', 'rule_waite_moon_reflected', 'evi_waite_036', 'tarot_moon', 'rule_waite_moon_imagination', 'concept_reflected_light', 'ego_consciousness', 'concept_abyss_tendency', 'house_12', 'shadow_jung']
    
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
        book_id="waite_tarot",
        chapter="",
        l1_anchor="wt_v1.0.0_the_star__星星_002_L1",
    )
    version: str = "1.0.0"
