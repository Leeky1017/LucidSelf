"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482465
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
    semantic_id="iod_v1.0.0_source_text_012",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "Certain dreams occur with almost identical content in different persons. The dream of nakedness, of...
    """
    
    original_text: str = """"Certain dreams occur with almost identical content in different persons. The dream of nakedness, of flying, of falling, of examination, of being pursued—these are typical dreams whose content derives from common human experiences and universal symbols."

#### English Paraphrase (Primary Language)

**Typical Dreams** = Dreams with **nearly identical content** across different individuals.

**Common types**:

| Dream Type | Content | Underlying Wish/Conflict |
|------------|---------|-------------------------|
| **Nakedness** | Being undressed in public | Exhibition wish vs shame |
| **Flying** | Floating, soaring | Power, freedom, sexual sensation |
| **Falling** | Falling from height | Loss of control, anxiety about failure |
| **Examination** | Unprepared for test | Fear of inadequacy, imposter feelings |
| **Pursuit** | Being chased | Repressed impulses pursuing ego |
| **Death of loved ones** | Parent/sibling dies | Childhood death wishes (Oedipal) |
| **Teeth falling out** | Teeth crumbling | Castration anxiety, aging fears |

**Why universal**:
- Derive from **common human experiences** (childhood development)
- Tap into **universal symbols** (shared body experiences)
- Express **species-wide conflicts** (Oedipus complex, sibling rivalry)

#### Complete Chinese Interpretation (Secondary Language)

**典型梦** = 不同个体内容**几乎相同**的梦。

**常见类型**：

| 梦类型 | 内容 | 潜在愿望/冲突 |
|--------|------|---------------|
| **裸体** | 公开场合赤身裸体 | 暴露愿望 vs 羞耻 |
| **飞翔** | 漂浮、翱翔 | 权力、自由、性快感 |
| **坠落** | 从高处坠落 | 失控、对失败的焦虑 |
| **考试** | 考试时毫无准备 | 对不足的恐惧、冒充者感 |
| **追逐** | 被追赶 | 被压抑的冲动追逐自我 |
| **亲人死亡** | 父母/兄弟姐妹死亡 | 童年死亡愿望（俄狄浦斯） |
| **牙齿脱落** | 牙齿崩碎 | 阉割焦虑、衰老恐惧 |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_freud_typical_dreams | dream_mechanism | dream_typical_dream | unconscious | Psychodynamic | When dream formation mechanism reveals unconscious content | revealing | Freud #Dreams |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_freud_typical_dreams | "Interpretation of Dreams" | dream_typical_dream | Mechanism -> manifestation | Dream theory | High | Yes | rule_freud_typical_dreams |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_freud_typical_dreams | Dream mechanism | | | dream_analysis | psychoanalysis | Freud |
<!-- L2.5_END -->

**为何普遍**：
- 源于**共同人类经验**（童年发展）
- 利用**普遍象征**（共享身体经验）
- 表达**种属层面冲突**（俄狄浦斯情结、兄弟姐妹竞争）

#### Core Points

- Typical dreams have nearly identical content across individuals
- Universal because derived from common developmental experiences
- Each type expresses specific underlying wish or conflict
- Foundation for dream symbol dictionaries

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Typical Dreams | Universal content | Cross-individual |
| Nakedness Dream | Public exposure | Exhibition vs shame |
| Examination Dream | Unprepared for test | Inadequacy fear |
| Flying/Falling Dream | Power/loss of control | Freedom or anxiety |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Typical dreams: universal content (nakedness, flying, falling, examination, pursuit). From common developmental experiences. Express species-wide conflicts.
- **中文**: 典型梦:普遍内容(裸体,飞翔,坠落,考试,追逐)。源于共同发展经历。表达种属层面冲突。"""
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_source_text_012_L1",
    )
    version: str = "1.0.0"
