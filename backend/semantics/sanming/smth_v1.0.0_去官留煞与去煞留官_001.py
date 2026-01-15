"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458387
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
    semantic_id="smth_v1.0.0_去官留煞与去煞留官_001",
    book_id="sanming",
    engine_id="bazi"
)
class 去官留煞与去煞留官(SemanticEntry):
    """
    - **原文（source_text）**：
  《喜忌篇》云：煞官混杂类，有去官留煞，亦有去煞留官。盖言柱中官星七煞交差：月上见官、时上见煞，或月上见煞、时上见官，或四柱叠见，有物去官留煞者，即以偏...
    """
    
    original_text: str = """- **原文（source_text）**：
  《喜忌篇》云：煞官混杂类，有去官留煞，亦有去煞留官。盖言柱中官星七煞交差：月上见官、时上见煞，或月上见煞、时上见官，或四柱叠见，有物去官留煞者，即以偏官论；有物去煞留官者，即以正官论。凡看去留，要详柱中官煞孰重孰轻：天干透者易去，月支所藏者难去；须伤官、食神去官煞之物众而有力，方才去得。
  
  五阳日食神，能去煞又能留官；五阳日伤官，但能去官，不能留煞，必须得羊刃合，方成去官留煞。假如甲日生人，甲以辛为官，庚为煞：若官重煞轻，得丙食一位，克去庚金，与辛相合，此谓去煞留官，有情而贵；若煞重官轻，得丁火伤官，克去辛金，再得乙木羊刃，与庚相合，此谓去官留煞，有情而贵。
  
  五阴日食神，能去煞却不能留官，日主自能留之；五阴日伤官，能去官又能留煞。假如乙日生人，以庚为官，辛为煞：若官重煞轻，得丁食一位，克去辛煞，则乙与庚合，此谓去煞留官，有情而贵；若煞重官轻，得丙火伤官，克去庚金，来合辛金，此谓去官留煞，有情而贵。《元理赋》云：去煞留官当论贵，去官留煞主威权。又曰：官星七煞交差，却有合煞为贵，此之谓也。有合煞者，有合去、合来之别：合来是去官留煞，合去是去煞留官。
  
  假令六甲生人，透辛正官，又透庚七煞，是官煞交差；柱中却有乙木合庚七煞，有丁火克辛官星，此是去官留煞。假令六己生人，透出甲正官，又透乙七煞，是官煞交差；柱中却有庚克甲正官，来合乙七煞，是去官留煞。上是羊刃合煞，此是伤官合煞。
  
  又如甲以辛酉为官，庚申为煞；若甲申日以申为煞，又有酉为官，缘申乃水长生之地，煞化印生助甲木，柱中虽有酉金，却有午丁字伤克，去官留煞，值此主生平心志巧妙，不受福德，不信任他人，常劳役自己。又如六庚生人，柱透丙煞，又透丁官，是官煞交差：若柱有壬克丙，又来合丁，是去煞留官。《赋》云：合官星不为贵，合七煞不为凶。盖言合官，是柱中闲神合去官星，所以不为贵；合煞，是柱中闲神与七煞相合，所以合官忘贵，合煞忘贱。若日主干支与官煞合，则为合官为贵，合煞为贱。
  
  经曰：官煞两停，喜者存之，憎者去之。盖言柱中正官、七煞两均相停：有物生扶会和者，其力专，宜存而留之；有物破损伤害者，其力散，宜弃而去之。官星有生扶，煞星有破害，则去煞留官；反是，则去官留煞。若两停俱无扶合而有破害，当斟酌柱中有力一字为用神：若是吉神，则以吉论。若两停俱有扶合而无破害，即是官煞混杂，反为贫贱。
  
  又曰：年月日时，或有四位官、四位煞，当以明者用之、藏者舍之：明见官则存其官，明见煞则存其煞。宜仔细分别：若两停无轻重，察其生助向时者用之，背时无助者弃之；去留不清，乃为混杂。又如甲生七月上旬，为煞得令，纵有丙火，亦不能去。
  
  又曰：去留二格，最宜身旺。若身果旺，虽无物去煞，亦能化煞为官。如甲见庚为煞，甲坐寅禄，旺，甲木自抱火气制煞，不须再见丙丁；如甲生秋令，却要丙丁制之，柱原无制，运到制地方发。又曰：地支天干合多，亦云贪合忘官。盖言日主天元、地支人元，与当生岁月时中干支明暗重重相合，有情贪恋：合神虽有官星，则财来盗气、官来克身，反为不利，官将不成，财将不遂，故曰贪合忘官。
  
  大抵凶神有物合去，则反凶为吉；吉神有物合去，则反吉为凶。吉凶神煞，看局中喜忌何神，不可执一论。《奥旨赋》云：阳日食神暗合官星，阴日食神窃侵印绶。观此则知，四柱无官印则喜食神，有官印则忌食神。又曰：贪合忘煞、忘官。如六癸生人，干头透出己字为煞，再透甲字，是己家合神，合去己字，不为煞矣，此谓贪合忘煞。如庚申、甲申、甲子、乙亥，年上庚字伤甲，得亥上乙字合庚去煞，奈月令又有申，不清二申，煞重不能尽合，所以只为吏命。又如六壬生人，干头透己字为官，再见申透，是己家合神，合去己字，不为官星，此谓贪合忘官。如辛丑、丙申、甲戌、己巳，甲日透出辛字，正是官星，奈因丙火合去，所以发贵不清。
  
  诀云：壬水相逢阳土时，心怀忿怒起争非；忽然癸水来相助，合住凶顽不见威，此贪合忘煞例。又云：壬逢己土欲为官，蓦被青阳起讼端，引诱合将真贵去，致令受挫万千般，此贪合忘官例。

- 分字分词释义：
  - **去官留煞 / 去煞留官**：在官煞并见时，通过食神、伤官、合神等作用，选择保留其中一方作为用神结构。
  - **官煞交差**：正官与七煞在不同柱上交错透出或藏于支中。
  - **食神去煞、伤官去官**：阳日多以食神去煞、伤官去官为主；阴日则相反，要注意区分。
  - **合煞为贵**：通过合神与七煞相合而不以凶论，反以其为威权之源。
  - **贪合忘官 / 贪合忘煞**：合神过多，官或煞被闲神合去，导致官煞失用，转为不利。
  - **官煞两停**：官星与七煞力量相当，需要视生扶、破害与合化来决定去留。

- **规范化释义（primary_lang_explained）**：
  本节是在官煞混杂的基础上，专门讨论如何"去留"的问题。官与煞并见时，不一定两者都用；可以通过食神、伤官、合神等，使其中一者被克去或被合去：若以正官为用，则去煞留官；若以七煞为用，则去官留煞。关键在于：哪一方更有力、与日主更有情，以及局中财、印、刃等如何配合。
  
  原文详细区分了阳日、阴日以及食神、伤官的不同作用方式，并给出大量例命，说明合煞、合官的不同结果。有时合去官星，反使贵气不显；有时合去煞星，反使威权不成。又提出"官煞两停"的情形：当官与煞势均力敌时，要看局中哪一类星辰在生扶、会合或破害，再决定去留，否则就成了真正意义上的"官煞混杂"，反主贫贱。

- **完整对等诠释（secondary_lang_full）**：
  The Joys-and-Taboos text notes that in mixed official–Killing structures there are cases where one 'removes official and keeps Killing' and others where one 'removes Killing and keeps official'. This refers to charts where official and Seven Killing criss‑cross: the month shows official while the hour shows Killing, or the month shows Killing and the hour shows official, or both appear repeatedly through the four pillars. When some agent—such as Hurting Officer or Eating God—removes the official but leaves the Killing in place, the pattern is judged as taking partial official as its use. When the same kinds of stars remove Killing and leave official, the pattern is judged as taking Proper Official instead.
  To decide what should be removed and what should be kept, one must weigh which of official or Killing is heavier or lighter in the chart: stars exposed on the stems are easier to remove, while those hidden in the branches of the month are much harder to dislodge. Only when the stars that remove official or Killing are numerous and strong can they truly take something away. In practice this becomes a technical art of 'removing and keeping' within mixed structures, where the goal is not to destroy both forces, but to leave in place whichever side can form an affectionate, supportive relationship with the day-master and the rest of the chart.


- 核心要点：
  - 官煞并见时，**必须处理去留**，不能两者皆用而致混乱。
  - 阳日、阴日在食神、伤官去留官煞上有不同规则，需要分开看。
  - 合神既可以合去凶煞而成吉，也可能合去吉神而成凶，关键是看"喜忌何神"。

- 详细解说：
  与前文"官煞混杂"强调不要一见官煞并见即判为贱不同，本节更进一步，从技术上说明如何处理官煞并见的结构。食神、伤官作为能量外泄之神，一方面可以克去官煞，另一方面又可能损伤用神；因此判断时要看它们究竟是在"去凶"还是在"去吉"。
  
  文字中多次出现"有情"一词，说明去留不在形式，而在关系：去煞留官也好，去官留煞也好，只要与日主、财印之间形成有情之合、有力之生扶，便可成贵；若只是孤立克合，不与全局气势相应，则难以成格。"贪合忘官 / 忘煞"的两种情况，则提醒我们：合多未必是好事，合神可能把真正有用的官或煞合去，反倒使局失其纲领。
  
  最后两条口诀借壬水与阳土、己土之例，说明在实际推命时，需要结合日主强弱、岁运流转来看"合"的方向与结果，切忌只见"合"便喜或只见"煞"便惧。

- 校勘与字词辨析：
  - 文中"官煞两停，喜者存之，憎者去之"一句，是后世讨论官煞去留的纲领句之一，本稿依原文保留。
  - "贪合忘官 / 忘煞"等语，在多部命书中有略异写，本稿取与原书最接近者，并在白话中解释其意，不作版本学展开。
  - **English**：
    - Meaning explained in vernacular; no textual criticism expansion.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_076]` `[trigger: 去留原则]` `[factor_trigger: quguan_liusha_pattern OR qusha_liuguan_pattern]` `[role: 主干]` 有物去官留煞者，即以偏官论；有物去煞留官者，即以正官论。 → 《三命通会》卷五#去官留煞
  - `[ns_smth_05_077]` `[trigger: 贵与威权]` `[factor_trigger: qu_liu_you_qing]` `[role: 主干依赖]` 去煞留官当论贵，去官留煞主威权。 → 《三命通会》卷五#去官留煞
  - `[ns_smth_05_078]` `[trigger: 官煞两停]` `[factor_trigger: guansha_liangting AND xi_zhe_cun_zhi]` `[role: 条件分支]` 官煞两停，喜者存之，憎者去之。 → 《三命通会》卷五#去官留煞
  - `[ns_smth_05_079]` `[trigger: 合神忘官煞]` `[factor_trigger: he_guan_bu_gui AND he_sha_bu_xiong]` `[role: 总结]` 合官星不为贵，合七煞不为凶。合官忘贵，合煞忘贱。 → 《三命通会》卷五#去官留煞"""
    normalized_text_zh: str = """"""
    subject: str = "去官留煞与去煞留官"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'guansha_quliu_jichu_config', 'bazi_semantic', 'shishang_heshen_config', 'bazi_semantic', 'quliu_youqing_score', 'bazi_semantic', 'yinyang_shishang_diff', 'bazi_semantic', 'guansha_liangting_quliu', 'bazi_semantic', 'tanhe_wangguansha_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_058', 'guansha_quliu_jichu_config', 'rel_smth_05_059', 'yinyang_shishang_diff', 'rel_smth_05_060', 'tanhe_wangguansha_risk', 'evi_smth_05_058', 'guansha_quliu_jichu_config', 'rule_quliu', 'evi_smth_05_059', 'yinyang_shishang_diff', 'rule_yangshi', 'evi_smth_05_060', 'guansha_liangting_quliu', 'rule_liangting', 'map_smth_05_039', 'map_smth_05_040']
    
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
        l1_anchor="smth_v1.0.0_去官留煞与去煞留官_001_L1",
    )
    version: str = "1.0.0"
