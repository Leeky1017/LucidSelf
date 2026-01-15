"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574940
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
    semantic_id="cw_v1.0.0_source_text_007",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "The two fundamental attitudes are introversion, in which psychic energy flows inward toward the sub...
    """
    
    original_text: str = """"The two fundamental attitudes are introversion, in which psychic energy flows inward toward the subject, and extraversion, in which it flows outward toward objects. Everyone possesses both attitudes, but one typically dominates as the superior attitude."

#### English Paraphrase (Primary Language)

**Introversion vs Extraversion** = Two **fundamental attitudes** of psychic energy orientation.

**Extraversion**: Energy flows **outward** toward objects and external world. Characteristics:
- Interest in people, events, things
- Action-oriented, sociable
- Draws energy from external engagement
- Reality = objective world

**Introversion**: Energy flows **inward** toward subject and inner world. Characteristics:
- Interest in inner thoughts, feelings, reflections
- Contemplative, reserved
- Draws energy from solitude and reflection
- Reality = subjective experience

**Key points**:
- Everyone has both attitudes; one dominates (superior attitude)
- The inferior attitude operates unconsciously
- Not good/bad, just different orientations
- Cultural bias often favors extraversion

#### Complete Chinese Interpretation (Secondary Language)

**内向与外向** = 两种**基本态度**，决定心理能量的流向。

**外向**：能量向**外**流向客体和外部世界。特征：
- 对人、事件、事物感兴趣
- 行动导向、善交际
- 从外在互动中获得能量
- 现实 = 客观世界

**内向**：能量向**内**流向主体和内心世界。特征：
- 对内在思想、感受、反思感兴趣
- 沉思、内敛
- 从独处和反思中获得能量
- 现实 = 主观体验

**要点**：
- 人人皆有两种态度；一种主导（优势态度）
- 劣势态度在无意识中运作
- 无好坏之分，只是不同取向
- 文化偏见常偏好外向

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Extraversion | Energy toward objects | Outward orientation |
| Introversion | Energy toward subject | Inward orientation |
| Superior Attitude | Dominant conscious | Primary mode |
| Inferior Attitude | Unconscious opposite | Shadow gateway |

#### Core Points

- Two fundamental attitudes: extraversion (outward) and introversion (inward)
- Everyone has both; one dominates consciously
- Inferior attitude operates unconsciously
- Foundation for psychological type theory

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Introversion/Extraversion: Two fundamental attitudes of psychic energy. Energy flows outward (extraversion) or inward (introversion). Everyone has both; one dominates. Inferior operates unconsciously. Foundation for type theory.
- **中文**: 内向/外向:两种心理能量基本态度。能量向外(外向)或向内(内向)流动。人人皆有;一种主导。劣势在无意识中运作。类型理论基础。

**Narrative Snippets**:
- `[ns_jung_029]` `[trigger: fundamental_attitudes]` `[factor_trigger: jung_extraversion AND jung_introversion AND jung_ei_axis]` `[role: 主干]` Two fundamental attitudes: extraversion (energy flows outward toward objects) and introversion (energy flows inward toward subject). → Core
- `[ns_jung_030]` `[trigger: superior_inferior]` `[factor_trigger: jung_superior_attitude AND jung_inferior_attitude]` `[role: 条件分支]` Everyone possesses both attitudes but one dominates as superior; the inferior attitude operates unconsciously. → Balance
- `[ns_jung_031]` `[trigger: energy_direction]` `[factor_trigger: jung_libido AND jung_orientation]` `[role: 条件分支]` Psychic energy orientation determines personality's basic stance—outward engagement or inward reflection. → Function"""
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
        l1_anchor="cw_v1.0.0_source_text_007_L1",
    )
    version: str = "1.0.0"
