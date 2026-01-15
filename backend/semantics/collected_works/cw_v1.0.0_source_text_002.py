"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574891
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
    semantic_id="cw_v1.0.0_source_text_002",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "Archetypes are not determined as regards their content, but only as regards their form and then onl...
    """
    
    original_text: str = """"Archetypes are not determined as regards their content, but only as regards their form and then only to a very limited degree. A primordial image is determined as to its content only when it has become conscious and is therefore filled out with the material of conscious experience. Its form, however, might perhaps be compared to the axial system of a crystal, which, as it were, preforms the crystalline structure in the mother liquid, although it has no material existence of its own... The archetype in itself is empty and purely formal, nothing but a facultas praeformandi, a possibility of representation which is given a priori."

#### English Paraphrase (Primary Language)

An **archetype** is a **pre-existent formal pattern** in the collective unconscious—not a fixed image but a **potential** for certain types of images and experiences. Jung's famous analogy: archetype is like a **crystal's invisible axial system** that determines how the crystal will form, though the actual crystal varies based on available material.

**Key understanding**:
- **Form not content**: Archetype is the pattern/structure, not specific image
- **Potential not actuality**: Capacityfor representation, not the representation itself
- **Universal structure**: Same form in all humans but filled with cultural content
- **Example**: Mother archetype isn't any specific mother image but the **pattern** that generates all mother images—Madonna, Kali, your actual mother, Mother Nature

**How they work**:
1. **Archetype-as-such** (noumenal): Invisible, formal pattern in collective unconscious—can never be known directly
2. **Archetypal image** (phenomenal): Conscious manifestation when archetype activated—culturally specific expression
3. **Personal experience**: Actual encounter with archetypal situation (meeting authority, falling in love, facing death)

**Analogy refined**: Like a riverbed that shapes water flow. The bed (archetype) is constant; the water (archetypal images) varies. Or like musical form (sonata) vs specific sonatas (Beethoven's 5th)—form repeatable, content unique.

**Why "empty"**: Jung insists archetypes are **formal** not **material**. The Mother archetype doesn't contain specific mother imagery but the **capacity to perceive/experience mothering** according to universal pattern. Cultural clothing varies (Madonna vs Kali) but underlying maternal pattern (nurturing, birth-giving, devouring) remains constant.

**Activation**: Archetypes normally dormant until triggered by life situation. Falling in love activates Anima/Animus archetype; authority conflict activates Father; identity crisis activates Hero. Once activated, archetype structures perception—you experience situation through archetypal lens.

**Numinosity**: When archetype constellates powerfully, produces **numinous** experience—overwhelming, fascinating, beyond personal control. Religious conversion, falling in love, creative inspiration—moments when archetypal energy floods consciousness.

#### Complete Chinese Interpretation (Secondary Language)

完整中文诠释：原型并不是某个具体的“图像”或“故事”，而是一种**先验的形式模式**——类似水晶在母液中看不见的轴系，先为未来的晶体提供结构框架，但具体结晶出何种形状与颜色，要看实际参与的物质为何。套用荣格的比喻：原型好比“河床”或“乐曲形式”，真正流动的河水、实际写出的奏鸣曲是各民族、各个人在不同文化与生活素材基础上完成的“填充”；然而所有这些具体图像与故事背后，都依托同一条看不见的结构线。

因此，原型本身是**空的、形式性的潜能（facultas praeformandi）**，并不预先装载任何固定内容。所谓“母亲原型”并不是某一幅具体的圣母像或某个神话中的母神，而是关于“滋养、孕育、包容、同时也可能吞噬”的一整套关系结构；它在基督教语境中可以表现为圣母玛利亚，在印度传统里则是卡莉，在个人经验里则可能是自己的生母或大地母亲意象。只要原型被生活情境触发（例如遭遇权威、坠入爱河、面对死亡），它便会自动吸引与之相容的文化素材，**生成原型意象（archetypal image）**，以便进入意识层面被我们“看见”。

当原型能量强烈“成形”（constellate）时，会带来一种荣格称之为**“神圣感/震撼感”（numinous）**的体验——既令人恐惧又充满魅惑，远远超出个人意志所能掌控。宗教皈依、灵光乍现的创作灵感、突然无法自拔的恋情，往往都伴随着这种“不是我在控制，而是有什么更大的力量在发生”的感受。临床与神话研究中，荣格正是通过追踪这些高度情绪化、反复出现的意象模式（英雄之旅、伟大母亲、智者、阴影等），才逐步描绘出原型世界的轮廓。

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Archetype | Pre-existent formal pattern | Universal template |
| Archetypal Image | Conscious manifestation | Cultural expression |
| Facultas Praeformandi | Possibility of representation | A priori capacity |
| Numinous | Overwhelming experience | Archetypal power |

#### Core Points

- **Form not content**: Pattern/structure not specific images
- **Empty and formal**: Potential for representation not the representation
- **Universal but culturally clothed**: Same form, different cultural expressions
- **Invisible structure**: Like crystal axis or riverbed shaping manifestation
- **Activated by situation**: Dormant until life triggers them
- **Numinous when active**: Powerful activation creates overwhelming experience
- **Never known directly**: Only known through archetypal images/expressions

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Archetype: Pre-existent formal pattern, not fixed image. Crystal axis analogy—invisible structure determining form. Archetype-as-such vs archetypal image. Activated by life situations. Numinous when powerfully constellated.
- **中文**: 原型:先在形式模式,非固定图像。水晶轴系类比——不可见结构决定形式。原型本身 vs 原型意象。被生活情境激活。强烈成形时具有神圣感。

**Narrative Snippets**:
- `[ns_jung_007]` `[trigger: archetype_form]` `[factor_trigger: jung_archetype AND jung_form]` `[role: 主干]` Archetypes are not determined as regards their content, but only as regards their form—a possibility of representation given a priori. → Source Text
- `[ns_jung_008]` `[trigger: crystal_analogy]` `[factor_trigger: jung_crystal AND jung_preform]` `[role: 主干依赖]` Form compared to axial system of crystal, preforming structure in mother liquid though having no material existence. → Source Text
- `[ns_jung_009]` `[trigger: empty_formal]` `[factor_trigger: jung_empty AND jung_potential]` `[role: 条件分支]` The archetype in itself is empty and purely formal—nothing but a facultas praeformandi. → Source Text
- `[ns_jung_010]` `[trigger: universal_pattern]` `[factor_trigger: jung_pattern AND jung_universal]` `[role: 总结]` Archetype is pre-existent formal pattern—not fixed image but potential for certain types of images. → English Paraphrase
- `[ns_jung_011]` `[trigger: numinous_experience]` `[factor_trigger: jung_numinous AND jung_archetype]` `[role: 主干]` When archetype constellates powerfully, produces numinous experience—overwhelming, fascinating, beyond personal control. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        book_id="collected_works",
        chapter="",
        l1_anchor="cw_v1.0.0_source_text_002_L1",
    )
    version: str = "1.0.0"
