"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237962
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
    semantic_id="ap_v1.0.0_entry_5__from_collective_to_co_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry5FromCollectiveToCo(SemanticEntry):
    """
    **Source Text** (Lines 4943-4972):
> Again, what makes matters rather complex is that individuation ...
    """
    
    original_text: str = """**Source Text** (Lines 4943-4972):
> Again, what makes matters rather complex is that individuation and collectivation operate at various levels and dovetail into each other. But if we grasp the following formula, an Ariadne thread may lead us safely through the labyrinth of the cyclic life-process: this life-process is from collective to collective through the individual. But we might also say: from any level of individuation to the next higher level through the creative. The first formulation is from the standpoint of substance; the second, from that of spirit, or unity.
>
> If we take the formulation according to spirit, we have the cyclic formula mentioned at the beginning of this chapter; beginning-middle-end; or God-of-the-beginning—the dualistic life-process—God-of-the-end; or Seed-plant-seed; or monad-personality-Self, psychologically speaking.

**Key Term Analysis**:
- **Substance formula**: `collective → individual → collective` / `life-process`
- **Spirit formula**: `individuation → creative → higher individuation` / `beginning-middle-end`
- **Parallel symbols**: `God-beginning / life-process / God-end` / `Seed-plant-seed` / `Monad-personality-Self`

**English Paraphrase (Primary Language)**:
Rudhyar offers two complementary formulas as "Ariadne thread" through the labyrinth:
1. **Substance view**: "from collective to collective through the individual"
2. **Spirit view**: "from any level of individuation to the next higher level through the creative"

These parallel: Beginning-Middle-End; God-of-beginning / life-process / God-of-end; Seed-plant-seed; Monad-Personality-Self. The individual is the creative bridge between collective phases.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar提供两个互补公式作为穿越迷宫的"阿里阿德涅之线"：
1. **物质观**："从集体到集体，通过个体"
2. **精神观**："从任何个体化层次到更高层次，通过创造性"

这些平行于：始-中-终；始之神/生命过程/终之神；种子-植物-种子；单子-人格-自性。个体是集体阶段之间的创造性桥梁。

**Narrative Snippets**:
- `[ns_aop_131]` `[trigger: ariadne_formula]` `[factor_trigger: astro_ariadne AND astro_dual_form AND astro_triple_princ]` `[role: 主干]` Ariadne formulas: substance (coll→indiv→coll) vs spirit (indiv→creative→higher). → L4943-4949
- `[ns_aop_132]` `[trigger: parallel_symbols]` `[factor_trigger: astro_parallel]` `[role: 总结]` Parallels: Begin-Middle-End; Seed-plant-seed; Monad-Personality-Self. → L4951-4965"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 5: From Collective to Collective Through the Individual"
    factor_refs: list = ['astro_coll_indiv_coll', 'astro_mon_pers_self']
    
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
        l1_anchor="ap_v1.0.0_entry_5__from_collective_to_co_001_L1",
    )
    version: str = "1.0.0"
