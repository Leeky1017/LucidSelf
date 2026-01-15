"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523773
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
    semantic_id="zpzq_v1.0.0_又有合而无伤于合者_合一留一_本身之合_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 又有合而无伤于合者合一留一本身之合(SemanticEntry):
    """
    - **原文（source_text）**：
  又有合而无伤于合者，何也？如甲生寅卯，月时两透辛官，以年丙合月辛，是为合一留一，官星反轻。甲逢月刃，庚辛并透，丙与辛合，是为合官留煞，而煞刃依然成格，...
    """
    
    original_text: str = """- **原文（source_text）**：
  又有合而无伤于合者，何也？如甲生寅卯，月时两透辛官，以年丙合月辛，是为合一留一，官星反轻。甲逢月刃，庚辛并透，丙与辛合，是为合官留煞，而煞刃依然成格，皆无伤于合也。又有合而不以合论者，何也？本身之合也。盖五阳逢财，五阴遇官，俱是作合，惟是本身十干合之，不为合去。假如乙用庚官，日干之乙，与庚作合，是我之官，是我合之，何为合去？若庚在年上，乙在月上，则月上之乙，先去合庚，而日干反不能合，是为合去也。又如女以官为夫，丁日逢壬，是我之夫，是我合之，正如夫妻相亲，其情愈密。惟壬在月上，而年丁合之，日干之丁，反不能合，是以己之夫星，被姊妹合去，夫星透而不透矣。

- 原注（原文注解）：
  　　本段说明两类“看似有合，却不坏格局甚至另有其义”的情形：
  - 合一留一：只合去其中一颗官星或煞星，另一颗仍在，格局不破；
  - 本身之合：日主亲自与财/官合者，不算“合去用神”，反而是情义更密之象。

- 分字分词释义：
  - 合一留一：多颗同类星中，只被合走一颗，另一颗留存发挥作用。
  - 合官留煞：丙合辛去官，留庚为煞，原煞刃格局仍然存在。
  - 本身之合：日干亲自与某干构成合，此合为“我所合之神”，不算“被合去”。
  - 五阳逢财，五阴遇官：阳干遇财多作合，阴干遇官多作合，皆属本身之合。
  - 夫星被姊妹合去：指女命之官星被别干（如姊妹之干）抢合，不再专属日主。

- **规范化释义（primary_lang_explained）**：
  有些合，看上去似乎会破坏原有格局，实际上影响有限，甚至丝毫不伤。比如甲日生于寅卯，月时上两透辛官，本来官星很重；若年干再来一丙，与其中一位辛相合成水，则变成“合一留一”：一颗辛被合走，另一颗辛仍留在天干，官星反而由双官变成单官，有时比原来更清。又如甲日逢月刃（如卯月），庚辛官煞并透，再有丙火出干与辛合去官，便形成“合官留煞”，原本的煞刃格局仍然成立。此类合，既没有破坏原格，反而帮忙清格。

 - 另有一类"合而不以合论"的情况：那就是"本身之合"。阳干遇财、阴干遇官，常常会和这颗财或官作合，这不叫"合去用神"，而是说这是"我自己的财、我自己的官"，合之则情更密。例如乙日用庚官，若日干之乙亲自与庚合，是"我来合我的官"，不能说官星被合去；真正的"官被合去"，是庚在年上、而月上另有一乙去合庚，使日主反而失去这个官。同理，丁日见壬为夫星，若丁壬直接相合，是妻夫相亲之象；若壬在月干而年干另有丁去合，则日主丁反而"被姊妹合走夫星"。

- **完整对等诠释（secondary_lang_full）**：  
  Some kinds of combination do little or no damage to the existing pattern, and may even make it cleaner. One is the situation the author calls "combine one, leave one": when several stars of the same type are present, combining away one of them still leaves another in place to carry the role. If a Jia Day Master born in Yin or Mao has two Xin Officers showing in month and hour, and a Bing Fire in the year stem combines with one of the Xins, the remaining Xin still functions as Officer; the pattern moves from double Officer to single Officer and can even become purer. Likewise, in a chart where both Geng and Xin are present as Killing and Officer and a Bing Fire combines with Xin, the Officer is removed but the Killing and Blade configuration remains intact. Here the combination does not break the pattern; it simply thins it out.

  A second case is what the text calls "self‑combination". Yang stems naturally tend to combine with their Wealth stars, and yin stems with their Officer stars. When the Day stem itself combines with Wealth or Officer, this is not "having the Useful God taken away" but rather "I am joining with what is mine"—the bond is closer, not weaker. For example, if an Yi Day Master uses Geng as Officer and the day stem Yi personally combines with Geng, this is Yi embracing its own Officer and must not be read as loss. True loss occurs when some other Yi in the chart, such as a year stem, combines with Geng first and the Day stem can no longer reach it. In a female chart, if Ding Day meets Ren as husband star and Ding‑Ren stand together in the day pillar, this looks like a close marital attachment; but if Ren sits in the month stem and a different Ding in the year stem combines with it, then the Day Ding has effectively had her husband star "taken away" by a sister. In practice we must therefore distinguish carefully between "I go to meet the star" and "another stem snatches the star before I can combine with it".

- 详细解说：
  - 合化分析必须细看“哪一颗被合”“是谁去合”，不能只凭“有合”二字就说格局破坏。
  - 合一留一：提醒我们多神并见时，合化只影响其中一部分，剩余部分仍可成格。
  - 本身之合：从日主立场看，“我去合”与“被别人抢去合”完全不同，前者为情合，后者为权失。

- 核心要点：
  - 多颗同类喜神时，适度合去一颗，反而有助于清格，而非必为坏事。
  - 本身之合不视为“合去用神”，而视为“我与用神关系更密”。
  - 真正需要警惕的是：别干抢合用神，使之不再专属于日主。

- 应用推演：
  1) 对多官、多煞、多印、多财之局，先数清同类星的数量与位置。
  2) 检查合化发生在谁与谁之间：是日主与用神之合，还是他干与用神之合？
  3) 对“合一留一”的局面，不急于判格局破坏，反看是否因此更清纯。
  4) 在六亲解读时，特别小心“夫星/妻星被合去”的情形。

- 反例与边界：
  - 见合即言“官星被合去”“财星被合去”，不区分是本身之合还是他干抢合。
  - 忽视多星局中“合一留一”的结构，一刀切地判“合则不成格”。

- 小例（示意）：
  - 甲日生卯月，月时两辛透官，年透丙合月辛，留时辛为官，格局反而更清；
  - 丁日见壬在日支，日干丁与壬紧贴，夫星与我同宫，合之为情密，不宜武断言“夫星被合去”。

- 校勘与字词辨析：
  - “夫星透而不透矣”一句，意在说明“表面上夫星仍在天干，实则情义已不属日主”，本精校版在白话中作了展开说明。

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_231]` `[trigger: 杂气概念]` `[factor_trigger: branch IN (chen, xu, chou, wei) AND zaqi=true AND neicang_duoshen_xu_zeyong]` `[role: 主干]` 辰戌丑未为杂气，内藏多神须择用。 → 《子平真诠·论杂气如何取用》#概念
  - `[ns_zpzy_232]` `[trigger: 库中取用]` `[factor_trigger: zaqi_tougan AND kuzhong_quyong]` `[role: 主干]` 杂气透干，库中取用。 → 《子平真诠·论杂气如何取用》#取用
  - `[ns_zpzy_233]` `[trigger: 透干为用]` `[factor_trigger: zaqi_tougan_zhe_xianyong AND butou_ze_kan_huihe]` `[role: 主干]` 杂气透干者先用，不透则看会合。 → 《子平真诠·论杂气如何取用》#透干
  - `[ns_zpzy_234]` `[trigger: 冲开库门]` `[factor_trigger: zaqi_feng_chong AND ku_kai AND caiguan_yinshi_ge_you_yong]` `[role: 主干]` 杂气逢冲则库开，财官印食各有用。 → 《子平真诠·论杂气如何取用》#冲开
  - `[ns_zpzy_235]` `[trigger: 空亡之说]` `[factor_trigger: kongwang_bubi_jinxin]` `[role: 主干]` 空亡不必尽信。 → 《子平真诠》#上卷
  - `[ns_zpzy_236]` `[trigger: 杂气月令]` `[factor_trigger: zaqi_yueling AND tougan_huizhi]` `[role: 主干]` 杂气月令，透干会支。 → 《子平真诠》#论杂气如何取用
  - `[ns_zpzy_237]` `[trigger: 病重药重]` `[factor_trigger: (bingzhong AND yaozhong) OR (bingqing AND yaoliang)]` `[role: 主干]` 病重药重，病轻药轻。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "又有合而无伤于合者，合一留一、本身之合"
    factor_refs: list = ['heyi_liuyi', 'heguan_liusha', 'benshen_zhihe', 'fuxing_hequ', 'engine_id', 'tongleixing_count', 'bazi_rule_engine', 'benshen_zhihe_flag', 'bazi_rule_engine', 'hequ_object_type', 'bazi_rule_engine', 'hehua_qingzhuo', 'bazi_rule_engine', 'spouse_hequ_flag', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_056', 'tongleixing_count', 'rel_zpzq_057', 'benshen_zhihe_flag', 'evi_zpzq_056', 'heyi_liuyi', 'rule_heyi_liuyi', 'evi_zpzq_057', 'benshen_zhihe', 'rule_benshen_he', 'concept_selective_pruning', 'concept_self_bonding']
    
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
        l1_anchor="zpzq_v1.0.0_又有合而无伤于合者_合一留一_本身之合_001_L1",
    )
    version: str = "1.0.0"
