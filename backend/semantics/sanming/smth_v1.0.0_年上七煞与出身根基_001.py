"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458344
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
    semantic_id="smth_v1.0.0_年上七煞与出身根基_001",
    book_id="sanming",
    engine_id="bazi"
)
class 年上七煞与出身根基(SemanticEntry):
    """
    - **原文（source_text）**：
  经云：年逢贵气，不用制伏，喜日主健旺，羊刃相合，柱中带财，更行财运，发福清秀。最忌身衰，盖七煞乃小人之象，既居祖宗之位，如朝廷老臣，祖父老仆。日主健旺...
    """
    
    original_text: str = """- **原文（source_text）**：
  经云：年逢贵气，不用制伏，喜日主健旺，羊刃相合，柱中带财，更行财运，发福清秀。最忌身衰，盖七煞乃小人之象，既居祖宗之位，如朝廷老臣，祖父老仆。日主健旺，老仆则尽力以事幼主；日主衰弱，不能与小人为主，何肯尽力事之？反成害已之物。年干见此，必主出身寒微，四柱行运有情，主寒门生贵子。若煞旺身衰，冲刑太过，必主贫穷，至重者带孝遭刑。
  
  又曰：岁煞一位，不宜制；四柱重见，却宜制。日主生旺，制伏略多，喜行煞旺地。制伏太过，或煞旺身衰，官煞混杂，岁运如之，碌碌之辈。若制伏不及，运至身衰煞旺乡，必生祸患。一命戊戌、庚申、壬午、癸卯：戊与癸合，卯与戌合，壬坐午支，财官俱备，为贵。古歌云：岁德壬来见戌年，财旺身强禄自然，更得运行财旺地，为人聪慧又忠贤。又云：年干七煞莫言凶，制合为权最有功；若得身强无忌破，此身多入禁庭中。又云：岁伤日干不和同，须要干支制伏重；煞旺喜行身旺地，初年难免一场凶。

- 分字分词释义：
  - **年上七煞**：年干为日主之七煞，居年柱，为祖上、出身环境及早年缘分中的煞象。
  - **年逢贵气**：年干七煞同时兼带贵人或禄位之气，若日主健旺，则煞可为权。
  - **羊刃相合**：年干七煞得日主羊刃相合，一方面增强煞势，一方面也为煞提供着力点。
  - **寒门生贵子**：出身虽寒微，但因官煞、财星、身旺配合得宜，反能在后天行运中发贵。
  - **岁煞一位，不宜制**：年柱只一位七煞时，原局不宜过分制伏，以免损伤可用之权力。
  - **四柱重见，却宜制**：若官煞在四柱多见，则须以食伤、印绶等适度制伏，以防煞多为殃。

- **规范化释义（primary_lang_explained）**：
  本节专论年干为七煞的情形。年柱代表祖上根基、出身背景与早年环境，当七煞居年干时，若同时带有贵气与财星，且日主健旺，则不必急于制伏，反可视作老成之臣、祖父老仆为幼主效劳，主寒门生贵子、以权煞之力而发福清秀。若日主衰弱，反为小人反客为主，轻则贫困、重则带孝遭刑。
  
  文中区分"岁煞一位"与"四柱重见"：若只一位年煞，则以不重制为宜，在行运中以身旺、财旺、印旺来承煞成权；若官煞在四柱重重出现，则必须以食神、伤官、印绶等制伏有度，否则煞旺身衰、冲刑太过，多成碌碌之辈，甚至有刑伤之祸。所举戊戌、庚申、壬午、癸卯之命，以合化与财官俱备为例，说明年上七煞若得身强、合制有情，反能入"禁庭"掌权。

- **完整对等诠释（secondary_lang_full）**：
  A saying runs: 'When the year meets noble Killing, there is no need to rush to suppress it; what is welcomed is a strong day-master, a Yang Blade in harmonious combination and wealth present in the pillars, with fortune cycles further entering wealth lands—then blessings arise in a pure and elegant way.' Year-top Seven Killing stands in the ancestral position, like an old minister or long‑serving retainer of the family. If the day-master is strong, such a 'servant' will do his utmost for the young master; if the day-master is weak and cannot truly be the master over such people, why would they devote themselves wholeheartedly? In that case the same force turns into something that harms rather than helps. Thus a single noble Seven Killing on the year stem, supported by body, wealth and Seal, can mark someone born humble who rises to high office, whereas heavy Killing with a weak body more often points to poverty and even criminal punishment.


- 核心要点：
  - 年上七煞主**出身、祖上与早年环境中的权煞力量**，身强则可用，身弱则为祸。
  - 一位岁煞不宜乱制，宜靠身旺、财印之助化其为权；官煞重重则须制伏，否则煞多为殃。
  - 行运关键在于"身衰煞旺乡"是否再被激发：若原局已煞重身弱，遇此运多有灾难。

- 详细解说：
  年柱位置在命局中具有“源头”性质：既代表祖宗、父祖之气，也代表命主的出身门第与早年环境。七煞若坐于年干，一方面意味着命主从一开始便生于竞争、压力或权力关系复杂的环境；另一方面也可能意味着有"老臣"般的强力人物在命局中长期施加影响。
  
  文中用"老仆"比喻七煞，揭示了一个关键：身旺者能御煞，则小人、强臣为我所用；身弱者反被其制，则小人反客为主，成为祸患之源。因此，年上七煞宜配合羊刃、财星、印绶，使日主有足够力量承煞、用煞；若单有七煞而无身、无印、无比，则多主贫困、刑伤。
  
  对于行运，原文强调：一位岁煞不必急制，惟恐制之太过反失其用；而四柱官煞重重则须制伏，否则煞重身轻，难以胜任。古歌中"年干七煞莫言凶，制合为权最有功"，即是告诫：七煞不必视作绝对凶星，而应看其与身、财、印之间的制化关系。

- 校勘与字词辨析：
  - "年逢贵气，不用制伏"之"不用"，并非全然不制，而是不宜过度、过早制煞，宜以合化、身旺承煞为主。
  - "带孝遭刑"指因丧事、刑狱等严重之灾而同时临身，并非仅指穿孝服本身。
  - **English**：
    - Both appearing together; not just literally wearing mourning clothes.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_060]` `[trigger: 老仆事幼主]` `[factor_trigger: laopu_youzhu_score AND shen_qiang]` `[role: 主干]` 日主健旺，老仆则尽力以事幼主；日主衰弱，不能与小人为主，何肯尽力事之？ → 《三命通会》卷五#年上七煞
  - `[ns_smth_05_061]` `[trigger: 岁煞制伏]` `[factor_trigger: yiwei_duowei_diff]` `[role: 主干依赖]` 岁煞一位，不宜制；四柱重见，却宜制。 → 《三命通会》卷五#年上七煞
  - `[ns_smth_05_062]` `[trigger: 寒门生贵]` `[factor_trigger: hanmen_shenggui AND si_zhu_you_qing]` `[role: 条件分支]` 四柱行运有情，主寒门生贵子。 → 《三命通会》卷五#年上七煞
  - `[ns_smth_05_063]` `[trigger: 制合为权]` `[factor_trigger: zhi_he_wei_quan]` `[role: 总结]` 年干七煞莫言凶，制合为权最有功。 → 《三命通会》卷五#年上七煞"""
    normalized_text_zh: str = """"""
    subject: str = "年上七煞与出身根基"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'nianshang_qisha_presence', 'bazi_semantic', 'chushen_genji_config', 'bazi_semantic', 'laopu_youzhu_score', 'bazi_semantic', 'yiwei_duowei_diff', 'bazi_semantic', 'hanmen_shenggui', 'bazi_semantic', 'daixiao_zaoxing_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_046', 'nianshang_qisha_presence', 'rel_smth_05_047', 'laopu_youzhu_score', 'rel_smth_05_048', 'daixiao_zaoxing_risk', 'evi_smth_05_046', 'chushen_genji_config', 'rule_chushen', 'evi_smth_05_047', 'laopu_youzhu_score', 'rule_yusha', 'evi_smth_05_048', 'hanmen_shenggui', 'rule_shenggui', 'map_smth_05_031', 'map_smth_05_032']
    
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
        l1_anchor="smth_v1.0.0_年上七煞与出身根基_001_L1",
    )
    version: str = "1.0.0"
