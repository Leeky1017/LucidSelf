"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412334
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
    semantic_id="smth_v1.0.0_六乙鼠贵格与子时之贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙鼠贵格与子时之贵(SemanticEntry):
    """
    - **原文（source_text）**：

  《喜忌篇》云：阴木独遇子时，为六乙鼠贵之地。乙以子申为贵神，独遇子者，用鼠不用猴也。乙用庚金为官星，得丙子时，以子上丙火遥归巳中本禄，巳来合申，申来...
    """
    
    original_text: str = """- **原文（source_text）**：

  《喜忌篇》云：阴木独遇子时，为六乙鼠贵之地。乙以子申为贵神，独遇子者，用鼠不用猴也。乙用庚金为官星，得丙子时，以子上丙火遥归巳中本禄，巳来合申，申来动子，是谓申子辰三合会贵，谓申中带将庚来，乙日得官星；用申时，则官星显露，所以不取。若子字多，谓之聚贵，尤妙。年月中有午冲、丑绊，则子不能遥禄，申庚为官露，酉辛为煞露，被丙伤，子反不中矣。岁运同。

  此格要月通木局，日下支神皆是木旺之地，水印亦可，忌见金火。若岁运逢申酉，凶悔，东方渐退，午运则亡。如一命：壬寅、辛亥、乙未、丙子，合格；若乙丑日绊子、乙酉日煞伤，则减分数。一子字怕见卯刑、丑绊，多则不妨；透辛字不旺，再有丙丁合克，丙合辛化水，运顺行不伤贵。如己丑、丙子、乙卯、丙子，两子夹一卯；丁巳、壬子、乙丑、丙子，两子夹一丑，虽犯上忌，却是交夹贵中生，故皆大贵。若生夏令，只以伤官论；生七八月，贫下。如得庚申月、运北地，却以官论。生四季，有财库，喜水局、伤官、食神、南运，亦吉。凡月令见财官印旺，即以财官取用，不以午冲子为祸。如合鼠贵柱，有未合午，略有损坏，富而虚名。《相心赋》云：六乙鼠贵，遇午冲而赤贫如洗。诗曰：乙木生临丙子时，要无午破卯刑之，四柱不逢申酉丑，管教年少拜丹墀。又：乙日生人得子时，名为鼠贵最为奇，切嫌午字来冲破，辛酉庚申总不宜。又：六乙生人时遇子，既带官星复用此，庚申辛酉马牛欺，一位逢之为丐子。

- 分字分词释义：

  - 阴木独遇子时：乙为阴木，子为水，指乙日配子时且子为唯一的子支，形成“六乙鼠贵”的基本结构。
  - 六乙鼠贵：六个乙日（乙丑、乙卯、乙巳、乙未、乙酉、乙亥）配子时成格，因子属鼠，故名“鼠贵”。
  - 乙以子申为贵神：乙木以子水、申金为贵神，其中申兼藏庚金为官。
  - 用鼠不用猴：独遇子时而不用申时入格，强调贵神在子而不在申；申时官星显露，格局改变。
  - 丙子时：丙火在子上，子中藏癸，构成火水同宫，为乙木带官的关键时点。
  - 遥归巳中本禄：子上丙火象征其禄归于巳中丙禄，巳来合申、申动子，成申子辰三合会贵之势。
  - 聚贵：命局中子字不止一位，子气聚合，贵气集中。
  - 遥禄：不直接坐禄地，而是通过合冲遥引禄气（本例为子引巳中禄）。
  - 木局、木旺之地：指寅卯辰、亥卯未等木旺三合局，或日支、月令属木，助乙身旺。
  - 赤贫如洗：形容午冲子、结构被破时，原本的鼠贵反转为极端贫困。

- **规范化释义（primary_lang_explained）**：

  六乙鼠贵格，是为乙日配子时的一种“以子起官、聚贵于鼠”的格局。乙木以庚金为官星，以子、申为贵神；在丙子时，子上丙火可以遥归巳中本禄，再由巳合申、申动子，三者联动，形成“申子辰三合会贵”的局面。其精妙在于：官星庚金并不明露在天干，而是藏于申中，由丙子—巳—申—子这一连锁结构暗中引动。

  格局要求“阴木独遇子时”：一方面，乙日必须配子时，且最好只有一位子在关键位置；另一方面，月令与日支宜通木局或得水印相扶，使乙木身旺可任官星。若再兼得多子构成“聚贵”，则贵气越集中。反之，如年月中有午冲、丑绊，则子水不能遥禄，申庚官星、酉辛煞星被丙火冲合显露，局面转而不吉；岁运行至申酉之地，也容易以官煞冲破原有精微结构。

- 核心要点：

  - 六乙鼠贵的核心，是乙日配子时，通过“丙子 → 巳禄 → 申庚 → 子申辰”这一链条暗起官星与贵神。
  - 成格前提是身旺、木局或水印得地，且子位不被午冲、丑绊、申酉金局破坏。
  - 一位子为“独贵”，多位子则成“聚贵”；但若伴随卯刑、丑绊过重，反成损格。
  - 本格重贵轻富，多应科甲名位、少年得志；若被午、申、酉破坏，则易落入“富而虚名”甚至赤贫之象。

- 详细解说：

  从结构上看，六乙鼠贵与卷六前诸“遥禄”“遥巳禄”“飞天禄马”等格一脉相承，都是围绕“远处起官、暗中起禄”的体系。不同在于：

  - 六乙鼠贵以“子”为枢纽：子为乙之贵神之一，也是长生之地；
  - 丙子时将丙火安置在子上，使官禄之源与长生之地重合；
  - 巳为丙禄，巳合申、申动子，构成申子辰三合水局，水印既生乙身又联通庚官。

  这种布局使得乙木并非“硬顶官星”，而是借贵神、禄地、合局来承载官煞压力，所以古书反复强调“阴木独遇子时”为奇。若改用申时，则庚官显露于申，官煞力线过于直接，反失“鼠贵”微妙的暗贵格局。

  原文列举若干命例，说明在现实命局中，往往会出现“上犯下合”的复杂情形：如两子夹卯、两子夹丑，表面看似午冲、卯刑、丑绊皆有，但因子位成“交夹格”，反而在冲合之间孕育出更强的贵气。这类结构必须通盘权衡身旺身弱、月令用神，不宜凭一两条“犯上忌”便仓促定论。

- **校勘与字词辨析（双语）**：

  - 原文“阴木独遇子时，为六乙鼠贵之地”一句，为格名与结构总纲，本稿据底本保留，只在释义中解释为“乙日配子时且贵在子位”。
  - “乙以子申为贵神，独遇子者，用鼠不用猴也”中，“用鼠不用猴”即强调本格专取子而不取申，本稿在白话中明确这一点，以避免误以为申亦同等成格。
  - 关于“子字多，谓之聚贵”，本稿按上下文将其理解为“多子叠现而不被午冲、卯刑、丑绊破坏”的情形，并在详细解说中提示须结合全局判断。
  - “六乙鼠贵，遇午冲而赤贫如洗”一句，本稿保留原文，作为格局被午火冲破时的极端反例，不单独视为必然结局。
  - **English**：
    - The sentence "Yin Wood alone meeting Zi hour is the territory of Six Yi Mouse-Noble" is the guiding principle; this edition explains it as "Yi day with Zi hour, nobility in Zi position."
    - The phrase "use mouse not monkey" emphasizes taking Zi exclusively rather than Shen; this edition clarifies this to avoid confusion with Shen-noble patterns.
    - Regarding "multiple Zi means gathered nobility," this edition interprets it as "multiple Zi appearing without being clashed by Wu, punished by Mao, or fettered by Chou."
    - The sentence "Six Yi Mouse-Noble meeting Wu clash becomes destitute" is preserved as an extreme counter-example when the pattern is broken by Wu fire.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_041]` `[trigger: 六乙鼠贵定义]` `[factor_trigger: liuyi_shugui_presence]` `[role: 主干]` 阴木独遇子时，为六乙鼠贵之地。 → 《三命通会》卷六#六乙鼠贵
  - `[ns_smth_06_042]` `[trigger: 用鼠不用猴]` `[factor_trigger: yong_shu_bu_yong_hou]` `[role: 主干依赖]` 乙以子申为贵神，独遇子者，用鼠不用猴也。 → 《三命通会》卷六#六乙鼠贵
  - `[ns_smth_06_043]` `[trigger: 聚贵与冲绊]` `[factor_trigger: ju_gui OR wu_chong_chou_ban]` `[role: 条件分支]` 若子字多，谓之聚贵，尤妙。年月中有午冲、丑绊，则子不能遥禄。 → 《三命通会》卷六#六乙鼠贵
  - `[ns_smth_06_044]` `[trigger: 年少拜丹墀]` `[factor_trigger: nianshao_bai_danchi]` `[role: 总结]` 乙木生临丙子时，要无午破卯刑之，四柱不逢申酉丑，管教年少拜丹墀。 → 《三命通会》卷六#六乙鼠贵

- **完整对等诠释（secondary_lang_full）**：
  The "Six Yi Mouse-Noble" pattern is a subtle remote-salary configuration for Yi days born at Bing-Zi hour. Yi Wood takes Geng metal as its Proper Official and regards Zi and Shen as its noble-god branches. In this pattern we "use the Mouse (Zi) and not the Monkey (Shen)": the hour pillar Bing-Zi places Bing fire above Zi water, and Bing's salary seat is in Si. Si then combines with Shen, Shen activates Zi, forming the Shen-Zi-Chen water trine that quietly brings Geng—Yi's official star hidden in Shen—into play without exposing it directly on the stems.
  
  The key is that the official star arrives from a distance rather than standing in plain sight. If one were to use Shen hour instead, Geng would be openly displayed, and the delicate "mouse noble" mechanism would collapse. When the chart contains multiple Zi branches, the pattern is called "Gathering Noble" and becomes even more powerful. However, if Wu fire clashes Zi, or Mao punishes Zi, or Chou ties Zi, then the remote link is severed. The classic warning "Six Yi Mouse-Noble, when Wu clashes, becomes destitute" captures this extreme reversal. Successful formation requires a wood-strong month or water-Seal support; reputation often outweighs material wealth."""
    normalized_text_zh: str = """"""
    subject: str = "六乙鼠贵格与子时之贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_yi_marker', 'bazi_semantic', 'bazi_structure_zi_si_shen', 'bazi_semantic', 'bazi_state_zi_1', 'bazi_semantic', 'bazi_state_wood', 'bazi_semantic', 'bazi_condition_wu_mao_chou', 'bazi_semantic', 'bazi_condition_shen_you_metal', 'bazi_semantic', 'source_ref', 'rel_smth_06_031', 'liuyi_shugui_presence', 'rel_smth_06_032', 'ziwei_chuncu_jugui', 'rel_smth_06_033', 'shenyou_jinju_minglu_risk', 'evi_smth_06_031', 'ziyao_si_heshen_lujing', 'rule_shugui', 'evi_smth_06_032', 'ziwei_chuncu_jugui', 'rule_ziwei', 'evi_smth_06_033', 'wuchong_maoxing_chouban', 'rule_chongxing', 'map_smth_06_021', 'map_smth_06_022']
    
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
        l1_anchor="smth_v1.0.0_六乙鼠贵格与子时之贵_001_L1",
    )
    version: str = "1.0.0"
