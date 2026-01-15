"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597024
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
    semantic_id="qtbj_v1.0.0_1__七月戊土_申月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1七月戊土申月(SemanticEntry):
    """
    - **原文（source_text）**：
  七月戊土，阳气渐入，寒气渐出，先丙后癸，甲木次之。
  丙癸甲透者，富贵极品。癸藏丙透，不仅秀才。丙甲两透，癸水会局藏辰，亦不失富贵。无丙得癸甲透，此...
    """
    
    original_text: str = """- **原文（source_text）**：
  七月戊土，阳气渐入，寒气渐出，先丙后癸，甲木次之。
  丙癸甲透者，富贵极品。癸藏丙透，不仅秀才。丙甲两透，癸水会局藏辰，亦不失富贵。无丙得癸甲透，此人清雅，家富千金。无癸甲者、常人。有丙火、妻贤子肖。若丙甲癸三者俱无，下流之命。
  或支成水局，休作弃命从才，宜取甲泄之。甲透者、稍有富贵。

- **分字分词释义**：
  - **阳气渐入**：阳气逐渐收敕 / 申月特点 / 秋来
  - **寒气渐出**：寒气逐渐出现 / 金气旺 / 需暖
  - **富贵极品**：富贵的极致 / 丙癸甲全 / 吉象
  - **清雅**：清新雅致 / 癸甲透无丙 / 次吉
  - **妻贤子肖**：妻子贤惠儿子肖似 / 有丙火 / 吉象
  - **弃命从才**：舍弃日主跟随财星 / 水局 / 变格
  - **下流之命**：卑下之命 / 三者俱无 / 凶象

- **规范化释义（primary_lang_explained）**：
  七月（申月）的戊土，阳气逐渐潜入（退气），寒气逐渐出来，先用丙火（暖土），后用癸水（泄金/润土），甲木（疏土）次之。
  丙火、癸水、甲木三者透出，富贵极品。癸水藏支丙火透出，不仅是个秀才。丙火甲木两透，癸水在地支会局或藏在辰土中，也不失为富贵。没有丙火得到癸水甲木透出，这人清雅，家富千金。没有癸水甲木的人，常人。有丙火，妻子贤惠子孙肖似。如果丙甲癸三者全无，是下流的命。
  如果地支合成水局，不要当作“弃命从财”看（申月戊土长生，不从），适宜取甲木泄水气（化财生杀？不，通常是比劫帮身或食神制杀，这里甲木泄水疑为水生木、木生火、火生土的流通，或者甲木吸水护土）。甲木透出，稍有富贵。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth in the 7th Month (Monkey Month): Yang Qi gradually enters (retreats); Cold Qi gradually emerges. First use Bing, then Gui, with Jia as secondary.
  If Bing, Gui, and Jia are all revealed, it is the highest grade of wealth and nobility. With Gui hidden and Bing revealed, not merely a Xiucai. With Bing and Jia revealed, and Gui forming a frame or hidden in Chen, one does not lose wealth and nobility. Without Bing but with Gui/Jia revealed, the person is refined and elegant, with a thousand gold in wealth. Without Gui/Jia, ordinary. With Bing, virtuous wife and capable children. If Bing/Jia/Gui are all absent, a lowly life.
  If branches form a Water Frame, do not view it as "Abandon Life Follow Wealth" (since Wu has root in Shen); it is suitable to take Jia to leak it (Water generates Wood). If Jia is revealed, there is slight wealth and nobility.

- **核心要点**：
  - **三宝**：申月戊土体泄而寒，喜丙（暖/生）、癸（润/泄金）、甲（疏/护）。
  - **从财难成**：申为戊土长生（阳干长生），故不轻言从。
  - **水局用甲**：水多土荡，甲木纳水（木吸水）。

- **详细解说**：
  - 申月戊土，金泄身寒。
  - 丙火是第一用神，制金暖土。
  - 癸水是配合，虽申月金旺生水，但戊土本燥，仍需水润，且癸水能泄庚金之顽。
  - 甲木在此月作用特殊，既疏土，又纳水防荡。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_521]` `[trigger: 申月戊土三用神]` `[factor_trigger: month_shen AND tiangan_wu AND tiangan_bing AND tiangan_gui AND tiangan_jia]` `[role: 主干]` 七月戊土，阳气渐入，寒气渐出，先丙后癸，甲木次之。 → 《穷通宝鉴·三秋戊土》#23.1
  - `[ns_qttbj_522]` `[trigger: 丙癸甲富贵极品]` `[factor_trigger: month_shen AND tiangan_wu AND tiangan_bing AND tiangan_gui AND tiangan_jia AND highest_wealth_nobility]` `[role: 条件分支]` 丙癸甲透者，富贵极品。 → 《穷通宝鉴·三秋戊土》#23.1
  - `[ns_qttbj_523]` `[trigger: 癸藏丙透秀才上格]` `[factor_trigger: month_shen AND tiangan_wu AND bing_revealed AND gui_in_branch AND above_xiucai]` `[role: 条件分支]` 癸藏丙透，不仅秀才。 → 《穷通宝鉴·三秋戊土》#23.1
  - `[ns_qttbj_524]` `[trigger: 丙甲两透癸会局富贵]` `[factor_trigger: month_shen AND tiangan_wu AND tiangan_bing AND tiangan_jia AND (dizhi_water_frame OR dizhi_chen) AND not_lose_wealth_nobility]` `[role: 条件分支]` 丙甲两透，癸水会局藏辰，亦不失富贵。 → 《穷通宝鉴·三秋戊土》#23.1
  - `[ns_qttbj_525]` `[trigger: 无丙癸甲清雅富家]` `[factor_trigger: month_shen AND tiangan_wu AND NOT tiangan_bing AND tiangan_gui AND tiangan_jia AND refined_wealthy]` `[role: 条件分支]` 无丙得癸甲透，此人清雅，家富千金。 → 《穷通宝鉴·三秋戊土》#23.1
  - `[ns_qttbj_526]` `[trigger: 无癸甲常人]` `[factor_trigger: month_shen AND tiangan_wu AND tiangan_bing AND NOT tiangan_gui AND NOT tiangan_jia AND ordinary_status]` `[role: 条件分支]` 无癸甲者、常人。 → 《穷通宝鉴·三秋戊土》#23.1
  - `[ns_qttbj_527]` `[trigger: 有丙妻贤子肖]` `[factor_trigger: month_shen AND tiangan_wu AND tiangan_bing AND spouse_virtuous_child_good]` `[role: 条件分支]` 有丙火、妻贤子肖。 → 《穷通宝鉴·三秋戊土》#23.1
  - `[ns_qttbj_528]` `[trigger: 三宝全无下流之命]` `[factor_trigger: month_shen AND tiangan_wu AND NOT tiangan_bing AND NOT tiangan_gui AND NOT tiangan_jia AND lowly_status]` `[role: 例外处理]` 若丙甲癸三者俱无，下流之命。 → 《穷通宝鉴·三秋戊土》#23.1
  - `[ns_qttbj_529]` `[trigger: 水局甲泄稍有富贵]` `[factor_trigger: month_shen AND tiangan_wu AND dizhi_water_frame AND tiangan_jia AND NOT abandon_follow_wealth AND slight_nobility]` `[role: 条件分支]` 或支成水局，休作弃命从才，宜取甲泄之，甲透者稍有富贵。 → 《穷通宝鉴·三秋戊土》#23.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 七月戊土（申月）"
    factor_refs: list = ['yang_entering', 'abandon_follow_wealth']
    
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
        l1_anchor="qtbj_v1.0.0_1__七月戊土_申月_001_L1",
    )
    version: str = "1.0.0"
