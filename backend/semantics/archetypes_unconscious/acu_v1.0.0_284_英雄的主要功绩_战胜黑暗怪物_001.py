"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535881
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
    semantic_id="acu_v1.0.0_284_英雄的主要功绩_战胜黑暗怪物_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 284英雄的主要功绩战胜黑暗怪物(SemanticEntry):
    """
    **原文** (¶284, 行4759-4769):

> [284] The hero's main feat is to overcome the monster of darkness: it ...
    """
    
    original_text: str = """**原文** (¶284, 行4759-4769):

> [284] The hero's main feat is to overcome the monster of darkness: it is the long-hoped-for and expected triumph of consciousness over the unconscious. Day and light are synonyms for consciousness, night and dark for the unconscious. The coming of consciousness was probably the most tremendous experience of primeval times, for with it a world came into being whose existence no one had suspected before. "And God said: 'Let there be light!'" is the projection of that immemorial experience of the separation of the conscious from the unconscious. Even among primitives today the possession of a soul is a precarious thing, and the "loss of soul" a typical psychic malady which drives primitive medicine to all sorts of psychotherapeutic measures. Hence the "child" distinguishes itself by deeds which point to the conquest of the dark.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Monster of darkness (黑暗怪物) | 黑暗中的怪物 | 无意识 | 英雄的对手 |
| Light (光) | 光明 | 意识 | 同义词 |
| Loss of soul (灵魂丧失) | 失去灵魂 | 典型心理疾病 | 原始心理学 |

**英文释义（主语言）**:

**英雄的主要功绩**：
战胜黑暗怪物——这是期待已久的**意识战胜无意识的胜利**。

**象征等式**：
- 白天和光 = 意识的同义词
- 黑夜和黑暗 = 无意识的同义词

**意识到来的原初体验**：
意识的到来可能是原始时代最巨大的体验，因为随之而来的是一个以前没有人怀疑存在的世界。

**"要有光"的心理学意义**：
"神说：'要有光！'"是意识与无意识分离这一太古体验的投射。

**灵魂丧失**：
即使在今天的原始人中，拥有灵魂也是不稳定的事，"灵魂丧失"是典型的心理疾病，驱使原始医学采取各种心理治疗措施。

**童子的功绩**：
因此，"童子"以指向**战胜黑暗**的功绩而著称。

**完整中文诠释（次语言）**:

**英雄的主要功绩**：
英雄的主要功绩是战胜黑暗怪物：这是期待已久的、期望的**意识战胜无意识的胜利**。

**象征学等式**：
白天和光是意识的同义词，黑夜和黑暗是无意识的同义词。

**意识到来的重大意义**：
意识的到来可能是原始时代最巨大的体验，因为随之而来的是一个以前没有人怀疑存在的世界。

**圣经的心理学解读**：
"神说：'要有光！'"是意识与无意识分离这一太古体验的投射。

**灵魂丧失的心理学意义**：
即使在今天的原始人中，拥有灵魂也是不稳定的事，"灵魂丧失"是典型的心理疾病，驱使原始医学采取各种心理治疗措施。

**童子的象征功能**：
因此，"童子"以指向**战胜黑暗**的功绩而著称——童子象征着意识战胜无意识的过程。

**核心要点**:
- 英雄主要功绩 = 战胜黑暗怪物 = 意识战胜无意识
- 光/白天 = 意识；黑暗/黑夜 = 无意识
- 意识到来 = 原始时代最巨大体验
- "要有光" = 意识与无意识分离的投射
- 灵魂丧失 = 原始人典型心理疾病
- 童子的功绩指向战胜黑暗

**叙事片段**:
- `[ns_cw9i_IV_284_001]` `[trigger: conquer_darkness]` `[factor_trigger: jung_hero AND jung_consciousness]` `[role: 主干]` 英雄主要功绩是战胜黑暗怪物——意识战胜无意识的胜利；"要有光"是此太古体验的投射。→ ¶284
- `[ns_cw9i_IV_284_002]` `[trigger: loss_of_soul]` `[factor_trigger: jung_soul_loss]` `[role: 主干依赖]` 灵魂丧失是原始人典型心理疾病——童子的功绩指向战胜黑暗。→ ¶284"""
    normalized_text_zh: str = """"""
    subject: str = "¶284 英雄的主要功绩：战胜黑暗怪物"
    factor_refs: list = ['engine_id', 'conquer_darkness', 'psych_semantic', 'light_consciousness', 'psych_semantic', 'soul_loss', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_284_英雄的主要功绩_战胜黑暗怪物_001_L1",
    )
    version: str = "1.0.0"
