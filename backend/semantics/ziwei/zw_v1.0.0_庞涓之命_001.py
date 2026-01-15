"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699138
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
    semantic_id="zw_v1.0.0_庞涓之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 庞涓之命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府科权禄昌曲魁钺**：多重吉星守身命，主富贵。
  - **左右夹垣**：左辅右彼夹守命宫，增强辅佐之力。
  - **廉贞七杀**：主积富之格，但命犯陀罗有隐患。...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府科权禄昌曲魁钺**：多重吉星守身命，主富贵。
  - **左右夹垣**：左辅右彼夹守命宫，增强辅佐之力。
  - **廉贞七杀**：主积富之格，但命犯陀罗有隐患。
  - **命犯陀罗**：命宫有陀罗星，主潜在危机。
  - **天罗地网**：太岁入天罗、小限在地网，诸凶齐聚。
  - **流羊流陀会并**：流年擎羊陀罗会合身命，主命亡。
  - **阳男水二局**：庞涓命盘的五行局数，水二局主智慧机敏。

- **原文（source_text）**：  
  庞涓之命。阳男水二局。紫府科权禄昌曲魁钺坐守身命，右右夹垣，为富贵之论。廉贞七杀，又为积富之人，命犯陀罗。庚辰太岁入天罗，小限在地网，身命逢流羊、流陀会并，故凶。

- **规范化释义（primary_lang_explained）**：  
  庞涓命属阳男水二局，紫府科权禄昌曲魁钺坐守身命，左右夹垣，主富贵。廉贞七杀主积富，然命犯陀罗。庚辰年太岁入天罗，小限在地网，身命逢流羊流陀会并，诸凶齐聚而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Pang Juan's Yang male Water Second chart has Ziwei‑Tianfu with Academic‑Authority‑Salary, Chang‑Qu, Kui‑Yue guarding Body‑Life, Left‑Right flanking—wealth and honour. Lian Zhen Seven Killings accumulates wealth, but Tuo Luo afflicts Life. Geng‑chen year Tai Sui enters Heaven Net, minor in Earth Net, transiting Blade‑Tuo converge on Body‑Life. Malefics cause death.

- **核心要点**：  
  1. 紫府科权禄昌曲魁钺守身命，主富贵。  
  2. 命犯陀罗，有隐患。  
  3. 天罗地网、流羊流陀会并，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **富贵格局**："紫府科权禄昌曲魁钺坐守身命，左右夹垣，为富贵之论"，庞涓命本主权贵荣耀。
  - **命犯陀罗**："廉贞七杀，又为积富之人，命犯陀罗"，一面积富、一面埋下陀罗隐患。
  - **天罗地网**："庚辰太岁入天罗，小限在地网，身命逢流羊、流陀会并"，天罗地网加流羊流陀会并，为战阵凶亡之应期。
  - **现代应用**：富贵权位配上高风险行业（如军政、金融）时，遇到命犯陀罗叠加天罗地网之年，宜严控冒险决策与出行安全。"""
    normalized_text_zh: str = """"""
    subject: str = "庞涓之命"
    factor_refs: list = ['star_tuoluoming', 'pattern_zuoyoujiayuan', 'pattern_liuyangtuo', 'source_ref', 'rel_pangjuan_001', 'pattern_zifukequanlu', 'rel_pangjuan_002', 'star_tuoluoming', 'rel_pangjuan_003', 'pattern_tianluodiwang', 'evi_pangjuan_001', 'pattern_liuyangtuo', 'rule_tianluoliuyangtuo', 'concept_tuo_luo', 'concept_transiting_blade']
    
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
        l1_anchor="zw_v1.0.0_庞涓之命_001_L1",
    )
    version: str = "1.0.0"
