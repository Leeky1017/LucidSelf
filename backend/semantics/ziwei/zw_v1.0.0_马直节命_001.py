"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699612
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
    semantic_id="zw_v1.0.0_马直节命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 马直节命(SemanticEntry):
    """
    - 分字分词释义：

  - **巨日拱照**：巨门与太阳同向拱照命宫，主光彩、名声与表达力。
  - **明禄暗禄**：明显俸禄与隐性收入并存的配置，主资源丰厚。
  - **天伤**：主病伤、损害...
    """
    
    original_text: str = """- 分字分词释义：

  - **巨日拱照**：巨门与太阳同向拱照命宫，主光彩、名声与表达力。
  - **明禄暗禄**：明显俸禄与隐性收入并存的配置，主资源丰厚。
  - **天伤**：主病伤、损害与身体创伤的凶星。
  - **小限冲命垣**：小限与命宫形成对冲，主命身承压与冲击。
  - **太岁天罗**：太岁行于天罗之位，主缠绕、困顿与难解之局。
  - **病符作恙**：病符星发动，主疾病缠身与健康危机。
  - **阳男水二局**：马直节命盘的五行局数，水二局主智慧刚正。

- **原文（source_text）**：  
  马直节命。阳男水二局。巨日拱照，明禄暗禄，允为富贵。四十七岁，大限到于天伤，小限冲命垣，太岁天罗，病符作恙，故死于是年已。

- **规范化释义（primary_lang_explained）**：  
  马直节命为阳男水二局，巨门与太阳拱照命宫，明禄与暗禄同来，既有表面俸禄也有隐性资源，「允为富贵」，是一生富贵稳固的结构。命主名中「直节」亦对应其性格刚直不屈的特征。  
  四十七岁时，大限行至天伤所在之地，小限又冲命垣，太岁行天罗并带病符之象，是「天伤 + 命冲 + 天罗病符」的组合。此时身体、气血与整体状态承受巨大压力，既有病象亦有缠绕与阻隔，最终死于该年。命例展示「富贵稳定而中年折于病伤与天罗之运」的轨迹。

- **完整对等诠释（secondary_lang_full）**：  
  Ma Zhijie’s chart is that of a Yang Water native in the Second Configuration. Ju Men and the Sun beam on the Life palace, with both visible and hidden Lu—"bright Lu and dark Lu"—indicating formal stipends as well as less visible resources. The chart supports a life of solid wealth and standing, fitting the name "Zhijie" (upright integrity).  
  At forty‑seven, however, the major period reaches the star Tian Shang, the minor period冲s the Life palace, and the Annual Tai Sui occupies the Celestial Net while disease‑related indicators arise. This blend of Tian Shang,冲 to Life, Tian Luo and illness signs suggests that health and vitality are deeply compromised under a net of constraints and afflictions, leading to death in that year. The case illustrates a steady, affluent life that is nonetheless curtailed by a midlife convergence of injurious and entangling influences.

- **核心要点**：  
  1. 巨日拱照配合明禄暗禄，是稳健富贵结构。  
  2. 四十七岁大限天伤、小限冲命垣、太岁天罗加病符，构成病伤与缠绕叠加的中年高危年份。  
  3. 命例体现「富贵而中年因病与结构性压力而亡」。

- **叙事素材（narrative_snippets）**：
  - **明禄暗禄**："巨日拱照，明禄暗禄，允为富贵"，明暗双禄，使马直节命主既有明面俸禄，又有隐性资源与支持。
  - **病伤重年**："四十七岁，大限到于天伤，小限冲命垣，太岁天罗，病符作恙"，天伤配天罗与病符，标记身体与气数被多重因素缠绕之年。
  - **中年折寿**：富贵格局本可长享，但在四十七岁遭遇天伤、天罗与病符合击，生命被提前截断。
  - **现代应用**：对事业稳健、资源丰厚的人而言，在明显「天伤 + 天罗 + 病符」年份，要把体检、慢性病管理与减压看作刚需，而非可选项，避免因长期透支在一个节点集中爆发。"""
    normalized_text_zh: str = """"""
    subject: str = "马直节命"
    factor_refs: list = ['pattern_juri_gongzhao', 'pattern_minglu_anlu', 'malefic_tianshang', 'timing_xiaoxian_chong', 'timing_taisui_tianluo', 'malefic_bingfu_zuoyang']
    
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
        l1_anchor="zw_v1.0.0_马直节命_001_L1",
    )
    version: str = "1.0.0"
