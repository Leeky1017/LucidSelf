"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535999
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
    semantic_id="acu_v1.0.0_298_299_童子作为开端与终结_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 298299童子作为开端与终结(SemanticEntry):
    """
    **原文** (¶298-299, 行5063-5092):

> [298] Faust, after his death, is received as a boy into the "choir...
    """
    
    original_text: str = """**原文** (¶298-299, 行5063-5092):

> [298] Faust, after his death, is received as a boy into the "choir of blessed youths."... The sea is the favourite symbol for the unconscious, the mother of all that lives...
>
> [299] The "child" is therefore renatus in novam infantiam. It is thus both beginning and end, an initial and a terminal creature. The initial creature existed before man was, and the terminal creature will be when man is not. Psychologically speaking, this means that the "child" symbolizes the pre-conscious and the post-conscious essence of man. His pre-conscious essence is the unconscious state of earliest childhood; his post-conscious essence is an anticipation by analogy of life after death. In this idea the all-embracing nature of psychic wholeness is expressed. Wholeness is never comprised within the compass of the conscious mind—it includes the indefinite and indefinable extent of the unconscious as well.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Renatus in novam infantiam | 重生为新婴儿 | 死后重生 | 拉丁语 |
| Beginning and end (开端与终结) | 开始和结束 | 童子的双重本质 | 循环性 |
| Pre-conscious (前意识) | 意识之前 | 最早童年 | 起源 |
| Post-conscious (后意识) | 意识之后 | 死后生命 | 终点 |

**英文释义（主语言）**:

**浮士德的例子**：
浮士德死后作为男孩被接入"有福青年的合唱"。海是无意识的最喜爱象征——一切生物的母亲。

**童子 = 开端与终结**：
"童子"因此是**renatus in novam infantiam（重生为新婴儿）**。因此它既是**开端也是终结**——一个初始和终端的生物。

**初始与终端生物**：
- 初始生物在人存在之前就存在
- 终端生物在人不存在时将存在

**心理学意义**：
"童子"象征人的**前意识本质和后意识本质**：
- 前意识本质 = 最早童年的无意识状态
- 后意识本质 = 死后生命的类比预期

**心理整体性的全包性**：
在这个观念中表达了心理整体性的**全包本性**。整体性永远不能包含在意识心智的范围内——它也包括无意识的不确定和不可定义的范围。

**整体性的时间特征**：
整体性，从经验上讲，因此是**不可测量的范围**，比意识更老也更年轻，在时间和空间上包裹着它。

**完整中文诠释（次语言）**:

**浮士德的象征性例子**：
浮士德死后作为男孩被接入"有福青年的合唱"。荣格不确定歌德是否在暗示古代墓碑上的丘比特。cucullatus（戴兜帽者）指向戴兜帽的、即不可见的离世者的守护神，他在类似童子的嬉戏中以新生命重新出现，被海豚和特里同的海洋形式环绕。海是无意识的最喜爱象征——一切生物的母亲。

**童子的双重本质**：
"童子"因此是**renatus in novam infantiam（重生为新婴儿）**。因此它既是**开端也是终结**——一个初始和终端的生物。初始生物在人存在之前就存在，终端生物在人不存在时将存在。

**心理学解读**：
从心理学上讲，这意味着"童子"象征人的**前意识本质和后意识本质**。他的前意识本质是最早童年的无意识状态；他的后意识本质是死后生命的类比预期。

**心理整体性的表达**：
在这个观念中表达了心理整体性的**全包本性**。整体性永远不能包含在意识心智的范围内——它也包括无意识的不确定和不可定义的范围。整体性，从经验上讲，因此是**不可测量的范围**，比意识更老也更年轻，在时间和空间上包裹着它。

**核心要点**:
- 浮士德死后作为男孩重生——海=无意识=一切生物之母
- 童子 = renatus in novam infantiam（重生为新婴儿）
- 童子 = 开端 + 终结（初始+终端生物）
- 初始生物在人之前，终端生物在人之后
- 童子象征前意识本质（最早童年）+ 后意识本质（死后生命）
- 整体性 = 全包，超越意识范围
- 整体性比意识更老更年轻，在时空上包裹意识

**叙事片段**:
- `[ns_cw9i_IV_298_001]` `[trigger: beginning_end]` `[factor_trigger: jung_child_archetype AND jung_time]` `[role: 主干]` 童子=开端+终结，初始+终端生物——象征前意识本质和后意识本质。→ ¶298-299
- `[ns_cw9i_IV_299_001]` `[trigger: wholeness_all_embracing]` `[factor_trigger: jung_wholeness AND jung_unconscious]` `[role: 主干依赖]` 整体性=全包，超越意识范围——比意识更老更年轻，在时空上包裹意识。→ ¶299"""
    normalized_text_zh: str = """"""
    subject: str = "¶298-299 童子作为开端与终结"
    factor_refs: list = ['engine_id', 'beginning_end', 'psych_semantic', 'pre_conscious', 'psych_semantic', 'post_conscious', 'psych_semantic', 'all_embracing', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_298_299_童子作为开端与终结_001_L1",
    )
    version: str = "1.0.0"
