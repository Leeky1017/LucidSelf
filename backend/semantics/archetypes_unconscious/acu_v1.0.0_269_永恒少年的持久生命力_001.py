"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535726
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
    semantic_id="acu_v1.0.0_269_永恒少年的持久生命力_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 269永恒少年的持久生命力(SemanticEntry):
    """
    **原文** (¶269, 行4536-4539):

> [269] In the strange tale called Das Reich ohne Raum, by Bruno Goetz, ...
    """
    
    original_text: str = """**原文** (¶269, 行4536-4539):

> [269] In the strange tale called Das Reich ohne Raum, by Bruno Goetz, a puer aeternus named Fo (= Buddha) appears with whole troops of "unholy" boys of evil significance. (Contemporary parallels are better let alone.) I mention this instance only to demonstrate the enduring vitality of the child archetype.

**英文释义（主语言）**:

布鲁诺·戈茨的奇异故事《无空间之国》(Das Reich ohne Raum)中，一个名叫福(Fo = 佛陀)的永恒少年与成群的具有邪恶意义的"不圣洁"男孩一起出现。（当代的类比最好不提。）荣格提及这个例子只是为了证明**童子原型的持久生命力**。

**完整中文诠释（次语言）**:

荣格引用了布鲁诺·戈茨的奇异故事《无空间之国》：一个名叫福(Fo = 佛陀)的永恒少年与成群的具有邪恶意义的"不圣洁"男孩一起出现。

荣格括号中说"当代的类比最好不提"——暗示了某些不便明说的政治或文化现象。

荣格明确指出，他提及这个例子只是为了证明**童子原型的持久生命力**——即使在现代文学中，这个古老的原型仍然以新的形式活跃着。

**核心要点**:
- 《无空间之国》中的永恒少年福(=佛陀)
- 与"不圣洁"男孩群出现——邪恶意义
- 证明童子原型的持久生命力
- 原型在现代文学中仍活跃

**叙事片段**:
- `[ns_cw9i_IV_269_001]` `[trigger: puer_aeternus_modern]` `[factor_trigger: jung_puer_aeternus]` `[role: 主干]` 现代文学中永恒少年仍以新形式出现——证明童子原型的持久生命力。→ ¶269"""
    normalized_text_zh: str = """"""
    subject: str = "¶269 永恒少年的持久生命力"
    factor_refs: list = ['engine_id', 'enduring_vitality', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_269_永恒少年的持久生命力_001_L1",
    )
    version: str = "1.0.0"
