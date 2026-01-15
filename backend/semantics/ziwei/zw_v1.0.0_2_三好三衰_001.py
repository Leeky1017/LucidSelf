"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778418
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
    semantic_id="zw_v1.0.0_2_三好三衰_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 2三好三衰(SemanticEntry):
    """
    ##### 1.2.1 命好身好限好，到老荣昌

- 原文（断句）：

  命好身好限好，到老荣昌；假如身命坐长生帝旺之乡，本宫又得士星庙旺，及大小二限，又遇相生吉地吉星，则一世谋为，无不顺遂。

-...
    """
    
    original_text: str = """##### 1.2.1 命好身好限好，到老荣昌

- 原文（断句）：

  命好身好限好，到老荣昌；假如身命坐长生帝旺之乡，本宫又得士星庙旺，及大小二限，又遇相生吉地吉星，则一世谋为，无不顺遂。

- 分字分词释义：

  - **命好身好限好**：命宫、身宫、限运三者都处于吉旺状态。
  - **到老荣昌**：一生直到老年都荣耀昌盛。
  - **长生帝旺之乡**：十二长生中最旺的两个位置，主生机与权力。
  - **本宫又得士星庙旺**：命身所在宫位有吉星处于庙旺状态。
  - **大小二限**：大限（十年一运）与小限（一年一运）。
  - **相生吉地吉星**：限运所行宫位有吉星且五行相生。
  - **命衰身衰限衰**：命宫、身宫、限运三者都处于衰弱状态。
  - **终身乞丐**：一生贫贱，沦为乞丐。
  - **死绝之乡**：十二长生中最衰的两个位置，主衰亡与断绝。
  - **羊陀火铃空劫**：六煞星群，主凶险破败。

- 规范化释义（primary_lang_explained）：

  命好身好限好，则到老荣昌。假如身命宫坐在长生帝旺之地，本宫又有吉星庙旺，大限小限又遇相生吉地吉星，则一生谋为无不顺遂。

- 原文（断句）：

  命衰身衰限衰，终身乞丐。假如身命居死绝之乡，本宫不见吉化，更会羊陀、火铃、空劫诸般恶曜，而运限又无吉星接应，定主贫贱。

- 规范化释义（primary_lang_explained）：

  命衰身衰限衰，则终身乞丐。假如身命宫居于死绝之地，本宫不见吉化，更有羊陀火铃空劫诸般恶曜，而运限又无吉星接应，定主贫贱。

- 完整对等诠释（secondary_lang_full）：

  When the Life Palace, Body Palace, and transiting limits all manifest auspiciously—termed "three favorable conditions"—one enjoys prosperity and honor throughout life. For instance, if the Life-Body palaces occupy longevity or emperor-prosperity positions, the natal palace hosts benefic stars in temple dignity, and both major and minor limits encounter mutually supportive auspicious positions and stars, then all endeavors throughout one's lifetime proceed smoothly without obstruction. Conversely, when Life, Body, and limits all show debilitation—termed "three unfavorable conditions"—one becomes destitute, reduced to begging. If the Life-Body palaces reside in death-extinction positions, the natal palace lacks any auspicious transformation, and malefics like Qingyang, Tuoluo, Huoxing, Lingxing, Dikong, and Dijie cluster together while transiting limits receive no benefic support, poverty and baseness are inevitable. This framework establishes a three-dimensional assessment model: innate foundation (Life-Body palace vitality), pattern configuration (natal palace star quality), and temporal opportunities (limit support). Only when all three align favorably does true prosperity manifest; when all three deteriorate, lifelong hardship ensues.

- 核心要点：

  - **三好齐全**（身命强旺+本宫吉星+限运吉地），一生顺遂。
  - **三衰齐全**（身命死绝+本宫恶曜+限运无吉），终身贫贱。

- 叙事素材（narrative_snippets）：

  - **三好典范**："命好身好限好，则到老荣昌"，身命强旺+本宫吉星+限运吉地的理想组合。
  - **三衰极端**："命衰身衰限衰，终身乞丐"，身命死绝+本宫恶曜+限运无吉的最差情况。
  - **三维评估**：本条建立"先天基础+格局配置+时运机遇"的三维评估模型。
  - **现代应用**：可作为命盘整体评分的框架——分别评估身命状态、格局质量、限运走势三个维度。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j2_016]` `[trigger: 生命旺衰]` `[factor_trigger: shengming_wangshuai]` `[role: 主干]` 身命旺衰为身命宫的强弱状态，分长生帝旺/平常/死绝。 → 《骨髓赋》"命好身好"
  - `[ns_zwds_j2_017]` `[trigger: 本宫星曜]` `[factor_trigger: bengong_xingyao]` `[role: 主干]` 本宫星曜为命宫所坐星曜的吉凶配置。 → 《骨髓赋》
  - `[ns_zwds_j2_018]` `[trigger: 限运吉凶]` `[factor_trigger: xianyun_jixi]` `[role: 主干]` 限运吉凶为大限小限所遇星曜的吉凶状态。 → 《骨髓赋》"限好"
  - `[ns_zwds_j2_019]` `[trigger: 长生帝旺]` `[factor_trigger: state_shengwang]` `[role: 条件分支]` 长生帝旺为十二长生中最强势的阶段。 → 《骨髓赋》"长生帝旺之地"
  - `[ns_zwds_j2_020]` `[trigger: 死绝之地]` `[factor_trigger: state_sijue]` `[role: 条件分支]` 死绝之地为十二长生中最衰弱的阶段。 → 《骨髓赋》"死绝之乡"
  - `[ns_zwds_j2_021]` `[trigger: 长期走势]` `[factor_trigger: changqi_zoushi]` `[role: 结果]` 长期走势为命运发展的总体趋势判断。 → 《骨髓赋》"到老荣昌"
  - `[ns_zwds_j2_022]` `[trigger: 财富宫位]` `[factor_trigger: caifu_gongwei]` `[role: 主干]` 财富宫位为财帛宫及相关宫位的统称。 → 《骨髓赋》
  - `[ns_zwds_j2_023]` `[trigger: 财富结构]` `[factor_trigger: caifu_jiegou]` `[role: 主干]` 财富结构为财帛宫与相关宫位的综合配置。 → 《骨髓赋》
  - `[ns_zwds_j2_024]` `[trigger: 冲破关系]` `[factor_trigger: chongpo_guanxi]` `[role: 条件分支]` 冲破关系为星曜相冲相破的对立状态。 → 《骨髓赋》
  - `[ns_zwds_j2_025]` `[trigger: 成就温度]` `[factor_trigger: chengjuwengdu]` `[role: 结果]` 成就温度为事业成就的高低程度评估。 → 《骨髓赋》"""
    normalized_text_zh: str = """"""
    subject: str = "2 三好三衰"
    factor_refs: list = ['engine_id', 'shengming_wangshuai', 'ziwei_calculator', 'bengong_xingyao', 'ziwei_calculator', 'xianyun_jixi', 'ziwei_rule_engine', 'sanwei_pinggu', 'ziwei_rule_engine', 'sanwei_pinggu', 'state_changsheng', 'state_sijue', 'star_miaowang', 'time_daxian_xiaoxian', 'source_ref', 'rel_sanhao_001', 'shengming_wangshuai', 'rel_sanhao_002', 'bengong_xingyao', 'rel_sanhao_003', 'xianyun_jixi', 'evi_sanhao_001', 'sanwei_pinggu', 'rule_sanhao_ji', 'evi_sanhao_002', 'sanwei_pinggu', 'rule_sanshuai_xiong', 'concept_three_dimension', 'concept_vitality_state']
    
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
        l1_anchor="zw_v1.0.0_2_三好三衰_001_L1",
    )
    version: str = "1.0.0"
