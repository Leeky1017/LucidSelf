"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458332
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
    semantic_id="smth_v1.0.0_偏官与七煞总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 偏官与七煞总论(SemanticEntry):
    """
    - **原文（source_text）**：
  偏官者，乃甲见庚、乙见辛之例。犹二男不同处，二女不同居，不成配偶，故谓之偏官。以其隔七位而相克战，故谓之七煞。譬如小人多凶暴，无忌惮，若无礼法控制之，...
    """
    
    original_text: str = """- **原文（source_text）**：
  偏官者，乃甲见庚、乙见辛之例。犹二男不同处，二女不同居，不成配偶，故谓之偏官。以其隔七位而相克战，故谓之七煞。譬如小人多凶暴，无忌惮，若无礼法控制之，不惩不戒，必伤其主，故有制谓之偏官，无制谓之七煞。
  
  如日主健旺，有印绶助化，即经云：逢煞看财。如身强煞弱，有财星则吉；身弱煞强，有财引鬼盗气，非贫则夭。有食神透制，即经云：一见制伏，却为贵本。有阳刃配合，即经云：煞无刃不显，逢煞看刃是也。以上诸制合生化，须要无太过不及，是借小人势力，卫护君子，以成威权，乃大权大贵之命。
  
  又性格聪明，忌日主衰弱，七煞重逢，三刑、六害、劫、亡相并，魁罡相冲，其凶不可具述。若七煞止一，而制伏有二三处，喜行煞旺地，倘运再遇制伏，则尽法无民，虽猛如虎狼，亦不能逞其技矣。是又不可专言制伏，要轻重得所。故经云：原有制伏，煞出为福；原无制伏，煞出为祸，此之谓也。
  
  假如甲见庚及申，乙见辛及酉，柱中煞旺有气，宜行东南方运，制庚辛无气方发。否则生寅卯月，或自坐长生、临官、帝旺，更多带比肩同类相扶，则能化鬼为官，化煞为权，行运引至印乡，必发富贵。倘岁运再遇煞地，祸不旋踵。
  
  假令甲寅生人为身旺，岁月见庚申为煞旺，柱中不透火制，地支子辰会印成局，则煞生印，印生身，作权贵看。年干露煞与月令、时支不同，太岁乃一生之主，最重。如甲见庚年，乙见辛年，又生申酉丑月，柱中金多，大运再行金乡，流年岁君并见，为凶尤甚；若生寅午戌及木旺之月，火制身强，金绝不能为害，则吉。
  
  经云：甲逢庚，败凋零，枝叶根枯；乙遇辛，伤消乏，本根苗损；炎炎丙火遇壬，而黑焰无光；灿灿丁红见癸，而辉光自灭。皆以七煞无制，反伤日主之象也。

- 分字分词释义：
  - **偏官**：同类中相隔七位而克我的五行，如甲见庚、乙见辛。因与日主同性，同属一气而又相克，故偏于猛烈。
  - **七煞**：偏官的极端形态。以十干顺序计算，相隔七位者为"七"；煞者，害也。无制约时，多主凶暴之力，故称七煞。
  - **二男不同处，二女不同居**：以男女同类不能为配偶比喻偏官非正配之官，与正官之"正配"相对。
  - **有制谓之偏官，无制谓之七煞**：有印、财、食、刃等星得当制化，偏官可为可用之权力；无制则为失控的戾气。
  - **逢煞看财**：身强煞弱时，财星可牵煞生官，为吉；身弱煞强时，财星反引煞来盗气，为祸。
  - **一见制伏，却为贵本**：指食神透出，制伏七煞，反成贵格。
  - **煞无刃不显，逢煞看刃**：七煞需配阳刃，方能显其权威；无刃则煞势难成格局。
  - **三刑、六害、劫、亡、魁罡**：皆为加重冲克、孤煞之神，若与七煞重叠，多主极端凶象。

- **规范化释义（primary_lang_explained）**：
  本节是对偏官、七煞格的总论。偏官是与日主同性、相隔七位而来克我的五行，如甲见庚、乙见辛。古人以"二男不同处，二女不同居，不成配偶"比喻，与正官之正配相对。因为偏官与日主同属一气，又兼克我之力，所以性质比正官更刚烈，故称七煞。
  
  然而，小人的力量并非一定为害。若日主健旺，又有印绶化煞、财星牵煞生官、食神制煞、阳刃配煞等多种制化配合，则七煞不但不为祸，反能成为卫护君子、成就威权的力量，即所谓"借小人势力卫护君子"。此时偏官格往往主大权在握、性格果决聪明。但若日主衰弱，七煞重逢，再叠加三刑六害、劫亡、魁罡等凶神，则多主祸患与夭折，不可轻言贵命。
  
  文中又以甲见庚、乙见辛在申酉等煞旺之地为例，指出若煞旺有气而行东南木火运，能制庚辛，则可化鬼为官、化煞为权；若反行西北金水运，则煞益旺，祸不旋踵。又举甲寅身旺，岁月见庚申而地支子辰会印之局，以说明"煞生印，印生身"亦可成权贵。最后引用"甲逢庚、乙遇辛、丙遇壬、丁见癸"等句，强调七煞无制时对日主的损害之大。

- **完整对等诠释（secondary_lang_full）**：
  A partial official is the star that stands seven steps away in the heavenly stem sequence and restrains the day-master while sharing the same polarity—for example Jia seeing Geng or Yi seeing Xin. Because it is of the same kind yet comes to attack, the classics compare it to 'two men who do not share a bed, two women who do not share a room': not a proper spouse, hence the name partial official. When such a star acts without restraint its harsher form is called Seven Killing. It is likened to a petty or lawless person—fierce, bold and unafraid—who, if not checked by ritual and law, inevitably harms their lord. When it is brought under proper control, we call it partial official and can use it; when it has no control, we call it Seven Killing and treat it as dangerous.
  If the day-master is strong and Seals help to transform Killing, the classics say 'when you meet Killing, look to wealth': when the body is strong and Killing is relatively weak, wealth can guide the harsh energy to produce official power and practical results; when the body is weak and Killing strong, wealth instead draws out ghosts to steal the qi, leading not to prosperity but to poverty or early death. Thus partial official and Seven Killing are simultaneously great omens of danger and great sources of power, and the whole judgement turns on the strength of the self and the presence or absence of well‑balanced controls from Seal, wealth, Eating God and Yang Blade.


- 核心要点：
  - 偏官 / 七煞本身既是**大凶之象**，亦是**大权之源**，关键在于日主强弱与制化是否得当。
  - 有印化煞、有财牵煞生官、有食神制煞、有阳刃配煞时，偏官可转为贵格，主权威与魄力。
  - 日主衰弱而煞重，再遇刑害、劫亡等凶星，多主祸患横生，不可勉强以贵格论之。
  - 论运势时，要分清原局是否本有制伏：原有制伏者，煞出反为福；原无制伏者，煞出则为祸。

- 详细解说：
  正官与偏官的差别，关键在于"阴阳配合"与"顺逆有情"。正官多为异性相克而有情，重在中和、礼法与名分；偏官则为同性相克，既同气相求，又互相争衡，更带危险性。古书以"小人"比附七煞，并非简单贬义，而是强调其力量不受礼法约束，若不加管理，反噬之力尤烈；若能善用，则可成护卫之兵、执行之手。
  
  本节多次强调"身强煞弱、有制方吉"与"身弱煞强、有财引鬼盗气"的对比，说明判断偏官格不能只看煞星多少，更要看日主根气、印绶强弱及制化结构。煞止一位而制化有二三处者，宜行煞旺运，以"用煞为权"；煞多制少者，则要行制伏运，先消其戾气。若一味以"制煞"为好，而不审轻重，反可能因制过其度，使格局反伤用神。
  
  同时，作者也提醒要结合年、月、日、时四柱及太岁来综合判断：年干露煞，与月令、时支之煞不同；太岁为一生之主，若再与原局七煞相应，则凶应尤重。由此可见，偏官 / 七煞格本身只是原理骨架，实际论命仍需与岁运仔细参照。

  - 校勘与字词辨析：
  -  - **"偏官者，乃甲见庚、乙见辛之例"**：此处只举甲、乙为例，余干可按十干相克体系类推其偏官与七煞。
  -  - **"二男不同处，二女不同居"**：是古人比喻之语，意在说明偏官非正配，今整理时保留原语，并在释义中作现代解读。
  -  - **"逢煞看财"、"煞无刃不显"**等句，在后世命书中多被反复引用，是理解偏官格制化原则的纲领性语句。
  - **English**：
    - Guiding statement for understanding Indirect-Official control principles.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_056]` `[trigger: 偏官七煞定义]` `[factor_trigger: pianguan_qisha_presence]` `[role: 主干]` 有制谓之偏官，无制谓之七煞。 → 《三命通会》卷五#偏官总论
  - `[ns_smth_05_057]` `[trigger: 借势卫护]` `[factor_trigger: zhihua_config AND shen_qiang]` `[role: 主干依赖]` 借小人势力，卫护君子，以成威权，乃大权大贵之命。 → 《三命通会》卷五#偏官总论
  - `[ns_smth_05_058]` `[trigger: 逢煞看刃]` `[factor_trigger: sha_wu_ren_bu_xian]` `[role: 条件分支]` 煞无刃不显，逢煞看刃是也。 → 《三命通会》卷五#偏官总论
  - `[ns_smth_05_059]` `[trigger: 原有制伏]` `[factor_trigger: yuan_you_zhi_fu AND sha_chu_wei_fu]` `[role: 总结]` 原有制伏，煞出为福；原无制伏，煞出为祸。 → 《三命通会》卷五#偏官总论"""
    normalized_text_zh: str = """"""
    subject: str = "偏官与七煞总论"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'pianguan_qisha_presence', 'bazi_semantic', 'zhihua_config', 'bazi_semantic', 'shen_sha_qiangruo_axis', 'bazi_semantic', 'quan_xiong_shuangmian_score', 'bazi_semantic', 'youzhi_wuzhi_condition', 'bazi_semantic', 'zhihua_qingzhong_balance', 'bazi_semantic', 'source_ref', 'rel_smth_05_043', 'pianguan_qisha_presence', 'rel_smth_05_044', 'quan_xiong_shuangmian_score', 'rel_smth_05_045', 'zhihua_qingzhong_balance', 'evi_smth_05_043', 'youzhi_wuzhi_condition', 'rule_pianguan', 'evi_smth_05_044', 'quan_xiong_shuangmian_score', 'rule_weiquan', 'evi_smth_05_045', 'zhihua_qingzhong_balance', 'rule_qingzhong', 'map_smth_05_029', 'map_smth_05_030']
    
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
        l1_anchor="smth_v1.0.0_偏官与七煞总论_001_L1",
    )
    version: str = "1.0.0"
