"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412348
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
    semantic_id="smth_v1.0.0_七日禄归时与青云得路_001",
    book_id="sanming",
    engine_id="bazi"
)
class 七日禄归时与青云得路(SemanticEntry):
    """
    - **原文（source_text）**：

  《喜忌篇》云：日禄归时没官星，号青云得路。此格有七日：甲寅、丁午、戊巳、己午、庚申、壬亥、癸子，日主之禄归于时位，喜日干坐旺、印绶生、月透财元、伤食...
    """
    
    original_text: str = """- **原文（source_text）**：

  《喜忌篇》云：日禄归时没官星，号青云得路。此格有七日：甲寅、丁午、戊巳、己午、庚申、壬亥、癸子，日主之禄归于时位，喜日干坐旺、印绶生、月透财元、伤食、天月二德，主大富贵。忌刑冲破害、空亡死绝、及劫财分禄、倒食作合、官煞克制，虽可取用，亦不纯粹。岁运同。

  如乙日见己卯时，是时上偏财；丙日见癸巳时，是官星显露；辛日见丁酉时，是时上偏官，不作归禄格看。四柱何如？若月有官星或天干透财官，只作财官论；若时支归禄，年月时支亦有禄，谓之聚福归禄，又谓五行归禄；若日禄归时，时禄归日，谓之互换禄；若年禄归时，时禄归年，如甲申见庚寅、乙酉见辛卯、壬午见丁亥、癸亥见壬子等类，俱主大贵享福。

  若重见禄位，如甲日寅时，又生正月，财官俱弱，只作建禄看；若月日天元同而止有时禄，谓之分禄，便为无用；若各自归禄，却又不妨。此格有七法：

  一曰青云得路，如戊子、甲寅、乙亥、己卯，柱中无一点官星，身旺得局，有印生助，虽子刑卯禄，不能破局，故贵。又壬午、庚戌、壬子、辛亥，身旺印助，登戊辰进士，为刑部郎中，作杂气格论尤是。

  二曰官星坐禄，如丙申、丙申、丙申、癸巳，丙以癸为正官，生七月金乡有托，运行西北官生旺之乡，丙临申无气，三丙相倚，冲寅长生，癸官临巳，用神坐贵，得财官双美，故少年及第，中年拜相。

  三曰归禄逢二德，如辛亥、辛卯、甲寅、丙寅，甲专禄，而得丙寅为食会禄，甲为月德，月令辛卯为甲正官，辛逢二月无气，二寅中丙合去二辛，止有二寅为甲之禄，月德逢归禄，乃平章辅国英雄。

  四曰归禄逢印绶，如丙戌、癸巳、戊午、丁巳，柱无一点官煞，止用印为主，归禄逢印绶，文贵之象。

  余诸变例，皆本此意推衍，不具载。

- 分字分词释义：

  - 日禄：日干在十二支中的临官、禄地，如甲禄在寅、丁禄在午等。
  - 日禄归时：日柱之禄不在日支，而回归到时支上，形成“禄在时位”的结构。
  - 没官星：命局中无明官或官不显，要以禄位自身为尊，不再另以官煞为主。
  - 青云得路：比喻仕途得路、平步青云，是本格的总称。
  - 聚福归禄：除时支外，年、月、日支亦见同一禄位，形成多重禄聚之象。
  - 互换禄：日禄归时、时禄归日，彼此互为禄地，相互成就。
  - 分禄：月日天元同而仅时支归禄，禄气分散，各自无力。
  - 青云七法：古人概括日禄归时的七种典型形态，如青云得路、官星坐禄、归禄逢二德、归禄逢印绶等。

- **规范化释义（primary_lang_explained）**：

  日禄归时格，是围绕“日干之禄落在时支”展开的一类贵格。七个日干（甲寅、丁午、戊巳、己午、庚申、壬亥、癸子）各有本禄，本来应坐在日支；若命局中日支不临禄地，而时支恰好为日禄所在，便构成“日禄归时”。此时，名与利的出路往往由“晚出”“后发”的时位引领，而非出于早年或家世。

  本格的关键在于：一方面，命局中不宜另有显露的官星来争主事权——所谓“没官星”；另一方面，日主必须坐旺、得印生、得财、伤、食等周全配合，使禄位真正能承载权力与福祉。否则，即便形式上“日禄归时”，也难免落入“分禄”“建禄”等低一格的形态。

  原文列举多种变化：有的重在“官星坐禄”，有的重在“归禄逢二德”、或“归禄逢印绶”，实质上都是围绕“禄位所在的支神，是否同时承载官、德、印”等不同能量来判断贵贱高下。

- 核心要点：

  - 日禄归时以“禄地在时支、命局无明官”为基本骨架，是一种“以禄代官”的贵格。
  - 成格关键：日主坐旺有印，时禄不受刑冲空亡，比劫不得分夺禄气。
  - 聚福、互换、逢德、逢印等变化，是在基本格局上的层层加分；若有官煞显露、禄位填实或空亡，则层层减分。
  - 在实务中，应先确定是否真的“无官可用”，再看日禄归时是否足以担任“官”的角色，避免与正常财官格混用。

- 详细解说：

  从命理结构看，日禄归时与前文“遥禄”“拱禄”“冲禄”等格局，都属于对“禄位”的特殊运用：

  - 遥禄多通过合冲远引禄地；
  - 拱禄通过日时夹拱；
  - 冲禄则以冲动对宫禄位；
  - 日禄归时则是“禄不在日而归于时”。

  这一格局特别强调“晚发”与“后位”：时柱象征人生后段或晚成之机，禄归于时，常见早年平平、中年以后渐入佳境之象。文中“青云七法”展示了不同组合的体例：

  - 若时禄配印，则多见以文章、学术、专业资格成名；
  - 若时禄配财，则多见以经商、资源调配致富；
  - 若时禄又逢二德（天德、月德）等吉神，则常有“扶国辅政”的象。

  需要特别警惕的是：一旦禄位重叠过多而无配套官、印、财、食，如“重见禄位”却财官俱弱，则仍只能视作建禄身旺；又或者月日天元同而仅时禄孤立，则成“分禄”，气散而难以成格。这些在原文中都通过例命与歌诀逐一呈现，本稿在此只提纲挈领。

- **校勘与字词辨析（双语）**：

  - 原文“日禄归时没官星，号青云得路”一句，为本格之总纲，本稿在分层结构中全部保留，并以此为小节标题之意涵来源。
  - 关于“日禄归时七法”，原文展开颇多，本稿在 L1 层仅保留代表性条目，并提示“余诸变例本此意推衍”，为后续 L2/L3 层留出空间。
  - 对“聚福归禄”“互换禄”“分禄”等术语，本稿在释义中统一给出现代语义，避免与一般“聚禄”“分财”等概念混淆。
  - **English**：
    - The sentence "Day-Salary Returns to Hour without official star, called Azure Cloud Gets the Path" is the guiding principle; this edition preserves it as the source for section titles.
    - Regarding the "seven methods of Day-Salary Returns to Hour," this edition keeps representative items in L1 and notes "other variations extend from this principle" for future L2/L3 layers.
    - Terms like "Gathered-Fortune Returns-Salary," "Exchange-Salary," and "Divided-Salary" are given unified modern interpretations to avoid confusion with general "gathered salary" or "divided wealth" concepts.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_045]` `[trigger: 日禄归时定义]` `[factor_trigger: rilu_guishi_presence]` `[role: 主干]` 日禄归时没官星，号青云得路。 → 《三命通会》卷六#日禄归时
  - `[ns_smth_06_046]` `[trigger: 增强条件]` `[factor_trigger: ri_gan_zuo_wang AND yin_sheng]` `[role: 主干依赖]` 喜日干坐旺、印绶生、月透财元、伤食、天月二德，主大富贵。 → 《三命通会》卷六#日禄归时
  - `[ns_smth_06_047]` `[trigger: 失效条件]` `[factor_trigger: xing_chong_po_hai OR kong_wang]` `[role: 条件分支]` 忌刑冲破害、空亡死绝、及劫财分禄、倒食作合、官煞克制。 → 《三命通会》卷六#日禄归时
  - `[ns_smth_06_048]` `[trigger: 互换大贵]` `[factor_trigger: huhuan_lu AND da_gui]` `[role: 总结]` 如甲申见庚寅、乙酉见辛卯、壬午见丁亥、癸亥见壬子等类，俱主大贵享福。 → 《三命通会》卷六#日禄归时

- **完整对等诠释（secondary_lang_full）**：
  The "Day-Salary Returns to Hour" pattern is built around seven specific day-pillars—Jia-Yin, Ding-Wu, Wu-Si, Ji-Wu, Geng-Shen, Ren-Hai and Gui-Zi—where the day-master's salary branch lands in the hour pillar rather than the day pillar. Because the hour pillar symbolises the later portion of life and one's legacy, this configuration often manifests as "late blooming": an unassuming early career followed by rising fortune in middle age and beyond. The classic epithet "Azure Cloud Path" (qingyun de lu) captures this trajectory of ascending to high station as if riding clouds.
  
  The pattern works best when there is no obvious official star competing on the stems. In such cases the salary itself assumes the noble function that an official would otherwise provide—hence "salary substitutes for official". Critical supporting factors include the day-master sitting strong, receiving Seal support, and having wealth, Eating-God or Hurting-Officer to circulate energy. If the salary position is isolated, clashed, voided or divided among too many parallel stars, the pattern degrades into mere "strong-body with salary" and loses its noble character.
  
  Ancient texts enumerate seven variations under the umbrella of "Azure Cloud Methods": Azure Cloud Path proper, Official Sitting on Salary, Salary Meeting Two Virtues, Salary Meeting Seal, and so on. Each variation adds a layer of enhancement when the salary pillar simultaneously carries official, virtue or Seal energy. Conversely, if excessive Robbery-of-Wealth stars divide the salary, or if the salary falls into emptiness or clash, the pattern collapses. In practice one must first confirm that no usable official star exists elsewhere, then verify that the hour-salary can genuinely shoulder the role of noble anchor."""
    normalized_text_zh: str = """"""
    subject: str = "七日禄归时与青云得路"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_14', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_factor_9', 'bazi_semantic', 'bazi_state_day_master_degree', 'bazi_semantic', 'bazi_condition_factor_142', 'bazi_semantic', 'bazi_condition_factor_143', 'bazi_semantic', 'source_ref', 'rel_smth_06_034', 'rilu_guishi_presence', 'rel_smth_06_035', 'luwei_chengzai_score', 'rel_smth_06_036', 'xingchong_kongwang_risk', 'evi_smth_06_034', 'rilu_guishi_presence', 'rule_qingyun', 'evi_smth_06_035', 'rizhu_zuowang_yinsheng', 'rule_zuowang', 'evi_smth_06_036', 'xingchong_kongwang_risk', 'rule_fenlu', 'map_smth_06_023', 'map_smth_06_024']
    
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
        l1_anchor="smth_v1.0.0_七日禄归时与青云得路_001_L1",
    )
    version: str = "1.0.0"
