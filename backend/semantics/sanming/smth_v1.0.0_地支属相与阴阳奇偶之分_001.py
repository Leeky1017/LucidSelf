"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042710
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
    semantic_id="smth_v1.0.0_地支属相与阴阳奇偶之分_001",
    book_id="sanming",
    engine_id="bazi"
)
class 地支属相与阴阳奇偶之分(SemanticEntry):
    """
    - **原文（source_text）**：
  或问：地支有属相，而天干则无者，何也？答曰：天干动而无相，地支静而有相。盖轻清者天也，重浊者地也，重浊之中，乃有物焉。故子属鼠，丑属牛，寅属虎，卯属兔...
    """
    
    original_text: str = """- **原文（source_text）**：
  或问：地支有属相，而天干则无者，何也？答曰：天干动而无相，地支静而有相。盖轻清者天也，重浊者地也，重浊之中，乃有物焉。故子属鼠，丑属牛，寅属虎，卯属兔，辰属龙，巳属蛇，午属马，未属羊，申属猴，酉属鸡，戌属犬，亥属猪。此十二属相，亦有奇偶之分、盛衰之用：奇者鼠、虎、龙、马、猴、犬，一则属阳，六兽之足皆单；偶者牛、兔、蛇、羊、鸡、猪，二则属阴，六兽之足皆双。唯蛇无足，又何取义？盖巳在月，乃纯阳之月；在时，乃春阳之时：数则偶，而时则阳，故用蛇以象之。蛇乃阴物，不用其足而象巳著疑，亦讳言乎阴之意尔，况亦有双头者。

- **分字分词释义**：
  - **天干动而无相**：干主天之轻清之气，偏向抽象、无形，不以具象动物比拟。
  - **地支静而有相**：支主地之重浊之气，可见可触，故以十二动物取象。
  - **奇偶之分**：以足之单双对应阴阳：足单者属阳，足双者属阴，用以强化支之阴阳属性。
  - **蛇无足而象巳**：蛇虽无足而归于偶数一类，借其阴物之性，专为巳月、巳时之阳气作对比与讳言之用。
- **规范化释义（primary_lang_explained）**：
  本段先解释为何只有地支有属相：天干属天，动而轻清，难以用具体形象来界定；地支属地，重而浊，承载万物，因此以十二种常见动物来比拟。作者进一步指出，十二属相本身也按照阴阳划分：足数为单的六兽属阳，对应阳支；足为双的六兽属阴，对应阴支。巳蛇无足却用以象巳，是利用其为阴物的特性，既暗合巳月春阳之时，又以「不用其足」讳言阴性之不便直说，显示古人象数取义的精细之处。

- **完整对等诠释（secondary_lang_full）**：
  This passage first answers why only the Earthly Branches, and not the Heavenly Stems, are assigned animals. The Stems belong to heaven: light, mobile and abstract, so they are harder to capture with concrete images. The Branches belong to earth: heavy, turbid and bearing all manifest things, so it is natural to picture them through twelve familiar creatures. The author then notes that the animals themselves are organised by yin and yang: those with an odd number of feet (counting pairs) are classed as yang and match yang branches; those with an even number of feet are yin and match yin branches. The one apparent exception, the footless snake assigned to Si, is in fact deliberate: the snake is a yin creature used to stand opposite the strongly yang month and hour of Si, and by "not using its feet" the text hints at yin qualities without naming them too bluntly. Altogether, the system is shown as a carefully crafted memory and symbolism aid rather than a random set of animal labels."""
    normalized_text_zh: str = """"""
    subject: str = "地支属相与阴阳奇偶之分"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'zodiac_yinyang_class', 'dizhi_to_zodiac_mapping', 'zodiac_temperament_hint', 'zodiac_weight_limit', 'source_ref', 'rel_smth_sxf_001', 'dizhi', 'rel_smth_sxf_002', 'jiou_zushu', 'rel_smth_sxf_003', 'shuxiang', 'evi_smth_sxf_001', 'dizhi_shuxiang', 'rule_sxf', 'concept_symbolic_layer']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_地支属相与阴阳奇偶之分_001_L1",
    )
    version: str = "1.0.0"
