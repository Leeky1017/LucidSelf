"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.885343
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
    semantic_id="zgjm_v1.0.0_水火盗贼灯烛_001",
    book_id="zhougong",
    engine_id="dream"
)
class 水火盗贼灯烛(SemanticEntry):
    """
    - **原文（source_text）**：

  水上行者主大吉，水上立者主凶事。水流洋洋有新婚。  
  水上火出主大吉，自在水中大吉利。自跌水中不出凶。  
  饮水不休得大财，流水绕身有狱讼。...
    """
    
    original_text: str = """- **原文（source_text）**：

  水上行者主大吉，水上立者主凶事。水流洋洋有新婚。  
  水上火出主大吉，自在水中大吉利。自跌水中不出凶。  
  饮水不休得大财，流水绕身有狱讼。大水澄清大吉利。  
  人家有水儿子亡，江海涨漫大吉昌。河水沙石益文章。  
  火烧日月有人助，火烧河水长命吉。火烧山野大显达。  
  火烧自屋主兴旺，火焰炎炎主发财。火从地生疾病至。  
  执火乘行官位至，大火烧天主国安。身在火中贵人扶。  
  火烟黑色主疾病，把火行路大通达。把火烧井主疾病。  
  宅中火光大吉利，厨中火出有急事。听选燃火作明府。  
  烧人臭秽主大吉，见烛者主大发财。灯烛光明主大吉。  
  众人闱炉和合吉，恶人相引疾病至。赶贼入市不出凶。  
  强贼入宅主家破，与贼同行大吉利。己身作贼所求得。

- 分字分词释义：

  - **水上行、水上立**：在水面上行走为吉，站立不动则为凶，体现"动则生、静则滞"的逻辑。
  - **水流洋洋**：水流宽广舒缓，象征喜庆与新婚之象。
  - **水上火出**：水面上冒出火焰，为水火既济之象，主大吉。
  - **自在水中、自跌水中不出**：自如游泳为吉，跌入水中无法出来为凶。
  - **流水绕身**：水流环绕身体，象征被纠缠或卷入纷争，主狱讼。
  - **火烧日月、火烧河水、火烧山野**：火势广大而向上，多主吉利、长命或显达。
  - **火烧自屋**：自家房屋起火，反主家业兴旺（逆反之象）。
  - **火从地生**：火从地面冒出，主疾病将至。
  - **灯烛光明**：灯火明亮，象征前途光明与财富临门。
  - **强贼入宅、与贼同行**：强盗入屋主家破，但与贼同行反主吉利。
  - **己身作贼**：自己成为盗贼，主所求之事能得。

- **规范化释义（primary_lang_explained）**：

  本类条目围绕"水火盗贼灯烛"展开，揭示梦象学中对**水、火与盗贼**的独特解读——水主财与流动，火主兴旺与疾病，盗贼则呈现复杂的吉凶两面。水上行走主吉，水流洋洋主新婚，大水澄清主吉利；火烧日月、河水、山野多主吉利长命，火烧自屋主兴旺；灯烛光明主发财。然而也有凶象：水上站立主凶，自跌水中不出为凶，流水绕身主狱讼，火从地生主疾病，强贼入宅主家破。

- 核心要点：

  - **水的吉凶在于动静与出入**：水上行走为吉，站立为凶；自在水中为吉，跌入不出为凶。
  - **水流宽广澄清多主吉**：水流洋洋主新婚，大水澄清主吉利，江海涨漫主吉昌。
  - **火势向上向外多主吉**：火烧日月、河水、山野、自屋多主吉利兴旺，但火从地生主疾病。
  - **灯烛光明主财富与光明**：见烛、灯烛光明皆主发财与吉利。
  - **盗贼的吉凶取决于关系**：强贼入宅主家破，但与贼同行、己身作贼反主吉利。

- 详细解说：

  **（一）水的动静与出入：生命力的流动**

  本类开篇即揭示"水上行者主大吉，水上立者主凶事"，构成梦象学中对水的基本理解：水象征财富与生命力的流动，在水上行走（动）则生机勃勃，站立不动（静）则滞塞不通。"自在水中大吉利，自跌水中不出凶"进一步强调"出入自如"的重要性：能自如游泳为吉，失控跌入为凶。

  **（二）水流宽广澄清：喜庆与财富**

  "水流洋洋有新婚，大水澄清大吉利，江海涨漫大吉昌"三句揭示宽广澄清之水的吉利象征：水流宽广舒缓主喜庆新婚，大水澄澈主吉利，江海涨潮主吉昌。但"流水绕身有狱讼"提示水若纠缠身体，则主被卷入纷争。

  **（三）火势向上向外：兴旺与显达**

  "火烧日月有人助，火烧河水长命吉，火烧山野大显达，火烧自屋主兴旺"四句构成火的吉利象征：火势向上向外、燃烧广大，多主兴旺、长命、显达与人助。"火烧自屋主兴旺"属逆反之象，自家起火反主家业兴旺。

  **（四）火从地生与火烟黑色：疾病之兆**

  "火从地生疾病至，火烟黑色主疾病"两句提示火的凶象：火从地面冒出（向下或内敛）主疾病将至，火烟呈黑色（污浊不清）亦主疾病。

  **（五）灯烛光明：财富与前途**

  "见烛者主大发财，灯烛光明主大吉"揭示灯火的吉利象征：灯烛明亮象征前途光明、财富临门与吉利。

  **（六）盗贼的双面性**

  "强贼入宅主家破，与贼同行大吉利，己身作贼所求得"三句呈现盗贼的复杂吉凶：被动遭贼（强贼入宅）主家破，但主动与贼同行或自己作贼，则反主吉利与所求能得，体现"主动与被动"的差异。

- 校勘与字词辨析（本类）：

  - "水火盗贼灯烛"六字标题按底本录入，涵盖水、火、盗贼与灯烛四大主题。
  - "水上行者主大吉，水上立者主凶事"一句，"行"与"立"的对比体现"动则生、静则滞"的梦象逻辑。
  - "火烧自屋主兴旺"一句为典型逆反之象，本稿在释义中特别标注。
  - "与贼同行大吉利，己身作贼所求得"两句，与"强贼入宅主家破"形成鲜明对比，体现主动与被动的差异。
  - "听选燃火作明府"一句，"听选"指等候选任，"明府"指州郡长官，本稿保留原文。

- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_1066]` `[trigger: 梦见水上行者]` `[factor_trigger: dream_walk_water_2]` `[role: 主干]` 水上行者，主大吉。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1067]` `[trigger: 梦见水上立者]` `[factor_trigger: dream_stand_water_2]` `[role: 主干]` 水上立者，主凶事。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1068]` `[trigger: 梦见水流洋洋]` `[factor_trigger: dream_water_flow_2]` `[role: 主干]` 水流洋洋，有新婚。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1069]` `[trigger: 梦见水上火出]` `[factor_trigger: dream_fire_water_2]` `[role: 主干]` 水上火出，主大吉。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1070]` `[trigger: 梦见自在水中]` `[factor_trigger: dream_in_water_2]` `[role: 主干]` 自在水中，大吉利。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1071]` `[trigger: 梦见饮水不休]` `[factor_trigger: dream_drink_water_2]` `[role: 主干]` 饮水不休，得大财。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1072]` `[trigger: 梦见流水绕身]` `[factor_trigger: dream_water_around_2]` `[role: 主干]` 流水绕身，有狱讼。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1073]` `[trigger: 梦见大水澄清]` `[factor_trigger: dream_clear_water_2]` `[role: 主干]` 大水澄清，大吉利。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1074]` `[trigger: 梦见江海涨漫]` `[factor_trigger: dream_sea_flood_2]` `[role: 主干]` 江海涨漫，大吉昌。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1075]` `[trigger: 梦见火烧日月]` `[factor_trigger: dream_fire_sun_2]` `[role: 主干]` 火烧日月，有人助。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1076]` `[trigger: 梦见火烧山野]` `[factor_trigger: dream_fire_mountain_2]` `[role: 主干]` 火烧山野，大显达。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1077]` `[trigger: 梦见火烧自屋]` `[factor_trigger: dream_fire_house_2]` `[role: 主干]` 火烧自屋，主兴旺。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1078]` `[trigger: 梦见火焰炎炎]` `[factor_trigger: dream_flame_2]` `[role: 主干]` 火焰炎炎，主发财。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1079]` `[trigger: 梦见火从地生]` `[factor_trigger: dream_fire_ground_2]` `[role: 主干]` 火从地生，疾病至。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1080]` `[trigger: 梦见大火烧天]` `[factor_trigger: dream_fire_sky_2]` `[role: 主干]` 大火烧天，主国安。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1081]` `[trigger: 梦见见烛者]` `[factor_trigger: dream_candle_2]` `[role: 主干]` 见烛者，主大发财。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1082]` `[trigger: 梦见灯烛光明]` `[factor_trigger: dream_lamp_bright_2]` `[role: 主干]` 灯烛光明，主大吉。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1083]` `[trigger: 梦见强贼入宅]` `[factor_trigger: dream_thief_home_2]` `[role: 主干]` 强贼入宅，主家破。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1084]` `[trigger: 梦见与贼同行]` `[factor_trigger: dream_walk_thief_2]` `[role: 主干]` 与贼同行，大吉利。 → 《周公解梦·水火盗贼灯烛》
  - `[ns_zgjm_1085]` `[trigger: 梦见己身作贼]` `[factor_trigger: dream_be_thief_2]` `[role: 主干]` 己身作贼，所求得。 → 《周公解梦·水火盗贼灯烛》"""
    normalized_text_zh: str = """"""
    subject: str = "水火盗贼灯烛"
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
        book_id="zhougong",
        chapter="",
        l1_anchor="zgjm_v1.0.0_水火盗贼灯烛_001_L1",
    )
    version: str = "1.0.0"
