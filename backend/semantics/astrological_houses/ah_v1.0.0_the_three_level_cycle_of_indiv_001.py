"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333913
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
    semantic_id="ah_v1.0.0_the_three_level_cycle_of_indiv_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class TheThreeLevelCycleOfIndiv(SemanticEntry):
    """
    #### Source Text

"The experiences of a person having achieved a consistent state of individualizati...
    """
    
    original_text: str = """#### Source Text

"The experiences of a person having achieved a consistent state of individualization can take place at three basic levels, and the natural process of growth in personality is cyclic; each cycle theoretically lasts 28 years. During each 28-year cycle a human being normally focuses attention successively upon each of the twelve fields of experience represented by natal houses. Then the process is repeated at a 'higher' level from age 28 to 56 and, potentially at a still more inclusive and spiritual level from 56 to 84. One can speak of three 'births' which represent a dialectical sequence—thesis, antithesis, and synthesis. A man is born in the physical biosphere at first breath—thesis. He is reborn in the psychomental noosphere at age 28. And potentially he can be born again in the spiritual realm—pneumosphere—at age 56."

#### English Paraphrase (Primary Language)

Rudhyar presents a profound developmental model based on 28-year cycles corresponding to the Uranus orbital period (84 years / 3 = 28). Each cycle represents passage through all twelve houses at a distinct level of consciousness:

1. **First Cycle (0-28)**: Birth in the physical biosphere—establishment of biological, cultural, and social roots in the collective unconscious. The young person brings the past to fulfillment while potentially rebelling against obsolete patterns.

2. **Second Cycle (28-56)**: "Birth in individuality"—the person realizes who they are as an individual, whether through vocation within society or struggle against tradition. True individuality emerges when, beyond protest, the maturing person becomes aware of their true self and destiny.

3. **Third Cycle (56-84)**: Potential "spiritual birth"—transcending both collective past and individual achievements. The person clearly realizes their function in human evolution, and society recognizes their contribution. This takes the form of "symbols" (deeds, art, teachings) that ensure relative immortality.

The Point of Self technique tracks this development: the Ascendant symbolically moves counterclockwise, reaching each angle at 7-year intervals, contacting natal planets and catalyzing consciousness changes.

#### Complete Chinese Interpretation (Secondary Language)

鲁迪亚基于与天王星轨道周期（84年÷3=28年）对应的28年周期提出深刻的发展模型。每个周期代表在不同意识层次上经过所有十二宫：

**三次诞生的辩证序列**：

1. **第一周期（0-28岁）**：物质生物圈的诞生——正题
   - 在集体无意识中建立生物、文化和社会根基
   - 年轻人将过去带向完成，同时可能反抗过时模式
   - 基础期：建立人格的地基

2. **第二周期（28-56岁）**：个体性的诞生——反题
   - 个人意识到自己作为个体是谁
   - 通过社会中的天职或对抗传统的斗争
   - 真正的个体性：超越抗议，觉知真我和命运
   - 成熟期：消极反叛让位于积极自我主张

3. **第三周期（56-84岁）**：灵性诞生——合题（潜在）
   - 超越集体过去和个人成就
   - 清晰认识在人类进化中的功能
   - 社会认可其贡献
   - 以"象征"形式（行为、艺术、教导）确保相对不朽

**自我点技术**：上升点象征性地逆时针移动，每7年到达一个角度，接触本命行星，催化意识变化。

#### Core Points

- **28-year cycles**: Three cycles of 28 years = 84-year Uranus cycle
- **Dialectical progression**: Thesis (physical) → Antithesis (individual) → Synthesis (spiritual)
- **Three births**: Biosphere → Noosphere → Pneumosphere
- **Point of Self**: Ascendant moves symbolically through houses, catalyzing changes
- **7-year rhythm**: Each angle reached at 7, 14, 21, 28, etc.
- **Symbol-making**: Third cycle produces transferable symbols ensuring immortality

#### Narrative Snippets

- `[ns_houses_034]` `[trigger: three_level_cycle]` `[factor_trigger: astro_uranus_cycle]` `[role: 主干]` Each 28-year cycle represents passage through all twelve houses at a distinct level: physical (0-28), psychomental (28-56), spiritual (56-84). → Three-Level Cycle
- `[ns_houses_035]` `[trigger: point_of_self]` `[factor_trigger: astro_ascendant_progression]` `[role: 条件分支]` The Point of Self moves counterclockwise, reaching each angle at 7-year intervals, contacting natal planets and catalyzing consciousness changes. → Three-Level Cycle"""
    normalized_text_zh: str = """"""
    subject: str = "The Three-Level Cycle of Individual Experiences"
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_the_three_level_cycle_of_indiv_001_L1",
    )
    version: str = "1.0.0"
