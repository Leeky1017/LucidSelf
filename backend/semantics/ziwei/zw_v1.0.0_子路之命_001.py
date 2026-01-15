"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.698971
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
    semantic_id="zw_v1.0.0_子路之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 子路之命(SemanticEntry):
    """
    - 分字分词释义：

  - **府相朝垣格**：天府天相拱照命宫的贵格，本主贤士之命。
  - **廉贞将军**：廉贞星坐命，主性情刚烈勇猛。
  - **贪狼忌星拱命**：贪狼化忌从对宫拱照命宫，...
    """
    
    original_text: str = """- 分字分词释义：

  - **府相朝垣格**：天府天相拱照命宫的贵格，本主贤士之命。
  - **廉贞将军**：廉贞星坐命，主性情刚烈勇猛。
  - **贪狼忌星拱命**：贪狼化忌从对宫拱照命宫，凶象暗伏。
  - **孛悲之难**：子路死于卫国孔悲之乱的历史事件，应验命中凶亡之象。
  - **紫微诸吉星拱合**：紫微等吉星会合命宫，本为显达贵格。
  - **凶亡**：非正常死亡，此命因凶星暗拱而死于非命。
  - **阴男木三局**：紫微斗数命盘的五行局数，木三局主生发进取。

- **原文（source_text）**：  
  子路之命。阴男木三局。此为府相朝垣格，且紫微诸吉星拱合，所以为贤士。但命坐廉贞将军，故主勇猛。更对垣遇贪狼忌星拱命，故主凶亡，果宛孔悝之难。

- **规范化释义（primary_lang_explained）**：  
  子路命属阴男木三局，命宫成府相朝垣格局，紫微等诸吉星拱合，本主贤士之命。然命宫坐廉贞将军星，性情刚烈勇猛；对宫又有贪狼化忌拱照命宫，凶象暗伏。最终果然应于孔悝之难，死于非命。此例说明：格局虽贵，若有凶星暗拱，仍主凶亡。

- **完整对等诠释（secondary_lang_full）**：  
  Zi Lu's chart belongs to a Yin male of Wood Third Configuration. The Life palace forms the "Fu Xiang Facing Court" pattern, with Ziwei and other auspicious stars converging—a classic sign of a worthy gentleman. However, the Life palace is occupied by the general star Lian Zhen, indicating a fierce and valiant temperament. Furthermore, the opposite palace has Tan Lang in taboo transformation flanking the Life palace, embedding hidden violence. In the end, Zi Lu met a violent death during the incident at Kong Kui's household, fulfilling the chart's ominous warning. This case illustrates that even a noble pattern can lead to violent demise if malefic stars secretly flank the chart.

- **核心要点**：  
  1. 府相朝垣、紫微拱合为贤士格局。  
  2. 廉贞坐命主勇猛刚烈，贪狼化忌拱照主凶亡。  
  3. 格局贵而凶星暗拱，仍主非命之终。

- **叙事素材（narrative_snippets）**：
  - **贤士格局**："府相朝垣，紫微诸吉星拱合"，子路命本主贤士。
  - **廉贞将军**："命坐廉贞将军，故主勇猛"，廉贞坐命主刚烈性情。
  - **凶亡之应**："贪狼忌星拱命，故主凶亡，果宛孔悝之难"，凶星暗拱终致非命。
  - **现代应用**：格局贵不等于安全——凶星暗拱可导致凶险，需综合评估隐藏风险。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j6_008]` `[trigger: 府相朝垣格]` `[factor_trigger: geju_fuxiangchaoyuan]` `[role: 条件分支]` 府相朝垣格为天府天相朝拱命宫的贵格。 → 《卷六》子路命
  - `[ns_zwds_j6_009]` `[trigger: 廉贞坐命]` `[factor_trigger: star_lianzhen AND palace_ming]` `[role: 条件分支]` 廉贞坐命主性情刚烈勇猛。 → 《卷六》"命坐廉贞将军"
  - `[ns_zwds_j6_010]` `[trigger: 贪狼化忌拱命]` `[factor_trigger: star_tanlang AND hua_ji AND gongzhao]` `[role: 条件分支]` 贪狼化忌拱命为凶星暗拱的凶险配置。 → 《卷六》"贪狼忌星拱命"
  - `[ns_zwds_j6_011]` `[trigger: 凶亡结果]` `[factor_trigger: result_xiongwang]` `[role: 结果]` 凶亡结果为非正常死亡的凶险结果。 → 《卷六》"故主凶亡"
  - `[ns_zwds_j6_012]` `[trigger: 凶星暗拱]` `[factor_trigger: xiongxing_angong]` `[role: 条件分支]` 凶星暗拱为对宫凶星潜在威胁的配置。 → 《卷六》
  - `[ns_zwds_j6_013]` `[trigger: 勇猛性情]` `[factor_trigger: xingge_yongmeng]` `[role: 结果]` 勇猛性情为廉贞将军坐命的性格特征。 → 《卷六》"故主勇猛""""
    normalized_text_zh: str = """"""
    subject: str = "子路之命"
    factor_refs: list = ['pattern_fuxiangchaoyuan', 'star_lianzhenjiang', 'sihua_tanlangji', 'result_xiongwang', 'pattern_angong', 'source_ref', 'rel_zilu_001', 'pattern_fuxiangchaoyuan', 'rel_zilu_002', 'sihua_tanlangji', 'rel_zilu_003', 'star_lianzhenjiang', 'evi_zilu_001', 'pattern_fuxiangchaoyuan', 'rule_fuxiang_xianshi', 'evi_zilu_002', 'sihua_tanlangji', 'rule_tanlangji_xiongwang', 'concept_noble_pattern', 'concept_hidden_malefic']
    
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
        l1_anchor="zw_v1.0.0_子路之命_001_L1",
    )
    version: str = "1.0.0"
