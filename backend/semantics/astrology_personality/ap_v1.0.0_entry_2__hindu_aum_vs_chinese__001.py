"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237934
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
    semantic_id="ap_v1.0.0_entry_2__hindu_aum_vs_chinese__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2HinduAumVsChinese(SemanticEntry):
    """
    **Source Text** (Lines 4471-4612):
> The Aryan-Hindu Formula: India represents typically the attitud...
    """
    
    original_text: str = """**Source Text** (Lines 4471-4612):
> The Aryan-Hindu Formula: India represents typically the attitude of devotion; that is, the dependence upon the One-that-is-in-the-beginning... the formula of the world-process is given as: "The Self —is not—the Not-Self." The integration is reached by denial and renunciation...
>
> The Chinese Formula: This system... emphasizes the reality of the "process" and the dualism involved therein. Yang and Yin, the two cosmic polarities, are seen in their cyclic interplay. Time is no longer the fatality that forces the spirit into reincarnation, but is the basic reality of the process of change...
>
> TAO is the solution of all conflicts; and therefore it is not a thing or even an essence, but a process. It is the Process in the Head; the going of the Initiate up the steps that lead to the top of the pyramid...

**Key Term Analysis**:
- **Hindu AUM formula**: `devotion to One-in-Beginning` / `Self is not Not-Self` / `denial/renunciation` / `time as fatality`
- **Chinese TAO formula**: `process emphasis` / `Yang-Yin interplay` / `time as reality` / `equilibrium/balance`
- **TAO meaning**: `Process in Head` / `Conscious Way` / `solution of conflicts` / `T-A-O = process-monad-Self`

**English Paraphrase (Primary Language)**:
Rudhyar contrasts two civilization formulas. Hindu AUM emphasizes the "One-in-the-beginning"—integration through denial ("Self is not Not-Self"), renunciation, and devotion. Time = fatality, karma, misery.

Chinese TAO emphasizes the "process"—Yang-Yin cyclic interplay, time as basic reality of change. TAO = "the solution of all conflicts... a process... the Process in the Head." T = process of becoming; A = monad; O = Self/consummation. The sage equilibrates polarities within himself.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar对比了两种文明公式。印度AUM强调"始于一"——通过否定（"自我不是非自我"）、弃绝和虔诚来整合。时间=宿命、业力、苦难。

中国TAO强调"过程"——阴阳周期性相互作用，时间作为变化的基本实在。TAO="一切冲突的解决……一个过程……头脑中的过程。"T=成为的过程；A=单子；O=自性/圆满。圣人在自身内平衡对立面。

**Narrative Snippets**:
- `[ns_aop_125]` `[trigger: hindu_aum]` `[factor_trigger: astro_hindu_aum AND astro_two_formulas]` `[role: 主干]` Hindu AUM: devotion to One-in-Beginning, denial/renunciation, time as fatality. → L4471-4524
- `[ns_aop_126]` `[trigger: chinese_tao]` `[factor_trigger: astro_chinese_tao AND astro_two_formulas]` `[role: 主干依赖]` Chinese TAO: process emphasis, Yang-Yin interplay, time as reality, equilibrium. → L4542-4612"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Hindu AUM vs Chinese TAO Formulas"
    factor_refs: list = ['astro_hindu_aum', 'astro_chinese_tao']
    
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
        l1_anchor="ap_v1.0.0_entry_2__hindu_aum_vs_chinese__001_L1",
    )
    version: str = "1.0.0"
