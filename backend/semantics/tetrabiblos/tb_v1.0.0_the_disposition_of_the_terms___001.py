"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182698
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
    semantic_id="tb_v1.0.0_the_disposition_of_the_terms___001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheDispositionOfTheTerms(SemanticEntry):
    """
    **Source Text** (Lines 2556-2712):
> There are two methods of disposing the terms of the planets: on...
    """
    
    original_text: str = """**Source Text** (Lines 2556-2712):
> There are two methods of disposing the terms of the planets: one is Ægyptian, and the other Chaldaic, or according to the order of the Decans... The Ægyptian method observes neither regular succession, nor any discernible ratio; and is as follows [tables follow]... Jupiter 79°, Mars 66°, Venus 82°, Mercury 76°, Saturn 57°. These are the Ægyptian terms.

**English Paraphrase (Primary Language)**:
**Egyptian Terms** represent the traditional system for dividing each sign into five unequal planetary segments:

**Structure**: Each 30° sign is divided into 5 portions, each ruled by one of the five non-luminary planets (Sun/Moon excluded).

**Egyptian allocation totals**:
- Jupiter: 79° (most benefic = largest share)
- Venus: 82° (second benefic)
- Mercury: 76° (neutral)
- Mars: 66° (lesser malefic)
- Saturn: 57° (greater malefic = smallest share)

**Ptolemy's critique**: The Egyptian system lacks consistent rationale—no clear mathematical or astronomical basis for the irregular distributions.

**Complete Chinese Interpretation (Secondary Language)**:
**埃及界**代表将每个星座分成五个不等行星部分的传统系统：

**结构**：每个30°星座被分成5份，每份由五颗非发光体行星之一主宰（太阳/月亮除外）。

**埃及分配总数**：
- 木星：79°（最大吉星 = 最大份额）
- 金星：82°（第二吉星）
- 水星：76°（中性）
- 火星：66°（小凶星）
- 土星：57°（大凶星 = 最小份额）

**托勒密的批评**：埃及系统缺乏一致的理据——不规则分布没有明确的数学或天文基础。

**Core Points**:
- Terms = minor essential dignity
- Each sign divided into 5 unequal segments
- Only 5 planets participate (luminaries excluded)
- Egyptian system: Traditional but irregular
- Benefics receive more degrees than malefics
- Total = 360° across entire zodiac

**Narrative Snippets**:
- `[ns_tetra_i054]` `[trigger: egyptian_terms]` `[factor_trigger: terms_ptolemaic]` `[role: 主干]` Egyptian terms divide each sign into five segments with irregular planetary allocations totaling 360°. → Source Text I.23"""
    normalized_text_zh: str = """"""
    subject: str = "The Disposition of the Terms - Egyptian System (Chapter XXIII)"
    factor_refs: list = ['engine_id', 'terms_egyptian', 'astrology_classical', 'source_ref', 'rel_i_021a', 'terms_egyptian', 'supporting', 'evi_i_017a', 'terms_egyptian', 'rule_egyptian_terms', 'concept_egyptian_terms', 'terms_egyptian', 'tradition']
    
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
        l1_anchor="tb_v1.0.0_the_disposition_of_the_terms___001_L1",
    )
    version: str = "1.0.0"
