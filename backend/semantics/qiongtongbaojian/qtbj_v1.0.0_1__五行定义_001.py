"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619628
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
    semantic_id="qtbj_v1.0.0_1__五行定义_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1五行定义(SemanticEntry):
    """
    - **原文（source_text）**：
  五行者，本乎天地之间而不穷者也，故谓之行。

- **分字分词释义**：
  - **五行**：五（数目五）/ 金木水火土五种基本气机 / 宇宙本体构...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行者，本乎天地之间而不穷者也，故谓之行。

- **分字分词释义**：
  - **五行**：五（数目五）/ 金木水火土五种基本气机 / 宇宙本体构成
  - **本**：根本、根源 / 发端之处 / 强调先天来源
  - **天地之间**：天与地之间的空间 / 宇宙万物所存在的场域 / 五行活动的舞台
  - **不穷**：不会穷尽、没有尽头 / 循环往复、生生不息 / 五行的永恒性特征
  - **行**：行走、运行 / 动态流转而非静态物质 / 强调"动"的本质

- **规范化释义（primary_lang_explained）**：
  所谓“五行”，是根源于天地之间、运行不息的五种基本气机。因为它们循环往复、永不穷尽，所以称为“行”（行动、运行）。

- **完整对等诠释（secondary_lang_full）**：
  The "Five Elements" (Wuxing) are the five fundamental dynamic energies rooted between Heaven and Earth that operate ceaselessly. They are called "Walking/Moving" (Xing) because they cycle continuously without exhaustion.

- **核心要点**：
  - 五行是“动态气机”而非静态物质。
  - 根本属性是“不穷”（生生不息）。
  - 存在场域为“天地之间”。

- **详细解说**：
  本条确立了全书的本体论基础。五行不是五个元素，而是五种运动方式。它们充塞于天地之间，构成了一个永恒流转的能量系统。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_001]` `[trigger: 五行概念]` `[factor_trigger: wuxing_dynamic_system]` `[role: 主干]` 五行是动态气机而非静态物质，循环往复、永不穷尽。 → 《穷通宝鉴·五行总论》#1.1
  - `[ns_qttbj_002]` `[trigger: 五行概念]` `[factor_trigger: wuxing_dynamic_system]` `[role: 主干依赖]` 五行根源于天地之间，构成一个永恒流转的能量系统。 → 《穷通宝鉴·五行总论》#1.1
  - `[ns_qttbj_003]` `[trigger: 五行概念]` `[factor_trigger: wuxing_dynamic_system AND dynamic_movement]` `[role: 主干依赖]` 因其生生不息、永不穷尽，故称之为"行"。 → 《穷通宝鉴·五行总论》#1.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 五行定义"
    factor_refs: list = ['wuxing_system', 'wuxing_moving_phase', 'wuxing_inexhaustible_cycle']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__五行定义_001_L1",
    )
    version: str = "1.0.0"
