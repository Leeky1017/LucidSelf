"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574967
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
    semantic_id="cw_v1.0.0_source_text_010",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "Synchronicity is the occurrence of two or more events that are causally unrelated yet are experienc...
    """
    
    original_text: str = """"Synchronicity is the occurrence of two or more events that are causally unrelated yet are experienced as occurring together in a meaningful manner. It points to a deeper order connecting psyche and matter."

#### English Paraphrase (Primary Language)

**Synchronicity** = **Meaningful coincidence** without causal connection.

**Definition**:
- Inner psychic event coincides with outer physical event
- No causal relationship between them
- Connected by **meaning**, not mechanism
- Example: Think of person → they call simultaneously

**Implications**:
- Challenges Western causality paradigm
- Suggests **Unus Mundus** (one world) underlying psyche and matter
- Psyche and matter are **complementary aspects** of same reality
- Archetypes operate in both domains

**Types of synchronicity**:
1. Coincidence of psychic state with simultaneous external event
2. Coincidence of psychic state with external event at distance
3. Coincidence of psychic state with future event

#### Complete Chinese Interpretation (Secondary Language)

**同步性** = 无因果联系的**有意义巧合**。

**定义**：
- 内在心理事件与外在物理事件同时发生
- 两者之间无因果关系
- 通过**意义**而非机制连接
- 例：想到某人 → 他们同时来电

**意涵**：
- 挑战西方因果范式
- 暗示心灵物质下存在**统一世界**
- 心灵与物质是同一实相的**互补面向**
- 原型在两个领域运作

**同步性类型**：
1. 心理状态与同时外部事件巧合
2. 心理状态与远距离外部事件巧合
3. 心理状态与未来事件巧合

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Synchronicity | Meaningful coincidence | Acausal connection |
| Unus Mundus | One world | Psyche-matter unity |
| Acausal | Not cause-effect | Challenges causality |
| Archetype | Operates in both | Bridges domains |

#### Core Points

- Synchronicity = meaningful coincidence without causation
- Connects psyche and matter through meaning
- Implies Unus Mundus (unified reality)
- Foundation for Jung's collaboration with physicist Pauli

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Synchronicity: Meaningful coincidence without causation. Inner-outer events connected by meaning. Implies Unus Mundus (one world). Challenges Western causality. Foundation for divination theory.
- **中文**: 同步性:无因果的有意义巧合。内外事件通过意义连接。暗示统一世界。挑战西方因果论。占卜理论基础。

**Narrative Snippets**:
- `[ns_jung_038]` `[trigger: synchronicity_principle]` `[factor_trigger: jung_synchronicity AND jung_acausal]` `[role: 主干]` Synchronicity is the occurrence of two or more causally unrelated events experienced as occurring together in a meaningful manner. → Core
- `[ns_jung_039]` `[trigger: unus_mundus]` `[factor_trigger: jung_unus_mundus AND jung_psyche_matter]` `[role: 条件分支]` It points to a deeper order connecting psyche and matter—the Unus Mundus (one world) underlying both domains. → Ontology
- `[ns_jung_040]` `[trigger: meaningful_coincidence]` `[factor_trigger: jung_meaning AND jung_coincidence AND jung_meaningful_coincidence]` `[role: 条件分支]` Inner psychic event coincides with outer physical event, connected by meaning not mechanism—foundation for divination theory. → Application"""
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
        l1_anchor="cw_v1.0.0_source_text_010_L1",
    )
    version: str = "1.0.0"
