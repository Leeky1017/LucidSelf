"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.465682
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
    semantic_id="zpzq_v1.0.0_妻宫与妻星的基本判准_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 妻宫与妻星的基本判准(SemanticEntry):
    """
    - **原文（source_text）**：
  二十四、论妻子。
  大凡命中吉凶，于人愈近，其验益灵。富贵贫贱，本身之事，无论矣，至于六亲，妻以配身，子为后嗣，亦是切身之事。故看命者，妻财子提纲得...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十四、论妻子。
  大凡命中吉凶，于人愈近，其验益灵。富贵贫贱，本身之事，无论矣，至于六亲，妻以配身，子为后嗣，亦是切身之事。故看命者，妻财子提纲得力，或年干有用，皆主父母身所自出，亦自有验。所以提纲得力，或年干有用，皆主父母双全得力。至于祖宗兄弟，不甚验矣。

  以妻论之，坐下财官，妻当贤贵；然亦有坐财官而妻不利，逢伤刃而妻反吉者，何也？此盖月令用神，配成喜忌。如妻宫坐财，吉也，而印格逢之，反为不美。妻坐官，吉也，而伤官逢之，岂能顺意？妻坐伤官，凶也，而财格逢之，可以生煞；煞格逢之，可以制煞，反主妻能内助。妻坐阳刃，凶也，而或财官煞伤等格，四柱已成格局，而日主无气，全凭日刃帮身，则妻必能相关，其理不可执一。

  既看妻宫，又看妻星。妻星者，干头之财也。妻透而成局，若官格透财、印多逢财、食伤透财为用之类，即坐下无用，亦主内助。妻透而破格，若印轻财露、食神伤官、透煞逢财之类，即坐下有用，亦防刑克。又有妻透成格，或妻宫有用，而坐下刑冲，未免得美妻而难偕老。又若妻星两透，偏正杂出，何一夫而多妻？亦防刑克之道也。

  至于子息，其看宫分与星所透喜忌，理与论妻略同。但看子息，长生沐浴之歌，亦当熟读，如“长生四子中旬半，沐浴一双保吉祥，冠带临官三子位，旺中五子自成行，衰中二子病中一，死中至老没儿郎，除非养取他之子，入墓之时命夭亡，受气为绝一个子，胎中头产养姑娘，养中三子只留一，男子宫中子细详”是也。

  然长生论法，用阳而不用阴。如甲乙日，只用庚金长生，巳酉丑顺数之局，而不用辛金逆数之子申辰。虽书有官为女、煞为男之说，然终不可以甲用庚男而用阳局，乙用辛男而阴局。盖木为日主，不问甲乙，总以庚为男辛为女，其理为然，拘于官煞，其能验乎？

  所以八字到手，要看子息，先看时支。如甲乙生日，其时果系庚金何宫？或生旺，或死绝，其多寡已有定数，然后以时干子星配之。如财格而时干透食，官格而时干透财之类，皆谓时干有用，即使时逢死绝，亦主子贵，但不甚繁耳。若又逢生旺，则麟儿绕膝，岂可量乎？若时干不好，子透破局，即逢生旺，难为子息。若又死绝，无所望矣。此论妻子之大略也。

- 原注（原文注解）：
  　　本章以“妻子”为核心，说明：
  - 命中吉凶，越接近“自身与最亲的六亲”，其应验往往越明显；
  - 富贵贫贱本身之事不赘述，此处重在妻与子这两类最关键的六亲；
  - 论妻须兼看“妻宫”（日支）与“妻星”（干头之财）；
  - 论子须看时柱（子女宫）、子星与长生沐浴歌.

  首段指出：
  - 妻以配身，子为后嗣，皆为切身之事；
  - 若妻财子提纲得力，或年干有用，则多主父母身所自出而有验；
  - 祖宗兄弟相对较远，往往不如妻子之应验灵动.

  中段“以妻论之”部分，是本章重点：
  - 妻宫坐财官，一般说妻贤而贵；
  - 然而作者强调，“妻宫坐财官”并非一律吉祥，还要看月令用神与全局喜忌：
    - 妻宫坐财本为吉，若印格却逢之，财来坏印，则反为不美；
    - 妻宫坐官本为吉，若伤官临之，官被伤克，岂能顺意？
    - 妻宫坐伤官本为凶，若财格逢之可生煞、煞格逢之可制煞，反而能成内助；
    - 妻宫坐阳刃本为凶，若局中财官煞伤等格已成而日主无气，反凭日刃帮身，则妻反而成为关键帮手.

  随后作者提出“既看妻宫，又看妻星”：
  - 妻星是干头之财：
    - 妻星透而成局，如官格透财、印多逢财、食伤透财为用等，即使妻宫不显，也主妻能内助；
    - 妻星透而破格，如印轻财露、食神伤官、透煞逢财等，则须防财来坏印、坏官，妻反成破局之力；
  - 妻星成格而妻宫受刑冲，多是“美妻而难偕老”；妻星两透、偏正杂出，则多夫多妻或感情复杂，亦防刑克.

  下半部分转入子息：
  - 子息看法大体与妻宫类似，以时支（子女宫）与子星配合，并结合长生沐浴歌；
  - 强调长生论法“用阳不用阴”，如甲乙日皆以庚之长生为男，不以辛之长生为男；
  - 反驳“官为女、煞为男”的死板说法，指出木日主本当同以庚为男、辛为女，不宜拘泥官煞名目.
  - 最后给出“看子息”的操作步骤：
    - 先看时支落何宫（生旺死绝），估计子多寡大致范围；
    - 再看时干子星有无用：财格时透食、官格时透财等，即便死绝亦主子贵；
    - 若时干无用又死绝，则子息难望.

- 分字分词释义：
  - 妻宫：日支所在之地支，多视为配偶宫位.
  - 妻星：天干之财星，正财为妻、偏财为妾.
  - 提纲：月令为提纲，也泛指全局纲领之处.
  - 坐下财官：日支为财或官星，象征妻宫坐财官.
  - 伤刃：伤官与阳刃，总称破格之神.
  - 妻能内助：妻对事业与人生有实质帮扶作用.
  - 长生沐浴之歌：古人总结的以十二长生看子息多寡的歌诀.
  - 生旺死绝：指长生、帝旺、死、绝等旺衰阶段.
  - 子星：时干所代表之子女用神，常以财、食、官等为子星.
  - 麟儿绕膝：子嗣繁盛之象.

- **规范化释义（primary_lang_explained）**：
  本章可以分为三块：
  1) 总论“妻子”为最切身之六亲；
  2) 详细讨论妻宫与妻星的组合；
  3) 概述子息判断的思路.

  开头强调：富贵贫贱是本身之事，此不多说；而妻子则是最贴近自身的六亲，其吉凶最易在命中体现.提纲有力、年干有用时，多主父母身所自出、父母得力.

  论妻宫时，作者提醒我们：
  - “妻坐财官必贤贵”的说法太粗，只能当作一个起点；
  - 真正判断，要把妻宫所坐之神放入全局用神喜忌中理解：
    - 若妻宫坐的是局中喜用之神，自然有利；
    - 若妻宫坐的是局中忌神，或虽为喜神却产生“贪财坏印”等副作用，则未必美.

  论妻星时，强调：
  - 妻星透而成局，甚至可以弥补妻宫之不足；
  - 妻星透而破格，则要谨防“因妻致祸”或感情与财务的负面影响；
  - 妻星两透偏正杂出，则感情结构往往复杂，或多重关系并存，亦需防刑克与分离.

  对子息部分，作者主要把长生沐浴歌作为辅助：
  - 用阳不用阴，避免死板地“官为女煞为男”；
  - 先看时支强弱与旺衰，再看时干子星是否有用；
 - **完整对等诠释（secondary_lang_full）**：  
  The spouse is read through both the spouse palace (Day Branch) and the spouse star (Wealth on the stems). A palace that appears auspicious by sitting on Wealth or Officer must still be judged within the whole pattern: if Wealth damages Resource or breaks the structure, marriage may bring strain rather than support. Children are read through the children palace at the Hour Branch together with the life‑cycle song and the usefulness of the child star on the Hour stem; because spouse and children are closest to the self, their indications tend to verify more vividly than those of more distant relatives.

  - 子星有用则“虽死绝亦有子贵”，子星无用则“虽生旺亦难以子繁”.

- 详细解说：
  - 本章与前一章“宫分用神配六亲”一脉相承：
    - 六亲之吉凶，不在星名好坏，而在于用神得力与否；
    - 妻、子尤为关键，需结合宫位、用神与全局喜忌综合看待.
  - 对现代应用而言：
    - 有助于在解读婚姻与子女问题时，避免简单“妻坐财则吉、子星透则多子”之类粗断；
    - 提醒我们关注“配偶与子女在命主生命中的实际作用”——是内助、是压力，还是因格局安排不同而有轻重之别.

- 核心要点：
  - 妻论两件事：
    1) 妻宫坐何神？（在全局是喜是忌？）
    2) 妻星透何神？（成格还是破格？）
  - 子论三步：
    1) 时支长生死旺判断子多寡的大致范围；
    2) 时干子星是否有用（财、官、食等）；
    3) 行运是否扶助或损坏子星.
  - 一切仍然围绕“用神得力”这一总纲，而非单凭一两句诀歌.

- 应用推演：
  1) 判定妻宫与妻星：分别标出日支与干头之财星，并放入格局体系中考察其喜忌；
  2) 检查是否存在“妻宫喜神而妻星破格”或反之的情况，判断婚姻中“人好局难”或“局好人难”的不同模式；
  3) 对子息部分，先用长生死旺歌给出子息大致多寡，再以子星有无与运势配合校正；
  4) 在咨询中，强调婚姻与子女并非“必然福/祸”，而是与命主格局匹配的不同角色，需要现实中的沟通与选择配合.

- 反例与边界：
  - 一见妻宫坐财便断“娶贤妻”，不看财在全局中是喜是忌；
  - 把子息全部交给长生歌诀，而不看时干子星与全局；
  - 忽略社会文化与个人选择，把所有婚育结果都简单归因于命局.

- 小例（示意）：
  - 一命妻宫坐财、妻星透财而为喜神，多主妻能内助，婚姻中财务与情感皆有良好互动；
  - 另一命妻宫坐官看似吉，但在伤官格中，官逢伤反成压抑，实际婚姻中常有“对方条件好但难以顺意”的体验；
  - 某命时支长生、子星有用，晚运再得子星之运，多主子息既多且成材；
  - 另有命局时支死绝、子星受克，虽早年有子，终因健康或关系问题缘薄，也属本章所言“时干不好，子透破局”的范畴.

- 校勘与字词辨析：
  - 长生沐浴歌各本略有差异，本精校仍从底本，仅在注中说明其大意，不做字面修正；
  - “官为女煞为男”“庚为男辛为女”等说法，在古籍中颇多争议，本精校倾向作者立场：以日主五行为本，不拘官煞名号.


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_406]` `[trigger: 墓库真义]` `[factor_trigger: branch IN (chen, xu, chou, wei) AND simu AND bubi_jie_xi_xingchong]` `[role: 主干]` 辰戌丑未四墓，不必皆喜刑冲。 → 《子平真诠·论墓库刑冲之说》#墓库
  - `[ns_zpzy_407]` `[trigger: 透干为先]` `[factor_trigger: zaqi_tougan_huizhi AND sheng_yu_xingchong_luandong]` `[role: 主干]` 杂气透干会支，胜于刑冲乱动。 → 《子平真诠·论墓库刑冲之说》#透干
  - `[ns_zpzy_408]` `[trigger: 库冲有别]` `[factor_trigger: (caiguan_shutu AND chong_ze_ku_qi) OR (caiguan_shushui AND chong_ze_fan_lei)]` `[role: 主干]` 财官属土冲则库启，属水冲则反累。 → 《子平真诠·论墓库刑冲之说》#库冲
  - `[ns_zpzy_409]` `[trigger: 妻财子禄]` `[factor_trigger: cai_wei_qi AND guan_wei_zi AND ge_you_qufa]` `[role: 主干]` 财为妻，官为子，各有取法。 → 《子平真诠》#中卷
  - `[ns_zpzy_410]` `[trigger: 冲开库门]` `[factor_trigger: chong_kai_kumen AND caiguan_shi_xian]` `[role: 主干]` 冲开库门，财官始显。 → 《子平真诠》#中卷
  - `[ns_zpzy_411]` `[trigger: 库中藏干]` `[factor_trigger: kuzhong_canggan AND tougan_fang_yong]` `[role: 主干]` 库中藏干，透干方用。 → 《子平真诠》#中卷
  - `[ns_zpzy_412]` `[trigger: 刑冲破害]` `[factor_trigger: xingchong_pohai AND ge_you_qingzhong]` `[role: 主干]` 刑冲破害，各有轻重。 → 《子平真诠》#中卷
  - `[ns_zpzy_413]` `[trigger: 煞有制化]` `[factor_trigger: sha_you_zhi_hua AND hua_xiong_wei_ji]` `[role: 主干]` 煞有制化，化凶为吉。 → 《子平真诠》#中卷
  - `[ns_zpzy_414]` `[trigger: 伤有印制]` `[factor_trigger: shang_you_yin_zhi AND congming_fan_wei]` `[role: 主干]` 伤有印制，聪明反为。 → 《子平真诠》#中卷
  - `[ns_zpzy_415]` `[trigger: 近远不同]` `[factor_trigger: rigan_jin_zhe_li_zhong]` `[role: 主干]` 日干近者力重。 → 《子平真诠》#中卷
  - `[ns_zpzy_416]` `[trigger: 轻重权衡]` `[factor_trigger: qingzhong_quanheng AND ding_qi_gaodi]` `[role: 主干]` 轻重权衡，定其高低。 → 《子平真诠》#中卷
  - `[ns_zpzy_417]` `[trigger: 真假分辨]` `[factor_trigger: zhenshen_jiashen AND yongfa_butong]` `[role: 主干]` 真神假神，用法不同。 → 《子平真诠》#中卷
  - `[ns_zpzy_418]` `[trigger: 有病无药]` `[factor_trigger: youbing=true AND wuyao=true AND result=zhongshen_buli]` `[role: 主干]` 有病无药，终身不利。 → 《子平真诠》#中卷
  - `[ns_zpzy_419]` `[trigger: 生克有情]` `[factor_trigger: shengke_youqing AND fang_wei_zhenyong]` `[role: 主干]` 生克有情，方为真用。 → 《子平真诠》#中卷
  - `[ns_zpzy_420]` `[trigger: 成格判定]` `[factor_trigger: chengge]` `[role: 主干]` 成格为格局成功之判定，用神得力、结构完整。 → 《子平真诠》#论用神成败救应
  - `[ns_zpzy_421]` `[trigger: 败格判定]` `[factor_trigger: baige]` `[role: 主干]` 败格为格局失败之判定，用神受损、结构破坏。 → 《子平真诠》#论用神成败救应
  - `[ns_zpzy_422]` `[trigger: 三会局]` `[factor_trigger: sanhui]` `[role: 主干]` 三会为地支三会局，寅卯辰会木、巳午未会火、申酉戌会金、亥子丑会水。 → 《子平真诠》#论刑冲会合解法
  - `[ns_zpzy_423]` `[trigger: 因败得成]` `[factor_trigger: yinbai_decheng]` `[role: 主干]` 因败得成为原本破格之局因运程变化而转为成格。 → 《子平真诠》#论用神因成得败因败得成
  - `[ns_zpzy_424]` `[trigger: 因成得败]` `[factor_trigger: yincheng_debai]` `[role: 主干]` 因成得败为原本成格之局因运程变化而转为败格。 → 《子平真诠》#论用神因成得败因败得成"""
    normalized_text_zh: str = """"""
    subject: str = "妻宫与妻星的基本判准"
    factor_refs: list = []
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_妻宫与妻星的基本判准_001_L1",
    )
    version: str = "1.0.0"
