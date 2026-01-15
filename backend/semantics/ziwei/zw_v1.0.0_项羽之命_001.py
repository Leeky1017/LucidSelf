"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699195
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
    semantic_id="zw_v1.0.0_项羽之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 项羽之命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄加会**：化权化禄同会命宫，主极富贵。
  - **禄存守命垣**：禄存星坐守命宫，主财禄。
  - **吉处藏凶**：贵格中对宫忌星冲破，荣耀背后潜伏覆灭之机。...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄加会**：化权化禄同会命宫，主极富贵。
  - **禄存守命垣**：禄存星坐守命宫，主财禄。
  - **吉处藏凶**：贵格中对宫忌星冲破，荣耀背后潜伏覆灭之机。
  - **大小二限相冲**：大限与小限宫位相冲，主凶亡。
  - **地劫天空**：大限逢地劫、小限逢天空，空劫齐聚。
  - **逗死于乌江**：项羽乌江自刐的历史事件，为命亡应期。
  - **阴男水二局**：项羽命盘的五行局数，水二局主智慧机敏。

- **原文（source_text）**：  
  项羽之命。阴男水二局。权禄加会，当至极富贵，禄存守命垣，被对宫忌星冲破，为吉处藏凶。三十二岁，大限到寅，地劫相合，小限到申，天空值守，大小二限相冲，故逼死于乌江。

- **规范化释义（primary_lang_explained）**：  
  项羽命属阴男水二局，权禄加会主极富贵，禄存守命垣。然对宫忌星冲破，吉处藏凶。三十二岁大限到寅逢地劫，小限到申逢天空，大小二限相冲，遂逼死于乌江。

- **完整对等诠释（secondary_lang_full）**：  
  Xiang Yu's Yin male Water Second chart has Authority‑Salary converging—extreme wealth and honour. Salary Keeper guards Life, but opposite taboo star clashes, hiding danger in auspice. At 32 major at Yin meets Di Jie, minor at Shen meets Tian Kong. Major‑minor clash, forced death at Wujiang.

- **核心要点**：  
  1. 权禄加会、禄存守命，主极富贵。  
  2. 对宫忌星冲破，吉处藏凶。  
  3. 大小二限相冲、劫空相合，为乌江自刎应期。

- **叙事素材（narrative_snippets）**：
  - **极贵之命**："权禄加会，当至极富贵，禄存守命垣"，项羽命主一生位极人臣、富贵无双。
  - **吉处藏凶**："被对宫忌星冲破，为吉处藏凶"，对宫忌星冲破禄存，使荣耀背后潜伏覆灭之机。
  - **乌江之劫**："三十二岁，大限到寅，地劫相合，小限到申，天空值守，大小二限相冲，故逼死于乌江"，大小限相冲配合空劫，为乌江自刎的命理应期。
  - **现代应用**：极富极贵者在大小限相冲又逢空劫之年，应格外提防政治与职场清算，谨防因一役败而前功尽弃。"""
    normalized_text_zh: str = """"""
    subject: str = "项羽之命"
    factor_refs: list = ['pattern_jichucangxiong', 'pattern_daxiaoxianchong', 'pattern_kongjie', 'source_ref', 'rel_xiangyu_001', 'pattern_quanlu_lucun', 'rel_xiangyu_002', 'pattern_jichucangxiong', 'rel_xiangyu_003', 'pattern_daxiaoxianchong', 'evi_xiangyu_001', 'pattern_daxiaoxianchong', 'rule_daxiaoxianchong_kongjie', 'concept_hidden_danger', 'concept_period_clash']
    
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
        l1_anchor="zw_v1.0.0_项羽之命_001_L1",
    )
    version: str = "1.0.0"
