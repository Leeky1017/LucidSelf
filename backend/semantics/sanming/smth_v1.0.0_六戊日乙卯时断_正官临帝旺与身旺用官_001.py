"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157720
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
    semantic_id="smth_v1.0.0_六戊日乙卯时断_正官临帝旺与身旺用官_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日乙卯时断正官临帝旺与身旺用官(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日乙卯时断。

  六戊日生时乙卯，正官临帝喜身强；月通身旺官有气，文章显达贵非常。戊日乙卯时，正官临帝旺，乙木正官在卯为帝旺，若通身旺月，官有气，文章...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日乙卯时断。

  六戊日生时乙卯，正官临帝喜身强；月通身旺官有气，文章显达贵非常。戊日乙卯时，正官临帝旺，乙木正官在卯为帝旺，若通身旺月，官有气，文章显达，大贵。身弱官旺，平常。

  戊子日乙卯时，子卯相刑，伤妻害子。春官旺，行南运，贵。夏身旺，吉。

  戊寅日乙卯时，寅卯相并，官旺。春官旺，行南运，贵。夏身旺，吉。

  戊辰日乙卯时，卯辰暗合，春官旺，行南运，贵。辰戌丑未月，杂气官星，大贵。

  戊午日乙卯时，卯午相破，伤妻害子。春官旺，行南运，贵。夏身旺，吉。

  戊申日乙卯时，春官旺，行南运，贵。秋财旺，行官运，贵。

  戊戌日乙卯时，卯戌合，合官。春官旺，行南运，大贵。辰戌丑未月，杂气官星，大贵。

  戊日乙卯时上逢，正官临帝喜身强；月通身旺官有气，文章显达贵非常。戊日乙卯时准，正官帝旺相逢。若然身旺福无边，定主文章贵显。

- 分字分词释义：

  - **正官临帝旺**：乙木正官在卯为帝旺，官星极旺。
  - **文章显达**：主文学才华出众，适合科举仕途。
  - **身旺用官**：日主身旺方能驾驭官星为用。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，乙卯时」：

  - 乙木正官在卯为帝旺，官星极旺；若通身旺月，官有气，文章显达，大贵；
  - 身弱官旺，则难以驾驭，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Yi-Mao Hour":

  - Yi Wood Direct Official at Mao is at emperor-prosperity—official star extremely strong; if connected with strong-body month, official has qi—literary prominence achieves great nobility.
  - If body is weak with prosperous official, unable to control—ordinary livelihood.

- 核心要点：

  - 本格以「正官临帝旺」为核心，官星极旺。
  - 身旺用官是关键，方能发挥官星优势。
  - 主文章显达，适合从事文职或仕途。

- 详细解说：

  1. **正官临帝旺的优势**  
     - 卯上乙木正官帝旺，官星有力；  
     - 正官主正统、规范，适合文职。

  2. **身旺用官的必要性**  
     - 身旺方能用官，身弱官旺反受压制；  
     - 需要月令通火土之气。

- 校勘与字词辨析：

  - 「贵非常」形容显贵非凡。
  - 「文章贵显」形容文学仕途显达。
  - **English**：
    - Describes prominence in literary and official career.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_205]` `[trigger: 正官临帝]` `[factor_trigger: zhengguan_lindi AND xi_shenqiang]` `[role: 主干]` 六戊日生时乙卯，正官临帝喜身强。 → 《三命通会》卷八#六戊日乙卯时
  - `[ns_smth_08_206]` `[trigger: 官有气]` `[factor_trigger: guan_youqi AND wenzhang_xianda]` `[role: 主干依赖]` 月通身旺官有气，文章显达贵非常。 → 《三命通会》卷八#六戊日乙卯时
  - `[ns_smth_08_207]` `[trigger: 身弱官旺]` `[factor_trigger: shenruo_guanwang AND ping_chang]` `[role: 条件分支]` 身弱官旺，平常。 → 《三命通会》卷八#六戊日乙卯时
  - `[ns_smth_08_208]` `[trigger: 文章贵显]` `[factor_trigger: wenzhang_guixian AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主文章贵显。 → 《三命通会》卷八#六戊日乙卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日乙卯时断：正官临帝旺与身旺用官"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_zhenguan', 'bazi_semantic', 'bazi_relation_factor_94', 'bazi_semantic', 'bazi_state_factor_208', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_154', 'zhengguan_lindiwang', 'rel_smth_08_155', 'shenwang_yongguan', 'rel_smth_08_156', 'tongshenwang_yue', 'evi_smth_08_154', 'zhengguan_lindiwang', 'rule_diwang4', 'evi_smth_08_155', 'shenwang_yongguan', 'rule_yongguan', 'evi_smth_08_156', 'wenzhang_xianda', 'rule_xianda', 'map_smth_08_103', 'map_smth_08_104']
    
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
        l1_anchor="smth_v1.0.0_六戊日乙卯时断_正官临帝旺与身旺用官_001_L1",
    )
    version: str = "1.0.0"
