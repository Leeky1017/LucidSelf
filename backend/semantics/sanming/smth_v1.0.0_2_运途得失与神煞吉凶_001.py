"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066693
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
    semantic_id="smth_v1.0.0_2_运途得失与神煞吉凶_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2运途得失与神煞吉凶(SemanticEntry):
    """
    - 原文（source_text）：
  运到旺乡身反弱，财逢劫处祸犹轻。
  财不有伤，还忌阴谋之贼；煞无明制，当寻伏敌之兵。
  贵人头上戴财官，门充驷马；生旺宫中藏亡劫，勇夺三军。
  为跨马以...
    """
    
    original_text: str = """- 原文（source_text）：
  运到旺乡身反弱，财逢劫处祸犹轻。
  财不有伤，还忌阴谋之贼；煞无明制，当寻伏敌之兵。
  贵人头上戴财官，门充驷马；生旺宫中藏亡劫，勇夺三军。
  为跨马以亡身，因得禄而避位。
  印解两贤之厄，财勾六国之争。
  众煞混行，一仁可化；一煞倡乱，独力可擒。
  印居煞地，化之以德；煞居印地，齐之以刑。

- 分字分词释义：
  - **旺乡身反弱**：从格（从财从煞），行身旺运，反为祸（身弱不能从，与旺神战）。
  - **祸犹轻**：身弱财多，行比劫运分财，祸反轻（得救）。
  - **阴谋之贼**：地支暗藏的比劫（羊刃）。
  - **伏敌之兵**：地支暗藏的食伤。
  - **两贤**：二煞（官煞混杂）。
  - **六国之争**：群比争财。
  - **一仁**：印绶。

- **规范化释义（primary_lang_explained）**：
  从格行至身旺之乡，格局破，反显身弱（受克）。身弱财多，行比劫运分财，祸患反而减轻。
  财星明处无伤，还要防备地支暗藏的比劫（阴谋之贼）劫夺。七煞天干无制，要寻找地支暗藏的食神（伏敌之兵）制煞。
  贵人（天乙）头上带财官，主富贵双全，门庭显赫。亡神劫煞居于长生帝旺之宫，主武职威权，勇夺三军。
  因贪财（跨马）而亡身（财滋煞杀身，或比劫争财）。因得禄（归禄）而避位（辞官？注云：原用官星，运至归禄，比肩争官，故避位）。
  印绶（仁）能化解官煞混杂（两贤）的灾厄。财星（利）能勾起比劫（六国）的争夺。
  众煞混杂，一个印绶（仁）就能化解（杀印相生）。一个七煞作乱，一个食神（独力）就能制伏。
  印绶坐在煞地（如甲用申煞，申中壬水长生，化煞），以德化煞。七煞坐在印地（如乙用辛煞，坐子印地），以刑（子午冲？注云：午冲子去生煞之宫）齐之。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Luck Journey Gains-Losses and Spirit-Killings Auspicious-Inauspicious" from the Six Spirits Chapter:

  - Luck arriving prosperous district body反weak; Wealth meets Robbery place disaster still light.
  - Noble person head above wears Wealth-Official, gate fills four-horses; Life-Prosperous palace hides Dead-Rob, bravely seizes three-armies.
  - Seal resolves two-worthy's disaster; Wealth hooks six-states'争.
  - Multitude Killings mixed traveling, one Benevolence can transform; one Killing incites chaos, lone power can capture.
  - Key: Hidden ambush (暗神) matters; Seal transforms Killings with virtue; Eating God controls alone.

- 核心要点：
  - **从格喜忌**：忌身旺。
  - **暗神**：暗劫、暗食。
  - **印化煞**：仁化暴。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_017]` `[trigger: 旺乡身弱]` `[factor_trigger: wangxiang_shenruo AND congge_pojue]` `[role: 主干]` 运到旺乡身反弱，财逢劫处祸犹轻。 → 《三命通会》卷十一#运途得失与神煞吉凶
  - `[ns_smth_11_018]` `[trigger: 阴谋之贼]` `[factor_trigger: yinmou_zhizei AND fubing_zhidi]` `[role: 主干依赖]` 财不有伤，还忌阴谋之贼；煞无明制，当寻伏敌之兵。 → 《三命通会》卷十一#运途得失与神煞吉凶
  - `[ns_smth_11_019]` `[trigger: 一仁可化]` `[factor_trigger: yiren_kehua AND duoli_keqin]` `[role: 条件分支]` 众煞混行，一仁可化；一煞倡乱，独力可擒。 → 《三命通会》卷十一#运途得失与神煞吉凶
  - `[ns_smth_11_020]` `[trigger: 化德齐刑]` `[factor_trigger: huade_qixing AND yinsha_zhidi]` `[role: 总结]` 印居煞地，化之以德；煞居印地，齐之以刑。 → 《三命通会》卷十一#运途得失与神煞吉凶"""
    normalized_text_zh: str = """"""
    subject: str = "2 运途得失与神煞吉凶"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_10', 'bazi_semantic', 'bazi_relation_factor_13', 'bazi_semantic', 'bazi_relation_factor_14', 'bazi_semantic', 'bazi_state_factor_52', 'bazi_semantic', 'bazi_state_factor_53', 'bazi_semantic', 'bazi_condition_factor_8', 'bazi_semantic', 'source_ref', 'rel_smth_11_013', 'yuntu_deshi', 'rel_smth_11_014', 'guiren_dai_caiguan', 'rel_smth_11_015', 'congge_zhi_shenwang', 'evi_smth_11_013', 'congge_zhi_shenwang', 'rule_congge_ji_shenwang1', 'evi_smth_11_014', 'guiren_dai_caiguan', 'rule_guiren_caiguan1', 'evi_smth_11_015', 'yin_jie_guansha', 'rule_yin_jie_guansha1', 'map_smth_11_009', 'map_smth_11_010']
    
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
        l1_anchor="smth_v1.0.0_2_运途得失与神煞吉凶_001_L1",
    )
    version: str = "1.0.0"
