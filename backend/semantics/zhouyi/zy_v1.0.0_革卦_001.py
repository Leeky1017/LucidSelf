"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919442
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
    semantic_id="zy_v1.0.0_革卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 革卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  革，己日乃孚。元亨利贞，悔亡。

  【彖传】
  《彖》曰：“革，水火相息，二女同居，其志不相得，曰革。己日乃孚，革而信也。文明以说...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  革，己日乃孚。元亨利贞，悔亡。

  【彖传】
  《彖》曰：“革，水火相息，二女同居，其志不相得，曰革。己日乃孚，革而信也。文明以说，大亨以正，革而当，其悔乃亡。天地革而四时成，汤武革命，顺乎天而应乎人，革之时大矣哉！”

  【象传】
  《象》曰：泽中有火，革；君子以治历明时。

  【爻辞】
  初九，巩用黄牛之革。
  六二，己日乃革之，征吉，无咎。
  九三，征凶，贞厉，革言三就，有孚。
  九四，悔亡，有孚，改命，吉。
  九五，大人虎变，未占有孚。
  上六，君子豹变，小人革面，征凶，居贞吉。

- 分字分词释义：

  - **革**：本义为去旧皮，引申为改变、变革、更新，并不专指近代意义上的“革命”。
  - **己日乃孚**：“己日”，指筹划已定、条件成熟之时；“乃孚”，于是获得信任。整体指在合适时机推行变革，方能赢得人心。
  - **水火相息**：水在下、火在上，相互制约又相互成全，比喻旧势与新势彼此牵制，需要通过“革”来重新协调。
  - **二女同居，其志不相得**：上下两卦皆为“女”象，同处一室而志向不合，比喻旧制度、新要求长期共存必然积累冲突，不革则难持久。此处为结构隐喻，并非价值评判。
  - **文明以说，大亨以正**：“文明”指内在光明有文采，“以说”指外在和悦可亲；在变革中内守文德、外持喜悦，再辅以“以正”为尺度，方能大亨而不乱。
  - **治历明时**：修订历法、明确时序，比喻通过厘清“节奏与时机”来引导变革，而不是任意鼓动。
  - **巩用黄牛之革**：以黄牛皮坚固绑缚，比喻在革新伊始要以忠厚、坚实之力稳住局面，不可草率松散。
  - **己日乃革之**：在“己日”那样已果熟的时刻才真正实施变革，强调择时与酝酿，而非一时冲动。
  - **革言三就，有孚**：“革言”，关于变革的宣言与主张；“三就”，多次沟通、渐次成形。说明变革之言需反复筹商、反复说明，方能积累诚信。
  - **改命**：改动既定命令或体制安排，不是宿命论中的“天命”观念，而是对“制度之命”的调整。
  - **大人虎变 / 君子豹变 / 小人革面**：以虎、豹换毛喻高层与君子之深度自我更新；“革面”则多指小人只改外表、不换内里。
  - **征凶，居贞吉**：在已成之局中轻率出征则凶，安居守贞则吉，提示变革完成后应有一段稳固期。

- **规范化释义（primary_lang_explained）**：

  革卦讨论的是“如何在旧局积弊已深时，择时而变、以信成革”。卦辞云：“革，己日乃孚。元亨利贞，悔亡。”——当变革酝酿成熟，在合适的“己日”推行，就有可能获得信任，成就通达而又合乎正道的变局，并且消除先前的忧悔。

  彖传用“水火相息、二女同居其志不相得”说明革卦的结构根源：上下相斥、内外不合，已到了“非变不可”的时段；但真正的“革”并非单纯破坏，而是“文明以说，大亨以正”——在文德与喜悦之中实施，以正道为准绳。天地四时的循环、汤武之“革命”，都被视为顺乎天时、应乎人心的“大利之革”；其关键在“顺时而动，以正自持”。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Ge (Revolution) addresses 变革鼎新. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 革卦的核心是**“有时有信的变革”**：不在于一味“变”或一味“守”，而在于何时变、怎样变、为谁而变。
  - 言与行都要经历“多次就成”：革言须三就，制度也需在多轮沟通中成熟，否则难以取信于众。
  - 变革完成后，仍需一段“守成期”：大人虎变、君子豹变之后，小人若仅革面，仍可能在“征”中招凶，唯有“居贞”才可长久。

- 详细解说：

  革卦卦象为上兑下离：离为火、为明，兑为泽、为悦，火在泽中，是“泽中有火”的局面。看似光明欢悦，实则内外不相安：火欲上炎，水欲下润，久而不调，迟早需要调整。与前卦井之“恒久供养”相比，革强调的是“当恒久之道被现实结构扭曲时，必须有所更新”。

  初九“巩用黄牛之革”处于变革之始：尚未公开翻案，而是在内部以坚实、忠厚的力量巩固即将展开的革局，避免一开始就陷入散乱。六二“己日乃革之，征吉，无咎”则把握时机：在条件尚不具备前，宁可再等；到了“己日”，动则有功，但仍需警惕出征过程中的风险。

  九三“征凶，贞厉，革言三就，有孚。”点出语言与行动的张力：若只顾出征、不顾说明与沟通，则“征凶、贞厉”；唯有让“革言三就”——多次陈说、充分酝酿，才可能转危为安。九四“悔亡，有孚，改命，吉。”则进入变革中段：在前期反思的基础上，有孚而“改命”，使原有制度或命令得以修正，此时“悔亡”。

  九五“大人虎变，未占有孚。”凸显高层在革局中的角色：真正的大人以“虎变”示人——变化之彻底如虎换毛，且其可信度无需再卜，占前即已“有孚”。上六“君子豹变，小人革面，征凶，居贞吉。”则作为收束：君子之变虽不及虎之剧烈，但也如豹纹换新，内外一致；小人多只革其面，缺乏内在转变，因此如果在此时再“征”则凶，反而“居贞”——守于本位、稳住局面，更为可取。


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_443]` `[trigger: 卦=革 AND 卦辞=己日乃孚]` `[factor_trigger: zhouyi_gua_ge AND zhouyi_guaci]` `[role: 主干]` 革，己日乃孚，元亨利贞：变革在适时，诚信方能亨通。 → 《周易·革卦·卦辞》
  - `[ns_zhouyi_444]` `[trigger: 卦=革 AND 彖传]` `[factor_trigger: zhouyi_gua_ge AND zhouyi_tuan]` `[role: 主干依赖]` 水火相息。二女同居。 → 《周易·革卦·彖传》
  - `[ns_zhouyi_445]` `[trigger: 卦=革 AND 象传=泽中有火]` `[factor_trigger: zhouyi_gua_ge AND zhouyi_xiang]` `[role: 主干依赖]` 泽中有火，革；君子以治历明时：水火相息，明辨时变。 → 《周易·革卦·象传》
  - `[ns_zhouyi_446]` `[trigger: 卦=革 AND 初九=巩用黄牛之革]` `[factor_trigger: zhouyi_gua_ge]` `[role: 条件分支]` 巩用黄牛之革：以柔顺坚固之物束缚，不可轻动。 → 《周易·革卦·爻辞》
  - `[ns_zhouyi_447]` `[trigger: 卦=革 AND 六二=己日乃革之]` `[factor_trigger: zhouyi_gua_ge]` `[role: 条件分支]` 己日乃革之，征吉：至时而变，征行则吉。 → 《周易·革卦·爻辞》
  - `[ns_zhouyi_448]` `[trigger: 卦=革 AND 九三=征凶贞厉]` `[factor_trigger: zhouyi_gua_ge]` `[role: 例外处理]` 征凶贞厉，革言三就：变革之言须三思而行。 → 《周易·革卦·爻辞》
  - `[ns_zhouyi_449]` `[trigger: 卦=革 AND 九四=悔亡有孚]` `[factor_trigger: zhouyi_gua_ge]` `[role: 条件分支]` 悔亡，有孚改命吉：变革得信，改命得吉。 → 《周易·革卦·爻辞》
  - `[ns_zhouyi_450]` `[trigger: 卦=革 AND 九五=大人虎变]` `[factor_trigger: zhouyi_gua_ge]` `[role: 主干依赖]` 大人虎变，未占有孚：大人如虎之变，威仪自明。 → 《周易·革卦·爻辞》
  - `[ns_zhouyi_451]` `[trigger: 卦=革 AND 上六=君子豹变]` `[factor_trigger: zhouyi_gua_ge]` `[role: 总结]` 君子豹变，小人革面：君子如豹纹之变，小人则改面从新。 → 《周易·革卦·爻辞》
  - **中文**：
  - 卦辞"革：己日乃孚，元亨利贞，悔亡"依通行王弼本立句；"己日"训为"适当时日"，非仅指干支之己日。
  - "大人虎变"之"虎变"释为虎之斑纹由浅而深之变化，比喻大人之变革显明有力；"豹变"则较虎变为细腻，象征渐进优化。
  - "革面"一词，小人之"革"仅在表面，非真实内在转化，与君子"豹变"相对。
  - "巩用黄牛之革"中"巩"释为束缚、固守，"黄牛之革"取其柔韧坚固，示初期不宜轻动。
  - **English**: Based on Wang Bi commentary edition. "己日" interpreted as "appropriate day" rather than literally the Ji day in the stem-branch cycle. "虎变/豹变" metaphors describe different degrees of transformation—dramatic versus gradual. "革面" indicates superficial change only."""
    normalized_text_zh: str = """"""
    subject: str = "革卦（䷰）"
    factor_refs: list = []
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_革卦_001_L1",
    )
    version: str = "1.0.0"
