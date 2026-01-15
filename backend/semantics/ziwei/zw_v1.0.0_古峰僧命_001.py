"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699771
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
    semantic_id="zw_v1.0.0_古峰僧命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 古峰僧命(SemanticEntry):
    """
    - 分字分词释义：

  - **命无正曜**：命宫无主星坐镇，主基础虚弱与依附性强。
  - **酉未宫权禄加会**：权禄于酉未宫加会，主有一定资源与名望。
  - **机梁照命**：天机与天梁照命...
    """
    
    original_text: str = """- 分字分词释义：

  - **命无正曜**：命宫无主星坐镇，主基础虚弱与依附性强。
  - **酉未宫权禄加会**：权禄于酉未宫加会，主有一定资源与名望。
  - **机梁照命**：天机与天梁照命宫，主智慧与清高。
  - **劫空会合**：劫空等星会合于命，主出世倾向或资源虚耗。
  - **岩泉之名**：以山林、岩洞与泉水道场闻名的清修形象。
  - **大限小限重逢天使擎羊**：大限与小限先后行至同一凶地，形成重复触发。
  - **阴男木三局**：古峰僧命盘的五行局数，木三局主清修出世。

- **原文（source_text）**：  
  古峰僧命。阴男木三局。命无正曜，虽有酉未宫权禄加会机梁照命，劫空会合，但主为僧，有岩泉之名。大限行到天使擎羊之地，凶也，小限又重逢在彼，其数安能逃哉？

- **规范化释义（primary_lang_explained）**：  
  古峰僧命为阴男木三局，「命无正曜」指命宫缺少典型主星坐镇，基础较虚；虽有酉未宫权禄加会、机梁照命，并伴随劫空会合，却不以俗世功名为主，而是「但主为僧，有岩泉之名」，多应在山林道场、岩泉之地成名，体现修行与清修之象。  
  当大限行至天使擎羊之地，小限又重逢于彼，是「天使 + 擎羊 + 重逢」的重凶结构：既有制度或因果层面的压力（天使），又有突发冲突与受伤之象（擎羊），且连续两个层级的行运都踩在同一凶点上，原文感叹「其数安能逃哉」，显示几乎难以回避，故命终于此阶段。

- **完整对等诠释（secondary_lang_full）**：  
  The "Gu Feng" monk’s chart is that of a Yin Wood native in the Third Configuration. With "no principal star" in the Life palace, the base is somewhat insubstantial. Yet power and Lu gather in You and Wei, Ji‑Liang shine on the Life, and Kong‑Jie meet; rather than pointing to secular achievement, the text states that he "is chiefly a monk, famed for cliffs and springs," an image of reclusion and practice in mountain temples.  
  When the major period reaches the Tian Shi–Qing Yang region and the minor period again passes through the same place, the combination of official/karma‑type pressure and Blade‑like impact repeats across layers. The exclamation "how could he escape his tally" underscores that this is a near‑inescapable convergence. Death occurs under this configuration. The case presents a recluse monk pattern whose life closes when repeated blows strike the same vulnerable sector.

- **核心要点**：  
  1. 命无正曜但权禄机梁与劫空会合，重在出世修行与山林清修，不以俗功名为主。  
  2. 大限、小限先后行至天使擎羊同一凶地，形成连续重击。  
  3. 命例呈现「清修僧人在同一凶点反复触发下」，难逃其数而终的情形。"""
    normalized_text_zh: str = """"""
    subject: str = "古峰僧命"
    factor_refs: list = ['pattern_ming_wu_zhengyao', 'pattern_youwei_quanlu', 'pattern_jiliang_zhaoming', 'malefic_jiekong_huihe', 'quality_yanquan_zhiming', 'timing_daxian_xiaoxian_chongfeng']
    
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
        l1_anchor="zw_v1.0.0_古峰僧命_001_L1",
    )
    version: str = "1.0.0"
