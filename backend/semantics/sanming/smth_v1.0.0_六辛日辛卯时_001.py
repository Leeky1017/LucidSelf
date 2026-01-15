"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339537
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
    semantic_id="smth_v1.0.0_六辛日辛卯时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日辛卯时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时辛卯，妻子难为遇比肩。秋产冬生贫下格，丙临寅马却当权。
  辛日辛卯时，比肩分财。辛以乙为财，卯上乙旺，遇比分夺，损伤妻子。生秋冬，财官无气，平常。...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时辛卯，妻子难为遇比肩。秋产冬生贫下格，丙临寅马却当权。
  辛日辛卯时，比肩分财。辛以乙为财，卯上乙旺，遇比分夺，损伤妻子。生秋冬，财官无气，平常。寅巳午月，干透丙火，丙合辛生，官贵显达。辛卯，悬针煞，柱多不吉。

- 分字分词释义：
  - **比肩分财**：两辛争一卯（乙木财），比劫夺财。
  - **秋产冬生**：秋金旺夺财，冬水寒木漂（财无气）。
  - **丙临寅马**：若见丙寅（丙为官，寅为财），财官相生，或丙火合辛（威制），主权贵。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于辛卯时，时干透辛比肩，分夺时支卯木偏财，主克妻破财。若生于秋冬，金水旺而财官无气，主贫下。若生于寅巳午月，天干透丙火正官，丙辛相合（化水或合绊），官星护财，主显达。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Xin-Mao Hour":

  - Wife-children difficult encountering Parallel Shoulder—two Xin contend for one Mao (Yi Wood Wealth), Rob-divides wealth.
  - Autumn-born winter-born indicates poverty low status pattern; if Bing reaches Yin-Horse (Bing-Yin), then holds power.
  - Born in autumn-winter, Wealth-Official have no qi, ordinary; Yin-Si-Wu months with Bing Fire revealing, Bing-Xin combine, Official nobility prominent.
  - Key: Parallel shoulder divides wealth damages spouse; requires Official (Fire) to control Rob and protect Wealth.

- 核心要点：
  - **比劫夺财**：二辛争卯，克妻。
  - **喜官煞**：喜丙丁火制比劫护财。
  - **悬针煞**：辛卯为悬针，主刑伤。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_109]` `[trigger: 妻子难为]` `[factor_trigger: qizi_nanwei AND yu_bijian]` `[role: 主干]` 六辛日生时辛卯，妻子难为遇比肩。 → 《三命通会》卷九#六辛日辛卯时
  - `[ns_smth_09_110]` `[trigger: 秋冬贫下]` `[factor_trigger: qiudong_pinxia AND bing_lin_que_dangquan]` `[role: 主干依赖]` 秋产冬生贫下格，丙临寅马却当权。 → 《三命通会》卷九#六辛日辛卯时
  - `[ns_smth_09_111]` `[trigger: 比肩分财]` `[factor_trigger: bijian_fencai AND sun_shang_qizi]` `[role: 条件分支]` 辛卯时，比肩分财，损伤妻子。 → 《三命通会》卷九#六辛日辛卯时
  - `[ns_smth_09_112]` `[trigger: 透丙显达]` `[factor_trigger: toubing_xianda AND guan_guixianda]` `[role: 总结]` 寅巳午月，干透丙火，丙合辛生，官贵显达。 → 《三命通会》卷九#六辛日辛卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日辛卯时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_bijian_3', 'bazi_semantic', 'bazi_relation_factor_124', 'bazi_semantic', 'bazi_state_factor_292', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_bing_fire', 'bazi_semantic', 'source_ref', 'rel_smth_09_082', 'bijian_fencai', 'rel_smth_09_083', 'bijian_fencai', 'rel_smth_09_084', 'tou_bing_huo_chunxia', 'evi_smth_09_082', 'bijian_fencai', 'rule_bijian_fencai1', 'evi_smth_09_083', 'bijian_fencai', 'rule_qiudong_pinxiage1', 'evi_smth_09_084', 'guanzhi_jie_hu_cai', 'rule_binglin_yinma1', 'map_smth_09_055', 'map_smth_09_056']
    
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
        l1_anchor="smth_v1.0.0_六辛日辛卯时_001_L1",
    )
    version: str = "1.0.0"
