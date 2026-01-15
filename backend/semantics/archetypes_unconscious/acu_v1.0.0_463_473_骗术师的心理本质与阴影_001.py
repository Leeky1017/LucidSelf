"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.545085
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
    semantic_id="acu_v1.0.0_463_473_骗术师的心理本质与阴影_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 463473骗术师的心理本质与阴影(SemanticEntry):
    """
    **原文** (§463-473, 行7248-7399):

> [463-464] Du Cange says that the more ridiculous the rite seemed, ...
    """
    
    original_text: str = """**原文** (§463-473, 行7248-7399):

> [463-464] Du Cange says that the more ridiculous the rite seemed, the greater the enthusiasm with which it was celebrated. The ass was brought into symbolic relationship with Christ. These medieval customs demonstrate the role of the trickster to perfection, and when they vanished from the Church, they appeared again on the profane level of Italian theatricals—Pulcinellas, Cucorognas, Chico Sgarras.
>
> [465] In picaresque tales, in carnivals and revels, in magic rites of healing, in man's religious fears and exaltations, this phantom of the trickster haunts the mythology of all ages. He is obviously a "psychologem," an archetypal psychic structure of extreme antiquity. In his clearest manifestations he is a faithful reflection of an absolutely undifferentiated human consciousness, corresponding to a psyche that has hardly left the animal level.
>
> [468-469] Split or double personality form the core of the earliest psychopathological investigations. The split-off personality stands in a complementary or compensatory relationship to the ego-personality. A collective personification like the trickster is the product of an aggregate of individuals. If the myth were nothing but an historical remnant, why has it not vanished? The trickster motif appears in the unsuspecting modern man whenever he feels himself at the mercy of "accidents"—"hoodoos" and "jinxes." I have called this character-component the shadow.
>
> [470-473] Radin's trickster cycle preserves the shadow in its pristine mythological form. Only when consciousness reached a higher level could he detach the earlier state and objectify it. The trickster is a forerunner of the saviour. The myth is not merely a sham exhibition; the sufferings of the trickster are real and therapeutic. Through laughter man rises above his own predicament.

**英文释义**：
- 中世纪仪式：越荒谬越热情地庆祝
- 驴被与基督联系 → 兽形神论危险
- 这些习俗完美展示骗术师角色
- 从教会消失后 → 世俗戏剧（Pulcinella等）
- 骗术师=psychologem（心理元素），极古老的原型心理结构
- 反映完全未分化的人类意识 ≈ 刚脱离动物水平的心灵
- 分裂人格是最早的精神病理学研究核心
- 分裂人格与自我人格处于补偿关系
- 现代人遇"倒霉"时骗术师出现 → 阴影
- 骗术师=原始形式的阴影
- 骗术师=救世主的先驱
- 骗术师的痛苦是真实的、治疗性的
- 通过笑声人超越自身困境

**中文诠释**：
- 中世纪驴子节：仪式越荒谬越热情
- 驴与基督的象征联系 → 兽形神论（theriomorphism）的危险
- 教会习俗消失后出现在世俗戏剧中
- 骗术师 = "psychologem" = 极古老的原型心理结构
- 反映完全未分化的意识 ≈ 几乎未脱离动物水平
- 分裂人格/双重人格 = 精神病理学的核心研究
- 分裂人格与自我处于补偿关系
- 现代人遇"倒霉事"时骗术师出现 → 阴影
- 拉丁的骗术师循环保存原始形式的阴影
- 只有意识达到更高水平才能客体化早期状态
- 骗术师 = 救世主的先驱
- 痛苦是真实的、具有治疗性
- 笑声使人超越困境

**Narrative Snippets**:
- `[ns_cw9i_VII_465]` `[trigger: trickster_psychologem]` `[factor_trigger: jung_trickster AND jung_archetype]` `[role: 主干]` Trickster is a psychologem—archetypal structure of extreme antiquity, reflecting undifferentiated consciousness barely above animal level. → §465
- `[ns_cw9i_VII_469]` `[trigger: trickster_shadow]` `[factor_trigger: jung_trickster AND jung_shadow]` `[role: 主干依赖]` Trickster motif appears in modern man's "accidents"—I call this component the shadow. → §469
- `[ns_cw9i_VII_472]` `[trigger: trickster_saviour]` `[factor_trigger: jung_trickster AND jung_redemption]` `[role: 条件分支]` Trickster is forerunner of saviour; his sufferings are real and therapeutic—through laughter man rises above his predicament. → §472"""
    normalized_text_zh: str = """"""
    subject: str = "§463-473 骗术师的心理本质与阴影"
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
        l1_anchor="acu_v1.0.0_463_473_骗术师的心理本质与阴影_001_L1",
    )
    version: str = "1.0.0"
