"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412757
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
    semantic_id="smth_v1.0.0_倒食_枭神_与食神反噬_001",
    book_id="sanming",
    engine_id="bazi"
)
class 倒食枭神与食神反噬(SemanticEntry):
    """
    - **原文（source_text）**：

  论倒食：倒食即偏印之谓，一名吞啖煞。食神最忌见之。如甲生丙火为食，火能生土，为甲之财，财旺生金，为甲之官。食神生旺，财官备矣。今甲见壬为倒食者，壬旺...
    """
    
    original_text: str = """- **原文（source_text）**：

  论倒食：倒食即偏印之谓，一名吞啖煞。食神最忌见之。如甲生丙火为食，火能生土，为甲之财，财旺生金，为甲之官。食神生旺，财官备矣。今甲见壬为倒食者，壬旺则克了丙火，丙被克去，不能生土，甲无财矣；壬合起丁，伤甲之辛，甲无官矣；壬克去丙，庚煞得安，来伤甲木，甲生灾矣。所谓“用食忌见者”，此也。凡命带倒食，福薄寿夭。若有制合，如甲日见壬辰、壬戌，辰戌中带有土制丁合；乙日见癸未、癸丑，丑未中有己制癸；丙日见甲申，丁日见乙巳、乙酉；戊日见丙子、丙申、丙辰；己日见丁亥；庚日见戊寅、戊辰；辛日见己卯、己亥；壬日见庚午、庚戌；癸日见辛巳、辛未，此等偏印不能为食害，有克制故也。柱中身旺，财官俱生，可取为福助身。阳日逢之，能暗合伤官生财；阴日逢之，能暗合财星。柱中无食，只以偏印论。又曰：凡命有食遇枭，犹尊长之制我，不得自由，作事进退悔懒，有始无终，财源屡成屡败，容貌欹斜，身品琐小，胆怯心虚，凡事无成，克害六亲。幼时克母，长大伤妻子。《赋》云：倒食者，名为偏印，号曰枭神，值身旺而财丰福厚，遇刑煞则寿夭身贫，财星若见，披星带月不停留；煞星若生，驰担息肩无定日。身弱重逢偏印，须愁颜子之伤；正食若遇枭神，未免韩信之祸。始遇者精神慵懒，重犯者容貌欹斜。《万祺赋》云：枭神见官煞，多成多败；偏印遇财曜，反辱为荣。身旺为贵，身弱乃常。有伤官而平生丰润，值食神则处世伶仃。古诗云：印星偏者是枭神，柱内最喜见财星，身旺遇此方为福，身衰枭旺更无情。

- 分字分词释义：

  - **倒食 / 枭神**：偏印在与食神同见时，对食神形成“反噬”，使原本有利的食神转为不利。
  - **用食忌见者**：以食神为用的格局最忌枭神来克食。
  - **有制合则不为害**：若偏印又被土、合等力量所制，则其害减轻甚至转为助力。

- **规范化释义（primary_lang_explained）**：

  倒食讲的是一种“反向夺食”的机制：本应由我所生的食神带来才华、饮食、子女与财源，但偏印（枭神）出现时，却不断克制食神，使：

  - 才华难以发挥；
  - 财源屡成屡败；
  - 与长辈、上级关系易紧张；
  - 在亲情上有“养而不亲”或“恩深缘浅”的体验。

- 核心要点：

  - 以食神为用者，最忌偏印多而强；
  - 若有恰当制合，偏印不必皆凶，反可在一定条件下护身、制煞；
  - 判断时需详看日干阴阳、食神位置与偏印强弱。

- 详细解说：

  现代实践中，枭神重而食神弱者，常见：

  - 学有专长却屡屡中断、难以坚持；
  - 工作上有想法却难以持续执行；
  - 对饮食与健康不甚节制，易有过劳与能量波动。

  若行运得当、制合得宜，则枭神可转为“冷静、审慎、深思”的一面，反而弥补纯食神的过于松散。

- **校勘与字词辨析（双语）**：

  - 关于“克母伤妻子”等说法，本稿以“对女性亲属的关系压力较大”理解，不以此作单线因果断语。
  - **English**：
    - Avoids simple linear cause-effect pronouncements.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_157]` `[trigger: 倒食枭神]` `[factor_trigger: daoshi_presence AND tundan_sha]` `[role: 主干]` 倒食即偏印之谓，一名吞啤煚。食神最忌见之。 → 《三命通会》卷六#论倒食
  - `[ns_smth_06_158]` `[trigger: 用食忌见]` `[factor_trigger: shishen_weiyong AND ji_jian_xiao]` `[role: 主干依赖]` 用食忌见者，壬旺则克了丙火，甲无财、无官、生灾矣。 → 《三命通会》卷六#论倒食
  - `[ns_smth_06_159]` `[trigger: 制合无害]` `[factor_trigger: youtu_zhi OR you_he]` `[role: 条件分支]` 若有制合，此等偏印不能为食害，有克制故也。 → 《三命通会》卷六#论倒食
  - `[ns_smth_06_160]` `[trigger: 身旺无食]` `[factor_trigger: shenwang AND wushi_zhiyinlun]` `[role: 总结]` 柱中无食，只以偏印论。身旺为贵，身弱乃常。 → 《三命通会》卷六#论倒食"""
    normalized_text_zh: str = """"""
    subject: str = "倒食（枭神）与食神反噬"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_41', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_strength_7', 'bazi_semantic', 'bazi_state_degree_29', 'bazi_semantic', 'bazi_condition_shishen_1', 'bazi_semantic', 'bazi_condition_condition_2', 'bazi_semantic', 'source_ref', 'rel_smth_06_145', 'daoshi_ge_presence', 'rel_smth_06_146', 'xiaoshen_qiangdu', 'rel_smth_06_147', 'shishen_beike_risk', 'evi_smth_06_145', 'daoshi_ge_presence', 'rule_daoshi', 'evi_smth_06_146', 'xiaoshen_qiangdu', 'rule_duoshi', 'evi_smth_06_147', 'shenwang_wushi', 'rule_wuhai', 'map_smth_06_097', 'map_smth_06_098']
    
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
        l1_anchor="smth_v1.0.0_倒食_枭神_与食神反噬_001_L1",
    )
    version: str = "1.0.0"
