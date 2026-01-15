"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192595
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
    semantic_id="tb_v1.0.0_distribution_of_nativity_inqui_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class DistributionOfNativityInqui(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Distribution | Systematic allocation | Methodical approach |
| Life inquiry | Areas of life examination | Comprehensive analysis |
| Planetary significators | Planets ruling topics | Topical lords |

#### Source Text

"The distribution of inquiry into the several topics of a nativity should be made in regular order: and the topics themselves admit of a fourfold general division; viz. 1st, the inquiry into the qualities of the mind; 2nd, into the qualities of the body; 3rd, into pecuniary circumstances; 4th, into dignities and honours."

#### English Paraphrase (Primary Language)

Ptolemy establishes a **systematic methodology** for natal analysis through a fourfold division of life topics:

1. **Mind**: Mental qualities, intelligence, psychological nature
2. **Body**: Physical constitution, health, appearance
3. **Wealth**: Material circumstances, possessions, livelihood
4. **Honours**: Social standing, career, reputation

This framework ensures **comprehensive analysis** by examining all major life domains systematically. Each topic has its own planetary significators and house associations.

**Methodological principle**: Proceed in regular order through each topic, determining the relevant significators before interpretation.

#### Complete Chinese Interpretation (Secondary Language)

托勒密通过将生命主题四分来建立**系统方法论**：

1. **心智**：心理品质、智力、心理本质
2. **身体**：身体体质、健康、外貌
3. **财富**：物质状况、财产、生计
4. **荣誉**：社会地位、事业、声誉

这个框架通过系统地检查所有主要生命领域来确保**全面分析**。每个主题都有其行星指示星和宫位关联。

**方法论原则**：按顺序逐一处理每个主题，在诠释前确定相关指示星。

#### Core Points

- **Fourfold division**: Mind, Body, Wealth, Honours
- **Systematic order**: Proceed methodically through topics
- **Significator-based**: Each topic has ruling planets
- **Comprehensive coverage**: All major life domains

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's fourfold division differs from later medieval divisions that added more categories. This simpler framework influenced Arabic and Renaissance astrology's topical methods.
- **中文**: 托勒密的四分法不同于后来增加更多类别的中世纪划分。这个更简单的框架影响了阿拉伯和文艺复兴占星术的主题方法。

**Narrative Snippets**:
- `[ns_ptolemy_iii_005]` `[trigger: distribution]` `[factor_trigger: astro_distribution AND astro_fourfold]` `[role: 主干]` The distribution of inquiry follows a fourfold division: mind, body, wealth, and honours. → Source Text
- `[ns_ptolemy_iii_006]` `[trigger: methodology]` `[factor_trigger: astro_methodology AND astro_significator]` `[role: 主干依赖]` Each topic has its own planetary significators, proceeding in regular order for comprehensive analysis. → English Paraphrase
- `[ns_tetra_iii_fd]` `[trigger: fourfold_div]` `[factor_trigger: fourfold_div]` `[role: 主干]` Fourfold division of natal inquiry: (1) Mind, (2) Body, (3) Wealth, (4) Honours—systematically covering all major life domains. → Ptolemy III
- `[ns_tetra_iii_si]` `[trigger: systematic_inquiry]` `[factor_trigger: systematic_inquiry]` `[role: 条件分支]` Systematic inquiry proceeds in regular order through each topic, determining significators before interpretation. → Ptolemy III
- `[ns_tetra_iii_ts]` `[trigger: topic_sig]` `[factor_trigger: topic_sig]` `[role: 条件分支]` Topic significators assign specific planets as rulers for each life domain—identified before interpretation begins. → Ptolemy III"""
    normalized_text_zh: str = """"""
    subject: str = "Distribution of Nativity Inquiry (Chapter IV)"
    factor_refs: list = ['distribution', 'new_candidate', 'significator']
    
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
        l1_anchor="tb_v1.0.0_distribution_of_nativity_inqui_001_L1",
    )
    version: str = "1.0.0"
