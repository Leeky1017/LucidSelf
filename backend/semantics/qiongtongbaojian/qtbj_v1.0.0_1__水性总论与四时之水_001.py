"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578525
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
    semantic_id="qtbj_v1.0.0_1__水性总论与四时之水_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1水性总论与四时之水(SemanticEntry):
    """
    - **原文（source_text）**：
  天倾西北，亥为出水之方，地陷东南，辰为纳水之库，逆流到申而作声，故水不西流。水性润下，顺则有容，顺行十二神，顺也，主有度量，有吉神扶助，乃贵格。逆则有...
    """
    
    original_text: str = """- **原文（source_text）**：
  天倾西北，亥为出水之方，地陷东南，辰为纳水之库，逆流到申而作声，故水不西流。水性润下，顺则有容，顺行十二神，顺也，主有度量，有吉神扶助，乃贵格。逆则有声，逆行十二神，逆也。入格者，主清贵，有声誉。忌刑克，则横流，爱自死自绝则吉。
  水不绝源，仗金生而流远，水流泛滥，赖土克以堤防。水火均，则合既济之美。水土混，则有浊源之凶。四时皆忌火多，则水受渴。忌见土重，则水不流。忌见金死，金死则水困。忌见木旺，木旺则水死。沈芝云：水命动摇，多主浊滥，女人尤忌之。口诀云︰阳水身弱、穷，阴水身弱、主贵。
  生于春月，性滥滔淫，再逢水助，必有崩堤之势。若加土盛，则无泛涨之忧。喜金生扶，不宜金盛，欲火既济，不要火多，见木而可施功，无土仍愁散漫。
  夏月之水，执性归源，时当涸际，欲得比肩，喜金生而助体。忌火旺而焙干。木盛则盗其气。土旺则制其流。
  秋月之水，母旺子相，表里晶莹，得金助则澄清。逢土旺而混浊。火多而财盛，木重而子荣，重重见水，增其泛滥之忧。叠叠逢土，始得清平之意。
  冬月之水，司令当权，遇火、则增暖除寒，见土、则形藏归化。金多、反曰无义。木盛、是谓有情。土太过、势成涸辙。水泛滥、喜土堤防。

- **分字分词释义**：
  - **天倾西北**：天向西北倾斜 / 宇宙观 / 水源方位
  - **亥为出水之方**：亥是水流出之地 / 水之源 / 西北方
  - **辰为纳水之库**：辰是收纳水之库 / 水之墓 / 东南方
  - **润下**：滋润向下流 / 水性 / 五行特性
  - **顺行十二神**：顺着十二长生流行 / 顺流 / 有度量
  - **水火既济**：水火平衡 / 易经卦名 / 吉象
  - **浊源**：源头浑浊 / 水土混杂 / 凶象
  - **崩堤**：堤坝崩溃 / 水泛滥 / 凶象
  - **执性归源**：收敛本性归源 / 夏水涸 / 水弱
  - **母旺子相**：母（金）旺子（水）相 / 秋水特点 / 吉象
  - **司令当权**：当令掌权 / 冬水旺 / 水势强
  - **涸辙**：干涸的车辙 / 水枯竭 / 凶象

- **规范化释义（primary_lang_explained）**：
  **总论**：天倾西北，亥为出水之方（水之源）；地陷东南，辰为纳水之库（水之库）。逆流到申（长生）而作声，故水不西流（水性东流）。水性润下，顺行十二神（顺流）则有容、有度量，有吉神扶助则为贵格。逆行十二神（逆流）则有声，入格者主清贵、有声誉。忌刑克则横流，爱自死自绝则吉（水到死绝之地，静而不动）。
  水不绝源，仗金生而流远；水流泛滥，赖土克以堤防。水火均平，则合"水火既济"之美。水土混杂，则有"浊源"之凶。四时皆忌火多，火多则水受渴（干涸）。忌见土重，土重则水不流（塞）。忌见金死，金死则水困（无源）。忌见木旺，木旺则水死（泄气）。沈芝云：水命动摇，多主浊滥，女人尤忌之。口诀云：阳水身弱主穷，阴水身弱主贵。
  **春月之水**：性滥滔淫（春水旺），再逢水助，必有崩堤之势。若加土盛，则无泛涨之忧。喜金生扶，不宜金盛（金多水浊）。欲火既济，不要火多。见木而可施功（水木清华），无土仍愁散漫。
  **夏月之水**：执性归源（水涸），时当涸际，欲得比肩（水）帮身，喜金生而助体（发源）。忌火旺而焙干。木盛则盗其气（泄水生火）。土旺则制其流。
  **秋月之水**：母旺子相（金旺水相），表里晶莹，得金助则澄清。逢土旺而混浊（己土混壬）。火多而财盛，木重而子荣。重重见水，增其泛滥之忧。叠叠逢土，始得清平之意。
  **冬月之水**：司令当权（旺极），遇火则增暖除寒，见土则形藏归化（止流）。金多反曰无义（金寒水冷）。木盛是谓有情（泄秀）。土太过势成涸辙。水泛滥喜土堤防。

- **完整对等诠释（secondary_lang_full）**：
  **General Theory**: Heaven tilts NW, Hai is direction of water exiting; Earth sinks SE, Chen is vault receiving water. Flowing upstream to Shen making sound, hence water flows not west. Water nature moisturizing-downward, flowing compliant has capacity, main degree-measure, auspicious spirits assisting is noble pattern. Flowing upstream has sound, entering pattern main pure-noble fame. Fear punishment/clashing then flowing-crosswise, loving self-death self-extinction then auspicious.
  Water source not cut, relying on Metal generating to flow far; Water flowing flooding, relying on Earth controlling to dike. Water/Fire balanced, fits "After Completion" beauty. Water/Earth mixed, has "Turbid Source" ominousness. All 4 seasons fear Fire many (Water thirsty), Earth heavy (Water not flow), Metal dead (Water trapped), Wood prosperous (Water dead). Shen Zhi says: Water destiny wavering main turbid-overflowing, women especially fear. Mnemonic: Yang Water weak body poor, Yin Water weak body noble.
  **Spring Water**: Nature overflowing, meeting Water help implies collapsing dikes. If Earth prosperous no flooding worry. Likes Metal generating, not suitable Metal prosperous. Desiring Fire balance not Fire many. Seeing Wood can perform merit, without Earth still worry scattering.
  **Summer Water**: Nature returning source, time at drying-up, desiring Parallel helping, likes Metal generating. Fears Fire prosperous baking dry. Wood prosperous steals Qi. Earth prosperous restricts flow.
  **Autumn Water**: Mother prosperous Child相, surface-interior crystal clear, gaining Metal help then clear. Meeting Earth prosperous then turbid. Fire many wealth prosperous, Wood heavy children glory. Heavy Water increases flooding worry. Piled Earth begins clear-peace intent.
  **Winter Water**: Commanding power, meeting Fire warms/removes cold, seeing Earth hides/returns. Metal many conversely no-righteousness. Wood prosperous is having-sentiment. Earth too much becomes dried tracks. Water flooding likes Earth dike.

- **核心要点**：
  - **喜忌**：喜金生源、土堤防、火既济。忌火多干涸、土重塞流、木旺泄气。
  - **四时**：春喜土制金生；夏喜比劫金生；秋喜火金木；冬喜火暖土制。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_377]` `[trigger: 水五行]` `[factor_trigger: element_water AND water_moisturizing_down]` `[role: 主干]` 天倾西北，亥为出水之方，地陷东南，辰为纳水之库。水性润下，顺则有容。 → 《穷通宝鉴·论水》#35.1
  - `[ns_qttbj_378]` `[trigger: 水火既济]` `[factor_trigger: element_water AND element_fire AND water_fire_balanced]` `[role: 条件分支]` 水火均，则合既济之美。水土混，则有浊源之凶。 → 《穷通宝鉴·论水》#35.1
  - `[ns_qttbj_379]` `[trigger: 春水]` `[factor_trigger: season_spring AND element_water AND water_excessive AND collapsing_dike]` `[role: 条件分支]` 生于春月，性滥滔淫，再逢水助，必有崩堤之势。 → 《穷通宝鉴·论水》#35.1
  - `[ns_qttbj_380]` `[trigger: 夏水]` `[factor_trigger: season_summer AND element_water AND likes_parallel AND likes_metal_source]` `[role: 条件分支]` 夏月之水，执性归源，时当涸际，欲得比肩，喜金生而助体。 → 《穷通宝鉴·论水》#35.1
  - `[ns_qttbj_381]` `[trigger: 秋水]` `[factor_trigger: season_autumn AND element_water AND mother_prosper_child AND crystal_clear]` `[role: 条件分支]` 秋月之水，母旺子相，表里晶莹，得金助则澄清。 → 《穷通宝鉴·论水》#35.1
  - `[ns_qttbj_382]` `[trigger: 冬水]` `[factor_trigger: season_winter AND element_water AND commanding_power AND likes_fire_warm]` `[role: 条件分支]` 冬月之水，司令当权，遇火则增暖除寒，见土则形藏归化。 → 《穷通宝鉴·论水》#35.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 水性总论与四时之水"
    factor_refs: list = ['water_moisturizing_down', 'water_fire_jiji', 'turbid_source']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__水性总论与四时之水_001_L1",
    )
    version: str = "1.0.0"
