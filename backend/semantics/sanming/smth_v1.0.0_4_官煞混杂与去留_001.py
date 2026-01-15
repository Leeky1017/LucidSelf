"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066870
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
    semantic_id="smth_v1.0.0_4_官煞混杂与去留_001",
    book_id="sanming",
    engine_id="bazi"
)
class 4官煞混杂与去留(SemanticEntry):
    """
    - **原文（source_text）**：
  类有去官留煞，亦有去煞留官。四柱纯煞，有制，定居一品之尊；略有一位正官，官煞混杂反贱。
  戊日午月，勿作刃看；时岁火多，却为印绶。
  月令虽逢建禄...
    """
    
    original_text: str = """- **原文（source_text）**：
  类有去官留煞，亦有去煞留官。四柱纯煞，有制，定居一品之尊；略有一位正官，官煞混杂反贱。
  戊日午月，勿作刃看；时岁火多，却为印绶。
  月令虽逢建禄，切忌会煞为凶。
  官星七煞交差，却以合煞为贵。
  柱中官星太旺，天元羸弱之名。
  日干旺甚无依，若不为僧即道。

- **分字分词释义**：
  - **去留**：食伤制煞留官，或合煞留官，或合官留煞。
  - **纯煞有制**：七煞格，煞旺身强有制。
  - **戊日午月**：午为戊之羊刃，亦为印绶（丁火）。
  - **会煞**：建禄格见七煞成局（身强煞旺，若无制则凶）。
  - **交差**：混杂。
  - **无依**：无财官印食可依。

- **白话原意**：
  命局中有“去官留煞”或“去煞留官”的情况。若四柱纯是七煞，且有制伏（食神），定主一品高官。但若混杂了一位正官，这就叫官煞混杂，反主贫贱（不清）。
  戊日生于午月，午虽是羊刃，但午中丁火是印绶，若岁时火多，可作印绶格看（杀印相生或印赖杀生）。
  月令虽然是建禄（身旺），但切忌地支会成七煞局（身强煞旺无制），主凶。
  官星七煞混杂（交差），若能合去七煞（或合官），取清为贵。
  柱中官星太旺（多），日主衰弱，这叫“天元羸弱”，主贫贱或夭折。
  日干极旺，而四柱无财官印食可依（满盘比劫印绶），若不为僧道，也是孤独之人。

- **核心要点**：
  - **官煞取清**：混杂必去一留一。
  - **纯煞有制**：大贵之格。
  - **旺衰极端**：太旺无依、太弱受克皆凶。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_071]` `[trigger: 去官留煞]` `[factor_trigger: quguan_liusha AND chunsha_youzhi]` `[role: 主干]` 类有去官留煞，亦有去煞留官。四柱纯煞，有制，定居一品之尊。 → 《三命通会》卷十一#官煞混杂与去留
  - `[ns_smth_11_072]` `[trigger: 官煞混杂]` `[factor_trigger: guansha_hunza AND fanjian]` `[role: 主干依赖]` 略有一位正官，官煞混杂反贱。 → 《三命通会》卷十一#官煞混杂与去留
  - `[ns_smth_11_073]` `[trigger: 戊午印刃]` `[factor_trigger: wuri_wuyue AND huoduo_yinshou]` `[role: 条件分支]` 戊日午月，勿作刃看；时岁火多，却为印绶。 → 《三命通会》卷十一#官煞混杂与去留
  - `[ns_smth_11_074]` `[trigger: 旺衰极端]` `[factor_trigger: wangshuai_jiduan AND sengdao_gudu]` `[role: 总结]` 柱中官星太旺，天元羸弱之名。日干旺甚无依，若不为僧即道。 → 《三命通会》卷十一#官煞混杂与去留"""
    normalized_text_zh: str = """"""
    subject: str = "4 官煞混杂与去留"
    factor_refs: list = ['engine_id', 'bazi_relation_factor_27', 'bazi_semantic', 'bazi_relation_factor_28', 'bazi_semantic', 'bazi_state_factor_227', 'bazi_semantic', 'bazi_state_factor_80', 'bazi_semantic', 'bazi_state_factor_81', 'bazi_semantic', 'bazi_condition_factor_21', 'bazi_semantic', 'source_ref', 'rel_smth_11_061', 'core_factor', 'rel_smth_11_062', 'cond_factor', 'rel_smth_11_063', 'risk_factor', 'evi_smth_11_061', 'core_factor', 'rule_name61', 'evi_smth_11_062', 'cond_factor', 'rule_name62', 'evi_smth_11_063', 'risk_factor', 'rule_name63', 'map_smth_11_041', 'map_smth_11_042']
    
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
        l1_anchor="smth_v1.0.0_4_官煞混杂与去留_001_L1",
    )
    version: str = "1.0.0"
