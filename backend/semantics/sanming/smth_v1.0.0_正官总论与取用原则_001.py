"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458172
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
    semantic_id="smth_v1.0.0_正官总论与取用原则_001",
    book_id="sanming",
    engine_id="bazi"
)
class 正官总论与取用原则(SemanticEntry):
    """
    - **原文（source_text）**：
  正官者，乃甲见辛、乙见庚之例。阴阳配合，相制有用，成其道也。故正官为六格之首，止许一位，多则不宜。正官先看月令，然后方看其余。以五行之气，惟月令当时为...
    """
    
    original_text: str = """- **原文（source_text）**：
  正官者，乃甲见辛、乙见庚之例。阴阳配合，相制有用，成其道也。故正官为六格之首，止许一位，多则不宜。正官先看月令，然后方看其余。以五行之气，惟月令当时为最，况四柱各管年限，年管十五，失之太早，时管五十后，失之太迟，故只此月令为正，余格例此。
  
  甲日生酉月，乙生申巳，丙生子，丁生亥，戊生卯，己生寅，庚生午，辛生寅巳，壬生午未丑，癸生辰巳戌月，皆为正气。官星更天干透出，如甲见辛酉、乙见庚申之例，谓之支藏干透，余位不宜再见，又须日主健旺，得财印两扶，柱中不见伤煞，行运引至官乡，大富大贵命也。
  
  大忌刑冲破害、伤官七煞、贪合忘官、劫财分福，为破格。如甲生酉月，见卯为冲、酉为刑、午为破、戌为害、丙为合、乙为劫、丁为伤克、庚为混杂，须是官星纯一，五行和粹，方以正官论。若见前忌柱中，虽有物去之，亦不纯粹。
  
  若官星结局，又有财资扶，非行身旺地不发。官止一二，无财有印，身弱无妨。若四柱皆归背禄，宜推岁运向背财官旺地。何如？若财官满目，日主衰弱，不能负荷，徒劳无用，运至财煞旺乡，多染痨瘵，但有七煞行运复遇，便是徒流之命。
  
  又曰：甲生酉月，辛金正禄，若见丁伤，支中无局，时引归衰败死绝之地，或有制合去之衰绝之火，岂能伤其旺禄。若时引官星临衰败死绝之位，反引丁火归生旺之乡或临煞地，降官失职，祸生无疑。时为归息之地，吉凶全在时消息。日主用神太盛，宜时以节制之；日主用神渐衰，宜时以补助之。柱中虽有凶神，时能节制，亦不能为祸，此看命之要法也。
  
  又曰：甲生丑月，内有辛金，又值酉时，己是重犯，若天干复透辛多，更行西方，力不胜任，变官为鬼，旺处必倾，多致灾夭，须有合制方吉。若自身乘旺，如甲寅、乙卯等日，更有印生助，官星虽多，亦不为害。甲生戌月，虽坐火库，若不成局，无党，不能为害。
  
  又曰：取官星，不必专泥月令支辰，或月干，或年、日、时支干，只一处有，不曾损伤，皆可取用。故经云："明干有气明干取，明干无气暗中取"。若明干无气，引归地支，或有助托，运行得地，亦不减月内官星之福。
  
  又曰：凡论官星，略见一位食神坐实，便能损局，惟月令隐禄，见食，却为三奇之贵。大要看官、食虚实何如：若官星坐实，合神略虚，随官助贵；合神坐实，官星渐弱，官随合神，谓之贪合忘官。
  
  又曰：正官格，要行印乡，即是逢官看印。柱中原有印随官之轻重、日干之强弱，以观所宜之运：身弱印轻，要补其印；身旺官轻，要补其官。行伤官运，即是背禄；行身旺运，即是逐马。

- **完整对等诠释（secondary_lang_full）**：
  Proper Official refers to an opposite-polarity star that restrains the day-stem in a measured, constructive way—for example Jia seeing Xin or Yi seeing Geng. Because this kind of restraint is orderly and "affectionate", Proper Official is placed first among the six classical patterns and is allowed only one clear instance; once the official stars multiply they tend to turn into mixed Killing. In judging the pattern one first looks at the month branch, since the qi that is in seasonal command there is the truest "proper qi" of the chart. Ideally the official star is rooted in the month branch and also revealed on the stem, the day-master is strong enough to carry it, wealth and Seal support both official and body, and there is no sign of injury or Killing. When such a structure is then led by fortune cycles into official territories, it usually produces great wealth and high rank.
  By contrast, the text lists several ways in which Proper Official is broken: the official root being damaged by punishments, clashes, breaks and harms; the official being attacked by Hurting Officer and Seven Killing; the official being dragged away by greedy combinations and "forgetting the official"; or wealth-robber stars dispersing what the official could actually use. When the body is weak but the chart is full of wealth and officials, the person cannot truly shoulder their duties and is prone to illness and loss, especially if later fortune strengthens wealth and Killing. A key remedy principle is "when you meet official, look to Seal": Proper Official patterns need Seal stars to nourish the day-master and moderate the restraint from official, so that responsibility can be taken up without being crushed. Thus the real quality of Proper Official lies not only in seeing an official star, but in how pure it is, how the body and official are balanced, and how the later fortune cycles touch the axes of official, Seal and body.

- 分字分词释义：
  - **正官**：异性相克而有情者，如甲见辛、乙见庚，阴阳配合，相制有用，故为六格之首。
  - **月令为正气**：以月令所藏之官星为当令之正气，优先于年、日、时，因其五行之气最旺，主一生中壮年之运程。
  - **支藏干透**：官星先藏于月支，再于天干透出，如甲见辛酉、乙见庚申，是为根气在支、形象在干，力量最纯。
  - **官星纯一**：官星只许一位，不宜多见；多则混杂为煞，难以成其清贵之象。
  - **刑冲破害**：卯冲酉为冲，酉刑酉为刑，午破酉为破，戌害酉为害，皆损伤官星根气，为破格之要因。
  - **贪合忘官**：合神坐实、官星渐弱之象，如丙火合辛金，官随合神而失本职，名为贪合忘官。
  - **背禄**：日主无根或失令，为禄气所背，须借行运向财官旺地以补其不足。
  - **逐马**：行身旺运、禄马奔走之象，相对于背禄，多主奔波求名。

- **规范化释义（primary_lang_explained）**：
  本段总论正官格的立意与取用原则。正官是指阴阳相配的官星，如甲木以辛金为官、乙木以庚金为官，因"阴阳配合，相制有用"，故列为六格之首。但正官格极重清纯：一要月令为正气官星，当令有力；二要官星支藏干透，既有根又显露；三要官星止许一位，不可多见；四要日主健旺，有财印扶助；五要柱中无刑冲破害与伤官七煞混杂。如能具备上述条件，再得行运引至官乡，多主大富大贵。
  
  若官星虽见，却被刑冲破害、伤官七煞、贪合忘官、劫财分福等诸多因素损伤，则正官之清气不存，纵有其他五行来制合，亦难言纯粹。尤其是日主衰弱而财官满目者，往往"不能负荷"，反因官多、财盛而生病受累，运行财煞旺乡，更易染疾破败，甚至流徙为徒。故作者又以甲生酉月为例，说明若日时再犯辛金过多而无制，则"变官为鬼"；但若日主乘旺，有印生扶，则官多亦可不害。由此可见，正官之吉凶，全在身官强弱、制化有无之间。

- 核心要点：
  - 正官格以**月令当令官星**为轴心，支藏干透、官星唯一、日主健旺是成格关键。
  - 破格主要来自四类：刑冲破害官星根气，伤官七煞克损官星，贪合忘官使官随合神，劫财分福削弱官星实用价值。
  - 日主与官星的力量配置至关重要：身弱官旺，多为不能胜任之象；身旺官轻，则宜行官地填补，使官星可用。
  - 取官不必拘泥于月令支辰，只要年、月、日、时某处官星有根有气且不被损伤，皆可以用；只是月令之官最为纯正。

- 详细解说：
  与前一节印食官财四纲的总论相对应，本节将重心落在其中"官"的一端。作者首先确立正官的理想形态：阴阳相配、清和有情，因此特别强调"止许一位、多则不宜"。这与后文偏官、七煞格的多煞论法形成鲜明对比，也说明正官格代表的是中和之道，而非刚猛之势。其次，作者以月令为纲，指出四柱虽各主一段年纪，但决定格局性质者，仍在于壮年之月令；年柱太早，时柱太迟，日柱偏于主体，不及月令之统摄力强。
  
  在用神层面，本段着重提出"逢官看印"的原则：正官格须有印绶以生扶日主，一方面使日主能胜任官星所代表的责任，一方面也用印来调和官日之间的克战，使克制不至于过度。若身弱而官重，就要借行运补印；若身旺而官轻，则要借行运补官。反之，行伤官运则为背禄，行身旺运则为逐马，皆是对禄命与行运组合的形象比喻。
  
  本节后半部分引用《三命铃》等书，对金木水火土五行为官时的性格与官职类型做了补充说明，如金官多掌刑狱钱谷，木官和厚清慎，火官炎烈不常，水官谦和渐进，土官稳重法明等，这些描述为后续细化格局提供了性格与职业方向的参考维度。

- 校勘与字词辨析：
  - **"六格之首"**：传统子平六格为正官、七煞、正印、偏印、正财、偏财，正官居首，体现其在古人命理体系中的核心地位。
  - **"明干有气明干取，明干无气暗中取"**："明干"指天干上显露之官星，"暗中"指地支所藏之官星；即若天干官星有根有气，则以之为主，反之则从支中暗藏官星取用。
  - **"贪合忘官"**：古籍中常以此形容官星被合神牵引而失去原有职责，多主因感情、利益等牵扯而误事，需结合实际命局谨慎判断。
  - **"背禄、逐马"**：皆为命书术语，前者指身弱失禄，后者指身旺奔走，二者在行运上有不同的倾向和表现，应结合日主强弱与行运实际分析。
  - **English**：
    - Combined with day-master strength and actual fortune-cycle analysis.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_005]` `[trigger: 正官取用]` `[factor_trigger: zhengguan_pattern AND month_pillar_priority]` `[role: 主干]` 正官格以月令当令官星为轴心，支藏干透、官星唯一、日主健旺是成格关键。 → 《三命通会》卷五#正官总论
  - `[ns_smth_05_006]` `[trigger: 破格条件]` `[factor_trigger: zhengguan_broken_conditions]` `[role: 主干依赖]` 破格主要来自四类：刑冲破害官星根气，伤官七煞克损官星，贪合忘官使官随合神，劫财分福削弱官星实用价值。 → 《三命通会》卷五#正官总论
  - `[ns_smth_05_007]` `[trigger: 逢官看印]` `[factor_trigger: zhengguan_pattern AND yin_support]` `[role: 主干依赖]` 逢官看印：正官格须有印绶以生扶日主，使日主能胜任官星所代表的责任。 → 《三命通会》卷五#正官总论
  - `[ns_smth_05_008]` `[trigger: 身官配置]` `[factor_trigger: day_master_strength AND official_strength]` `[role: 总结]` 身弱官旺，多为不能胜任之象；身旺官轻，则宜行官地填补，使官星可用。 → 《三命通会》卷五#正官总论"""
    normalized_text_zh: str = """"""
    subject: str = "正官总论与取用原则"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'zhengguan_ge_presence', 'bazi_semantic', 'zhicang_gantou_structure', 'bazi_semantic', 'guanxing_purity_score', 'bazi_semantic', 'shen_guan_balance_axis', 'bazi_semantic', 'cai_yin_support_score', 'bazi_semantic', 'xingchong_pohai_risk', 'bazi_semantic', 'shangguan_qisha_mix', 'bazi_semantic', 'tanhe_wangguan_condition', 'bazi_semantic', 'source_ref', 'rel_smth_05_004', 'zhengguan_ge_presence', 'rel_smth_05_005', 'shen_guan_balance_axis', 'rel_smth_05_006', 'xingchong_pohai_risk', 'evi_smth_05_004', 'guanxing_purity_score', 'rule_guan_pure', 'evi_smth_05_005', 'cai_yin_support_score', 'rule_caiyin_fu', 'evi_smth_05_006', 'xingchong_pohai_risk', 'rule_no_shang', 'map_smth_05_003', 'map_smth_05_004']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_正官总论与取用原则_001_L1",
    )
    version: str = "1.0.0"
