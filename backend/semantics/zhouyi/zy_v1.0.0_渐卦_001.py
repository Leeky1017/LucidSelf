"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919480
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
    semantic_id="zy_v1.0.0_渐卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 渐卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  渐，女归吉，利贞。

  【彖传】
  《彖》曰：“渐之进也，女归吉也。进得位，往有功也。进以正，可以正邦也。其位刚，得中也。止而巽，...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  渐，女归吉，利贞。

  【彖传】
  《彖》曰：“渐之进也，女归吉也。进得位，往有功也。进以正，可以正邦也。其位刚，得中也。止而巽，动不穷也。”

  【象传】
  《象》曰：山上有木，渐；君子以居贤德，善俗。

  【爻辞】
  初六，鸿渐于干，小子厉，有言，无咎。
  六二，鸿渐于磐，饮食衎衎，吉。
  九三，鸿渐于陆，夫征不复，妇孕不育，凶；利御寇。
  六四，鸿渐于木，或得其桷，无咎。
  九五，鸿渐于陵，妇三岁不孕，终莫之胜，吉。
  上九，鸿渐于陆，其羽可用为仪，吉。

- 分字分词释义：

  - **渐**：渐进、逐步之意，强调按次序、按时势慢慢前行，而非急骤跃迁。
  - **女归吉，利贞**：“女归”指女子出嫁，遵礼而行则吉，亦利于守正；以婚礼六礼比喻一切“按程序渐进”的事。
  - **山上有木**：下艮为山，上巽为木，山上生木，象征在稳固根基之上缓慢生长。
  - **鸿渐于干 / 磐 / 陆 / 木 / 陵**：大雁逐步迁徙、渐次登高，从水边到岩石、旷野、树木、高陵，构成一条渐进路径。
  - **衎衎**：读作“坎（kǎn）”，形容欢然自得的状态。
  - **夫征不复，妇孕不育**：丈夫远征不归，妻子虽孕而不育，比喻在不合时宜的推进中，两端皆失。
  - **桷**：椽木，用以支撑屋顶，比喻所获未必为全体，但足以构成结构一部分。
  - **其羽可用为仪**：大雁的羽毛可为礼仪之用，比喻渐进之功可转化为制度与礼仪的装点。

- **规范化释义（primary_lang_explained）**：

  渐卦接于艮卦之后，讲的是“在止之后如何渐进”。卦辞“渐，女归吉，利贞。”用女子出嫁为喻：婚礼须循六礼而行，一步一步推进，方为吉且利贞。若越次急行，则失其正。

  彖传说：“渐之进也，女归吉也。进得位，往有功也。”——所谓渐进，是在每一阶段各得其位的前提下前行，因此“往有功”；“进以正，可以正邦也”则将个体渐进提升到国家层面：循正道而前进，可以安定邦国。九五之刚居中，使渐进不至偏斜；“止而巽，动不穷也”说明渐卦兼具艮之止与巽之入，既能安顿，又能入世，动而有节。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Jian (Gradual Progress) addresses 循序渐进. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 渐卦核心是**“循序渐进”**：不越级、不躁进，在时间与结构上逐层推进。
  - 婚礼六礼是渐之范式：一切重大关系与事业，都应如“女归”一般循礼而行。
  - 渐进并非停滞，而是在适当等待中寻找合宜的推进点。

- 详细解说：

  卦象为上巽下艮：艮为山、为止，巽为风、为入，风行山上而树木渐长，是“由静到动、由根至枝”的图景。与升卦之直上相比，渐更强调“迂缓且有台阶”的成长。

  初六“鸿渐于干，小子厉，有言，无咎。”描绘的是渐进之初：大雁才到水边浅处（干），下位者易于轻举，故“小子厉”；然能从言语中得到提醒，终可“无咎”。六二“鸿渐于磐，饮食衎衎，吉。”则是稍进一步：立足于磐石之上，饮食安然，是稳健渐进之吉象。

  九三“鸿渐于陆，夫征不复，妇孕不育，凶；利御寇。”转为警戒：若在尚未稳固时过快推进，如夫远征不返、妻孕而不育，两端皆失，乃凶；但其位刚，有御寇之利，在防御层面仍有用武之地。六四“鸿渐于木，或得其桷，无咎。”则说明渐入结构内部：如鸟落于木，所获不一定是整栋房屋，却可得椽木之才，以成局部，无咎。

  九五“鸿渐于陵，妇三岁不孕，终莫之胜，吉。”呈现的是渐进高位但仍有迟滞：起初“三岁不孕”，成果未显；然终究无人能胜，终归于吉。上九“鸿渐于陆，其羽可用为仪，吉。”作为收束，强调渐进之果：大雁已行至平陆，其羽可供礼仪之饰，象征渐进之德可化为制度与文化的部分，成为可见之“仪”。


#### L2 语义提取


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_479]` `[trigger: 卦=渐 AND 卦辞=女归吉]` `[factor_trigger: zhouyi_gua_jian2 AND zhouyi_guaci]` `[role: 主干]` 渐，女归吉，利贞：渐进之道，如女归夫家。 → 《周易·渐卦·卦辞》
  - `[ns_zhouyi_480]` `[trigger: 卦=渐 AND 彖传]` `[factor_trigger: zhouyi_gua_jian AND zhouyi_tuan]` `[role: 主干依赖]` 进也。女归吉也。 → 《周易·渐卦·彖传》
  - `[ns_zhouyi_481]` `[trigger: 卦=渐 AND 象传=山上有木]` `[factor_trigger: zhouyi_gua_jian2 AND zhouyi_xiang]` `[role: 主干依赖]` 山上有木，渐；君子以居贤德善俗：如木渐长于山，以德渐化风俗。 → 《周易·渐卦·象传》
  - `[ns_zhouyi_482]` `[trigger: 卦=渐 AND 初六=鸿渐于干]` `[factor_trigger: zhouyi_gua_jian2]` `[role: 条件分支]` 鸿渐于干，小子厉：鸿雁渐进于涯岸。 → 《周易·渐卦·爻辞》
  - `[ns_zhouyi_483]` `[trigger: 卦=渐 AND 六二=鸿渐于磐]` `[factor_trigger: zhouyi_gua_jian2]` `[role: 条件分支]` 鸿渐于磐，饮食衎衎：鸿雁进于磐石，安乐饮食。 → 《周易·渐卦·爻辞》
  - `[ns_zhouyi_484]` `[trigger: 卦=渐 AND 九三=鸿渐于陆]` `[factor_trigger: zhouyi_gua_jian2]` `[role: 例外处理]` 鸿渐于陆，夫征不复：鸿雁进于陆地，远征不归。 → 《周易·渐卦·爻辞》
  - `[ns_zhouyi_485]` `[trigger: 卦=渐 AND 六四=鸿渐于木]` `[factor_trigger: zhouyi_gua_jian2]` `[role: 条件分支]` 鸿渐于木，或得其桷：鸿雁进于树上。 → 《周易·渐卦·爻辞》
  - `[ns_zhouyi_486]` `[trigger: 卦=渐 AND 九五=鸿渐于陵]` `[factor_trigger: zhouyi_gua_jian2]` `[role: 主干依赖]` 鸿渐于陵，妇三岁不孕：鸿雁进于高陵。 → 《周易·渐卦·爻辞》
  - `[ns_zhouyi_487]` `[trigger: 卦=渐 AND 上九=鸿渐于逵]` `[factor_trigger: zhouyi_gua_jian2]` `[role: 总结]` 鸿渐于逵，其羽可用为仪：鸿雁渐至高处，羽毛可作仪饰。 → 《周易·渐卦·爻辞》
  - **中文**：
  - 卦辞"渐：女归吉，利贞"依通行王弼本；"女归"指女子出嫁归夫家，取其循序渐进、合礼合节之义。
  - "鸿渐于干/磐/陆/木/陵/逵"六爻以鸿雁渐进为喻，由低至高：干（水涯）、磐（大石）、陆（平地）、木（树）、陵（高丘）、逵（九达之道）。
  - "衎衎"释为安乐和悦之貌；"桷"为椽木或屋角；"逵"为四通八达之大路。
  - "其羽可用为仪"谓鸿雁飞至高处，羽毛可作礼仪装饰，象征渐进之终成就。
  - **English**: Based on Wang Bi commentary edition. "女归" metaphor for gradual proper process. Wild goose progresses through six stages: 干(bank)→磐(rock)→陆(land)→木(tree)→陵(hill)→逵(crossroads). Each stage shows proper gradual advancement."""
    normalized_text_zh: str = """"""
    subject: str = "渐卦（䷴）"
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
        l1_anchor="zy_v1.0.0_渐卦_001_L1",
    )
    version: str = "1.0.0"
