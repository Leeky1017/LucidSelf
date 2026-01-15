"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535667
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
    semantic_id="acu_v1.0.0_264_心理水平下降与原始意识_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 264心理水平下降与原始意识(SemanticEntry):
    """
    **原文** (¶264, 行4451-4455):

> [264] Reduced intensity of consciousness and absence of concentration ...
    """
    
    original_text: str = """**原文** (¶264, 行4451-4455):

> [264] Reduced intensity of consciousness and absence of concentration and attention, Janet's abaissement du niveau mental, correspond pretty exactly to the primitive state of consciousness in which, we must suppose, myths were originally formed. It is therefore exceedingly probable that the mythological archetypes, too, made their appearance in much the same manner as the manifestations of archetypal structures among individuals today.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Abaissement du niveau mental | 心理水平下降（法语） | 意识降低状态 | 雅内术语 |
| Primitive state of consciousness | 原始意识状态 | 神话形成的条件 | 神话起源 |

**英文释义（主语言）**:

**雅内的概念**：
意识强度降低、注意力和集中力缺失 = 雅内的"心理水平下降"(abaissement du niveau mental)

**与原始意识的对应**：
这种状态相当精确地对应于原始意识状态——我们必须假设神话最初就是在这种状态中形成的。

**结论**：
因此，神话原型很可能也以与今天个体中原型结构显现非常相似的方式出现。

**完整中文诠释（次语言）**:

荣格在此引用雅内(Janet)的概念来解释原型产生的心理条件。

**心理水平下降**：
意识强度降低、注意力和集中力缺失——这就是雅内所称的"心理水平下降"(abaissement du niveau mental)。

**与原始意识的平行**：
这种状态相当精确地对应于原始意识状态。我们必须假设，神话最初就是在这种原始意识状态中形成的。

**古今的平行**：
因此，神话原型很可能也以与今天个体中原型结构显现非常相似的方式出现——即通过心理水平下降的状态。

**核心要点**:
- 雅内术语：abaissement du niveau mental = 心理水平下降
- 心理水平下降 = 原始意识状态
- 神话最初在原始意识状态中形成
- 今天个体中的原型显现 ≈ 古代神话原型的产生

**叙事片段**:
- `[ns_cw9i_IV_264_001]` `[trigger: abaissement]` `[factor_trigger: jung_consciousness AND jung_janet]` `[role: 主干]` 雅内的"心理水平下降"对应原始意识状态——神话最初就在此状态中形成，与今天个体中原型显现相似。→ ¶264

**版本考证（双语）**:
- **English**: N/A - Single authoritative source.
- **中文**: 无版本差异。"""
    normalized_text_zh: str = """"""
    subject: str = "¶264 心理水平下降与原始意识"
    factor_refs: list = ['engine_id', 'abaissement', 'psych_semantic', 'primitive_consciousness', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_264_心理水平下降与原始意识_001_L1",
    )
    version: str = "1.0.0"
