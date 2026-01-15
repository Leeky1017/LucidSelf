"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699339
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
    semantic_id="zw_v1.0.0_马周之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 马周之命(SemanticEntry):
    """
    - 分字分词释义：

  - **巨机居卯**：巨门天机同在卯宫，主位至公卿。
  - **限步逆行**：限运逆行为美兆，主仕途顺遂。
  - **未宫擎羊**：未宫有擎羊，为寿元的硬伤。
  - *...
    """
    
    original_text: str = """- 分字分词释义：

  - **巨机居卯**：巨门天机同在卯宫，主位至公卿。
  - **限步逆行**：限运逆行为美兆，主仕途顺遂。
  - **未宫擎羊**：未宫有擎羊，为寿元的硬伤。
  - **大限天使**：大限入天使宫位，主凶险。
  - **倒限**：限运不顺主伤寿，为运势逆转的信号。
  - **擎羊冲会**：擎羊冲照加会，主寿命骤折。
  - **阴男火六局**：马周命盘的五行局数，火六局主热情谋略。

- **原文（source_text）**：  
  马周之命。阴男火六局。巨机居卯，位至公卿，限步逆行，以为美兆。未宫见有擎羊，故主寿难长久。大限入于天使，小限擎羊冲会，故作倒限伤寿。

- **规范化释义（primary_lang_explained）**：  
  马周命属阴男火六局，巨机居卯，位至公卿，限步逆行为美兆。然未宫有擎羊，寿难长久。大限入天使，小限擎羊冲会，故作倒限伤寿。

- **完整对等诠释（secondary_lang_full）**：  
  Ma Zhou's Yin male Fire Sixth chart has Jumen‑Tianji at Mao—rank reaching Duke. Periods reverse, auspicious sign. But Blade at Wei, short lifespan. Major enters Envoy, minor Blade clashes. Inverted period harms lifespan.

- **核心要点**：  
  1. 巨机居卯，位至公卿。  
  2. 未宫擎羊，寿难长久。  
  3. 大限天使、小限擎羊冲会，为倒限伤寿应期。

- **叙事素材（narrative_snippets）**：
  - **公卿之贵**："巨机居卯，位至公卿，限步逆行，以为美兆"，马周命主以谋臣之姿位列公卿。
  - **未宫擎羊**："未宫见有擎羊，故主寿难长久"，未宫擎羊成为寿元上的硬伤。
  - **倒限伤寿**："大限入于天使，小限擎羊冲会，故作倒限伤寿"，倒限配擎羊冲会，为寿命骤折的标记年份。
  - **现代应用**：对高位文臣而言，遇到倒限配擎羊的阶段，宜主动减负与交班，避免在高压公务中损害健康。"""
    normalized_text_zh: str = """"""
    subject: str = "马周之命"
    factor_refs: list = ['pattern_jujijumao', 'pattern_daoxian', 'pattern_qingyangchonghui', 'source_ref', 'rel_mazhou_001', 'pattern_jujijumao', 'rel_mazhou_002', 'pattern_weigongqingyang', 'rel_mazhou_003', 'pattern_daoxian', 'evi_mazhou_001', 'pattern_daoxian', 'rule_daoxian_shangshou', 'concept_juji_mao', 'concept_inverted_period']
    
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
        l1_anchor="zw_v1.0.0_马周之命_001_L1",
    )
    version: str = "1.0.0"
