"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101543
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
    semantic_id="smth_v1.0.0_亡神本义与泄气之忧_001",
    book_id="sanming",
    engine_id="bazi"
)
class 亡神本义与泄气之忧(SemanticEntry):
    """
    - **原文（source_text）**：
  水生木，申子辰以亥为亡神，亥中甲木，泄水也。火生土，寅午戌以巳为亡神，巳中戊土，泄火也。金生水，巳酉丑以申为亡神，申中壬水，泄金也。木生火，亥卯未以寅...
    """
    
    original_text: str = """- **原文（source_text）**：
  水生木，申子辰以亥为亡神，亥中甲木，泄水也。火生土，寅午戌以巳为亡神，巳中戊土，泄火也。金生水，巳酉丑以申为亡神，申中壬水，泄金也。木生火，亥卯未以寅为亡神，寅中丙火，泄木也。古歌云：「亡神七煞祸非轻，用尽机关一不成；克子刑妻无祖业，仕人犹恐有虚名。」又云：「命宫若也值亡神，须是长生遇贵人；时日更兼天地合，匪躬蹇蹇作王臣。」又云：「皆言七煞是亡神，莫道亡神祸非轻；身命若还居此地，贫穷蹇滞过平生。凶星恶曜如临到，大限浑如履薄冰；三合更须明审察，煞来夹拱必难行。」

- **分字分词释义**：
  - **亡神**：以五行生我之处为「泄气之神」，标示本气被消耗、难以自守之位。
  - **泄水 / 泄火 / 泄金 / 泄木**：分别说明亡神所在支中所藏天干，会把原五行的力量泄散。
  - **亡神七煞祸非轻**：亡神与七煞等重煞同见时，主祸端颇重，难以全身而退。

- **规范化释义（primary_lang_explained）**：
  相对劫煞的「外来夺取」，亡神偏向「内在泄漏」：从五行相生的角度看，水生木、火生土、金生水、木生火，各有生出之处；这些位置若落在命盘关键宫位，就像能量出口，把本源气机不断泄出，因此称为亡神。歌诀强调其凶性：易有劳而无功、克子刑妻、祖业不守等象；若再与七煞、凶星等同见，则一生多有贫困、蹇滞与险象。不过原文亦指出：命宫见亡神若又逢长生、贵人、天地合等结构，仍可转为「匪躬蹇蹇作王臣」之格，体现亡神并非绝对之凶。

- **完整对等诠释（secondary_lang_full）**：
  Loss Spirit marks the outlets where an element qi constantly flows away toward what it generates, creating chronic leakage rather than sudden robbery.
  Charts with heavy Loss Spirit often show patterns of working hard with modest visible return, or of resources and attention repeatedly draining into others or into background maintenance.
  When it is accompanied by longevity positions or noble stars, some of this leaking can be reframed as service, loyalty or self sacrifice, so modelling should reduce but not erase the value of affected factors.
- **核心要点**：
  - 亡神着重刻画「能量泄漏点」：即便格局有力，若亡神重叠，又被凶煞夹拱，就容易出现付出与收获严重不对等的状况。
  - 在系统建模中，可将亡神视为削弱主气的权重因子：既要在财、官、印等层面扣减其有效强度，又要保留「逢贵化吉」的可能，通过与长生、贵人等特征的同宫情况，来调整最终评估。

- **详细解说**：
  1) 按照五行相生关系推算各局亡神所在支位，在命盘中标注 `wang_shen_positions`，并记录其是否落在日主、财星、官星、印星等关键宫位；
   2) 计算亡神的「泄气强度」，如与七煞、劫煞等同宫或夹拱则提高其权重，与长生、贵人、印绶等同见则相应减弱其负面效应；
   3) 在评分模型中，将亡神用于调整「努力—回报匹配度」与「资源留存率」等指标：亡神重而无救者提高「高投入低产出」的概率；
   4) 在解释层，将亡神更多描述为「能量与资源外泄的结构」，提示在时间管理、财务管理与情绪边界上需要特别注意，而不是简单断为「一生无成」。

 - 反例与边界：
   - 不宜因命盘见亡神就否定命主既有的成绩或努力，把一切挫折都归咎于「命不好」；
   - 若现实中命主已经通过制度、团队或工具建立了良好的「防泄漏结构」（如财务规划、心理支持系统），亡神的负向作用会明显被削弱，应在模型中允许这一修正；
   - 工程上若简单以是否有亡神来划分「成功 / 失败」人群，会得到高度偏颇的分类边界，应更多把它视为修正因子而非主导因子；
   - 反向误区是完全无视亡神标签，使模型对「明明很努力但总差一步」这类体验缺乏表达能力。

 - 小例（示意）：
   - 某命局财星、官星都颇为有力，却有亡神多重叠现且被煞夹拱，现实表现为长期加班、频繁投入项目却回报不成比例，系统可用「亡神泄气」解释其高投入低产出的轨迹，并在建议中强调建立边界与选择性投入；
  - 另一命局亦有亡神，但同时得长生、贵人同宫相扶，现实中虽多波折却常能在关键节点获得支持，最终在公共服务或组织体系中担任稳重角色，系统则将其视为「在耗散中仍能累积」的结构，而非单纯凶象。"""
    normalized_text_zh: str = """"""
    subject: str = "亡神本义与泄气之忧"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_62', 'bazi_semantic', 'bazi_state_strength_9', 'bazi_semantic', 'bazi_state_factor_140', 'bazi_semantic', 'bazi_function_factor_13', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_亡神本义与泄气之忧_001_L1",
    )
    version: str = "1.0.0"
