"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162759
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
    semantic_id="tb_v1.0.0_familiarity_of_regions_with_fi_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class FamiliarityOfRegionsWithFi(SemanticEntry):
    """
    **Source Text** (Lines 3633-3659):
> In addition to the rules which have been already given, respect...
    """
    
    original_text: str = """**Source Text** (Lines 3633-3659):
> In addition to the rules which have been already given, respecting the familiarity of the regions of the earth with the signs and planets, it must be observed, that all fixed stars which may be posited on any line, drawn from one zodiacal pole to the other, through such parts of the zodiac as may be connected with any particular country, are also in familiarity with that particular country. And, with regard to metropolitan cities, those points or degrees of the zodiac, over which the Sun and Moon were in transit, at the time when the construction of any such city was first undertaken and commenced, are to be considered as sympathizing with that city in an especial manner.

**English Paraphrase (Primary Language)**:
Ptolemy extends regional familiarity to include **fixed stars** and **city foundation charts**:

1. **Fixed Star Familiarity**: Stars on a line from zodiacal pole to pole, passing through a region's zodiacal degree, share familiarity with that region
2. **City Foundation**: The zodiacal degrees where Sun and Moon were at a city's founding are in sympathy with that city—especially the Ascendant
3. **Alternative**: If foundation date unknown, use the ruler's MC at birth

**Complete Chinese Interpretation (Secondary Language)**:
托勒密将地区亲和性扩展到包括**恒星**和**城市建城图**：

1. **恒星亲和性**：从黄道极到黄道极的线上，经过某地区黄道度数的恒星，与该地区共享亲和性
2. **城市建城**：城市建城时太阳和月亮所在的黄道度数与该城市有共鸣——尤其是上升点
3. **替代方案**：如果建城日期未知，使用统治者出生时的中天

**Core Points**:
- Fixed stars connect to regions through zodiacal pole lines
- City founding charts establish regional sympathy
- Ascendant degree most significant for cities
- Ruler's MC can substitute for unknown foundation

**Narrative Snippets**:
- `[ns_tetra_ii_010]` `[trigger: fixed_star_region]` `[factor_trigger: astro_fixed_star AND astro_region]` `[role: 主干]` Fixed stars on zodiacal pole lines share familiarity with connected regions. → Source Text II.4
- `[ns_tetra_ii_srl]` `[trigger: star_region_line]` `[factor_trigger: star_region_line]` `[role: 条件分支]` A line from zodiacal pole through a region's zodiacal degree connects fixed stars to that region's fate. → Source Text II.4
- `[ns_tetra_ii_rf]` `[trigger: region_fate]` `[factor_trigger: region_fate]` `[role: 效果]` Region's fate is determined by familiarity with zodiacal degrees, fixed stars, and eclipse positions. → Source Text II.4"""
    normalized_text_zh: str = """"""
    subject: str = "Familiarity of Regions with Fixed Stars (Chapter IV)"
    factor_refs: list = ['engine_id', 'star_region_line', 'astrology_classical', 'city_foundation', 'astrology_classical', 'source_ref', 'rel_ii_010', 'star_region_line', 'participating', 'evi_ii_010', 'star_region_line', 'rule_star_region', 'concept_star_region', 'star_region_line', 'homeland']
    
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
        l1_anchor="tb_v1.0.0_familiarity_of_regions_with_fi_001_L1",
    )
    version: str = "1.0.0"
