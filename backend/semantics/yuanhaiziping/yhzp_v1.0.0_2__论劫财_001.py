"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558988
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
    semantic_id="yhzp_v1.0.0_2__论劫财_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 2论劫财(SemanticEntry):
    """
    - **原文（source_text）**：
  亦名'逆刃'，如乙见甲为劫财。乙以庚为夫，见丙克庚，故克夫；男命则克妻。五阳见五阴为败财，主克妻害子。五阴见五阳为劫财，主破耗、防小人，不克妻。乙以戊...
    """
    
    original_text: str = """- **原文（source_text）**：
  亦名'逆刃'，如乙见甲为劫财。乙以庚为夫，见丙克庚，故克夫；男命则克妻。五阳见五阴为败财，主克妻害子。五阴见五阳为劫财，主破耗、防小人，不克妻。乙以戊己为财，甲见夺己坏戊；丁以庚辛为财，丙能夺辛破庚；类如此也。兄见弟，弟能败兄之财，夺兄之妻。弟见兄，兄能劫弟之财，而不敢取弟之妻。财者，人之所欲，方令弟兄见之，多有争竞，如夷、齐能几人。男命见劫财多克妻，女命见伤官多克夫。此极论也。

- **分字分词释义**：
  - **劫财/逆刃**：与日主同类而阴阳相异者，如甲木见乙木为劫财，亦名"逆刃"。
  - **败财**：阳日主见阴同类，如甲见乙，主克妻害子。
  - **劫财**：阴日主见阳同类，如乙见甲，主破耗防小人，不克妻。
  - **乙以庚为夫见丙克庚**：乙木以庚金为夫星（正官），丙火伤官克庚金，故女命劫财（甲）引出伤官克夫。
  - **甲见夺己坏戊**：甲木以戊己土为财，甲木见乙木（劫财），乙木与己土合化，甲木见甲木（比肩），争夺戊土正财。
  - **兄见弟弟能败兄之财**：比喻劫财分财之象，弟夺兄之财并夺兄之妻。
  - **夷齐能几人**：伯夷叔齐让国之典故，讽刺世人多争财而难有高风亮节。
  - **男命劫财克妻**：劫财克正财，正财为妻，故克妻。
  - **女命伤官克夫**：伤官克正官，正官为夫，故克夫。

- **规范化释义（primary_lang_explained）**：
  劫财亦名"逆刃"，如乙木见甲木为劫财。败财与劫财有别："五阳见五阴为败财，主克妻害子；五阴见五阳为劫财，主破耗、防小人，不克妻"——阳日主见阴同类主克妻害子，阴日主见阳同类主破耗防小人但不克妻。女命劫财引出伤官克夫："乙以庚为夫，见丙克庚，故克夫"。劫财分财之象以兄弟比喻："兄见弟，弟能败兄之财，夺兄之妻；弟见兄，兄能劫弟之财，而不敢取弟之妻"——弟（劫财）敢于夺兄之妻财，兄（比肩）只敢劫弟之财而不敢取妻。"财者，人之所欲，方令弟兄见之，多有争竞"——财是人所欲之物，兄弟见之必争，"如夷、齐能几人"——能如伯夷叔齐般让国者世间几人？"男命见劫财多克妻，女命见伤官多克夫"是六亲的极论。

- **完整对等诠释（secondary_lang_full）**：
  Rob Wealth is also called "Reverse Blade," such as Yi Wood seeing Jia Wood as Rob Wealth. Defeat-Wealth and Rob-Wealth differ: "Five Yang seeing Five Yin becomes Defeat-Wealth, indicating harming wife and children; Five Yin seeing Five Yang becomes Rob-Wealth, indicating losses and guarding against petty people, not harming wife"—Yang Day Master seeing Yin same-element indicates harming wife and children, while Yin Day Master seeing Yang same-element indicates losses and caution against petty people but doesn't harm wife. Female fate's Rob Wealth triggers Injuring Officer harming husband: "Yi uses Geng as husband, seeing Bing controlling Geng, hence harming husband." Rob Wealth dividing wealth is analogized through siblings: "Elder seeing younger, younger can defeat elder's wealth and seize elder's wife; younger seeing elder, elder can rob younger's wealth but dares not take younger's wife"—younger sibling (Rob Wealth) dares seize both wealth and wife, elder (Parallel) only dares rob wealth not wife. "Wealth is what people desire; when siblings see it, much competition arises"—wealth is universally desired; siblings meeting it must compete. "How many are like Bo Yi and Shu Qi?"—how many in this world can yield like the legendary brothers? "Male fate seeing abundant Rob Wealth harms wife; female fate seeing abundant Injuring Officer harms husband" is the ultimate principle of Six Relations.

- **核心要点**：
  - 劫财亦名逆刃，与日主同类阴阳相异者
  - 五阳见五阴为败财主克妻害子
  - 五阴见五阳为劫财主破耗防小人不克妻
  - 女命劫财引出伤官克夫
  - 兄弟争财之象：弟敢夺兄妻财，兄只敢劫弟财
  - 男命劫财克妻，女命伤官克夫

- **详细解说**：
  本条专论劫财的性质与六亲应验。劫财"亦名逆刃"，是与日主同类而阴阳相异者。关键区分是败财与劫财："五阳见五阴为败财，主克妻害子；五阴见五阳为劫财，主破耗、防小人，不克妻"——阳日主见阴同类（如甲见乙）为"败财"，主克妻害子；阴日主见阳同类（如乙见甲）为"劫财"，主破耗防小人，但不主克妻。这是因为阳干为兄、阴干为弟的传统伦理观念。女命劫财的特殊之处是"乙以庚为夫，见丙克庚，故克夫"——劫财引出伤官克夫星。兄弟争财的比喻非常精彩："兄见弟，弟能败兄之财，夺兄之妻；弟见兄，兄能劫弟之财，而不敢取弟之妻"——弟（阴干劫财）敢于夺兄之妻财，因为"弟妹贪合"；兄（阳干比肩）只敢劫弟之财而不敢取弟之妻，因为有伦理约束。"如夷、齐能几人"引用伯夷叔齐让国典故，讽刺世人多为财争竞。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_575]` `[trigger: 劫财定义]` `[factor_trigger: rob_wealth]` `[role: 主干]` 亦名'逆刃'，如乙见甲为劫财。 → 《渊海子平·论劫财》
  - `[ns_yhzp_576]` `[trigger: 败财克妻]` `[factor_trigger: defeat_wealth AND direct_wealth]` `[role: 主干依赖]` 五阳见五阴为败财，主克妻害子。 → 《渊海子平·论劫财》
  - `[ns_yhzp_577]` `[trigger: 劫财破耗]` `[factor_trigger: rob_wealth]` `[role: 条件分支]` 五阴见五阳为劫财，主破耗、防小人，不克妻。 → 《渊海子平·论劫财》
  - `[ns_yhzp_578]` `[trigger: 女命劫财克夫]` `[factor_trigger: rob_wealth AND female_fate AND injuring_officer]` `[role: 条件分支]` 乙以庚为夫，见丙克庚，故克夫。 → 《渊海子平·论劫财》
  - `[ns_yhzp_579]` `[trigger: 兄弟争财]` `[factor_trigger: rob_wealth AND parallel AND direct_wealth]` `[role: 条件分支]` 兄见弟，弟能败兄之财，夺兄之妻。 → 《渊海子平·论劫财》
  - `[ns_yhzp_580]` `[trigger: 夷齐让国]` `[factor_trigger: rob_wealth AND direct_wealth]` `[role: 例外处理]` 财者，人之所欲，方令弟兄见之，多有争竞，如夷、齐能几人。 → 《渊海子平·论劫财》
  - `[ns_yhzp_581]` `[trigger: 男劫克妻女伤克夫]` `[factor_trigger: rob_wealth AND injuring_officer AND six_relations]` `[role: 总结]` 男命见劫财多克妻，女命见伤官多克夫。此极论也。 → 《渊海子平·论劫财》"""
    normalized_text_zh: str = """"""
    subject: str = "2. 论劫财"
    factor_refs: list = ['rob_wealth', 'defeat_wealth_proposal', 'rob_wealth']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_2__论劫财_001_L1",
    )
    version: str = "1.0.0"
