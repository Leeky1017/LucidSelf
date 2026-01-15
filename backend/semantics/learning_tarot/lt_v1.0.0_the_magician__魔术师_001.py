"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.007964
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
    semantic_id="lt_v1.0.0_the_magician__魔术师_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheMagician魔术师(SemanticEntry):
    """
    **Source Text** (Lines 3523-3590):
> **Keywords**: Action • Conscious Awareness • Concentration • Po...
    """
    
    original_text: str = """**Source Text** (Lines 3523-3590):
> **Keywords**: Action • Conscious Awareness • Concentration • Power
>
> **Actions**:
> - **Taking Action**: doing what needs to be done, realizing your potential, making what's possible real, practicing what you preach, carrying out plans, producing magical results, using your talents
> - **Acting Consciously**: knowing what you are doing and why, acknowledging your motivations, understanding your intentions, examining the known situation
> - **Concentrating**: having singleness of purpose, being totally committed, applying the force of your will, feeling centered, setting aside distractions, focusing on a goal
> - **Experiencing Power**: making a strong impact, having vitality, creating miracles, becoming energized, feeling vigorous, being creative
>
> **Description**: The Magician is the archetype of the active, masculine principle—the ultimate achiever. He symbolizes the power to tap universal forces and use them for creative purposes. Note his stance in the picture. He acts as a lightning rod—one arm extended up into the Divine for inspiration, the other pointing toward Earth to ground this potent energy.

**Key Term Analysis**:
- **The Magician (1)**: `active masculine principle` / `ultimate achiever` / `lightning rod`
- **Action**: `doing what needs to be done` / `realizing potential` / `making possible real`
- **Conscious Awareness**: `knowing what you are doing and why` / `understanding intentions`
- **Concentration**: `singleness of purpose` / `totally committed` / `applying will`
- **Power**: `tap universal forces` / `creative purposes` / `creating miracles`

**English Paraphrase (Primary Language)**:
**The Magician (Card 1)** is "the archetype of the active, masculine principle—the ultimate achiever." He represents the power to channel divine inspiration into earthly manifestation.

**Key aspects**:
1. **Action**: "Doing what needs to be done, realizing your potential, making what's possible real." The Magician doesn't just dream—he manifests.

2. **Conscious Awareness**: "Knowing what you are doing and why." Unlike the Fool's unconscious trust, the Magician operates with full awareness of his motivations and intentions.

3. **Concentration**: "Having singleness of purpose, being totally committed, applying the force of your will." Focus is the Magician's tool for channeling power.

4. **Power**: "He acts as a lightning rod—one arm extended up into the Divine for inspiration, the other pointing toward Earth to ground this potent energy."

**Reading implication**: "This card is a signal to act and act now, provided you understand exactly what you want and are committed to getting it."

**Complete Chinese Interpretation (Secondary Language)**:
**魔术师（第1号牌）**是"主动、阳性原则的原型——终极成就者"。他代表将神圣灵感引导到尘世显化的力量。

**关键方面**：
1. **行动**："做需要做的事，实现你的潜能，让可能变为现实。"魔术师不只是做梦——他显化梦想。

2. **意识觉知**："知道你在做什么以及为什么。"不同于愚者的无意识信任，魔术师以对其动机和意图的完全觉知来运作。

3. **专注**："目标单一，完全投入，运用意志力。"专注是魔术师引导力量的工具。

4. **力量**："他充当避雷针——一只手臂向上伸向神圣以获取灵感，另一只手指向大地以接地这股强大能量。"

**解读含义**："这张牌是立即行动的信号，前提是你确切知道自己想要什么并致力于获得它。"

**Core Points**:
- Card 1 = active masculine principle, ultimate achiever
- Action: making what's possible real, manifesting potential
- Conscious Awareness: knowing what and why, understanding intentions
- Concentration: singleness of purpose, applying will
- Power: lightning rod between Divine and Earth

**Narrative Snippets**:
- `[ns_ltt_023]` `[trigger: magician_card]` `[factor_trigger: tarot_magician]` `[role: 主干]` The Magician is the archetype of the active, masculine principle—the ultimate achiever who symbolizes the power to tap universal forces for creative purposes. → L3573-3575
- `[ns_ltt_024]` `[trigger: magician_action]` `[factor_trigger: tarot_magician AND tarot_action AND conscious_awareness]` `[role: 主干依赖]` This card is a signal to act and act now, provided you understand exactly what you want and are committed to getting it. → L3587-3588
- `[ns_ltt_025]` `[trigger: magician_channel]` `[factor_trigger: tarot_magician AND tarot_power AND power]` `[role: 条件分支]` He acts as a lightning rod—one arm extended up into the Divine for inspiration, the other pointing toward Earth to ground this potent energy. → L3575-3577
- `[ns_ltt_026]` `[trigger: magician_focus]` `[factor_trigger: tarot_magician AND tarot_concentration AND concentration]` `[role: 总结]` The Magician can focus with single-minded determination—as long as he remembers the divine source of his power, he remains the perfect conduit for miracles. → L3583-3585"""
    normalized_text_zh: str = """"""
    subject: str = "The Magician (魔术师)"
    factor_refs: list = ['tarot_magician', 'conscious_awareness', 'concentration', 'power']
    
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_the_magician__魔术师_001_L1",
    )
    version: str = "1.0.0"
