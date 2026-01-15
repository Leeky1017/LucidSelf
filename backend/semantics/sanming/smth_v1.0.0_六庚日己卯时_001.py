"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339458
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
    semantic_id="smth_v1.0.0_六庚日己卯时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六庚日己卯时(SemanticEntry):
    """
    - 原文（source_text）：
  六庚日生时己卯，胎生元命发因妻。柱中有托逢庚旺，财禄丰盈福寿齐。
  庚日己卯时，胎生元命。庚金卯上受胎，见巳为生气印绶。庚以乙为财，卯有旺乙，因妻发福。若柱...
    """
    
    original_text: str = """- 原文（source_text）：
  六庚日生时己卯，胎生元命发因妻。柱中有托逢庚旺，财禄丰盈福寿齐。
  庚日己卯时，胎生元命。庚金卯上受胎，见巳为生气印绶。庚以乙为财，卯有旺乙，因妻发福。若柱旺丁，生月带禄者，贵；有倚托者，富。通生气财旺者，生财旺运者，俱贵。

- 分字分词释义：
  - **胎生元命**：庚金在卯为胎地，己土印绶生身。
  - **发因妻**：卯为乙木（财）禄地，财星得位，妻宫（财）有力。

- **规范化释义（primary_lang_explained）**：
  六庚日出生于己卯时，庚金在卯位受胎，己土正印生身。卯中乙木正财旺盛，主因妻致富或得妻财。若柱中丁火（官）旺，且生月带禄（申月），主贵。若有印比倚托，主富。通财旺之气，行财旺之运，亦贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Geng Days with Ji-Mao Hour":

  - Fetus-born original life—Geng Metal at Mao is in fetus stage; Ji Earth Direct Seal generates body; Yi Wood Direct Wealth prospers at Mao.
  - Prosperity comes through wife; if pillars have support encountering Geng prosperous, wealth and fortune abundant with blessings and longevity complete.
  - If Ding Fire Official is prosperous in pillars with month carrying fortune, indicates nobility; with support indicates wealth.
  - Key: Body weak wealth abundant requires strong body luck or parallel support to handle wealth.

- 核心要点：
  - **财印交错**：己印卯财，财印互碍（财克印），但己卯干支自合（甲己合，乙己克），此处己坐卯，受克，印力减弱。
  - **身弱财多**：庚胎于卯，身弱，需身旺运或比劫帮身，方能任财。

- 详细解说：
  此格主要看身财平衡。财在时支得禄，财气通门户。若身强，自然富贵双全，因妻得财。若身弱，反为财困，或惧内（妻管严）。己土印纶虽透，但坐卯病地（受克），生身无力，需年日支补根。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_061]` `[trigger: 胎生元命]` `[factor_trigger: taisheng_yuanming AND fa_yinqi]` `[role: 主干]` 六庚日生时己卯，胎生元命发因妻。 → 《三命通会》卷九#六庚日己卯时
  - `[ns_smth_09_062]` `[trigger: 有托庚旺]` `[factor_trigger: youtuo_gengwang AND cailu_fengying]` `[role: 主干依赖]` 柱中有托逢庚旺，财禄丰盈福寿齐。 → 《三命通会》卷九#六庚日己卯时
  - `[ns_smth_09_063]` `[trigger: 旺丁带禄]` `[factor_trigger: wang_ding_dailu AND gui]` `[role: 条件分支]` 若柱旺丁，生月带禄者，贵。 → 《三命通会》卷九#六庚日己卯时
  - `[ns_smth_09_064]` `[trigger: 有倔托富]` `[factor_trigger: you_yituo_fu AND shengcai_wangyun]` `[role: 总结]` 有倔托者，富。通生气财旺者，俱贵。 → 《三命通会》卷九#六庚日己卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六庚日己卯时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_geng', 'bazi_semantic', 'bazi_state_factor_273', 'bazi_semantic', 'bazi_relation_factor_117', 'bazi_semantic', 'bazi_state_factor_274', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_factor_122', 'bazi_semantic', 'source_ref', 'rel_smth_09_046', 'taisheng_yuanming', 'rel_smth_09_047', 'caiyin_jiaocuo', 'rel_smth_09_048', 'youtuo_shenwang', 'evi_smth_09_046', 'taisheng_yuanming', 'rule_taisheng_yuanming1', 'evi_smth_09_047', 'youtuo_shenwang', 'rule_youtuo_gengwang1', 'evi_smth_09_048', 'yinqi_fafu', 'rule_cailu_fengying1', 'map_smth_09_031', 'map_smth_09_032']
    
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
        l1_anchor="smth_v1.0.0_六庚日己卯时_001_L1",
    )
    version: str = "1.0.0"
