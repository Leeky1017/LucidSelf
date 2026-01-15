"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.541698
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
    semantic_id="acu_v1.0.0_section_0__neurosis_vs_psychos_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class Section0NeurosisVsPsychos(SemanticEntry):
    """
    **Source Text** (¶489-495, Lines 7680-7711):

> [493] If the unconscious consisted of nothing but co...
    """
    
    original_text: str = """**Source Text** (¶489-495, Lines 7680-7711):

> [493] If the unconscious consisted of nothing but contents accidentally deprived of consciousness, one could identify the ego more or less with the totality of the psyche. But the situation is not quite so simple. Neither Janet nor Freud had any specifically psychiatric experience. In psychosis, the unconscious displays contents that are utterly different from conscious ones, so strange that nobody can understand them, neither the patient himself nor his doctors.
>
> [494] There is no field directly known to us from which we could derive certain pathological ideas. They are products whose nature is at first completely baffling. The material of a neurosis is understandable in human terms, but that of a psychosis is not.
>
> [495] Neurotic contents can be integrated without appreciable injury to the ego, but psychotic ideas cannot. They remain inaccessible, and ego-consciousness is more or less swamped by them.

**English Paraphrase**:
- Janet/Freud: no psychiatric experience, only neurosis
- Psychosis: unconscious displays utterly strange contents
- Neurosis material = understandable; Psychosis = not
- Neurotic contents = integrable; Psychotic = swamp the ego

**中文诠释**：
- 珍妮特/弗洛伊德：无精神科经验，仅研究神经症
- 精神病：无意识显示完全陌生的内容
- 神经症材料=可理解；精神病=不可理解
- 神经症内容=可整合；精神病=淹没自我

**Narrative Snippets**:
- `[ns_cw9i_VIII_000]` `[trigger: psychosis_neurosis]` `[factor_trigger: jung_psychosis AND jung_ego]` `[role: 主干]` Psychosis differs from neurosis: unconscious contents utterly strange, ego swamped by them. → ¶493-495"""
    normalized_text_zh: str = """"""
    subject: str = "Section 0: Neurosis vs Psychosis (¶489-495)"
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
        l1_anchor="acu_v1.0.0_section_0__neurosis_vs_psychos_001_L1",
    )
    version: str = "1.0.0"
