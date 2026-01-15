"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725506
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
    semantic_id="zw_v1.0.0_1_紫微星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 1紫微星(SemanticEntry):
    """
    - **原文（source_text）**：

  问：紫微所主若何？
  
  答曰：紫微属土，乃中天之尊星，为帝座，主掌造化枢机。人生主宰，仗五行，育万物，以人命为之，立定数安星缠各根所司处年数内...
    """
    
    original_text: str = """- **原文（source_text）**：

  问：紫微所主若何？
  
  答曰：紫微属土，乃中天之尊星，为帝座，主掌造化枢机。人生主宰，仗五行，育万物，以人命为之，立定数安星缠各根所司处年数内，常掌爵禄。诸宫降福，能消百恶，须看三台。盖紫微守命是中台，前一位是上台，后一位为下台，俱看在庙旺之乡否，有何吉凶之守照。如庙旺化吉甚妙，陷又化凶甚凶，吉限不为美，凶限则凶也。人之身命，若值禄存同宫，日月三合相照，贵不可言。无辅弼同行，则为孤君，虽美玉不足。更与诸杀同宫，或诸吉合照，则君子在野，小人在位，主人奸诈假义，平生恶积。与囚同居，无左右相佐，定为胥吏。如落疾厄、兄弟、奴仆相貌四陷宫，主人劳碌，作事无成，虽得相助，亦不为福。
  
  希夷先生曰：紫微为帝座，在诸宫，能降福消灾，解诸星之恶虚，能制火铃为善，能降七杀为权。若得府相、左右、昌曲吉集，无有不贵，不然亦主巨富。纵有四杀冲破，亦作中局。若遇破军，在辰戌丑未，主为臣不忠，为子不孝之论。女命逢之，作贵妇断。加杀冲破，亦作平常，不为下贱。
  
  歌曰：紫微原属土，官禄宫主星。有相为有用，无相为孤君。诸宫皆降福，逢凶福自申。文昌发科甲，文曲受皇恩。僧道有师号，快乐度春秋。众星皆拱照，为吏协公平。女人会帝座，遇吉事贵人。若与桃花会，飘荡落风尘。擎羊火铃聚，用窃狗偷群。三方有吉拱，方作贵人评。若还无辅弼，诸恶共欺凌。帝为无道主，考究要知因。二限若遇帝，喜气自然新。
  
  玉蟾先生曰：紫微乃中天星主，为众星之枢纽，为造化之根柢，为人命之主宰，掌五行，育万物，各有所司。以左辅、右弼为相，以天相、昌曲为从，以魁钺为传令，以日月为分司，以禄马为掌爵之司，以天府为帑藏之主。身命逢之，不胜其吉。如遇四杀羊陀火铃劫空，机梁冲破，定是僧道。此星在命，为人厚重，面紫色，专作吉断。

- **分字分词释义**：

  - **紫微**：北斗星系中最尊贵的帝座星，象征权威、统领与核心地位。
  - **帝座**：皇帝御座，象征最高权力与统摄枢纽。
  - **造化枢机**：造化指天地万物之生成变化，枢机为运转之核心关键。
  - **三台**：上台、中台、下台三星，与紫微形成护卫配置，中台为紫微本宫。
  - **孤君**：没有辅佐的帝王，虽居高位却无人相助，难以施政。
  - **降福消灾**：紫微能化解凶象、带来福泽的核心功能。
  - **制火铃为善**：将火星、铃星的凶性转化为可用之力。
  - **降七杀为权**：将七杀的杀伐之气转化为权威与执行力。

- **规范化释义（primary_lang_explained）**：

  紫微为中天帝座，是紫微斗数体系中最尊贵的主星，属土性，主掌造化枢机与爵禄福德。紫微在命盘中如同皇帝御座，能够统领诸星、降福消灾、解诸恶虚。但帝座需要配合才能发挥：若有辅弼同行、禄存相守、日月三合照临，则贵不可言；若无辅弼相佐，则为"孤君"，虽居高位却无人相助，难以真正成贵。
  
  判断紫微格局需看"三台"配置：紫微本宫为中台，前一位为上台，后一位为下台，三台均需庙旺方为完整贵格。紫微的特殊能力在于"化恶为用"：能制火铃为善、降七杀为权，纵有四杀冲破，也能维持中局而不至败落。但若紫微落入疾厄、兄弟、奴仆、相貌等"四陷宫"，则劳碌无成，贵气难发。女命逢紫微作贵妇断，即便加杀冲破，也不至下贱。

- **完整对等诠释（secondary_lang_full）**：

  Ziwei (Purple Sovereign) is the supreme star of the Northern Dipper system, representing the imperial throne at the center of heaven. As the most honorable principal star in Ziwei Doushu, it governs the pivot of creation, ranks, and blessings. In a chart, Ziwei functions like an emperor's seat—it can command all stars, dispel disasters, and transform malefic influences. However, a throne requires ministers to function: when accompanied by assistants like Zuo Fu and You Bi, with Lucun in support and Sun-Moon in triangular illumination, the native achieves undeniable nobility; without such companions, Ziwei becomes a "Lonely Emperor"—high in position but lacking helpers, unable to manifest true greatness.
  
  Reading Ziwei's pattern requires examining the "Three Terraces" configuration: Ziwei's own palace forms the Middle Terrace, with Upper and Lower Terraces in adjacent positions. All three must be dignified for a complete noble pattern. Ziwei's unique power lies in "transforming evil into utility": it can subdue Fire and Bell stars into beneficial forces, convert Qisha's killing energy into authoritative power. Even when struck by the Four Killers, the configuration maintains middle-grade status rather than collapsing. However, if Ziwei falls into the "Four Declining Houses" (Illness, Siblings, Servants, Appearance), the native toils without achievement and nobility fails to manifest. For women's charts, Ziwei indicates a noble lady; even with malefic disruption, she does not descend to lowly status.

- **核心要点**：

  - 紫微为中天帝座尊星，主掌造化枢机、爵禄福德
  - 紫微需辅弼相佐方成贵格，无辅弼则为"孤君"
  - 三台配置（上中下台）需庙旺方为完整
  - 紫微能制火铃、降七杀，化恶为用
  - 与禄存同宫、日月三合照临者贵不可言
  - 落四陷宫（疾厄、兄弟、奴仆、相貌）则劳碌无成
  - 女命逢紫微作贵妇断，加杀亦不下贱

- **详细解说**：

  1. **帝座核心地位**：紫微在斗数中的地位相当于"众星之主"，所有其他星曜都围绕它运转。但这种核心地位需要"配合"才能发挥——正如皇帝需要宰相辅佐、官员执行，紫微需要辅弼、昌曲、魁钺等吉星相佐，才能真正施展"降福消灾"的功能。

  2. **孤君与有相**：本条最重要的判断点是"有相为有用，无相为孤君"。有辅弼同行、府相昌曲吉集者，贵气得以落实；无辅佐而孤立的紫微，虽占据尊位却无力实现其价值，多见有才无位、有志难伸的状态。

  3. **化恶为用的能力**：紫微与一般吉星不同，它能够"制火铃为善、降七杀为权"——将凶星的破坏力转化为可用的执行力与权威感。这意味着紫微坐命者，即便遇到凶星，也有化解的潜力，但前提是紫微本身得地且有辅佐。

  4. **四陷宫的限制**：紫微落入疾厄、兄弟、奴仆、相貌等"四陷宫"时，帝座的尊贵难以发挥，反而主劳碌作事无成。这提醒我们：即便是最尊贵的星曜，位置不当也难以成贵。

- **叙事素材（narrative_snippets）**：

  - `[ns_zwds_j1_001]` `[trigger: 紫微守命]` `[factor_trigger: star_ziwei AND palace_life]` `[role: 主干]` 紫微为帝座，在诸宫能降福消灾，解诸星之恶虚。 → 《紫微斗数全书·诸星问答论》#紫微星
  - `[ns_zwds_j1_002]` `[trigger: 紫微有辅弼]` `[factor_trigger: star_ziwei AND (star_zuofu OR star_youbi)]` `[role: 主干依赖]` 有相为有用，无相为孤君。 → 《紫微斗数全书·诸星问答论》#紫微星
  - `[ns_zwds_j1_003]` `[trigger: 紫微无辅弼]` `[factor_trigger: star_ziwei AND NOT (star_zuofu OR star_youbi)]` `[role: 条件分支]` 若还无辅弼，诸恶共欺凌，帝为无道主。 → 《紫微斗数全书·诸星问答论》#紫微星
  - `[ns_zwds_j1_004]` `[trigger: 紫微遇禄存日月]` `[factor_trigger: star_ziwei AND star_lucun AND (star_taiyang OR star_taiyin)]` `[role: 增强条件]` 人之身命，若值禄存同宫，日月三合相照，贵不可言。 → 《紫微斗数全书·诸星问答论》#紫微星
  - `[ns_zwds_j1_005]` `[trigger: 紫微制杀]` `[factor_trigger: star_ziwei AND (star_huoxing OR star_lingxing OR star_qisha)]` `[role: 例外处理]` 能制火铃为善，能降七杀为权。 → 《紫微斗数全书·诸星问答论》#紫微星
  - `[ns_zwds_j1_006]` `[trigger: 紫微落四陷宫]` `[factor_trigger: star_ziwei AND (palace_jie OR palace_xiongdi OR palace_nupu OR palace_xiangmao)]` `[role: 条件分支]` 如落疾厄、兄弟、奴仆相貌四陷宫，主人劳碌，作事无成。 → 《紫微斗数全书·诸星问答论》#紫微星
  - `[ns_zwds_j1_007]` `[trigger: 女命紫微]` `[factor_trigger: gender_female AND star_ziwei]` `[role: 总结]` 女命逢之，作贵妇断。加杀冲破，亦作平常，不为下贱。 → 《紫微斗数全书·诸星问答论》#紫微星"""
    normalized_text_zh: str = """"""
    subject: str = "1 紫微星"
    factor_refs: list = ['star_ziwei', 'concept_dizuo', 'pattern_gujun', 'combo_santai', 'existing', 'palace_sixian']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_1_紫微星_001_L1",
    )
    version: str = "1.0.0"
