"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535910
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
    semantic_id="acu_v1.0.0_287_遗弃是必要条件_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 287遗弃是必要条件(SemanticEntry):
    """
    **原文** (¶287, 行4804-4824):

> [287] "Child" means something evolving towards independence. This it c...
    """
    
    original_text: str = """**原文** (¶287, 行4804-4824):

> [287] "Child" means something evolving towards independence. This it cannot do without detaching itself from its origins: abandonment is therefore a necessary condition, not just a concomitant symptom. The conflict is not to be overcome by the conscious mind remaining caught between the opposites, and for this very reason it needs a symbol to point out the necessity of detaching itself from its origins. Because the symbol of the "child" fascinates and grips the conscious mind, its redemptive effect passes over into consciousness and brings about that separation from the conflict-situation which the conscious mind by itself was unable to achieve. The symbol anticipates a nascent state of consciousness. So long as this is not actually in being, the "child" remains a mythological projection which requires religious repetition and renewal by ritual. The Christ Child, for instance, is a religious necessity only so long as the majority of men are incapable of giving psychological reality to the saying: "Except ye become as little children…"

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Independence (独立) | 自主 | 个体化目标 | 童子的方向 |
| Abandonment as condition (遗弃作为条件) | 遗弃作为必要条件 | 与起源分离 | 非仅症状 |
| Religious repetition (宗教重复) | 仪式重复 | 象征的维持 | 在意识实现前 |

**英文释义（主语言）**:

**童子 = 走向独立**：
"童子"意味着某种**向独立进化的东西**。这必须通过与起源分离才能做到：因此遗弃是**必要条件**，不仅仅是伴随症状。

**象征的必要性**：
冲突不能通过意识心智继续困在对立之间来克服。正因如此，需要一个象征来指出与起源分离的必要性。

**童子象征的救赎效果**：
因为"童子"象征迷住并抓住意识心智，其救赎效果传入意识，带来意识心智自身无法实现的与冲突情境的分离。

**象征预期萌芽意识**：
象征预期一种萌芽的意识状态。只要这种状态尚未实际存在，"童子"就仍然是一个需要宗教重复和仪式更新的神话投射。

**基督童子的例子**：
例如，基督童子只在大多数人无法给"你们若不变成小孩子……"这句话以心理现实时才是宗教必需。

**完整中文诠释（次语言）**:

**童子的本质 = 走向独立**：
"童子"意味着某种**向独立进化的东西**。这必须通过与起源分离才能做到：因此遗弃是**必要条件**，不仅仅是伴随症状。

**象征的功能必要性**：
冲突不能通过意识心智继续困在对立之间来克服。正因如此，需要一个象征来指出与起源分离的必要性。

**童子象征的心理机制**：
因为"童子"象征迷住并抓住意识心智，其救赎效果传入意识，带来意识心智自身无法实现的与冲突情境的分离。象征预期一种萌芽的意识状态。

**宗教形式的心理学功能**：
只要这种状态尚未实际存在，"童子"就仍然是一个需要宗教重复和仪式更新的神话投射。例如，基督童子只在大多数人无法给"你们若不变成小孩子……"这句话以心理现实时才是宗教必需。

**所有神话形象的一般原则**：
人应该但又不能成为或做的一切（无论是正面还是负面意义）——作为神话形象和预期，与其意识一起存在，要么作为宗教投射，要么——更危险的——作为无意识内容自发投射到不协调的对象上，如卫生和其他"救赎"主义学说或实践。所有这些都是神话的理性化替代品，其不自然性弊大于利。

**核心要点**:
- 童子 = 向独立进化的东西
- 遗弃 = 必要条件，非仅伴随症状
- 必须与起源分离才能独立
- 象征指出分离必要性
- 童子象征的救赎效果传入意识
- 象征预期萌芽意识状态
- 基督童子是宗教必需——当人们无法内化其意义时
- 神话投射需要宗教重复和仪式更新

**叙事片段**:
- `[ns_cw9i_IV_287_001]` `[trigger: abandonment_necessary]` `[factor_trigger: jung_child_archetype AND jung_independence]` `[role: 主干]` 童子=向独立进化；遗弃是必要条件，非仅症状——必须与起源分离才能独立。→ ¶287
- `[ns_cw9i_IV_287_002]` `[trigger: symbol_redemption]` `[factor_trigger: jung_symbol AND jung_consciousness]` `[role: 主干依赖]` 童子象征迷住意识，其救赎效果带来意识自身无法实现的分离；象征预期萌芽意识状态。→ ¶287"""
    normalized_text_zh: str = """"""
    subject: str = "¶287 遗弃是必要条件"
    factor_refs: list = ['engine_id', 'abandonment_necessary', 'psych_semantic', 'independence', 'psych_semantic', 'redemptive_effect', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_287_遗弃是必要条件_001_L1",
    )
    version: str = "1.0.0"
