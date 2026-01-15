"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578422
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
    semantic_id="qtbj_v1.0.0_3__十一月辛金_子月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3十一月辛金子月(SemanticEntry):
    """
    - **原文（source_text）**：
  十一月辛金，癸水司令，为寒冬雨露，切忌癸出冻金，而困丙火，壬丙两透，不见戊癸，衣锦腰金。即壬藏丙透，一榜堪图。
  或壬多有戊，丙甲出干者，青云之客。...
    """
    
    original_text: str = """- **原文（source_text）**：
  十一月辛金，癸水司令，为寒冬雨露，切忌癸出冻金，而困丙火，壬丙两透，不见戊癸，衣锦腰金。即壬藏丙透，一榜堪图。
  或壬多有戊，丙甲出干者，青云之客。若壬多无戊丙者，泄金太过，定主寒儒。或壬多、甲乙重重，无丙火者，贫寒。
  或支成水局，癸水出干，有二戊制者，富贵恩荣，无戊者常人。或支见亥子丑，干出比劫，无丙、名润下格，富贵双全，运喜西北。若无庚辛，又出甲乙，无戊丙者，必主僧道。
  或支成木局，有丁出干，又见戊者，功名特达。冬月辛金，须丙温暖方妙。

- **分字分词释义**：
  - **寒冬雨露**：冬季寒冷雨水 / 癸水特点 / 子月
  - **冻金**：冰冻金气 / 癸水寒冷 / 凶象
  - **困丙火**：困住丙火 / 癸克丙 / 凶象
  - **衣锦腰金**：穿锦衣系金带 / 大富贵 / 吉象
  - **青云之客**：青云直上之人 / 壬戊丙甲配合 / 吉象
  - **寒儒**：贫寒读书人 / 壬多无戊丙 / 凶象
  - **润下格**：水润下流格 / 从儿格 / 格局名
  - **富贵双全**：富与贵兼得 / 润下成格 / 吉象
  - **功名特达**：功名卓越特出 / 丁戊配合 / 吉象

- **规范化释义（primary_lang_explained）**：
  十一月（子月）辛金，癸水司令为寒冬雨露，切忌癸出冻金困丙火。壬丙两透不见戊癸衣锦腰金。即壬藏丙透一榜可期。
  或壬多有戊（止水）丙甲出干者青云之客。若壬多无戊丙者泄金太过定主寒儒。或壬多甲乙重重无丙火者贫寒。
  或支成水局癸水出干有二戊制者富贵恩荣无戊者常人。或支见亥子丑干出比劫无丙名"润下格"富贵双全运喜西北。若无庚辛又出甲乙无戊丙者必主僧道。
  或支成木局有丁出干又见戊者功名特达。冬月辛金须丙温暖方妙。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 11th Month (Rat Month): Gui Water commands winter cold rain-dew. Beware Gui revealing freezing Metal trapping Bing. Ren/Bing revealing not見Wu/Gui silk-robed gold-belted. Even Ren hidden Bing reveals one list possible.
  If Ren many with Wu Bing/Jia revealing Azure Cloud guest. If Ren many without Wu/Bing draining Metal too much surely poor scholar. If Ren many Jia/Yi heavy no Bing poverty.
  If branches form Water Frame Gui reveals having two Wu制wealthy noble honors without Wu ordinary. If branches見Hai/Zi/Chou stems出比劫 no Bing name "Flowing Downward Pattern" wealth-nobility雙全 luck喜NW. If no Geng/Xin also出Jia/Yi no Wu/Bing surely monk/Taoist.
  If branches form Wood Frame Ding reveals also見Wu fame outstanding. Winter Xin Metal must Bing warm才妙.

- **核心要点**：
  - **首要用神**：壬丙。忌癸（冻金困火）
  - **格局**：润下格（从儿格金水双清）
  - **冬月必要**：丙火暖局

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_395]` `[trigger: 辛生子月]` `[factor_trigger: month_zi AND tiangan_xin AND tiangan_ren AND tiangan_bing AND NOT tiangan_gui]` `[role: 主干]` 十一月辛金，癸水司令，为寒冬雨露，切忌癸出冻金，而困丙火，壬丙两透，衣锦腰金。 → 《穷通宝鉴·三冬辛金》#34.3
  - `[ns_qttbj_396]` `[trigger: 壬多无戊丙]` `[factor_trigger: month_zi AND tiangan_xin AND ren_excessive AND NOT tiangan_wu AND NOT tiangan_bing]` `[role: 例外处理]` 若壬多无戊丙者，泄金太过，定主寒儒。 → 《穷通宝鉴·三冬辛金》#34.3
  - `[ns_qttbj_397]` `[trigger: 润下格]` `[factor_trigger: month_zi AND tiangan_xin AND (dizhi_hai OR dizhi_zi OR dizhi_chou) AND shishen_parallel AND NOT tiangan_bing AND flowing_downward_pattern]` `[role: 条件分支]` 或支见亥子丑，干出比劫，无丙，名润下格，富贵双全。 → 《穷通宝鉴·三冬辛金》#34.3
  - `[ns_qttbj_398]` `[trigger: 冬月暖局]` `[factor_trigger: season_winter AND tiangan_xin AND likes_bing_warm]` `[role: 总结]` 冬月辛金，须丙温暖方妙。 → 《穷通宝鉴·三冬辛金》#34.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 十一月辛金（子月）"
    factor_refs: list = ['gui_freeze_metal', 'flowing_downward_pattern', 'azure_cloud_guest']
    
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
        l1_anchor="qtbj_v1.0.0_3__十一月辛金_子月_001_L1",
    )
    version: str = "1.0.0"
