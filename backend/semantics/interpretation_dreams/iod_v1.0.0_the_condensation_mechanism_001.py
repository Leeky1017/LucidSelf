"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.469042
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
    semantic_id="iod_v1.0.0_the_condensation_mechanism_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class TheCondensationMechanism(SemanticEntry):
    """
    **Source Text**:
"The first thing which becomes clear to the investigator in the comparison of the d...
    """
    
    original_text: str = """**Source Text**:
"The first thing which becomes clear to the investigator in the comparison of the dream content with the dream thoughts is that a tremendous work of condensation has taken place. The dream is reserved, paltry, and laconic when compared with the range and copiousness of the dream thoughts. The dream when written down fills half a page; the analysis, in which the dream thoughts are contained, requires six, eight, twelve times as much space."

"Thus the amount of condensation is—strictly speaking—indeterminable. An objection, which at first sight seems very plausible, might be raised against the assertion that the disproportion between dream content and dream thought justifies the conclusion that an abundant condensation of psychic material has taken place in the formation of dreams."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Condensation | Compression of multiple thoughts into single image | Primary dream-work mechanism |
| Disproportion | Ratio of manifest to latent content (1:6-12) | Evidence for condensation |
| Laconic | Brief, terse expression | Quality of manifest content |
| Indeterminable | Cannot be fully measured | Condensation has no limit |
| Nodal Point | Element where multiple thought-chains converge | Condensation marker |

**English Paraphrase (Primary Language)**:

**Condensation** (Verdichtung) is the first and most fundamental mechanism of dream-work. Freud observes a dramatic **disproportion**: a dream that fills half a page when written requires six to twelve times as much space for its analysis. The manifest content is "reserved, paltry, and laconic" compared to the "range and copiousness" of latent thoughts.

This compression is **indeterminable**—one can never fully exhaust a dream's meanings because condensation has no theoretical limit. Each dream element serves as a **nodal point** where multiple thought-chains converge. A single dream image may represent:
- Multiple persons (composite figures)
- Multiple ideas (overdetermination)
- Multiple time periods (temporal compression)
- Multiple associations (verbal bridges)

The objection that we simply "forget" most of our dreams (and thus the disproportion is illusory) is addressed: even preserved dream portions show condensation from their associated thought-chains. Forgetting would merely reveal more condensed material, not eliminate condensation.

**Complete Chinese Interpretation (Secondary Language)**:

**凝缩**（Verdichtung）是梦的工作的第一个也是最根本的机制。弗洛伊德观察到一个戏剧性的**不成比例**：一个写下来只占半页的梦，其分析却需要六到十二倍的篇幅。显性内容与隐性思想的"丰富广泛"相比是"保守、贫乏、简洁"的。

这种压缩是**不可确定的**——永远无法完全穷尽一个梦的含义，因为凝缩在理论上没有极限。每个梦元素都作为**节点**发挥作用，多条思想链在此汇聚。单一梦境图像可能代表：
- 多个人物（复合形象）
- 多重观念（多重决定）
- 多个时间段（时间压缩）
- 多重联想（语言桥梁）

对于"我们只是遗忘了大部分梦境"（因此不成比例是幻觉）的反驳：即使保留下来的梦境部分也显示出来自其关联思想链的凝缩。遗忘只会揭示更多凝缩材料，而非消除凝缩。

**Core Points**:

- Condensation = compression of multiple thoughts into single images
- Ratio: 1 page dream → 6-12 pages analysis
- Manifest content is laconic; latent content is copious
- Condensation is indeterminable (no theoretical limit)
- Nodal points: where multiple thought-chains converge
- Forgetting doesn't eliminate condensation evidence

**Detailed Explanation**:

Condensation explains why dreams appear strange and illogical: they are **compressed archives** of vast mental content. A single dream figure may combine features of three different people because the dreamer's thoughts about all three share a common element. This is not confusion but **efficient encoding**.

The **1:6-12 ratio** has methodological implications. Brief dream elements require extensive unpacking. Analysts must resist the temptation to find quick symbolic meanings; proper interpretation requires following all associative threads to discover how many thoughts converge on each element.

**Nodal points** are interpretively crucial—they are overdetermined elements where multiple meanings intersect. Finding the nodal point often unlocks the dream's core meaning because it represents where the dreamer's concerns most intensely converge.

The **indeterminability** of condensation means interpretation is theoretically infinite. This is not a weakness but reflects the dream's nature as a compression of unconscious material that itself has no clear boundaries.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: Freud's German "Verdichtung" literally means "condensation" or "compression" but also carries poetic connotations (Dichtung = poetry). The dream as poetry is implicit.
- **中文**: 德语"Verdichtung"字面意思是"凝缩"或"压缩"，但也带有诗意内涵（Dichtung = 诗歌）。梦作为诗歌这一隐喻在此暗含。中文"凝缩"较好地保留了压缩的物理意象。

**Narrative Snippets**:

- `[ns_freud_dw_004]` `[trigger: condensation_mechanism]` `[factor_trigger: dream_condensation]` `[role: 主干]` The dream is reserved, paltry, and laconic when compared with the range and copiousness of the dream thoughts. The dream when written fills half a page; the analysis requires six, eight, twelve times as much space. → Freud Ch.VI #Condensation
- `[ns_freud_dw_005]` `[trigger: condensation_ratio]` `[factor_trigger: dream_condensation]` `[role: 主干依赖]` The amount of condensation is—strictly speaking—indeterminable. One is never sure of having interpreted a dream completely; a further meaning may always be manifested. → Freud Ch.VI #Condensation
- `[ns_freud_dw_006]` `[trigger: nodal_point]` `[factor_trigger: dream_condensation AND dream_overdetermination]` `[role: 条件分支]` Each dream element serves as a nodal point where multiple thought-chains converge—a single image may represent multiple persons, ideas, and time periods. → Freud Ch.VI #Condensation
- `[ns_freud_dw_023]` `[trigger: composite_figure]` `[factor_trigger: dream_condensation AND dream_person]` `[role: 条件分支]` A single dream figure may combine features of three different people—not confusion but efficient encoding where thoughts about all three share a common element. → Freud Ch.VI #Condensation"""
    normalized_text_zh: str = """"""
    subject: str = "The Condensation Mechanism"
    factor_refs: list = ['condensation', 'nodal_point', 'new_candidate', 'composite_figure']
    
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_the_condensation_mechanism_001_L1",
    )
    version: str = "1.0.0"
