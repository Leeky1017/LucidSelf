"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.995093
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
    semantic_id="pt_v1.0.0_ace_of_pentacles__material_gif_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class AceOfPentaclesMaterialGif(SemanticEntry):
    """
    **Visual Elements**:
- Hand from cloud holding pentacle
- Garden path leading to mountains
- Archway...
    """
    
    original_text: str = """**Visual Elements**:
- Hand from cloud holding pentacle
- Garden path leading to mountains
- Archway of roses (victory wreath)
- Lush, abundant garden
- **Only Ace without yods** (divine letters)

**English Paraphrase**:

The **Ace of Pentacles** represents the **gift of material manifestation** - opportunities for prosperity, health, and tangible success. Unlike other Aces (which have yods showing divine origin), this Ace's power comes from **Earth itself** - the physical world as sacred.

**Core Symbolism**:
- **No yods**: Earth-rooted, not from above but from ground itself
- **Garden**: Enclosed security, cultivated abundance
- **Archway**: Gateway like World Dancer's wreath - physical leads to spiritual
- **Mountains beyond**: Higher consciousness accessible through material path
- **Hand offering**: Gift of opportunity, not just possession

**Upright Meaning**:
- **New material opportunity**: Job, money, property, health improvement
- **Prosperity**: Beginning of financial or physical abundance
- **Security**: Safe, protected situation
- **Manifestation**: Ideas becoming tangible reality
- **Body/health**: Physical vitality, healing
- **Grounded beginning**: Practical foundation established

**Reversed/Challenged**:
- **Missed opportunity**: Gift not recognized or accepted
- **Materialism**: Focusing on物质 at expense of spirit
- **Insecurity**: Safety becomes confinement
- **Blocked manifestation**: Ideas don't become real
- **Physical problems**: Health issues, material loss

**完整中文诠释**:
**星币王牌**=**物质显化之礼物**——繁荣、健康、有形成功的机会。不同于其他王牌（有yods显示神圣起源），此王牌力量来自**土地本身**——物质世界作为神圣。**图像元素**：**无yods**=扎根土地，非来自上方而是来自地面本身；**花园**=封闭、安全、培育丰盛；**拱门**=如世界舞者花环之门户，物质通向灵性；**远山**=通过物质路径可达更高意识；**手提供**=机会之礼物，非仅拥有。**正位含义**：**新物质机会**（工作、金钱、财产、健康改善），**繁荣**（财务或身体丰盛的开始），**安全**（安全、受保护的情境），**显化**（想法成为有形现实），**身体/健康**（身体活力、疗愈），**扎根开始**（实际基础建立）。**逆位/挑战**：**错失机会**（礼物未被承认或接受），**唯物主义**（以灵性为代价关注物质），**不安全**（安全变成囚禁），**阻塞显化**（想法不能成真），**物质问题**（健康问题、物质损失）。**哲学层面**：当小阿尔卡纳结束时，星币王牌显示从花园出口形成**类似世界舞者花环的拱门**——物质世界既是开始也是通向超越的门户。

**Philosophical Layer**: As Minor Arcana ends, Ace of Pentacles shows exit from garden forming **arch similar to World Dancer's wreath** - physical world is both beginning and gateway to transcendence.

**Narrative Snippets**:
- `[ns_78deg_290]` `[trigger: ace_pentacles_gift]` `[factor_trigger: tarot_ace_pentacles AND state_manifestation]` `[role: 主干]` Ace of Pentacles represents the gift of material manifestation—opportunities for prosperity, health, tangible success; power comes from Earth itself, physical world as sacred. → English Paraphrase
- `[ns_78deg_291]` `[trigger: no_yods]` `[factor_trigger: tarot_ace_pentacles AND symbol_no_yods]` `[role: 主干依赖]` Only Ace without yods (divine letters)—Earth-rooted, not from above but from ground itself; garden archway like World Dancer's wreath—physical leads to spiritual. → Core Symbolism
- `[ns_78deg_292]` `[trigger: ace_pentacles_opportunity]` `[factor_trigger: tarot_ace_pentacles AND event_opportunity]` `[role: 条件分支]` New material opportunity—job, money, property, health improvement; prosperity beginning, secure protected situation; ideas becoming tangible reality. → Upright Meaning
- `[ns_78deg_293]` `[trigger: ace_pentacles_reversed]` `[factor_trigger: tarot_ace_pentacles AND polarity_reversed]` `[role: 例外处理]` Reversed: missed opportunity, gift not recognized; materialism at expense of spirit; safety becomes confinement; blocked manifestation, physical problems. → Reversed Meaning
- `[ns_78deg_294]` `[trigger: garden_archway]` `[factor_trigger: tarot_ace_pentacles AND symbol_garden_archway]` `[role: 条件分支]` Garden path leading to mountains through rose archway—enclosed security, cultivated abundance; gateway where physical world opens to higher consciousness. → Core Symbolism
- `[ns_78deg_295]` `[trigger: earth_transcendence]` `[factor_trigger: tarot_ace_pentacles AND principle_earth_gateway]` `[role: 总结]` Exit from garden forms arch similar to World Dancer's wreath—physical world is both beginning and gateway to transcendence; matter as sacred path. → Philosophical Layer
- `[ns_78deg_452]` `[trigger: lush_garden]` `[factor_trigger: tarot_ace_pentacles AND symbol_lush_garden]` `[role: 条件分支]` Lush abundant garden surrounding the path—cultivated prosperity, the fruit of careful tending; nature in its most generous aspect offering its bounty. → Visual Elements
- `[ns_78deg_453]` `[trigger: mountains_beyond]` `[factor_trigger: tarot_ace_pentacles AND symbol_mountains]` `[role: 条件分支]` Mountains visible beyond garden—higher consciousness accessible through material path; the journey from physical to spiritual is through, not around, matter. → Core Symbolism
- `[ns_78deg_496]` `[trigger: rose_archway]` `[factor_trigger: tarot_ace_pentacles AND symbol_rose_arch]` `[role: 条件分支]` Archway of roses forms victory wreath—matter crowned with beauty; the physical path adorned not bare; prosperity and spiritual attainment united in garden's gate. → Visual Elements
- `[ns_78deg_553]` `[trigger: body_health_vitality]` `[factor_trigger: tarot_ace_pentacles AND state_physical_vitality]` `[role: 条件分支]` Body and health emphasized—physical vitality, healing potential; the gift of embodiment; Earth element manifesting as tangible wellness and grounded presence. → Upright Meaning"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Pentacles: Material Gift"
    factor_refs: list = ['gift', 'existing', 'origin', 'existing', 'process', 'existing', 'function', 'existing', 'gift', 'existing']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_ace_of_pentacles__material_gif_001_L1",
    )
    version: str = "1.0.0"
