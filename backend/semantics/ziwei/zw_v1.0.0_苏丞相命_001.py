"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699106
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
    semantic_id="zw_v1.0.0_苏丞相命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 苏丞相命(SemanticEntry):
    """
    - 分字分词释义：

  - **日月权禄**：太阳太阴与化权化禄同宫，主极贵。
  - **丑未宫**：日月权禄在丑未宫成格，主方伯之贵。
  - **方伯之贵**：古代方伯为一方诸侯之长，主封疆大...
    """
    
    original_text: str = """- 分字分词释义：

  - **日月权禄**：太阳太阴与化权化禄同宫，主极贵。
  - **丑未宫**：日月权禄在丑未宫成格，主方伯之贵。
  - **方伯之贵**：古代方伯为一方诸侯之长，主封疆大员。
  - **劫空冲守**：地劫天空冲照守命宫，破坏福禄。
  - **福不全美**：劫空冲守使贵格福禄大打折扣。
  - **天罗地网**：大小限太岁皆入天罗地网，为早亡应期。
  - **阴男土五局**：苏丞相命盘的五行局数，土五局主厚重稳健。

- **原文（source_text）**：  
  苏丞相命。阴男土五局。虽曰日月权禄，丑未宫，定是方伯公，左右加会，名誉声扬，只嫌劫空冲守，福不全美，故主三十四岁而亡。大限入地网，小限又入地网，太岁在天罗，故凶。

- **规范化释义（primary_lang_explained）**：  
  苏丞相命属阴男土五局，日月权禄在丑未宫，主方伯之贵，左右加会名誉声扬。然劫空冲守，福禄不全；三十四岁大小限皆入地网，太岁天罗，天罗地网齐聚而早亡。

- **完整对等诠释（secondary_lang_full）**：  
  Prime Minister Su's Yin male Earth Fifth chart has Sun‑Moon with Authority‑Salary in Chou‑Wei—Regional Governor rank. Left‑Right join, spreading fame. Robbery‑Void clash and guard, blessings incomplete. At 34 both periods enter Earth Net, Tai Sui in Heaven Net. Double Nets converge, early death.

- **核心要点**：  
  1. 日月权禄在丑未宫，主方伯之贵。  
  2. 劫空冲守，福禄不全。  
  3. 大小限地网、太岁天罗齐聚，为早亡应期。

- **叙事素材（narrative_snippets）**：
  - **方伯之贵**："日月权禄在丑未宫，左右加会"，苏丞相命主一方封疆、名誉远播。
  - **福不全美**："只嫌劫空冲守，福不全美"，劫空冲守命垣，使富贵之福大打折扣。
  - **天罗地网**："大限入地网，小限又入地网，太岁在天罗"，天罗地网齐聚为早亡应期。
  - **现代应用**：贵格遇劫空与天罗地网时，应提前规划中年前后的健康与仕途风险，切忌恃宠而骄。"""
    normalized_text_zh: str = """"""
    subject: str = "苏丞相命"
    factor_refs: list = ['pattern_riyuequanlu', 'result_fangbo', 'pattern_jiekongchong', 'pattern_tianluodiwang', 'source_ref', 'rel_sucheng_001', 'pattern_riyuequanlu', 'rel_sucheng_002', 'pattern_jiekongchong', 'rel_sucheng_003', 'pattern_tianluodiwang', 'evi_sucheng_001', 'pattern_jiekongchong', 'rule_jiekong_fubuquan', 'evi_sucheng_002', 'pattern_tianluodiwang', 'rule_tianluodiwang_wang', 'concept_robbery_void', 'concept_double_nets']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_苏丞相命_001_L1",
    )
    version: str = "1.0.0"
