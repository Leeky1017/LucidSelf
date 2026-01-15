"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997473
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
    semantic_id="dts_v1.0.0_人有精神_不可以一偏求也_要在损之益之得其中_001",
    book_id="dts",
    engine_id="bazi"
)
class 人有精神不可以一偏求也要在损之益之得其中(SemanticEntry):
    """
    - **原文（source_text）**：
  人有精神，不可以一偏求也，要在损之益之得其中。

- 原注（原文注解）：
  　　五行大率以金水为精气，木火为神气，而土所以实之者也，有神足不见其精，...
    """
    
    original_text: str = """- **原文（source_text）**：
  人有精神，不可以一偏求也，要在损之益之得其中。

- 原注（原文注解）：
  　　五行大率以金水为精气，木火为神气，而土所以实之者也，有神足不见其精，而精自足者，有精足不见其神，而神自足者，有精缺神索而日主孤弱者，有神不足而精有馀者，有精不足而神有馀者，有精神俱缺而气旺者，有精缺而得神以助之者，有神缺而得精以生之者，有精助精而精反泄者，有神助神而神反毙者，皆无气以生也，凡此不可以一偏求之，俱要损益其进退，勿使过兴不及可也。

- 分字分词释义：
  - 精：偏于金水之精气，主收敛、根本、藏养。
  - 神：偏于木火之神气，主外显、意识、活动。
  - 损之益之：对有余者损，对不足者益，以求平衡。
  - 其中：不过不及之中道。

- **规范化释义（primary_lang_explained）**：
  精与神好比“根与花”：金水为精，重在藏养根柢；木火为神，重在表现神采；土则承载二者。命局之妙，不在单求“神旺”或“精足”，而在随局势损其有余、益其不足，使精与神相生相守，气机得其中。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 精神 | Essence and Spirit (Jing-Shen) | 金水为精木火为神 | Metal/Water as Jing, Wood/Fire as Shen | jing_shen | new_candidate |
| 损之益之 | Reduce and Supplement | 损有余益不足 | Reduce excess, supplement deficiency | sun_yi | new_candidate |
| 得其中 | Achieve Balance | 达到中和 | Achieve the middle path | de_qi_zhong | new_candidate |
| 精足 | Sufficient Essence | 金水充盈 | Abundant Metal/Water | jing_zu | new_candidate |
| 神足 | Sufficient Spirit | 木火充盈 | Abundant Wood/Fire | shen_zu | new_candidate |
| 土实 | Solid Earth | 土能承载 | Earth capable of supporting | tu_shi | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Jing-Shen (Essence-Spirit) theory: Jin-Shui is Essence (Jing), Mu-Huo is Spirit (Shen), Earth supports both. Balance via 损 excess and 益 deficiency. Must distinguish types: Jing-Sufficient-Shen-Hidden, Shen-Sufficient-Jing-Hidden, Jing-Deficient-Shen-Weak, etc. The goal is to make Jing and Shen support each other (得其中), avoiding extremes."""
    normalized_text_zh: str = """"""
    subject: str = "人有精神，不可以一偏求也，要在损之益之得其中。"
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
        l1_anchor="dts_v1.0.0_人有精神_不可以一偏求也_要在损之益之得其中_001_L1",
    )
    version: str = "1.0.0"
