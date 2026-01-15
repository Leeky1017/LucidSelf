"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157529
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
    semantic_id="smth_v1.0.0_六丙日丙申时断_身坐煞位与偏财同居_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日丙申时断身坐煞位与偏财同居(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日丙申时断。

  六丙日生时丙申，身坐煞位财同居；不贵即富逢身旺，煞重身轻命不舒。丙日丙申时，丙见壬为煞、庚为财，申上庚壬皆旺，丙火无气，身坐煞、财之...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日丙申时断。

  六丙日生时丙申，身坐煞位财同居；不贵即富逢身旺，煞重身轻命不舒。丙日丙申时，丙见壬为煞、庚为财，申上庚壬皆旺，丙火无气，身坐煞、财之位，若通身旺月者，不贵即富。煞重身轻，非僧即道。

  丙子日丙申时，申子半官，丑月，杂气财官，贵。卯月，偏官。寅午戌，羊刃用煞，俱吉。

  丙寅日丙申时，文学成名。生子丑寅月，行北运，贵。巳酉丑，合煞，制伏有权，行北运，贵。辰戌丑未月，俱吉。

  丙辰日丙申时，丑未年月，亦吉。亥卯未印局，不贵即富。辰申子会煞无制，贫薄。

  丙午日丙申时，身旺，不贵即富。寅卯月，透官印，大贵。午丑，财官印三奇，三四品贵。亥月正官，风宪。

  丙申日丙申时，身衰煞旺，早荣晚枯。春冬身旺，吉。夏平，秋凶。透官印透煞，行财运，贵。

  丙戌日丙申时，身衰财旺，出家僧道。春身旺，吉。秋，身弱煞旺，凶。丑未年月，行南运，大贵。

  丙日丙申时上逢，身弱无资财禄空；透印透官行财运，儒林清职有英雄。丙日丙申时内，如逢癸亥为财。身生旺地遇官星，定主功名高大。

- 分字分词释义：

  - **身坐煞位**：丙火日主在申上，申为壬水七煞的长生位。
  - **偏财同居**：申中庚金偏财与壬水七煞同居。
  - **煞重身轻**：七煞太重而日主太弱，形成危险格局。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，丙申时」：

  - 丙火在申无气，申上庚金偏财、壬水七煞皆旺，身坐煞财之位；
  - 若月令通身旺之气，身能承担煞财，则不贵即富；若煞重身轻，则非僧即道。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Bing-Shen Hour":

  - Bing Fire has no energy at Shen; Shen contains prosperous Geng Metal (Indirect Wealth) and Ren Water (Seven-Killing)—self seated at killing-wealth position.
  - If monthly pillar connects with strong-body energy, body can bear killing and wealth, resulting in either nobility or riches; if killing is heavy and self is light, the outcome is monastic life.

- 核心要点：

  - 本格以「身坐煞位」为核心，结构偏险。
  - 身旺可用煞财，身弱则受煞克。
  - 需要印绶扶身或身旺运来化解。

- 详细解说：

  1. **身坐煞位的风险**  
     - 申为壬水七煞长生，煞星有力；  
     - 丙火在申无气，若无扶助，身弱难敌。

  2. **身旺的重要性**  
     - 若月令通火木之气，身旺可用煞财；  
     - 形成「身旺用煞」的结构，可成就富贵。

- 校勘与字词辨析：

  - 「出家僧道」指身弱财旺，难以享受俗世福禄。
  - 「早荣晚枯」指早年得意、晚年衰落。
  - **English**：
    - Success in early years; decline in later years.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_129]` `[trigger: 身坐煞位]` `[factor_trigger: shenzuo_shawei AND cai_tongju]` `[role: 主干]` 六丙日生时丙申，身坐煞位财同居。 → 《三命通会》卷八#六丙日丙申时
  - `[ns_smth_08_130]` `[trigger: 不贵即富]` `[factor_trigger: bugui_jifu AND feng_shenwang]` `[role: 主干依赖]` 不贵即富逢身旺，煞重身轻命不舒。 → 《三命通会》卷八#六丙日丙申时
  - `[ns_smth_08_131]` `[trigger: 非僧即道]` `[factor_trigger: feiseng_jidao AND sha_zhong_qing]` `[role: 条件分支]` 煞重身轻，非僧即道。 → 《三命通会》卷八#六丙日丙申时
  - `[ns_smth_08_132]` `[trigger: 儒林英雄]` `[factor_trigger: rulin_yingxiong AND touyin_touguan]` `[role: 总结]` 透印透官行财运，儒林清职有英雄。 → 《三命通会》卷八#六丙日丙申时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日丙申时断：身坐煞位与偏财同居"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_factor_177', 'bazi_semantic', 'bazi_relation_piancai_2', 'bazi_semantic', 'bazi_state_factor_178', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_factor_54', 'bazi_semantic', 'source_ref', 'rel_smth_08_097', 'shenzuo_shawei', 'rel_smth_08_098', 'piancai_tongju', 'rel_smth_08_099', 'shenwang_youli', 'evi_smth_08_097', 'shenzuo_shawei', 'rule_zuosha', 'evi_smth_08_098', 'piancai_tongju', 'rule_tongju', 'evi_smth_08_099', 'shazhong_shenqing', 'rule_shazhong', 'map_smth_08_065', 'map_smth_08_066']
    
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
        l1_anchor="smth_v1.0.0_六丙日丙申时断_身坐煞位与偏财同居_001_L1",
    )
    version: str = "1.0.0"
