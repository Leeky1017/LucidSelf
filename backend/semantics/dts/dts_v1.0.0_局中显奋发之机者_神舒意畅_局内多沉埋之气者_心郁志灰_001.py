"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997602
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
    semantic_id="dts_v1.0.0_局中显奋发之机者_神舒意畅_局内多沉埋之气者_心郁志灰_001",
    book_id="dts",
    engine_id="bazi"
)
class 局中显奋发之机者神舒意畅局内多沉埋之气者心郁志灰(SemanticEntry):
    """
    - **原文（source_text）**：
  局中显奋发之机者，神舒意畅；局内多沉埋之气者，心郁志灰。

- 原注（原文注解）：
  　　阳明用事，用神得力，天地交泰，神显精通，大都奋发。阴晦用事...
    """
    
    original_text: str = """- **原文（source_text）**：
  局中显奋发之机者，神舒意畅；局内多沉埋之气者，心郁志灰。

- 原注（原文注解）：
  　　阳明用事，用神得力，天地交泰，神显精通，大都奋发。阴晦用事，情多私恋，主弱臣强，神暗精泄，大抵困郁。纯阳之势，身旺而财官旺者必发；纯阴之局，身弱而官煞多者必困。

- **规范化释义（primary_lang_explained）**：
  看“奋”与“郁”，在于“阳明/阴晦、用神得力与否、纯阳/纯阴之偏”。

- 分字分词释义：
  - 奋发：旺而上行、流通而显。
  - 沉埋：气闭于下、无以透达。
  - 神舒意畅：神气舒展、意志通达。
  - 心郁志灰：心志抑郁、锐气消弭。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 奋郁 | Rousing-Depressed (Fen-Yu) | 奋发与郁结 | Rousing and stagnation | fenyu | existing |
| 神舒意畅 | Spirit Comfortable | 精神舒展 | Spiritually free | shenshu_yichang | new_candidate |
| 心郁志灰 | Heart Depressed Will Ash | 意志消沉 | Depressed and discouraged | xinyu_zhihui | new_candidate |
| 沉埋之气 | Buried Qi | 气机不通 | Qi blocked underground | chenmai_zhiqi | new_candidate |
| 阳明 | Yang Brightness | 阳气显露 | Yang energy visible | yangming | new_candidate |
| 阴晦 | Yin Darkness | 阴气晦暗 | Yin energy obscure | yinhui | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Fen-Yu (Rousing-Depressed) theory: "Rousing" (Fen) means spirit is comfortable and free (Shen-Shu Yi-Chang). "Depressed" (Yu) means Qi is buried (Chen-Mai) and will is ash (Xin-Yu Zhi-Hui). Yang-Bright (Yang-Ming) and Empowered Use God lead to Fen. Yin-Dark (Yin-Hui) and buried Qi lead to Yu."""
    normalized_text_zh: str = """"""
    subject: str = "局中显奋发之机者，神舒意畅，局内多沉埋之气者，心郁志灰。"
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
        l1_anchor="dts_v1.0.0_局中显奋发之机者_神舒意畅_局内多沉埋之气者_心郁志灰_001_L1",
    )
    version: str = "1.0.0"
