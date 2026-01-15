"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755846
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
    semantic_id="zw_v1.0.0_论立命行限宫歌_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论立命行限宫歌(SemanticEntry):
    """
    - 分字分词释义：

  - **立命行限宫**：命主五行属性与行限所到宫位卦象之间的匹配关系。
  - **五行命格**：金、木、水、火、土五种命主类型，各有对应的敏感宫位。
  - **坦离艮兑震...
    """
    
    original_text: str = """- 分字分词释义：

  - **立命行限宫**：命主五行属性与行限所到宫位卦象之间的匹配关系。
  - **五行命格**：金、木、水、火、土五种命主类型，各有对应的敏感宫位。
  - **坦离艮兑震巽**：八卦方位象征，对应行限所到的方向与环境特性。
  - **金人遇坦命须伤**：金命之人行限落坦宫（水位），多主伤损与险阻。
  - **土到震巽脹血惊慌**：土命之人行限到东南震巽之方，需防脹血之疾与惊恐之事。
  - **吉曜照临未免官灾**：即使有吉星同度或拱照，触发五行敏感组合仍难完全避免波折。
  - **体质不适配**：命主五行与行限宫位之间的不兼容，导致原本顺利的运程多出折腾。

- 原文（断句）：

  论立命行限宫歌：

  歌：金人遇坎命须伤，木命逢离有祸殃。水遇艮宫应蹇滞，火来兑上祸难藏。土到东南逢震巽，曰须防脓血及惊慌。

  纵然吉曜相逢照，未免官灾闹一场。

- 规范化释义（primary_lang_explained）：

  本条以歌诀的形式，将五行命格与行限所到宫位的卦象对应起来，用以快速提示行限期间的身体与事件风险。大意是说：金命之人行限若落坎宫，多主伤损与险阻；木命之人行限落离宫，多见祸殃与波折；水命之人行限到艮宫，易有蹇滞、停滞不前之象；火命行限至兑宫，灾祸难以完全掩藏；土命之人行限走到东南震巽之方，则需特别防范脓血之疾与惊慌之事。这里的「坎、离、震、巽、兑、艮」可视为方位与宫位的象征，对应不同类型的风险主题。

  尾句「纵然吉曜相逢照，未免官灾闹一场」，强调的是：即便该期有吉星同度或拱照，只要命五行与行限宫位之间触发了这类敏感组合，仍难完全避免某种形式的风波，只是轻重有别。换言之，这条歌诀并不否定吉星的作用，而是提醒占者：在某些组合下，行限的「体质不适配」会让原本可以全然顺利的运程，多出几场不必要的折腾，尤其体现为官非、争执、疾病或突发事故，需要预先有心理与实际准备。

- 完整对等诠释（secondary_lang_full）：

  This short verse links a person's elemental life type with the house or
  direction where a travelling period is anchored. It says that metal people
  meeting Kan, wood people meeting Li, water people meeting Gen, fire people
  meeting Dui and earth people moving through the south-eastern Zhen–Xun sector
  are especially prone to certain troubles: injuries, misfortune, stagnation,
  hidden crises or illnesses involving pus and blood. Rather than listing
  detailed star combinations, it uses the language of trigrams to sketch where a
  person's inherent qualities and a period's environment may rub against each
  other.

  The closing line adds that even when benefic stars shine on such a period, one
  may still experience at least some noise—an official dispute, a health scare,
  a bout of turbulence. In modern work this rule is best treated as a coarse
  sensitivity map. Once a period has been judged basically good or bad from
  stars and houses, the element–trigram pairing can indicate which kinds of
  issues to watch for and where extra prudence can turn a potentially messy year
  into one of manageable lessons instead of avoidable crises.

- 核心要点：

  1. 将命主五行（金、木、水、火、土）与行限所到宫位的卦象（坎、离、艮、兑、震、巽）建立风险对照关系。
  2. 不同组合对应不同类型的潜在问题，如伤损、祸殃、蹇滞、隐性灾祸、脓血与惊恐等。
  3. 即使有吉曜照临，只要触发这些敏感组合，往往仍难免有官非或波折，只是轻重强弱因格局而异。
  4. 此歌适合作为「大略体感」层面的提示，用以评估某一行限在身体、官非与突发事件上的敏感度。
  5. 实务中应将其与具体星曜、宫位所属事务、现实场景合参，而非单凭五行与卦象配对就下绝对结论。"""
    normalized_text_zh: str = """"""
    subject: str = "论立命行限宫歌"
    factor_refs: list = ['type_wuxingming', 'system_guaxiang', 'pos_xinxianguaxiang', 'event_guanzai', 'risk_nongxue', 'source_ref', 'rel_wuxing_001', 'type_wuxingming', 'rel_wuxing_002', 'pos_xinxianguaxiang', 'rel_wuxing_003', 'event_guanzai', 'evi_wuxing_001', 'type_wuxingming', 'rule_wuxing_guaxiang', 'evi_wuxing_002', 'event_guanzai', 'rule_wuxing_bozhe', 'concept_element_trigram', 'concept_period_sensitivity']
    
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
        l1_anchor="zw_v1.0.0_论立命行限宫歌_001_L1",
    )
    version: str = "1.0.0"
