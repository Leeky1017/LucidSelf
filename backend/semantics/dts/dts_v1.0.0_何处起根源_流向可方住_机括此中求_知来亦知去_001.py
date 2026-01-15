"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997543
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
    semantic_id="dts_v1.0.0_何处起根源_流向可方住_机括此中求_知来亦知去_001",
    book_id="dts",
    engine_id="bazi"
)
class 何处起根源流向可方住机括此中求知来亦知去(SemanticEntry):
    """
    - **原文（source_text）**：
  何处起根源，流向可方住，机括此中求，知来亦知去。

- 原注（原文注解）（节要）：
  　　不必论当令不当令，以取最多旺，可为全局祖者宗为源头，看此源...
    """
    
    original_text: str = """- **原文（source_text）**：
  何处起根源，流向可方住，机括此中求，知来亦知去。

- 原注（原文注解）（节要）：
  　　不必论当令不当令，以取最多旺，可为全局祖者宗为源头，看此源头，流到何方，流去之处，若是所喜之神，即在此住了为妙……（举例略）。

- 分字分词释义：
  - 根源：全局之祖宗之位，可为旺气之始发；
  - 流向：气机运行之方向与归宿；
  - 住：气行至此而安顿不再迁移之处；
  - 机括：关键转折之处。

- **规范化释义（primary_lang_explained）**：
  源流之道，在于先找出全局起点，再追踪其流向与落点：从何处起根、向何处流、终在何处住。如果起点、流向与落点皆为所喜之神，则为善局；若源喜而流、住皆忌，则为“好头坏尾”；反之亦然。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 源流 | Source-Flow (Yuan-Liu) | 气之起止 | Origin and destination of Qi | yuanliu | existing |
| 根源 | Source Root | 气之发端 | Start of Qi | genyuan | new_candidate |
| 流向 | Flow Direction | 气之路径 | Path of Qi | liuxiang | new_candidate |
| 住 | Stay (Zhu) | 气之归宿 | Where Qi stops | zhu | new_candidate |
| 机括 | Key Mechanism | 转折关键 | Key turning point | jikuo | new_candidate |
| 知来知去 | Know Past and Future | 洞悉因果 | Understand cause and effect | zhilai_zhiqu | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Yuan-Liu (Source-Flow) theory: Find where the Qi starts (Source/Root), where it flows (Flow), and where it stops (Stay/Zhu). The Source is the strongest/most organized element, not necessarily the Month Command. The Flow path and the Final Stay determine if the chart is auspicious (stops at Favored God) or not (stops at Disfavored God)."""
    normalized_text_zh: str = """"""
    subject: str = "何处起根源，流向可方住，机括此中求，知来亦知去。"
    factor_refs: list = []
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_何处起根源_流向可方住_机括此中求_知来亦知去_001_L1",
    )
    version: str = "1.0.0"
