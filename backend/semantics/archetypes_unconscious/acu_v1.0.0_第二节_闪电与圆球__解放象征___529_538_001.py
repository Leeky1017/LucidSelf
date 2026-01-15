"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.519955
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
    semantic_id="acu_v1.0.0_第二节_闪电与圆球__解放象征___529_538_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第二节闪电与圆球解放象征529538(SemanticEntry):
    """
    **原文** (¶529-538, 行8221-8405):

> [529] 我已经从她之前的历史中看到无意识如何利用病人无法绘画的能力来暗示自己的建议。我没有忽视石头已经悄悄地转变成了蛋...蛋是...
    """
    
    original_text: str = """**原文** (¶529-538, 行8221-8405):

> [529] 我已经从她之前的历史中看到无意识如何利用病人无法绘画的能力来暗示自己的建议。我没有忽视石头已经悄悄地转变成了蛋...蛋是具有崇高象征意义的生命胚芽。它不仅是宇宙起源的象征——它也是"哲学"象征。
>
> [530] 从这个暗示，我已经能看到无意识心中有什么解决方案，即个体化，因为这是松开对无意识依附的转化过程。
>
> [538] 闪电击入黑暗和"硬度"，从黑暗的混沌物质中炸出一个圆形，并在其中点燃了光。毫无疑问，黑暗的石头意味着黑暗，即无意识。

**英文释义**:

石头 → 蛋的转变：无意识暗示。蛋 = 生命胚芽，宇宙起源（俄耳甫斯蛋）+ 哲学象征（炼金术蛋 → 小人 → 内在完整人）。荣格识别出无意识的解决方案 = 个体化（松开对无意识的依附）。第二幅画：闪电取代魔法师，圆球取代病人 = 非个人自然过程。闪电 = 突然、出人意料的心理状态改变。圆球 = 自性/整体。

**完整中文诠释**:

**象征转变**：
- 石头 → 蛋：无意识自动暗示（利用她无法绘画）
- 蛋 = 俄耳甫斯蛋（世界起源）+ 哲学蛋（炼金术）
- 哲学蛋 → 小人（homunculus）→ 内在完整人（Anthropos）

**个体化线索**：
- 荣格从蛋的象征看出无意识的"解决方案"
- 个体化 = 松开对无意识依附的转化过程
- 是"决定性解决方案"

**第二幅画**：
- 魔法师 → 闪电（非个人化）
- 病人 → 圆球（非个人化）
- 个人关系消失 → 非个人自然过程
- 闪电 = 突然、出人意料的心理状态改变

**圆球的意义**：
- = rotundum（圆形）= Anthropos的原始形式
- = 灵魂（圆形，按传统）
- = 自性（荣格术语）

**核心要点**:
- 石头→蛋：无意识利用技术限制暗示自己的象征
- 蛋 = 宇宙起源 + 哲学象征 → 内在完整人
- 个体化 = 无意识提供的决定性解决方案
- 闪电取代魔法师 = 非个人化过程
- 圆球 = 自性象征

**叙事片段**:
- `[ns_cw9i_IX_002]` `[trigger: 蛋象征]` `[factor_trigger: jung_egg_symbol AND jung_individuation]` `[role: 主干]` 石头转变为蛋——生命胚芽，哲学象征——无意识暗示个体化是解决方案。→ ¶529-530
- `[ns_cw9i_IX_003]` `[trigger: 闪电解放]` `[factor_trigger: jung_lightning AND jung_liberation]` `[role: 主干依赖]` 闪电从黑暗混沌中炸出圆球——突然的心理状态改变——圆球=自性。→ ¶538"""
    normalized_text_zh: str = """"""
    subject: str = "第二节：闪电与圆球——解放象征 (¶529-538)"
    factor_refs: list = ['egg_symbol', 'lightning_liberation', 'rotundum', 'depersonalization']
    
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
        l1_anchor="acu_v1.0.0_第二节_闪电与圆球__解放象征___529_538_001_L1",
    )
    version: str = "1.0.0"
