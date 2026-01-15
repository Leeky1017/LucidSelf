"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.152267
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
    semantic_id="ca_v1.0.0_determining_life_span_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class DeterminingLifeSpan(SemanticEntry):
    """
    #### Source Text
(Lilly Book III, pp. 525-530): "Of Hylech or Aphaeta, and the Intersicient Planet. ...
    """
    
    original_text: str = """#### Source Text
(Lilly Book III, pp. 525-530): "Of Hylech or Aphaeta, and the Intersicient Planet. The Hylech is the giver of life; the Anareta is the destroyer of life. In day nativities, the Sun may be Hylech if well-placed; in night nativities, the Moon. The Anareta is usually Mars or Saturn directing to Hylech."

#### English Paraphrase (Primary Language)

**Hyleg (Apheta)** = the "Giver of Life," the vital point in the natal chart:

**Hyleg Candidates** (in order of preference):
1. **Day birth**: Sun (if in houses 1, 7, 9, 10, 11)
2. **Night birth**: Moon (if in houses 1, 7, 9, 10, 11)
3. **ASC degree** (if neither luminary qualifies)
4. **Part of Fortune** (alternative)
5. **Prenatal Syzygy** (New/Full Moon before birth)

**Anareta (Interfector)** = the "Destroyer of Life," threatening the Hyleg:
- Usually **Mars** or **Saturn** (malefics)
- Direction of Hyleg to Anareta = life-threatening period
- Benefic aspects to Hyleg extend life; malefic aspects shorten it

**Calculation**: Use primary directions to determine when Hyleg reaches dangerous aspects.

#### Complete Chinese Interpretation (Secondary Language)

**命主星（Hyleg/Apheta）**="生命赋予者"，本命盘中的生命点。**命主星候选**（按优先顺序）：1. 日生：太阳（若在1、7、9、10、11宫）；2. 夜生：月亮（若在1、7、9、10、11宫）；3. 上升度数（若两发光体都不合格）；4. 福点（替代）；5. 产前朔望（出生前新月/满月）。**杀主星（Anareta）**="生命毁灭者"，威胁命主星：通常是火星或土星（凶星）；命主星推运至杀主星=生命威胁期；吉星相位延长寿命，凶星相位缩短寿命。

**Narrative Snippets**:
- `[ns_lilly_hyleg_001]` `[trigger: hyleg]` `[factor_trigger: astro_life_vitality]` `[role: 主干]` Hyleg is the giver of life—Sun by day, Moon by night, if well-placed. → CA III #Hyleg
- `[ns_lilly_hyleg_002]` `[trigger: anareta]` `[factor_trigger: astro_life_threat]` `[role: 条件分支]` Anareta (Mars or Saturn) directing to Hyleg indicates life-threatening periods. → CA III #Hyleg
- `[ns_lilly_hyleg_003]` `[trigger: timing]` `[factor_trigger: astro_timing]` `[role: 总结]` Primary directions measure life span—1 degree = 1 year for timing events. → English Paraphrase
- `[ns_lilly_hyleg_004]` `[trigger: hyleg_position]` `[factor_trigger: astro_hyleg_position]` `[role: 主干依赖]` Hyleg candidates: Sun (day), Moon (night), ASC, Part of Fortune, prenatal syzygy. → English Paraphrase
- `[ns_lilly_hyleg_005]` `[trigger: anareta_aspect]` `[factor_trigger: astro_anareta_aspect]` `[role: 条件分支]` Anareta (Mars/Saturn) direction to Hyleg marks life-threatening period. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Determining Life Span"
    factor_refs: list = ['hyleg', 'anareta', 'primary_direction']
    
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
        l1_anchor="ca_v1.0.0_determining_life_span_001_L1",
    )
    version: str = "1.0.0"
