"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620006
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
    semantic_id="qtbj_v1.0.0_3__十二月甲木_丑月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3十二月甲木丑月(SemanticEntry):
    """
    - **原文（source_text）**：
  十二月甲木，天寒气冻，木性极寒，无生发之象，先用庚噼甲，方引丁火始得木火有通明之象，故丁次之。
  庚丁两透，科甲恩封。庚透丁藏，小贵。丁透庚藏，小富...
    """
    
    original_text: str = """- **原文（source_text）**：
  十二月甲木，天寒气冻，木性极寒，无生发之象，先用庚噼甲，方引丁火始得木火有通明之象，故丁次之。
  庚丁两透，科甲恩封。庚透丁藏，小贵。丁透庚藏，小富贵。无庚者，贫贱。无丁者，寒儒。
  或有丁透重重，亦是富贵中人，但须比肩，能发丁之焰，自有德业才能。如无比肩，寻常之士，稍有衣食而已。
  或支多见水，即有比肩，亦属平常。
  总之腊月甲木，虽有庚金，丁不可少。乏庚略可，乏丁无用。经云：甲木无根，男女夭寿。

- **分字分词释义**：
  - **天寒气冻**：天气寒冷冻结 / 丑月特征 / 极寒
  - **无生发之象**：没有生长萌发的迹象 / 冻木 / 无生机
  - **庚噼甲**：庚金劈开甲木 / 劈甲引丁 / 核心机制
  - **木火通明**：木生火明亮 / 吉象 / 格局成
  - **恩封**：皇帝恩赐封号 / 高官 / 极贵
  - **寒儒**：贫穷的读书人 / 无丁 / 有才无运
  - **发丁之焰**：发挥丁火的火焰 / 比肩助燃 / 辅助条件
  - **甲木无根**：甲木没有根基 / 无寅卯 / 夭寿

- **规范化释义（primary_lang_explained）**：
  十二月（丑月）的甲木，天气寒冷冻结，木性极度寒冷，没有生发的迹象。先用庚金劈开甲木，才能引燃丁火，从而得到木火通明的气象，所以丁火是第二步（机制上先庚后丁）。
  庚金和丁火都透出，科甲及第，受皇恩封赠。庚金透出丁火藏支，小贵。丁火透出庚金藏支，小富贵。没有庚金的人，贫贱。没有丁火的人，是寒酸的儒生。
  如果有重重丁火透出，也是富贵中人，但必须有比肩（甲木）助燃，才能发出丁火的火焰，自然有德业和才能。如果没有比肩，只是寻常之士，稍有衣食罢了。
  如果地支多见水（湿木），即使有比肩，也属于平常（湿木不能生火）。
  总之腊月（丑月）的甲木，虽然要有庚金，但丁火是绝对不可少的。缺乏庚金还可以勉强，缺乏丁火就无用了（冻木无用）。经书说：甲木无根（指无寅卯根或水生），男女都夭折短寿。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 12th Month (Ox Month) is in freezing weather; Wood nature is extremely cold with no sign of growth. First use Geng to split Jia, only then can Ding Fire be ignited, achieving the image of "Wood Fire Bright"; thus Ding is secondary (in sequence).
  If Geng and Ding are both revealed, Civil Service and Imperial honors are granted. Geng revealed and Ding hidden means small nobility. Ding revealed and Geng hidden means small wealth and nobility. Without Geng, one is poor and lowly. Without Ding, one is a poor scholar.
  If heavy Ding Fire is revealed, one is also among the wealthy and noble, but Parallel Shoulders are required to fuel Ding's flame, bringing virtue and talent. Without Parallel Shoulders, one is an ordinary person with just enough food and clothing.
  If branches see much Water (Wet Wood), even with Parallel Shoulders, it is ordinary.
  In summary, for Jia Wood in the Wax Month, although Geng is needed, Ding is indispensable. Lacking Geng is passable, but lacking Ding makes it useless. The classic says: If Jia Wood has no root, men and women suffer premature death.

- **核心要点**：
  - **机制**：劈甲引丁（Splitting Jia to ignite Ding）。
  - **先后**：先庚（劈）后丁（引）。但价值上丁更重要（暖）。
  - **条件**：需比肩（甲）引火，忌湿水（Wet Water）灭火。
  - **结论**：无丁无用，无根夭寿。

- **详细解说**：
  丑月二阳进气，但湿土寒冻。
  - 甲木在丑月是冠带位（进气），但本质仍寒。
  - “劈甲引丁”在此月最为典型。庚金劈开冻木，生火取暖。
  - “无庚者贫贱”：因为无法劈开冻木引火。
  - “无丁者寒儒”：有才（庚修剪）但无运（无暖局展示）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_165]` `[trigger: 丑月甲木]` `[factor_trigger: month_chou AND tiangan_jia AND tiangan_geng AND tiangan_ding]` `[role: 主干]` 十二月甲木，天寒气冻，木性极寒，无生发之象，先用庚噼甲，方引丁火。 → 《穷通宝鉴·三冬甲木》#6.3
  - `[ns_qttbj_166]` `[trigger: 丑月恩封]` `[factor_trigger: month_chou AND tiangan_jia AND geng_revealed AND ding_revealed]` `[role: 主干依赖]` 庚丁两透，科甲恩封。无庚者贫贱，无丁者寒儒。 → 《穷通宝鉴·三冬甲木》#6.3
  - `[ns_qttbj_167]` `[trigger: 发丁之焰]` `[factor_trigger: month_chou AND tiangan_jia AND ding_multiple_revealed AND shishen_parallel]` `[role: 条件分支]` 丁透重重，亦是富贵中人，但须比肩，能发丁之焰，自有德业才能。 → 《穷通宝鉴·三冬甲木》#6.3
  - `[ns_qttbj_168]` `[trigger: 乏丁无用]` `[factor_trigger: month_chou AND tiangan_jia AND NOT tiangan_ding]` `[role: 总结]` 腊月甲木，虽有庚金，丁不可少，乏庚略可，乏丁无用。 → 《穷通宝鉴·三冬甲木》#6.3
  - `[ns_qttbj_169]` `[trigger: 无根夭寿]` `[factor_trigger: tiangan_jia AND NOT (dizhi_yin OR dizhi_mao)]` `[role: 例外处理]` 经云：甲木无根，男女夭寿。 → 《穷通宝鉴·三冬甲木》#6.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 十二月甲木（丑月）"
    factor_refs: list = ['imperial_honors', 'poor_scholar', 'wax_month']
    
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
        l1_anchor="qtbj_v1.0.0_3__十二月甲木_丑月_001_L1",
    )
    version: str = "1.0.0"
