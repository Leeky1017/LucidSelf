"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558722
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
    semantic_id="yhzp_v1.0.0_论太岁吉凶_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论太岁吉凶(SemanticEntry):
    """
    - **原文（source_text）**：太岁乃年中天子，故不可犯，犯之则凶。经云：'日犯岁君，灾殃必重；五行有救，其年反必招财。'且如甲日见戊年，太岁是也，克重者死。甲乙若寅卯亥未日时者，犯克岁君...
    """
    
    original_text: str = """- **原文（source_text）**：太岁乃年中天子，故不可犯，犯之则凶。经云：'日犯岁君，灾殃必重；五行有救，其年反必招财。'且如甲日见戊年，太岁是也，克重者死。甲乙若寅卯亥未日时者，犯克岁君，决死无疑；有救则吉，乃八字庚辛巳酉丑金局也，经云：'戊己愁逢甲乙，干头须要庚辛'；或丙丁火局焚木，有灾勿咎，效此推之；或得己合甲亦解之。大抵太岁不可伤之，相生者吉；乃五行有救，其年反必为财。犯岁君者，其年必主凶丧、克妻妾及破财是非、犯上之悔；加以勾绞、空亡、咸池、宅墓、病符、死符、白虎、阳刃诸杀并临，祸患百出。

- **分字分词释义**：
  - **太岁**：流年天干地支，又称"岁君"，为一年之主宰，如君王般尊崇不可冒犯。
  - **犯太岁**：日干克制太岁天干，形成下犯上的关系，为大忌。
  - **五行有救**：命中有克制日干的五行，可以"救"太岁免受日干之克。
  - **戊己愁逢甲乙**：戊己土最怕甲乙木来克，需有庚辛金制木方解。
  - **己合甲**：甲己合化土，可以化解甲木克戊土的关系。
  - **勾绞**：神煞名，主牵连纠葛之事。
  - **咸池**：神煞名，主桃花色情之事。
  - **病符/死符**：神煞名，主疾病或丧亡之事。
  - **白虎**：神煞名，主血光凶险之事。

- **规范化释义（primary_lang_explained）**：太岁如君王不可犯。日干克太岁为"犯上"主凶，但若有五行救应可化凶为吉。例如甲日见戊年太岁，甲木克戊土为犯，若命中有庚辛金克甲木，则金救土而解灾；或有己土合甲木亦可化解。太岁不可伤，相生者吉；犯之主凶丧克妻破财，加诸凶煞则祸患百出。

- **完整对等诠释（secondary_lang_full）**：Tai Sui (Annual Sovereign) functions like a monarch—Day Stem controlling Tai Sui constitutes offending the superior bringing misfortune. However, with Five-Element rescue, disaster transforms to fortune. For instance, Jia Day meeting Wu Year Tai Sui—Jia Wood controls Wu Earth as offense; if natal chart contains Geng/Xin Metal controlling Jia Wood, Metal rescues Earth resolving disaster; or Ji Earth combining Jia Wood also neutralizes. Tai Sui must not be harmed; mutual generation brings auspice; offense brings mourning, spouse harm, wealth loss—compounded by inauspicious spirits multiplies calamities.

- **核心要点**：
  - 太岁为年中天子，如君王不可冒犯
  - 日干克太岁为"犯上"，主凶灾祸患
  - 五行有救可化凶为吉，如庚辛制甲乙救戊己
  - 天干合化亦可化解犯太岁，如己合甲
  - 犯太岁加凶煞（勾绞、空亡、咸池等）则祸患百出

- **详细解说**：  
  本条论述太岁吉凶的核心法则。太岁即流年干支，被尊为"年中天子"，代表一年的主宰力量。日干克太岁形成"下犯上"的关系，是命理中的大忌。文中举例：甲木日干遇戊土太岁年，甲木克戊土即为犯太岁。若命中有庚辛金局克制甲木，则金救土而化解灾厄；或命中有己土与甲木合化，也可化解冲突。这体现了子平法"五行有救"的重要原则：任何凶险的五行关系，若有适当的制化或合化，都可能转危为安。犯太岁的后果包括凶丧、克妻妾、破财是非等，若再加勾绞、空亡、咸池、病符、死符、白虎、阳刃等凶煞并临，则祸患百出。此条是流年断法的基础理论。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_622]` `[trigger: 太岁概念]` `[factor_trigger: tai_sui]` `[role: 主干]` 太岁乃年中天子，故不可犯，犯之则凶。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_623]` `[trigger: 犯太岁]` `[factor_trigger: tai_sui AND day_stem AND fan_taisui]` `[role: 条件分支]` 日犯岁君，灾殃必重。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_624]` `[trigger: 五行有救]` `[factor_trigger: five_element_control]` `[role: 例外处理]` 五行有救，其年反必招财。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_625]` `[trigger: 戊己见甲乙]` `[factor_trigger: tiangan_wu OR tiangan_ji AND tiangan_jia OR tiangan_yi]` `[role: 条件分支]` 戊己愁逢甲乙，干头须要庚辛。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_626]` `[trigger: 甲己合化]` `[factor_trigger: tiangan_jia AND tiangan_ji]` `[role: 例外处理]` 得己合甲亦解之。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_627]` `[trigger: 犯太岁凶象]` `[factor_trigger: tai_sui]` `[role: 条件分支]` 犯岁君者，其年必主凶丧、克妻妾及破财是非。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_628]` `[trigger: 凶煞叠加]` `[factor_trigger: ]` `[role: 条件分支]` 加以勾绞、空亡、咸池、白虎、阳刃诸杀并临，祸患百出。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_421]` `[trigger: 七杀旺]` `[factor_trigger: seven_killings_strong]` `[role: 条件分支]` 七杀旺无制主凶险。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_422]` `[trigger: 天干配脏]` `[factor_trigger: stem_organ_mapping]` `[role: 主干]` 天干配脏腑：甲胆乙肝丙小肠等。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_423]` `[trigger: 太岁]` `[factor_trigger: tai_sui]` `[role: 主干]` 太岁为流年天子，主一年吉凶。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_424]` `[trigger: 三刑]` `[factor_trigger: three_penalties]` `[role: 条件分支]` 三刑主灾厄，刑中有刑更凶。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_425]` `[trigger: 天乙]` `[factor_trigger: tianyi]` `[role: 条件分支]` 天乙贵人为第一吉神。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_426]` `[trigger: 化象]` `[factor_trigger: transformation_image]` `[role: 条件分支]` 化象者合化成功之格。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_427]` `[trigger: 传送]` `[factor_trigger: transmission]` `[role: 条件分支]` 传送者引发也，运引命发。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_428]` `[trigger: 用神有力]` `[factor_trigger: use_god_strong]` `[role: 条件分支]` 用神有力主吉，无力主凶。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_429]` `[trigger: 德]` `[factor_trigger: virtue]` `[role: 条件分支]` 天德月德为吉神，主化灾。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_430]` `[trigger: 空亡]` `[factor_trigger: void]` `[role: 条件分支]` 空亡主虚无，逢填实方能发用。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_431]` `[trigger: 战格]` `[factor_trigger: warring_pattern]` `[role: 条件分支]` 战格者冲克交战之格，主动荡。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_432]` `[trigger: 财]` `[factor_trigger: wealth]` `[role: 主干]` 财为我克之神，主财富。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_433]` `[trigger: 财运]` `[factor_trigger: wealth_fortune]` `[role: 条件分支]` 身旺行财运主发财。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_434]` `[trigger: 财官]` `[factor_trigger: wealth_officer]` `[role: 条件分支]` 财官双美主富贵。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_435]` `[trigger: 财官印]` `[factor_trigger: wealth_officer_seal]` `[role: 条件分支]` 财官印三奇全主大贵。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_436]` `[trigger: 财官旺]` `[factor_trigger: wealth_officer_strong]` `[role: 条件分支]` 财官旺身旺主富贵。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_437]` `[trigger: 财旺]` `[factor_trigger: wealth_strong]` `[role: 条件分支]` 财旺身强主富。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_438]` `[trigger: 妻]` `[factor_trigger: wife]` `[role: 主干]` 正财为妻星，日支为妻宫。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_439]` `[trigger: 木多]` `[factor_trigger: wood_excess]` `[role: 条件分支]` 木多主肝病。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_440]` `[trigger: 年]` `[factor_trigger: year]` `[role: 主干]` 年柱为根，代表祖上。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_441]` `[trigger: 年柱]` `[factor_trigger: year_post]` `[role: 主干]` 年柱为四柱之首。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_442]` `[trigger: 渊海]` `[factor_trigger: yuanhai]` `[role: 主干]` 渊海子平为命理经典。 → 《渊海子平·论太岁吉凶》
  - `[ns_yhzp_443]` `[trigger: 原元]` `[factor_trigger: yuanyuan]` `[role: 主干]` 原元者命之根本也。 → 《渊海子平·论太岁吉凶》"""
    normalized_text_zh: str = """"""
    subject: str = "论太岁吉凶"
    factor_refs: list = ['tai_sui', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="yhzp_v1.0.0_论太岁吉凶_001_L1",
    )
    version: str = "1.0.0"
