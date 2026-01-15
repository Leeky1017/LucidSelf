"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.122574
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
    semantic_id="tis_v1.0.0_eighth_house___transformation__001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class EighthHouseTransformation(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Sex/Death/Occult Triad |...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Sex/Death/Occult Triad | Ego-instinct meeting | Core linkage |
| Pulling the Cork | Release instinct | Process |
| Occult Power | Latent energy | Access |
| Letting Go | Release control | Mastery |

#### Source Text

"Sex, death, and the occult—why linked? In each we confront an instinct. We pull the cork in the dam separating ego from instinct. Successful navigation depends on accepting the reality of feelings arising beyond personality. By acknowledging those instinctive feelings, we learn to flow with an 'occult power' that normally lies latent."

#### English Paraphrase

The **Eighth House** is the arena of **deep transformation, instinct, and merging**. It governs experiences where the ego loses control: sex, death, and the occult.

**The Common Thread: Instinct**:
In the 7th house, we meet a person. In the 8th, we meet an **instinctive force** that shatters our normal personality structure.
- **Sex**: Gut feelings, bonding, loss of boundaries.
- **Death**: The ultimate loss of control and personality dissolution.
- **Occult**: Encountering dimensions of reality that defy logic (life after death, psychic connection).

**Transformation**:
This house is about **ego death** and **rebirth**. It demands we surrender control to a greater power.

**Successful Navigation**:
- **Acceptance**: Acknowledging irrational, powerful feelings without being consumed by them.
- **Flow**: Learning to ride the waves of instinct rather than fighting them.
- **Depth**: Willingness to explore the taboo and hidden sides of life.

**Unsuccessful Navigation**:
- **Blockage**: Fear of intimacy, sexual dysfunction, terror of death.
- **Obsession**: Being consumed by jealousy, power struggles, or morbid fixations.

#### Complete Chinese Interpretation

**第八宫**是**深度转化、本能和融合**的领域。它掌管小我失去控制的体验：性、死亡和玄秘。

**共同线索：本能**：
在第七宫，我们遇见一个人。在第八宫，我们遇见一种**本能力量**，它粉碎了我们正常的人格结构。
- **性**：直觉感受、结合、边界的丧失。
- **死亡**：控制的终极丧失和人格的消解。
- **玄秘**：遭遇违背逻辑的现实维度（死后生命、通灵连接）。

**转化**：
这一宫是关于**小我死亡**和**重生**。它要求我们将控制权通过一个更大的力量。

**成功的驾驭**：
- **接受**：承认非理性的、强大的感觉，而不被它们吞噬。
- **流动**：学习驾驭本能的波浪而不是与之对抗。
- **深度**：愿意探索生活的禁忌和隐藏面。

**不成功的驾驭**：
- **阻塞**：对亲密的恐惧、性功能障碍、对死亡的恐惧。
- **痴迷**：被嫉妒、权力斗争或病态的固着所吞噬。

#### Core Points

- Arena of instinct, transformation, and ego death.
- Sex, Death, and Occult are linked by loss of ego control.
- Requires surrender and acceptance of irrational forces.
- East parallel: 疾厄宫/七杀/生死 (Health/Danger Palace, Power, Life/Death).

#### Detailed Explanation

The Eighth House links three seemingly disparate domains: **sex, death, and the occult**. Forrest's insight is that all three involve **confronting instinctual forces** that overwhelm ego control. In each, we meet something larger than personality—something primal and non-negotiable.

These experiences are **transformative** precisely because they disrupt ordinary consciousness. Sexual passion can sweep away rational thought; death forces us to face our mortality; occult experiences reveal dimensions beyond everyday perception. The ego must **surrender** to forces it cannot control.

**Successful navigation** means accepting the reality of these irrational forces rather than fighting or repressing them. Flow with sexuality rather than being its victim. Accept death as part of life rather than hiding from it. Remain open to mystery. **Unsuccessful navigation** produces either obsession (being controlled by these forces) or deadening (cutting oneself off from depth and passion).

#### Narrative Snippets

- `[ns_innersky_h8_001]` `[trigger: house_8_general]` `[factor_trigger: astro_house_8]` `[role: 主干]` Sex, death, and the occult—in each we confront one of the basic givens of human life. In each we confront needs and issues that release intense and disruptive emotional energies into consciousness. In each we meet an instinct. → The Inner Sky Ch.7 #8H
- `[ns_innersky_h8_002]` `[trigger: house_8_instinct]` `[factor_trigger: astro_house_8]` `[role: 主干依赖]` Once evoked, those feelings are virtually unstoppable. We have pulled the cork in the dam separating ego from instinct. → The Inner Sky Ch.7 #8H
- `[ns_innersky_h8_003]` `[trigger: house_8_mastery]` `[factor_trigger: astro_house_8 AND astro_state_success]` `[role: 条件分支]` A successful passage depends on accepting the reality of feelings arising beyond personality—accepting illogical feelings that may violate our accustomed description of the world. → The Inner Sky Ch.7 #8H
- `[ns_innersky_h8_004]` `[trigger: house_8_transformation]` `[factor_trigger: astro_house_8]` `[role: 条件分支]` Flow with the sexual force. Accept death. Integrate it. Learn from it instead of hiding from it. Grope within yourself for something immortal. Try to feel your 'soul.' → The Inner Sky Ch.7 #8H
- `[ns_innersky_h8_005]` `[trigger: house_8_failure]` `[factor_trigger: astro_house_8 AND astro_state_dysfunction]` `[role: 总结]` Fail, and those same instincts snag you. They make you moody and bitter, full of heaviness. You may have a beautiful mate or a million lovers—still, you are unsatisfied. → The Inner Sky Ch.7 #8H"""
    normalized_text_zh: str = """"""
    subject: str = "Eighth House - Transformation (Sex, Death, Occult)"
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
        l1_anchor="tis_v1.0.0_eighth_house___transformation__001_L1",
    )
    version: str = "1.0.0"
