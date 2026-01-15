"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997511
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
    semantic_id="dts_v1.0.0_天道有寒暖_发育万物_人道得之_不可过也_001",
    book_id="dts",
    engine_id="bazi"
)
class 天道有寒暖发育万物人道得之不可过也(SemanticEntry):
    """
    - **原文（source_text）**：
  天道有寒暖，发育万物，人道得之，不可过也。

- 原注（原文注解）：
  　　阴支为寒，阳支为暖，金水为寒，木火为暖，得气之寒，遇暖而发，得气之暖，遇...
    """
    
    original_text: str = """- **原文（source_text）**：
  天道有寒暖，发育万物，人道得之，不可过也。

- 原注（原文注解）：
  　　阴支为寒，阳支为暖，金水为寒，木火为暖，得气之寒，遇暖而发，得气之暖，遇寒而成，寒之甚，暖之至，内有一二成象，必无好处，若五行阳遇子月，则一阳后万物怀胎，阳乘阳位，可东可西，阴逄午月，则一阴后，万物收藏，阴乘阴位，可南可北。

- 分字分词释义：
  - 寒暖：偏于气候、温度之象，命中以阴阳支、金水木火之偏寒偏暖体现；
  - 不可过：不可偏激到极端，否则虽成象而非佳象。

- **规范化释义（primary_lang_explained）**：
  寒与暖是天道之纲。寒极需暖、暖极需寒，以成均衡；过则不吉。命中若寒而得暖，则发生；若暖而得寒，则成就；若寒暖过极而又失其对冲，则虽成一二怪象，终非正道之福。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 寒暖 | Cold-Warmth (Han-Nuan) | 金水寒木火暖 | Metal/Water Cold Wood/Fire Warm | hannuan | existing |
| 发育万物 | Nurture All Things | 寒暖调和 | Balanced climate nurtures | fayu_wanwu | new_candidate |
| 不可过 | Cannot be Excessive | 不可偏枯 | Cannot be unbalanced | bukeguo | new_candidate |
| 得气之寒 | Cold Qi | 金水之气 | Metal/Water Qi | deqi_han | new_candidate |
| 得气之暖 | Warm Qi | 木火之气 | Wood/Fire Qi | deqi_nuan | new_candidate |
| 反佐 | Reverse Assistance | 寒极用暖暖极用寒 | Opposite to balance extreme | fanzuo | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Han-Nuan (Cold-Warm) theory: Yin/Metal/Water is Cold, Yang/Wood/Fire is Warm. "Cannot be excessive" (不可过) means balance is key. Cold needs Warmth to sprout (发), Warmth needs Cold to complete (成). Extreme Cold or Extreme Warmth without balance might form a unique pattern but is rarely auspicious."""
    normalized_text_zh: str = """"""
    subject: str = "天道有寒暖，发育万物，人道得之，不可过也。"
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
        l1_anchor="dts_v1.0.0_天道有寒暖_发育万物_人道得之_不可过也_001_L1",
    )
    version: str = "1.0.0"
