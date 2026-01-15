"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535653
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
    semantic_id="acu_v1.0.0_263_原型内容的产生条件_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 263原型内容的产生条件(SemanticEntry):
    """
    **原文** (¶263, 行4440-4449):

> [263] The products of this second category resemble the types of struc...
    """
    
    original_text: str = """**原文** (¶263, 行4440-4449):

> [263] The products of this second category resemble the types of structures to be met with in myth and fairytale so much that we must regard them as related. It is therefore wholly within the realm of possibility that both, the mythological types as well as the individual types, arise under quite similar conditions. As already mentioned, the fantasy-products of the second category (as also those of the first) arise in a state of reduced intensity of consciousness (in dreams, delirium, reveries, visions, etc.). In all these states the check put upon unconscious contents by the concentration of the conscious mind ceases, so that the hitherto unconscious material streams, as though from opened side-sluices, into the field of consciousness. This mode of origination is the general rule.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Reduced intensity of consciousness (意识强度降低) | 意识减弱 | 原型浮现条件 | 梦、谵妄、幻想等 |
| Check (抑制) | 阻止 | 意识对无意识的控制 | 正常清醒状态 |
| Side-sluices (侧闸) | 水闸 | 无意识涌入的通道 | 隐喻 |

**英文释义（主语言）**:

**第二类产物与神话/童话的关系**：
- 非常相似，必须视为相关
- 两者可能在相当相似的条件下产生

**产生条件**：
- 意识强度降低的状态
- 包括：梦、谵妄、幻想、幻觉等
- 在这些状态中，意识集中对无意识内容的抑制停止
- 迄今为止的无意识材料涌入意识领域
- 如同"打开的侧闸"

**完整中文诠释（次语言）**:

**第二类产物与神话的关联**：
第二类产物（非个人幻想）与神话和童话中的结构类型非常相似，我们必须视它们为相关的。因此，神话类型和个体类型都在相当相似的条件下产生，这完全在可能性范围内。

**原型内容产生的条件**：
如前所述，第二类（以及第一类）幻想产物产生于**意识强度降低的状态**，包括：
- 梦
- 谵妄
- 幻想
- 幻觉等

**机制解释**：
在所有这些状态中，意识心智的集中对无意识内容的抑制停止了。结果是，迄今为止的无意识材料涌入意识领域——就像打开了侧闸一样。这种产生方式是一般规律。

**核心要点**:
- 非个人幻想与神话/童话结构高度相似
- 两者在相似条件下产生
- 条件 = 意识强度降低（梦、谵妄、幻想、幻觉）
- 机制 = 意识抑制停止 → 无意识涌入
- "侧闸"隐喻：无意识内容的涌入通道

**叙事片段**:
- `[ns_cw9i_IV_263_001]` `[trigger: reduced_consciousness]` `[factor_trigger: jung_consciousness AND jung_archetype]` `[role: 主干]` 原型内容产生于意识强度降低的状态——梦、谵妄、幻想、幻觉——此时意识抑制停止，无意识如打开的侧闸涌入。→ ¶263

**版本考证（双语）**:
- **English**: N/A - Single authoritative source.
- **中文**: 无版本差异。"""
    normalized_text_zh: str = """"""
    subject: str = "¶263 原型内容的产生条件"
    factor_refs: list = ['engine_id', 'reduced_consciousness', 'psych_semantic', 'check_cessation', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_263_原型内容的产生条件_001_L1",
    )
    version: str = "1.0.0"
