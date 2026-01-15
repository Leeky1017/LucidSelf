"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523346
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
    semantic_id="zpzq_v1.0.0_予自束发就传_即喜读子史诸集_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 予自束发就传即喜读子史诸集(SemanticEntry):
    """
    - **原文（source_text）**：
  予自束发就传，即喜读子史诸集，暇则子平《渊海》、《大全》略为流览，亦颇晓其意。然无师授，而于五行生克之理，终若有所未得者。后复购得《三命通会》、《星学...
    """
    
    original_text: str = """- **原文（source_text）**：
  予自束发就传，即喜读子史诸集，暇则子平《渊海》、《大全》略为流览，亦颇晓其意。然无师授，而于五行生克之理，终若有所未得者。后复购得《三命通会》、《星学大成》诸书，悉心参究，昼夜思维，乃恍然于命之不可不信，而知命之君子当有以顺受其正。

- 原注（原文注解）：
  　　原书此段为自序开篇，并无另行夹注。

- 分字分词释义：
  - 予：我，自称。
  - 束发：古代十五岁左右束发为冠，指少年时期。
  - 就传：入学就读，开始受业于师长与经典。
  - 子史诸集：诸子百家及史传文集，指广泛的经史子集阅读基础。
  - 略为流览：大致翻阅浏览，非逐字精读。
  - 五行生克之理：以五行生克说明万物变化与命局吉凶的根本法理。
  - 终若有所未得者：始终好像还有没有领会透彻之处。
  - 悉心参究：尽心钻研、参详考究。
  - 恍然：忽然大悟的样子。
  - 知命之君子：不以命理逃避责任，而是明白命运边界、安于义理之人。
  - 顺受其正：顺着“正当之命”去承担，不妄求非分之福。

- **规范化释义（primary_lang_explained）**：
  从少年入学起，我就喜欢阅读诸子百家和史传典籍，闲时也会翻看子平命理的《渊海》、《大全》，对其中义理多少有所领会。但因为没有老师系统传授，对于五行生克的根本规律，总觉悟得不真切。后来又购得《三命通会》、《星学大成》等书，便专心致志地研读推求，昼夜思索，终于忽然明白：人的命运实在不可轻言不信；而真正懂得命理的君子，应当在理解命运规律的前提下，顺受自己应当承担的那一份"正命"。
- **完整对等诠释（secondary_lang_full）**：  
  From my teenage years, once I entered formal study, I was drawn to the classical writings of philosophers and historians. In spare moments I also browsed Ziping manuals such as Yuanhai and Daquan and gained a rough sense of their ideas. Yet without systematic guidance from a teacher I still felt that I had not truly grasped the fundamental principles behind the Five Elements and their cycles of mutual generation and control. Later, after obtaining works like Sanming Tonghui and Xingxue Dacheng, I devoted myself to them day and night. Only then did I awaken to two points: destiny patterns are real and cannot simply be dismissed, and a person who truly understands destiny should accept the rightful share that belongs to him and fulfil his responsibilities within it, rather than hiding behind "fate" to evade duty or chase blessings that lie beyond his proper lot.

- 详细解说：
  - 命理学习应有扎实的人文基础：先读子史诸集，再入术数，不可本末倒置。
  - 经典需系统研读与反复思维，而非只靠断语与口诀。
  - “不可不信”不是迷信，而是承认规律存在；“顺受其正”强调在规律之内守义尽分。

- 核心要点：
  - 以“经史”打底，再学命理，避免术数脱离人伦与历史经验。
  - 五行生克是命理的根本秩序，不能只背格局名目，不究其理。
  - 真正的知命，是用命理帮助自己顺势尽责，而不是逃避或纵欲。

- 应用推演：
  1) 先广读经史子集，建立世界观与价值观。
  2) 再系统研读命理经典（渊海、大全、三命通会、星学大成等）。
  3) 在阅读中不断推演思考，而非停留在记诵与查表。
  4) 把“顺受其正”当作命理解读的底线：断吉凶不离义理。

- 反例与边界：
  - 只背断语、不懂经史：易把命理用成恐吓或讨巧的工具。
  - 把“命不可不信”理解为“凡事推给命”，反而违背“君子当有以顺受其正”的本意。

- 小例（示意）：
  - 学命理者若只急于“算准”，不肯先打基础、读原典，多半停留在术而不入道。

- 校勘与字词辨析（双语）：
 - **中文**：“星学大成”一书，有部分版本作“星平大成”。两书皆为星命名著，今从本书原文与中华典藏本作“星学大成”，并存此异文以备考。
 - **English**: In some editions the title of the work appears as "Xingping Dacheng" rather than "Xingxue Dacheng". Both are well-known classics of astral lore. This edition follows the reading "Xingxue Dacheng" found in the base text and in the Zhonghua Canon edition, while recording the variant for reference.

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_001]` `[trigger: 阳顺阴逆]` `[factor_trigger: (stem_polarity=yang AND changsheng_direction=forward) OR (stem_polarity=yin AND changsheng_direction=reverse)]` `[role: 主干依赖]` 阳干顺行长生，阴干逆行长生。 → 《子平真诠·论阴阳生死》#顺逆
  - `[ns_zpzy_002]` `[trigger: 长生十二宫]` `[factor_trigger: twelve_stages_sequence=changsheng_muyu_guandai_linguan_diwang_shuai_bing_si_mu_jue_tai_yang]` `[role: 主干依赖]` 长生沐浴冠带临官帝旺衰病死墓绝胎养。 → 《子平真诠·论阴阳生死》#十二宫
  - `[ns_zpzy_003]` `[trigger: 死绝活看]` `[factor_trigger: (stage=si OR stage=jue) AND (deshi=true OR dedi=true)]` `[role: 条件分支]` 死绝非必凶，得时得地则生机自足。 → 《子平真诠·论阴阳生死》#活看
  - `[ns_zpzy_004]` `[trigger: 五行本源]` `[factor_trigger: cosmology=yiqi AND dongjing_fenyinyang AND laoshao_chengsixiang]` `[role: 主干]` 天地之间一气而已，动静分阴阳，老少成四象。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_005]` `[trigger: 土为中和]` `[factor_trigger: element_tu AND role=zhonghe AND function=chengzai_tiaoji]` `[role: 主干依赖]` 土者阴阳老少冲气所结，承载调剂诸行。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_006]` `[trigger: 生克同功]` `[factor_trigger: four_seasons AND shengke_cycle AND tonggong_chengsui]` `[role: 主干依赖]` 春夏秋冬相生相克，同功于成岁。 → 《子平真诠》#论阴阳生克
  - `[ns_zpzy_007]` `[trigger: 克为节制]` `[factor_trigger: ke_relation AND function=jiezhi AND ke_yi_baosheng]` `[role: 条件分支]` 杀者使发泄于外者藏收于内，克以保生。 → 《子平真诠》#论阴阳生克
  - `[ns_zpzy_008]` `[trigger: 八格取用]` `[factor_trigger: pattern_type IN (zhengguan, cai, yin, shi, pianguan, shangguan, yangren, jianlu)]` `[role: 主干]` 八格者：正官、财、印、食、偏官、伤官、阳刃、建禄。 → 《子平真诠》#论用神
  - `[ns_zpzy_009]` `[trigger: 月令为纲]` `[factor_trigger: yongshen_source=yueling AND rigan_pei_yueling_dizhi]` `[role: 主干]` 八字用神，专求月令，以日干配月令地支。 → 《子平真诠》#论用神
  - `[ns_zpzy_010]` `[trigger: 生旺库绝]` `[factor_trigger: twelve_stages_complete_cycle]` `[role: 主干依赖]` 长生沐浴冠带临官帝旺衰病死墓绝胎养。 → 《子平真诠》#论阴阳生死
  - `[ns_zpzy_011]` `[trigger: 长生帝旺]` `[factor_trigger: stage IN (changsheng, linguan, diwang) AND qi_state=sheng]` `[role: 主干依赖]` 长生临官帝旺，气之盛也。 → 《子平真诠》#论阴阳生死
  - `[ns_zpzy_012]` `[trigger: 衰病死绝]` `[factor_trigger: stage IN (shuai, bing, si, mu, jue) AND qi_state=shuai]` `[role: 主干依赖]` 衰病死墓绝，气之衰也。 → 《子平真诠》#论阴阳生死
  - `[ns_zpzy_013]` `[trigger: 胎养长生]` `[factor_trigger: stage IN (tai, yang, changsheng) AND qi_state=fangxing_weiai]` `[role: 主干依赖]` 胎养长生，方兴未艾。 → 《子平真诠》#论阴阳生死
  - `[ns_zpzy_014]` `[trigger: 木主仁]` `[factor_trigger: element=mu AND virtue=ren AND character=(zheng, ci)]` `[role: 主干依赖]` 甲乙木主仁，性直心慈。 → 《子平真诠》#上卷
  - `[ns_zpzy_015]` `[trigger: 火主礼]` `[factor_trigger: element=huo AND virtue=li AND character=(ji, ming)]` `[role: 主干依赖]` 丙丁火主礼，性急心明。 → 《子平真诠》#上卷
  - `[ns_zpzy_016]` `[trigger: 格局为纲]` `[factor_trigger: geju=gang AND lunming_foundation]` `[role: 主干]` 以格局为纲，论命之本。 → 《子平真诠》#上卷
  - `[ns_zpzy_017]` `[trigger: 用神为目]` `[factor_trigger: yongshen=mu AND jixiong_criterion]` `[role: 主干]` 用神为目，吉凶之判。 → 《子平真诠》#上卷
  - `[ns_zpzy_018]` `[trigger: 相神辅格]` `[factor_trigger: xiangshen_exists AND function=fuge AND geju_level_increase]` `[role: 主干依赖]` 相神辅格，格局愈高。 → 《子平真诠》#上卷
  - `[ns_zpzy_019]` `[trigger: 命局组合]` `[factor_trigger: mingju_zuhe AND jixiong_manifest]` `[role: 总结]` 命局组合，吉凶自现。 → 《子平真诠》#上卷
  - `[ns_zpzy_020]` `[trigger: 格成格破]` `[factor_trigger: (ge_status=cheng AND result=ji) OR (ge_status=po AND result=xiong)]` `[role: 总结]` 格成则吉，格破则凶。 → 《子平真诠》#上卷
  - `[ns_zpzy_021]` `[trigger: 日主强弱]` `[factor_trigger: rizhu_strength IN (qiang, ruo) AND geju_foundation]` `[role: 主干依赖]` 日主强弱，定格局之基。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "予自束发就传，即喜读子史诸集"
    factor_refs: list = ['wuxing_shengke', 'zhiming_attitude', 'shunshou_qizheng', 'ziping_method', 'text_yuanhai', 'text_sanming_tonghui']
    
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
        l1_anchor="zpzq_v1.0.0_予自束发就传_即喜读子史诸集_001_L1",
    )
    version: str = "1.0.0"
