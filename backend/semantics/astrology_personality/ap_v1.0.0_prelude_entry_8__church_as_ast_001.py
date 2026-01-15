"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237671
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
    semantic_id="ap_v1.0.0_prelude_entry_8__church_as_ast_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PreludeEntry8ChurchAsAst(SemanticEntry):
    """
    **Source Text** (Lines 1273-1310):
> In this jungle, as in any jungle, there was fear. Monstrous cre...
    """
    
    original_text: str = """**Source Text** (Lines 1273-1310):
> In this jungle, as in any jungle, there was fear. Monstrous creatures, incubi, succubi, evil forces crowded it; no longer physiological creatures connected with earthy elements, but products of sins, of self-deceptions and of biological starvation. From this arose a psychological type of animism...
>
> Yet the Church was a refuge, a token of the possibility of a supernal world to which she alone led. And therefore the Church took the place of astrology. It did so with many festivals and ceremonies arranged with great order throughout the year—in fact duplicating the old biological festivals based on the astrology of the archaic era...
>
> But it was still astrology under a different garb! Astrology without the name. The wheel of the zodiac was replaced by a system of permutations of the four elements: hot, cold, dry, humid—not unlike the Chinese Yi King...
>
> There came, however, during the Middle Ages (especially after the eleventh century) a great renewal of astrological ideas proper, which, while repudiated and combated by the Church, still came more and more to control the minds of the period. This astrology was the result of the "psychological animism" already mentioned; and it can be generally characterized by the term Kabbalistic.

**Key Term Analysis**:
- **Psychological jungle**: `incubi, succubi, evil forces` / `products of sin and repression` / `psychological animism`
- **Church as astrology**: `festivals duplicating astrological cycles` / `astrology without name` / `Christian zodiac`
- **Four elements system**: `hot, cold, dry, humid` / `replacing zodiac wheel` / `Yi King parallel`
- **Kabbalistic astrology**: `11th century revival` / `psychological animism` / `ceremonial magic link`
- **Christian cosmic order**: `saints and archangels` / `ceremonies keeping jungle away` / `security through ritual`

**English Paraphrase (Primary Language)**:
The psychological jungle that replaced the physiological one was populated by new creatures: incubi, succubi, products of sin and repression rather than elemental nature. This created "psychological animism"—a new form of the archaic pattern at a different level.

The Church became astrology's functional successor. Its liturgical calendar duplicated archaic astrological festivals; its cycle of ceremonies provided the same order-security that vitalistic astrology once did. "It was still astrology under a different garb!" The zodiac wheel was replaced by four-element permutations (hot, cold, dry, humid)—not unlike the Yi King. Saints and archangels populated the Christian zodiac. Ceremonies kept the psychological jungle at bay.

However, after the eleventh century, explicit astrological revival occurred—Kabbalistic astrology, linked to ceremonial magic, arriving through Arabic Spain (especially Fez, Morocco). This represented "psychological animism" taking astrological form: addressing the new psycho-mental chaos with magical-symbolic techniques.

**Complete Chinese Interpretation (Secondary Language)**:
取代生理丛林的心理丛林充满了新的生物：梦魇、女妖、罪恶和压抑的产物，而非元素自然。这创造了"心理泛灵论"——古老模式在不同层次的新形式。

教会成为占星学的功能继承者。其礼仪日历复制了古代占星节日；其仪式周期提供了与生机论占星学相同的秩序-安全感。"这仍然是另一种外衣下的占星学！"黄道轮被四元素排列（热、冷、干、湿）取代——与易经相似。圣徒和天使长居住在基督教黄道中。仪式将心理丛林阻隔在外。

然而，11世纪后，明确的占星学复兴发生了——卡巴拉占星学，与仪式魔法相连，通过阿拉伯西班牙（特别是摩洛哥非斯）传入。这代表了"心理泛灵论"采取占星形式：用魔法-符号技术处理新的心理-精神混乱。

**Core Points**:
- Psychological jungle replaces physiological (incubi, succubi)
- Psychological animism = new pattern at mental level
- Church = astrology's functional successor
- Liturgical calendar duplicates astrological festivals
- Four elements (hot/cold/dry/humid) replace zodiac
- Christian zodiac with saints and archangels
- Ceremonies provide order-security
- 11th century Kabbalistic astrology revival
- Arrived through Arabic Spain (Fez)
- Linked to ceremonial magic

**Narrative Snippets**:
- `[ns_aop_049]` `[trigger: psychological_jungle]` `[factor_trigger: psych_animism AND astro_psych_animism AND astro_psych_jungle_state]` `[role: 主干]` Psychological jungle populated by incubi, succubi—products of sin and repression, not elemental nature. → Source Text L1273-1276
- `[ns_aop_050]` `[trigger: church_as_astrology]` `[factor_trigger: church AND astro_church_function AND astro_heavenly_order]` `[role: 主干依赖]` Church took place of astrology with festivals duplicating archaic cycles—astrology under different garb. → Source Text L1280-1290
- `[ns_aop_051]` `[trigger: kabbalistic_revival]` `[factor_trigger: kabbalistic_astro AND sympathetic_magic AND astro_kabbalistic_revival]` `[role: 条件分支]` 11th century Kabbalistic astrology revival—result of psychological animism, linked to ceremonial magic. → Source Text L1300-1308
- `[ns_aop_052]` `[trigger: four_elements]` `[factor_trigger: four_elements AND astro_four_elements]` `[role: 总结]` Zodiac wheel replaced by four elements (hot/cold/dry/humid)—not unlike Chinese Yi King. → Source Text L1291-1296

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Rudhyar's reading of Church as astrology's successor is provocative but has support in liturgical scholarship. The Kabbalistic astrology section anticipates later work on medieval magical traditions.
- **中文**: Rudhyar将教会解读为占星学继承者具有挑衅性，但在礼仪学术中有支持。卡巴拉占星学部分预见了后来对中世纪魔法传统的研究。"""
    normalized_text_zh: str = """"""
    subject: str = "Prelude Entry 8: Church as Astrology's Successor and Kabbalistic Revival"
    factor_refs: list = ['astro_psych_animism', 'astro_church_astro', 'astro_kabbalistic', 'astro_four_elements']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_prelude_entry_8__church_as_ast_001_L1",
    )
    version: str = "1.0.0"
