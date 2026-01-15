"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237832
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
    semantic_id="ap_v1.0.0_entry_11__intuition_as_holisti_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry11IntuitionAsHolisti(SemanticEntry):
    """
    **Source Text** (Lines 2699-2753):
> This is perhaps only a symbol, but it indicates the consummatio...
    """
    
    original_text: str = """**Source Text** (Lines 2699-2753):
> This is perhaps only a symbol, but it indicates the consummation of the process which extols exclusively intellectual logic, and the analytical, causalistic attitude of the mind. In opposition to this we see the development of the faculty of intuition, which is the power to identify oneself with the whole-making power of time.
>
> [C. G. Jung:] "Intuition is a kind of instinctive apprehension, irrespective of the nature of its contents.... Through intuition any one content is presented as a complete whole.... Intuitive cognition possesses an intrinsic nature of certainty and conviction..."
>
> The best definition would seem to us to be that intuition is holistic perception. It can also be defined as awareness of self. It is the faculty which enables us to be aware of the self (the wholeness) of any whole. It is thus opposed to sensations, which are always fragmentary and therefore need the causal logic of the intellect...
>
> Astrology is based upon one of these intuitive realizations identifying "order" and "the celestial motions of the stars." The conceptual quality of "order" was latent in the unconscious. It was the psychological result of a yearning to find a compensation for the apparent chaos of every-day existence... All intuitions are based on symbols.

**Key Term Analysis**:
- **Intuition**: `holistic perception` / `awareness of self` / `whole-making power identification`
- **Jung's definition**: `instinctive apprehension` / `content as complete whole` / `certainty and conviction`
- **Intuition vs sensation**: `whole vs fragmentary` / `holistic logic vs causal logic`
- **Astrology's basis**: `intuitive realization` / `"order" + "celestial motions"` / `symbol-based`
- **Symbol origin**: `inner yearning` + `outer perception` = `identity` / `all intuitions based on symbols`

**English Paraphrase (Primary Language)**:
Rudhyar introduces intuition as the faculty opposed to intellectual logic. Jung defines it: "instinctive apprehension... content presented as complete whole... intrinsic certainty." Rudhyar's definition: "intuition is holistic perception"—awareness of the self (wholeness) of any whole.

Intuition opposes sensations (fragmentary, needing causal logic). Intuition operates through "holistic logic"—a different kind of tautology where a whole is identified with a quality (knowing intuitively a man is honest = man and honesty become identical).

Astrology's foundation is an intuitive realization: "order" and "celestial motions" became identified as symbols of each other. Inner yearning (for compensation to chaos) + outer perception (regular celestial movements) = symbolic identity. "All intuitions are based on symbols."

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar介绍直觉作为与知性逻辑对立的能力。Jung定义它："本能的理解……内容作为完整整体呈现……内在的确定性。"Rudhyar的定义："直觉是整体性感知"——对任何整体的自我（整体性）的觉知。

直觉与感觉（碎片化的，需要因果逻辑）相对。直觉通过"整体论逻辑"运作——一种不同的同义反复，其中整体与品质被等同（直觉地知道一个人诚实=人与诚实成为一体）。

占星学的基础是一种直觉实现："秩序"与"天体运动"被等同为彼此的象征。内在渴望（对混沌的补偿）+外在感知（规律的天体运动）=象征性同一。"所有直觉都基于符号。"

**Core Points**:
- Intuition = holistic perception, awareness of wholeness
- Jung: instinctive apprehension, content as complete whole
- Opposed to fragmentary sensations
- Works through holistic logic, not causal logic
- Identifies wholes with qualities
- Astrology founded on intuition: order + celestial motions
- Inner yearning + outer perception = symbolic identity
- All intuitions based on symbols

**Narrative Snippets**:
- `[ns_aop_097]` `[trigger: intuition_defined]` `[factor_trigger: intuition AND astro_intuition_struct]` `[role: 主干]` Intuition = holistic perception, awareness of self/wholeness—power to identify with whole-making. → L2701-2721
- `[ns_aop_098]` `[trigger: jung_intuition]` `[factor_trigger: sensation AND intuition]` `[role: 主干依赖]` Jung: intuition presents content as complete whole, has intrinsic certainty and conviction. → L2713-2717
- `[ns_aop_099]` `[trigger: astrology_foundation]` `[factor_trigger: celestial_motion AND order_celest_identity AND astro_order_celest AND astro_symbol_form AND astro_symbol_def]` `[role: 条件分支]` Astrology based on intuitive realization: "order" identified with "celestial motions." → L2746-2752
- `[ns_aop_100]` `[trigger: symbols_basis]` `[factor_trigger: astro_symbols AND astro_symbol_form]` `[role: 总结]` Inner yearning + outer perception = symbolic identity. All intuitions based on symbols. → L2750-2753"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 11: Intuition as Holistic Perception"
    factor_refs: list = ['astro_intuition', 'astro_symbol_intuit', 'astro_found_order']
    
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
        l1_anchor="ap_v1.0.0_entry_11__intuition_as_holisti_001_L1",
    )
    version: str = "1.0.0"
