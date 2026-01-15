"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755590
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
    semantic_id="zw_v1.0.0_谭星要论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 谭星要论(SemanticEntry):
    """
    - 分字分词释义：

  - **身命禄马**：身宫、命宫与禄存、天马的综合格局。
  - **空亡**：天空、截空、旬空等虚耗之位。
  - **命主**：由命宫地支决定的主星。
  - **身主*...
    """
    
    original_text: str = """- 分字分词释义：

  - **身命禄马**：身宫、命宫与禄存、天马的综合格局。
  - **空亡**：天空、截空、旬空等虚耗之位。
  - **命主**：由命宫地支决定的主星。
  - **身主**：由生年地支决定的主星。
  - **八座**：身命、迁移、财帛、官禄、福德六宫的架构。
  - **庙旺聚吉**：星曜入庙旺地且吉星聚集。
  - **化吉化忌**：四化星的吉凶转化。
  - **刑冲克破**：宫位间的刑冲与星曜间的克破关系。
  - **禄元相守**：天干禄星守护命身，可挽救陷地凶杀。
  - **正曜**：紫微、天府等主要尊星。
  - **僧之命**：父母妻子三宫多劫空杀忌的出家命格。
  - **二姓延生**：过继或赘婿以延续血脉家业。
  - **六畜之命**：极端贫贱的最低等命格。

- 原文（断句）：

  先看身命禄马，不落空亡，天空、截空最紧，旬空次之。第一看命主吉凶庙旺化吉化忌生克；次看身主吉凶生克，三看迁移、财帛、官禄三方星辰刑冲克破；四看福德宫权禄劫空庙陷，以福德对财帛宫也。身命迁移、财官福德六宫，名曰八座，俱在庙旺聚吉化吉，富贵高寿；六宫俱陷聚凶化忌，夭寿贫孤，若卯酉时生人者尤紧。外有田宅疾厄，已录于后。又看父母妻子三宫俱有劫空杀忌，则僧之命，否则孤独贫穷。若命宫无正曜者，财官二宫有吉星拱照，富贵全美；或偏房庶母所生，三方有恶星冲照，或二姓可延生离祖，可保成家。如命官有正曜吉星庙旺化吉，三方又有吉宿会合，上上之命；如无正曜吉星，三方有吉，上次之命。命宫星辰无吉无凶，或吉凶相半者，如三方亦有中等星辰，为中格。及命宫星辰入庙旺，三方有恶星守照破格，及命星陷背加羊火化忌，却得十干禄元来相守化吉，亦为中等之命。若命无吉星，反有凶杀化忌，无禄落陷，为下格之命。三方有吉星，亦可为中等，先小后大，不能久远，终为成败夭折论。若安命星缠陷地，又加凶杀化忌，三方又会羊陀火铃空劫，为下格，贫贱二姓延生奴仆之命，否则夭拆六畜之命。

- 规范化释义（primary_lang_explained）：

  断命首先要看身命与禄马，不可落入空亡，其中以天空、截空最为关键，旬空次之。第一步先看命主之星的吉凶与庙旺、落陷，以及其化吉、化忌与生克关系；第二步看身主之星的吉凶生克；第三步考察迁移、财帛、官禄三宫的星曜是否刑冲克破；第四步则看福德宫的权星、禄星、劫空与庙旺落陷，因为福德与财帛成对宫呼应。身命、迁移、财官、福德这六宫合称「八座」（连同命主、身主所依），若都在庙旺之地，吉星聚会、化吉明显，则主富贵高寿；若六宫俱陷，凶星聚集、化忌繁多，则多主夭寿贫孤，尤其对于卯、酉时生人更为紧要。田宅、疾厄等宫位的分论在后文另录。

  此外，还须看父母、妻子三宫：若三宫皆见劫空、杀忌，则多为僧道命；否则多是孤独贫穷的格局。若命宫无正曜，却有财帛与官禄二宫吉星拱照，则仍可富贵全美；若为偏房庶出，则多见三方恶星冲照，需凭二姓过继、离祖另立才能成家。若命宫有正曜吉星居庙旺地并化吉，三方又有吉宿会合，则为上上之命；若命宫无正曜吉星，而三方吉星得位，则为次一等。命宫星辰若无明显吉凶，或吉凶相半，而三方也是中等星曜相应，则为中格。

  若命宫星辰入庙旺而本身不错，却因三方有恶星守照、破坏格局，或命主落陷又加羊刃、火星、化忌，但同时得到天干禄元来相守、化吉，则整体仍可归为中等之命。若命宫全无吉星而尽是凶杀、化忌，又无禄星、落入陷地，则为下格之命；若三方尚有吉星可扶，则仍能视作中等，只是多半先小后大，福祸更替，终究难以长久，多有成败与夭折之虞。若安命之星缠于陷地，又加凶杀、化忌，三方再会羊陀、火铃、空劫等恶曜，则为下格之下，主贫贱、二姓延生、奴仆之命；若连此等延生之机亦无，则至多只应于六畜之命而已。

- 完整对等诠释（secondary_lang_full）：

  This opening essay lays out the basic road map for judging a Ziwei chart. It
  begins with the Life and Body palaces together with Salary and Horse,
  checking that they do not fall into voids, especially the harsher kinds of
  emptiness such as Tiankong and Jiekong. Then it moves through four steps:
  first assess the main star of the Life palace in dignity, debility and
  transformations; next examine the Body star; then inspect the three
  practical palaces of Travel, Wealth and Career for clashes and breaks; and
  finally weigh the Fortune palace, which stands opposite Wealth and answers
  it. Taken together, these six palaces form the "Eight Seats" framework:
  when they are mainly dignified and gather benefics and auspicious
  transformations, they can carry wealth, honour and long life; when they are
  mostly fallen and crowded with malefics and taboos, they tend toward
  poverty, isolation and early death.

  The text then turns to kinship and social position. Heavy voids and killing
  stars in the Parents and Spouse palaces point toward a monastic life or,
  failing that, a fate of loneliness and poverty. A Life palace without
  principal stars can still be lifted by strong Wealth and Career palaces,
  often through adoption, concubine lineage or leaving the ancestral home.
  When the Life palace holds principal benefics in full dignity, supported by
  three-directional benefics and auspicious transformations, the chart is
  judged top tier; when these supports are weaker or mixed, it falls to middle
  or lower ranks. At the extreme, a deeply fallen Life star entwined with
  malefics and voids and unsupported by salary roots is said to drop below the
  ordinary human range, suitable only for servant-like or symbolic "livestock"
  fates. The point is not to insult people, but to remind the reader that
  structural capacity sets hard limits long before minor omens are counted.

- 核心要点：

  1. 断命四步：先看命主，其次身主，再看迁移财官三宫，最后看福德与财帛对宫。
  2. 八座成局：身命、迁移、财官、福德六宫庙旺聚吉，则富贵高寿；六宫俱陷聚凶，则夭寿贫孤。
  3. 亲缘格局：父母、妻子三宫多劫空杀忌，多主僧道命；否则易成孤独贫穷之局。
  4. 格局分层：命宫正曜庙旺化吉且三方吉会为上上格；无正曜而三方吉为次；中等与下格由吉凶星多少与禄元相守与否决定。
  5. 败中有救：命陷加凶若仍得天干禄元化吉，可由下格拔回中格，但多先小后大，难以长久。
  6. 极端下格：命星陷地加凶杀空劫，连延生之机皆薄者，只足以应于「六畜之命」的极端贫贱格局。

- 叙事素材（narrative_snippets）：

  - **断命四步**："先看命主，次身主，再看迁移财官，最后福德财帛"，建立标准的看命流程。
  - **八座成局**："身命迁移财官福德六宫庙旺聚吉，则富贵高寿"，六宫俱佳为上格。
  - **亲缘格局**："父母妻子三宫多劫空杀忌，多主僧道命"，三亲宫凶主孤独。
  - **格局分层**："命宫正曜庙旺化吉且三方吉会为上上格"，上中下格的判定标准。
  - **败中有救**："命陷加凶若仍得天干禄元化吉，可由下格拔回中格"，凶中有救的转机。
  - **现代应用**：本条可作为命盘"总体评分"的框架——四步法+八座成局+格局分层。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j5_001]` `[trigger: 八座结构]` `[factor_trigger: structure_bazuo]` `[role: 主干]` 八座结构为身命迁移财帛官禄福德六宫的架构。 → 《卷五》入格总则
  - `[ns_zwds_j5_002]` `[trigger: 格局层次]` `[factor_trigger: level_geju]` `[role: 主干]` 格局层次为命盘上上格/中格/下格的分级评估。 → 《卷五》"上上格、中等、下格"
  - `[ns_zwds_j5_003]` `[trigger: 正曜庙旺]` `[factor_trigger: type_zhengyao AND state_miaowang]` `[role: 条件分支]` 正曜庙旺为主星处于庙旺之地的上等配置。 → 《卷五》
  - `[ns_zwds_j5_004]` `[trigger: 禄元相守]` `[factor_trigger: pattern_luyuanxiangshou]` `[role: 条件分支]` 禄元相守为禄星守命身的救应配置。 → 《卷五》"禄元化吉"
  - `[ns_zwds_j5_005]` `[trigger: 僧道命]` `[factor_trigger: pattern_sengzhiming]` `[role: 条件分支]` 僧道命为三亲宫劫空杀忌的出家命格。 → 《卷五》"僧道命"
  - `[ns_zwds_j5_006]` `[trigger: 命主身主]` `[factor_trigger: star_mingzhu AND star_shenzhu]` `[role: 主干]` 命主身主为命盘两大核心星曜。 → 《卷五》"先看命主，次身主"
  - `[ns_zwds_j5_007]` `[trigger: 天干四化]` `[factor_trigger: principle_tiangansihua]` `[role: 主干]` 天干四化为年干所化禄权科忌四星的体系。 → 《卷五》
  - `[ns_zwds_j5_008]` `[trigger: 格局结构]` `[factor_trigger: structure_geju]` `[role: 主干]` 格局结构为命盘整体星曜配置形成的格局。 → 《卷五》
  - `[ns_zwds_j5_009]` `[trigger: 大贵格局]` `[factor_trigger: result_dagui]` `[role: 结果]` 大贵格局为极品富贵的命格结果。 → 《卷五》
  - `[ns_zwds_j5_010]` `[trigger: 晚年结果]` `[factor_trigger: result_wannian]` `[role: 结果]` 晚年结果为命盘主晚年运势的判断。 → 《卷五》"""
    normalized_text_zh: str = """"""
    subject: str = "谭星要论"
    factor_refs: list = ['structure_shenmingluma', 'structure_bazuo', 'type_zhengyao', 'pattern_luyuanxiangshou', 'pattern_sengzhiming', 'pattern_erxingyansheng', 'source_ref', 'rel_tanxing_001', 'structure_bazuo', 'rel_tanxing_002', 'pattern_luyuanxiangshou', 'rel_tanxing_003', 'pattern_sengzhiming', 'evi_tanxing_001', 'structure_bazuo', 'rule_tanxing_bazuo', 'evi_tanxing_002', 'pattern_luyuanxiangshou', 'rule_tanxing_luyuan', 'concept_pattern_level', 'concept_rescue']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_谭星要论_001_L1",
    )
    version: str = "1.0.0"
