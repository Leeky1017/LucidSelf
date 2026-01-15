"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227525
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
    semantic_id="smth_v1.0.0_伏羲八卦与纳音之端_001",
    book_id="sanming",
    engine_id="bazi"
)
class 伏羲八卦与纳音之端(SemanticEntry):
    """
    - **原文（source_text）**：
  至于伏羲仰观象于天，俯观法于地，中观万物与人，始画八卦以通神明之德，以类万物之情，以作甲历而文字生焉。逮及黄帝授河图，见日月星辰之象，于是始有星官之书...
    """
    
    original_text: str = """- **原文（source_text）**：
  至于伏羲仰观象于天，俯观法于地，中观万物与人，始画八卦以通神明之德，以类万物之情，以作甲历而文字生焉。逮及黄帝授河图，见日月星辰之象，于是始有星官之书。命大尧探五行之情，占斗纲所建，于是始作甲子配五行纳音之属。

- 分字分词释义：
  - **画八卦**：伏羲所作的八卦，用以统摄天地万物之理与象。
  - **甲历**：以干支纪年的历法，后世甲子纪年制之源头。
  - **河图、星官之书**：黄帝时代所据以观察天象、分布星宿的图籍与著作。
  - **甲子配五行纳音**：以六十甲子与五行、音律相配，是后文纳音体系的起点。

- **规范化释义（primary_lang_explained）**：
  这一段承上启下，从伏羲画卦、制定历法说到黄帝观河图、建星官，再说到尧帝命人探究五行之情，由此创立「甲子配五行纳音」的制度。干支不只是记日记年符号，而是与卦象、星辰、五行和音律连成一体的综合系统。

- **完整对等诠释（secondary_lang_full）**：

  This paragraph bridges earlier discussions by linking Fuxi, who "gazed up at heaven and down to earth" and drew the Eight Trigrams, to the Yellow Emperor, who received the River Diagram and organised the stars, and then to Emperor Yao, who ordered investigations into the Five‑Element qualities and established the system of matching the sixty Jiazi with Wuxing and musical tones—the Nayin. Stems and branches are therefore not merely date labels, but nodes in a larger network that connects trigrams, star patterns, elements and tonal qualities. Practically, this means that a given stem–branch combination can be viewed simultaneously through calendrical, cosmological and acoustic lenses, and that Nayin should be treated as a fine‑grained elaboration of the stem–branch structure rather than a free‑floating, independent oracle.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_975]` `[trigger: 土木松疏态]` `[factor_trigger: earth_wood_loosening_state]` `[role: 条件分支]` 土木松疏态主调和。 → 《三命通会》卷一
  - `[ns_smth_976]` `[trigger: 堤坝困水风险]` `[factor_trigger: embankment_traps_water_risk]` `[role: 条件分支]` 堤坝困水有风险。 → 《三命通会》卷一
  - `[ns_smth_977]` `[trigger: 建禄印配置]` `[factor_trigger: establish_salary_seal_config]` `[role: 条件分支]` 建禄印配置定格局。 → 《三命通会》卷一
  - `[ns_smth_978]` `[trigger: 反复进退]` `[factor_trigger: fanfu_jintui]` `[role: 条件分支]` 反复进退主变化。 → 《三命通会》卷一
  - `[ns_smth_979]` `[trigger: 飞财年份风险]` `[factor_trigger: feicai_nianfen_risk]` `[role: 条件分支]` 飞财年份有风险。 → 《三命通会》卷一
  - `[ns_smth_980]` `[trigger: 飞截木大火]` `[factor_trigger: feijiemu_dahuo]` `[role: 条件分支]` 飞截木大火主燃尽。 → 《三命通会》卷一
  - `[ns_smth_981]` `[trigger: 飞天巳日类型]` `[factor_trigger: feitian_siri_leixing]` `[role: 条件分支]` 飞天巳日类型定格局。 → 《三命通会》卷一
  - `[ns_smth_982]` `[trigger: 火旺评分]` `[factor_trigger: fire_dominance_score]` `[role: 条件分支]` 火旺评分定强度。 → 《三命通会》卷一
  - `[ns_smth_983]` `[trigger: 火土调支]` `[factor_trigger: fire_earth_regulate_support]` `[role: 条件分支]` 火土调支主调和。 → 《三命通会》卷一
  - `[ns_smth_984]` `[trigger: 火土木平衡]` `[factor_trigger: fire_earth_wood_balance]` `[role: 条件分支]` 火土木平衡主调和。 → 《三命通会》卷一
  - `[ns_smth_985]` `[trigger: 火表达特征]` `[factor_trigger: fire_expression_profile]` `[role: 条件分支]` 火表达特征定性格。 → 《三命通会》卷一
  - `[ns_smth_986]` `[trigger: 火峰强度]` `[factor_trigger: fire_peak_intensity]` `[role: 条件分支]` 火峰强度定旺衰。 → 《三命通会》卷一
  - `[ns_smth_987]` `[trigger: 火峰官杀控制]` `[factor_trigger: fire_peak_official_killing_control]` `[role: 条件分支]` 火峰官杀控制定格局。 → 《三命通会》卷一
  - `[ns_smth_988]` `[trigger: 火炼金器]` `[factor_trigger: fire_refines_metal_tool]` `[role: 条件分支]` 火炼金器主成器。 → 《三命通会》卷一
  - `[ns_smth_989]` `[trigger: 火季节态]` `[factor_trigger: fire_season_state]` `[role: 条件分支]` 火季节态定时令。 → 《三命通会》卷一
  - `[ns_smth_990]` `[trigger: 五行基础]` `[factor_trigger: five_element_base]` `[role: 条件分支]` 五行基础定属性。 → 《三命通会》卷一
  - `[ns_smth_991]` `[trigger: 五行]` `[factor_trigger: five_elements]` `[role: 条件分支]` 五行定基础。 → 《三命通会》卷一
  - `[ns_smth_992]` `[trigger: 流金熔石警示]` `[factor_trigger: flowing_gold_melting_stone_alert]` `[role: 条件分支]` 流金熔石有警示。 → 《三命通会》卷一
  - `[ns_smth_993]` `[trigger: 形态转化]` `[factor_trigger: form_transformation]` `[role: 条件分支]` 形态转化主变化。 → 《三命通会》卷一
  - `[ns_smth_994]` `[trigger: 伏不发法风险]` `[factor_trigger: fu_bufafa_risk]` `[role: 条件分支]` 伏不发法有风险。 → 《三命通会》卷一
  - `[ns_smth_995]` `[trigger: 伏偏残]` `[factor_trigger: fu_piancan]` `[role: 条件分支]` 伏偏残主残缺。 → 《三命通会》卷一
  - `[ns_smth_996]` `[trigger: 富贵等级]` `[factor_trigger: fugui_dengji]` `[role: 条件分支]` 富贵等级定高低。 → 《三命通会》卷一
  - `[ns_smth_997]` `[trigger: 富豪显达]` `[factor_trigger: fuhao_xianda]` `[role: 条件分支]` 富豪显达主大富。 → 《三命通会》卷一
  - `[ns_smth_998]` `[trigger: 富贫变质]` `[factor_trigger: fupin_bianzhi]` `[role: 条件分支]` 富贫变质主变化。 → 《三命通会》卷一
  - `[ns_smth_999]` `[trigger: 扶神辅助评分]` `[factor_trigger: fushen_fuzhu_score]` `[role: 条件分支]` 扶神辅助评分定强度。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "伏羲八卦与纳音之端"
    factor_refs: list = []
    
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
        l1_anchor="smth_v1.0.0_伏羲八卦与纳音之端_001_L1",
    )
    version: str = "1.0.0"
