"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237623
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
    semantic_id="ap_v1.0.0_prelude_entry_4__heavenly_orde_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PreludeEntry4HeavenlyOrde(SemanticEntry):
    """
    **Source Text** (Lines 912-977):
> The notion of Heavenly Order becomes the one great security again...
    """
    
    original_text: str = """**Source Text** (Lines 912-977):
> The notion of Heavenly Order becomes the one great security against the chaos of elemental nature, still so apparent in storms, inundations, droughts and cataclysms of all sorts. An archetypal, divine world of Order is shown in the Heavens where every object moves according to immutable laws. Man's task is then obviously so to operate upon the "earth" (the soil and cattle, but also his own earthly instinctual nature) that it becomes a perfect replica of the celestial Order...
>
> From such premises two basic needs can be deduced: the need for a calendar determining at first solely the time when all agricultural operations must be performed (sowing, harvesting, etc), and the days which are favorable and unfavorable to any such operation; then the need for an Ethical Law determining how man is to deal with and to cultivate his own nature...
>
> In ancient China we see the Emperor as high-priest of this celestial religion, mediator between the Heavenly Order centered around the Pole Star (where resides the great God of Order) and mankind. He is assisted by four astronomers... music being the agency whereby the earthly State may become tuned up to the "Harmony of the Spheres"...
>
> The Emperor is the fixed point of reference for all ethical social measurements, as the North Pole is astronomically. His voice is a paragon for all tones; his body, for all measurements. All roads are measured from the center of his palace...

**Key Term Analysis**:
- **Heavenly Order**: `security against chaos` / `archetypal divine world` / `immutable celestial laws`
- **Calendar**: `agricultural timing` / `favorable/unfavorable days` / `practical necessity`
- **Ethical Law**: `cultivation of human nature` / `social-cosmic alignment` / `State conformity`
- **Emperor as Mediator**: `high-priest` / `Pole Star connection` / `One Man`
- **Harmony of the Spheres**: `music as cosmic tuning` / `Pythagorean parallel` / `earthly-celestial alignment`
- **Four astronomers**: `imperial advisors` / `calendar establishers` / `cosmic knowledge keepers`

**English Paraphrase (Primary Language)**:
Rudhyar describes the mature vitalistic civilization: the Heavenly Order becomes humanity's psychological security against elemental chaos. The sky reveals archetypal Order—celestial bodies moving according to immutable laws—and humanity's task is to make earthly life a replica of this cosmic pattern.

Two practical needs emerge: (1) a Calendar for agricultural operations, specifying favorable and unfavorable times; (2) an Ethical Law governing human nature and social relations to align with cosmic order. In ancient China, the Emperor embodies this function: he is the high-priest mediating between Heavenly Order (centered on the Pole Star) and mankind.

The Emperor becomes the fixed reference point for all measurements—his voice standardizes musical tones, his body standardizes physical measures, all roads radiate from his palace. Music serves as the agency for cosmic tuning: bodily motions harmonized with celestial rhythms. This represents astrology at its most socially integrated—not fortune-telling but civilization-structuring knowledge.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar描述了成熟的生机论文明：天体秩序成为人类对抗元素混沌的心理安全保障。天空揭示原型秩序——天体按不变法则运动——人类的任务是使地上生活成为这一宇宙模式的复制品。

两个实际需求出现：(1)农业操作的历法，规定吉利和不吉利的时间；(2)管理人性和社会关系以与宇宙秩序对齐的伦理法则。在古代中国，皇帝体现这一功能：他是在天体秩序（以北极星为中心）与人类之间进行调解的大祭司。

皇帝成为所有度量的固定参照点——他的声音标准化音调，他的身体标准化物理度量，所有道路从他的宫殿辐射。音乐作为宇宙调谐的媒介：身体运动与天体节奏和谐。这代表了占星学最具社会整合性的形态——不是算命而是构建文明的知识。

**Core Points**:
- Heavenly Order = security against elemental chaos
- Celestial bodies reveal archetypal immutable laws
- Human task: make earth a replica of celestial Order
- Two needs: Calendar (agricultural timing) + Ethical Law (human nature)
- Emperor as high-priest mediator (China)
- Pole Star as center of cosmic order
- Music tunes earthly State to Harmony of Spheres
- Emperor = fixed reference for all social measurements
- Four astronomers assist in calendar establishment
- Astrology as civilization-structuring knowledge

**Narrative Snippets**:
- `[ns_aop_033]` `[trigger: heavenly_order]` `[factor_trigger: heavenly_order AND chaos AND astro_vitalistic_stage]` `[role: 主干]` Heavenly Order is security against chaos—archetypal divine world where objects move according to immutable laws. → Source Text L912-918
- `[ns_aop_034]` `[trigger: calendar_ethics]` `[factor_trigger: astro_calendar AND astro_astro_ethical_law AND astro_calendar_system AND astro_emperor_mediate]` `[role: 主干依赖]` Two needs: Calendar for agricultural timing, Ethical Law for cultivating human nature in cosmic alignment. → Source Text L920-927
- `[ns_aop_035]` `[trigger: emperor_mediator]` `[factor_trigger: emperor AND heaven_earth]` `[role: 条件分支]` Emperor is high-priest mediating between Heavenly Order (Pole Star) and mankind—One Man, One Mediator. → Source Text L928-948
- `[ns_aop_036]` `[trigger: harmony_spheres]` `[factor_trigger: cosmic_harmony AND music AND astro_musical_tuning]` `[role: 总结]` Music tunes earthly State to Harmony of Spheres—bodily motions harmonized with celestial rhythms. → Source Text L932-937

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Rudhyar's comparison of Chinese Emperor with Christian Christ as mediators is provocative but illuminates the structural parallel between astrological and religious civilizational functions.
- **中文**: Rudhyar将中国皇帝与基督作为中介者的比较具有挑衅性，但阐明了占星与宗教文明功能之间的结构平行。"""
    normalized_text_zh: str = """"""
    subject: str = "Prelude Entry 4: Heavenly Order and the Emperor as Mediator"
    factor_refs: list = ['astro_heavenly_order', 'astro_emperor_mediator', 'astro_harmony_spheres', 'astro_calendar_cosmic']
    
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
        l1_anchor="ap_v1.0.0_prelude_entry_4__heavenly_orde_001_L1",
    )
    version: str = "1.0.0"
