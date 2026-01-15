"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699563
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
    semantic_id="zw_v1.0.0_子羽之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 子羽之命(SemanticEntry):
    """
    - 分字分词释义：

  - **巨日拱命**：巨门与太阳拱照命宫，主聪慧、声名与表达力。
  - **禄权科合**：禄星、权星与科星同会，主功名、权位与实际俸禄兼具。
  - **命坐文昌**：命宫...
    """
    
    original_text: str = """- 分字分词释义：

  - **巨日拱命**：巨门与太阳拱照命宫，主聪慧、声名与表达力。
  - **禄权科合**：禄星、权星与科星同会，主功名、权位与实际俸禄兼具。
  - **命坐文昌**：命宫坐文昌星，主儒雅多才、文采出众。
  - **天同正遇机梁**：天同星正遇天机、天梁，主宽厚调和、福泽深长。
  - **大限劫地**：大限行至地劫所在宫位，主虚耗与结构被抽空。
  - **空杀交并**：空亡与杀星在同一限运中重叠，主机会落空与灾祸并至。
  - **阴男土五局**：子羽命盘的五行局数，土五局主厚重儒雅。

- **原文（source_text）**：  
  子羽之命。阴男土五局。此为寅有巨日，立命申垣，又合禄权、科合，左右，寅子二方照拱，命坐文昌，故主儒雅。秘云：天同正遇机梁宿，左辅扶持福不轻。直大限劫地，小限空杀交并死。

- **规范化释义（primary_lang_explained）**：  
  子羽命为阴男土五局，「寅有巨日，立命申垣」大致可理解为巨门与太阳在寅方拱照申宫命垣，配合禄权、科星与左右同会，命坐文昌，为「巨日拱命、禄权科合、左右夹命、文昌临垣」的复合文贵结构。此类格局多主人品端方、儒雅多才，兼具科第与仕途潜力。秘文又言「天同正遇机梁宿，左辅扶持福不轻」，进一步强调天同、机梁与左辅等星曜对其福泽与温厚气质的加持。  
  然而，行运至大限地劫之地，小限又逢空杀交并，虚耗与杀伐之气叠加，一方面象征现实中机会与支撑被抽空，另一方面也暗示身体与气数在短时间内遭到剧烈冲击，遂于该阶段死亡。此命例呈现的是「儒雅文士、结构佳而终败于空劫杀曜重叠之运」的格局。

- **完整对等诠释（secondary_lang_full）**：  
  Ziyu’s chart is that of a Yin Earth native in the Fifth Configuration. The phrase "Ju and Sun present in Yin, with Life set in Shen" suggests a pattern where Ju Men and the Sun in Yin beam towards the Life palace in Shen. Combined with Lu and Quan, academic Ke, Left and Right Assistants and Wen Chang at the Life position, this forms a layered literary noble structure: intellectual ability, examination merit and official prospects all converging. The secret text adds that Tian Tong properly meets Ji and Liang, with Zuo Fu supporting—stars that further accent a gentle, cultivated temperament and steady blessings.  
  Nonetheless, when the major period reaches the region of Di Jie and the minor period simultaneously encounters Kong and Sha, void and killing influences intertwine. In lived terms this speaks to support structures being hollowed out, opportunities turning to nothing and the body being subject to sharp strain, leading to death in that span. The example depicts a refined scholar‑official whose well‑formed pattern is ultimately undone by a convergence of void‑and‑killing transits.

- **核心要点**：  
  1. 巨日拱命、禄权科合、左右夹命、文昌临垣，配合天同机梁与左辅，是标准儒雅文士与科名仕途格。  
  2. 命主体性温厚、多才多艺，兼具读书人气质与官场发展潜能。  
  3. 行至大限劫地、小限空杀交并之运，虚耗与杀伐叠加，终致死亡。

- **叙事素材（narrative_snippets）**：
  - **巨日文昌**："此为寅有巨日，立命申垣，又合禄权、科合，左右，寅子二方照拱，命坐文昌，故主儒雅"，巨日拱命配文昌，使子羽命主温文儒雅、才学出众。
  - **同梁左辅**："秘云：天同正遇机梁宿，左辅扶持福不轻"，天同机梁与左辅同会，增加其宽厚、调和与福泽。
  - **劫地空杀**："直大限劫地，小限空杀交并死"，大限地劫加小限空杀交并，为结构被抽空与杀伐叠加的致命年份。
  - **现代应用**：对典型「文贵儒士」命局而言，在现实支撑（工作平台、人际网络、健康基础）被削弱且空杀叠加的年份，要格外警惕不要同时在事业与情绪上过度消耗自己，以免整体结构在短时间内崩塌。"""
    normalized_text_zh: str = """"""
    subject: str = "子羽之命"
    factor_refs: list = ['pattern_juri_gongming', 'pattern_luquanke_he', 'pattern_mingzuo_wenchang', 'pattern_tiantongjiliang', 'timing_daxian_jiedi', 'malefic_kongsha_jiaobing']
    
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
        l1_anchor="zw_v1.0.0_子羽之命_001_L1",
    )
    version: str = "1.0.0"
