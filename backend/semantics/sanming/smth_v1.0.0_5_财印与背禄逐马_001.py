"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066880
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
    semantic_id="smth_v1.0.0_5_财印与背禄逐马_001",
    book_id="sanming",
    engine_id="bazi"
)
class 5财印与背禄逐马(SemanticEntry):
    """
    - **原文（source_text）**：
  印绶生月，岁时忌见财星；运入财乡，却宜退身避位。
  劫财阳刃，切忌时逢；岁运并临，灾殃立至。
  十干背禄，岁时喜见财星；运至比肩，号曰背禄逐马。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  印绶生月，岁时忌见财星；运入财乡，却宜退身避位。
  劫财阳刃，切忌时逢；岁运并临，灾殃立至。
  十干背禄，岁时喜见财星；运至比肩，号曰背禄逐马。
  五行正贵，忌冲刑克破之宫。
  四柱干支，喜三合六合之地。
  日干无气，时逢阳刃不为凶。
  官煞两停，喜者存之，憎者弃之。
  地支天干合多，亦云贪合忘官。

- **分字分词释义**：
  - **印绶生月**：月令印格。
  - **退身避位**：辞官归隐（避灾）。
  - **背禄**：伤官（伤尽官星为背禄）。
  - **逐马**：比劫夺财。
  - **日干无气**：身弱。
  - **贪合忘官**：合多羁绊，不顾官星（事业）。

- **白话原意**：
  月令印绶格，岁运和时柱忌见财星（财坏印）。若行运进入财乡，应该退身避位，否则有灾。
  劫财阳刃，最忌在时柱遇到（晚年不保或子息亦伤）。若岁运再遇羊刃，灾殃立至。
  十干背禄（伤官格），岁运喜见财星（伤官生财）。若运到比肩之地，比肩劫财，这叫“背禄逐马”（伤官背禄，比劫逐马），主贫困。
  五行正贵（正官、贵人），忌讳在刑冲克破的宫位。
  四柱干支，喜欢三合六合（有情、团结）。
  日干无气（身弱），时柱遇到阳刃（如甲日卯时），不作凶论（刃能帮身）。
  官煞两停（混杂），喜欢的保留，憎恶的去掉（去留舒配）。
  干支合多，也叫“贪合忘官”，主玩物丧志，不求上进。

- **核心要点**：
  - **印格忌财**：运入财乡凶。
  - **伤官喜财**：背禄逐马凶。
  - **身弱喜刃**：刃能帮身。
  - **合多失志**：贪合忘官。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_075]` `[trigger: 印忌财]` `[factor_trigger: yin_jicai AND tuishen_biwei]` `[role: 主干]` 印绶生月，岁时忌见财星；运入财乡，却宜退身避位。 → 《三命通会》卷十一#财印与背禄逐马
  - `[ns_smth_11_076]` `[trigger: 背禄逐马]` `[factor_trigger: beilu_zhuma AND bijian_duocai]` `[role: 主干依赖]` 十干背禄，岁时喜见财星；运至比肩，号曰背禄逐马。 → 《三命通会》卷十一#财印与背禄逐马
  - `[ns_smth_11_077]` `[trigger: 身弱喜刃]` `[factor_trigger: shenruo_xiren AND rigan_wuqi]` `[role: 条件分支]` 日干无气，时逢阳刃不为凶。 → 《三命通会》卷十一#财印与背禄逐马
  - `[ns_smth_11_078]` `[trigger: 贪合忘官]` `[factor_trigger: tanhe_wangguan AND heduo_shizhi]` `[role: 总结]` 地支天干合多，亦云贪合忘官。 → 《三命通会》卷十一#财印与背禄逐马"""
    normalized_text_zh: str = """"""
    subject: str = "5 财印与背禄逐马"
    factor_refs: list = ['engine_id', 'bazi_relation_factor_29', 'bazi_semantic', 'bazi_relation_shangguan_1', 'bazi_semantic', 'bazi_state_factor_148', 'bazi_semantic', 'bazi_state_factor_83', 'bazi_semantic', 'bazi_state_factor_84', 'bazi_semantic', 'bazi_condition_factor_22', 'bazi_semantic', 'source_ref', 'rel_smth_11_064', 'core_factor', 'rel_smth_11_065', 'cond_factor', 'rel_smth_11_066', 'risk_factor', 'evi_smth_11_064', 'core_factor', 'rule_name64', 'evi_smth_11_065', 'cond_factor', 'rule_name65', 'evi_smth_11_066', 'risk_factor', 'rule_name66', 'map_smth_11_043', 'map_smth_11_044']
    
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
        l1_anchor="smth_v1.0.0_5_财印与背禄逐马_001_L1",
    )
    version: str = "1.0.0"
