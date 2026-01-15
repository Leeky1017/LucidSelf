"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.519970
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
    semantic_id="acu_v1.0.0_第二_5节_闪电_波墨与四元性___531_537_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第二5节闪电波墨与四元性531537(SemanticEntry):
    """
    **原文** (¶531-537, 行8248-8396):

> [531-532] Again there are boulders, the round and pointed forms; b...
    """
    
    original_text: str = """**原文** (¶531-537, 行8248-8396):

> [531-532] Again there are boulders, the round and pointed forms; but the round ones are no longer eggs, they are complete circles, and the pointed ones are tipped with golden light. One of the round forms has been blasted out by a golden flash of lightning. The magician is no longer there—the picture shows an impersonal natural process. The eggs turned into abstract spheres or circles; the magician's touch became a flash of lightning. She had rediscovered the historical synonym of the philosophical egg: the rotundum, the round original form of the Anthropos.
>
> [533-534] The liberating flash of lightning is a symbol also used by Paracelsus and the alchemists. Lightning signifies a sudden, unexpected, overpowering change of psychic condition. Böhme says: "In this Spirit of the Fire-flash consists the Great Almighty Life." The flash is the "Birth of the Light." It has transformative power: "If I could in my Flesh comprehend the Flash, I could transfigure my Body therewith."
>
> [535-536] Böhme associates lightning with the quaternity. When caught in the four "Qualities" or "Spirits," the Flash subsists in the Centre as a Heart. When it reaches the dark substance, it makes a Cross with the Comprehension of all Properties. The cross in the mandala pertains to the Kingdom of Glory; Nature remains in darkness.
>
> [537] The sign ⊕ is for cinnabar (HgS), the most important quicksilver ore. Cinnabar stood for the rubedo stage of the transforming substance. It was also supposed to be identical with the uroboros dragon. On account of its redness it was often identified with the philosophical sulphur.

**英文释义**：
- 圆形不再是蛋，是完整的圆；金色闪电炸开圆形
- 魔法师消失 → 非人格自然过程
- 蛋 → 抽象球/圆；魔法师触碰 → 闪电
- 重新发现哲学蛋的同义词：rotundum = Anthropos的圆形原始形式
- 闪电 = 帕拉塞尔苏斯和炼金术士的象征
- 闪电 = 突然、意外、压倒性的心理状态改变
- 波墨：火闪电之灵 = 伟大全能生命；闪电 = 光的诞生
- 闪电与四元性关联；被四品质/四灵捕获时，闪电作为心存于中心
- 闪电达到黑暗物质时形成十字 = 所有属性的理解
- 朱砂(HgS) = 最重要的水银矿；代表rubedo阶段
- 朱砂 = 衔尾蛇龙 = 哲学硫磺

**中文诠释**：
- 圆形变为完整的圆（不再是蛋）
- 金色闪电炸开圆形
- 魔法师消失 = 非人格自然过程
- 重新发现rotundum = Anthropos原始形式
- 闪电 = 突然心理状态改变
- 波墨：火闪电之灵 = 全能生命
- 闪电 = 光的诞生；有转化力量
- 闪电与四元性：被四灵捕获时作为心存于中心
- 达到黑暗时形成十字
- 朱砂 = 水银矿 = rubedo阶段 = 衔尾蛇龙

**Narrative Snippets**:
- `[ns_cw9i_IX_532]` `[trigger: rotundum_anthropos]` `[factor_trigger: jung_self AND jung_transformation]` `[role: 主干]` Eggs transformed into abstract spheres; magician's touch became lightning—rediscovering the rotundum, original form of Anthropos. → ¶531-532
- `[ns_cw9i_IX_534]` `[trigger: fire_flash]` `[factor_trigger: jung_light AND jung_transformation]` `[role: 主干依赖]` Böhme: "In this Spirit of the Fire-flash consists the Great Almighty Life." Flash = Birth of Light with transformative power. → ¶534
- `[ns_cw9i_IX_535]` `[trigger: cross_quaternity]` `[factor_trigger: jung_quaternity AND jung_symbol]` `[role: 条件分支]` Lightning caught in the four Qualities makes a Cross—pertaining to the Kingdom of Glory while Nature remains in darkness. → ¶535-536"""
    normalized_text_zh: str = """"""
    subject: str = "第二.5节：闪电、波墨与四元性 (¶531-537)"
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
        l1_anchor="acu_v1.0.0_第二_5节_闪电_波墨与四元性___531_537_001_L1",
    )
    version: str = "1.0.0"
