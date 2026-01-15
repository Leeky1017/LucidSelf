"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739936
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
    semantic_id="zw_v1.0.0_批富命_财宫武曲旺格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批富命财宫武曲旺格(SemanticEntry):
    """
    - 分字分词释义：

  - **财宫武曲旺**：武曲星在财宫庙旺，主财源丰厚。
  - **富而不贵**：命无贵格但财宫得力，富商而非官嬦。
  - **刚不吐柔不茹**：刚柔并济、不偏不债的处世态...
    """
    
    original_text: str = """- 分字分词释义：

  - **财宫武曲旺**：武曲星在财宫庙旺，主财源丰厚。
  - **富而不贵**：命无贵格但财宫得力，富商而非官嬦。
  - **刚不吐柔不茹**：刚柔并济、不偏不债的处世态度。
  - **到底期君富必盈**：虽无官禄但期待财富必定充盈。
  - **辅彼星尊人慷慨**：得辅彼拱照之人性情慷慨豪爆。
  - **富厉家肥定莫量**：晚发大富，家业丰厚无法估量。
  - **君子小人泾渭明**：富命之人待人沾渭分明，不谄不骄。

- **原文（source_text）**：  
  当初人许位公卿，此格推来却不真。命垣星曜虽庙旺，三方杀合少祥祯。更无被克无生化，故知无分夺功名。格取左右同宫是，无冲无破妙堪评。独喜财宫武曲旺，到底期君富必盈。辅弼星尊人慷慨，豪气无骄谄谀心。主心天机忧疑大，身送心劳却未宁。性稳傲又慈心，待人以礼少骄矜。刚不吐兮柔不茹，似石之介；澄不清兮桡不浊，如水之平。懒随倍子炎凉辈，自有汪洋亚圣心。指背三分应莫免，盖因三合有凶星。破军杀守忧刑重，庄卜难兑鼓盆声。财犯天空才得失，田宫地劫不宽庄。田财二主加关美，化曜居临富橐囊。到头才发无凶耗，富厚家肥定莫量。

- **规范化释义（primary_lang_explained）**：  
  此为批断「命格不贵但财宫武曲旺」富命的标准套语。开篇直言：此命虽有人许为公卿（贵命），但推断不真，命宫虽庙旺却三方杀会、少吉祯，无缘功名仕途。然而套语笔锋一转，独喜财宫武曲旺守，「到底期君富必盈」。此后论述命主性情（慷慨豪气、刚柔并济）、六亲宫位、限运吉凶，以及晚年享福。此套语适用于无官却巨富的命格。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the "No Nobility but Wealth Palace Wu Qu Prosperous" pattern. Opening with candor: though some predict noble rank, the analysis proves otherwise—Life Palace though dignified has malefics in three-harmony lacking auspice, no share in official career. However, the template pivots: uniquely fortunate that Wealth Palace has Wu Qu in prosperity, "ultimately expecting you to be filled with riches". Subsequently discussing temperament (generous spirit, balanced firmness and gentleness), Six Relations, period fortunes, and late-life enjoyment.

- **核心要点**：  
  1. 命格定位：命宫无贵格，但财宫武曲庙旺主富。  
  2. 性情特征：慷慨豪气、刚柔并济、不谄不骄。  
  3. 富命特征：「到底期君富必盈」。"""
    normalized_text_zh: str = """"""
    subject: str = "批富命·财宫武曲旺格"
    factor_refs: list = ['star_wuqu_caigong_wang', 'trait_fu_er_bugui', 'trait_gangrou_bingji', 'symbol_fu_tuonang', 'symbol_qijun_fubiying', 'source_ref', 'rel_vol7_11_001', 'star_wuqu_caigong_wang', 'rel_vol7_11_002', 'trait_gangrou_bingji', 'rel_vol7_11_003', 'result_wuqu_fuming', 'evi_vol7_11_001', 'rule_wuqu_caigong_fuerbugui', 'evi_vol7_11_002', 'trait_gangrou_bingji', 'rule_gangrou_bingji_trait', 'evi_vol7_11_003', 'symbol_fu_tuonang', 'rule_wanfa_dafu', 'concept_wealth_not_nobility', 'concept_balanced_temperament', 'concept_late_wealth']
    
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
        l1_anchor="zw_v1.0.0_批富命_财宫武曲旺格_001_L1",
    )
    version: str = "1.0.0"
