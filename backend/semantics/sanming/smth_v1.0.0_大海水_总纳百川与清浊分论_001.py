"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228953
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
    semantic_id="smth_v1.0.0_大海水_总纳百川与清浊分论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大海水总纳百川与清浊分论(SemanticEntry):
    """
    - **原文（source_text）**：
  壬戌、癸亥大海水。大海水者，总纳百川，汪洋无际，包括乾坤之大，升沉日月之光。此水原有清浊，以两般分论。壬戍有土气为浊，癸亥干支纯水，而纳音又水，故清。...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬戌、癸亥大海水。大海水者，总纳百川，汪洋无际，包括乾坤之大，升沉日月之光。此水原有清浊，以两般分论。壬戍有土气为浊，癸亥干支纯水，而纳音又水，故清。壬戌人嫌山，以土气太盛，有金清之，方吉。癸亥最喜见山，然后海水之性始安。涧下丁丑为山，天河与海，上下相通，柱中有木为槎，则乘槎入于天河，极为上格。长流、大溪等水，毕竟皆归于海，以海水不择细流，故能成其大也。壬辰为龙，归大海尤吉，中间又分阴阳互见，干支合化方可。井泉则有所制，与海不通，故不喜见之。诸金独海中第一，以壬戌、癸亥喜见甲子、乙丑，砂中亦得，余金，又当以贵人禄马参之。火喜天上，与海水相为照耀，最吉。霹雳己丑为山，戊癸合化，柱得木火旺地亦吉。山下山头覆灯，诸火不宜见木，惟壬子、癸丑、壬午、癸未俱吉。大林有风冲动，水性不安，平地厚载，则就位相得。松柏石榴，若无土制，则漂泊无定。土爱路傍大驿，惟此二土，足以振之不泄。况癸亥见戊申，为天关地轴大格，日时遇此𫝗土，总有风雷，亦不为害。城头己卯，须资艮则吉，加逄霹雳，则雷火变化，海水汹涌，亦主贫寒。

- **规范化释义（primary_lang_explained）**：
  壬戌、癸亥为大海水。大海水总纳百川，汪洋无际，包含天地之大、承载日月升沉之光，是整个水系的终极汇聚之处。此水本身分清浊两端：壬戌夹土气而为浊，癸亥干支皆水、纳音亦水，为至清之象。壬戌之人忌山土过重，须有清金来澄之方吉；癸亥则最喜见山，方可使海水之性安定。丁丑涧下水可作山，天河水与大海水上下相通，柱中若再有木为槎，则有"乘槎入天河"之上格。长流水、大溪水等终归于海，体现"大海不择细流，故能成其大"之理。壬辰如龙归大海尤吉，中间需阴阳互见、干支合化而成。井泉水因有所束制、与海不通，故不宜多见。金方面，海中金为第一，以壬戌癸亥喜见甲子乙丑，砂中金亦可，余金则须配贵人禄马而用。火以天上火为最吉，与海水相互辉映，为"水火既济"之高格；霹雳火配己丑成山，戊癸合化、柱中得木火旺地亦佳。山下火、山头火、覆灯火诸小火若再见木，多主焚林之祸，唯壬子、癸丑、壬午、癸未等特定组合可为吉。大林木有风冲动，则海性不安；平地木若厚载，则木土就位，与海势相得。松柏与石榴木若无土制，则如漂泊之舟，难定其所。土以路傍土、大驿土为佳，足以振海而不使其泄势；癸亥见戊申为"天关地轴"大格，日时再遇厚土虽有风雷亦不为大害。城头己卯须资艮土为山方吉，加逢霹雳火则雷火搅动海水汹涌，多主贫寒与劳碌。

- **完整对等诠释（secondary_lang_full）**：
  Renxu and Guihai belong to Ocean Water. Ocean Water gathers all rivers, vast and boundless, embracing the greatness of heaven and earth and reflecting the rising and setting of sun and moon—it is the final confluence of the entire water system. This Water naturally divides into clear and turbid forms: Renxu, laden with Earth qi, tends toward turbidity; Guihai, with both stem and branch as Water and its Nayin also Water, embodies crystalline purity. Natives of Renxu dislike mountains because heavy Earth thickens the water; only clear Metal can clarify it. Guihai, by contrast, loves mountains, for only then can the ocean's nature settle. Stream-Below Water at Dingchou can act as mountain; Heavenly-River Water and Ocean Water communicate vertically, and when Wood in the chart serves as raft, one "rides a raft into Heavenly-River", an exalted pattern. Long-Flowing and Great-Stream Waters ultimately return to the sea, illustrating the ocean's greatness in accepting all small tributaries. Renchen as dragon returning to the sea is extremely fortunate, provided yin-yang interseeing and stem-branch transformations occur. Well-Spring Water restricts flow and does not mix with the sea, thus it is unwelcome. Among Metals, Sea-Center Metal ranks first; Renxu and Guihai delight in seeing Jiazi and Yichou, and Sand-Center Metal can also be used; other Metals must be evaluated via nobleman and stipend. For Fire, Sky-Above Fire is most auspicious, illuminating the ocean in a "water-and-fire mutually fulfilled" configuration; Thunder-Bolt Fire with Jichou as mountain, when combined with Wugui transformation and Wood-Fire flourishing, is also good. Hillside-Beneath, Mountain-Top, and Covered-Lamp Fires should not see much Wood, or forest fires ensue; only specific combinations such as Renzi, Guichou, Renwu, Guiwei remain favorable. Great-Forest Wood stirred by wind unsettles the sea; Flat-Earth Wood when thick enough forms a compatible base. Pine-Cypress and Pomegranate Woods without Earth restraints float rootlessly upon the waves. Earth prefers Roadside and Grand-Post Earths, which can brace the sea without draining it; especially when Guihai encounters Wushen, it forms the "Heaven-Gate Earth-Axis" grand pattern, where even with thunder and storms no great harm comes. City-Top Earth at Jimao must receive Gen-Earth to be good; if Thunder-Bolt Fire is added, thunder-fire churns the sea into raging waves, indicating poverty and hardship.

- **核心要点**：
  - 大海水为水系终点，总纳百川，内部分清浊（壬戌浊、癸亥清）
  - 喜山以安其性（癸亥尤喜），喜海中金与甲子乙丑等源头配合
  - 长流、大溪等皆可归海，构成完整水系；井泉则多为受制，不宜多见
  - 土以路傍、大驿为佳，可振而不泄；忌城头配霹雳搅海、木风过动

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_125]` `[trigger: 大海水]` `[factor_trigger: renxu_guihai AND dahai_shui]` `[role: 主干]` 大海水者，总纳百川，汪洋无际，包括乾坤之大，升沉日月之光。此水原有清浊，以两般分论。 → 《三命通会》卷一#大海水

- **详细解说**：
  大海水的关键在于"容量"与"清浊"：它可以容纳一切水的流入，却不必对每一股细流作出区分，这也是"不择细流"的要义。壬戌与癸亥的差异，则揭示了同属大海水却有清浊之别——前者偏向"浊海"，更需要金来澄清与适当的山土节制；后者偏向"清海"，反而需要山来安顿波涛。命理实务中，大海水与长流水、大溪水、天河水、涧下水、井泉水等的关系，可理解为"终点—干道—支流—雨露—泉源"之间的层级：终点若稳且清，则上游再杂亦可化；终点若浊且动，则上游再好也易被拖累。土与风（巽风）决定海面是"有岸可依"还是"风浪不止"，所以路傍土、大驿土象征港口与堤岸，而城头土加霹雳火则象征战乱与风暴。整体判断时，可把壬戌癸亥命局看作承接全局资源与变动的底层容器，其贵贱系于：能否保持清明、不致反噬上游。

- **校勘与字词辨析（双语）**：
  - **中文**："总纳百川"点明大海之容量；"天关地轴"形容癸亥见戊申时海与天地枢纽相接之大格。
  - **English**: "Gathering all hundred rivers" highlights the ocean’s capacity; "Heaven-Gate Earth-Axis" names the grand pattern where Guihai meets Wushen, linking sea with cosmic pivots."""
    normalized_text_zh: str = """"""
    subject: str = "大海水：总纳百川与清浊分论"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_大海水_总纳百川与清浊分论_001_L1",
    )
    version: str = "1.0.0"
