"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498229
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
    semantic_id="acu_v1.0.0_400_406_童话中的老人形象_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 400406童话中的老人形象(SemanticEntry):
    """
    **原文** (§400-406, 行6136-6248):

> [400] I would gladly present the reader with some more modern drea...
    """
    
    original_text: str = """**原文** (§400-406, 行6136-6248):

> [400] I would gladly present the reader with some more modern dream-material, but I fear that the individualism of dreams would make too high a demand upon our exposition... We shall therefore turn to folklore...
>
> [401] The frequency with which the spirit-type appears as an old man is about the same in fairytales as in dreams. The old man always appears when the hero is in a hopeless and desperate situation from which only profound reflection or a lucky idea... can extricate him.
>
> [406] The old man thus represents knowledge, reflection, insight, wisdom, cleverness, and intuition on the one hand, and on the other, moral qualities such as goodwill and readiness to help, which make his "spiritual" character sufficiently plain.

**英文释义（主语言）**:

**从梦到童话**：
童话中精神类型以老人形象出现的频率与梦中大致相同。

**老人出现的时机**：
老人总是在英雄处于**绝望境地**时出现——只有深刻反思或幸运想法才能使他摆脱困境。

**老人的象征功能**：
老人代表两方面品质：
- **智性品质**：知识、反思、洞察、智慧、聪明、直觉
- **道德品质**：善意、乐于助人

**老人的帮助方式**：
- 提问引发自我反思（谁？为何？从何？往何？）
- 给予必要的魔法护身符
- 指出通往目标的道路
- 警告即将到来的危险并提供应对手段
- 有时是批判性的老人

**完整中文诠释（次语言）**:

**转向童话材料**：
由于梦的个人主义会对阐释提出过高要求，荣格转向民间传说。在神话和童话中，如在梦中，心灵讲述自己的故事，原型的相互作用在其自然环境中展现。

**老人在童话中的普遍性**：
童话中精神类型以老人形象出现的频率与梦中大致相同。老人总是在英雄处于绝望境地时出现——只有深刻反思或幸运想法——换言之，精神功能或某种内心自动性——才能使他摆脱困境。

**老人的本质**：
老人代表两方面品质：一方面是知识、反思、洞察、智慧、聪明和直觉；另一方面是善意和乐于助人等道德品质——这使他的"精神"性质充分显明。由于原型是无意识的自主内容，童话使老人以与现代梦中相同的方式出现在梦中。

**核心要点**:
- 童话中老人出现频率 ≈ 梦中
- 出现时机：英雄处于绝望境地
- 老人功能：深刻反思/幸运想法的人格化
- 老人代表：知识、反思、洞察、智慧、聪明、直觉
- 老人代表：善意、乐于助人
- 帮助方式：提问、给护身符、指路、警告
- 老人 = 精神功能的自发客体化

**叙事片段**:
- `[ns_cw9i_VI_401_001]` `[trigger: old_man_fairytale]` `[factor_trigger: jung_wise_old_man AND jung_fairytale]` `[role: 主干]` 老人在英雄绝望时出现——代表知识、智慧、善意，是精神功能的人格化。→ §401-406"""
    normalized_text_zh: str = """"""
    subject: str = "§400-406 童话中的老人形象"
    factor_refs: list = ['engine_id', 'desperate_situation', 'psych_semantic', 'intellectual_qualities', 'psych_semantic', 'moral_qualities', 'psych_semantic', 'spontaneous_objectivation', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_400_406_童话中的老人形象_001_L1",
    )
    version: str = "1.0.0"
