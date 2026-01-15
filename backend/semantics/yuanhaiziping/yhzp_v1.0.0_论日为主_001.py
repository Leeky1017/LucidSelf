"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558690
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
    semantic_id="yhzp_v1.0.0_论日为主_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论日为主(SemanticEntry):
    """
    - **原文（source_text）**：  
  予尝观唐书所载，有李虚中者，取人所生年月日时干支生克，论命之贵贱寿夭之说，已详之矣！至于宋时，方有子平之说；取日干为主，以年为根，以月为苗，以日为...
    """
    
    original_text: str = """- **原文（source_text）**：  
  予尝观唐书所载，有李虚中者，取人所生年月日时干支生克，论命之贵贱寿夭之说，已详之矣！至于宋时，方有子平之说；取日干为主，以年为根，以月为苗，以日为花，以时为果；以生旺死绝休囚制化，决人生休咎。其理必然矣，复有何疑哉！
  
  一曰官，分之阴阳，曰官、曰杀，甲乙见庚辛也；二曰财，分之阴阳，曰正财、偏财，甲乙见戊己也；三曰生气之阴阳，曰印绶、曰倒食，甲乙见壬癸是也；四曰窃气之阴阳，曰食神、曰伤官，甲乙见丙丁是也；五曰同类之阴阳，曰劫财、曰阳刃，甲乙见甲乙是也。大抵贵贱寿夭死生，皆不出于五者；倘有妄立格局，从列其名，而无实用，其飞天禄马、倒冲井栏叉，即伤官，析而为之。举此一端，馀可知矣！
  
  以日为主，年为本，月为提纲，时为辅佐。
  
  以日为主，大要看日加临于甚度，或身旺？或身弱？又看地支有何格局？金木水火土之数；后看月令中金木水火土，何者旺？又看岁运有何旺？却次日下消详。此非是拘之一隅之说也。
  
  且如甲子日生，四柱中有个申字，合用子辰为水局；次看馀辰有何损益？四柱中有何字，损其甲子日主之秀气？有坏其月神，则要别制之，不要益之。论命者切不可泥之，月令消详；故表而出之。

- **分字分词释义**：
  - **李虚中**：唐代命理家，传为年月日时四柱推命法的开创者。
  - **子平**：宋代徐子平（徐大升），创立以日干为主的子平法，现代八字命理的核心体系。
  - **日干为主**：以出生日的天干作为命主本人的代表，子平法区别于其他体系的核心特征。
  - **年为根、月为苗、日为花、时为果**：四柱功能定位，年柱代表祖基，月柱代表父母环境，日柱代表自身配偶，时柱代表子女后代。
  - **十神**：官杀、财、印、食伤、比劫五类，依日干与他干生克关系定义的核心分析工具。
  - **官杀**：克我者，阴阳相同为七杀（偏官），阴阳相异为正官。
  - **财**：我克者，阴阳相同为偏财，阴阳相异为正财。
  - **印**：生我者，阴阳相异为正印（印绶），阴阳相同为偏印（倒食）。
  - **食伤**：我生者，阴阳相异为食神，阴阳相同为伤官。
  - **比劫**：同类者，阴阳相同为比肩，阴阳相异为劫财（阳刃）。
  - **提纲**：月令，四柱中最重要的节点，主宰命局旺衰。

- **规范化释义（primary_lang_explained）**：  
  这条阐述子平法的核心理论：以日干为中心的命理体系。作者首先回顾历史，指出唐代李虚中已使用年月日时四柱论命，但到宋代徐子平才确立"以日干为主"的方法论。子平法将四柱比作树木：年为根（祖基），月为苗（父母环境），日为花（自身配偶），时为果（子女后代）。判断命运时综合考虑生旺死绝休囚制化等状态。接着阐述十神体系：根据日干与他干的生克关系，分出官杀、财、印、食伤、比劫五大类，每类再分阴阳为十神。官杀（克我）分正官与七杀；财（我克）分正财与偏财；印（生我）分正印与偏印；食伤（我生）分食神与伤官；比劫（同类）分比肩与劫财。人生贵贱寿夭皆可从这十神关系中推断。作者强调许多传统格局名称（如飞天禄马）实为同一原理的不同表述，无需妄立名目。论命时以日干为主，年月时为辅，先看日主旺衰，再看地支格局，最后看月令、岁运的影响，综合判断，不可机械教条。

- **完整对等诠释（secondary_lang_full）**：  
  This passage expounds the core theory of Ziping Method: the fate-analysis system centered on the Day Stem. The author first reviews history, noting that Li Xuzhong of Tang Dynasty already used the Four Pillars for fate analysis, but Xu Ziping of Song Dynasty established the methodology of "taking the Day Stem as primary." Ziping Method likens the Four Pillars to a tree: Year as root (ancestral foundation), Month as sprout (parents and environment), Day as flower (self and spouse), Hour as fruit (children and descendants). When judging fate, one comprehensively considers states of prosperity, decline, death, extinction, rest, imprisonment, control, and transformation. Next comes the Ten Gods system: based on generation-control relationships between Day Stem and other Stems, five major categories emerge—Officials/Killings, Wealth, Seals, Food/Injury, and Parallels/Robs—each further divided by yin-yang polarity into ten deities. Officials/Killings (controlling me) split into Direct Officer and Seven Killings; Wealth (I control) splits into Direct and Indirect Wealth; Seals (generating me) split into Direct Seal and Indirect Seal; Food/Injury (I generate) splits into Eating God and Injuring Officer; Parallels/Robs (same category) splits into Shoulder and Rob Wealth. Human life's nobility and longevity can be deduced from these ten relational dynamics. The author emphasizes that many traditional pattern names are merely different labels for the same principles. When analyzing fate, take Day Stem as primary with Year-Month-Hour as auxiliary; first assess Day Master's strength, then examine Earthly Branches' patterns, finally consider Month Command and yearly cycles—synthesizing judgment without mechanical rigidity.

- **核心要点**：
  - 子平法核心：以日干为主，日干代表命主本人
  - 四柱定位：年根（祖）、月苗（父母）、日花（自身配偶）、时果（子女）
  - 十神体系：根据日干与他干生克关系分出十神，是判断六亲格局的核心工具
  - 判断顺序：先看日主旺衰，次看地支格局，再看月令岁运
  - 反对妄立格局：很多传统格局名称本质相同

- **详细解说**：  
  这是《渊海子平》全书最核心的理论基础，标志着子平法与其他命理体系的根本区别。子平法的革命性在于：将日干确立为命主本人的唯一代表，所有判断都围绕日干展开。这种"主体化"的方法论使命理分析变得更清晰可操作。四柱的"根苗花果"比喻体现了时间流向与人生阶段的对应。十神体系是核心工具，通过日干与他干的五行生克关系建立起完整的六亲与命运分析框架。十神不仅代表六亲关系，更代表命局的功能与格局。作者特别强调"贵贱寿夭死生，皆不出于五者"，意即所有命运判断都可归结为十神的生克制化关系。对于"飞天禄马"等传统格局，作者认为不过是十神关系的不同表述。论命方法论也很重要：先看日主旺衰，次看地支格局，再看月令，最后看岁运，综合判断不可拘泥。

- **校勘与字词辨析**：
  - **李虚中**：历史上确有其人，但《渊海子平》作者托名李虚中，实为宋元间人所作。
  - **倒食**：偏印的别名，因偏印克食神，故称"倒食"或"枭神"。
  - **阳刃**：劫财的别称，因劫财力量强劲如刃。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_024]` `[trigger: 子平法核心]` `[factor_trigger: day_stem]` `[role: 主干]` 以日干为主，日干代表命主本人，是子平法的核心特征。 → 《渊海子平·论日为主》
  - `[ns_yhzp_025]` `[trigger: 四柱定位]` `[factor_trigger: four_pillars_position AND guo AND miao AND month_pillar]` `[role: 主干依赖]` 年为根、月为苗、日为花、时为果，四柱各有功能定位。 → 《渊海子平·论日为主》
  - `[ns_yhzp_026]` `[trigger: 十神体系]` `[factor_trigger: ten_gods]` `[role: 主干依赖]` 根据日干与他干生克关系分出十神，是判断六亲格局的核心工具。 → 《渊海子平·论日为主》
  - `[ns_yhzp_027]` `[trigger: 官杀分类]` `[factor_trigger: ten_gods]` `[role: 条件分支]` 官杀分正官与七杀，克我而阴阳相异为正官，相同为七杀。 → 《渊海子平·论日为主》
  - `[ns_yhzp_028]` `[trigger: 财星分类]` `[factor_trigger: ten_gods]` `[role: 条件分支]` 财分正财与偏财，我克而阴阳相异为正财，相同为偏财。 → 《渊海子平·论日为主》
  - `[ns_yhzp_029]` `[trigger: 印星分类]` `[factor_trigger: ten_gods]` `[role: 条件分支]` 印分正印与偏印，生我而阴阳相异为正印，相同为偏印。 → 《渊海子平·论日为主》
  - `[ns_yhzp_030]` `[trigger: 食伤分类]` `[factor_trigger: ten_gods]` `[role: 条件分支]` 食伤分食神与伤官，我生而阴阳相异为食神，相同为伤官。 → 《渊海子平·论日为主》
  - `[ns_yhzp_031]` `[trigger: 比劫分类]` `[factor_trigger: ten_gods]` `[role: 条件分支]` 比劫分比肩与劫财，同类而阴阳相同为比肩，相异为劫财。 → 《渊海子平·论日为主》
  - `[ns_yhzp_032]` `[trigger: 论命顺序]` `[factor_trigger: day_master_strength]` `[role: 总结]` 论命时先看日主旺衰，次看地支格局，再看月令岁运，综合判断。 → 《渊海子平·论日为主》
  - `[ns_yhzp_373]` `[trigger: 吉运起]` `[factor_trigger: good_luck_start]` `[role: 结果]` 运逢喜用，吉运起而发达。 → 《渊海子平·论日为主》
  - `[ns_yhzp_374]` `[trigger: 害破]` `[factor_trigger: harm_break]` `[role: 条件分支]` 害破主不顺，暗中破坏。 → 《渊海子平·论日为主》
  - `[ns_yhzp_375]` `[trigger: 害官]` `[factor_trigger: harm_officer]` `[role: 条件分支]` 伤官害官，主官灾。 → 《渊海子平·论日为主》
  - `[ns_yhzp_376]` `[trigger: 伤官见官]` `[factor_trigger: harm_officer_meets_officer]` `[role: 条件分支]` 伤官见官，为祸百端。 → 《渊海子平·论日为主》
  - `[ns_yhzp_377]` `[trigger: 六合]` `[factor_trigger: harmony]` `[role: 条件分支]` 六合主合好，合则有情。 → 《渊海子平·论日为主》
  - `[ns_yhzp_378]` `[trigger: 克夫]` `[factor_trigger: harms_husband]` `[role: 条件分支]` 官杀混杂主克夫，女命大忌。 → 《渊海子平·论日为主》
  - `[ns_yhzp_379]` `[trigger: 天]` `[factor_trigger: heaven]` `[role: 主干]` 天干为天元，主显象。 → 《渊海子平·论日为主》
  - `[ns_yhzp_380]` `[trigger: 驿马]` `[factor_trigger: horse]` `[role: 条件分支]` 驿马主迁动、远行。 → 《渊海子平·论日为主》
  - `[ns_yhzp_381]` `[trigger: 夫]` `[factor_trigger: husband]` `[role: 主干]` 官星为夫星，日支为夫宫。 → 《渊海子平·论日为主》
  - `[ns_yhzp_382]` `[trigger: 夫旺]` `[factor_trigger: husband_prosperity]` `[role: 结果]` 官星得用主夫贵。 → 《渊海子平·论日为主》
  - `[ns_yhzp_383]` `[trigger: 疾病]` `[factor_trigger: illness]` `[role: 结果]` 五行受克主疾病。 → 《渊海子平·论日为主》
  - `[ns_yhzp_384]` `[trigger: 偏官]` `[factor_trigger: indirect_officer AND direct_officer_single]` `[role: 条件分支]` 偏官即七杀，克我而阴阳相同。 → 《渊海子平·论日为主》
  - `[ns_yhzp_385]` `[trigger: 偏财空]` `[factor_trigger: indirect_wealth_void]` `[role: 条件分支]` 偏财空亡主父缘薄。 → 《渊海子平·论日为主》
  - `[ns_yhzp_386]` `[trigger: 偏财弱]` `[factor_trigger: indirect_wealth_weak]` `[role: 条件分支]` 偏财弱主父不利。 → 《渊海子平·论日为主》
  - `[ns_yhzp_387]` `[trigger: 伤尽]` `[factor_trigger: injury_fully]` `[role: 条件分支]` 伤官伤尽最为奇，主贵显。 → 《渊海子平·论日为主》
  - `[ns_yhzp_388]` `[trigger: 杀]` `[factor_trigger: killing]` `[role: 条件分支]` 七杀无制主凶险，有制主权。 → 《渊海子平·论日为主》
  - `[ns_yhzp_389]` `[trigger: 杀运]` `[factor_trigger: killing_luck]` `[role: 条件分支]` 身弱行杀运主凶。 → 《渊海子平·论日为主》
  - `[ns_yhzp_390]` `[trigger: 懒惰]` `[factor_trigger: lazy]` `[role: 结果]` 日主无气主懒惰。 → 《渊海子平·论日为主》
  - `[ns_yhzp_391]` `[trigger: 凶神]` `[factor_trigger: malefic]` `[role: 条件分支]` 凶神宜制化，不宜生旺。 → 《渊海子平·论日为主》
  - `[ns_yhzp_392]` `[trigger: 多合]` `[factor_trigger: multiple_combines]` `[role: 条件分支]` 多合主人情世故，女命多合不贞。 → 《渊海子平·论日为主》
  - `[ns_yhzp_393]` `[trigger: 无金]` `[factor_trigger: no_metal]` `[role: 条件分支]` 无金主肺病。 → 《渊海子平·论日为主》
  - `[ns_yhzp_394]` `[trigger: 贵]` `[factor_trigger: nobility]` `[role: 结果]` 格局成就主贵显。 → 《渊海子平·论日为主》
  - `[ns_yhzp_395]` `[trigger: 官]` `[factor_trigger: officer]` `[role: 条件分支]` 正官为克我之善神，主地位。 → 《渊海子平·论日为主》
  - `[ns_yhzp_396]` `[trigger: 官杀无制]` `[factor_trigger: officer_killing_no_control]` `[role: 条件分支]` 官杀无制主凶险。 → 《渊海子平·论日为主》"""
    normalized_text_zh: str = """"""
    subject: str = "论日为主"
    factor_refs: list = ['day_stem', 'ten_gods', 'ten_gods', 'ten_gods', 'ten_gods', 'ten_gods', 'ten_gods']
    
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
        l1_anchor="yhzp_v1.0.0_论日为主_001_L1",
    )
    version: str = "1.0.0"
