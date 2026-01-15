"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535627
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
    semantic_id="acu_v1.0.0_261_神话是经历而非发明_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 261神话是经历而非发明(SemanticEntry):
    """
    **原文** (¶261, 行4408-4420):

> [261] The primitive mentality does not invent myths, it experiences th...
    """
    
    original_text: str = """**原文** (¶261, 行4408-4420):

> [261] The primitive mentality does not invent myths, it experiences them. Myths are original revelations of the preconscious psyche, involuntary statements about unconscious psychic happenings, and anything but allegories of physical processes. Such allegories would be an idle amusement for an unscientific intellect. Myths, on the contrary, have a vital meaning. Not merely do they represent, they are the psychic life of the primitive tribe, which immediately falls to pieces and decays when it loses its mythological heritage, like a man who has lost his soul. A tribe's mythology is its living religion, whose loss is always and everywhere, even among the civilized, a moral catastrophe. But religion is a vital link with psychic processes independent of and beyond consciousness, in the dark hinterland of the psyche.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Primitive mentality (原始心智) | 未开化的思维 | 前意识状态 | 神话产生的心理条件 |
| Preconscious psyche (前意识心灵) | 意识之前的心理 | 神话的真正源头 | 集体无意识 |
| Vital meaning (生命意义) | 重要意义 | 存在性价值 | 神话对部落的意义 |
| Living religion (活的宗教) | 实践中的信仰 | 神话的宗教功能 | 神话=宗教 |

**英文释义（主语言）**:

**核心论断**：原始心智不发明神话，而是**经历**神话。

**神话的本质**：
- 前意识心灵的原初启示
- 关于无意识心理事件的非自愿陈述
- 绝非物理过程的寓言（那只是"非科学智力的无聊消遣"）
- 相反，神话具有**生命意义**

**神话与部落**：
- 神话不仅代表，神话**就是**原始部落的心理生活
- 失去神话遗产 = 部落立即崩溃瓦解
- 如同"失去灵魂的人"

**神话 = 活的宗教**：
- 失去神话/宗教 = 道德灾难（无论文明与否）
- 宗教是与独立于意识之外的心理过程的重要联系
- 在心灵的"黑暗腹地"

**完整中文诠释（次语言）**:

**神话的经历性本质**：

荣格在此提出关于神话本质的核心论断：原始心智不是"发明"神话，而是"经历"神话。这个区分至关重要——神话不是智力创造的产物，而是心灵直接经验的内容。

**神话是什么**：
- 前意识心灵的原初启示
- 关于无意识心理事件的非自愿陈述
- 绝非物理过程的寓言

**神话不是什么**：
- 不是物理过程的象征性表达
- 那种解释只是"非科学智力的无聊消遣"

**神话的生命意义**：
神话不仅仅是"代表"什么，神话**就是**原始部落的心理生活本身。当一个部落失去其神话遗产时，它会立即崩溃瓦解——就像一个失去灵魂的人。

**神话作为活的宗教**：
一个部落的神话就是它的活宗教。失去这种宗教——无论在原始人还是文明人中——总是、到处都是一场道德灾难。宗教是与独立于意识之外、超越意识的心理过程的重要联系，在心灵的黑暗腹地中。

**核心要点**:
- 神话是经历，不是发明
- 神话 = 前意识心灵的原初启示
- 神话 ≠ 物理过程的寓言
- 神话 = 部落的心理生活本身
- 失去神话 = 失去灵魂 = 道德灾难
- 神话 = 活的宗教
- 宗教联系心灵的黑暗腹地

**叙事片段**:
- `[ns_cw9i_IV_261_001]` `[trigger: myth_experience]` `[factor_trigger: jung_myth]` `[role: 主干]` 原始心智不发明神话，而是经历神话——神话是前意识心灵的原初启示。→ ¶261
- `[ns_cw9i_IV_261_002]` `[trigger: myth_vital]` `[factor_trigger: jung_myth AND jung_soul]` `[role: 主干依赖]` 神话就是原始部落的心理生活——失去神话遗产如同失去灵魂。→ ¶261
- `[ns_cw9i_IV_261_003]` `[trigger: myth_religion]` `[factor_trigger: jung_myth AND jung_religion]` `[role: 主干依赖]` 部落的神话就是它的活宗教——失去它总是道德灾难。→ ¶261

**版本考证（双语）**:
- **English**: N/A - Single authoritative source.
- **中文**: 无版本差异。"""
    normalized_text_zh: str = """"""
    subject: str = "¶261 神话是经历而非发明"
    factor_refs: list = ['engine_id', 'myth_as_experience', 'psych_semantic', 'preconscious_psyche', 'psych_semantic', 'living_religion', 'psych_semantic', 'soul_loss', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_261_神话是经历而非发明_001_L1",
    )
    version: str = "1.0.0"
