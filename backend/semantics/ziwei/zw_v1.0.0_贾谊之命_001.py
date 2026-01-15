"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699330
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
    semantic_id="zw_v1.0.0_贾谊之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 贾谊之命(SemanticEntry):
    """
    - 分字分词释义：

  - **文星暗拱**：文星从暗处拱照命宫，主年少登科。
  - **天机天钺正照**：天机天钺直接照命，为吉兆。
  - **命原犯擎羊**：命宫本带擎羊，为一生暗伏的危险因...
    """
    
    original_text: str = """- 分字分词释义：

  - **文星暗拱**：文星从暗处拱照命宫，主年少登科。
  - **天机天钺正照**：天机天钺直接照命，为吉兆。
  - **命原犯擎羊**：命宫本带擎羊，为一生暗伏的危险因子。
  - **天罗地网**：小限天罗、大限地网，为困境之象。
  - **流羊流陀三方合命**：流年擎羊陀罗三方会合命垣，主凶亡。
  - **二十八岁夭亡**：贾谊英年早逝的命理应期。
  - **阴男金四局**：贾谊命盘的五行局数，金四局主才华锐利。

- **原文（source_text）**：  
  贾谊之命。阴男金四局。文星暗拱，年少登科，天机、天钺正照，以为吉兆。小限到天罗，大限到地网，太岁、天伤夹地，流羊、流陀三方合命垣，且命原犯鸄羊，故夭亡于二十八岁。

- **规范化释义（primary_lang_explained）**：  
  贾谊命属阴男金四局，文星暗拱，年少登科，天机天钺正照为吉。然小限天罗、大限地网，太岁天伤夹地，流羊流陀三方合命垣，命原犯擎羊，故二十八岁夭亡。

- **完整对等诠释（secondary_lang_full）**：  
  Jia Yi's Yin male Metal Fourth chart has Literary Star secretly flanking—young success in exams. Tianji‑Tianyue directly illuminate, auspicious. Minor at Heaven Net, major at Earth Net; Tai Sui‑Wound flank Earth; transiting Blade‑Tuo triplicity converge on Life; Life originally afflicted by Blade. Death at 28.

- **核心要点**：  
  1. 文星暗拱，年少登科。  
  2. 命原犯擎羊，有隐患。  
  3. 天罗地网、流羊流陀三方合命，为二十八夭亡应期。

- **叙事素材（narrative_snippets）**：
  - **少壮登科**："文星暗拱，年少登科，天机、天钺正照，以为吉兆"，贾谊命主少年得志、科名早成。
  - **命犯擎羊**："且命原犯鸄羊"，命宫本带擎羊，为一生暗伏的危险因子。
  - **天罗地网**："小限到天罗，大限到地网，太岁、天伤夹地，流羊、流陀三方合命垣"，天罗地网配流羊流陀，为二十八岁夭亡应期。
  - **现代应用**：天资出众、早成之人，在命犯擎羊又遇天罗地网叠加的年头，应避免情绪激烈的仕途/学术博弈，防止英年早逝。"""
    normalized_text_zh: str = """"""
    subject: str = "贾谊之命"
    factor_refs: list = ['pattern_wenxinganggong', 'pattern_tianluodiwang', 'pattern_mingfanqingyang', 'source_ref', 'rel_jiayi_001', 'pattern_wenxinganggong', 'rel_jiayi_002', 'pattern_mingfanqingyang', 'rel_jiayi_003', 'pattern_tianluodiwang', 'evi_jiayi_001', 'pattern_tianluodiwang', 'rule_tianluo_yaowang', 'concept_literary_flank', 'concept_heaven_earth_net']
    
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
        l1_anchor="zw_v1.0.0_贾谊之命_001_L1",
    )
    version: str = "1.0.0"
