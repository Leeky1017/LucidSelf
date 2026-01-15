"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919290
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
    semantic_id="zy_v1.0.0_家人卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 家人卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  家人：利女贞。

  【彖传】
  《彖》曰：家人，女正位乎内，男正位乎外。男女正，天地之大义也。家人有严君焉，父母之谓也。父父，子子...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  家人：利女贞。

  【彖传】
  《彖》曰：家人，女正位乎内，男正位乎外。男女正，天地之大义也。家人有严君焉，父母之谓也。父父，子子，兄兄，弟弟，夫夫，妇妇，而家道正。正家而天下定矣。

  【象传】
  《象》曰：风自火出，家人；君子以言有物，而行有恒。

  【爻辞】
  初九，闲有家，悔亡。
  六二，无攸遂，在中馈，贞吉。
  九三，家人嗃嗃，悔厉，吉；妇子嘻嘻，终吝。
  六四，富家，大吉。
  九五，王假有家，勿恤，吉。
  上九，有孚威如，终吉。

- 分字分词释义：

  - **家人**：家中的人，也指家庭之道、家政之理。
  - **利女贞**：利于女子守贞守正，强调内位之正，对全家结构尤为关键。
  - **女正位乎内，男正位乎外**：女主人安于内位，男主人当其外职，指角色分工各得其当（在 L1 层尊重原文结构）。
  - **严君焉，父母之谓也**：家中有严明的主事者，即父母，强调慈而有节的威严。
  - **父父，子子，兄兄，弟弟，夫夫，妇妇**：各司其名、各尽其位，是家道正的基础。
  - **风自火出**：下离为火，上巽为风，风从火中出，象征内在德行向外感化。
  - **言有物，而行有恒**：说话有内容、有根据，行为常久如一。
  - **闲有家**：预先防范家庭内部之乱，设置边界与规范。
  - **中馈**：指掌管家中饮食之职，引申为居于内、管理日常生活。
  - **嗃嗃 / 嘻嘻**：嗃嗃为严厉有声；嘻嘻为嬉笑无度。

- **规范化释义（primary_lang_explained）**：

  家人卦讨论的是“如何经营一个有秩序、有温度的家庭”，并由此推及天下。卦辞“家人：利女贞”点出一个关键：家之稳定有赖于内位（多由女性承担）守正守节，维持内部秩序和温度。

  彖传从家内外的结构出发：“女正位乎内，男正位乎外。男女正，天地之大义也。”——内外分工各得其当，是家庭秩序的基础。父母作为“严君”，既有威严又有爱护，通过各人“像其所是”（父像父、子像子等），使家道正，进而“正家而天下定矣”。

  象传“风自火出，家人；君子以言有物，而行有恒”说明：家庭内部的德行如火，风从火中出，象征家中气息影响外在世界。君子从家人之道学习：说话要有内容和分寸，行为要恒常而不反复无常。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Jia Ren (Family) addresses 家道与齐家. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 家人卦核心是**“从家之正出发，推及天下之定”**。
  - “利女贞”强调内位守正的重要性，但并不否定外位之责，而是指出“内外皆正”方为大义。
  - 爻辞从防范家乱、内治中馈、严厉与嬉戏的平衡，到富家、王假有家、有孚威如，呈现家庭治理的层级与成熟度。

- 详细解说：

  卦象上巽下离：离为火、为明；巽为风、为入。火在内而风在外，风自火出，象征内在明德通过言行之风影响外界。与明夷相比，明夷是光明入地而晦，家人则是光明在家中燃烧，再被风带出。

  初九“闲有家，悔亡”强调预防：在家道尚未混乱之时就“闲”——防范、设限，可免后悔。六二“无攸遂，在中馈，贞吉”说明：内位之人不必追求对外的“有所成就”，而是把中馈之职做好，即为贞吉。

  九三“家人嗃嗃，悔厉，吉；妇子嘻嘻，终吝”呈现家庭气氛的两极：过严则有悔厉但能吉，过嬉则终致可吝，提示在严与乐之间寻求平衡。六四“富家，大吉”说明当家人得其道时，物质富裕可以成为善用的资源，而非纷争之源。

  九五“王假有家，勿恤，吉”将视角扩展到统治者：君王视天下如家，自然“交相爱”，不必忧虑，则为吉；上九“有孚威如，终吉”则收束全卦：家庭与领导者都需要“有孚”（可信）与“威如”（可畏），二者兼备，才能终吉。


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_335]` `[trigger: 卦=家人 AND 卦辞=利女贞]` `[factor_trigger: zhouyi_gua_jiaren AND zhouyi_guaci]` `[role: 主干]` 家人，利女贞：治家之道在于女正位乎内。 → 《周易·家人卦·卦辞》
  - `[ns_zhouyi_336]` `[trigger: 卦=家人 AND 彖传]` `[factor_trigger: zhouyi_gua_jiaren AND zhouyi_tuan AND zhouyi_jiating_chengdu]` `[role: 主干依赖]` 女正位乎内，男正位乎外。 → 《周易·家人卦·彖传》
  - `[ns_zhouyi_337]` `[trigger: 卦=家人 AND 象传=风自火出]` `[factor_trigger: zhouyi_gua_jiaren AND zhouyi_xiang]` `[role: 主干依赖]` 风自火出，家人；君子以言有物而行有恒：言行一致以治家。 → 《周易·家人卦·象传》
  - `[ns_zhouyi_338]` `[trigger: 卦=家人 AND 初九=闲有家]` `[factor_trigger: zhouyi_gua_jiaren]` `[role: 条件分支]` 闲有家，悔亡：以规矩治家，悔恨自消。 → 《周易·家人卦·爻辞》
  - `[ns_zhouyi_339]` `[trigger: 卦=家人 AND 六二=无攸遂]` `[factor_trigger: zhouyi_gua_jiaren]` `[role: 条件分支]` 无攸遂，在中馈，贞吉：专事中馈，守正则吉。 → 《周易·家人卦·爻辞》
  - `[ns_zhouyi_340]` `[trigger: 卦=家人 AND 九三=家人嗃嗃]` `[factor_trigger: zhouyi_gua_jiaren]` `[role: 例外处理]` 家人嗃嗃，悔厉吉：严厉治家，虽厉而终吉。 → 《周易·家人卦·爻辞》
  - `[ns_zhouyi_341]` `[trigger: 卦=家人 AND 六四=富家大吉]` `[factor_trigger: zhouyi_gua_jiaren]` `[role: 条件分支]` 富家，大吉：家道丰裕，大为吉祥。 → 《周易·家人卦·爻辞》
  - `[ns_zhouyi_342]` `[trigger: 卦=家人 AND 九五=王假有家]` `[factor_trigger: zhouyi_gua_jiaren]` `[role: 主干依赖]` 王假有家，勿恤吉：王以有家为本，不忧自吉。 → 《周易·家人卦·爻辞》
  - `[ns_zhouyi_343]` `[trigger: 卦=家人 AND 上九=有孚威如]` `[factor_trigger: zhouyi_gua_jiaren]` `[role: 总结]` 有孚威如，终吉：以诚信立威，终得其吉。 → 《周易·家人卦·爻辞》
  - **中文**：
  - 卦辞"家人：利女贞"依通行王弼本；"家人"谓一家之人，重在治家之道，"利女贞"强调女子守内之正。
  - "风自火出"谓巽风由离火而出，火热生风，象征家教由内而外传播。
  - "言有物，行有恒"谓君子治家须言语有实、行为有常，内外一致。
  - "闲有家"之"闲"释为防闲、规矩，以礼法规范家人，悔恨可消。
  - "中馈"指主持家中饮食之事，六二柔居中位，专事内务。
  - "嗃嗃"释为严厉之声，治家过严虽令人畏惧，但可避免放纵之祸。
  - "王假有家"之"假"释为至、临，王者以治家为本而治天下。
  - **English**: Based on Wang Bi commentary edition. "家人" means household members. "风自火出" shows wind from fire—family teachings spread outward. "闲" means protective rules. "中馈" refers to managing household food. "嗃嗃" indicates stern discipline."""
    normalized_text_zh: str = """"""
    subject: str = "家人卦（䷤）"
    factor_refs: list = ['zhouyi_gua_037', 'principle_woman_inner_position_proposal', 'principle_words_substance_actions_proposal', 'principle_dignity_fortune_proposal', 'principle_family_order_world_peace_proposal']
    
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
        l1_anchor="zy_v1.0.0_家人卦_001_L1",
    )
    version: str = "1.0.0"
