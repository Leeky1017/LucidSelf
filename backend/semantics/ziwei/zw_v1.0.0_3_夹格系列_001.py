"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778433
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
    semantic_id="zw_v1.0.0_3_夹格系列_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 3夹格系列(SemanticEntry):
    """
    ##### 1.3.1 夹贵夹禄夹权夹科（上格）

- 原文（断句）：

  夹贵夹禄少人知，夹权夹科世所宜，假如丙丁壬癸生人在辰戌安命，魁钺加夹，更遇紫微天府、日月权禄，左右昌曲，夹身夹命，是左夹贵...
    """
    
    original_text: str = """##### 1.3.1 夹贵夹禄夹权夹科（上格）

- 原文（断句）：

  夹贵夹禄少人知，夹权夹科世所宜，假如丙丁壬癸生人在辰戌安命，魁钺加夹，更遇紫微天府、日月权禄，左右昌曲，夹身夹命，是左夹贵，富贵必矣。如甲生人，身命丑卯，而寅禄居中，是生成之禄，尤为上格。

- 分字分词释义：

  - **夹贵**：天魁天钺等贵人星夹持命宫。
  - **夹禄**：禄存居中被两侧星曜夹持，形成禄气包裹。
  - **夹权**：化权星夹命，主权力被环护。
  - **夹科**：化科星夹命，主科名文章被环护。
  - **丙丁壬癸生人**：特定天干生人，与贵人位置相合。
  - **辰戌安命**：命宫在辰宫或戌宫。
  - **魁钺加夹**：天魁天钺在命宫两侧形成夹持。
  - **夹日夹月**：太阳太阴在命宫前后形成夹持。
  - **夹昌夹曲**：文昌文曲夹命，主文章科名被环护。
  - **夹空夹劫**：天空地劫夹命，主破败虚耗。
  - **夹羊夹陀**：擎羊陀罗夹命，主困顿刑克。
  - **生成之禄**：天干所带之禄自然落在有利位置。
  - **孤寒下格**：贫穷孤苦的低等格局。

- 规范化释义（primary_lang_explained）：

  夹贵夹禄夹权夹科皆为上格，少有人知。假如丙丁壬癸生人在辰戌安命，魁钺加夹，更遇紫微天府日月权禄左右昌曲夹身夹命，是为夹贵，富贵必然。如甲生人身命在丑卯，而寅禄居中，是生成之禄，尤为上格。

- 核心要点：
  - **夹贵**：魁钺夹命、紫府夹命、日月夹命
  - **夹禄**：禄存居中被夹
  - **夹权夹科**：权科星夹命
  - **上格条件**：吉星前后夹命，不遇恶曜

##### 1.3.2 夹月夹日夹昌夹曲（贵格）

- 原文（断句）：

  夹月夹日谁能遇。夹昌夹曲亦贵兮，假如太阳、太阴在身命前后二宫夹命，不逢空劫羊铃，其贵必矣。如昌曲夹命亦如之。

- 规范化释义（primary_lang_explained）：

  夹月夹日谁能遇，夹昌夹曲亦贵。假如太阳太阴在身命前后二宫夹命，不逢空劫羊铃，其贵必然。昌曲夹命亦如此。

- 核心要点：
  - **日月夹命**、**昌曲夹命**，不逢空劫羊铃，主贵。

##### 1.3.3 夹空夹劫夹羊夹陀（下格）

- 原文（断句）：

  夹空、夹劫主贫贱；夹羊、夹陀为乞丐，假如命化忌遇天空、地劫、羊陀等杀夹身命者，及廉、破、武等星值之，定主孤寒下格，如不应即夭。又如命化忌廉贞、羊陀、火铃来夹者，亦为下格。或禄在生旺酉地，虽夹禄羊陀，不为下格。

- 规范化释义（primary_lang_explained）：

  夹空夹劫主贫贱，夹羊夹陀为乞丐。假如命化忌遇天空地劫羊陀等杀夹身命者，及廉贞破军武曲等星值之，定主孤寒下格，如不应则夭折。又如命化忌廉贞羊陀火铃来夹者，亦为下格。但若禄在生旺地，虽夹禄羊陀，不为下格。

- 完整对等诠释（secondary_lang_full）：

  The "Flanking" pattern series represents a critical pattern-recognition method in Ziwei Doushu. When auspicious stars (Tiankui-Tianyue, Ziwei-Tianfu, Sun-Moon, Wenchang-Wenqu) or Lucun occupy the palaces immediately preceding and following the Life or Body Palace, forming a "flanking embrace," this constitutes superior patterns indicating nobility and wealth. The Sun-Moon flanking is particularly rare and precious. Conversely, when malefics (Dikong-Dijie, Qingyang-Tuoluo) flank the Life Palace, especially accompanied by transformation-taboo and inauspicious stars like Lianzhen, Pojun, or Wuqu, this creates inferior patterns portending destitution or begging. An exception exists: if Lucun resides in prosperous-longevity positions, even flanked by Qingyang-Tuoluo, the pattern does not degenerate into inferiority. This system emphasizes positional relationship geometry—benefics flanking amplify blessings, malefics flanking intensify afflictions. The key lies in examining what stars occupy the two palaces adjacent to Life-Body, their temple-dignity states, and whether transformation-taboo amplifies the malefic configuration.

- 核心要点：
  - **夹空劫**：空劫夹命主贫贱
  - **夹羊陀**：羊陀夹命为乞丐
  - **例外**：禄在生旺地，虽夹羊陀不为下格

- 叙事素材（narrative_snippets）：

  - **六吉夹命**："夹贵夹禄少人知，夹权夹科世所宜"，以魁钺、紫府、日月、科权禄等吉星前后夹命，形成上等贵格。
  - **日月昌曲夹**："夹月夹日谁能遇，夹昌夹曲亦贵兮"，日月或昌曲夹命且不逢空劫羊铃，象征光明文章被贵气环护。
  - **四凶夹命**："夹空、夹劫主贫贱；夹羊、夹陀为乞丐"，空劫、羊陀从两侧包夹命宫，多主困顿流离、求存不易。
  - **禄在生旺例外**："或禄在生旺酉地，虽夹禄羊陀，不为下格"，强调当禄气足够强时，仍可部分抵消凶夹的拖累。
  - **几何视角**：夹格本质是在看命宫前后两宫的"几何态势"——是被贵气拱卫，还是被凶煞锁死，决定一生行走的轨道高度。
  - **现代应用**：解盘时可先检查命宫两侧星群，作为判断"出生环境与外部结构"友善与否的第一道筛选。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j2_026]` `[trigger: 夹贵格局]` `[factor_trigger: geju_jiagui]` `[role: 条件分支]` 夹贵格局为魁钺夹命的上等贵格。 → 《骨髓赋》"夹贵夹禄"
  - `[ns_zwds_j2_027]` `[trigger: 夹禄格局]` `[factor_trigger: geju_jialu]` `[role: 条件分支]` 夹禄格局为禄存或化禄夹命的富贵格局。 → 《骨髓赋》"夹贵夹禄"
  - `[ns_zwds_j2_028]` `[trigger: 日月夹命]` `[factor_trigger: geju_riyuejiaming]` `[role: 条件分支]` 日月夹命为太阳太阴夹命宫的贵格。 → 《骨髓赋》"夹月夹日"
  - `[ns_zwds_j2_029]` `[trigger: 昌曲夹命]` `[factor_trigger: geju_changqujiaming]` `[role: 条件分支]` 昌曲夹命为文昌文曲夹命宫的贵格。 → 《骨髓赋》"夹昌夹曲"
  - `[ns_zwds_j2_030]` `[trigger: 空劫夹命]` `[factor_trigger: geju_kongjiejiaming]` `[role: 条件分支]` 空劫夹命为地空地劫夹命宫的下格，主贫贱。 → 《骨髓赋》"夹空夹劫主贫贱"
  - `[ns_zwds_j2_031]` `[trigger: 羊陀夹命]` `[factor_trigger: geju_yangtuojiaming]` `[role: 条件分支]` 羊陀夹命为擎羊陀罗夹命宫的下格，主乞丐。 → 《骨髓赋》"夹羊夹陀为乞丐"
  - `[ns_zwds_j2_032]` `[trigger: 财印夹名]` `[factor_trigger: combo_caiyin_jiaming]` `[role: 条件分支]` 财印夹名为财星印星夹命的富贵格局。 → 《骨髓赋》
  - `[ns_zwds_j2_033]` `[trigger: 禄存守元]` `[factor_trigger: star_lucunzuoming]` `[role: 条件分支]` 禄存守命为禄存坐命宫的配置。 → 《骨髓赋》
  - `[ns_zwds_j2_034]` `[trigger: 禄存寿元]` `[factor_trigger: star_lucunshouyuan]` `[role: 条件分支]` 禄存寿元为禄存守疾厄主长寿的配置。 → 《骨髓赋》
  - `[ns_zwds_j2_035]` `[trigger: 错宫风险]` `[factor_trigger: risk_cuogong]` `[role: 条件分支]` 错宫风险为星曜落入不当宫位的风险。 → 《骨髓赋》
  - `[ns_zwds_j2_036]` `[trigger: 加禄格局]` `[factor_trigger: combo_jialu]` `[role: 条件分支]` 加禄格局为吉星加会禄存的配置。 → 《骨髓赋》"""
    normalized_text_zh: str = """"""
    subject: str = "3 夹格系列"
    factor_refs: list = ['engine_id', 'jiage_leixing', 'ziwei_rule_engine', 'jiaxing_zuhe', 'ziwei_calculator', 'jiage_poge', 'ziwei_rule_engine', 'jiage_cengci', 'ziwei_rule_engine', 'jiage_leixing', 'combo_jiagui', 'combo_jialu', 'combo_jiakongjie', 'combo_jiayangtuo', 'combo_shengcheng', 'source_ref', 'rel_jiage_001', 'jiaxing_zuhe', 'rel_jiage_002', 'jiage_poge', 'rel_jiage_003', 'combo_jialu', 'evi_jiage_001', 'rule_jiagui_jialu', 'evi_jiage_002', 'combo_jiakongjie', 'rule_jiakongjie', 'evi_jiage_003', 'rule_lu_jie_xiong', 'concept_flanking', 'concept_protection']
    
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
        l1_anchor="zw_v1.0.0_3_夹格系列_001_L1",
    )
    version: str = "1.0.0"
