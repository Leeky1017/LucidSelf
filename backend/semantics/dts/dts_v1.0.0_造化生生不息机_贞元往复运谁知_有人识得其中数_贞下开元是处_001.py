"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997854
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
    semantic_id="dts_v1.0.0_造化生生不息机_贞元往复运谁知_有人识得其中数_贞下开元是处_001",
    book_id="dts",
    engine_id="bazi"
)
class 造化生生不息机贞元往复运谁知有人识得其中数贞下开元是处(SemanticEntry):
    """
    - **原文（source_text）**：
  造化生生不息机，贞元往复运谁知，有人识得其中数，贞下开元是处宜。

- 原注（原文注解）：
  　　三元皆有贞元。如以八字论，则年为元，月为亨，日为利...
    """
    
    original_text: str = """- **原文（source_text）**：
  造化生生不息机，贞元往复运谁知，有人识得其中数，贞下开元是处宜。

- 原注（原文注解）：
  　　三元皆有贞元。如以八字论，则年为元，月为亨，日为利，时为贞。年月吉者前半世吉；日时吉者后半世吉。以大运论，初十五年为元，次十五年为亨，中十五年为利，后十五年为贞……运数一定不易，故“贞下起元”，生生不息。

- **规范化释义（primary_lang_explained）**：
  贞为收束转折之机，能识“贞下开元”，则前后半世各得其宜，家运亦可延世。

- 分字分词释义：
  - 贞：收束、定向之机。
  - 贞下开元：旧运终而新运始，循环不息。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 贞元 | Zhen-Yuan (Cycle Ends/Starts) | 贞下起元 | End and new beginning | zhenyuan_cycle_stage | existing |
| 造化 | Creation/Nature (Zao-Hua) | 天地造化 | Nature's creation | creation_mechanism | new_candidate |
| 生生不息 | Ceaseless Creation | 循环往复 | Unending cycle | cycle_continuity | new_candidate |
| 往复 | Cyclical Return | 来回循环 | Cycle back and forth | cycle_pattern | new_candidate |
| 数 | Number/Fate (Shu) | 定数气数 | Fate/Number | fate_number | new_candidate |
| 贞下开元 | End Starts New Beginning | 否极泰来 | End leads to new start | zhenyuan_transition_point | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Zhen-Yuan (Cycle Ends/Starts) theory: "Creation Without Ceasing" (Sheng-Sheng-Bu-Xi). Zhen-Yuan cycles (Year=Origin/Yuan, Month=Heng, Day=Li, Hour=Zhen; or 15-year luck cycles). "Zhen leads to Yuan" (Zhen-Xia-Qi-Yuan) means the end begins a new cycle. Knowing the numbers (Shu) allows predicting proper outcomes."""
    normalized_text_zh: str = """"""
    subject: str = "造化生生不息机，贞元往复运谁知，有人识得其中数，贞下开元是处宜。"
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
        l1_anchor="dts_v1.0.0_造化生生不息机_贞元往复运谁知_有人识得其中数_贞下开元是处_001_L1",
    )
    version: str = "1.0.0"
