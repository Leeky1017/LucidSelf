"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755688
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
    semantic_id="zw_v1.0.0_论小儿命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论小儿命(SemanticEntry):
    """
    - 分字分词释义：

  - **小儿命**：婴幼儿的命格判断。
  - **博士力士**：小儿命中的神煞星。
  - **青龙将军**：小儿命中的神煞星。
  - **大耗死符病符**：主灾病的神煞...
    """
    
    original_text: str = """- 分字分词释义：

  - **小儿命**：婴幼儿的命格判断。
  - **博士力士**：小儿命中的神煞星。
  - **青龙将军**：小儿命中的神煞星。
  - **大耗死符病符**：主灾病的神煞星。
  - **落地无声**：婴儿出生时不哭，主凶。
  - **弱遭伤**：体弱易受伤害。
  - **关杀**：小儿命中的关煞。
  - **易养难养**：婴幼儿是否容易养育。
  - **刑克父母**：对父母有刑克作用。

- 原文（断句）：

  小儿博士、力士上短下长，青龙将军，腮小头圆，大耗鼻仰唇缩，死符病符，声高性雄；官府奏书逢恶曜，落地无声；白虎大岁遇七杀，防弱遭伤。湏分生克制化之垣，更看帝禄盛衰之地，复观关杀，方知寿天穷通。

  凡小儿初生，命中星辰庙旺，大小二限未行，断其灾少，易养，父母无克。若命坐恶杀，又缠陷地，大小二限未行，断其灾多，难养，刑克父母。

- 规范化释义（primary_lang_explained）：

  本条先以一串带有神煞名号的形貌暗示，说明古人观察小儿命时，会留意头型、五官、声音与初生反应等征象，将之与「小儿」「博士」「力士」「青龙」「将军」「大耗」「死符」「病符」「官府奏书」「白虎」「七杀」等神煞体系对应：例如上短下长的身形、腮小头圆、鼻仰唇缩、声高性雄、落地无声，或弱小之体逢伤等，皆被视为早年安危、灾伤与夭折风险的提醒。但原文也强调，这些只是象征性的提示，必须放回命盘结构中，与诸神煞所落之宫位、所会恶曜一并参详。

  第二段回到一般性的判断原则：凡小儿初生之命，若命中主星庙旺得地，且大小二限尚未来到凶陷之地，多主灾少易养，父母无大刑克；若命宫或相关要害宫位被恶杀守照，又落于陷地，即便大小二限尚未正式行到，也往往应在早年灾病频仍、难以养育，并可能带出刑克父母的格局。本条重点在于：小儿命的吉凶，不可只看一时形貌吉凶征象，而须结合星曜庙旺、神煞生克与限运早晚，共同判断其寿天穷通、易养与否，以及与父母之间的刑克关系。

- 完整对等诠释（secondary_lang_full）：

  This section deals with how Ziwei astrology judges the fates of infants. It
  begins with a series of symbolic spirit names—Infant, Scholar, Strongman,
  Green Dragon, General, Great Loss, Death Talisman, Illness Talisman,
  Official Documents, Petitions, White Tiger and Seven Killings—tied to
  features such as a short upper body and long lower body, small cheeks and a
  round head, an upturned nose and tight lips, a loud and forceful voice, a
  baby that does not cry at birth, or a frail body prone to injury. These
  signs are not meant to be read in isolation, but as visual hints that certain
  auxiliary stars may be active and that early years could carry heightened
  risk of illness, harm or even early death.

  The core rule is then stated more plainly. When the main stars in an infant's
  chart stand in temple dignity and the major and minor periods have not yet
  reached harsh places, misfortunes tend to be few, the child is easier to
  raise and there is little harm to the parents. If, however, the Life palace
  or other key positions are occupied by killing stars in debility, even before
  the periods arrive the chart already leans toward frequent sickness, hard
  upbringing and possible loss or injury to the parents. Reading an infant's
  destiny therefore requires combining bodily signs, spirit-star patterns and
  the timing of periods, rather than making extreme predictions from any single
  omen.

- 核心要点：

  1. 小儿形貌、声音与初生反应，被古法用来对应特定神煞组合，提示早年安危与伤病风险。
  2. 真正的寿夭轻重，仍以命中主星庙旺与否、恶杀多寡、所处地势（庙旺/陷地）为根本依据。
  3. 大小二限尚未来到凶陷之地而命星庙旺，多主灾少易养，父母无大刑克。
  4. 命坐恶杀又加陷地，即便限运未至，仍易见灾多难养，并有刑克父母的可能。
  5. 断小儿命须综合形貌征象、神煞配置与限运推移，避免只凭单一征兆下夭折或克亲的极端断语。

- 叙事素材（narrative_snippets）：

  - **形貌征象**："小儿形貌声音与初生反应，对应神煞组合"，古法以外观推命。
  - **庙旺为本**："寿夭轻重以命中主星庙旺与否、恶杀多寡为根本"，星力决定寿夭。
  - **灾少易养**："大小限未至凶陷而命星庙旺，灾少易养，父母无刑克"，命旺限吉则安全。
  - **灾多难养**："命坐恶杀加陷地，灾多难养，刑克父母"，命凶则风险高。
  - **现代应用**：本条提醒对幼儿命盘应综合评估而非极端断语，可用于评估早年健康风险。"""
    normalized_text_zh: str = """"""
    subject: str = "论小儿命"
    factor_refs: list = ['group_xiaoershensha', 'system_daxiaoxian', 'result_yiyang', 'pattern_xingkefumu', 'level_dilu', 'source_ref', 'rel_xiaoer_001', 'state_miaoxian', 'rel_xiaoer_002', 'group_xiaoershensha', 'rel_xiaoer_003', 'pattern_xingkefumu', 'evi_xiaoer_001', 'state_miaoxian', 'rule_xiaoer_yiyang', 'evi_xiaoer_002', 'pattern_xingkefumu', 'rule_xiaoer_nanyang', 'concept_infant_fate', 'concept_parent_harm']
    
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
        l1_anchor="zw_v1.0.0_论小儿命_001_L1",
    )
    version: str = "1.0.0"
