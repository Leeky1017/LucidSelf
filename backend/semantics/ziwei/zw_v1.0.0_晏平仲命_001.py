"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699117
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
    semantic_id="zw_v1.0.0_晏平仲命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 晏平仲命(SemanticEntry):
    """
    - 分字分词释义：

  - **丹墩贵格**：特定星曜组合的贵格，秋月生为真格。
  - **太阳守命垣**：太阳星守命宫，主光明显贵。
  - **日月争耀**：太阳太阴同时明亮，主文武兼资。
 ...
    """
    
    original_text: str = """- 分字分词释义：

  - **丹墩贵格**：特定星曜组合的贵格，秋月生为真格。
  - **太阳守命垣**：太阳星守命宫，主光明显贵。
  - **日月争耀**：太阳太阴同时明亮，主文武兼资。
  - **科权禄会合**：化科化权化禄同会命宫，主文武双全。
  - **申生人有忌**：申年生人逢寅岁有特定禁忌。
  - **丧门病符天哭**：多重凶星冲照命宫，主疾病丧事。
  - **阳男金四局**：晏平仲命盘的五行局数，金四局主刚断决绝。

- **原文（source_text）**：  
  晏平仲命。阳男金四局。此为丹墀贵格，秋月生者是真格。且太阳守命垣，日月争耀，科权禄会合，文武双全。四十三岁，太岁行寅，大星申生人有忌，小限丧门、病符、天哭冲照，故命亡。

- **规范化释义（primary_lang_explained）**：  
  晏平仲命属阳男金四局，成丹墀贵格（秋月生为真格），太阳守命、日月争耀、科权禄会合，主文武双全。四十三岁太岁行寅，申生人有忌，小限丧门、病符、天哭冲照，诸凶叠加而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Yan Pingzhong's Yang male Metal Fourth chart forms the Cinnabar Terrace Noble pattern (true for autumn‑born). Sun guards Life, Sun‑Moon vie for brilliance, Academic‑Authority‑Salary converge—dual civil and martial talents. At 43 Tai Sui in Yin, Shen natives face taboos. Minor period with Mourning Gate, Illness Talisman, Crying clash. Malefics cause death.

- **核心要点**：  
  1. 丹墀贵格、日月争耀、科权禄会合，主文武双全。  
  2. 申生人于寅岁有忌。  
  3. 丧门、病符、天哭冲照，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **丹墀贵格**："此为丹墀贵格，秋月生者是真格"，晏平仲命主朝廷重臣、文武兼资。
  - **申生忌寅**："四十三岁，太岁行寅，大星申生人有忌"，点出申年生人逢寅岁需严防的禁忌年份。
  - **丧门病符**："小限丧门、病符、天哭冲照"，多重疾病与丧服之星冲命，为命亡信号。
  - **现代应用**：身居高位者在生年忌岁、且丧门病符齐聚之年，应提前做健康体检与权力交接规划，减轻极端风险。"""
    normalized_text_zh: str = """"""
    subject: str = "晏平仲命"
    factor_refs: list = ['pattern_danchigui', 'pattern_riyuezhengyao', 'star_bingfu', 'source_ref', 'rel_yanping_001', 'pattern_danchigui', 'rel_yanping_002', 'taboo_shenshengji', 'rel_yanping_003', 'star_sangmenbingfu', 'evi_yanping_001', 'taboo_shenshengji', 'rule_shenshengji', 'evi_yanping_002', 'star_sangmenbingfu', 'rule_sangmenbingfu', 'concept_cinnabar', 'concept_illness_stars']
    
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
        l1_anchor="zw_v1.0.0_晏平仲命_001_L1",
    )
    version: str = "1.0.0"
