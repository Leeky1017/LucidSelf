"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.520025
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
    semantic_id="acu_v1.0.0_第四节_曼陀罗的发展与自性显现___569_590_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第四节曼陀罗的发展与自性显现569590(SemanticEntry):
    """
    **原文** (¶569-590, 行8902-9218):

> [569-570] Picture 6: The background is cloudy grey. The mandala is...
    """
    
    original_text: str = """**原文** (¶569-590, 行8902-9218):

> [569-570] Picture 6: The background is cloudy grey. The mandala is done in the vividest colours. A swastika appears, wheeling to the right. In this mandala an attempt is made to unite the opposites red and blue, outside and inside. The rightward movement aims at bringing about an ascent into the light of consciousness. The black snake has disappeared but imparts its darkness to the background. A dream associated: a tree growing in the middle of the room where she worked—maternal significance. The tree = philosophical tree = individuation process.
>
> [571-573] Justin's gnosis: Baruch = tree of life, Naas = tree of knowledge. The Heracles myth has all the features of an individuation process. The mandala is a God-image: the central point, circle, and quaternity are symbols for the deity. "God is an infinite circle whose centre is everywhere and circumference nowhere." Parmenides: "In the centre is the goddess who guides everything."
>
> [574-576] Picture 7: It has turned to night—the entire sheet is black. All light is concentrated in the sphere. The blackness has penetrated to the centre, compensated by golden light radiating out in a cross. The wings of Mercury keep the sphere afloat. The golden cross binds the four together—inner bond and consolidation as defence. The cortices (layers of skin) give protection against outside influences—same purpose as inner consolidation. These cortices probably correspond to the cabalistic klippoth.
>
> [580] The original four eddies have coalesced into wavy squares in the middle. Golden points at the outer rim emit rainbow colours—the cauda pavonis of alchemy. Böhme speaks of "love-desire or a Beauty of Colours; and here all Colours arise."

**英文释义**：
- 画作6：背景灰色；曼陀罗最鲜艳颜色；卐出现（向右旋转）
- 试图统一对立（红/蓝；内/外）；向右运动 = 意识提升
- 黑蛇消失但将黑暗传给背景
- 树的梦 = 母性意义 = 个体化过程
- 曼陀罗 = 神像：中心点、圆、四元性 = 神性象征
- "上帝是无限圆，中心在everywhere，周长在nowhere"
- 画作7：整张纸黑色；光集中在球体；黑暗穿透中心
- 金色十字从中心辐射 = 补偿；墨丘利翅膀使球漂浮
- 皮层（cortices）= 保护层 = 卡巴拉的klippoth
- 四个漩涡合并为中间的波浪方形
- 金点发出彩虹色 = cauda pavonis

**完整中文诠释**：
- 画作6：灰色背景，鲜艳色彩曼陀罗
- 卐符号出现（向右旋转 = 意识提升）
- 统一红/蓝、内/外对立
- 黑蛇消失但黑暗传给背景
- 树梦 = 母性 = 个体化过程
- 曼陀罗 = 神像（中心点+圆+四元性）
- 画作7：全黑纸张；光集中在球体
- 黑暗穿透中心 → 金色十字补偿
- 墨丘利翅膀保持漂浮
- 皮层 = 保护层 = klippoth
- 彩虹色 = cauda pavonis（孔雀尾）

**Narrative Snippets**:
- `[ns_cw9i_IX_570]` `[trigger: swastika_ascent]` `[factor_trigger: jung_mandala AND jung_consciousness]` `[role: 主干]` Swastika wheeling to the right = ascent into light of consciousness; philosophical tree = individuation process. → ¶569-570
- `[ns_cw9i_IX_572]` `[trigger: god_image]` `[factor_trigger: jung_mandala AND jung_god]` `[role: 主干依赖]` Mandala is a God-image: "God is an infinite circle whose centre is everywhere and circumference nowhere." → ¶571-573
- `[ns_cw9i_IX_576]` `[trigger: golden_cross]` `[factor_trigger: jung_quaternity AND jung_integration]` `[role: 条件分支]` Cortices (layers of skin) = cabalistic klippoth; golden cross binds the four together as inner consolidation. → ¶574-576
- `[ns_cw9i_IX_580]` `[trigger: cauda_pavonis]` `[factor_trigger: jung_alchemy AND jung_color]` `[role: 总结]` Four eddies coalesced into wavy squares; golden points emit rainbow colours = cauda pavonis. → ¶580"""
    normalized_text_zh: str = """"""
    subject: str = "第四节：曼陀罗的发展与自性显现 (¶569-590)"
    factor_refs: list = ['mandala_development', 'quaternity', 'golden_flower']
    
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
        l1_anchor="acu_v1.0.0_第四节_曼陀罗的发展与自性显现___569_590_001_L1",
    )
    version: str = "1.0.0"
