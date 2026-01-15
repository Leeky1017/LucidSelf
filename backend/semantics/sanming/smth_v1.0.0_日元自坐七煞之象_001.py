"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458310
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
    semantic_id="smth_v1.0.0_日元自坐七煞之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 日元自坐七煞之象(SemanticEntry):
    """
    - **原文（source_text）**：
  谓甲申、乙酉等日。如乙丑日，丑中自坐辛金为煞，喜生春夏，乙木健旺，煞自有制，不喜明见丙丁。生秋月雕零，坐下藏鬼，岂不为害？凡值此等日，要日干倚旺，再无...
    """
    
    original_text: str = """- **原文（source_text）**：
  谓甲申、乙酉等日。如乙丑日，丑中自坐辛金为煞，喜生春夏，乙木健旺，煞自有制，不喜明见丙丁。生秋月雕零，坐下藏鬼，岂不为害？凡值此等日，要日干倚旺，再无官煞复克，喜印化煞，财旺身旺为福。如煞旺，有伤官合制，亦贵；如无助化，再行煞旺运，或再见煞克，为人必面目瘢痕，侏儒跛鳖，骈指瘤赘，奸贪猛暴，恃强不惮，累犯宪章。克重多夭，合格为武贵。但为人心多性急，阴险怀毒，僭伪谋害，不近人情。

- 分字分词释义：
  - **天元坐煞**：以日干为"天元"，其所坐之日支自藏七煞，如甲申、乙酉、乙丑坐辛等，谓之天元坐煞。
  - **坐下藏鬼**："鬼"即七煞，日支藏煞而不透干，如乙丑日丑中辛金，是煞潜伏于根基之下。
  - **春夏喜、秋冬忌**：春夏乙木健旺，足以驭煞；秋令金旺木衰，坐煞成"藏鬼为害"之象。
  - **印化煞、财旺身旺为福**：印绶可化煞生身，财旺身旺则可承煞之力，使七煞转为权力来源。
  - **伤官合制**：伤官透出合制七煞，有时亦可成贵，尤多见于武职或激烈职业。

- **规范化释义（primary_lang_explained）**：
  天元坐煞，是指日主自己坐在七煞之上，如甲申日、乙酉日等，或如乙丑日丑中自坐辛金为煞。若出生于春夏，乙木日主尚健旺，日支辛金七煞虽在，却自然受制，不致为祸；若生于秋季金旺木衰，则日支成"坐下藏鬼"，七煞伏于根基之下，一旦行运再激发，容易为害。
  
  凡遇此等日柱，必须日干有根有气，再无其他官煞重叠克身，且局中有印化煞、财旺身旺等配置，方可转凶为吉，成就武职之贵；若煞势过旺，而印、财、比劫等无以扶身制煞，则多主身体残疾（面目瘢痕、侏儒跛鳖、骈指瘤赘等），性情奸急狠毒，屡犯刑章，严重者多夭。

- **完整对等诠释（secondary_lang_full）**：
  'Heaven-prime sitting on Killing' refers to day-stems such as Jia-Shen or Yi-You where the day-master sits directly on its Seven Killing in the day branch—for example Yi day on Chou, with hidden Xin metal as Killing. When such a day is born in spring or summer, Yi wood is still strong enough to control the hidden Xin, so the Killing is naturally kept in check and one should avoid exposing further Bing or Ding fire on the stems to stir it up. If it is born in an autumn month when metal is flourishing and wood is withered, the same structure becomes 'ghosts hidden beneath the seat': the Killing lurks at the root and easily turns harmful when later fortune activates it.
  For people born on these days, the chart requires a robust, well-rooted day-master, no extra officials and Killings repeatedly striking the body, and preferably Seals that can transform Killing and strong wealth and body to carry it. When Killing is strong but properly combined with Hurting Officer to control and express it, the result can still be martial nobility. If Killing is strong and there is no help from Seal, wealth or peers to transform or support the self, and later fortune further strengthens Killing, then the pattern tends toward physical damage, harsh and violent temperament and repeated violations of law, with many dying young. Thus this structure can produce either powerful commanders who ride harsh energies, or deeply destructive lives, depending entirely on whether the self can master the Killing.


- 核心要点：
  - 天元坐煞格的关键，在于**日主有无力量驭煞**：身旺有制则成权贵，身弱无制则为祸根。
  - 春夏木旺时，乙木能御辛金之煞；秋冬金旺木衰，则藏煞易为病源和祸端。
  - 印化煞、财旺身旺、伤官合制等，是将天元坐煞转为武贵、权贵的主要制化路径。

- 详细解说：
  相比一般七煞，天元坐煞的特殊性在于：七煞直接根植于日主之根基（坐下之支），是一种"自带煞气"的结构。这使得命主的性格、多事之地以及人生遭遇往往与"煞"紧密相连：若能善用，则为果决、敢当、不畏强权；若不能善用，则为偏激、暴烈、好斗。
  
  文中强调"喜印化煞，财旺身旺为福"，说明要把天元坐煞导向正面，必须同时兼顾身弱身强与煞之轻重：身旺且有印、比劫，则七煞可被化为权力；身弱而煞重，又缺乏印比支撑，则煞气反过来损身、伤体。伤官合制煞，在此类格局中多与武职相连，既有战斗、执行之象，也带一定伤残风险，因此仍需结合大运流年谨慎权衡。

- 校勘与字词辨析：
  - 文中所举"甲申、乙酉等日"只是例举，余干如丙午、丁巳等自坐七煞之日，可仿此推论。
  - "侏儒跛鳖，骈指瘤赘"等语是古书常见对身体缺陷的形容，现代整理时保留原文，并在白话中以"身体残疾"概括之。
  - **English**：
    - Summarized in vernacular as physical disability.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_048]` `[trigger: 天元坐煞]` `[factor_trigger: tianyuan_zuosha_presence]` `[role: 主干]` 谓甲申、乙酉等日。乙丑日，丑中自坐辛金为煞。 → 《三命通会》卷五#天元坐煞
  - `[ns_smth_05_049]` `[trigger: 春夏喜秋冬忌]` `[factor_trigger: jijie_yingxiang_score AND mu_wang_jin_shuai]` `[role: 主干依赖]` 喜生春夏，乙木健旺，煞自有制；生秋月雕零，坐下藏鬼，岂不为害？ → 《三命通会》卷五#天元坐煞
  - `[ns_smth_05_050]` `[trigger: 印化煞]` `[factor_trigger: yin_huasha_condition AND cai_wang_shen_wang]` `[role: 条件分支]` 喜印化煞，财旺身旺为福。 → 《三命通会》卷五#天元坐煞
  - `[ns_smth_05_051]` `[trigger: 合格武贵]` `[factor_trigger: hege_wugui AND shang_guan_he_zhi]` `[role: 总结]` 如煞旺，有伤官合制，亦贵。合格为武贵。 → 《三命通会》卷五#天元坐煞"""
    normalized_text_zh: str = """"""
    subject: str = "日元自坐七煞之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tianyuan_zuosha_presence', 'bazi_semantic', 'zuosha_config', 'bazi_semantic', 'yusha_nengli_score', 'bazi_semantic', 'jijie_yingxiang_score', 'bazi_semantic', 'yin_huasha_condition', 'bazi_semantic', 'shenruo_shazhong_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_037', 'tianyuan_zuosha_presence', 'rel_smth_05_038', 'yusha_nengli_score', 'rel_smth_05_039', 'shenruo_shazhong_risk', 'evi_smth_05_037', 'yusha_nengli_score', 'rule_yusha', 'evi_smth_05_038', 'jijie_yingxiang_score', 'rule_jijie', 'evi_smth_05_039', 'tianyuan_zuosha_presence', 'rule_wugui', 'map_smth_05_025', 'map_smth_05_026']
    
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
        l1_anchor="smth_v1.0.0_日元自坐七煞之象_001_L1",
    )
    version: str = "1.0.0"
