"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997518
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
    semantic_id="dts_v1.0.0_地道有燥湿_生成品汇_人道得之_不可偏也_001",
    book_id="dts",
    engine_id="bazi"
)
class 地道有燥湿生成品汇人道得之不可偏也(SemanticEntry):
    """
    - **原文（source_text）**：
  地道有燥湿，生成品汇，人道得之，不可偏也。

- 原注（原文注解）：
  　　过于湿者，滞而无成，过于燥者，烈而有祸，水有金生，遇寒土而愈湿，火有木生...
    """
    
    original_text: str = """- **原文（source_text）**：
  地道有燥湿，生成品汇，人道得之，不可偏也。

- 原注（原文注解）：
  　　过于湿者，滞而无成，过于燥者，烈而有祸，水有金生，遇寒土而愈湿，火有木生，遇暖土而愈燥，皆偏枯也，木火而成其燥者，言木火伤官要湿也，土水而成其湿者，言金水伤官要燥也，间有火土而宜燥者，用土而后用火，金燥而宜湿者，用金而后用水。

- 分字分词释义：
  - 燥湿：偏干偏湿之地气；
  - 偏枯：偏而不平之象，虽有其用而多生弊病；
  - 主剂：先行调整的大药味；
  - 佐使：辅佐主剂，使之成方。

- **规范化释义（primary_lang_explained）**：
  燥湿为地气之主。燥极要润，湿极要燥。若水多遇寒土，则愈湿；火多遇暖土，则愈燥，皆为偏枯。故用神之配伍，需先立主剂（如先土后火、先金后水），再定佐使，使燥湿得其中，不致偏激。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 燥湿 | Dryness-Wetness (Zao-Shi) | 燥土与湿土 | Dry Earth and Wet Earth | zaoshi | existing |
| 偏枯 | Withered Bias (Pian-Ku) | 偏颇有病 | Biased and diseased | pianku | new_candidate |
| 滞而无成 | Stagnant without Success | 湿极而滞 | Stagnant from extreme wet | zhi_wucheng | new_candidate |
| 烈而有祸 | Violent with Disaster | 燥极而烈 | Violent from extreme dry | lie_youhuo | new_candidate |
| 主剂 | Main Agent | 调候主药 | Main adjusting element | zhuji | new_candidate |
| 佐使 | Assistant | 辅助之神 | Assisting element | zuoshi | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Zao-Shi (Dry-Wet) theory: Earth dictates Dryness/Wetness. Wet Earth (Shi-Tu) makes Water wetter; Warm Earth (Nuan-Tu) makes Fire drier. "Cannot be biased" (不可偏) means avoid Pian-Ku (withering bias). Use "Main Agent" (e.g. Earth/Metal) and "Assistant" (e.g. Fire/Water) sequence to adjust."""
    normalized_text_zh: str = """"""
    subject: str = "地道有燥湿，生成品汇，人道得之，不可偏也。"
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
        l1_anchor="dts_v1.0.0_地道有燥湿_生成品汇_人道得之_不可偏也_001_L1",
    )
    version: str = "1.0.0"
