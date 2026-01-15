"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919318
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
    semantic_id="zy_v1.0.0_蹇卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 蹇卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  蹇：利西南，不利东北。利见大人，贞吉。

  【彖传】
  《彖》曰：“蹇，难也，险在前也。见险而能止，知矣哉！蹇，利西南，往得中也；...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  蹇：利西南，不利东北。利见大人，贞吉。

  【彖传】
  《彖》曰：“蹇，难也，险在前也。见险而能止，知矣哉！蹇，利西南，往得中也；不利东北，其道穷也。利见大人，往有功也。当位贞吉，以正邦也。蹇之时义大矣哉！”

  【象传】
  《象》曰：山上有水，蹇；君子以反身修德。

  【爻辞】
  初六，往蹇，来誉。
  六二，王臣蹇蹇，匪躬之故。
  九三，往蹇，来反。
  六四，往蹇，来连。
  九五，大蹇，朋来。
  上六，往蹇，来硕，吉，利见大人。

- 分字分词释义：

  - **蹇**：本义为跛行、难行，引申为处境艰难、前路多阻。
  - **利西南，不利东北**：西南为坤方，象征顺势而下、亲近群众与基础；东北为艮止之方，象征道路受阻、局面穷尽。趋向“得众、得地”则利，逆势而行为不利。
  - **利见大人**：在蹇难之时，有利于求见有德有位的“大人”，借助外在力量共同化解艰难。
  - **贞吉**：在困局中能守中守正，终可以得吉，不是单凭硬撑。
  - **山上有水**：水在山上，既不易下流，又难以积聚，象征环境尴尬、进退维艰。
  - **反身修德**：外路不通时，转向内在，检点自身言行与德行，以自我修正代替盲目前行。
  - **往蹇，来誉 / 来反 / 来连 / 来硕**：“往”为向外而行，“来”为回身而归，在难中选择继续硬往或知难而返，会得到赞誉、喜悦、连难或硕果各不相同。
  - **王臣蹇蹇，匪躬之故**：忠臣为国家艰难奔走受累，并非个人过错，而是代君分忧。
  - **大蹇，朋来**：处于极大艰难之时，若守中守节，反而会有同道者前来相助。

- **规范化释义（primary_lang_explained）**：

  蹇卦讲的是“面对艰难阻滞时，如何选择方向与用力方式”。卦辞说：“蹇：利西南，不利东北。利见大人，贞吉。”——并不是鼓励在任何困难面前硬冲，而是强调要顺势而为：向“西南”之坤方，象征下行、亲近众人和实际基础；避免向“东北”之艮方硬上，象征道路已尽。遇到此局，应求助于有德的大人，共同分担艰难，并在此过程中守住正道，才会吉祥。

  彖传将“蹇”定为“险在前”的局势，而智者之为在于“见险而能止”，知所不为。所谓“利西南”是说向众处、向实处、向柔处走；“不利东北，其道穷也”则告诫不要在穷途末路处固执逞强。“利见大人，往有功也，当位贞吉，以正邦也”则把个体处境提升到国家层面：当邦国遇难，当位者能守正、善用贤臣，便可借蹇中之势修正国政。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Jian (Difficulty) addresses 艰难险阻. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 蹇卦的核心是**“在难中知止与择向，而非盲目前进”**。
  - “利西南、不利东北”不仅是方位，更是选择：是去到得众得地之处，还是执意走向穷尽之路。
  - 爻辞呈现多种应对艰难的方式：有知返而得誉，有往返皆蹇，有大难中得朋援，构成一幅“困境下的行为谱系”。

- 详细解说：

  卦象为上坎下艮：艮为山，坎为水，水在山上，既难以下流，又不易聚成湖海，是“行难”的图景。这一结构比起前卦睽的“同而异”，更着重在外部环境客观阻碍之下，人如何调节自我行动节奏。

  初六“往蹇，来誉”说明，身处最下位者若一味向外奔走，只会处处受阻；若能及时收脚、回到合宜的位置，反而会得到“知险而止”的好名声。六二“王臣蹇蹇，匪躬之故”强调忠臣在艰难中的责任：所受的辛劳与困蹇，并非为一己之身，而是为君、为国、为众承担。

  九三“往蹇，来反”体现的是“知返”的喜悦：处于刚位而有行动能力的人，发现前路艰难时，能主动掉头回返，这种“回头”本身就是内心欢喜之事。六四“往蹇，来连”则显示另一面：身在结构夹层，上下皆难，往有蹇，来亦连，只能在多重束缚中守位待时。

  九五“大蹇，朋来”把视角提升到尊位：当整个系统身处“大蹇”，若居中者仍能守节秉义、调和各方，则自然会有同道来援，此时“解难”的关键是聚众而非独斗。上六“往蹇，来硕，吉，利见大人”则作为收束：最后的动作是带着“硕果”而归——在艰难中完成应有之功，然后退回到合适的位置，再一次“见大人”，让功业归入正统而不再逞强。


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_353]` `[trigger: 卦=蹇 AND 卦辞=利西南不利东北]` `[factor_trigger: zhouyi_gua_jian AND zhouyi_guaci]` `[role: 主干]` 蹇，利西南，不利东北：行险之时，宜向平易之地。 → 《周易·蹇卦·卦辞》
  - `[ns_zhouyi_354]` `[trigger: 卦=蹇 AND 彖传]` `[factor_trigger: zhouyi_gua_jian AND zhouyi_tuan AND zhouyi_jianan_chengdu]` `[role: 主干依赖]` 难也。险在前也。见险而能止。 → 《周易·蹇卦·彖传》
  - `[ns_zhouyi_355]` `[trigger: 卦=蹇 AND 象传=山上有水]` `[factor_trigger: zhouyi_gua_jian AND zhouyi_xiang]` `[role: 主干依赖]` 山上有水，蹇；君子以反身修德：遇险当自省修德。 → 《周易·蹇卦·象传》
  - `[ns_zhouyi_356]` `[trigger: 卦=蹇 AND 初六=往蹇来誉]` `[factor_trigger: zhouyi_gua_jian]` `[role: 条件分支]` 往蹇来誉：前往则蹇，退守则有誉。 → 《周易·蹇卦·爻辞》
  - `[ns_zhouyi_357]` `[trigger: 卦=蹇 AND 六二=王臣蹇蹇]` `[factor_trigger: zhouyi_gua_jian]` `[role: 主干依赖]` 王臣蹇蹇，匪躬之故：臣子虽蹇，非为私利。 → 《周易·蹇卦·爻辞》
  - `[ns_zhouyi_358]` `[trigger: 卦=蹇 AND 九三=往蹇来反]` `[factor_trigger: zhouyi_gua_jian]` `[role: 条件分支]` 往蹇来反：前进则蹇，返回乃宜。 → 《周易·蹇卦·爻辞》
  - `[ns_zhouyi_359]` `[trigger: 卦=蹇 AND 六四=往蹇来连]` `[factor_trigger: zhouyi_gua_jian]` `[role: 例外处理]` 往蹇来连：前进则蹇，退而与众相连。 → 《周易·蹇卦·爻辞》
  - `[ns_zhouyi_360]` `[trigger: 卦=蹇 AND 九五=大蹇朋来]` `[factor_trigger: zhouyi_gua_jian]` `[role: 主干依赖]` 大蹇，朋来：大难之中，援友来助。 → 《周易·蹇卦·爻辞》
  - `[ns_zhouyi_361]` `[trigger: 卦=蹇 AND 上六=往蹇来硕]` `[factor_trigger: zhouyi_gua_jian]` `[role: 总结]` 往蹇来硕，吉：归而得硕果。 → 《周易·蹇卦·爻辞》
  - **中文**：
  - 卦辞"蹇：利西南，不利东北。利见大人，贞吉"依通行王弼本；"蹇"为行路艰难，坎险在上、艮止在下。
  - "西南"为坤方，平易之地；"东北"为艮方，险阻之地。利往平易，不利入险。
  - "山上有水"谓坎水在艮山之上，水阻于山，行路艰难。
  - "反身修德"谓遇险不能强行，宜返身自省、修养德行。
  - "王臣蹇蹇，匪躬之故"谓臣子虽遭困厄，非为一己之私，乃为君国。
  - "往蹇来誉/来反/来连/来硕"四爻皆以"来"为吉，示退守反思胜于冒进。
  - **English**: Based on Wang Bi commentary edition. "蹇" means limping/difficulty. "西南/东北" refer to level vs dangerous terrain. "山上有水" shows water blocked by mountain. "反身修德" advises self-reflection. "往蹇来X" pattern shows return is preferable."""
    normalized_text_zh: str = """"""
    subject: str = "蹇卦（䷦）"
    factor_refs: list = ['zhouyi_gua_039', 'principle_see_danger_stop_proposal', 'principle_benefit_great_person_proposal', 'state_go_difficult_return_honored_proposal', 'principle_self_reflection_virtue_proposal']
    
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
        l1_anchor="zy_v1.0.0_蹇卦_001_L1",
    )
    version: str = "1.0.0"
