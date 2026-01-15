"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789235
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
    semantic_id="mlxj_v1.0.0_3_二气盛衰虚实图说_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3二气盛衰虚实图说(SemanticEntry):
    """
    #### 原文摘要

**阳盛阴衰**：火多而水涸，火多则气旺，水涸则血虚，血虚则阳火愈炽，阳盛则阴血愈亏。梦见炎炎燎原，勺水难制。调养：滋其真水，以抑阳光。

**阴实阳虚**：元气弱而阴邪盛。经云...
    """
    
    original_text: str = """#### 原文摘要

**阳盛阴衰**：火多而水涸，火多则气旺，水涸则血虚，血虚则阳火愈炽，阳盛则阴血愈亏。梦见炎炎燎原，勺水难制。调养：滋其真水，以抑阳光。

**阴实阳虚**：元气弱而阴邪盛。经云：邪之所凑，其气必虚。正气衰微，阴邪易入，君子道消，小人道长。梦中惟见阴凝魔魅、幽暗不明之事。调养：扶匡心肺之元，保脾胃之气。

**二气俱盛**：阴阳俱盛，二气太过而无偏逊。故梦战斗不休，交睫之顷纷纷乱乱。调养：调其阴阳，和其脏腑，抑其有余，以协中道。

**二气俱虚**：气血衰微，神形怯弱。或老年精元疲敝，或少壮斲丧太多。梦中两相畏缩。调养：补助真元，滋培精髓。"""
    normalized_text_zh: str = """"""
    subject: str = "3 二气盛衰虚实图说"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_3_二气盛衰虚实图说_001_L1",
    )
    version: str = "1.0.0"
