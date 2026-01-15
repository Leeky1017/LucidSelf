"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237771
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
    semantic_id="ap_v1.0.0_entry_5__astrology_as_formal_s_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry5AstrologyAsFormalS(SemanticEntry):
    """
    **Source Text** (Lines 2014-2058):
> Astrology Compared to Logic and Mathematics... Mathematics, it ...
    """
    
    original_text: str = """**Source Text** (Lines 2014-2058):
> Astrology Compared to Logic and Mathematics... Mathematics, it is said, is concerned with symbols, the truth or falsehood of which can be known without studying the outside world. Mathematical propositions are thus purely formal...
>
> If, now, we come back to our definition of astrology as the algebra of life, we shall make our meaning plainer by stating that astrology is to all the empirical sciences dealing with the formation, growth, behavior and disintegration of organic wholes what mathematics is to physics and in general to sciences of inanimate objects.
>
> Astrology of itself has no more meaning than algebra. It measures relationships between symbols whose concreteness is entirely a matter of convention... The astrologers use terms like opposition, conjunction, squares, exactly as the mathematician uses signs of addition and multiplication...
>
> In other words, the astrological realm of moving celestial bodies is like the realm of logical propositions. Neither one nor the other has any real content. Both are purely formal, symbolical, and conventional. They acquire real value only in function of the actual living experiences which they serve to correlate. Alone, astrology and mathematics are without substance. But they invest with coherence, pattern, logic and order whatever substantial reality is associated with them.

**Key Term Analysis**:
- **Astrology = mathematics for organic sciences**: `what math is to physics` / `astrology is to organic wholes` / `structural parallel`
- **Purely formal**: `no real content` / `symbolic, conventional` / `like logical propositions`
- **Without substance alone**: `acquires value through association` / `invests coherence on reality`
- **Operational symbols**: `opposition = addition` / `conjunction = multiplication` / `progressions = calculus`

**English Paraphrase (Primary Language)**:
Rudhyar's pivotal formulation: "astrology is to all empirical sciences dealing with organic wholes what mathematics is to physics." Just as mathematics is purely formal—concerned with symbols whose truth can be known without studying the outside world—so is astrology.

The astrological realm has no more real content than logical propositions. Oppositions, conjunctions, squares function like addition and multiplication signs. Without connection to actual experience, astrology is "without substance"—but when associated with living reality, it invests coherence, pattern, logic, and order.

This is the fundamental reconception: astrology doesn't cause or predict—it measures and correlates. It brings formal order to the chaos of organic processes.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar的核心表述："占星学之于所有处理有机整体的经验科学，如同数学之于物理学。"正如数学是纯形式的——关注可以不研究外部世界就能知道其真假的符号——占星学也是如此。

占星领域没有比逻辑命题更多的真实内容。对冲、合相、四分相如同加法和乘法符号。没有与实际经验的联系，占星学是"无实体的"——但当与活生生的现实关联时，它赋予连贯性、模式、逻辑和秩序。

这是根本性的重新概念化：占星学不是导致或预测——它测量和关联。它为有机过程的混沌带来形式秩序。

**Core Points**:
- Astrology : organic sciences = mathematics : physics
- Both purely formal, symbolic, conventional
- No real content—like logical propositions
- Acquires value through association with experience
- Invests coherence, pattern, logic, order on reality
- Opposition, conjunction, squares = operational symbols
- Astrology measures and correlates, doesn't cause

**Narrative Snippets**:
- `[ns_aop_073]` `[trigger: math_parallel]` `[factor_trigger: mathematics AND organic_reality]` `[role: 主干]` Astrology : organic sciences = mathematics : physics—purely formal symbolic system. → L2026-2031
- `[ns_aop_074]` `[trigger: no_content]` `[factor_trigger: astro_no_content]` `[role: 主干依赖]` Astrological realm like logical propositions—no real content, purely formal, conventional. → L2049-2052
- `[ns_aop_075]` `[trigger: operational_symbols]` `[factor_trigger: astro_operations]` `[role: 条件分支]` Opposition, conjunction, squares = addition, multiplication—operational symbols. → L2036-2039
- `[ns_aop_076]` `[trigger: invests_order]` `[factor_trigger: astro_invests AND astro_order_invest]` `[role: 总结]` Alone without substance; but invests coherence, pattern, logic, order on associated reality. → L2053-2058"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 5: Astrology as Formal Symbolic System—Like Mathematics"
    factor_refs: list = ['astro_math_parallel', 'astro_purely_formal', 'astro_operations', 'astro_invests_order']
    
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
        l1_anchor="ap_v1.0.0_entry_5__astrology_as_formal_s_001_L1",
    )
    version: str = "1.0.0"
