"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515562
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
    semantic_id="acu_v1.0.0_1_the_symbolic_process___80_82_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1TheSymbolicProcess8082(SemanticEntry):
    """
    **Source Text** (¶80-82, Lines 1393-1441):

> [80] The three archetypes—shadow, anima, wise old man—...
    """
    
    original_text: str = """**Source Text** (¶80-82, Lines 1393-1441):

> [80] The three archetypes—shadow, anima, wise old man—can be directly experienced in personified form. But there is another class: the archetypes of transformation. They are not personalities, but typical situations, places, ways and means, that symbolize transformation. They are genuine symbols—ambiguous, full of half-glimpsed meanings, inexhaustible.
>
> [81] Examples: alchemy series, Tantric chakras, Chinese yoga nerve system, Tarot cards—all "descended from the archetypes of transformation."
>
> [82] The symbolic process shows an enantiodromian structure like the I Ching: rhythm of negative/positive, dark/light. Beginning = stuck in blind alley. Goal = illumination or higher consciousness. Chief danger: succumbing to archetypes' fascinating influence, especially when not made conscious—can produce possession.

**English Paraphrase (Primary Language)**:

- **Two kinds**: Personified (shadow, anima, wise old man) vs Transformation (situations, places, means)
- **Examples**: Alchemy, Tantric chakras, Chinese yoga, Tarot
- **Symbolic process**: Enantiodromia (I Ching pattern); negative↔positive alternation
- **Danger**: Archetype possession when not made conscious

**中文释义**：
- **两类**：人格化（阴影、阿尼玛、智慧老人）vs 转化（情境、地点、手段）
- **例子**：炼金术、密宗脉轮、中国瑜伽、塔罗
- **象征过程**：对转（易经模式）；负↔正交替
- **危险**：未意识化时的原型附身

**Narrative Snippets**:
- `[ns_cw9i_062]` `[trigger: transformation_archetypes]` `[factor_trigger: jung_archetype AND jung_transformation]` `[role: 主干]` Archetypes of transformation are not personalities but typical situations that symbolize transformation. → ¶80
- `[ns_cw9i_063]` `[trigger: enantiodromia]` `[factor_trigger: jung_opposites AND jung_iching]` `[role: 主干依赖]` Symbolic process shows enantiodromian structure like I Ching—rhythm of opposites. → ¶82"""
    normalized_text_zh: str = """"""
    subject: str = "1 The Symbolic Process (¶80-82)"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_1_the_symbolic_process___80_82_001_L1",
    )
    version: str = "1.0.0"
