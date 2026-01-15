"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535640
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
    semantic_id="acu_v1.0.0_262_两类幻想_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 262两类幻想(SemanticEntry):
    """
    **原文** (¶262, 行4424-4438):

> [262] Modern psychology treats the products of unconscious fantasy-act...
    """
    
    original_text: str = """**原文** (¶262, 行4424-4438):

> [262] Modern psychology treats the products of unconscious fantasy-activity as self-portraits of what is going on in the unconscious, or as statements of the unconscious psyche about itself. They fall into two categories. First, fantasies (including dreams) of a personal character, which go back unquestionably to personal experiences, things forgotten or repressed, and can thus be completely explained by individual anamnesis. Second, fantasies (including dreams) of an impersonal character, which cannot be reduced to experiences in the individual's past, and thus cannot be explained as something individually acquired. These fantasy-images undoubtedly have their closest analogues in mythological types. We must therefore assume that they correspond to certain collective (and not personal) structural elements of the human psyche in general, and, like the morphological elements of the human body, are inherited. Although tradition and transmission by migration certainly play a part, there are, as we have said, very many cases that cannot be accounted for in this way and drive us to the hypothesis of "autochthonous revival." These cases are so numerous that we are obliged to assume the existence of a collective psychic substratum. I have called this the collective unconscious.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Personal fantasy (个人幻想) | 个体的想象 | 传记性内容 | 可还原为个人经验 |
| Impersonal fantasy (非个人幻想) | 非个体的想象 | 集体性内容 | 不可还原为个人经验 |
| Anamnesis (回忆) | 医学问诊 | 个人历史回溯 | 精神分析方法 |
| Autochthonous revival (自生复活) | 本土的复兴 | 非传承的再现 | 集体无意识证据 |
| Collective unconscious (集体无意识) | 共同的无意识 | 人类共有心理基层 | 荣格核心概念 |

**英文释义（主语言）**:

**现代心理学的处理方式**：
无意识幻想活动的产物 = 无意识正在发生什么的自画像 = 无意识心灵关于自身的陈述

**两类幻想**：

1. **个人性质的幻想**（包括梦）：
   - 无疑可追溯到个人经验
   - 如遗忘或压抑的内容
   - 可通过个人回忆(anamnesis)完全解释

2. **非个人性质的幻想**（包括梦）：
   - 不能还原为个体过去的经验
   - 不能解释为个体获得的东西
   - 与神话类型有最接近的类比
   - 对应人类心灵的集体（非个人）结构元素
   - 如身体形态元素一样是遗传的

**自生复活假说**：
虽然传统和迁移传播确实起作用，但有很多案例无法这样解释，迫使我们假设"自生复活"。这些案例如此之多，我们不得不假设存在一个**集体心理基层**。荣格称之为**集体无意识**。

**完整中文诠释（次语言）**:

**现代心理学的观点**：
现代心理学将无意识幻想活动的产物视为：
- 无意识中正在发生什么的自画像
- 无意识心灵关于自身的陈述

**两类幻想的划分**：

**第一类：个人性质的幻想**（包括梦）
- 无疑可追溯到个人经验
- 包括遗忘或压抑的内容
- 可通过个人回忆(anamnesis)完全解释
- 这是弗洛伊德关注的领域

**第二类：非个人性质的幻想**（包括梦）
- 不能还原为个体过去的经验
- 不能解释为个体后天获得的东西
- 与神话类型有最接近的类比
- 我们必须假设它们对应于人类心灵的某些集体（而非个人）结构元素
- 如同人体的形态元素一样，它们是遗传的

**集体无意识假说的产生**：
虽然传统和通过迁移的传播确实起作用，但有非常多的案例无法用这种方式解释。这些案例迫使我们假设"自生复活"(autochthonous revival)——即独立于任何传统的自发再现。

这些案例如此之多，我们不得不假设存在一个**集体心理基层**。荣格将此命名为**集体无意识**。

**核心要点**:
- 无意识幻想 = 无意识的自画像/自我陈述
- 幻想分两类：个人的（可还原）和非个人的（不可还原）
- 个人幻想通过回忆可完全解释
- 非个人幻想与神话类型平行，是遗传的
- "自生复活"概念解释非传承的原型再现
- 集体无意识 = 集体心理基层

**叙事片段**:
- `[ns_cw9i_IV_262_001]` `[trigger: two_fantasy_types]` `[factor_trigger: jung_fantasy]` `[role: 主干]` 幻想分两类：个人的可通过回忆解释；非个人的不可还原，与神话类型平行。→ ¶262
- `[ns_cw9i_IV_262_002]` `[trigger: impersonal_inherited]` `[factor_trigger: jung_impersonal_fantasy AND jung_inheritance]` `[role: 主干依赖]` 非个人幻想对应集体结构元素，如身体形态元素一样是遗传的。→ ¶262
- `[ns_cw9i_IV_262_003]` `[trigger: collective_unconscious_origin]` `[factor_trigger: jung_collective_unconscious]` `[role: 主干依赖]` 大量无法用传统解释的案例迫使假设"自生复活"——由此产生集体无意识概念。→ ¶262

**版本考证（双语）**:
- **English**: N/A - Single authoritative source.
- **中文**: 无版本差异。"""
    normalized_text_zh: str = """"""
    subject: str = "¶262 两类幻想"
    factor_refs: list = ['engine_id', 'personal_fantasy', 'psych_semantic', 'impersonal_fantasy', 'psych_semantic', 'autochthonous_revival', 'psych_semantic', 'collective_unconscious', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_262_两类幻想_001_L1",
    )
    version: str = "1.0.0"
