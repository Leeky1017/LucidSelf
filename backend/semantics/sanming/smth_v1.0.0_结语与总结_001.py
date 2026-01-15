"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264193
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
    semantic_id="smth_v1.0.0_结语与总结_001",
    book_id="sanming",
    engine_id="bazi"
)
class 结语与总结(SemanticEntry):
    """
    - **原文（source_text）**：
  以上诸条，皆命理之要法，学者当细心玩味，触类旁通。
  五行生克，变化无穷；神煞吉凶，应验有准。
  要之，以日干为主，月令为纲，岁运为用，神煞为辅。...
    """
    
    original_text: str = """- **原文（source_text）**：
  以上诸条，皆命理之要法，学者当细心玩味，触类旁通。
  五行生克，变化无穷；神煞吉凶，应验有准。
  要之，以日干为主，月令为纲，岁运为用，神煞为辅。
  明得此理，则看命无难矣。

- **核心总结**：
  本卷涵盖了看命口诀、巫咸撮要、玉井奥诀等重要赋文，是《三命通会》实战应用的核心。
  强调了**月令提纲**的重要性，**日主旺衰**的判断，**财官印食**的取用，以及**岁运神煞**的吉凶应期。
  对于**天元地元**、**三元吉凶**、**五行成象**、**纳音交互**等高阶技法也有深入论述。
  掌握这些口诀与心法，是通往命理高手的必经之路。
  看流年主要看天干（天元），看大运虽重地支，也要兼顾天干。
  月令是运元，最怕岁运冲克。八字中的官星是禄元，最怕被冲坏。财星是马元，最怕被劫夺（比劫争财）。

- 核心要点：
  - **干支体用**：干为禄（表），支为命（里）。
  - **根气为重**：地支有根方为真财官。
  - **三元**：运元（月）、禄元（官）、马元（财）。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_057]` `[trigger: 看命总纲]` `[factor_trigger: kanming_zonglun AND rigan_yuegang]` `[role: 主干]` 以日干为主，月令为纲，岁运为用，神煞为辅。明得此理，则看命无难矣。 → 《三命通会》卷十#结语与总结
  - `[ns_smth_10_058]` `[trigger: 五行无穷]` `[factor_trigger: wuxing_shengke AND bianhua_wuqiong]` `[role: 主干依赖]` 五行生克，变化无穷；神煞吉凶，应验有准。 → 《三命通会》卷十#结语与总结
  - `[ns_smth_10_059]` `[trigger: 玩味旁通]` `[factor_trigger: xixin_wanwei AND chulei_pangtong]` `[role: 条件分支]` 学者当细心玩味，触类旁通。 → 《三命通会》卷十#结语与总结
  - `[ns_smth_10_060]` `[trigger: 命理要法]` `[factor_trigger: mingli_yaofa AND zhugao_pianyao]` `[role: 总结]` 以上诸条，皆命理之要法。 → 《三命通会》卷十#结语与总结"""
    normalized_text_zh: str = """"""
    subject: str = "结语与总结"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_factor_31', 'bazi_semantic', 'bazi_factor_32', 'bazi_semantic', 'bazi_month_command_1', 'bazi_semantic', 'bazi_factor_33', 'bazi_semantic', 'bazi_factor_34', 'bazi_semantic', 'source_ref', 'rel_smth_10_025', 'kanming_cengci', 'rel_smth_10_026', 'rigan_weizhu', 'rel_smth_10_027', 'yueling_weigang', 'evi_smth_10_025', 'kanming_cengci', 'rule_kanming_cengci1', 'evi_smth_10_026', 'benben_hexin', 'rule_rigan_weizhu1', 'evi_smth_10_027', 'geju_kuangjia', 'rule_yueling_weigang1', 'map_smth_10_017', 'map_smth_10_018']
    
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
        l1_anchor="smth_v1.0.0_结语与总结_001_L1",
    )
    version: str = "1.0.0"
