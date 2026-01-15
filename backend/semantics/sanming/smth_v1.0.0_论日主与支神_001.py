"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264253
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
    semantic_id="smth_v1.0.0_论日主与支神_001",
    book_id="sanming",
    engine_id="bazi"
)
class 论日主与支神(SemanticEntry):
    """
    - 原文（source_text）：
  凡推究造化之理，其法以日为主。单提作体，要认为主者之端，为化气，为本体。入门便要通变，识得主干有本象、有化象，方可消详。如甲即本象是木，化象是土。
  坐下支...
    """
    
    original_text: str = """- 原文（source_text）：
  凡推究造化之理，其法以日为主。单提作体，要认为主者之端，为化气，为本体。入门便要通变，识得主干有本象、有化象，方可消详。如甲即本象是木，化象是土。
  坐下支神，先求其意。乃日干坐下，首先看此地支，与月支一位、时支一位、年支一位，刑冲破害、生克比和何如？主干喜忌何物？得来不可视为泛常，不可顾盼。
  月气浅深，何者主权。月建之下，气候浅深，五行之气，是何干神正当此日天时之令？五日一候之气。一云德秀有无。
  地支至切，党盛为强。地支乃四位支神，至切者，视天干为尤切也。要看何者为主干之宅舍？何者为用神之基业？何者力轻？何者力重？宅舍即得地之方，基业即乘贵之所。

- 分字分词释义：
  - **以日为主**：子平法核心，日干代表命主。
  - **本象化象**：日干五行（本象）与合化五行（化象）。
  - **坐下支神**：日支，离日主最近，关系最切。
  - **党盛为强**：地支会局、成方，力量最强。

- **规范化释义（primary_lang_explained）**：
  推命之法，以日干为主。首先要辨明日干是看本气五行，还是看化气五行。
  其次要看日支，日支与年月时支的关系（刑冲破害合）如何，对日主是喜是忌，这是关键，不可忽视。
  再看月令，月令中哪一个藏干当令司权（如寅月，立春后七日戊土，次七日丙火，后十六日甲木）。
  地支的力量比天干更切实际。要看地支中哪个五行结党成势，哪个是日主的根基（宅舍），哪个是用神的根基（基业）。

- 核心要点：
  - **日主为尊**：分本体与化气。
  - **日支关键**：日支与他支关系。
  - **月令深浅**：人元司事。
  - **地支结党**：地支局势决定强弱。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_053]` `[trigger: 以日为主]` `[factor_trigger: yiri_weizhu AND benti_huaxiang]` `[role: 主干]` 凡推究造化之理，其法以日为主。单提作体，要认为主者之端。 → 《三命通会》卷十#论日主与支神
  - `[ns_smth_10_054]` `[trigger: 坐下支神]` `[factor_trigger: zuoxia_zhishen AND xianqiu_qiyi]` `[role: 主干依赖]` 坐下支神，先求其意。乃日干坐下，首先看此地支。 → 《三命通会》卷十#论日主与支神
  - `[ns_smth_10_055]` `[trigger: 月气浅深]` `[factor_trigger: yueqi_qianshen AND hezhe_zhuquan]` `[role: 条件分支]` 月气浅深，何者主权。月建之下，气候浅深，五行之气，是何干神正当此日天时之令？ → 《三命通会》卷十#论日主与支神
  - `[ns_smth_10_056]` `[trigger: 党盛为强]` `[factor_trigger: dangsheng_weiqiang AND dizhi_zhiqie]` `[role: 总结]` 地支至切，党盛为强。地支乃四位支神，至切者，视天干为尤切也。 → 《三命通会》卷十#论日主与支神"""
    normalized_text_zh: str = """"""
    subject: str = "论日主与支神"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_day_master', 'bazi_semantic', 'bazi_relation_factor_106', 'bazi_semantic', 'bazi_condition_factor_103', 'bazi_semantic', 'bazi_state_factor_237', 'bazi_semantic', 'bazi_factor_35', 'bazi_semantic', 'source_ref', 'rel_smth_10_043', 'rizhu_weizhu', 'rel_smth_10_044', 'dangsheng_weiqiang', 'rel_smth_10_045', 'yueqi_qianshen', 'evi_smth_10_043', 'rizhu_weizhu', 'rule_rizhu_weizhu1', 'evi_smth_10_044', 'dangsheng_weiqiang', 'rule_dangsheng_weiqiang1', 'evi_smth_10_045', 'renyuan_siling', 'rule_yueqi_qianshen1', 'map_smth_10_029', 'map_smth_10_030']
    
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
        l1_anchor="smth_v1.0.0_论日主与支神_001_L1",
    )
    version: str = "1.0.0"
