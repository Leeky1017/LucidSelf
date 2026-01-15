"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412454
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
    semantic_id="smth_v1.0.0_巳酉丑金局与福德秀气格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 巳酉丑金局与福德秀气格(SemanticEntry):
    """
    - **原文（source_text）**：

  此格专以巳酉丑金局而看所得天干，如乙巳、乙酉、乙丑三日，是乙用金为煞，喜印绶，喜制伏，不宜生六月逢未，以墓上带旺，金能克木，不宜生八月再露其煞，运行...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格专以巳酉丑金局而看所得天干，如乙巳、乙酉、乙丑三日，是乙用金为煞，喜印绶，喜制伏，不宜生六月逢未，以墓上带旺，金能克木，不宜生八月再露其煞，运行印绶官旺乡，便能发福。丁巳、丁酉、丁丑三日，是丁用壬为官，喜金旺生水，亦不喜生八月，以八月火死，功名蹭蹬，又不喜生十一月，以十一月癸水为煞为寿不耐，柱中喜见财官，旺位为贵，运行官旺，便可发福。己巳、己酉、己丑三日，是己用甲木为官，巳酉丑金局皆伤其官，亦名盗气，何以为吉？殊不知金能生水财，喜行财运便发，柱中不要见丙丁寅午戌，以伤金局及刑冲破害，又不喜生四月火旺，秀气浅薄，立身在晚，多成败孤克。癸巳、癸酉、癸丑三日，是用金神为印，见巳酉丑金局能生癸水，喜秋冬，亦不喜生四月，以水绝于巳，虽然金生在巳，以金生水亦不能绝，得官印运便能发福，只嫌火财伤金。辛巳、辛酉、辛丑三日，柱全金局为妙，若见午戌火旺有破，反生灾咎，若通丙火旺为正气官星，或值寅位为天乙贵人，俱吉。岁运同。古歌曰：阴木加临酉丑蛇，生居六月暗咨嗟，为官得禄难长久，纵有文章不足夸。又：乙巳乙酉并乙丑，八月生人人短寿，四柱若见火伤官，降官失职定然有。又：阴火相临巳酉丑，生居丑月寿难长，更兼名利多成败，破败荒淫不可当。又：丁巳丁酉并丁丑，八月生人人不久，前程名利两区区，更忌饮酒及交友。又：阴土逢蛇鸡与牛，名为福德号貔貅，秀气火来侵克破，须教名利一时休。又：己巳己酉及己丑，福德秀气造化有，大怕四柱火相侵，纵有功名不长久。又：阴金合局主前程，造化清奇大有情，四柱火来侵克破，须知名利两无成。又：西方金气坐阴柔，不怕休时不怕囚，鬼煞生时方发福，功名随步上瀛洲。又：癸巳癸酉月临风，百务迟延作事空，名利生成难有望，始知人在五行中。又：癸巳癸酉及癸丑，四月生人人不久，功名成败在晚年，最忌贪花并饮酒。

- 分字分词释义：

  - **巳酉丑金局**：指地支巳、酉、丑三支成局，主金气成势，为本格之结构基础。
  - **乙用金为煞，喜印绶制伏**：乙木日主见金为七煞，若有印绶制伏，则煞化为用，可成“有威有节”的贵格。
  - **丁用壬为官，喜金旺生水**：丁火以壬水为正官，金旺能生壬水，使官星有源，利于功名。
  - **己用甲为官，巳酉丑金局皆伤其官**：己土以甲木为官，金局能克木官，表面似凶，实则可借金生水为财而转化为财旺之象。
  - **癸以金神为印**：癸水日主，巳酉丑金局所生之水为印绶，护身养性，宜在秋冬金水旺地。
  - **辛巳辛酉辛丑柱全金局为妙**：辛金日主若四柱成全金局，金气纯粹，配合适当官星与贵人，则“造化清奇”。
  - **不喜四月、六月、八月等火旺、墓旺之时**：强调季节对金局的影响，火旺或墓旺之月会损金局秀气，影响寿命与功名稳定。

- **规范化释义（primary_lang_explained）**：

  福德秀气格，是围绕巳酉丑金局展开的一类组合格局，主要针对乙、丁、己、癸、辛等阴干日。总体思想是：在金局成势的前提下，通过“金生水、印制煞、财官有源”的方式，使命局呈现出一种既有福德、又有秀气的状态。

  具体而言，乙日见巳酉丑金局，是“以金为煞而喜印制煞”的结构，若生于适当时令、再有印绶制伏七煞，便能从“煞重伤身”转为“以煞为权”；丁日则以壬水为官，借金生水，使官星不绝其源；己日虽本以甲木为官，却因金局伤官而易成“盗气”，但若能借金生水成财，反而易在财运中得福；癸日以金为印，金局既成则印绶有力，秋冬尤佳；辛日若四柱成金局，则更重在“纯粹”与“清奇”的造化。

  原文多首歌诀不断提醒：此类格局一方面有“福德秀气”的潜力，另一方面又极惧火旺、时令不当以及过度贪恋酒色、交游不慎等现实因素——若火来破金，或命主自身行为偏激，则名利往往“成败频仍”，甚至有寿命不长之虞。

- 核心要点：

  - 本格以**巳酉丑金局成势**为前提，针对多种阴干日（乙、丁、己、癸、辛）分别论其用神与取舍。
  - 关键在于**金生水、印制煞、财官有源**，使煞化为权、官得其源、印能护身。
  - 季节与火气极为关键：火旺或墓旺之月多耗损金局秀气，易损寿与功名的持续性。
  - 行运上，宜印绶、官旺、财旺而不过火；忌火多破金、刑冲金局及纵酒色以自耗。

- 详细解说：

  福德秀气格可以视为一组“金局主导、阴干分途”的综合型格局。原文先按日干分成若干小类：乙日重在“煞印相生”、丁日重在“官星有源”、己日重在“化官为财”、癸日重在“印绶护身”、辛日重在“金局纯粹”。这些不同取向，共同构成了“福德秀气”的整体图像。

  实务中，应特别留意几个要点：

  1. 巳酉丑金局是否真成——若局不成，只能按一般金多之命论，不足以称“福德秀气”；
  2. 日主强弱与用神方向——乙、丁宜得印官，己宜得财，癸宜得印官，辛宜得适量火来成其器；
  3. 火气与时令的配合——火过旺则损金局秀气，火全无则金气过寒，皆非上选；
  4. 行为层面的约束——原文反复以歌诀警示“贪花饮酒”的风险，暗示此类命局往往有“外在条件不坏，但需慎行以保福”的特点。

- **校勘与字词辨析（双语）**：

  - 原文“巳酉丑金局皆伤其官，亦名盗气，何以为吉？殊不知金能生水财”一句，本稿在白话中作“化官为财”之解释，以顺应整体财官结构的思路。
  - 若干歌诀中“降官失职”等语，本稿保持原貌，仅在白话中将其理解为“官运反复、职名难久”。
  - “福德秀气”一语，本稿理解为“既有福德之象，又有文秀之气”，并在详细解说中以行为约束来呼应其“德”之维度。
  - **English**：
    - The sentence "Si-You-Chou metal formation all harm its official, also called stealing qi, why is it auspicious?" is explained in vernacular as "transforming official into wealth" to clarify the logic.
    - The term "fortune-virtue elegant-qi" is understood as "having both fortune-virtue imagery and refined elegance"; the detailed explanation uses behavioral constraints to echo the "virtue" dimension.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_081]` `[trigger: 福德秀气定义]` `[factor_trigger: fude_xiuqi_presence]` `[role: 主干]` 此格专以巳酉丑金局而看所得天干。 → 《三命通会》卷六#福德秀气
  - `[ns_smth_06_082]` `[trigger: 乙用金为煞]` `[factor_trigger: yi_yong_jin_wei_sha AND xi_yinshou]` `[role: 主干依赖]` 如乙巳、乙酉、乙丑三日，是乙用金为煞，喜印绶，喜制伏。 → 《三命通会》卷六#福德秀气
  - `[ns_smth_06_083]` `[trigger: 己化官为财]` `[factor_trigger: ji_hua_guan_wei_cai]` `[role: 条件分支]` 己用甲木为官，巳酉丑金局皆伤其官，亦名盗气，何以为吉？殊不知金能生水财，喜行财运便发。 → 《三命通会》卷六#福德秀气
  - `[ns_smth_06_084]` `[trigger: 阴土福德貔貅]` `[factor_trigger: yin_tu_fude_pixiu]` `[role: 总结]` 阴土逢蛇鸡与牛，名为福德号貔貅。 → 《三命通会》卷六#福德秀气"""
    normalized_text_zh: str = """"""
    subject: str = "巳酉丑金局与福德秀气格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_20', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_metal_degree', 'bazi_semantic', 'bazi_state_fire', 'bazi_semantic', 'bazi_condition_factor_157', 'bazi_semantic', 'bazi_condition_factor_158', 'bazi_semantic', 'source_ref', 'rel_smth_06_061', 'fude_xiuqi_presence', 'rel_smth_06_062', 'jinju_chengfou_xiuqi', 'rel_smth_06_063', 'xingchong_pohai_risk', 'evi_smth_06_061', 'fude_xiuqi_presence', 'rule_fude', 'evi_smth_06_062', 'huoqi_peihe_shidu', 'rule_huojin', 'evi_smth_06_063', 'xingchong_pohai_risk', 'rule_chonghai', 'map_smth_06_041', 'map_smth_06_042']
    
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
        l1_anchor="smth_v1.0.0_巳酉丑金局与福德秀气格_001_L1",
    )
    version: str = "1.0.0"
