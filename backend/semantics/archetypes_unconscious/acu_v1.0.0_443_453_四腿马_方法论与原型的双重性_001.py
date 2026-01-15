"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498308
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
    semantic_id="acu_v1.0.0_443_453_四腿马_方法论与原型的双重性_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 443453四腿马方法论与原型的双重性(SemanticEntry):
    """
    **原文** (§443-453, 行6900-7065):

> [443-446] The four-legged horse has, as owner and rider, the hunte...
    """
    
    original_text: str = """**原文** (§443-453, 行6900-7065):

> [443-446] The four-legged horse has, as owner and rider, the hunter: a male figure. The quaternity, as we have shown, corresponds to a more conscious state. The hunter has a claim to the anima because he has raised a triad to a quaternity. But his claim is not legitimate because he has acquired his horse by transgression. The hero legitimately owns the horse because he obtained it with the witch's permission.
>
> [447-450] The two horses together form a complete union of opposites: the lower, feminine triad and the upper, masculine quaternity. The fairy-story presents a totality symbol: the union of conscious (quaternity) and unconscious (triad). This psychological interpretation has been confirmed by various mythological parallels: the triskele (three-legged) and tetraktys (four-legged).
>
> [451-453] The archetype of spirit has a double aspect, both helpful and harmful. The ambivalence is reflected in the figure of the old man in fairy-tales who gives good advice but may also be dangerous. This duality corresponds to the psychological reality: spirit can either help or possess man. The decisive factor is consciousness.

**英文释义**：
- 四腿马的主人/骑手 = 猎人（男性形象）
- 四元组 = 更有意识的状态
- 猎人对阿尼玛有要求权（将三升为四），但非法（通过违规获得马）
- 英雄合法拥有马（得到女巫许可）
- 两匹马一起 = 完整的对立统一：下部女性三元组 + 上部男性四元组
- 童话呈现整体性象征：意识（四）+ 无意识（三）的统一
- 神话学平行：三足形（三腿）和四元组（四腿）
- 精神原型的双重性：既有帮助也有伤害
- 老人形象体现这种歧义性：给好建议但也可能危险
- 决定性因素 = 意识

**中文诠释**：
- 四腿马 = 猎人的坐骑（男性）
- 四元组对应更高意识状态
- 猎人通过将三升为四而对阿尼玛有要求权
- 但猎人的要求不合法——他通过违规获得马
- 英雄合法拥有——得到女巫（无意识）的许可
- 两匹马合成完整的对立统一：
  - 三腿马 = 下部/女性/无意识三元组
  - 四腿马 = 上部/男性/意识四元组
- 童话呈现心理整体性象征
- 精神原型的双重面向：帮助 + 伤害
- 老人形象体现这种歧义——既给好建议又可能危险
- 决定因素 = 人的意识

**Narrative Snippets**:
- `[ns_cw9i_VI_443]` `[trigger: four_legged]` `[factor_trigger: jung_quaternity AND jung_conscious]` `[role: 主干]` Four-legged horse = hunter's mount; quaternity = more conscious state; hero's claim is legitimate through witch's permission. → §443-446
- `[ns_cw9i_VI_447]` `[trigger: two_horses]` `[factor_trigger: jung_opposites AND jung_wholeness]` `[role: 主干依赖]` Two horses together = complete union of opposites: feminine triad (unconscious) + masculine quaternity (conscious). → §447-450
- `[ns_cw9i_VI_453]` `[trigger: spirit_ambivalent]` `[factor_trigger: jung_spirit AND jung_ambivalence]` `[role: 总结]` Spirit archetype is ambivalent—can help or possess; the decisive factor is consciousness. → §451-453"""
    normalized_text_zh: str = """"""
    subject: str = "§443-453 四腿马、方法论与原型的双重性"
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
        l1_anchor="acu_v1.0.0_443_453_四腿马_方法论与原型的双重性_001_L1",
    )
    version: str = "1.0.0"
