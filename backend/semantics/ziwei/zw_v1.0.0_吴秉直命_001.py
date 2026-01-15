"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699571
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
    semantic_id="zw_v1.0.0_吴秉直命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 吴秉直命(SemanticEntry):
    """
    - 分字分词释义：

  - **巨日拱照**：巨门与太阳同向拱照命宫，主光彩、名声与表达力。
  - **日辰月戌并争荣曜**：日居辰、月居戌相争而光彩并见，主荣曜华贵。
  - **禄科俱会左右拱...
    """
    
    original_text: str = """- 分字分词释义：

  - **巨日拱照**：巨门与太阳同向拱照命宫，主光彩、名声与表达力。
  - **日辰月戌并争荣曜**：日居辰、月居戌相争而光彩并见，主荣曜华贵。
  - **禄科俱会左右拱朝**：禄星与科星同会，左辅右彼环拱，主终身富贵。
  - **天伤忌凶之地**：天伤及诸忌星聚集之宫位，主损伤与不利事件。
  - **陀罗天刑**：陀罗与天刑同会，主刑狱、纠缠与致命打击。
  - **其年命终**：在该年限运中遇重凶叠加而身亡。
  - **阳男水二局**：吴秉直命盘的五行局数，水二局主智慧刚正。

- **原文（source_text）**：  
  吴秉直命。阳男水二局。巨日拱照，日辰月戌并争，荣曜，禄科俱会，左右拱朝，终身富贵。大小二限入天伤忌凶之地，太岁逢佗罗、天刑，俱主凶兆，其年命终。

- **规范化释义（primary_lang_explained）**：  
  吴秉直命为阳男水二局，「巨日拱照，日辰月戌并争，荣曜」大致可理解为巨门与太阳对拱命宫，日辰月戌相争而光彩并见，配合禄星与科星同会，左右辅弼环拱，是「巨日拱命 + 禄科俱会 + 左右拱朝」的华贵结构，一生终身富贵。命主名中有「秉直」，亦暗合此类格局常见的刚直、公正形象。  
  然而，原文指出大小二限行入「天伤忌凶之地」，太岁又逢陀罗与天刑等重凶，象征在该阶段天伤、忌星与刑杀之气集中一处，对身体、名誉乃至人身安全形成多重夹击。结果是在本应仍可享荣的阶段，突遭重创而命终。此命例呈现的是「华贵富贵格局，在天伤天刑与陀罗等杀曜叠加之运中折损」的形态。

- **完整对等诠释（secondary_lang_full）**：  
  Wu Bingzhi’s chart is that of a Yang Water native in the Second Configuration. Ju Men and the Sun beam onto the Life palace—"Ju and Sun illuminating," with Sun in Chen and Moon in Xu contesting yet shining. Together with Lu and academic Ke stars, and Left and Right Assistants flanking the configuration, this becomes a brilliant pattern of honour and wealth. The name "Bingzhi" (upholding rectitude) echoes the upright, forthright quality often associated with such structures.  
  But the text warns that both major and minor periods move into regions of Tian Shang and other "Ji‑凶" influences, while the Annual Tai Sui meets Tuo Luo and Tian Xing. This cluster of wounding, malefic and penal stars signals severe pressure on health, reputation and personal safety. Thus, despite a life marked by sustained wealth and status, the native’s end comes in a year where these heavy transits converge. The case illustrates a radiant, high‑status chart cut short by a concentration of injury‑and‑penalty indicators.

- **核心要点**：  
  1. 巨日拱命配合禄科俱会与左右拱朝，是华贵而端正的富贵命格。  
  2. 大小二限行入天伤忌凶之地，太岁逢陀罗、天刑等重凶，构成终结性高危年份。  
  3. 呈现「终身富贵而结局被重凶运截断」的命局特征。

- **叙事素材（narrative_snippets）**：
  - **秉直富贵**："巨日拱照，日辰月戌并争，荣曜，禄科俱会，左右拱朝，终身富贵"，吴秉直命主以巨日华贵格局，名利双全。
  - **性格投射**：姓名中有"秉直"，亦呼应巨日格局常见的刚正、公平与自我要求。
  - **天伤天刑**："大小二限入天伤忌凶之地，太岁逢佗罗、天刑，俱主凶兆，其年命终"，天伤、陀罗、天刑齐至，为富贵人生画上突然而沉重的句号。
  - **现代应用**：对性格刚直、在组织中常扮演「执法者」或「把关人」角色的人来说，当运势集中天伤、天刑与陀罗之年，应在坚持原则的同时，为自己设下安全边界与法律/医疗防线，避免因一时硬碰而付出不可逆代价。"""
    normalized_text_zh: str = """"""
    subject: str = "吴秉直命"
    factor_refs: list = ['pattern_juri_gongzhao', 'pattern_richenyuexu', 'pattern_luke_juhui', 'pattern_zuoyou_gongchao', 'malefic_tianshang_jiexiong', 'malefic_tuoluo_tianxing']
    
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
        l1_anchor="zw_v1.0.0_吴秉直命_001_L1",
    )
    version: str = "1.0.0"
