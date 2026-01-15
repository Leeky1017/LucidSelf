"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157711
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
    semantic_id="smth_v1.0.0_六戊日甲寅时断_七煞临官与身旺制煞_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日甲寅时断七煞临官与身旺制煞(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日甲寅时断。

  六戊日生时甲寅，七煞临官喜身强；月通身旺煞有制，武职权贵福禄昌。戊日甲寅时，七煞临官，甲木七煞在寅为建禄，若通身旺月，煞有制伏，武职...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日甲寅时断。

  六戊日生时甲寅，七煞临官喜身强；月通身旺煞有制，武职权贵福禄昌。戊日甲寅时，七煞临官，甲木七煞在寅为建禄，若通身旺月，煞有制伏，武职权贵，大贵。身弱煞旺，平常。

  戊子日甲寅时，寅为长生，身旺制煞，贵。申子辰月，官旺，行南运，贵。

  戊寅日甲寅时，两寅相并，身煞两旺。春煞旺，行南运，贵。夏身旺，吉。

  戊辰日甲寅时，身旺制煞，贵。寅卯月，煞旺有制，大贵。

  戊午日甲寅时，寅午半合，身旺制煞，大贵。春煞旺，行南运，贵。

  戊申日甲寅时，寅申相冲，伤妻害子。春煞旺，行南运，贵。夏身旺，吉。

  戊戌日甲寅时，寅午戌月，身旺制煞，大贵。春煞旺，有制，贵。

  戊日甲寅时上逢，七煞临官喜身强；月通身旺煞有制，武职权贵福禄昌。戊日甲寅时准，七煞临官相逢。若然身旺福无边，定主武职权贵。

- 分字分词释义：

  - **七煞临官**：甲木七煞在寅为建禄，煞星得令。
  - **身旺制煞**：日主身旺可以制伏七煞，化险为夷。
  - **武职权贵**：主武职官职，有权威之象。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，甲寅时」：

  - 甲木七煞在寅为建禄，煞星得令；若通身旺月，煞有制伏，武职权贵，大贵；
  - 身弱煞旺，则难以驾驭，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Jia-Yin Hour":

  - Jia Wood Seven-Killing at Yin is at establishment—killing star in season; if connected with strong-body month, killing has control—military-official authority achieves great nobility.
  - If body is weak with prosperous killing, unable to control—ordinary livelihood.

- 核心要点：

  - 本格以「七煞临官」为核心，煞星有力。
  - 身旺制煞是关键，方能化险为夷。
  - 主武职权贵，适合从事军政工作。

- 详细解说：

  1. **七煞临官的特点**  
     - 寅上甲木七煞得禄，煞星有力；  
     - 七煞主权威、执行力，适合武职。

  2. **身旺制煞的优势**  
     - 若身旺，可驾驭七煞为权威；  
     - 形成「身旺用煞」的结构，可成就大贵。

- 校勘与字词辨析：

  - 「福禄昌」形容福禄兴旺。
  - 「武职权贵」形容军政官职、有权势。
  - **English**：
    - Describes military-political office with authority.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_201]` `[trigger: 七煞临官]` `[factor_trigger: qisha_linguan AND xi_shenqiang]` `[role: 主干]` 六戊日生时甲寅，七煞临官喜身强。 → 《三命通会》卷八#六戊日甲寅时
  - `[ns_smth_08_202]` `[trigger: 煞有制]` `[factor_trigger: sha_youzhi AND wuzhi_quangui]` `[role: 主干依赖]` 月通身旺煞有制，武职权贵福禄昌。 → 《三命通会》卷八#六戊日甲寅时
  - `[ns_smth_08_203]` `[trigger: 身弱煞旺]` `[factor_trigger: shenruo_shawang AND ping_chang]` `[role: 条件分支]` 身弱煞旺，平常。 → 《三命通会》卷八#六戊日甲寅时
  - `[ns_smth_08_204]` `[trigger: 武职权贵]` `[factor_trigger: wuzhi_quangui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主武职权贵。 → 《三命通会》卷八#六戊日甲寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日甲寅时断：七煞临官与身旺制煞"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_factor_206', 'bazi_semantic', 'bazi_condition_factor_43', 'bazi_semantic', 'bazi_state_factor_207', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_151', 'qisha_linguan', 'rel_smth_08_152', 'shenwang_zhisha', 'rel_smth_08_153', 'tongshenwang_yue', 'evi_smth_08_151', 'qisha_linguan', 'rule_qishalinguan', 'evi_smth_08_152', 'shenwang_zhisha', 'rule_zhisha2', 'evi_smth_08_153', 'wuzhi_quangui', 'rule_wuzhi', 'map_smth_08_101', 'map_smth_08_102']
    
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
        l1_anchor="smth_v1.0.0_六戊日甲寅时断_七煞临官与身旺制煞_001_L1",
    )
    version: str = "1.0.0"
