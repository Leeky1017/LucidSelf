"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192732
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
    semantic_id="tb_v1.0.0_the_duration_of_life___introdu_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheDurationOfLifeIntrodu(SemanticEntry):
    """
    **Source Text** (Lines 5536-5560):
> Of all events whatsoever, which take place after birth, the mos...
    """
    
    original_text: str = """**Source Text** (Lines 5536-5560):
> Of all events whatsoever, which take place after birth, the most essential is the continuance of life: and as it is, of course, useless to consider, in cases wherein the life of a child does not extend to the period of one year, what other events contingent on its birth might otherwise have subsequently happened, the inquiry into the duration of life consequently takes precedence of all other questions.

**English Paraphrase (Primary Language)**:
**Duration of life** is the most essential inquiry in natal astrology—all other predictions presuppose survival. Ptolemy introduces the **prorogation system**:

**Core principle**: The duration of life is regulated by:
1. **Prorogatory places** (where life-giver may be found)
2. **Rulers of prorogatory places** (planets governing those positions)
3. **Anæretic places/stars** (life-ending degrees)

This chapter establishes that longevity inquiry takes precedence over all other natal questions.

**Complete Chinese Interpretation (Secondary Language)**:
**寿命长度**是本命占星术中最本质的问询——所有其他预测都以生存为前提。托勒密引入**主限系统**：

**核心原则**：寿命长度由以下因素调节：
1. **主限宫位**（生命主可能所在）
2. **主限宫位的主星**（管辖这些位置的行星）
3. **截寿位置/星体**（终结生命的度数）

本章确立寿命问询优先于所有其他本命问题。

**Core Points**:
- Duration of life = most essential natal inquiry
- Takes precedence over all other predictions
- Three regulatory factors: prorogatory places, rulers, anæretic

**Narrative Snippets**:
- `[ns_tetra_iii022]` `[trigger: duration_intro]` `[factor_trigger: astro_lifespan]` `[role: 主干]` Duration of life is the most essential natal inquiry, taking precedence over all other predictions. → Source Text III.11
- `[ns_ptolemy_iii_037]` `[trigger: prorogation_system]` `[factor_trigger: astro_prorogation AND astro_lifespan]` `[role: 条件分支]` Life duration is regulated by prorogatory places (where life-giver found), their rulers, and anæretic places (life-ending degrees). → System
- `[ns_tetra_iii_li]` `[trigger: lifespan_inquiry]` `[factor_trigger: lifespan_inquiry]` `[role: 主干]` Lifespan inquiry is the most essential natal question—survival must be established before other matters can be predicted. → Source Text III.11
- `[ns_tetra_iii_oi]` `[trigger: other_inquiries]` `[factor_trigger: other_inquiries]` `[role: 条件分支]` Other inquiries (fortune, marriage, children, profession) depend on lifespan—they presuppose the native will survive to experience them. → Source Text III.11"""
    normalized_text_zh: str = """"""
    subject: str = "The Duration of Life - Introduction (Chapter XI)"
    factor_refs: list = ['engine_id', 'lifespan_inquiry', 'astrology_classical', 'source_ref', 'rel_iii_022', 'lifespan_inquiry', 'foundational', 'evi_iii_022', 'lifespan_inquiry', 'rule_lifespan_priority', 'concept_lifespan', 'lifespan_inquiry', 'mortality_awareness']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_the_duration_of_life___introdu_001_L1",
    )
    version: str = "1.0.0"
