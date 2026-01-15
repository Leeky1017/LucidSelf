"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288769
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
    semantic_id="smth_v1.0.0_子月_印_官_财的交错_001",
    book_id="sanming",
    engine_id="bazi"
)
class 子月印官财的交错(SemanticEntry):
    """
    - **原文（source_text）**：
  子月。甲乙日得子月为印绶，喜见官露印，忌坐天财、伤印，岁运喜忌同。丙丁日为官，贵，阴阳和合，喜露财官，见三合、六合、官印合，须考月令中气：身旺喜财官，...
    """
    
    original_text: str = """- **原文（source_text）**：
  子月。甲乙日得子月为印绶，喜见官露印，忌坐天财、伤印，岁运喜忌同。丙丁日为官，贵，阴阳和合，喜露财官，见三合、六合、官印合，须考月令中气：身旺喜财官，身弱喜印旺；忌七煞、伤官、岁运伤为福之地。丁得之为偏官，两阴相攻，喜身旺有合制，忌身弱无合，露正官及四柱带多无制伏，运喜身旺合偏官，忌身弱。戊己日为财，喜露财身旺，忌坐刃透比，不遇亥子日生，难为财运：身旺喜财，身弱喜旺，忌劫。庚辛日为长生财，喜坐露财身旺，忌无财身弱；如四柱全无财星，便不是长生财，只是伤官背禄，月令须时带偏官，庚日丙时巳时，辛日丁时午时，便为有制，吉；次宜日时带诸不见之形，贵；如年日时三官皆不遇，其命可知，行运身旺喜财，身弱喜旺，通忌比、劫。壬癸日，壬为旺，癸为建禄，只是身强，奈名利二者却被月令销熔尽了，颇宜时带偏官，贵，如壬日戊巳时、癸日巳午时是也；次宜日时带诸不见之形，贵。如年月时三宫皆不遇，其命可知，运喜行偏官，忌正官。

- 分字分词释义：
  - **印绶**：子月为亥子北水之气，对甲乙而言为印绶之地，主资质与庇护，而非直接财利。
  - **长生财**：庚辛在子月得水为长生之地，若再见财透，主财源有根、有生机。
  - **伤官背禄**：本应为长生财之月，反因无财而多伤官，象征才气外泄、难承禄位。
  - **偏官（七煞）合制**：偏官有合且得制时，可以转为权力与担当；无合无制则多为压力与凶险。
  - **诸不见之形**：指刑冲会合等格局隐伏于地支处，不显于天干，需要通过结构识别。

- 规范化释义（primary_lang_explained）：
  子月是一年最深冬之时，水气极盛，原文从不同日主的角度，描述「在子月之中，谁得势、谁受损」。对甲乙木而言，子月为印绶之地，重在资质与学习，不在直接发财：见官露印则有科名与庇护，反之若坐天财、伤印，则易因财坏学、因名损身。丙丁火在子月逢旺水，反成官星：若财官并露、官印相合，且身旺，则能在寒水之中借官星立身；若身弱或七煞、伤官太重，则易变成压力与是非。戊己土在子月以财星论，喜财透身旺，忌比劫与羊刃夺财，尤其不遇亥子日则难以真正聚财。庚辛金在子月名为「长生财」：有水生金，有财透而身旺，则为「财源有根」的佳象；若一味伤官而无财，则从长生财滑向伤官背禄。壬癸日主在子月自身虽旺或得禄，但月令水气过盛，往往「身强而名利被销熔」，需借时上偏官等结构，另辟出贵显之路。


- **完整对等诠释（secondary_lang_full）**：
  In Zi month the chart stands in the coldest part of winter, with water at its peak. The text first sorts the ten stems by what they primarily receive here: Jia and Yi gain seal, Bing and Ding gain official power, Wu and Ji treat Zi as a wealth month, Geng and Xin are promised a kind of "long‑life wealth", while Ren and Gui themselves become very strong yet see their fame and profit easily melted away by the season. For Jia–Yi, having official stars show and being supported by strong seal in this deep‑water month favours study, credentials and patronage more than quick money; if instead heavenly wealth and hurting‑seal combinations dominate, learning is sacrificed for gain and reputation is hard to protect.
  Bing–Ding fire in Zi month borrow water to become officials: when wealth and official are both visible and link cleanly with seal, and the person is strong, they can stand in cold environments through institutions, offices or formal roles. Wu–Ji take Zi as a wealth month and need exposed, rooted wealth with a sturdy body; heavy peers and Blades simply rob what appears. For Geng–Xin, Zi is called a month of long‑life wealth, but this promise is conditional: only when water clearly produces metal and real wealth stars emerge with a robust day stem does it become "wealth with roots"; if wealth is missing and only Hurting Officers are present, the pattern slides into talent without corresponding reward. Ren–Gui themselves are powerful or have salary here, yet the surplus water of the month tends to dissolve visible achievement, so the classic advises seeking partial‑official patterns and hidden nobles in the hour and other branches to turn raw strength into actual status.

- 核心要点：
  - 子月为水气极盛之时，与各日主的关系，以「印、官与财」三类为核心：木得印、火成官、水身旺、金为长生财、土为财星。
  - 判断吉凶不能只看「子水旺」，而要细辨身强身弱与财官印的显露、伏藏及合制关系，尤其注意偏官是否有合、有制。
  - 「长生财」与「伤官背禄」是同一月令的两种结果：关键在财星是否透出、有无劫比夺财，以及是否被纯伤官结构替代。

- 应用推演（操作顺序）：
  1) 判盘时先识别是否生于子月，并据日干标记此月为印绶月、官月、财月或身旺之月，例如甲乙视为印月、庚辛视为长生财月等。
  2) 分析财官印在天干、地支中的显露情况：记录「官透/不透」「财透/不透」「印透/不透」及是否形成三合、六合、官印合等结构。
  3) 根据身强身弱判断取用：身旺则优先取财官，身弱则优先取印比，特别注意偏官（七煞）是否有合、有制，避免无制之煞被误判为贵。
  4) 在行运模拟中，将子月所对应的水分野运标记为「印旺/水旺期」，对各日干分别编码为「学业/资质强化」「财官潜力被压制」或「长生财启动」等标签，用于后续预测与推荐。

- 反例与边界：
  - 不宜一见子月就简单断为「水旺必吉」或「聪明好学」，忽视日主五行立场与财官印的不同归属。
  - 不可将庚辛生于子月一概视作「长生财必富」，若四柱无财反多伤官，反而应以伤官背禄论之。
  - 工程实现中若只把子月映射成「高智商水象标签」，会忽视其中对不同日干而言可能是官、是财、是印的差异，导致模型偏差。
  - 反向误区是见子月就过度担忧「水太旺」，将所有水旺结构一律当成情绪与惰性，而不看偏官合制、官印相生等激活路径。

- 小例（示意）：
  - 某甲日命局生于子月，柱中有官星透出并见印生身，行运再入北方水运，系统可将其识别为「印绶得地、官印相生」的类型：适合走学术、文职体系，由学习与资历铺路。
  - 另一命局辛日生于子月，四柱无财透而伤官重，行运又多比劫，系统则标记为「伤官背禄」：虽有聪明与表达力，但在制度与资源获取上反复受阻，需要刻意设计稳定职业路径与长期积累机制。"""
    normalized_text_zh: str = """"""
    subject: str = "子月：印、官、财的交错"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'zi_month_seal_official_wealth', 'bazi_semantic', 'long_life_wealth_pattern', 'bazi_semantic', 'harm_official_back_salary_risk', 'bazi_semantic', 'partial_official_merge_control', 'bazi_semantic', 'hidden_noble_forms', 'bazi_semantic', 'official_seal_mutual_birth', 'bazi_semantic', 'source_ref', 'rel_smth_04_016', 'zi_month_seal_official_wealth', 'rel_smth_04_017', 'partial_official_merge_control', 'rel_smth_04_018', 'harm_official_back_salary_risk', 'evi_smth_04_016', 'long_life_wealth_pattern', 'rule_long_life_wealth', 'evi_smth_04_017', 'harm_official_back_salary_risk', 'rule_back_salary_risk', 'evi_smth_04_018', 'partial_official_merge_control', 'rule_merge_control', 'map_smth_04_011', 'map_smth_04_012']
    
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
        l1_anchor="smth_v1.0.0_子月_印_官_财的交错_001_L1",
    )
    version: str = "1.0.0"
