"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654048
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
    semantic_id="zw_v1.0.0_六十花甲子纳音歌_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 六十花甲子纳音歌(SemanticEntry):
    """
    - **原文（source_text）**：  
  紫微天机逆行傍，隔一阳武天同当，又隔二位，廉贞地空三复见紫微郎。天府太阴与贪狼，巨门天相及天梁七杀空三破军位，八星顺数细推详。

- **分字分词...
    """
    
    original_text: str = """- **原文（source_text）**：  
  紫微天机逆行傍，隔一阳武天同当，又隔二位，廉贞地空三复见紫微郎。天府太阴与贪狼，巨门天相及天梁七杀空三破军位，八星顺数细推详。

- **分字分词释义**：  
  - **紫微天机逆行傍**：以紫微为起点，天机等北斗诸星依逆行次序相傍而布。  
  - **隔一阳武天同当**：逆数时中间留一空宫，接着为太阳、武曲、天同等星曜。  
  - **又隔二位，廉贞地空三复见紫微郎**：再隔两宫安廉贞，与地空等星同垣，构成再次与紫微呼应的格局。  
  - **天府太阴与贪狼，巨门天相及天梁**：点出南斗六星的顺行次序，为天府、太阴、贪狼、巨门、天相、天梁。  
  - **七杀空三破军位**：七杀与破军再按特定间隔安置，其中“空三”指中间留出三宫的落点规律。  
  - **八星顺数细推详**：强调南斗诸星需顺行推算，具体细节须在实盘中一一推演。

- **规范化释义（primary_lang_explained）**：  
  本诀总摄紫微斗数十四主星的安放规则。北斗一系以紫微为起点，依逆时针方向布星：紫微坐镇一宫，其后间隔一宫安天机，再隔一宫安太阳、武曲、天同，之后再隔两宫安廉贞，并与地空等星形成呼应结构，构成一条完整的北斗主星链。南斗一系则以天府为首，按顺时针方向依次安太阴、贪狼、巨门、天相、天梁，形成与北斗相对而又互为补充的另一条主星链。七杀与破军不直接写在歌诀字面之中，而是作为附加主星，依南斗起点和三宫间隔等规则另行安置。整体而言，本条以简练歌诀概括十四主星的空间分布与顺逆、隔位规律，并暗示“先定紫微、再排余星”的核心程序。

- **完整对等诠释（secondary_lang_full）**：  
  This verse condenses how Ziwei Doushu arranges its fourteen major stars as two coordinated chains. On the North Dipper side, Ziwei is taken as the origin. From that palace the stars are laid out counter‑clockwise with deliberate gaps: one empty house, then Tianji; another empty house, then the sequence that brings in the Sun, Wuqu and Tiantong; after skipping two further palaces, Lianzhen appears in a position that resonates again with Ziwei and with the emptiness stars such as Dikong. Together they form a backbone of northern, more sovereign‑style stars. On the South Dipper side, Tianfu is the starting point. From Tianfu the line runs clockwise through Taiyin, Tanlang, Jumen, Tianxiang and Tianliang, outlining a second backbone that focuses more on resources, reception and mediation. Qisha and Pojun are not fully spelled out in the wording of the verse, but are understood to be placed at fixed offsets from Tianfu, one three palaces away and the other opposite, so that the two killing stars complete the overall field of strength and risk. In practice, an astrologer first anchors Ziwei by separate algorithms based on the native’s year, month and day, and then uses this verse to distribute the remaining main stars by reversing or advancing through the houses with the prescribed skips. The result is a stable stellar framework on which all later auspicious and inauspicious influences are interpreted.

- **核心要点**：  
  - 以紫微为北斗起点、以天府为南斗起点，构成两条主星链。  
  - 北斗逆行并带有“隔一、隔二”的空宫节奏，凸显紫微—廉贞等关键节点。  
  - 南斗顺行，六星连珠，偏重承载、资源与人事调和。  
  - 七杀、破军作为补充杀星，按固定间隔嵌入南斗体系，完善格局的锋锐与风险。  
  - 实务中必须先定紫微位置，再依歌诀逆顺推星，是排盘算法的核心步骤之一。

- **详细解说**：  
  这一条将十四主星视作两组互相呼应的星系：紫微—北斗代表“中枢与权柄”，天府—南斗代表“承载与资源”。北斗部分以“逆行”与“隔位”为特征：紫微所在宫位被视为全盘原点，天机等星则在逆数中依节奏依次出现，中间的空宫既是技术上的间隔，也为后续吉凶星腾挪留下空间。廉贞与地空等星的交汇位置，往往是格局中既有变动又带压力的关键点。  
  南斗部分则靠“顺行”与“连珠”来表现：天府为仓库与中枢，太阴主承载与滋润，贪狼带来欲求与开拓，巨门主言语与是非，天相主衡平与规制，天梁主庇护与善后。六星沿着同一方向依序铺开，使得从天府出发即可一眼看出资源流向与人事格局。  
  七杀、破军的安放使整个主星体系具有“锋刃”：七杀多落在离天府一定间隔之处，象征主动出击的破局力量；破军多在对宫或关键对冲点，象征推倒重来的瓦解力量。歌诀虽然只以“七杀空三破军位”一语带过，但实际算法中已将其纳入整体布局。对实务者而言，熟练掌握本条，不仅是能把星安对位置，更是能从星系结构一眼看出命盘的骨架与张力所在。

- **校勘与字词辨析（双语）**：  
  - **中文**：本条歌文在通行本中多作“紫微天机逆行傍……八星顺数细推详”。个别版本在“地空三”处有写作“地空星”或将“八星”作“诸星”的异文，本书暂不据此分立新解，而是仍按“北斗逆行、南斗顺行、七杀破军另安”的传统理解来处理。  
  - **English**：Different printed editions sometimes vary in how they spell the segment “Di‑kong san” or the closing “eight stars in forward counting”, but these do not change the underlying algorithm: Ziwei sets the origin for the northern chain, Tianfu sets the origin for the southern chain, and Qisha and Pojun are added as killing stars at fixed offsets. A full philological collation is beyond the scope of this volume; here we follow the mainstream technical reading used in practice."""
    normalized_text_zh: str = """"""
    subject: str = "六十花甲子纳音歌"
    factor_refs: list = ['structure_shisizhuxing', 'structure_nandoliuxing', 'structure_beidouqixing', 'new_candidate', 'algo_tianfudingwei', 'algo_shunxingnixing', 'structure_gewekonggong']
    
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
        l1_anchor="zw_v1.0.0_六十花甲子纳音歌_001_L1",
    )
    version: str = "1.0.0"
