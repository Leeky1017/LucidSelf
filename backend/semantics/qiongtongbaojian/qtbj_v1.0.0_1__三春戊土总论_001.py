"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596966
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
    semantic_id="qtbj_v1.0.0_1__三春戊土总论_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三春戊土总论(SemanticEntry):
    """
    - **原文（source_text）**：
  三春戊土，无丙照暖，戊土不生，无甲疏噼，戊土不灵，无癸滋润，万物不长。
  正二月先丙后甲，癸又次之。三月先甲后丙，癸又次之，因戊土司权故也。
  有...
    """
    
    original_text: str = """- **原文（source_text）**：
  三春戊土，无丙照暖，戊土不生，无甲疏噼，戊土不灵，无癸滋润，万物不长。
  正二月先丙后甲，癸又次之。三月先甲后丙，癸又次之，因戊土司权故也。
  有甲、丙、癸，三者齐透，必主一品当朝，或二透一藏，亦登金榜，二藏一透，也可异途。
  正二月即有甲癸，若无丙除寒，如万物生而不长，故无丙者，富贵艰辛。或有丙无甲癸者，名曰春旱，如万物生而多厄。无甲癸者，一生勤苦，劳而无功。
  或一派丙火，有甲欠癸，先泰后否。或支成火局，不见壬癸，僧道孤贫。癸透者贵。壬透者富。
  用水者，要审水之多少。

- **分字分词释义**：
  - **三春戊土**：春季的戊土 / 寅卯辰 / 高厚之土
  - **无丙照暖**：没有丙火照耀温暖 / 寒土无阳 / 不生
  - **无甲疏噼**：没有甲木疏通劈开 / 土顽不灵 / 郁闭
  - **无癸滋润**：没有癸水滋润 / 土燥万物不长 / 润枯
  - **先丙后甲**：先用丙火后用甲木 / 解寒再疏土 / 寅卯月次序
  - **先甲后丙**：先用甲木后用丙火 / 先制服厚土再温养 / 辰月次序
  - **一品当朝**：一品大臣在朝掌权 / 极品贵官 / 贵象
  - **春旱**：春天干旱无雨 / 有丙无水 / 万物多厄
  - **先泰后否**：先通达后否塞 / 初运顺利后运闭塞 / 运势消长
  - **僧道孤贫**：出家僧道孤清而贫 / 火局无水 / 身弱无依

- **规范化释义（primary_lang_explained）**：
  春天的戊土，没有丙火照暖，戊土就没有生机；没有甲木疏劈，戊土就不灵动；没有癸水滋润，万物不能生长。
  正月（寅月）二月（卯月），先用丙火（解寒），后用甲木（疏土），癸水（润燥）再次之。三月（辰月），先用甲木（制土），后用丙火，癸水再次之，这是因为三月戊土当权旺盛的缘故。
  如果甲木、丙火、癸水三者齐透天干，必主一品当朝的大官。或者两个透出一个藏支，也能登金榜。两个藏支一个透出，也可以异途显达。
  正月二月即使有甲木和癸水，如果没有丙火消除寒气，就像万物萌生却不能长大，所以没有丙火的人，富贵来得艰辛。如果有丙火而没有甲木癸水，叫“春旱”，万物生长却多灾多难。没有甲癸的人，一生勤苦，劳而无功。
  如果一派丙火，有甲木而欠缺癸水，先通泰后闭塞（先泰后否）。如果地支合成火局，不见壬癸水，是僧道孤贫之命。癸水透出者贵，壬水透出者富。
  用水的人，要审视水的多少（不宜太多）。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth in the Three Spring Months: Without Bing to warm, Wu Earth does not generate; without Jia to split/dredge, Wu Earth is not active; without Gui to moisten, nothing grows.
  In the 1st and 2nd Months, prioritize Bing, then Jia, with Gui as secondary. In the 3rd Month, prioritize Jia, then Bing, with Gui as secondary, because Wu Earth holds authority.
  If Jia, Bing, and Gui are all revealed, one is surely a First Rank official. If two revealed and one hidden, one enters the Golden List. If two hidden and one revealed, alternative success.
  In the 1st/2nd Months, even with Jia/Gui, without Bing to remove cold, things sprout but don't grow; thus without Bing, wealth and nobility are arduous. If Bing exists without Jia/Gui, it is "Spring Drought"; things grow but suffer disasters. Without Jia/Gui, one toils for life without merit.
  If there is a mass of Bing Fire, with Jia but lacking Gui, it is "First Peace then Stagnation". If branches form a Fire Frame without Ren/Gui, it is a monk/Taoist, lonely and poor. Gui revealed implies nobility; Ren revealed implies wealth.
  When using Water, assess the amount carefully.

- **核心要点**：
  - **三宝**：丙（暖）、甲（疏）、癸（润）。缺一不可。
  - **顺序**：寅卯月丙先，辰月甲先。
  - **春旱**：有丙无水，万物多厄。
  - **无丙**：生而不长，富贵艰辛。

- **详细解说**：
  - 戊土为高山厚土，春季气寒土冻。
  - 丙火是太阳，也是戊土的源头（火生土）。
  - 甲木是森林，疏通戊土顽气，使之灵动。
  - 癸水是雨露，滋润万物。
  - 三者配合，构成“山明水秀、阳光普照、万物生长”的象，故极贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_300]` `[trigger: 三春戊土三宝]` `[factor_trigger: season_spring AND tiangan_wu AND tiangan_bing AND tiangan_jia AND tiangan_gui AND three_treasures]` `[role: 主干]` 三春戊土，无丙照暖，戊土不生；无甲疏噼，戊土不灵；无癸滋润，万物不长。 → 《穷通宝鉴·三春戊土》#21.1
  - `[ns_qttbj_301]` `[trigger: 无丙除寒]` `[factor_trigger: month_yin_mao AND tiangan_wu AND tiangan_jia AND tiangan_gui AND NOT tiangan_bing AND no_bing_hardship]` `[role: 例外处理]` 正二月有甲癸，若无丙除寒，如万物生而不长，故无丙者，富贵艰辛。 → 《穷通宝鉴·三春戊土》#21.1
  - `[ns_qttbj_302]` `[trigger: 春旱多厄]` `[factor_trigger: season_spring AND tiangan_wu AND tiangan_bing AND NOT tiangan_jia AND NOT tiangan_gui AND spring_drought]` `[role: 例外处理]` 有丙无甲癸者，名曰春旱，如万物生而多厄。 → 《穷通宝鉴·三春戊土》#21.1
  - `[ns_qttbj_303]` `[trigger: 僧道孤贫]` `[factor_trigger: season_spring AND tiangan_wu AND dizhi_fire_frame AND NOT tiangan_ren AND NOT tiangan_gui AND monk_poor]` `[role: 例外处理]` 支成火局，不见壬癸，僧道孤贫；癸透者贵，壬透者富。 → 《穷通宝鉴·三春戊土》#21.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三春戊土总论"
    factor_refs: list = ['spring_drought', 'split_dredge', 'first_peace_stagnation']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__三春戊土总论_001_L1",
    )
    version: str = "1.0.0"
