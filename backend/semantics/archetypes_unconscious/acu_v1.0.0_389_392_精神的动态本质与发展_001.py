"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498109
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
    semantic_id="acu_v1.0.0_389_392_精神的动态本质与发展_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 389392精神的动态本质与发展(SemanticEntry):
    """
    **原文** (§389-392, 行5941-5984):

> [389] In keeping with its original wind-nature, spirit is always a...
    """
    
    original_text: str = """**原文** (§389-392, 行5941-5984):

> [389] In keeping with its original wind-nature, spirit is always an active, winged, swift-moving being as well as that which vivifies, stimulates, incites, fires, and inspires. Spirit is the dynamic principle, forming the classical antithesis of matter—of its stasis and inertia. Basically it is the contrast between life and death.
>
> [390] Man's special development of spirit rests on the recognition that its invisible presence is a psychic phenomenon. Among the first are images and shadowy presentations; among the second, thinking and reason which organize the world of images. A transcendent spirit superimposed itself upon the original life-spirit and became the supranatural cosmic principle of order, given the name "God."
>
> [391] The corresponding development of spirit in the reverse, hylozoistic direction took place under anti-Christian auspices in materialism. The premise is the spirit's identity with psychic functions dependent upon brain and metabolism. One had only to call the One Substance "matter" to produce the idea of a spirit entirely dependent on nutrition and environment.
>
> [392] Spirit as "subjective spirit" came to mean a purely endopsychic phenomenon, while "objective spirit" meant merely the sum total of intellectual and cultural possessions. Spirit had forfeited its original nature, its autonomy and spontaneity, except in the religious field.

**英文释义**：
- 精神的风之本性：主动、有翅、敏捷、活化、刺激、激发
- 精神 = 动态原理 ↔ 物质 = 静止和惰性
- 基本对比：生命 vs 死亡
- 发展：自然生命精神 → 超验精神 → 宇宙秩序原理 = "上帝"
- 唯物主义反向发展：精神 = 依赖脑和代谢的心理功能
- 结果：精神丧失自主性和自发性（除宗教领域外）

**中文诠释**：
- 精神的原始风之本性 = 主动、有翅、敏捷
- 精神活化、刺激、激发、燃烧、启发
- 精神 = 动态原理 ↔ 物质 = 静止惰性
- 基本对比 = 生命 vs 死亡
- 精神发展史：自然生命精神 → 超验精神 → 宇宙秩序原理(上帝)
- 唯物主义：精神 = 依赖脑/代谢的心理功能
- 克拉格斯：精神 = 灵魂的敌人
- 精神丧失原始自主性（除宗教外）

**Narrative Snippets**:
- `[ns_cw9i_VI_389]` `[trigger: spirit_wind]` `[factor_trigger: jung_spirit AND jung_nature]` `[role: 主干]` Spirit's wind-nature: active, winged, swift—dynamic principle vs matter's stasis. → §389
- `[ns_cw9i_VI_390]` `[trigger: spirit_god]` `[factor_trigger: jung_spirit AND jung_god]` `[role: 主干依赖]` Transcendent spirit became supranatural cosmic order, named "God." → §390
- `[ns_cw9i_VI_391]` `[trigger: materialism]` `[factor_trigger: jung_spirit AND jung_materialism]` `[role: 条件分支]` Materialism: spirit = psychic functions dependent on brain/metabolism. → §391"""
    normalized_text_zh: str = """"""
    subject: str = "§389-392 精神的动态本质与发展"
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
        l1_anchor="acu_v1.0.0_389_392_精神的动态本质与发展_001_L1",
    )
    version: str = "1.0.0"
