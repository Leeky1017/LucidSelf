"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620104
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
    semantic_id="qtbj_v1.0.0_3__九月乙木_戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3九月乙木戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  九月乙木，根枯叶落，必赖癸水滋养。如见甲申时，名为藤萝系甲，可秋可冬。
  若见癸水，又遇辛金发水之源，定主科甲。或有癸无辛，常人。有辛无癸，贫贱。或...
    """
    
    original_text: str = """- **原文（source_text）**：
  九月乙木，根枯叶落，必赖癸水滋养。如见甲申时，名为藤萝系甲，可秋可冬。
  若见癸水，又遇辛金发水之源，定主科甲。或有癸无辛，常人。有辛无癸，贫贱。或四柱壬多，水难生乙，亦是寻常之辈。
  或支多戊土，又逢天干，作从才看，无比劫方妙，一逢比劫，富屋贫人。
  用癸者，金妻、水子。但子女艰难，季土克制故也。

- **分字分词释义**：
  - **根枯叶落**：根枯萎叶落尽 / 戌月特征 / 木衰
  - **藤萝系甲**：藤蔓缠绕大树 / 甲申时 / 依附格
  - **可秋可冬**：能度过秋冬 / 系甲后 / 生存
  - **发水之源**：发出水的源头 / 辛金生癸 / 杀印相生
  - **季土克制**：季土克制水 / 戌土燥 / 子女难
  - **水难生乙**：水难以生木 / 壬多 / 水大木漂

- **规范化释义（primary_lang_explained）**：
  九月（戌月）的乙木，根枯叶落，必须依赖癸水滋养。如果生于甲申时，叫“藤萝系甲”，无论秋天冬天都可以生存。
  如果见到癸水，又遇到辛金（七杀）发水源（杀印相生），定主科甲。如果有癸水无辛金，常人。有辛金无癸水，贫贱（杀重身轻）。如果四柱壬水多，水难生乙（水大木漂），也是寻常之辈。
  如果地支多戊土，又透出天干，作“从财格”看，没有比劫才妙，一旦遇到比劫，就是富屋贫人。
  用癸水的人，金为妻，水为子。但子女艰难，因为季土（戌土）克制水的缘故。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 9th Month (Dog Month) has withered roots and fallen leaves; it must rely on Gui Water for nourishment. If born in Jia-Shen Hour, it is called "Vine Clinging to Pine" (Teng Luo Xi Jia), viable in both Autumn and Winter.
  If Gui Water is seen, and Xin Metal is met to generate the Water source, Civil Service is certain. With Gui but no Xin, one is ordinary. With Xin but no Gui, poor and lowly. If Ren Water is abundant, Water is hard to generate Yi (Drifting), also implying an ordinary person.
  If branches have much Wu Earth, revealed on stems, view it as "Follow Wealth". It is wondrous without Parallel/Rob Wealth; once Parallel/Rob Wealth is met, it is a "Rich House Poor Man".
  Those using Gui take Metal as Wife and Water as Child. But children are difficult, because Seasonal Earth (Xu) controls the Water.

- **核心要点**：
  - **首要用神**：癸水（滋养）。戌月燥土，非水不能生木。
  - **藤萝系甲**：甲申时，乙木依附甲木，不畏秋冬。
  - **从财格**：土多无劫，从财。
  - **杀印相生**：辛金生癸水，贵。

- **详细解说**：
  戌月乙木入墓，气机衰绝。
  - “藤萝系甲”是乙木生存的绝招，尤其在死绝之月。
  - “辛金发水之源”：戌中辛金为源，癸水为流，源流长远，故贵。
  - 戌月燥土克水，故用神癸水易受伤，这也导致“子女艰难”（水为子）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_202]` `[trigger: 戌月乙木]` `[factor_trigger: month_xu AND tiangan_yi AND tiangan_gui]` `[role: 主干]` 九月乙木，根枯叶落，必赖癸水滋养。 → 《穷通宝鉴·三秋乙木》#9.3
  - `[ns_qttbj_203]` `[trigger: 藤萝系甲]` `[factor_trigger: month_xu AND tiangan_yi AND hour_jiashen AND vine_clinging_to_jia]` `[role: 主干依赖]` 如见甲申时，名为藤萝系甲，可秋可冬。 → 《穷通宝鉴·三秋乙木》#9.3
  - `[ns_qttbj_204]` `[trigger: 辛金发水]` `[factor_trigger: month_xu AND tiangan_yi AND gui_revealed AND xin_revealed AND xin_gen_gui]` `[role: 条件分支]` 见癸水，又遇辛金发水之源，定主科甲。 → 《穷通宝鉴·三秋乙木》#9.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 九月乙木（戌月）"
    factor_refs: list = ['vine_clinging_to_jia', 'generating_water_source']
    
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
        l1_anchor="qtbj_v1.0.0_3__九月乙木_戌月_001_L1",
    )
    version: str = "1.0.0"
