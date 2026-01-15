"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.152302
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
    semantic_id="ca_v1.0.0_marriage__7th_house_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class Marriage7thHouse(SemanticEntry):
    """
    #### Source Text
(Lilly Book III, pp. 586-602): "Of men's Marriages. Whether the Native shall marry:...
    """
    
    original_text: str = """#### Source Text
(Lilly Book III, pp. 586-602): "Of men's Marriages. Whether the Native shall marry: if Venus and Moon be well-placed, he shall marry. Lord of 7th in good dignity = happy marriage. Mars afflicting Venus = strife."

#### English Paraphrase (Primary Language)

**Marriage indicators** (for men):
- **Venus** = wife's nature and relationship quality
- **Moon** = emotional compatibility
- **Lord of 7th** = spouse's character
- **Planets in 7th** = marriage circumstances

**Will he marry?**
- Venus/Moon well-aspected = yes
- Lord of 7th angular and dignified = yes
- Malefics afflicting 7th = delays or denial

**Number of marriages**:
- Multiple signs applying to 7th cusp = multiple marriages
- Lord of 7th in double sign (Gemini, Sagittarius, Pisces) = more than one

**Marriage timing**: Directions of Venus or Lord of 7th to benefic aspects.

#### Complete Chinese Interpretation (Secondary Language)

**婚姻指标**（男性）：金星=妻子性质和关系质量；月亮=情感兼容性；第7宫主=配偶性格；第7宫内行星=婚姻情况。**是否会结婚**：金星/月亮相位良好=会；第7宫主在角宫且尊贵=会；凶星克第7宫=延迟或无婚。**婚姻次数**：多个星座趋近第7宫尖=多次婚姻；第7宫主在双体星座（双子、射手、双鱼）=不止一次。**婚姻时间**：金星或第7宫主推运至吉星相位。

**Narrative Snippets**:
- `[ns_lilly_marriage_001]` `[trigger: marriage]` `[factor_trigger: astro_marriage_likelihood]` `[role: 主干]` Venus and Moon well-placed = native shall marry; afflicted = difficulties. → CA III #Marriage
- `[ns_lilly_marriage_002]` `[trigger: spouse_quality]` `[factor_trigger: astro_spouse_quality]` `[role: 主干依赖]` Lord of 7th dignified = happy marriage; debilitated = spouse of poor quality or strife. → CA III #Marriage
- `[ns_lilly_marriage_003]` `[trigger: venus_dignity]` `[factor_trigger: astro_venus_dignity]` `[role: 主干依赖]` Venus dignity indicates wife's nature and relationship quality for men. → English Paraphrase
- `[ns_lilly_marriage_004]` `[trigger: moon_aspect]` `[factor_trigger: astro_moon_aspect]` `[role: 条件分支]` Moon aspects show emotional compatibility in marriage. → English Paraphrase
- `[ns_lilly_marriage_005]` `[trigger: lord_7th]` `[factor_trigger: astro_lord_7th_dignity]` `[role: 主干依赖]` Lord of 7th dignity determines spouse character and marriage quality. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Marriage (7th House)"
    factor_refs: list = ['lord_7th', 'marriage_significator']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_marriage__7th_house_001_L1",
    )
    version: str = "1.0.0"
