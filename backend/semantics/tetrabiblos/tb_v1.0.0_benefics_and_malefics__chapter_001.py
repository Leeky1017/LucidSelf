"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182475
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
    semantic_id="tb_v1.0.0_benefics_and_malefics__chapter_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class BeneficsAndMaleficsChapter(SemanticEntry):
    """
    **Source Text** (Lines 1646-1658):
> Of the four temperaments or qualities above mentioned, two are ...
    """
    
    original_text: str = """**Source Text** (Lines 1646-1658):
> Of the four temperaments or qualities above mentioned, two are nutritive and prolific, viz. heat and moisture; by these all matter coalesces and is nourished: the other two are noxious and destructive, viz. dryness and cold; by these all matter is decayed and dissipated. Therefore, two of the planets, on account of their temperate quality, and because heat and moisture are predominant in them, are considered by the ancients as benefic, or causers of good: these are Jupiter and Venus. And the Moon also is so considered for the same reasons. But Saturn and Mars are esteemed of a contrary nature, and malefic, or causers of evil: the first from his excess of cold, the other from his excess of dryness.

**Key Term Analysis**:
- **Benefic**: ἀγαθοποιός - doer of good, life-promoting planet
- **Malefic**: κακοποιός - doer of evil, life-harming planet
- **Nutritive**: τρόφιμος - nourishing, growth-promoting
- **Prolific**: γόνιμος - fertile, life-generating

**English Paraphrase (Primary Language)**:
Ptolemy derives the **benefic/malefic distinction** directly from planetary qualities. The logic is biological: **heat and moisture** are life-promoting (they allow matter to coalesce and grow); **cold and dryness** are life-harming (they cause decay and dissipation).

**Benefics** (Jupiter, Venus, Moon): Their temperate, warm-moist qualities promote growth and fertility.
**Malefics** (Saturn, Mars): Saturn's excessive cold and Mars's excessive dryness are destructive to life.

This is not moralistic good/evil but **physiological benefit/harm**. A benefic planet supports biological flourishing; a malefic disrupts it. The distinction has profound implications for chart interpretation: benefic planets in strong positions enhance life; malefic planets in affliction indicate obstacles and dangers.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密直接从行星属性推导出**吉/凶行星**的区分。逻辑是生物学的：**热和湿**促进生命（它们使物质凝聚和生长）；**冷和干**损害生命（它们导致衰败和消散）。

**吉星**（木星、金星、月亮）：它们温和、温暖湿润的属性促进生长和生育。
**凶星**（土星、火星）：土星的过度寒冷和火星的过度干燥对生命具有破坏性。

这不是道德上的善/恶，而是**生理上的有益/有害**。吉星支持生物繁荣；凶星干扰它。这一区分对命盘解读有深远影响：吉星在强位增强生命；凶星受克表示障碍和危险。

**Core Points**:
- Heat and moisture are nutritive and prolific—promote life
- Cold and dryness are noxious and destructive—harm life
- Benefics (Jupiter, Venus, Moon): Warm-moist, life-promoting
- Malefics (Saturn, Mars): Cold/dry or hot/dry, life-harming
- Distinction is physiological, not moralistic
- Sun and Mercury classified separately (luminaries/neutral)

**Narrative Snippets**:
- `[ns_tetra_i024]` `[trigger: benefic_malefic_basis]` `[factor_trigger: planet_benefic AND life_promotion]` `[role: 主干]` Heat and moisture are nutritive; cold and dryness are destructive—this determines benefic vs malefic. → Source Text I.5
- `[ns_tetra_i025]` `[trigger: benefic_planets]` `[factor_trigger: planet_malefic AND life_harm]` `[role: 主干依赖]` Jupiter and Venus are benefic because heat and moisture predominate in their temperate quality. → Source Text I.5
- `[ns_tetra_i026]` `[trigger: malefic_planets]` `[factor_trigger: harmony_discord AND equal_power]` `[role: 主干依赖]` Saturn and Mars are malefic: Saturn from excess of cold, Mars from excess of dryness. → Source Text I.5

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The Moon is included with benefics here, though later traditions sometimes treat her as neutral. The Sun is not explicitly classified in this chapter, consistent with his unique status as primary luminary.
- **中文**: 月亮在此被归入吉星，尽管后来的传统有时将她视为中性。太阳在本章中没有明确分类，与他作为主要发光体的独特地位一致。"""
    normalized_text_zh: str = """"""
    subject: str = "Benefics and Malefics (Chapter V)"
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_benefics_and_malefics__chapter_001_L1",
    )
    version: str = "1.0.0"
