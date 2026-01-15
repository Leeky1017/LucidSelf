"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558670
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
    semantic_id="yhzp_v1.0.0_论五行生克制化__各有所喜所害例_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论五行生克制化各有所喜所害例(SemanticEntry):
    """
    - **原文（source_text）**：  
  金旺得火，方成器皿；火旺得水，方成相济；水旺得土，方成池沼；土旺得木，方能疏通；木旺得金，方成栋梁。  
  
  金赖土生，土多金埋；土赖火生，...
    """
    
    original_text: str = """- **原文（source_text）**：  
  金旺得火，方成器皿；火旺得水，方成相济；水旺得土，方成池沼；土旺得木，方能疏通；木旺得金，方成栋梁。  
  
  金赖土生，土多金埋；土赖火生，火多土焦；火赖木生，木多火炽；木赖水生，水多木漂；水赖金生，金多水浊。  
  
  金能生水，水多金沉；水能生木，木盛水缩；木能生火，火多木焚；火能生土，土多火埋；土能生金，金多土变。  
  
  金能克木，木坚金缺；木能克土，土重木折；土能克水，水多土流；水能克火，火多水热；火能克金，金多火熄。  
  
  金衰遇火，必见销镕；火弱逢水，必为熄灭；水弱逢土，必为淤塞；土衰遇木，必遭倾陷；木弱逢金，必为砍折。  
  
  强金得水，方挫其锋；强水得木，方泄其势；强木得火，方化其顽；强火得土，方止其焰；强土得金，方制其害。

- **分字分词释义**：
  - **旺**：五行力量强盛，处于得令有根的状态。
  - **赖**：依赖、依靠，指五行之间的相生关系。
  - **器皿**：比喻经过淬炼而成的有用之物，金得火炼方能成器。
  - **相济**：相互调节、平衡，火旺得水克则不过燥。
  - **池沼**：蓄水之地，水旺得土围则不泛滥。
  - **疏通**：疏导畅通，土旺得木疏则不板结。
  - **栋梁**：房屋的主梁，比喻有用之材，木得金修剪方成材。
  - **埋/焦/炽/漂/浊**：五行过旺反而被生者所累的五种状态。
  - **沉/缩/焚/埋/变**：生者被泄过度而衰弱的五种状态。
  - **缺/折/流/热/熄**：克者遇强被反克的五种状态。
  - **销镕/熄灭/淤塞/倾陷/砍折**：弱者遇克必败的五种状态。
  - **挫锋/泄势/化顽/止焰/制害**：强者得泄得克反而平衡的五种状态。

- **规范化释义（primary_lang_explained）**：  
  这六段歌诀系统阐述五行生克制化的辩证关系，揭示"旺者宜克宜泄，弱者忌克忌泄"的核心法则。第一段讲"旺者宜制"：金木水火土五行各自旺盛时，需要克制或调节才能发挥正面作用，否则过旺成害。第二段讲"生多为累"：五行虽然依赖相生，但生者过多反而被埋、被焦、被炽等，适得其反。第三段讲"泄多为耗"：五行虽能生养他物，但被泄过度则自身衰弱，如水多金沉、火多木焚等。第四段讲"克者遇强反伤"：克制关系并非绝对，若被克者过强，反而会伤害克者，如木坚金缺、火多水热等。第五段讲"弱者遇克必败"：五行本身衰弱时，再遇克制则彻底败坏，如金衰遇火必销镕、木弱逢金必砍折等。第六段讲"强者宜泄宜制"：五行过强时，得克得泄反而能平衡其力量，化害为利。整体来看，这六段形成完整的五行平衡理论：五行不宜过旺，不宜过衰，需要在生克制化中达到中和状态，方为吉命。

- **完整对等诠释（secondary_lang_full）**：  
  These six verses systematically expound the dialectical relationships of Five Elements' generation, control, transformation, and balancing, revealing the core principle: "The strong should be controlled or drained; the weak should avoid being controlled or drained." The first verse teaches "the prosperous need regulation": when Metal, Wood, Water, Fire, or Earth are each at peak strength, they require restraint or adjustment to manifest positive effects—otherwise excess becomes harm. The second verse explains "excessive generation becomes burden": though elements rely on being generated, too much generation paradoxically buries, scorches, blazes, floats away, or muddies the receiver. The third verse shows "excessive draining depletes": though elements can nourish others, over-draining weakens the giver—as in "water abundance sinks metal" or "fire abundance burns wood." The fourth verse reveals "controllers meeting strength suffer reverse injury": control relationships are not absolute; when the controlled party is overly strong, it harms the controller—as in "firm wood chips metal" or "abundant fire evaporates water." The fifth verse warns "the weak meeting control face certain defeat": when an element is already feeble and then encounters its controller, complete ruin ensues—as in "weak metal meeting fire melts entirely" or "weak wood meeting metal gets chopped down." The sixth verse teaches "the strong benefit from draining and control": when an element is excessive, being controlled or drained paradoxically balances its force and transforms harm into benefit. Taken together, these six verses form a complete theory of Five-Element equilibrium: elements should be neither excessively prosperous nor excessively weak, but must achieve a harmonious state through generation, control, transformation, and balancing—only then manifesting auspicious fate.

- **核心要点**：
  - 旺者宜制：五行过旺需要克制或泄耗，否则成害
  - 生多为累：相生过度反而成为负担，如土多金埋
  - 泄多为耗：被泄过度则自身衰弱，如水多金沉
  - 克者遇强反伤：被克者过强会反克克者，如木坚金缺
  - 弱者遇克必败：本身衰弱再遇克制则彻底败坏
  - 强者宜泄：过强得泄得克反而能平衡，化害为利

- **详细解说**：  
  这六段歌诀是子平命理中五行理论的精髓，体现了"物极必反、过犹不及"的辩证思想。传统命理常说"身旺为吉、身弱为凶"，但这是简化的说法。真实情况是：过旺过弱皆非吉，唯有中和方为美。这六段歌诀从不同角度阐述这一原理。第一段"金旺得火方成器皿"等，强调旺者需要制约，才能"成器"。金属原矿虽多，不经火炼不成器皿；木材虽旺，不经金砍不成栋梁。这是"旺而有制"的吉象。第二段"金赖土生，土多金埋"等，揭示生扶也有度。命局中若财星生官星，本为吉象；但财星过多，反而埋没官星，此即"土多金埋"之理。第三段"金能生水，水多金沉"等，说明被泄过度的危害。日主虽能生食伤，但食伤过旺则盗泄日主之气，使日主衰弱，此即"水多金沉"之理。第四段"金能克木，木坚金缺"等，最能体现五行力量的对比性。克制关系不是机械的，而是要看双方力量对比。若木极旺而金衰，则金不仅克不了木，反被木的坚硬所伤，此即"木坚金缺"。第五段"金衰遇火必见销镕"等，是针对弱者的警示。命局中若日主本已衰弱，再行克制之运，必然凶险，如金弱行火运、木弱行金运等。第六段"强金得水方挫其锋"等，则指出强者的化解之道。日主过旺并非绝对吉利，需要泄耗或制约来平衡。如金日主过强，得水泄秀或火炼制，反而能化顽为美，成就贵格。

- **校勘与字词辨析**：
  - **方成器皿**："方"作副词，表示"才能"之意，非方向之"方"。
  - **土多土变**：底本作"土多土变"，部分版本作"金多土弱"。"土变"可理解为土性改变；"土弱"则直指土被金泄而衰弱。本次据底本作"土变"。
  - **火多水热**：字面看似矛盾，实则指水克火但火过旺时，水反被蒸腾、沸腾，失去克制之功，与"克者遇强反伤"主旨相符。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_016]` `[trigger: 五行旺衰]` `[factor_trigger: five_element_generation]` `[role: 主干]` 五行生克制化形成动态平衡系统，旺者需制、弱者需扶。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_017]` `[trigger: 旺者宜制]` `[factor_trigger: five_element_control]` `[role: 条件分支]` 金旺得火方成器皿，五行过旺需要克制才能发挥正面作用。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_018]` `[trigger: 生多为累]` `[factor_trigger: five_element_generation]` `[role: 条件分支]` 土多金埋，相生过度反而成为负担，被生者反而受累。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_019]` `[trigger: 泄多为耗]` `[factor_trigger: five_element_generation]` `[role: 条件分支]` 水多金沉，被泄过度则自身衰弱，生者反而损耗。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_020]` `[trigger: 克者遇强反伤]` `[factor_trigger: five_element_control AND fanke_xianxiang]` `[role: 条件分支]` 木坚金缺，被克者过强会反克克者，克制关系并非绝对。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_021]` `[trigger: 弱者遇克必败]` `[factor_trigger: five_element_control]` `[role: 条件分支]` 金衰遇火必见销镕，本身衰弱再遇克制则彻底败坏。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_022]` `[trigger: 强者宜泄]` `[factor_trigger: five_element_generation]` `[role: 条件分支]` 强金得水方挫其锋，五行过强时得克得泄反而能平衡。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_023]` `[trigger: 中和为贵]` `[factor_trigger: ]` `[role: 总结]` 五行不宜过旺不宜过衰，需在生克制化中达到中和状态方为吉命。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_349]` `[trigger: 金]` `[factor_trigger: metal]` `[role: 主干]` 金为西方之气，主义主肺。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_350]` `[trigger: 月令]` `[factor_trigger: month_order]` `[role: 主干]` 月令为四柱提纲，主一生格局。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_351]` `[trigger: 母]` `[factor_trigger: mother]` `[role: 主干]` 正印为母星，年支为母宫。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_352]` `[trigger: 贵人]` `[factor_trigger: noble AND combine_noble_promiscuity]` `[role: 条件分支]` 天乙贵人临命主贵人相助。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_353]` `[trigger: 正官]` `[factor_trigger: official]` `[role: 条件分支]` 正官为克我之神，主权威、地位。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_354]` `[trigger: 格局]` `[factor_trigger: pattern]` `[role: 主干]` 格局由月令定，喜用神配合定吉凶。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_355]` `[trigger: 相刑]` `[factor_trigger: penalty]` `[role: 条件分支]` 三刑主灾厄，自刑主自伤。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_356]` `[trigger: 权势]` `[factor_trigger: power]` `[role: 结果]` 官杀有力主权势。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_357]` `[trigger: 禄]` `[factor_trigger: prosperity_lu]` `[role: 条件分支]` 禄者临官也，日主之禄为食禄之位。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_358]` `[trigger: 扶抑]` `[factor_trigger: restrain_support]` `[role: 主干]` 扶抑者取用之法，强抑弱扶。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_359]` `[trigger: 富贵]` `[factor_trigger: riches_honor]` `[role: 结果]` 格局成就主富贵。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_360]` `[trigger: 比劫]` `[factor_trigger: rob_wealth]` `[role: 条件分支]` 劫财克财，主争夺、破财。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_361]` `[trigger: 有根]` `[factor_trigger: rooted]` `[role: 条件分支]` 天干有根则力强，无根则虚浮。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_362]` `[trigger: 七杀]` `[factor_trigger: seven_killing]` `[role: 条件分支]` 七杀为偏官，主威权、刚毅。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_363]` `[trigger: 比肩]` `[factor_trigger: shoulder_compare]` `[role: 条件分支]` 比肩为同类，主竞争、助力。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_364]` `[trigger: 六合]` `[factor_trigger: six_harmony]` `[role: 条件分支]` 六合主合化，合则变性。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_365]` `[trigger: 配偶]` `[factor_trigger: spouse]` `[role: 主干]` 日支为配偶宫，财官为配偶星。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_366]` `[trigger: 身强]` `[factor_trigger: strong_body AND abundant_wealth_strong_body AND body_vigorous_no_reliance AND body_vigorous_weak_adjustment]` `[role: 条件分支]` 身强可任财官，喜财官运。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_367]` `[trigger: 三合]` `[factor_trigger: three_harmony]` `[role: 条件分支]` 三合成局力大，会合化气。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_368]` `[trigger: 调候]` `[factor_trigger: tiao_hou]` `[role: 条件分支]` 调候者调和寒暖燥湿，为取用之法。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_369]` `[trigger: 透出]` `[factor_trigger: transparent]` `[role: 条件分支]` 天干透出则显，藏于地支则隐。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_370]` `[trigger: 用神]` `[factor_trigger: use_god]` `[role: 主干]` 用神为命局核心，喜用定吉凶。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_371]` `[trigger: 水]` `[factor_trigger: water]` `[role: 主干]` 水为北方之气，主智主肾。 → 《渊海子平·论五行生克制化》
  - `[ns_yhzp_372]` `[trigger: 身弱]` `[factor_trigger: weak_body AND abundant_wealth_weak_body AND body_vigorous_no_reliance AND body_vigorous_weak_adjustment]` `[role: 条件分支]` 身弱不胜财官，喜印比扶助。 → 《渊海子平·论五行生克制化》"""
    normalized_text_zh: str = """"""
    subject: str = "论五行生克制化——各有所喜所害例"
    factor_refs: list = ['five_element_generation', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论五行生克制化__各有所喜所害例_001_L1",
    )
    version: str = "1.0.0"
