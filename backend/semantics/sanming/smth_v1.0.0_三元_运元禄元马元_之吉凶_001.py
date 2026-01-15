"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264171
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
    semantic_id="smth_v1.0.0_三元_运元禄元马元_之吉凶_001",
    book_id="sanming",
    engine_id="bazi"
)
class 三元运元禄元马元之吉凶(SemanticEntry):
    """
    - **原文（source_text）**：
  人命以当生之月为运元，最怕大运并岁君来冲，为祸。
  以当生官星为禄元，最怕冲坏。如丁日生人以壬为官，而生亥月，亥中有壬是丁之禄；若年与时有巳字，则冲...
    """
    
    original_text: str = """- **原文（source_text）**：
  人命以当生之月为运元，最怕大运并岁君来冲，为祸。
  以当生官星为禄元，最怕冲坏。如丁日生人以壬为官，而生亥月，亥中有壬是丁之禄；若年与时有巳字，则冲坏禄元。
  以当生财星为马元，最怕劫夺。如庚日生人以甲乙木为财，而生寅卯月，寅中甲木偏财，卯中乙木正财；若年时有辛字，却有争夺之患。岁运同论。

- **分字分词释义**：
  - **运元**：月令提纲，大运所从出。
  - **禄元**：正官星（官禄）。
  - **马元**：财星（财马）。
  - **冲坏/劫夺**：冲月令为冲运元；冲官星为冲禄元；劫财克财为夺马元。

- **白话原意**：
  人的命局中，以出生之月为“运元”（大运发端），最怕大运和流年来冲月令，主大祸（冲提纲）。
  以命局中的官星为“禄元”，最怕被刑冲破害。例如丁火日主以壬水为官，生在亥月（亥中藏壬），亥即是禄元；如果年支或时支有巳火来冲亥水，就冲坏了禄元。
  以命局中的财星为“马元”，最怕被比劫劫夺。例如庚金日主以甲乙木为财，生在寅卯月（木旺），寅卯即是马元；如果年干或时干透出辛金（劫财）来克制，就有争夺破财之患。岁运遇到冲官劫财的情况，论法相同。

- **核心要点**：
  - **三元**：运元（月）、禄元（官）、马元（财）。
  - **忌讳**：运元怕冲，禄元怕冲，马元怕劫。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_021]` `[trigger: 运元怕冲]` `[factor_trigger: yunyuan_pachong AND dayun_suijun]` `[role: 主干]` 人命以当生之月为运元，最怕大运并岁君来冲，为祸。 → 《三命通会》卷十#三元之吉凶
  - `[ns_smth_10_022]` `[trigger: 禄元怕冲]` `[factor_trigger: luyuan_pachong AND guanxing_chonghuai]` `[role: 主干依赖]` 以当生官星为禄元，最怕冲坏。 → 《三命通会》卷十#三元之吉凶
  - `[ns_smth_10_023]` `[trigger: 马元怕劫]` `[factor_trigger: mayuan_pajie AND caixin_duoduo]` `[role: 条件分支]` 以当生财星为马元，最怕劫夺。 → 《三命通会》卷十#三元之吉凶
  - `[ns_smth_10_024]` `[trigger: 岁运同论]` `[factor_trigger: suiyun_tonglun AND sanyuan_baohu]` `[role: 总结]` 岁运同论。 → 《三命通会》卷十#三元之吉凶"""
    normalized_text_zh: str = """"""
    subject: str = "三元（运元禄元马元）之吉凶"
    factor_refs: list = ['engine_id', 'three_origins', 'bazi_semantic', 'bazi_state_factor_224', 'bazi_semantic', 'bazi_state_factor_225', 'bazi_semantic', 'bazi_state_factor_226', 'bazi_semantic', 'bazi_condition_factor_91', 'bazi_semantic', 'source_ref', 'rel_smth_10_016', 'sanyuan', 'rel_smth_10_017', 'chong_luyuan', 'rel_smth_10_018', 'jie_mayuan', 'evi_smth_10_016', 'yunlu_mayuan', 'rule_sanyuan1', 'evi_smth_10_017', 'shiguan', 'rule_chong_luyuan1', 'evi_smth_10_018', 'pocai', 'rule_jie_mayuan1', 'map_smth_10_011', 'map_smth_10_012']
    
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
        l1_anchor="smth_v1.0.0_三元_运元禄元马元_之吉凶_001_L1",
    )
    version: str = "1.0.0"
