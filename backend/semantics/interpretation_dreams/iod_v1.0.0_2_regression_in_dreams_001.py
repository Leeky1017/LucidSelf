"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.461033
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
    semantic_id="iod_v1.0.0_2_regression_in_dreams_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 2RegressionInDreams(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Regression | Reversal of direction | Key dream mechanism |
| Topographical | Backward through systems | Spatial regression |
| Temporal | Revival of infantile | Historical regression |
| Formal | Primitive expression | Mode regression |

**English Paraphrase (Primary Language)**:

**Regression** = the reversal of psychical direction during sleep, from motor output back toward perception.

| Regression Type | Description |
|-----------------|-------------|
| **Topographical** | Excitation moves backward through systems |
| **Temporal** | Revival of earlier (infantile) psychical structures |
| **Formal** | Primitive modes of expression replace verbal thought |

**Why regression occurs**:
1. Motor output is blocked during sleep.
2. Unconscious wishes cannot discharge forward.
3. Excitation flows backward → reaches perceptual system.
4. Result: **hallucinatory wish-fulfillment**.

**Complete Chinese Interpretation (Secondary Language)**:

**回退** = 睡眠期间心理方向的逆转，从运动输出回到知觉。

| 回退类型 | 描述 |
|---------|------|
| **地形的** | 兴奋通过系统向后移动 |
| **时间的** | 早期（婴儿期）心理结构复活 |
| **形式的** | 原始表达模式取代言语思想 |

**为何发生回退**：
1. 睡眠期间运动输出被阻断。
2. 无意识愿望无法向前释放。
3. 兴奋向后流动 → 到达知觉系统。
4. 结果：**幻觉性愿望满足**。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Regression: Reversal of psychical direction during sleep. Three types: topographical (backward through systems), temporal (infantile revival), formal (primitive modes). Motor blocked→backward flow→hallucination.
- **中文**: 回退:睡眠期间心理方向的逆转。三种类型:地形的(通过系统向后)、时间的(婴儿期复活)、形式的(原始模式)。运动阻断→向后流动→幻觉。

**Narrative Snippets**:
- `[ns_freud_ch7_004]` `[trigger: regression]` `[factor_trigger: dream_regression]` `[role: 主干]` Regression: reversal of psychical direction during sleep; motor blocked, excitation flows backward. → Core
- `[ns_freud_ch7_005]` `[trigger: three_types]` `[factor_trigger: dream_regression AND classification]` `[role: 条件分支]` Three types: topographical (backward through systems), temporal (infantile revival), formal (primitive modes). → Structure
- `[ns_freud_ch7_006]` `[trigger: hallucinatory_result]` `[factor_trigger: dream_regression AND perception]` `[role: 条件分支]` Backward flow reaches perceptual system; result = hallucinatory wish-fulfillment. → Outcome"""
    normalized_text_zh: str = """"""
    subject: str = "2 Regression in Dreams"
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
        l1_anchor="iod_v1.0.0_2_regression_in_dreams_001_L1",
    )
    version: str = "1.0.0"
