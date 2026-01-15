"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535849
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
    semantic_id="acu_v1.0.0_281_童神与童英雄的区分_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 281童神与童英雄的区分(SemanticEntry):
    """
    **原文** (¶281, 行4722-4731):

> [281] Sometimes the "child" looks more like a child god, sometimes mor...
    """
    
    original_text: str = """**原文** (¶281, 行4722-4731):

> [281] Sometimes the "child" looks more like a child god, sometimes more like a young hero. Common to both types is the miraculous birth and the adversities of early childhood—abandonment and danger through persecution. The god is by nature wholly supernatural; the hero's nature is human but raised to the limit of the supernatural—he is "semi-divine." While the god, especially in his close affinity with the symbolic animal, personifies the collective unconscious which is not yet integrated into a human being, the hero's supernaturalness includes human nature and thus represents a synthesis of the ("divine," i.e., not yet humanized) unconscious and human consciousness. Consequently he signifies the potential anticipation of an individuation process which is approaching wholeness.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Child god (童神) | 儿童神祇 | 纯粹集体无意识 | 完全超自然 |
| Child hero (童英雄) | 儿童英雄 | 意识与无意识综合 | 半神 |
| Semi-divine (半神) | 一半神性 | 人性提升到超自然极限 | 英雄本质 |

**英文释义（主语言）**:

**两种童子类型**：
- 有时"童子"更像**童神**
- 有时更像**年轻英雄**

**共同特征**：
- 奇迹诞生
- 幼年的逆境：被遗弃、被迫害的危险

**童神vs童英雄的本质区别**：
- **童神**：本性完全超自然
  - 与象征动物的亲近性
  - 人格化尚未整合进人类的集体无意识
  
- **童英雄**：人性提升到超自然极限——"半神"
  - 超自然性包含人性
  - 代表（"神性"即尚未人化的）无意识与人类意识的综合
  - 意味着接近整体性的个体化过程的潜在预期

**完整中文诠释（次语言）**:

**两种童子类型**：
有时"童子"更像童神，有时更像年轻英雄。两种类型共同的是奇迹诞生和幼年的逆境——被遗弃和被迫害的危险。

**童神的本质**：
神的本性是完全超自然的。特别是在他与象征动物的亲近性中，神人格化了**尚未整合进人类的集体无意识**。

**童英雄的本质**：
英雄的本性是人性但提升到超自然的极限——他是"半神"。英雄的超自然性**包含人性**，因此代表（"神性"即尚未人化的）无意识与人类意识的**综合**。

**童英雄的个体化意义**：
因此，童英雄意味着**接近整体性的个体化过程的潜在预期**。

**核心要点**:
- 两种童子：童神 vs 童英雄
- 共同：奇迹诞生 + 幼年逆境
- 童神：完全超自然，人格化未整合的集体无意识
- 童英雄：半神，人性+超自然，意识与无意识综合
- 童英雄=个体化过程的潜在预期

**叙事片段**:
- `[ns_cw9i_IV_281_001]` `[trigger: child_god_hero]` `[factor_trigger: jung_child_archetype]` `[role: 主干]` 童神完全超自然，人格化未整合的集体无意识；童英雄是半神，代表意识与无意识的综合。→ ¶281
- `[ns_cw9i_IV_281_002]` `[trigger: hero_individuation]` `[factor_trigger: jung_hero AND jung_individuation]` `[role: 主干依赖]` 童英雄意味着接近整体性的个体化过程的潜在预期。→ ¶281"""
    normalized_text_zh: str = """"""
    subject: str = "¶281 童神与童英雄的区分"
    factor_refs: list = ['engine_id', 'child_god', 'psych_semantic', 'child_hero', 'psych_semantic', 'conscious_unconscious_synthesis', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_281_童神与童英雄的区分_001_L1",
    )
    version: str = "1.0.0"
