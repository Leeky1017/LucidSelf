"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333635
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
    semantic_id="ah_v1.0.0_four_angles__cardinal_cross_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class FourAnglesCardinalCross(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Cardinal Cross | Four an...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Cardinal Cross | Four angles | Maximum power |
| Horizon Axis | Asc-Desc | Self-Other |
| Meridian Axis | MC-IC | Public-Private |
| Cross of Matter | Spirit grounded | Embodiment |

#### Source Text

"The Ascendant and Descendant form the horizon axis, while the Midheaven and Imum Coeli form the meridian axis. Together these four angles create the 'cross of matter,' the cardinal points that are the most powerful positions in any natal chart. They represent the four fundamental orientations of embodied existence: birth/self (Asc), culmination/achievement (MC), relationship/other (Desc), and roots/foundation (IC)."

#### English Paraphrase (Primary Language)

The astrological chart's four angles constitute its structural foundation, forming two intersecting axes. The horizontal axis connects the Ascendant (eastern horizon, dawn point) with the Descendant (western horizon, dusk point), representing the encounter between self and other. The vertical axis connects the Midheaven (culmination point, noon) with the Imum Coeli (nadir point, midnight), representing the polarity between public achievement and private foundation. These four cardinal points—termed the "cross of matter" because they ground spirit in physical embodiment—hold maximum power in chart interpretation, as they define the individual's primary orientations toward life.

#### Complete Chinese Interpretation (Secondary Language)

四角(上升/下降/天顶/天底)构成**物质十字**(Cardinal Cross)，是命盘最强力的基本方位点。**上升**(ASC，东方地平线)=自我出生点，意识进入物质；**下降**(DESC，西方地平线)=他者相遇点，自我镜像于关系；**天顶**(MC，子午线最高点)=社会巅峰点，公众成就；**天底**(IC，子午线最低点)=根源深处点，私密基础。四角形成两条轴线：**地平轴**(ASC-DESC)代表自我-他者极性；**子午轴**(MC-IC)代表公-私极性。角宫行星获得最大力量因处于这些关键交叉点。四角是个人生命最活跃表达点。

#### Core Points

- **Horizon axis**: Asc-Desc (self-other polarity)
- **Meridian axis**: MC-IC (achievement-foundation polarity)
- **Cross of matter**: Four angles ground spirit in embodiment
- **Maximum power**: Most influential chart positions
- **Fourfold orientation**: Birth/achievement/relationship/roots"""
    normalized_text_zh: str = """"""
    subject: str = "Four Angles (Cardinal Cross)"
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_four_angles__cardinal_cross_001_L1",
    )
    version: str = "1.0.0"
