"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066787
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
    semantic_id="smth_v1.0.0_2_刑冲拱夹与格局成败_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2刑冲拱夹与格局成败(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日时逢寅位，岁月怕戊己二方。
  甲子日再逢子时，畏庚辛申酉丑午。
  辛癸日多逢丑地，不喜官星；岁时逢子巳二宫，虚名虚利。
  拱禄拱贵，填实则凶。
 ...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日时逢寅位，岁月怕戊己二方。
  甲子日再逢子时，畏庚辛申酉丑午。
  辛癸日多逢丑地，不喜官星；岁时逢子巳二宫，虚名虚利。
  拱禄拱贵，填实则凶。
  时上偏财，别宫忌见。
  六辛日时逢戊子，嫌午位运喜西方。
  五行遇月支偏官，岁时中亦宜制伏。
  类有去官留煞，亦有去煞留官。四柱纯煞有制，定居一品之尊；略有一位正官，官煞混杂反贱。
  戊日午月，勿作刃看；时岁火多，却为印绶。
  月令虽逢建禄，切忌会煞为凶。
  官星七煞交差，却以合煞为贵。
  柱中官星太旺，天元羸弱之名；日干旺甚无依，若不为僧即道。

- 分字分词释义：
  - **癸日寅时**：刑合格（寅刑巳）。怕戊己（官煞填实）。
  - **甲子日子时**：子遥巳禄。怕庚辛（官煞）、申酉（填实）、丑（合绊）、午（冲）。
  - **辛癸日丑地**：丑遥巳禄。不喜官星（填实）。子巳（填实或绊）。
  - **拱禄拱贵**：虚拱。
  - **时上偏财**：时上偏财格，忌年离月有财（别宫忌见）。
  - **辛日戊子**：六阴朝阳。嫌午（冲）。
  - **戊日午月**：羊刃格，但午中丁火印绶旺，火多论印。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于甲寅时（刑合格），岁月怕见戊己官煞填实。
  甲子日出生于甲子时（子遥巳），怕庚辛申酉官煞填实，丑字合绊，午字冲破。
  辛日和癸日多逢丑地（丑遥巳），不喜见官星填实。若岁时逢子（绊丑）或巳（填实），则虚名虚利。
  拱禄格（如癸亥癸丑拱子）、拱贵格（如甲寅甲子拱丑），若填实（见子或丑）则凶。
  时上偏财格，忌年月柱再见财星（别宫忌见），否则为财多身弱或比劫争夺。
  六辛日出生于戊子时（六阴朝阳），嫌午字冲子。运喜西方金地（助身）。
  月令七煞格，岁时中也应当有制伏（食伤）。
  官煞混杂时，有去官留煞，也有去煞留官。若四柱纯是七煞且有制伏，定居一品高官。若混杂一位正官，反而贫贱（不清）。
  戊日生于午月，通常作羊刃看（午为戊刃）。但若时岁火多，午中丁火印绶强，可作印绶格看（印赖煞生）。
  月令建禄格，切忌地支会成煞局（如甲生寅月，支会巳酉丑金局），主凶。
  官煞混杂，若能合煞留官（或合官留煞），主贵。
  官星太旺而日主衰弱，名为“天元羸弱”，主贫夭。日主极旺而无财官倚托（无依），若不是僧道，也是孤独之人。

- 核心要点：
  - **虚邀格忌填实**：刑合、遥巳、拱禄、朝阳。
  - **官煞去留**：纯粹为贵。
  - **印刃之辨**：戊午月。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_039]` `[trigger: 癸日寅时]` `[factor_trigger: guiri_yinshi AND wuji_erfang]` `[role: 主干]` 六癸日时逢寅位，岁月怕戊己二方。 → 《三命通会》卷十一#刑冲拱夹与格局成败
  - `[ns_smth_11_040]` `[trigger: 拱禄拱贵]` `[factor_trigger: gonglu_gonggui AND tianshi_zexiong]` `[role: 主干依赖]` 拱禄拱贵，填实则凶。 → 《三命通会》卷十一#刑冲拱夹与格局成败
  - `[ns_smth_11_041]` `[trigger: 去官留煞]` `[factor_trigger: quguan_liusha AND chunsha_youzhi]` `[role: 条件分支]` 类有去官留煞，亦有去煞留官。四柱纯煞有制，定居一品之尊；略有一位正官，官煞混杂反贱。 → 《三命通会》卷十一#刑冲拱夹与格局成败
  - `[ns_smth_11_042]` `[trigger: 戊午印刃]` `[factor_trigger: wuri_wuyue AND huoduo_lunyin]` `[role: 条件分支]` 戊日午月，勿作刃看；时岁火多，却为印绶。 → 《三命通会》卷十一#刑冲拱夹与格局成败
  - `[ns_smth_11_043]` `[trigger: 天元羸弱]` `[factor_trigger: tianyuan_leiruo AND riganwang_wuyi]` `[role: 总结]` 柱中官星太旺，天元羸弱之名；日干旺甚无依，若不为僧即道。 → 《三命通会》卷十一#刑冲拱夹与格局成败"""
    normalized_text_zh: str = """"""
    subject: str = "2 刑冲拱夹与格局成败"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_21', 'bazi_semantic', 'bazi_state_factor_71', 'bazi_semantic', 'bazi_relation_factor_27', 'bazi_semantic', 'bazi_relation_factor_28', 'bazi_semantic', 'bazi_state_factor_72', 'bazi_semantic', 'bazi_condition_factor_21', 'bazi_semantic', 'source_ref', 'rel_smth_11_037', 'core_factor', 'rel_smth_11_038', 'cond_factor', 'rel_smth_11_039', 'risk_factor', 'evi_smth_11_037', 'core_factor', 'rule_name37', 'evi_smth_11_038', 'cond_factor', 'rule_name38', 'evi_smth_11_039', 'risk_factor', 'rule_name39', 'map_smth_11_025', 'map_smth_11_026']
    
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
        l1_anchor="smth_v1.0.0_2_刑冲拱夹与格局成败_001_L1",
    )
    version: str = "1.0.0"
