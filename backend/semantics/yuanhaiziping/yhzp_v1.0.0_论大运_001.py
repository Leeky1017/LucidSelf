"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558747
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
    semantic_id="yhzp_v1.0.0_论大运_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论大运(SemanticEntry):
    """
    - **原文（source_text）**：夫大运者，以天干曰'五运'，地支曰'六气'，故名'范气'。子平之法，大运看支，岁君看干，交运同接木。出癸入甲，如返汗之人；且如甲戌接癸亥，此乃干支接木。丑运...
    """
    
    original_text: str = """- **原文（source_text）**：夫大运者，以天干曰'五运'，地支曰'六气'，故名'范气'。子平之法，大运看支，岁君看干，交运同接木。出癸入甲，如返汗之人；且如甲戌接癸亥，此乃干支接木。丑运交寅，辰交巳，未交申，戌交亥，此乃转角接木。东南西北四方转角，谓之接木；格局凶者死，格局善者灾。寅卯辰一气，申酉戌一气，亥子丑一气；气之相连，皆非接木之说。

- **分字分词释义**：
  - **大运**：十年一运的人生阶段，由月柱起运，男女顺逆不同。
  - **五运**：天干甲乙丙丁戊己庚辛壬癸十干配五行，运用于大运天干。
  - **六气**：地支十二支配六气（风寒暑湿燥火），运用于大运地支。
  - **范气**：五运六气的统称，指大运干支所代表的气机。
  - **交运**：大运转换的时间节点，如从一步运进入下一步运。
  - **接木**：运程交接如树木嫁接，新旧交替时最为脆弱。
  - **转角接木**：四墓库（丑辰未戌）与四生（寅巳申亥）之间的转换，东西南北四方转角，最为凶险。
  - **三支一气**：寅卯辰（东方木）、巳午未（南方火）、申酉戌（西方金）、亥子丑（北方水）连续相接，气脉相连非接木。
  - **返汗之人**：病后初愈复发汗出之人，比喻运程交接时身体脆弱。

- **规范化释义（primary_lang_explained）**：大运天干为五运，地支为六气。子平法大运看地支，流年看天干。交运如接木，尤其转角接木（如丑交寅、辰交巳等）最为关键，格局凶者遇之主死，格局善者主灾。若三支一气相连（如寅卯辰）则非接木。

- **完整对等诠释（secondary_lang_full）**：Major Cycles—Heavenly Stems called Five Cycles, Earthly Branches called Six Qi. Ziping Method examines Branches in Major Cycles, Stems in Annual Cycles. Cycle transitions like grafting trees, especially corner-turning grafts (Chou to Yin, Chen to Si, etc.) most critical—inauspicious patterns bring death, auspicious patterns bring disaster. When three Branches form continuous qi (like Yin-Mao-Chen), it's not grafting.

- **核心要点**：
  - 大运天干为五运，地支为六气
  - 子平法大运看地支，流年看天干
  - 交运如接木，新旧交替时最脆弱
  - 转角接木（丑交寅、辰交巳等）最凶险
  - 三支一气相连（寅卯辰等）则非接木

- **详细解说**：  
  本条论述大运的基本概念与交运吉凶。大运以天干配五运、地支配六气，统称"范气"，代表人生各阶段的气运走势。子平法的核心原则是"大运看支，岁君看干"，即大运主要看地支对命局的影响，流年主要看天干。"交运"是运程转换的关键时刻，本文用"接木"比喻——如同树木嫁接，新旧交替时最为脆弱。尤其是"转角接木"：丑运交寅、辰运交巳、未运交申、戌运交亥，这四个转换点是东南西北四方的"转角"，从墓库转入生旺之地，气机骤变最为凶险。格局凶者遇转角接木主死，格局善者亦主灾。但若三支一气相连（如寅卯辰东方木局连续），则气脉贯通而非接木，不以凶论。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_659]` `[trigger: 大运定义]` `[factor_trigger: dayun_def]` `[role: 主干]` 大运者，以天干曰五运，地支曰六气。 → 《渊海子平·论大运》
  - `[ns_yhzp_660]` `[trigger: 大运看法]` `[factor_trigger: dayun_method]` `[role: 主干依赖]` 子平之法，大运看支，岁君看干。 → 《渊海子平·论大运》
  - `[ns_yhzp_685]` `[trigger: 交运接木]` `[factor_trigger: jiaoyun_jiemu AND jiemu_jiedian]` `[role: 主干依赖]` 交运同接木，如树木嫁接，新旧交替时最脆弱。 → 《渊海子平·论大运》
  - `[ns_yhzp_686]` `[trigger: 转角接木]` `[factor_trigger: zhuanjiao_jiemu]` `[role: 条件分支]` 丑运交寅，辰交巳，未交申，戌交亥，此乃转角接木，最为凶险。 → 《渊海子平·论大运》
  - `[ns_yhzp_687]` `[trigger: 转角接木凶象]` `[factor_trigger: zhuanjiao_xiongxiang]` `[role: 条件分支]` 东南西北四方转角，格局凶者死，格局善者灾。 → 《渊海子平·论大运》
  - `[ns_yhzp_688]` `[trigger: 三支一气]` `[factor_trigger: sanzhi_yiqi]` `[role: 例外处理]` 寅卯辰一气，申酉戌一气，亥子丑一气；气之相连，皆非接木。 → 《渊海子平·论大运》
  - `[ns_yhzp_689]` `[trigger: 返汗之人]` `[factor_trigger: fanhan_ren]` `[role: 总结]` 出癸入甲，如返汗之人，运程交接时身体脆弱。 → 《渊海子平·论大运》"""
    normalized_text_zh: str = """"""
    subject: str = "论大运"
    factor_refs: list = ['major_cycle', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="yhzp_v1.0.0_论大运_001_L1",
    )
    version: str = "1.0.0"
