"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725683
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
    semantic_id="zw_v1.0.0_20_天马星与四化星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 20天马星与四化星(SemanticEntry):
    """
    - 原文（source_text）：

  问：天马星所主若何？

  希夷先生答曰：诸宫各有制化，如身命临之，谓之驿马，喜禄存、紫府、昌曲守照为吉。如大小二限临之，更遇禄存、紫府、流昌必利。如与禄存...
    """
    
    original_text: str = """- 原文（source_text）：

  问：天马星所主若何？

  希夷先生答曰：诸宫各有制化，如身命临之，谓之驿马，喜禄存、紫府、昌曲守照为吉。如大小二限临之，更遇禄存、紫府、流昌必利。如与禄存同宫，谓之禄马交驰；紫府同宫，谓之扶举马；刑杀同宫，谓之负尸马；火星同宫，谓之战马；日月同宫，谓之雌雄马；逢空亡，谓之死马；居绝死，谓之死马；遇陀罗，谓之折足马。以上犯此数者，俱主灾病。流年值之，依此断。

- 分字分词释义：

  - **驿马**：象征奔波迁移与路程变动的星曜，主行动频仍、环境转换。
  - **禄马交驰**：天马与禄存同宫，象征“动中有禄”，奔波中获得俸禄与机缘。
  - **扶举马**：天马与紫微、天府同宫，主有人提携、升迁快速。
  - **负尸马**：刑杀同宫之马，多主灾病、意外、重负压身。
  - **折足马**：遇陀罗成折足之象，行动受阻、行程受损甚至伤残。

- 规范化释义（primary_lang_explained）：

  天马在紫微斗数中，是把“行动”“位移”“奔波”这一整套人生经验集中抽象出来的一颗星。落在身命宫，多主命主性格上坐不住、路上机缘多，人生需要透过不断移动来完成；落在迁移宫，则更强调现实空间上的出差、远行、调动、移民。经文强调“喜禄存、紫府、昌曲守照为吉”，意思是说：当天马与禄存、紫微天府、文昌文曲这些代表资源、平台与文化资本的星曜同会时，奔波本身就会带来财富、声望和成长——人越动越开阔，越跑越有东西可拿。

  但同一颗天马，也可能因为伴星不同而变成完全不同的“马”：刑杀同宫是负尸马，奔波中容易扛着伤病与压力；火星同宫为战马，多见争执、事故或高风险任务；空亡、绝死成死马，动而无成甚至以凶险收场；陀罗则成折足马，象征被迫停滞、行动受挫。整体来看，天马并不简单主好主坏，而是提示命主：你一生中哪些领域与阶段，必须通过“在路上”来应对课题，同时提醒哪些马象需要格外谨慎，以免把该成长的移动，走成无谓的消耗。

- 完整对等诠释（secondary_lang_full）：

  In Ziwei Doushu, Tianma embodies the principle of movement and displacement in a chart. It shows where life refuses to stay static—where work, circumstance or temperament keep pushing a person to travel, relocate or operate across distances. When Tianma is placed in the Life or Body palaces, it often describes a mobile temperament: someone who thrives on change, learns through exposure to different places and rarely feels fulfilled in a fixed, enclosed setting. When it appears in the Travel or Movement palace, the focus shifts to concrete relocation patterns: frequent business trips, cross‑regional careers, migration, or repeated changes of residence.

  The classic text then translates complex combinations into a series of horse images. When Tianma runs together with Lucun, it forms "Galloping Stipend Horse": resources, pay and opportunities arrive precisely through going out. With Ziwei and Tianfu, it becomes a "Supporting Horse", symbolising patrons, promotions and being lifted by institutions. In harsher mixtures—"Corpse‑Bearing Horse" with punitive stars, "War Horse" with Huoxing, "Dead Horse" with void and death sectors, or "Broken‑Leg Horse" with Tuoluo—movement is coloured by illness, conflict, exhaustion or sudden breakdown. Rather than labelling travel as simply lucky or unlucky, Tianma maps a landscape of motion: some journeys are avenues of advancement, others are marches into depletion. Interpreting this star well means knowing when to lean into movement, and when a restless urge or external push is leading into avoidable harm.

- 核心要点：

  1. **驿马主动**：身命临之谓驿马，主动荡奔波。
  2. **禄马交驰**：与禄存同宫为禄马交驰，大吉之格。
  3. **多种马象**：扶举马（紫府）、负尸马（刑杀）、战马（火星）、雌雄马（日月）、死马（空亡绝死）、折足马（陀罗）。
  4. **吉凶分判**：禄存紫府昌曲守照为吉，刑杀空劫为凶。

- 叙事素材（narrative_snippets）：

  - **驿马奔波**："身命临之，谓之驿马"，命带天马多主一生在路上，以奔波换取视野与成长。
  - **禄马交驰**："如与禄存同宫，谓之禄马交驰"，动中有禄，出门奔走反而带来俸禄机缘。
  - **扶举之马**："紫府同宫，谓之扶举马"，天马遇紫微天府，多有贵人扶举、升迁快速之象。
  - **凶险诸马**："刑杀同宫谓负尸马，火星同宫谓战马，逢空亡居绝死谓死马，遇陀罗谓折足马"，提示奔波中夹带灾病、争战与行程中断的风险。
  - **吉凶分判**："喜禄存、紫府、昌曲守照为吉，如大小二限临之，更遇禄存、紫府、流昌必利"，说明同为奔波，有的开路，有的耗损。
  - **现代应用**：天马可作为评估"迁移/职业流动"的指标——看动起来是打开格局，还是在高风险环境中消耗生命力。"""
    normalized_text_zh: str = """"""
    subject: str = "20 天马星与四化星"
    factor_refs: list = ['star_tianma', 'concept_yima', 'pattern_luma_jiaoqu', 'pattern_fuju_ma', 'pattern_zhezu_ma']
    
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
        l1_anchor="zw_v1.0.0_20_天马星与四化星_001_L1",
    )
    version: str = "1.0.0"
