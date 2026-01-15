"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.081129
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
    semantic_id="smth_v1.0.0_2_搜髓歌格局精要_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2搜髓歌格局精要(SemanticEntry):
    """
    - 原文（source_text）：
  造化先须看日主，后把提纲分次第。四柱专一论财官，身旺财官多富贵。
  若还身旺财官损，只是朝求暮讨儿。财官旺时日主旺，紫袍金带有何疑。
  财官旺而日主弱，运...
    """
    
    original_text: str = """- 原文（source_text）：
  造化先须看日主，后把提纲分次第。四柱专一论财官，身旺财官多富贵。
  若还身旺财官损，只是朝求暮讨儿。财官旺时日主旺，紫袍金带有何疑。
  财官旺而日主弱，运行身旺最为奇。日主旺而财官弱，运入财官利名驰。
  日主坐下有财官，月令相逢贵不难。总把财官为紧要，早年富贵禄高攀。
  财官微薄身太旺，太旺无依受孤寒。更有印来比劫助，伤妻克子可立看。
  官煞太重身更强，一逢制伏作贤良。煞官拱印贵不小，烜赫威名定振扬。
  生居九夏火土多，利逢水济贵中和。水火原来要既济，管教名利镇山河。
  火热炎炎如无水，运行水乡亦是美。水势滔滔若无土，运入土乡真可喜。
  东方木多宜西运，西方金旺爱东行。五行相济成造化，人命逢之福不轻。
  三丘五墓怕见重，骨肉参商损六亲。提纲刑冲克父母，日时对冲妻子屯。
  比劫伤官若再旺，不但伤妻更损儿。纵有一子亦不孝，或者乞养总非宜。
  身旺比肩坐驿马，兄弟飘蓬好潇洒。八字驿马纷交驰，身荣劳苦东西也。
  倘得身闲心不定，动则风流静则愁。若是财星坐驿马，妻贤无处不悠悠。
  财星入库主聚财，谨守资财不做人。妻儿悭吝善持助，只怕暗藏羊刃嗔。
  官煞重重不带财，妻能内助不和谐。公姑不敬全无礼，夺却夫权命所排。
  官星若也逢生旺，更得长生旺在时。子息聪明多俊秀，儿孙个个着绯衣。
  日主七煞带枭食，妻主虚胎小产多。经脉不调成血疾，更看行运又如何。
  男子枭食重重见，身弱多应痨病随。女人枭食非为吉，产难惊人病亦危。
  女命官旺兼财旺，招得贤夫更好儿。若是财官俱受损，伤夫克子有何疑。
  印绶生身身更旺，为人刑克主贫孤。若得官显财又显，亦为超迈贵人扶。
  女命若也伤官旺，坐下伤官会骂夫。朝暮喃喃口不绝，百年终是见刑枯。

- 分字分词释义：
  - **朝求暮讨**：乞丐。
  - **三丘五墓**：辰戌丑未。
  - **不做人**：吝啬，不通人情。
  - **着绯衣**：做官（绯袍）。
  - **骂夫**：伤官克官。

- **规范化释义（primary_lang_explained）**：  
  搜髓歌这一段把整套命理判断浓缩为几条“抓骨髓”的原则。首要是看日主与财官的力量对比：身旺而财官亦旺，格局清纯，则富贵两得；身旺而财官被冲克或落空，则反成“朝求暮讨”的乞丐命。若财官旺而日主偏弱，则需行身旺之运来托得起财官；反之，日主旺而财官单薄，则要靠行财官运来弥补结构缺口。其次是通过日坐、月令、行运三层叠加，看财官是否“得位而有源”：日坐财官，再逢财官月，行到财官运，多主贵显。再次，歌诀强调过旺的比劫与印绶会反向侵蚀六亲——身太旺又多比劫印绶时，往往伤妻克子、孤寒清苦。另一方面，官煞重而身强、且有食伤制伏、煞印相生，则能化煞为权，名扬一世。最后，歌中还穿插了调候与六亲判断：夏日火土偏燥，喜水济润；水泛则喜土以制；三丘五墓重重，容易刑克骨肉；驿马星临比肩财星，则一主兄弟飘泊，一主妻贤勤劳；枭神、七煞成格又无制伏时，则关涉病疾与婚育风险。

- **完整对等诠释（secondary_lang_full）**：  
  This companion to the Bone‑Marrow Song distills a working method for chart evaluation. It begins by insisting that one must first weigh the Day Master's strength against that of Wealth and Office. If the body is strong and Wealth/Office are also strong and clean, prosperity and rank come naturally; if the body is strong but its Wealth and Office are damaged, emptied or trapped, the same vigorous capacity finds no proper channel and may end up in begging and hardship. When Wealth and Office are abundant while the Day Master is weak, the ideal remedy is to encounter fortune cycles that reinforce the self so that it can carry the load. Conversely, when the self is robust but its Wealth and Office are meager, beneficial cycles of Wealth and Office can turn raw potential into social success.  
  The text further refines this by looking at whether Wealth/Office sit under the Day Master, are echoed by the month, and are supported by luck cycles. It warns that an over‑abundance of Parallels and Seals, particularly when they lack clear outlets, often translates into harm to spouse and children and a sense of lonely struggle. Heavy Killings and Officials paired with a strong body become noble when checked by Eating and Wounded stars or when they give rise to Seals—"transforming killing into authority". Climatic adjustment and kinship diagnostics are woven throughout: summer charts crave Water to cool Fire and enliven Earth; overflowing Water needs Earth to contain it; repeated graveyard branches point to strain among relatives; a Horse star under Parallels speaks of roving siblings, while under Wealth it suggests a hardworking, mobile spouse. Multiple layers of Seven Killings and Devouring Seal without adequate counterbalance foreshadow illness and reproductive issues. In short, the song offers a compact map of how balance, containment and outlet determine whether the same raw forces yield comfort, isolation, authority or loss.

- 核心要点：
  - **平衡论**：身旺财官旺最佳。
  - **调候论**：夏火喜水。
  - **六亲论**：伤官骂夫，财库吝啬。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_029]` `[trigger: 日主财官]` `[factor_trigger: rizhu_caiguan AND shenwan_fugui]` `[role: 主干]` 造化先须看日主，后把提纲分次第。四柱专一论财官，身旺财官多富贵。 → 《三命通会》卷十二#搜髓歌格局精要
  - `[ns_smth_12_030]` `[trigger: 调候既济]` `[factor_trigger: tiaohou_jiji AND shuihuo_xiangji]` `[role: 主干依赖]` 水火原来要既济，管教名利镇山河。火热炎炎如无水，运行水乡亦是美。 → 《三命通会》卷十二#搜髓歌格局精要
  - `[ns_smth_12_031]` `[trigger: 三丘五墓]` `[factor_trigger: sanqiu_wumu AND kegurou_liuqin]` `[role: 条件分支]` 三丘五墓怕见重，骨肉参商损六亲。提纲刑冲克父母，日时对冲妻子屯。 → 《三命通会》卷十二#搜髓歌格局精要
  - `[ns_smth_12_032]` `[trigger: 女命伤官]` `[factor_trigger: nvming_shangguan AND mafu_xingku]` `[role: 总结]` 女命若也伤官旺，坐下伤官会骂夫。朝暮喃喃口不绝，百年终是见刑枯。 → 《三命通会》卷十二#搜髓歌格局精要"""
    normalized_text_zh: str = """"""
    subject: str = "2 搜髓歌格局精要"
    factor_refs: list = ['engine_id', 'bazi_structure_day_master', 'bazi_state_unnamed', 'bazi_condition_wuxing_state', 'fire_water_balance', 'bazi_relation_degree', 'bazi_relation_yima', 'bazi_factor_39', 'source_ref', 'rel_smth_12_028', 'core_factor', 'rel_smth_12_029', 'cond_factor', 'rel_smth_12_030', 'risk_factor', 'evi_smth_12_028', 'core_factor', 'rule_name28', 'evi_smth_12_029', 'cond_factor', 'rule_name29', 'evi_smth_12_030', 'risk_factor', 'rule_name30', 'map_smth_12_019', 'map_smth_12_020']
    
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
        l1_anchor="smth_v1.0.0_2_搜髓歌格局精要_001_L1",
    )
    version: str = "1.0.0"
