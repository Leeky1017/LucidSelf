"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.461010
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
    semantic_id="iod_v1.0.0_2_secondary_revision__sekund_r_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 2SecondaryRevisionSekundR(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Secondary Revision | Final stage | Near waking |
| Narrative Coherence | Makes tellable | Surface logic |
| False Front | Disguise of rationality | Warning for interpretation |
| Gaps/Contradictions | More revealing | Analytic value |

**English Paraphrase (Primary Language)**:

**Secondary revision** = the final stage of dream-work, occurring near waking, that imposes logical coherence on dream material.

**Characteristics**:
- Makes dream "tellable" as narrative.
- Fills gaps, smooths contradictions.
- Often produces **false front** of rationality.
- Operates closer to waking consciousness.

**Warning for interpretation**: The coherent story is often a **disguise**; the gaps and contradictions are analytically more revealing.

**Complete Chinese Interpretation (Secondary Language)**:

**次级修饰** = 梦的工作最后阶段，在接近醒来时发生，对梦材料强加逻辑一致性。

**特征**：
- 使梦可以作为叙事"讲述"。
- 填补空白，平滑矛盾。
- 常常产生理性的**虚假表面**。
- 更接近清醒意识运作。

**解读警告**：连贯的故事往往是**伪装**；空白和矛盾在分析上更有揭示性。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Secondary Revision: Final stage near waking, imposes narrative coherence. Makes dream "tellable." Warning: coherent story is often disguise; gaps and contradictions more revealing analytically.
- **中文**: 次级修饰:接近醒来的最后阶段,强加叙事连贯性。使梦"可讲述"。警告:连贯故事常是伪装;空白和矛盾在分析上更有揭示性。

**Narrative Snippets**:
- `[ns_freud_ch6_004]` `[trigger: secondary_revision]` `[factor_trigger: dream_work_revision]` `[role: 主干]` Secondary revision: final stage near waking; imposes narrative coherence on dream material. → Core
- `[ns_freud_ch6_005]` `[trigger: false_front]` `[factor_trigger: dream_work_revision AND rationality]` `[role: 条件分支]` False front of rationality; fills gaps, smooths contradictions; disguise mechanism. → Warning
- `[ns_freud_ch6_006]` `[trigger: gaps_revealing]` `[factor_trigger: dream_work_revision AND interpretation]` `[role: 条件分支]` Gaps and contradictions more revealing analytically than coherent surface story. → Principle"""
    normalized_text_zh: str = """"""
    subject: str = "2 Secondary Revision (Sekundäre Bearbeitung)"
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
        l1_anchor="iod_v1.0.0_2_secondary_revision__sekund_r_001_L1",
    )
    version: str = "1.0.0"
