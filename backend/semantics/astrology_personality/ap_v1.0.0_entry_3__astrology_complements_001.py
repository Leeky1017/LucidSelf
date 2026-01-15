"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238375
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
    semantic_id="ap_v1.0.0_entry_3__astrology_complements_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3AstrologyComplements(SemanticEntry):
    """
    **Source Text** (Lines 15848-15870):
> Astrology, as we understand it, complements modern science, i...
    """
    
    original_text: str = """**Source Text** (Lines 15848-15870):
> Astrology, as we understand it, complements modern science, insofar as it deals essentially with the individual super-structure rather than with the generic-collective under-structure... it is able also to unveil the mystery of significance, which is a purely individual factor.
>
> What it is able to grasp of the life-process of becoming itself, is principally in terms of structural periods of destiny rather than in terms of set concrete events... it does not know events in themselves so much as crises in the curve of an individual destiny.
>
> This is what "life-interpretation" means. It is the perception of individual form and of individual significance by an evolving or individuating personality.

**Key Term Analysis**:
- **Complements science**: `individual super-structure` vs `generic under-structure`
- **Unveils significance**: `purely individual factor` / `mystery of significance`
- **Structural periods**: `not concrete events` / `crises in destiny curve`
- **Life-interpretation**: `individual form + significance` / `by individuating personality`

**English Paraphrase (Primary Language)**:
Astrology "complements modern science"—deals with "individual super-structure" vs science's "generic-collective under-structure."

Astrology "unveils the mystery of significance, which is a purely individual factor."

Grasps life-process "in terms of structural periods of destiny rather than set concrete events"—knows "crises in the curve of individual destiny."

"Life-interpretation = perception of individual form and significance by an evolving personality."

**Complete Chinese Interpretation (Secondary Language)**:
占星学"补充现代科学"——处理"个体上层结构"vs科学的"类属-集体下层结构"。

占星学"揭示意义的奥秘，这是一个纯粹的个体因素"。

把握生命过程"以命运的结构周期而非固定具体事件的术语"——知道"个体命运曲线中的危机"。

"生命解读 = 进化中的人格对个体形式和意义的感知。"

**Narrative Snippets**:
- `[ns_aop_221]` `[trigger: astro_science]` `[factor_trigger: astro_complement_science]` `[role: 主干]` Astrology complements science: individual super-structure vs generic under-structure. → L15848-15852
- `[ns_aop_222]` `[trigger: life_interpretation]` `[factor_trigger: astro_life_interp]` `[role: 总结]` Life-interpretation = perception of individual form and significance by individuating personality. → L15862-15870"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Astrology Complements Science - Individual vs Generic"
    factor_refs: list = ['super_struct', 'life_interp']
    
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
        l1_anchor="ap_v1.0.0_entry_3__astrology_complements_001_L1",
    )
    version: str = "1.0.0"
