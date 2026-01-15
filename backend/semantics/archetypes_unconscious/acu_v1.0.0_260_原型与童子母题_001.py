"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535609
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
    semantic_id="acu_v1.0.0_260_原型与童子母题_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 260原型与童子母题(SemanticEntry):
    """
    **原文** (¶260, 行4370-4406):

> [260] These products are never (or at least very seldom) myths with a ...
    """
    
    original_text: str = """**原文** (¶260, 行4370-4406):

> [260] These products are never (or at least very seldom) myths with a definite form, but rather mythological components which, because of their typical nature, we can call "motifs," "primordial images," types or—as I have named them—archetypes. The child archetype is an excellent example. Today we can hazard the formula that the archetypes appear in myths and fairytales just as they do in dreams and in the products of psychotic fantasy. The medium in which they are embedded is, in the former case, an ordered and for the most part immediately understandable context, but in the latter case a generally unintelligible, irrational, not to say delirious sequence of images which nonetheless does not lack a certain hidden coherence. In the individual, the archetypes appear as involuntary manifestations of unconscious processes whose existence and meaning can only be inferred, whereas the myth deals with traditional forms of incalculable age...
>
> The archetype does not proceed from physical facts, but describes how the psyche experiences the physical fact, and in so doing the psyche often behaves so autocratically that it denies tangible reality or makes statements that fly in the face of it.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Motifs (母题) | 反复出现的主题 | 原型的表现形式 | 神话学术语 |
| Primordial images (原始意象) | 最初的图像 | 集体无意识内容 | 荣格早期术语 |
| Archetypes (原型) | 原初类型 | 心灵结构元素 | 荣格正式术语 |
| Child archetype (童子原型) | 儿童形象 | 新生、潜能、未来 | 本论文主题 |

**英文释义（主语言）**:

荣格定义原型的多重名称：
- **母题 (motifs)**
- **原始意象 (primordial images)**  
- **类型 (types)**
- **原型 (archetypes)** — 荣格的正式术语

**童子原型**是极好的例子。

**原型出现的媒介**：
- 神话/童话中 → 有序、可理解的语境
- 梦/精神病幻想中 → 不可理解、非理性的图像序列（但有隐藏的连贯性）

**原型的本质**：
- 不源于物理事实
- 描述心灵如何体验物理事实
- 心灵行为专制——可否认有形现实

**完整中文诠释（次语言）**:

荣格在此定义原型的基本概念：

**原型的多重命名**：
这些无意识产物从来不是（或极少是）具有确定形式的神话，而是神话组成成分。由于其典型性质，我们可称之为：
- "母题"
- "原始意象"  
- "类型"
- 或荣格命名的"原型"

**童子原型的典范地位**：
今天我们可以大胆提出公式：原型出现在神话和童话中，正如它们出现在梦和精神病幻想的产物中一样。

**两种出现媒介的对比**：
1. **神话/童话**：有序的、大部分可立即理解的语境
2. **梦/精神病幻想**：普遍难以理解、非理性、近乎谵妄的图像序列——但并非缺乏某种隐藏的连贯性

**在个体中**：原型表现为无意识过程的非自愿显现，其存在和意义只能推断。

**原型的根本本质**：
- 不是从物理事实推导而来
- 而是描述心灵如何体验物理事实
- 心灵常常表现得如此专制，以至于否认有形现实或作出与现实相悖的陈述

**核心要点**:
- 原型 = 母题 = 原始意象 = 类型（四个名称指同一概念）
- 童子原型是极好的例子
- 原型在神话/童话（有序）和梦/精神病幻想（无序但有隐藏连贯性）中出现
- 原型不源于物理事实，而是心灵体验物理事实的方式
- 心灵可专制地否认有形现实

**叙事片段**:
- `[ns_cw9i_IV_260_001]` `[trigger: archetype_names]` `[factor_trigger: jung_mandala_center AND jung_wholeness_symbol]` `[role: 主干]` 原型有多重名称：母题、原始意象、类型——童子原型是极好的例子。→ ¶260
- `[ns_cw9i_IV_260_002]` `[trigger: archetype_media]` `[factor_trigger: jung_opposites_union AND jung_jung_self]` `[role: 主干依赖]` 原型在神话/童话中以有序形式出现，在梦/精神病幻想中以无序但隐含连贯的形式出现。→ ¶260
- `[ns_cw9i_IV_260_003]` `[trigger: archetype_nature]` `[factor_trigger: jung_jung_yantra AND jung_contemplation_aid]` `[role: 主干依赖]` 原型不源于物理事实，而是描述心灵如何体验物理事实——心灵可专制地否认现实。→ ¶260
- `[ns_cw9i_IV_260_004]` `[trigger: shiva_shakti]` `[factor_trigger: jung_jung_shiva_shakti]` `[role: 条件分支]` The union of opposites in Eastern symbolism parallels the integration of archetypes. → ¶260

**版本考证（双语）**:
- **English**: N/A - Single authoritative source.
- **中文**: 无版本差异。"""
    normalized_text_zh: str = """"""
    subject: str = "¶260 原型与童子母题"
    factor_refs: list = ['engine_id', 'archetype', 'psych_semantic', 'child_archetype', 'psych_semantic', 'myth_fairytale', 'psych_semantic', 'dream_fantasy', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_260_原型与童子母题_001_L1",
    )
    version: str = "1.0.0"
