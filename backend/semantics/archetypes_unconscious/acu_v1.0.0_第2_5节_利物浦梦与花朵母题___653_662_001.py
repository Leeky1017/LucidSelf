"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559192
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
    semantic_id="acu_v1.0.0_第2_5节_利物浦梦与花朵母题___653_662_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第25节利物浦梦与花朵母题653662(SemanticEntry):
    """
    **原文** (¶653-662, 行10100-10217):

> [653] The vessel motif is an expression of the content, just as ...
    """
    
    original_text: str = """**原文** (¶653-662, 行10100-10217):

> [653] The vessel motif is an expression of the content, just as Shakti represents Shiva. As alchemy shows, the self is androgynous—consisting of masculine and feminine principles. Conrad of Würzburg speaks of Mary, the flower of the sea in which Christ lies hidden.
>
> [654-655] The rose in the centre is depicted as a ruby. The mandala was a spontaneous product from a dream: The dreamer found himself in Liverpool. It was night, raining, dark and disagreeable. In the middle of the city was a public garden with a lake. On a little island was a single tree, a red-flowering magnolia, which miraculously stood in everlasting sunshine. "I was beginning to understand why the man had settled here." When painted, the magnolia turned into a rose made of ruby-coloured glass, a four-rayed star. "The whole thing seemed like a window opening on to eternity."
>
> [660-662] In this painting we see at the cardinal points four creatures: a bird, a sheep, a snake, and a lion with a human face. The interior of the mandala is empty—or contains a "Nothing" expressed by a quaternity. The four animals remind us of the cherubim in Ezekiel's vision, the four symbols of the evangelists, and the four sons of Horus. Animals signify the instinctive forces of the unconscious brought into unity within the mandala. This integration of instincts is a prerequisite for individuation.

**英文释义**：
- 容器母题 = 内容表达；沙克提代表湿婆
- 自性是雌雄同体（男性+女性原则）
- 红宝石玫瑰在中心
- 利物浦梦：黑暗城市中心有公园，湖中岛上红花木兰在永恒阳光中
- 绘画时木兰变成红宝石色玻璃玫瑰 = 四射线星
- "整个东西像打开永恒的窗户"
- 四方位四生物：鸟、羊、蛇、狮（人面）
- 曼陀罗内部空/包含四元组表达的"无"
- 四动物 = 以西结异象的基路伯 = 福音书四象征 = 荷鲁斯四子
- 动物 = 本能力量在曼陀罗中统一
- 本能整合 = 个体化的先决条件

**中文诠释**：
- 容器母题表达内容（如沙克提代表湿婆）
- 炼金术：自性是雌雄同体
- 红宝石玫瑰在曼陀罗中心
- 利物浦梦：黑暗阴雨的城市
- 城中心公园湖中岛上：红花木兰在永恒阳光中
- 绘画转化：木兰 → 红宝石色玻璃玫瑰 → 四射线星
- "像打开永恒的窗户"
- 四方位四生物对应四元素/福音书四象征
- 曼陀罗内部的"无"以四元组表达
- 动物 = 无意识本能力量
- 本能整合 = 个体化先决条件

**Narrative Snippets**:
- `[ns_cw9i_X_654]` `[trigger: liverpool_dream]` `[factor_trigger: jung_dream AND jung_self]` `[role: 主干]` Liverpool dream: red-flowering magnolia in everlasting sunshine amidst dark city—became ruby rose, "window opening on to eternity." → ¶654-655
- `[ns_cw9i_X_660]` `[trigger: four_animals]` `[factor_trigger: jung_quaternity AND jung_instinct]` `[role: 主干依赖]` Four animals at cardinal points = instinctive forces brought into unity; integration of instincts is prerequisite for individuation. → ¶660"""
    normalized_text_zh: str = """"""
    subject: str = "第2.5节：利物浦梦与花朵母题 (¶653-662)"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_第2_5节_利物浦梦与花朵母题___653_662_001_L1",
    )
    version: str = "1.0.0"
