"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.698912
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
    semantic_id="zw_v1.0.0_孔仲尼命_阳男土五局_其一_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 孔仲尼命阳男土五局其一(SemanticEntry):
    """
    - 分字分词释义：

  - **活禄逢迎**：禄存与化禄同临或拱照命宫的极贵格局，此命主文名冠世。
  - **劫空**：地劫天空的简称，此命辛亥年太岁带此，主困厄绝粮。
  - **天伤**：流年...
    """
    
    original_text: str = """- 分字分词释义：

  - **活禄逢迎**：禄存与化禄同临或拱照命宫的极贵格局，此命主文名冠世。
  - **劫空**：地劫天空的简称，此命辛亥年太岁带此，主困厄绝粮。
  - **天伤**：流年凶星，小限逢此主灾患，与劫空叠加更凶。
  - **天罗地网**：辰戌两宫形成的束缚格局，七十三岁小限入天罗、太岁入地网，为寿终应期。
  - **戌生人有忌**：戌年生人的特定禁忌，叠加天罗地网风险极高。
  - **在陈绝粮**：孔子困于陈国断粮七日的历史事件，此命例中为六十二岁限运应期。
  - **阳男土五局**：紫微斗数命盘的五行局数，土五局主厚重稳健。

- **原文（source_text）**：  
  孔仲尼命。阳男土五局。活禄逢迎，夫子文童冠世。辛亥年六十二岁，在陈绝粮。盖因太岁有劫空，小限逢天伤，七十三岁，小限在天罗，太岁入地网，戌生人有忌，故死。

- **规范化释义（primary_lang_explained）**：  
  此为孔子命例其一。阳男土五局，命宫得活禄逢迎之格，主文名冠世，为万代圣师。辛亥年六十二岁，因太岁带劫空、小限逢天伤，故在陈国遭困绝粮之厄。七十三岁，小限入天罗、太岁入地网，戌生人本有忌讳，诸凶齐聚，遂殁于此岁。命局虽极贵，亦难逃限运之劫。

- **完整对等诠释（secondary_lang_full）**：  
  This is the first version of Confucius's chart. As a Yang male in the Earth Fifth Configuration, his Life palace enjoys the pattern of "Active Salary Greeting", indicating supreme literary fame and the title of Teacher for Ten Thousand Generations. At age 62, in the xin‑hai year, the Annual Tai Sui carried Robbery and Void while the minor period met the Celestial Wound star, hence the hardship of running out of grain while stranded in the state of Chen. At 73, the minor period entered the Net of Heaven while Tai Sui fell into the Net of Earth; being born in xu year brought additional taboos. With all malefics converging, the Sage passed away in that year. Even the most honoured chart cannot escape the ordeals set by periods and transits.

- **核心要点**：  
  1. 活禄逢迎格局主文名极盛，为圣贤之象。  
  2. 限运逢劫空、天伤等凶星，可致困厄。  
  3. 天罗地网与戌忌叠加，为最终寿终之应期。

- **叙事素材（narrative_snippets）**：
  - **圣人格局**："活禄逢迎，夫子文童冠世"，孔子命格主文名极盛。
  - **困陈之厄**："辛亥年六十二岁，太岁劫空，小限逢天伤，故在陈绝粮"，限运凶星致困厄。
  - **寿终之应**："七十三岁，小限天罗，太岁地网，戌生人有忌"，诸凶齐聚遂殁。
  - **现代应用**：即使极贵命格，亦难逃限运之劫——格局定高度，限运定时点。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j6_001]` `[trigger: 活禄逢迎格]` `[factor_trigger: pattern_huolufengying]` `[role: 条件分支]` 活禄逢迎格为禄星活跃逢迎命宫的极贵格局。 → 《卷六》孔子命
  - `[ns_zwds_j6_002]` `[trigger: 天伤星]` `[factor_trigger: star_tianshang]` `[role: 主干]` 天伤星为主伤灾疾病困厄的凶星。 → 《卷六》"小限逢天伤"
  - `[ns_zwds_j6_003]` `[trigger: 限运凶星]` `[factor_trigger: xianxun_xiongxing]` `[role: 条件分支]` 限运凶星为大限小限遇凶星的配置。 → 《卷六》"太岁劫空"
  - `[ns_zwds_j6_004]` `[trigger: 困厄应期]` `[factor_trigger: kune_yingqi]` `[role: 结果]` 困厄应期为遭遇困厄的时间节点。 → 《卷六》"在陈绝粮"
  - `[ns_zwds_j6_005]` `[trigger: 寿终应期]` `[factor_trigger: shouzhong_yingqi]` `[role: 结果]` 寿终应期为寿命终结的时间节点。 → 《卷六》"七十三岁...遂殁"
  - `[ns_zwds_j6_006]` `[trigger: 夭于九岁]` `[factor_trigger: result_yao_yu_jiusui]` `[role: 结果]` 夭于九岁为童年夭折的凶险结果。 → 《卷六》
  - `[ns_zwds_j6_007]` `[trigger: 太岁冲克]` `[factor_trigger: taisui_chongke]` `[role: 条件分支]` 太岁冲克为流年太岁冲克命宫的配置。 → 《卷六》"太岁地网""""
    normalized_text_zh: str = """"""
    subject: str = "孔仲尼命（阳男土五局·其一）"
    factor_refs: list = ['pattern_huolufengying', 'star_jiekong', 'star_tianshang', 'pattern_tianluodiwang', 'taboo_xuji', 'source_ref', 'rel_kongzi_001', 'pattern_huolufengying', 'rel_kongzi_002', 'star_jiekong', 'rel_kongzi_003', 'pattern_tianluodiwang', 'evi_kongzi_001', 'pattern_huolufengying', 'rule_huolu_wenming', 'evi_kongzi_002', 'star_jiekong', 'rule_jiekong_kune', 'evi_kongzi_003', 'pattern_tianluodiwang', 'rule_tianluodiwang_si', 'concept_supreme_fame', 'concept_period_crisis']
    
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
        l1_anchor="zw_v1.0.0_孔仲尼命_阳男土五局_其一_001_L1",
    )
    version: str = "1.0.0"
