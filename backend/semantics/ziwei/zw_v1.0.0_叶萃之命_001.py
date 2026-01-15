"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699595
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
    semantic_id="zw_v1.0.0_叶萃之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 叶萃之命(SemanticEntry):
    """
    - 分字分词释义：

  - **机月同梁之格**：天机、太阴、天同、天梁成组合，主聪慧细腻、讲理持平。
  - **一生吏业峙嵘**：在仕途与吏治方面颇有建树。
  - **大限夹地**：大限行至受...
    """
    
    original_text: str = """- 分字分词释义：

  - **机月同梁之格**：天机、太阴、天同、天梁成组合，主聪慧细腻、讲理持平。
  - **一生吏业峙嵘**：在仕途与吏治方面颇有建树。
  - **大限夹地**：大限行至受地劫或地网夹困之地。
  - **太岁埋蛇**：太岁带埋蛇之象，主暗伏危机与缠绕。
  - **小限丧门忌星为害**：小限逢丧门且忌星并起，主丧煮与制度缠绕。
  - **五十二岁主死**：在夹地、埋蛇、丧门与忌星叠加之年身亡。
  - **阳男水二局**：叶萃命盘的五行局数，水二局主智慧吏治。

- **原文（source_text）**：  
  叶萃之命。阳男水二局。机月同梁之格，一生吏业峥嵘。五十二岁，大限夹地。辛已年，太岁埋蛇，小限丧门，忌星为害，主死。

- **规范化释义（primary_lang_explained）**：  
  叶萃之命为阳男水二局，「机月同梁之格」指天机、太阴、天同、天梁等星曜成组合，多主聪慧细腻、讲理持平，适宜吏治与行政工作，故「一生吏业峥嵘」，在仕途与吏治方面颇有建树。  
  然而，在五十二岁这一关键节点，大限行至「夹地」之处，可理解为受地劫或地网夹困之地。辛巳年，太岁带「埋蛇」之象，小限又逢丧门，忌星并起，是「地网夹困 + 埋蛇 + 丧门 + 忌星」的重叠结构。一方面象征在制度与环境中受到多重牵制与暗中阻击，另一方面对健康与气数造成巨大消耗，最终于此年身亡。此命例展示了「机月同梁」高明吏治格，在重丧曜与地网合击下难以善终的一面。

- **完整对等诠释（secondary_lang_full）**：  
  Ye Cui’s chart is that of a Yang Water native in the Second Configuration, featuring the "Ji‑Yue‑Tong‑Liang" pattern where Tian Ji, the Moon, Tian Tong and Tian Liang form a coherent structure. This combination favours intelligence, sensitivity, fairness and administrative talent—hence the phrase "a lifetime of outstanding bureaucratic service." Such a chart suits a career in governance, law or civil administration.  
  At age fifty‑two, however, the major period reaches a "clamped earth" region suggestive of Di Jie or Di Wang‑type entanglement. In the year Xin‑Si, the Annual Tai Sui carries the image of "buried snake," while the minor period encounters Sang Men and other Ji‑type malefics. The resulting pattern—earthly nets, buried snake, funeral stars and忌星—is one of constriction, hidden danger and depletion. Systems and structures that once supported the native now become cages, and the cumulative strain leads to death in that year. The case portrays a highly capable administrator whose life is ultimately overtaken by a convergence of entangling and funerary influences.

- **核心要点**：  
  1. 机月同梁格主聪慧、公正与吏治才能，一生吏业峥嵘。  
  2. 五十二岁大限行夹地，辛巳年太岁埋蛇，小限丧门并起，忌星为害。  
  3. 在地网与丧曜合击下，终于高压环境与虚耗中身亡，是「高明吏治而难免重压折损」的命局示例。

- **叙事素材（narrative_snippets）**：
  - **机月同梁吏格**："机月同梁之格，一生吏业峥嵘"，叶萃命主以聪慧、公正与行政才能见长，是典型吏治型高压命。
  - **夹地埋蛇**："五十二岁，大限夹地。辛已年，太岁埋蛇，小限丧门，忌星为害"，夹地配埋蛇与丧门、忌星，象征制度缠绕与暗伏危机一齐爆发。
  - **中年折损**：中年遇到此类「地网 + 丧曜 + 忌星」叠加，代表人在体制深处承压多年后突然被整体结构反噬。
  - **现代应用**：现代长期身在基层治理、纪检、审计、合规等高压岗位者，若命局类似机月同梁格，在明显「夹地 + 丧曜」年份宜主动调岗或减负，让制度压力不过度集中在自己身上。"""
    normalized_text_zh: str = """"""
    subject: str = "叶萃之命"
    factor_refs: list = ['pattern_jiyuetongliang', 'result_liye_zhengrong', 'timing_daxian_jiadi', 'timing_taisui_maishe', 'malefic_xiaoxian_sangmen', 'malefic_jixing_weihai']
    
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
        l1_anchor="zw_v1.0.0_叶萃之命_001_L1",
    )
    version: str = "1.0.0"
