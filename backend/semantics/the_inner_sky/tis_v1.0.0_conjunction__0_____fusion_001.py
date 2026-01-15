"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.109836
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
    semantic_id="tis_v1.0.0_conjunction__0_____fusion_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class Conjunction0Fusion(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Conjunction | 0° aspect, planets at same degree | Fusion of energies |
| Fusion | Blending of planetary principles | Combined expression |
| Intensification | Concentrated energy | Heightened manifestation |

#### Source Text

"The simplest of all the aspects is the conjunction. This occurs when two planets are right on top of each other. In such a case, the two planets fuse. It is as if they were in the same room talking with each other. Every time one of them acts, it acts through the other, and vice versa. The result is an intensification of both principles."

#### English Paraphrase (Primary Language)

The **conjunction** (0°) represents the most fundamental aspect relationship: **complete fusion** of two planetary energies. When planets occupy the same degree, they cannot act independently—every expression of one automatically involves the other. This creates **intensification**: the combined energy is greater than the sum of its parts.

**Function**: Planets in conjunction operate as a **unified force**. Mercury conjunct Mars means every thought (Mercury) is colored by assertion (Mars), and every action (Mars) is guided by mental strategy (Mercury).

**Key insight**: Forrest emphasizes that conjunction is not simply addition but **multiplication**—the planets amplify each other's expression, for better or worse.

#### Complete Chinese Interpretation (Secondary Language)

**合相**（0度）代表最基本的相位关系：两颗行星能量的**完全融合**。当行星占据同一度数时，它们无法独立行动——一方的每次表达都自动涉及另一方。这创造了**增强效应**：合并的能量大于各部分之和。

**功能**：合相中的行星作为**统一力量**运作。水星合火星意味着每个思想（水星）都带有主张色彩（火星），每个行动（火星）都由心智策略（水星）引导。

**关键洞见**：Forrest强调合相不是简单的加法而是**乘法**——行星相互放大彼此的表达，无论好坏。

#### Core Points

- **0° aspect**: Planets at same zodiacal degree
- **Fusion principle**: Energies blend into unified expression
- **Intensification**: Combined force greater than sum of parts
- **Inseparable action**: One planet cannot act without involving the other

#### Detailed Explanation

The conjunction represents the most primal of all aspect relationships—two planets sharing the same space and therefore the same moment of expression. Forrest's "room" metaphor captures the essential dynamic: the planets are in constant dialogue, unable to speak without the other hearing and responding. This has profound implications for interpretation.

First, **intensification** occurs not through addition but through multiplication. Sun conjunct Mars doesn't simply add will to identity; it creates an identity that is inherently martial, competitive, and action-oriented. The conjunction creates a **psychological complex** where the functions cannot be separated even in the person's own experience.

Second, the quality of the fusion depends entirely on the **nature of the planets involved**. Venus-Jupiter conjunctions tend toward excess generosity or indulgence; Saturn-Moon conjunctions may create emotional reserve or depth depending on development. The aspect itself is neutral—it simply says "these principles are one."

Third, conjunctions often represent **blind spots** precisely because the functions are so merged. The person may not recognize that their Mercury is always colored by Pluto, for instance—that intensity feels normal to them. Growth involves learning to consciously work with the fusion rather than being unconsciously driven by it.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Forrest's conjunction interpretation emphasizes fusion over domination. Traditional astrology often sees conjunction as the stronger planet "winning"—Forrest sees mutual amplification.
- **中文**: Forrest的合相诠释强调融合而非支配。传统占星常视合相为较强行星"获胜"——Forrest视之为相互放大。

**Narrative Snippets**:
- `[ns_forrest_asp_001]` `[trigger: conjunction]` `[factor_trigger: aspect_conjunction AND planetary_energy]` `[role: 主干]` The conjunction occurs when two planets fuse at the same degree, intensifying both principles into unified expression. → Source Text
- `[ns_forrest_asp_002]` `[trigger: fusion]` `[factor_trigger: aspect_conjunction AND planet_inseparable]` `[role: 主干依赖]` Planets in conjunction cannot act independently—every expression of one automatically involves the other. → English Paraphrase
- `[ns_forrest_asp_011]` `[trigger: intensification]` `[factor_trigger: aspect_conjunction AND aspect_multiplication]` `[role: 条件分支]` Conjunction is not addition but multiplication—the planets amplify each other's expression, for better or worse. → Key Insight
- `[ns_forrest_asp_012]` `[trigger: blind_spot]` `[factor_trigger: aspect_conjunction AND psychological_complex]` `[role: 条件分支]` Conjunctions often represent blind spots because the functions are so merged the person may not recognize the fusion. → Development"""
    normalized_text_zh: str = """"""
    subject: str = "Conjunction (0°) - Fusion"
    factor_refs: list = ['aspect_conjunction', 'new_candidate', 'new_candidate', 'engine_id', 'aspect_conjunction', 'astro_semantic', 'new_candidate', 'astro_semantic', 'new_candidate', 'astro_semantic', 'source_ref', 'rel_forrest_conj_001', 'aspect_conjunction', 'intensifying', 'rel_forrest_conj_002', 'aspect_conjunction', 'blending', 'evi_forrest_conj_001', 'rule_aspect_conjunction', 'concept_conjunction', 'tongzhu_same_pillar', 'fusion_dream']
    
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
        l1_anchor="tis_v1.0.0_conjunction__0_____fusion_001_L1",
    )
    version: str = "1.0.0"
