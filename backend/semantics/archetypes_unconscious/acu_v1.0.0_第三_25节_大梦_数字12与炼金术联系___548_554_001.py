"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.520004
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
    semantic_id="acu_v1.0.0_第三_25节_大梦_数字12与炼金术联系___548_554_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第三25节大梦数字12与炼金术联系548554(SemanticEntry):
    """
    **原文** (¶548-554, 行8549-8649):

> [548] Miss X was born immediately after midnight. Her father used ...
    """
    
    original_text: str = """**原文** (¶548-554, 行8549-8649):

> [548] Miss X was born immediately after midnight. Her father used to tease her by saying she was born "at the twelfth hour." The number 12 meant the culminating point of her life, which she had only now reached. It is indeed an hour of birth—not of the dreamer but of the self.
>
> [549-550] Two "big" dreams have amalgamated in the picture. The sphere has floated up to heaven. The increase of light indicates conscious realization. The term "true personality" coincides with the Chinese chen-yen ("true man") and the homo quadratus of alchemy. For the alchemists the opus was an analogy of God's work of creation. The birth of the self appears as a microcosm—the "total" man is as big as the world, like an Anthropos.
>
> [551-552] The nodes in the picture signify numbers—two stages: first up to 3, then up to 12. Twelve is four times three: the axiom of Maria, the dilemma of three and four. This tetrameria (four stages of three parts each) is analogous to the twelve transformations of the zodiac. The present aeon of Pisces is drawing to its end—the twelfth house of the zodiac.
>
> [553-554] Mercurius forms a world-encircling band, usually represented by a snake. Mercurius is duplex—himself an antithesis. As Hermes Trismegistus he is the patriarch of alchemy. The primordial image underlying the sphere girdled with quicksilver is the world egg encoiled by a snake. The self, or its symbol, is entwined by the mercurial serpent.

**英文释义**：
- X小姐生于午夜后 → "第十二时辰" → 生命的高潮
- 这是自性的诞生，非做梦者的诞生
- "真人格" = 中国的"真人"(chen-yen) = 炼金术的homo quadratus
- 炼金术opus = 上帝创世的类比
- 自性诞生 = 微观宇宙；"完整的人"如Anthropos般大如世界
- 数字阶段：3 → 12（四乘三）= Maria公理
- 四分体（四阶段各三部分）= 黄道十二变换
- 双鱼座时代即将结束 = 第十二宫
- 墨丘利形成环绕世界的带 = 蛇
- 墨丘利是二重的，自身是对立
- 原始意象：被蛇缠绕的世界蛋

**中文诠释**：
- X小姐生于午夜后 → 父亲戏称"第十二时辰出生"
- 12 = 生命高潮 = 自性的诞生时刻
- "真人格" = 中国"真人" = 炼金术homo quadratus
- opus = 上帝创世的类比；自性诞生 = 微观宇宙
- 数字阶段：3→12（4×3）= Maria公理（三与四的困境）
- 四分体对应黄道十二变换
- 双鱼座时代（第十二宫）即将结束
- 墨丘利 = 环绕世界的蛇；Hermes Trismegistus = 炼金术始祖
- 原始意象：被墨丘利蛇缠绕的世界蛋

**Narrative Snippets**:
- `[ns_cw9i_IX_548]` `[trigger: number_twelve]` `[factor_trigger: jung_number AND jung_self]` `[role: 主干]` Number 12 = culminating point of life; this is the birth of the self, not of the dreamer. → ¶548
- `[ns_cw9i_IX_550]` `[trigger: true_personality]` `[factor_trigger: jung_self AND jung_anthropos]` `[role: 主干依赖]` "True personality" = Chinese chen-yen = alchemical homo quadratus; the "total" man is as big as the world like an Anthropos. → ¶549-550
- `[ns_cw9i_IX_554]` `[trigger: world_egg]` `[factor_trigger: jung_symbol AND jung_self]` `[role: 条件分支]` Primordial image: the world egg encoiled by a snake—the self entwined by the mercurial serpent. → ¶554"""
    normalized_text_zh: str = """"""
    subject: str = "第三.25节：大梦、数字12与炼金术联系 (¶548-554)"
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
        l1_anchor="acu_v1.0.0_第三_25节_大梦_数字12与炼金术联系___548_554_001_L1",
    )
    version: str = "1.0.0"
