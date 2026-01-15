"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.152329
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
    semantic_id="ca_v1.0.0_primary_directions_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class PrimaryDirections(SemanticEntry):
    """
    #### Source Text
(Lilly Book III, pp. 652-700): "The Effects of Directions. Directions show when goo...
    """
    
    original_text: str = """#### Source Text
(Lilly Book III, pp. 652-700): "The Effects of Directions. Directions show when good or evil shall happen. The Ascendant directed to Saturn = melancholy, illness, restrictions. To Jupiter = honor, wealth, success. One degree of direction equals approximately one year of life."

#### English Paraphrase (Primary Language)

**Primary Directions** = the fundamental predictive technique in traditional natal astrology:

**Principle**: Significators (ASC, MC, Sun, Moon) are "directed" (moved forward in the chart) to meet promittors (planets, aspects, fixed stars). When they meet, events occur.

**Timing**: 1° of arc ≈ 1 year of life (Ptolemy's key)

**Significators directed**:
- **ASC** → body, health, personal life
- **MC** → career, honor, public standing
- **Sun** → vitality, father, authority
- **Moon** → emotions, mother, changes

**Effects of ASC to Planets**:
| Promittor | Effect |
|-----------|--------|
| Saturn | Illness, melancholy, delays, losses |
| Jupiter | Honor, wealth, success, expansion |
| Mars | Accidents, conflicts, fevers, courage |
| Sun | Recognition, vitality, father-related events |
| Venus | Love, pleasure, marriage, artistic success |
| Mercury | Intellectual gains, travel, communication |
| Moon | Changes, public matters, mother-related events |

#### Complete Chinese Interpretation (Secondary Language)

**主限**=传统本命占星的基本预测技术。**原理**：象征星（上升、天顶、太阳、月亮）被"推运"（在星盘中向前移动）以遇到应许星（行星、相位、恒星）。当它们相遇时，事件发生。**时间**：1°弧度≈1年生命（托勒密的关键）。**被推运的象征星**：上升→身体/健康/个人生活；天顶→事业/荣誉/公众地位；太阳→生命力/父亲/权威；月亮→情感/母亲/变化。**上升推运至行星的效果**：土星=疾病/忧郁/延迟/损失；木星=荣誉/财富/成功/扩张；火星=事故/冲突/发烧/勇气；太阳=认可/活力/父亲相关事件；金星=爱情/愉悦/婚姻/艺术成功；水星=智识收获/旅行/沟通；月亮=变化/公众事务/母亲相关事件。

**Narrative Snippets**:
- `[ns_lilly_direct_001]` `[trigger: direction]` `[factor_trigger: astro_asc_direction_to]` `[role: 主干]` ASC directed to Jupiter = honor, wealth, success; to Saturn = illness, melancholy, restrictions. → CA III #Directions
- `[ns_lilly_direct_002]` `[trigger: timing]` `[factor_trigger: astro_direction_degree_year]` `[role: 主干依赖]` One degree of direction equals approximately one year of life—Ptolemy's key. → CA III #Directions"""
    normalized_text_zh: str = """"""
    subject: str = "Primary Directions"
    factor_refs: list = ['primary_direction', 'significator', 'promittor']
    
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
        l1_anchor="ca_v1.0.0_primary_directions_001_L1",
    )
    version: str = "1.0.0"
