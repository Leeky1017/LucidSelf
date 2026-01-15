"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339797
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
    semantic_id="smth_v1.0.0_六壬日戊申时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日戊申时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时戊申，长生之地鬼伤身。身强制伏为高命，反此定知贫薄人。
  壬日戊申时，水土混浊。壬以戊为鬼，庚为印，申上庚金健旺，壬水长生，戊土偏官，身鬼俱强，为...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时戊申，长生之地鬼伤身。身强制伏为高命，反此定知贫薄人。
  壬日戊申时，水土混浊。壬以戊为鬼，庚为印，申上庚金健旺，壬水长生，戊土偏官，身鬼俱强，为人勇暴，若通旺月，行身旺运，有甲木制伏者贵；不通，聪明不贵，再行鬼旺运，难以显达。

- 分字分词释义：
  - **水土混浊**：壬水长生在申，戊土长生在寅（或以火土同宫，申为病地？古法水土长生同在申）。此处指申中藏壬、庚、戊，水土金混杂。
  - **身鬼俱强**：壬长生在申，戊亦长生在申（土寄生于申），煞旺身旺。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于戊申时，壬水在申长生，戊土七煞亦在申得气（或通根），身煞两强。为人勇猛暴躁。若生于身旺月，行身旺运，且有甲木食神制煞，主大贵。若不通月气，虽聪明但不贵。若行煞旺运，更难显达。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Wu-Shen Hour":

  - Long Life place Ghost hurts body—Ren Water in Shen is Long Life; Wu Earth Seven-Killing also strong; body-ghost both strong.
  - Body strong controlling-subduing makes high fate; opposite this definitely know poor thin person.
  - Water-Earth turbid mixed; person brave violent; if connecting prosperous month with Jia Wood controlling, noble; not connecting, clever but not noble.
  - Key: Body-Killing both strong needs Eating God control; otherwise brave violent difficult achieving.

- 核心要点：
  - **煞印相生**：申中庚生壬，戊生庚。
  - **身煞两停**：身旺煞旺。
  - **喜制伏**：喜甲木食神。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_177]` `[trigger: 长生鬼伤]` `[factor_trigger: changsheng_guishang AND shen_qi]` `[role: 主干]` 六壬日生时戊申，长生之地鬼伤身。 → 《三命通会》卷九#六壬日戊申时
  - `[ns_smth_09_178]` `[trigger: 身强制伏]` `[factor_trigger: shenqiang_zhifu AND wei_gaoming]` `[role: 主干依赖]` 身强制伏为高命，反此定知贫薄人。 → 《三命通会》卷九#六壬日戊申时
  - `[ns_smth_09_179]` `[trigger: 身鬼俱强]` `[factor_trigger: shengui_juqiang AND yongbao]` `[role: 条件分支]` 身鬼俱强，为人勇暴，若通旺月，有甲木制伏者贵。 → 《三命通会》卷九#六壬日戊申时
  - `[ns_smth_09_180]` `[trigger: 不通隐贵]` `[factor_trigger: butong_yingui AND xing_guiwang_yun]` `[role: 总结]` 不通，聪明不贵，再行鬼旺运，难以显达。 → 《三命通会》卷九#六壬日戊申时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日戊申时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_factor_340', 'bazi_semantic', 'bazi_relation_water_earth', 'bazi_semantic', 'bazi_state_factor_341', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_jia_wood_1', 'bazi_semantic', 'source_ref', 'rel_smth_09_133', 'shensha_juqi', 'rel_smth_09_134', 'shensha_juqi', 'rel_smth_09_135', 'shensha_juqi', 'evi_smth_09_133', 'shensha_juqi', 'rule_shensha_juqi1', 'evi_smth_09_134', 'gaoming', 'rule_gaoming_shensha1', 'evi_smth_09_135', 'pinbo_ren', 'rule_pinbo_ren1', 'map_smth_09_089', 'map_smth_09_090']
    
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
        l1_anchor="smth_v1.0.0_六壬日戊申时_001_L1",
    )
    version: str = "1.0.0"
