"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458201
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
    semantic_id="smth_v1.0.0_日主自作官星_001",
    book_id="sanming",
    engine_id="bazi"
)
class 日主自作官星(SemanticEntry):
    """
    - **原文（source_text）**：
  经云：金若遇火，有重权，防御刺史臣（如庚午、庚寅、庚戌、辛巳、辛未等日）。水若遇土，入官局，可沾侍郎禄（如壬午、壬戌、癸巳、癸丑、癸未等日）。木若遇金...
    """
    
    original_text: str = """- **原文（source_text）**：
  经云：金若遇火，有重权，防御刺史臣（如庚午、庚寅、庚戌、辛巳、辛未等日）。水若遇土，入官局，可沾侍郎禄（如壬午、壬戌、癸巳、癸丑、癸未等日）。木若遇金，主伤衰化煞，为权势若雷（如甲申、甲戌、乙巳、乙酉、乙丑等日）。火若遇水，主兵权，为将镇三边（如丙申、丙子、丙辰、丁亥、丁丑等日）。土若遇木，为正禄八座三台福（如戊寅、戊辰、己卯、己未、己亥等日）。此即白虎持世等格要，日主与官贵相亭，偏枯则不成造化，大忌刑冲破害，伤损贵气，不成格矣。
  
  如庚午日，坐丁官，喜见甲乙财生官，戊己印生身；忌丙煞杂官，癸水伤官，子冲破午，余干例推。又曰：日主自作官星，不大忌冲，譬执物在手，无可夺之理，主为人伶俐好色，机变有谋。若只日下一位，行财官运方发；若生月带禄，支坐财官，生时得地，方为真贵。壬午日是禄、马同乡，更逢庚戌时为妙。壬自坐禄，有庚辛制甲乙，使壬得己土，为官贵。如戊辰日，辰中乙木为戊之官，春生贵重，秋生虚誉，无禄。古歌曰：座下官星最是奇，多因祖荫见根基，若还行往印乡去，脱去青衣换紫衣。

- 分字分词释义：
  - **天元作禄**：以日主天干为"天元"，自坐官星于日支之下，谓之天元作禄，亦即"日坐官星"。
  - **金若遇火 / 水若遇土 / 木若遇金 / 火若遇水 / 土若遇木**：分别指五行日主自坐其官星之日柱组合，如庚午、壬午、甲申、丙子、戊寅等，各有不同官位与权柄之象。
  - **白虎持世**：白虎为西方金神，此处泛指官煞格局中执掌权柄者，"持世"即主事在身，有执掌全局之象。
  - **相亭**：相称、相当之意，指日主与官星力量均衡，不偏不枯。
  - **禄马同乡**：如壬午日，午为壬之财马，壬又得己土为官，禄马并临一处，故曰禄马同乡。
  - **脱去青衣换紫衣**：青衣指卑职，紫衣指显贵，喻由寒微而升至显宦。

- **规范化释义（primary_lang_explained）**：
  本节论"日主自作官星"之格，即天元作禄。金日主坐火官，如庚午、庚寅、庚戌、辛巳、辛未，多主掌兵权、守边防；水日主坐土官，如壬午、壬戌、癸巳、癸丑、癸未，易入官局，近侍郎之禄；木日主坐金官，如甲申、甲戌、乙巳、乙酉、乙丑，主以伤煞化权，声势如雷；火日主坐水官，如丙申、丙子、丙辰、丁亥、丁丑，多掌兵权，镇守三边；土日主坐木官，如戊寅、戊辰、己卯、己未、己亥，则正禄在身，有三台八座之福。此等日柱，皆属日主与官星同在一柱，如执物在手，不易被夺，若日主与官星之力相亭，不偏不枯，又不被刑冲破坏，方成贵格。
  
  以庚午日为例，日支午中丁火为官，若再得甲乙财星生官、戊己印星生身，则官身两旺，为武职持权之象；若见丙煞杂官、癸水伤官、子冲破午，则贵气受损。壬午日尤为奇特，壬自坐禄，又兼财马同乡，再逢庚戌时，庚为壬之官，戌为财库，最为贵显。古歌所谓"座下官星最是奇，多因祖荫见根基，若还行往印乡去，脱去青衣换紫衣"，正是形容这类日坐官星之人，得祖荫与行运相助，由寒微而登高位的过程。

- **完整对等诠释（secondary_lang_full）**：
  This section describes the pattern of the day-stem "making its own salary", that is, sitting directly on its official star in the day branch. When metal day-masters sit on fire officials—such as Geng-Wu, Geng-Yin, Geng-Xu, Xin-Si or Xin-Wei—they tend to hold heavy military or defensive authority; when water day-masters sit on earth officials—such as Ren-Wu, Ren-Xu, Gui-Si, Gui-Chou or Gui-Wei—they are drawn into official formations and can enjoy ranks comparable to vice ministers. Wood day-masters sitting on metal officials—such as Jia-Shen, Jia-Xu, Yi-Si, Yi-You or Yi-Chou—often turn injury and Killing into power, with reputations that crash like thunder; fire day-masters sitting on water officials—such as Bing-Shen, Bing-Zi, Bing-Chen, Ding-Hai or Ding-Chou—frequently command troops and guard the borders; earth day-masters sitting on wood officials—such as Wu-Yin, Wu-Chen, Ji-Mao, Ji-Wei or Ji-Hai—carry proper salaries and enjoy the luck of "three terraces and eight seats". In all these cases the official star is in the same pillar as the self, like holding an object firmly in one’s hand, and so is not easily taken away.
  For the pattern to count as truly noble, however, the day-master and official must be balanced rather than biased or withered, and the day branch must not be damaged by punishments, clashes or harms. Additional support from wealth stars that generate the official and from Seals that nourish the body further raises the quality: such people often combine inherited backing with their own talent and good fortune to rise from modest circumstances to high office, exactly as the old verse says about those who sit on their own official star and, when they travel into Seal lands, "take off the blue robe and put on the purple".

- 核心要点：
  - 天元作禄格的关键，在于**日主自坐官星**：官星离身最近，易得其力而不易被夺。
  - 日主与官星必须力量相亭：身太弱则难胜其官，身太强则压制其官，皆非中正之道。
  - 行运上宜行财官印旺地，以成其官格；大忌刑冲破害日支，或伤官、杂煞扰乱官星。
  - 此格多主近身之权，如实权职位、兵权、近侍之职，若配合印绶与财星，则由祖荫与自身才力共成其贵。

- 详细解说：
  与"岁德正官"注重年柱根基不同，天元作禄更重视日柱自身结构：日主与官星同处日柱，象征个人本性与权力责任紧密相连。因此，命理上说"日主自作官星，不大忌冲"，意在强调这种结构比一般外来之官更牢固。但若日支遭重冲破害，则如脚下之地动摇，原有之牢固也会转成危机。
  
  此节列举的五行日柱组合，其实构成了一个小型的日柱贵格表：金遇火、木遇金、火遇水偏重武权与锋锐，水遇土、土遇木偏重文职与稳重。实际判命中，可将这些组合视为"日柱贵格候选"，再结合月令、全局与行运，审其到底成真贵、虚名，还是因偏枯、刑冲而失格。

- 校勘与字词辨析：
  - **"防御刺史臣"**：古代职官名，掌边防、治军与地方防御，今可大致理解为军政合一的地方高级官员。
  - **"侍郎禄"**：侍郎为尚书之副，位高俸厚，此处用以形容官职品级之高。
  - **"三台八座"**：三台指三公之属，八座指尚书诸曹，皆为朝廷高位，此处以形容土日自坐木官之尊贵。
  - **English**：
    - Describes nobility of Earth day sitting on Wood official.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_013]` `[trigger: 五行坐官]` `[factor_trigger: tianyuan_zuolu_presence AND wuxing_day_master]` `[role: 主干]` 金若遇火，有重权，防御刺史臣。水若遇土，入官局，可沾侍郎禄。 → 《三命通会》卷五#天元作禄
  - `[ns_smth_05_014]` `[trigger: 官星在手]` `[factor_trigger: ri_zhi_guanxing AND day_master_balance]` `[role: 主干依赖]` 日主自作官星，不大忌冲，譬执物在手，无可夺之理。 → 《三命通会》卷五#天元作禄
  - `[ns_smth_05_015]` `[trigger: 身官相亭]` `[factor_trigger: shen_guan_xiangting]` `[role: 条件分支]` 日主与官贵相亭，偏枯则不成造化，大忌刑冲破害，伤损贵气。 → 《三命通会》卷五#天元作禄
  - `[ns_smth_05_016]` `[trigger: 青衣换紫]` `[factor_trigger: xing_yun_yin_xiang AND zu_yin_support]` `[role: 总结]` 座下官星最是奇，多因祖荫见根基，若还行往印乡去，脱去青衣换紫衣。 → 《三命通会》卷五#天元作禄"""
    normalized_text_zh: str = """"""
    subject: str = "日主自作官星"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tianyuan_zuolu_presence', 'bazi_semantic', 'rizuo_guanxing_config', 'bazi_semantic', 'shen_guan_xiangting', 'bazi_semantic', 'cai_yin_fuchi', 'bazi_semantic', 'jinshen_quanbing', 'bazi_semantic', 'source_ref', 'rel_smth_05_010', 'tianyuan_zuolu_presence', 'rel_smth_05_011', 'shen_guan_xiangting', 'rel_smth_05_012', 'jinshen_quanbing', 'evi_smth_05_010', 'shen_guan_xiangting', 'rule_xiangting', 'evi_smth_05_011', 'jinshen_quanbing', 'rule_jinshen', 'evi_smth_05_012', 'cai_yin_fuchi', 'rule_fuchi', 'map_smth_05_007', 'map_smth_05_008']
    
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
        l1_anchor="smth_v1.0.0_日主自作官星_001_L1",
    )
    version: str = "1.0.0"
