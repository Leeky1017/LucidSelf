"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559383
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
    semantic_id="yhzp_v1.0.0_论命细法_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论命细法(SemanticEntry):
    """
    - **原文（source_text）**：
  过房七杀带三刑，母明父暗是偷生。
  我明我暗从化象，父死之时不送灵。
  庚金化成火相时，父亡见血不须疑。
  比肩三合族人害，三刑零落及离妻。
 ...
    """
    
    original_text: str = """- **原文（source_text）**：
  过房七杀带三刑，母明父暗是偷生。
  我明我暗从化象，父死之时不送灵。
  庚金化成火相时，父亡见血不须疑。
  比肩三合族人害，三刑零落及离妻。
  比肩暗损及门房，兄弟无情被罔欺。如带比肩成别象，弟兄不睦报君知。
  妻带三合及坐妻，妻曾认得是亲支。坐妻透妻成别象，定主离妻再娶妻。
  多透妻财须怕妇。妻归绝地不生儿。
  化成别象克正夫，必主欺夫礼义疏。身旺食强亦如此，食明旺相懵然殂。
  阳母专位主伤生，母来父上受其惊。
  天时地利生过月，七杀兼刑顶上偏。印归杀地母有病。
  丙丁双者顶双灵。日禄归时须应梦。小儿无乳食冲刑。
  壬子乙酉对偏生，丙戌丁丑妻获灵。
  背父而生甲乙卯，此时须要记分明。
  (后附多条断语，如：运中忌财作凶财... 戊用癸为妻坐酉好酒... 火入水乡主血疾... 等)

- **分字分词释义**：
  - **过房七杀带三刑**：七杀带三刑（寅巳申/丑戌未）主过继或偷生。
  - **母明父暗是偷生**：印透而财藏或无财，主非婚生或父不明。
  - **背父而生甲乙卯**：甲乙日卯时生，主出生时父不在旁。
  - **比肩三合族人害**：比肩成三合局，主受族人或兄弟之害。
  - **坐妻透妻成别象**：日支财星又天干透财，主离妻再娶。
  - **妻归绝地不生儿**：财星临绝地，主妻不生子。
  - **化成别象克正夫**：化气格克制正官，主女命欺夫克夫。
  - **七杀兼刑顶上偏**：七杀带三刑，主头顶偏斜或有疤痕。
  - **丙丁双者顶双灵**：丙丁双透，主有两个发旋。
  - **火入水乡主血疾**：火日主入水旺之运或地支，主眼疾血疾。

- **规范化释义（primary_lang_explained）**：
  本篇提供了一系列具体的论命细则，多涉及隐秘的身世、家庭关系与疾病：
  1. **身世**：七杀带三刑主过房或偷生；"母明父暗"（印透财藏或无财）主非婚生；"背父而生"（甲乙卯时）主生时父不在旁。
  2. **六亲**：比肩成局主兄弟不睦受欺；财星三合或多透，主畏妻、离妻、娶亲戚之女。
  3. **女命**：化象克夫或食伤过旺，主欺夫、克夫。
  4. **健康与特征**：七杀兼刑主头顶偏斜（顶上偏）；丙丁双透主双顶（两个发旋）；火入水乡主眼疾血疾；小儿食神受冲主缺乳。
  5. **特定断语**：戊日用癸妻坐酉（死地/咸池）主妻好酒；壬癸水盛女多淫滥。

- **完整对等诠释（secondary_lang_full）**：
  **Detailed Method of Fate Analysis**:
  - **Birth Origin**: Seven Killings with Three Penalties indicates adoption or illegitimate birth. "Mother clear, Father obscure" = secret birth. "Born turning back on Father" (Jia/Yi/Mao hour) = Father absent at birth.
  - **Siblings**: Parallels in Three Harmony frame = harm from clansmen; siblings distinct and ruthless.
  - **Wife**: Wealth in Three Harmony or Sitting on Wealth = Wife might be a relative. Multiple Wealth revealed = Fear of wife. Wealth in Extinction = No children from wife.
  - **Husband**: Transformation pattern controlling Husband = Bullying husband. Strong Self with Strong Food = Same result.
  - **Physical Marks**: Seven Killings with Penalties = Slanted crown/head. Double Bing/Ding = Double hair whorls. Fire entering Water = Eye/Blood disease.
  - **Specifics**: Wu Day using Gui Wife sitting on You = Wife loves wine.

- **核心要点**：
  - **出生异象**：过房、偷生、偏生之命理标志
  - **婚姻隐情**：亲上加亲、畏妻、克夫之细断
  - **身体特征**：头旋、头偏、疤痕、眼疾之断法

- **详细解说**：  《论命细法》是子平法中涉及隐秘身世、婚姻细节与身体特征的精细断法篇章。**出生异象**——"过房七杀带三刑"主过继或偷生，"母明父暗是偷生"揭示印透财藏的身世暗示，"背父而生甲乙卯"则指生时父不在旁。**六亲隐情**——"比肩三合族人害"主兄弟不睦受欺，"坐妻透妻成别象"主离妻再娶，"妻归绝地不生儿"主妻不育。**女命克夫**——"化成别象克正夫，必主欺夫礼义疏"，化气格克制官星主欺夫克夫。**身体特征**——"七杀兼刑顶上偏"主头顶偏斜或疤痕，"丙丁双者顶双灵"主双发旋，"火入水乡主血疾"主眼疾。此类细法虽小道，却是验证命理准确性的重要依据，需结合具体命局灵活运用。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_672]` `[trigger: 过房偷生]` `[factor_trigger: guofang AND qisha_dai_sanxing AND tousheng]` `[role: 条件分支]` 过房七杀带三刑，母明父暗是偷生。 → 《渊海子平·论命细法》
  - `[ns_yhzp_673]` `[trigger: 背父而生]` `[factor_trigger: beifu_ersheng AND shengshi_fu_buzaipang]` `[role: 条件分支]` 背父而生甲乙卯，此时须要记分明；生时父不在旁。 → 《渊海子平·论命细法》
  - `[ns_yhzp_674]` `[trigger: 离妻再娶]` `[factor_trigger: zuoqi_touqi AND liqi_zaiqu]` `[role: 条件分支]` 坐妻透妻成别象，定主离妻再娶妻。 → 《渊海子平·论命细法》
  - `[ns_yhzp_675]` `[trigger: 化象克夫]` `[factor_trigger: huaqi_ge AND ke_zhengfu AND qifu]` `[role: 条件分支]` 化成别象克正夫，必主欺夫礼义疏；女命克夫断法。 → 《渊海子平·论命细法》
  - `[ns_yhzp_676]` `[trigger: 头顶偏斜]` `[factor_trigger: qisha_jianxing AND toudingpian AND shenti_tezheng AND bing_ding_shuang AND dingshuangling]` `[role: 条件分支]` 七杀兼刑顶上偏；丙丁双者顶双灵；身体特征断法。 → 《渊海子平·论命细法》
  - `[ns_yhzp_677]` `[trigger: 火入水疾]` `[factor_trigger: huo_rushui AND xueji AND wuxing_kezhan]` `[role: 条件分支]` 火入水乡主血疾；五行克战致疾病。 → 《渊海子平·论命细法》
  - `[ns_yhzp_678]` `[trigger: 论命细法纲领]` `[factor_trigger: lunming_xifa AND shenshixijie AND shenti_tezheng]` `[role: 总结]` 论命细法提供隐秘身世、婚姻细节与身体特征的精细断法。 → 《渊海子平·论命细法》
  - `[ns_yhzp_679]` `[trigger: 比肩三合族害]` `[factor_trigger: bijian_sanhe AND zuhai AND xiongdi_buhe]` `[role: 条件分支]` 比肩三合族人害；比肩成局主兄弟不睦受族人欺害。 → 《渊海子平·论命细法》"""
    normalized_text_zh: str = """"""
    subject: str = "论命细法"
    factor_refs: list = ['adoption', 'illegitimate_birth', 'mother_clear_father_obscure', 'double_crown']
    
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
        l1_anchor="yhzp_v1.0.0_论命细法_001_L1",
    )
    version: str = "1.0.0"
