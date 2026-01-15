"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997636
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
    semantic_id="dts_v1.0.0_合有宜不宜_合多不为奇_001",
    book_id="dts",
    engine_id="bazi"
)
class 合有宜不宜合多不为奇(SemanticEntry):
    """
    - **原文（source_text）**：
  合有宜不宜，合多不为奇。

- 原注（原文注解）：
  　　喜神有能合助之者，以庚为喜神，得乙合而助之（化金）为宜。凶神有能合而去之者，以甲为凶神，得...
    """
    
    original_text: str = """- **原文（source_text）**：
  合有宜不宜，合多不为奇。

- 原注（原文注解）：
  　　喜神有能合助之者，以庚为喜神，得乙合而助之（化金）为宜。凶神有能合而去之者，以甲为凶神，得己合而去之（化土）为宜。动局有能合而静者，如子午相冲，得丑合而静，为宜。生局有能合而成者，如甲生于亥，得寅合而成，为宜。若助其凶神之合（如己为凶神，而甲合之），或绊其喜神之合（乙为喜神，庚合之），或合成闲神、增凶势，皆不宜。大率多合则不流通，不奋发，虽有秀气，亦不为奇。

- **规范化释义（primary_lang_explained）**：
  合需“助喜去忌、静动成生”，忌“助凶绊喜、繁合滞局”。

- 分字分词释义：
  - 宜合：合以助喜去忌。
  - 不宜之合：助凶、绊喜、徒增闲神。
  - 合多不奇：合繁则滞，不流不奋。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 合多不为奇 | Too Many Combinations | 合多不贵 | Many combinations not noble | heduo_buweiqi | new_candidate |
| 宜不宜 | Appropriate or Not | 宜合与不宜合 | Suitable and unsuitable | yi_buyi | new_candidate |
| 助喜 | Assist Happy God | 助用神 | Help the Useful God | zhuxi | new_candidate |
| 去忌 | Remove Malicious God | 去忌神 | Remove the Annoying God | quji | new_candidate |
| 绊喜 | Tangle Happy God | 羁绊喜神 | Restrain the Happy God | banxi | new_candidate |
| 助凶 | Assist Malicious | 助纣为虐 | Help the bad element | zhuxiong | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  He-Patterns: "Appropriate Combination" (Yi-He) helps the Happy God (Zhu-Xi) or removes the Malicious God (Qu-Ji). "Inappropriate Combination" (Bu-Yi-He) aids the Malicious or tangles the Happy. "Too Many Combinations" (He-Duo) cause stagnation (Bu-Wei-Qi). Quality over quantity."""
    normalized_text_zh: str = """"""
    subject: str = "合有宜不宜，合多不为奇。"
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
        l1_anchor="dts_v1.0.0_合有宜不宜_合多不为奇_001_L1",
    )
    version: str = "1.0.0"
