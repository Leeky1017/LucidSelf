"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515585
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
    semantic_id="acu_v1.0.0_1_definition___88_92_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1Definition8892(SemanticEntry):
    """
    **Source Text** (¶88-92, Lines 1507-1573):

> [88] Personal unconscious: contents once conscious but...
    """
    
    original_text: str = """**Source Text** (¶88-92, Lines 1507-1573):

> [88] Personal unconscious: contents once conscious but forgotten/repressed. Collective unconscious: contents never in consciousness, owe existence exclusively to heredity. Personal = complexes. Collective = archetypes.
>
> [89] Archetype = definite forms in psyche present always and everywhere. Called "motifs," "représentations collectives," "elementary thoughts." Archetype = "pre-existent form."
>
> [90] My thesis: Besides immediate consciousness, there exists a second psychic system—collective, universal, impersonal, identical in all individuals, inherited.
>
> [92] Hypothesis of CU is no more daring than assuming instincts exist. This is empirical, not speculative.

**English Paraphrase**:
- **Personal vs Collective**: Acquired vs Inherited; Complexes vs Archetypes
- **Archetype**: Pre-existent forms present always and everywhere
- **Thesis**: Second psychic system—universal, identical in all, inherited
- **Defense**: No more daring than instinct hypothesis; empirical

**中文释义**：
- **个人vs集体**：获得的vs遗传的；情结vs原型
- **原型**：始终处处存在的先存形式
- **论点**：第二心理系统——普遍、所有人相同、遗传
- **辩护**：不比本能假设更大胆；经验的"""
    normalized_text_zh: str = """"""
    subject: str = "1 Definition (¶88-92)"
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
        l1_anchor="acu_v1.0.0_1_definition___88_92_001_L1",
    )
    version: str = "1.0.0"
