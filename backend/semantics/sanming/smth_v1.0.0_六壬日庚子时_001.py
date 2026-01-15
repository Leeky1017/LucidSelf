"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339726
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
    semantic_id="smth_v1.0.0_六壬日庚子时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日庚子时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时庚子，子上明庚暗损伤。火土月中仍主吉，不通凶狠只平常。
  壬日庚子时，刃旺身强。壬以庚为倒食，癸为羊刃，时上明庚癸旺，若通火土月气，制伏庚癸，大贵...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时庚子，子上明庚暗损伤。火土月中仍主吉，不通凶狠只平常。
  壬日庚子时，刃旺身强。壬以庚为倒食，癸为羊刃，时上明庚癸旺，若通火土月气，制伏庚癸，大贵；不通，凶狠平常。通运亦贵。

- 分字分词释义：
  - **子上明庚暗损伤**：庚金偏印透干，子为壬水羊刃。羊刃旺，易伤妻财，故云“暗损伤”。
  - **倒食**：庚金为壬水偏印。
  - **制伏庚癸**：喜财（火）制印（庚），官杀（土）制刃（癸）。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于庚子时，时干透庚金偏印，时支子水为羊刃。身旺刃旺。若生于火土旺月（财官月），财能坏印，官能制刃，主大贵。若不通火土气，身旺无制，性情凶狠，只是平常之命。若行运见财官，亦贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Geng-Zi Hour":

  - Zi above bright Geng dark damage-injury—Geng Metal Partial Seal reveals; Zi is Ren Water's Yang Blade; Blade prosperous body strong.
  - In Fire-Earth months still rules auspicious; not connected fierce violent only ordinary.
  - Ren uses Geng as Reversed-Food, Gui as Yang-Blade; hour above bright Geng Gui prosperous; if connecting Fire-Earth monthly qi controlling Geng-Gui, great nobility.
  - Key: Blade-Owl double heavy needs Wealth-Official control; otherwise fierce violent ordinary fate.

- 核心要点：
  - **羊刃格**：壬日子时，羊刃。
  - **枭印**：庚金透，生身太过。
  - **喜财官**：制枭制刃。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_145]` `[trigger: 明庚暗损伤]` `[factor_trigger: minggeng_ansunshang AND zishang_yangren]` `[role: 主干]` 六壬日生时庚子，子上明庚暗损伤。 → 《三命通会》卷九#六壬日庚子时
  - `[ns_smth_09_146]` `[trigger: 火土月吉]` `[factor_trigger: huotu_yue_ji AND butong_xionghen]` `[role: 主干依赖]` 火土月中仍主吉，不通凶狠只平常。 → 《三命通会》卷九#六壬日庚子时
  - `[ns_smth_09_147]` `[trigger: 刃旺身强]` `[factor_trigger: renwang_shenqiang AND tong_huotu_yueqi]` `[role: 条件分支]` 刃旺身强，若通火土月气，制伏庚癸，大贵。 → 《三命通会》卷九#六壬日庚子时
  - `[ns_smth_09_148]` `[trigger: 通运亦贵]` `[factor_trigger: tongyun_yigui AND zhifu_genggui]` `[role: 总结]` 不通，凶狠平常。通运亦贵。 → 《三命通会》卷九#六壬日庚子时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日庚子时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_yangren_4', 'bazi_semantic', 'bazi_relation_factor_133', 'bazi_semantic', 'bazi_state_factor_328', 'bazi_semantic', 'hour_branch_zi', 'bazi_semantic', 'bazi_condition_fire_earth_3', 'bazi_semantic', 'source_ref', 'rel_smth_09_109', 'yangren_daoshi', 'rel_smth_09_110', 'yangren_daoshi', 'rel_smth_09_111', 'huotu_cai_guan_yun', 'evi_smth_09_109', 'tong_huotu_yueqi', 'rule_tong_huotu_yueqi1', 'evi_smth_09_110', 'xingqing_xionghen', 'rule_rengeng_butong_huotu1', 'evi_smth_09_111', 'huotu_cai_guan_yun', 'rule_tongyun_yigui1', 'map_smth_09_073', 'map_smth_09_074']
    
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
        l1_anchor="smth_v1.0.0_六壬日庚子时_001_L1",
    )
    version: str = "1.0.0"
