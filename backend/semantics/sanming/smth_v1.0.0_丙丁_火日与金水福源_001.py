"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288714
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
    semantic_id="smth_v1.0.0_丙丁_火日与金水福源_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙丁火日与金水福源(SemanticEntry):
    """
    - **原文（source_text）**：
  丙火属阳，乃太阳之正气，能生万物。喜生春夏月间，自然成就精神百倍，更遇天月二德，行东方运，大妙，虽见壬癸水，不妨，惟忌戊土透露，减其分数。大运、岁君相...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙火属阳，乃太阳之正气，能生万物。喜生春夏月间，自然成就精神百倍，更遇天月二德，行东方运，大妙，虽见壬癸水，不妨，惟忌戊土透露，减其分数。大运、岁君相犯，官府刑狱，破财丧服。生于秋冬，更遇夜时，地支再合水局，非仆即从，一生离别孤独，贫夭残疾。丁火属阴，为凡火，可制万物；金银铜铁，不得丁制，不能成器。喜生夜分，巳酉丑月令为妙，正月逢寅，乃天德印元，更得卯字最好。忌壬癸水，如日主生旺，多克妻子，遇南方运，剥官退职，行西北方运，则多见其贵。丙丁日主，火为根，金水二星是福源：行运若临西与北，纵然富贵不周全。丙丁日，自坐申子辰亥水位，又引归金时，如生寅午巳月，为水火既济，大贵。夏五月，忌三合火局，火炎水干；冬子月，忌三合水局，水盛火灭，水火相停，斯成既济。大运宜金水分野，却忌过与不及：偏阴偏阳，则苗而不秀。若生申子辰亥月，须要寅午戌巳时取贵，非此时者，行木运方好，否则虚名不贵。六丙日用庚辛为财，癸为正官，壬为偏官。若年月时中透出庚辛癸字，生秋冬金水局中，财官有用；如不透此三字，生秋冬金水局中，亦作财官论。见丙丁夺财，已为伤官，名利艰难。若生九夏四季火土局中，纵有财官，无气，虽得滋助，亦轻。喜行西北金水分野，向官临财之运。若柱中壬癸俱见，官煞混杂，无制反贱；如有壬无癸，不见制，当作鬼论。要分身鬼强弱，定其吉凶寿夭：制伏得中，作偏官用；太过，反不为福。更详日干于所生月内，有力无力、有救无救，分节气轻重言之，喜行身旺鬼衰之运，忌行身衰鬼旺之乡。六丁日用庚辛为财，壬为正官，癸为偏官。若年月时中透出庚辛壬字，生秋冬金水局中，财官有用，如不透此三字，生秋冬金水局，亦作财官论。见丙丁夺财，戊为伤官，名利艰辛。若生九夏四季火土局中，纵有财官，无气，虽得滋助，亦轻。喜行西北及金水分野，忌伤官败财之运。怕官煞混杂，有煞无制，鬼论；制太过则贫。更详日干于所生月内，有无力助，分轻重言之，运喜忌同上。

- 分字分词释义：
  - **火为根，金水为福源**：丙丁日主以火为体，以金水为用，金能制器、水能济火，皆为福之根源。
  - **水火既济**：水火相停、不相覆没之局，既不至火炎水干，也不致水盛火灭，为上等平衡状态。
  - **偏阴偏阳、苗而不秀**：五行与阴阳失于平衡，虽有格局之名，却难以真正发荣结果。
  - **官煞混杂**：壬癸并见且无制伏时，官煞不分，主名利反覆、是非相缠。

- 规范化释义（primary_lang_explained）：
  本段总论丙丁火日主在不同节令与行运分野中的吉凶消长。丙火如太阳，宜生于春夏得时得令，更逢天月二德与东方木火之运，精神百倍、富贵可期，即便透出壬癸水，只要不过度，反能成既济之局；惟独忌戊土到处透出，反泄丙火之力。若生于秋冬，又逢夜生、水局成势，则火势衰弱，多主从性或卑下孤寒。丁火为凡火，重在「制器」，金银铜铁皆赖丁制而成器：宜夜生，尤喜巳酉丑月令，有印有禄；正月逢寅为天德印元，再得卯字，则印绶俱足。丁火最忌壬癸强水，不仅有克火之凶，亦多有克妻之象：运入南方火地，易有剥官退职、名位受损；反而行西北金水之运，多有贵显之机。综之，丙丁日主以火为根，而金水为主要福源：西北金水之运，有助于调剂火炎，成就既济之美；但若金水太盛则火被熄灭，太弱则火炎土燥，皆属「偏阴偏阳，苗而不秀」。丙丁生于寅午巳月而坐水地者，若能在行运中引归金局，使水火既济，则为上格；反之，若火局过旺又再逢火运，或水局太重仍行水乡，则多有早夭、贫薄、孤寡之忧。六丙、六丁用神，大体皆以庚辛为财，壬癸为官，宜在秋冬金水局透出方可为用；若反见丙丁比劫夺财、戊己伤官无制，则名利艰难，纵有财官之名，终多无气。


- **完整对等诠释（secondary_lang_full）**：
  Here the text treats Bing and Ding as two faces of fire. Bing is the great, open flame of the sun, best when it rises in spring and summer and has real seasonal strength. In such charts, if Heavenly Virtue and Monthly Virtue assist and the person walks fortunes through the eastern wood–fire regions, spirit and visibility are high and honour is attainable; moderate Ren and Gui water can even help produce a balanced "water–fire in harmony" pattern. What Bing truly fears is being endlessly drained by exposed Wu earth: too much earth turns bright fire into a smouldering burden and often coincides with lawsuits, losses and official trouble when transits clash.
  Ding is the focused, man‑made fire of hearths and forges. It is described as the fire that actually tempers metal: gold, silver and iron are useless without Ding to refine them. Ding does best when born at night and in Si, You and Chou months where it has both seal and salary; Yin in the first month is called the root of Heavenly Virtue, and adding Mao further strengthens the seal. Strong, uncontrolled Ren and Gui, by contrast, easily overwhelm Ding, extinguish its light and show up as harm to spouse or position, especially when combined with southern fire fortunes that burn without structure. For both Bing and Ding, fire is the body but metal and water are the main sources of blessing: western–northwestern metal–water fortunes cool what is too hot, give shape and channels to action, and help transform raw enthusiasm into lasting offices and resources. If metal–water is entirely absent, summer fire becomes scorching and destructive; if metal–water is excessive with no root fire, the person may be clever and restless but unable to sustain output. The six Bing and six Ding days are therefore judged by whether fire has a real root, whether metal and water can moderate it without smothering it, and whether wealth and office stars appear with qi and appropriate control.

- 核心要点：
  - 丙丁火日的关键在于「火为根、金水为福源」：需凭金制与水济来成器与发用，忌火土过旺或水金过重而失衡。
  - 「既济」之局重在水火相停：夏火需水来济，冬水需火来温，过与不及都破坏了原文所推崇的中道之美。
  - 六丙六丁日的官财用法，本质是在判断财官是否「有气且有制」：金水得令而不过度、壬癸有制而不乱，方能真正转为贵格。

- 应用推演（操作顺序）：
  1) 判盘时先以节令与日主位置评估火根强弱：春夏得令且有根者视为火体充足，秋冬夜生且坐水地者视为火体偏弱或随从。
  2) 其次评估金水配置：看庚辛、壬癸的数量与位置，是「成器与既济」还是「官煞混杂、水火相倾」，并据此给出初步格局标签。
  3) 再结合六丙六丁官财用神原则，判断当前财官是否在有气之地，是否得到适度制伏，将「财官有用/无用」「官煞混/不混」编码为可计算特征。
  4) 在行运模拟中，将西北金水分野标记为「调剂火势、开财启官」的优选区域，同时根据原局火根强弱控制其上限，防止水太盛或金太重反伤火体。

- 反例与边界：
  - 不宜把一切丙丁日主都视作「火旺必贵」，忽略秋冬夜生、水局过盛导致火体微弱甚至从格的情况。
  - 不可简单以「见水必凶」来判断丁火命，原文明确指出在适度金水调济下反为贵格，关键在量与节制。
  - 工程上若只用「火旺=正向标签」「见官杀=升档」之类粗糙规则，既违背丙丁对金水平衡的精细要求，也会使大量偏阴偏阳格局被误判。
  - 反向误区是过度强调从格与既济，一见火弱就硬判从水或从金，而不看实际是否构成严格从局与行运配合。

- 小例（示意）：
  - 某丙日生于巳月，日坐子水，柱中庚辛透出而壬水适度，行运西北金水，系统可将其识别为「水火既济、金水为福源」的格局：既有执行力与光照度，又能在冷静评估与规则约束下发挥作用，适合在技术与管理结合的岗位上发展。
  - 另一命局丁日生于冬月，日坐亥水，柱中壬癸重叠而无火根，行运仍频入北方水乡，系统则标记为「水盛火灭」：虽有思维敏捷与感知力，却难以持续输出与担当，建议在现实中刻意引入「火性活动」（如创造、表达、领导）以及稳定制度来补强。"""
    normalized_text_zh: str = """"""
    subject: str = "丙丁：火日与金水福源"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'water_fire_harmony_state', 'bazi_semantic', 'metal_water_fortune_config', 'bazi_semantic', 'extreme_yin_yang_imbalance', 'bazi_semantic', 'wu_earth_drains_fire', 'bazi_semantic', 'official_killing_mixed_risk', 'bazi_semantic', 'northwest_metal_water_luck', 'bazi_semantic', 'commanding_season_label', 'bazi_semantic', 'source_ref', 'rel_smth_04_004', 'water_fire_harmony_state', 'rel_smth_04_005', 'extreme_yin_yang_imbalance', 'rel_smth_04_006', 'wu_earth_drains_fire', 'evi_smth_04_004', 'metal_water_fortune_config', 'rule_fire_root_fortune', 'evi_smth_04_005', 'water_fire_harmony_state', 'rule_water_fire_harmony', 'evi_smth_04_006', 'extreme_yin_yang_imbalance', 'rule_extreme_imbalance', 'map_smth_04_003', 'map_smth_04_004']
    
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
        l1_anchor="smth_v1.0.0_丙丁_火日与金水福源_001_L1",
    )
    version: str = "1.0.0"
