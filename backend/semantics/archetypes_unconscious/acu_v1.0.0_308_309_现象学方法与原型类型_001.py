"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.552666
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
    semantic_id="acu_v1.0.0_308_309_现象学方法与原型类型_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 308309现象学方法与原型类型(SemanticEntry):
    """
    **原文** (§308-309, 行5190-5215):

> [308] In view of the enormous complexity of psychic phenomena, a p...
    """
    
    original_text: str = """**原文** (§308-309, 行5190-5215):

> [308] In view of the enormous complexity of psychic phenomena, a purely phenomenological point of view is, and will be for a long time, the only possible one and the only one with any prospect of success...
>
> [309] Since for years I have been observing and investigating the products of the unconscious in the widest sense of the word, namely dreams, fantasies, visions, and delusions of the insane, I have not been able to avoid recognizing certain regularities, that is, types. There are types of situations and types of figures that repeat themselves frequently and have a corresponding meaning. I therefore employ the term "motif" to designate these repetitions... Among the latter there are human figures that can be arranged under a series of archetypes, the chief of them being... the shadow, the wise old man, the child (including the child hero), the mother ("Primordial Mother" and "Earth Mother") as a supraordinate personality ("daemonic" because supraordinate), and her counterpart the maiden, and lastly the anima in man and the animus in woman.

**英文释义（主语言）**:

**现象学方法的必要性**：
鉴于心理现象的巨大复杂性，纯粹的**现象学观点**是且将长期是唯一可能的、唯一有成功前景的观点。

**类型的发现**：
多年来观察和研究无意识产物（梦、幻想、幻觉、精神病妄想），荣格不得不承认某些**规律性**，即**类型**。存在反复出现的**情境类型**和**人物类型**，具有相应的意义。

**母题的使用**：
荣格使用**"母题"(motif)**一词来指称这些重复。

**主要原型列表**：
可按原型系列排列的人物形象，主要包括：
- **阴影**
- **智慧老人**
- **童子**（包括童子英雄）
- **母亲**（"原初母亲"和"大地母亲"）作为超位人格（因超位而"灵异"）
- **少女**（母亲的对应物）
- **阿尼玛**（在男性中）和**阿尼姆斯**（在女性中）

**完整中文诠释（次语言）**:

**现象学方法的必要性**：
鉴于心理现象的巨大复杂性，纯粹的**现象学观点**是且将长期是唯一可能的、唯一有成功前景的观点。"从何而来"和"是什么"这些问题，特别是在心理学领域，容易引发不成熟的解释尝试。

**类型和规律的发现**：
多年来观察和研究无意识产物（梦、幻想、幻觉、精神病妄想），荣格不得不承认某些**规律性**，即**类型**。存在反复出现的**情境类型**和**人物类型**，具有相应的意义。荣格使用**"母题"(motif)**一词来指称这些重复。

**主要原型的分类**：
可按原型系列排列的人物形象，主要包括：阴影、智慧老人、童子（包括童子英雄）、母亲（"原初母亲"和"大地母亲"）作为超位人格（因超位而"灵异"）、少女（母亲的对应物）、阿尼玛（在男性中）和阿尼姆斯（在女性中）。

**核心要点**:
- 现象学方法是研究心理现象的唯一可行途径
- 无意识产物（梦、幻想、幻觉、妄想）显示规律性类型
- "母题"指称反复出现的情境和人物类型
- 主要原型：阴影、智慧老人、童子、母亲、少女、阿尼玛/阿尼姆斯
- 母亲作为超位人格因超位而"灵异"

**叙事片段**:
- `[ns_cw9i_V_308_001]` `[trigger: phenomenology]` `[factor_trigger: jung_method]` `[role: 主干]` 现象学方法是研究心理现象的唯一可行途径——描述和分类优于过早解释。→ §308
- `[ns_cw9i_V_309_001]` `[trigger: archetype_list]` `[factor_trigger: jung_archetypes]` `[role: 主干]` 主要原型：阴影、智慧老人、童子、母亲、少女、阿尼玛/阿尼姆斯——反复出现的情境和人物类型。→ §309"""
    normalized_text_zh: str = """"""
    subject: str = "§308-309 现象学方法与原型类型"
    factor_refs: list = ['engine_id', 'phenomenology', 'psych_semantic', 'motif', 'psych_semantic', 'shadow', 'psych_semantic', 'wise_old_man', 'psych_semantic', 'anima_animus', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_308_309_现象学方法与原型类型_001_L1",
    )
    version: str = "1.0.0"
