"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.094009
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
    semantic_id="tis_v1.0.0_fourth_house___the_nadir__inne_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class FourthHouseTheNadirInne(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Secret Garden | Private ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Secret Garden | Private inner world | Core concept |
| Hero & Shadow | Fantasy/fear poles | Depth |
| Inner Foundation | Unconscious roots | Structure |
| Home as Symbol | Outer reflects inner | Sanctuary |

#### Source Text

"The fourth house is the most subjective of the twelve. The arena it represents is secret. No one outside ourselves can see it. The contents of the fourth house are utterly isolated from the outer world. They exist only in the mind. 'Reality' is irrelevant to them. They grow and develop with a logic all their own."

#### English Paraphrase

The **Fourth House** (Nadir) is the **root of the self**—our private, subjective inner world. It represents home, family, and the unconscious foundations of personality.

**The Secret Garden**:
This is the part of us that is **invisible** to the public. It is our private sanctuary, our emotional bedrock. It operates on feelings, memories, and irrational logic.

**The Hero and The Shadow**:
- **The Hero**: Secret fantasies of greatness, what we truly yearn to be. Unrealistic but inspiring.
- **The Shadow**: Secret fears and insecurities, nightmares, what we repress.
- Both inhabit the Fourth House, shaping our behavior from beneath the surface.

**Home as Sanctuary**:
The physical home is a symbol of this inner state. We create a home to have a safe space to encounter our own depths. Homemaking is the means to nurture the inner self, not the end in itself.

**Roots**:
It governs our origins—parents, ancestry, childhood atmosphere. These roots feed the tree of our life. If roots are damaged, the tree struggles.

#### Complete Chinese Interpretation

**第四宫**（天底）是**自我的根基**——我们私密、主观的内在世界。它代表家、家庭和人格的无意识基础。

**秘密花园**：
这是我们对公众**不可见**的部分。它是我们的私人庇护所，我们的情感基石。它基于感觉、记忆和非理性逻辑运作。

**英雄与阴影**：
- **英雄**：关于伟大的秘密幻想，我们真正渴望成为的样子。不切实际但充满鼓舞。
- **阴影**：秘密的恐惧和不安全感，噩梦，我们压抑的东西。
- 两者都居住在第四宫，从表面之下塑造我们的行为。

**家作为庇护所**：
物理的家是这种内在状态的象征。我们创造一个家，以便有一个安全空间来面对我们自己的深处。营造家庭是滋养内在自我的手段，而非目的本身。

**根源**：
它掌管我们的起源——父母、祖先、童年氛围。这些根须滋养我们生命的树。如果根须受损，树木就会挣扎。

#### Core Points

- Most subjective/private sector (The Nadir).
- Contains the Hero (fantasies) and Shadow (fears).
- Home is sanctuary for the inner self.
- Roots, ancestry, emotional foundation.
- East parallel: 田宅宫/地支/根基 (Property Palace, Earthly Branches, Roots).

#### Detailed Explanation

The Fourth House is the **most private** sector of the chart—the Nadir, where the Sun is most hidden. It contains our **inner world**: the fantasies, fears, and emotional foundations that no one else can see. Forrest identifies two key contents: the **Hero** (grandiose self-images that inspire us) and the **Shadow** (fears and wounds we hide from ourselves).

**Home** in the Fourth House sense is not just a physical dwelling but a **sanctuary** where the inner self can exist safely. We need spaces where we can be unguarded, process emotions, and connect with our depths. Without adequate Fourth House expression, we remain strangers to ourselves.

This house also governs **roots**: parents, ancestry, childhood atmosphere. These early experiences create the emotional foundation from which we grow. **Successful navigation** means developing a secure inner base and healthy relationship with one's origins. **Unsuccessful navigation** leaves the person rootless, unable to feel at home anywhere, or trapped in unexamined family patterns.

#### Narrative Snippets

- `[ns_innersky_h4_001]` `[trigger: house_4_general]` `[factor_trigger: astro_house_4]` `[role: 主干]` The fourth house is the most subjective of the twelve. The arena it represents is a secret one. No one outside ourselves can see it. → The Inner Sky Ch.7 #4H
- `[ns_innersky_h4_002]` `[trigger: house_4_contents]` `[factor_trigger: astro_house_4]` `[role: 主干依赖]` The contents of the fourth house are utterly isolated from the outer world. They exist only in the mind. "Reality" is irrelevant to them. They grow and develop with a logic all their own. → The Inner Sky Ch.7 #4H
- `[ns_innersky_h4_003]` `[trigger: house_4_hero]` `[factor_trigger: astro_house_4 AND astro_archetype_hero]` `[role: 条件分支]` The Hero—a set of grandiose, imaginary self-images. Although they are always embarrassingly unrealistic, those images inspire us and help us understand what we really want. → The Inner Sky Ch.7 #4H
- `[ns_innersky_h4_004]` `[trigger: house_4_shadow]` `[factor_trigger: astro_house_4 AND astro_archetype_shadow]` `[role: 条件分支]` The Shadow draws a picture of the fear we are afraid to feel. Decode it, face it, and we establish balance between the inner self and the personality we present to those around us. → The Inner Sky Ch.7 #4H
- `[ns_innersky_h4_005]` `[trigger: house_4_home]` `[factor_trigger: astro_house_4]` `[role: 总结]` The fourth house describes our attitudes toward the haven we create from the noise of the world. That haven must be created if we are to touch the nadir. But homemaking is the means, not the end. → The Inner Sky Ch.7 #4H"""
    normalized_text_zh: str = """"""
    subject: str = "Fourth House - The Nadir (Inner Foundation)"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_fourth_house___the_nadir__inne_001_L1",
    )
    version: str = "1.0.0"
