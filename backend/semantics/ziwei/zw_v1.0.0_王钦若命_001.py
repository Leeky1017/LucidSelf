"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699443
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
    semantic_id="zw_v1.0.0_王钦若命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 王钦若命(SemanticEntry):
    """
    - 分字分词释义：

  - **科权禄拱**：科星、权星、禄星三吉同拱命宫，主高位文臣。
  - **左辅右彼**：左辅右彼拱照命宫，主贵人扶持。
  - **尊居八位**：居于受尊重的高位，为富贵...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权禄拱**：科星、权星、禄星三吉同拱命宫，主高位文臣。
  - **左辅右彼**：左辅右彼拱照命宫，主贵人扶持。
  - **尊居八位**：居于受尊重的高位，为富贵双全之命。
  - **大小二限入地网**：大限与小限同时行入天罗地网之地，主凶险。
  - **擎羊冲命**：擎羊冲照命宫，对酉人尤为不利。
  - **凶捐寿**：位高权重而寿不尽的结果。
  - **阴男水二局**：王钦若命盘的五行局数，水二局主智慧权谋。

- **原文（source_text）**：  
  王钦若命。阴男水二局。科权禄拱，文学声杨，左辅右弼，尊居八位，富贵双全之命。大小二限入地网，又遇擎羊，酉人忌之，必凶捐寿。

- **规范化释义（primary_lang_explained）**：  
  王钦若命为阴男水二局，命宫得科、权、禄三吉同拱，再加左辅、右弼扶持，是典型「科权禄拱、贵辅朝垣」的高位文臣格局。原文称其「文学声扬，尊居八位，富贵双全」，说明其以学问与政务才能著称，既有名誉又有实际权力与财富。  
  然而，此命亦隐藏寿命上的软肋：大小二限先后入天罗地网之地，又遇擎羊等杀星，使原本稳固的官贵格局在特定阶段承受极大压力。对酉年生人而言，此类组合尤为不利，一旦应于权力斗争、政局剧变或身体重疾之年，往往形成「位高而寿不永」的结局。原文以「必凶捐寿」收束，点出此类高位文臣命在中后期仍难完全逃开倒寿之风险。

- **完整对等诠释（secondary_lang_full）**：  
  Wang Qinruo’s chart is that of a Yin Water native whose Life palace is flanked by the trio of Ke, Quan and Lu, with Left and Right Assistants in attendance. This "Ke‑Quan‑Lu" pattern, backed by noble helpers, is a classic signature of high‑ranking civil ministers whose reputation rests on learning and administrative skill. The text describes him as possessing both fame and substance, seated among the "eight ranks" of respected officials.  
  Yet the same chart carries a structural weakness in terms of longevity. Both major and minor periods eventually enter the Net of Heaven and Earth while meeting the cutting star Yang Blade. For natives of the You branch this combination is especially fraught, as it often coincides with years of political turbulence, sharp conflict or serious illness. The note that he "surely loses years in misfortune" underlines that even a chart rich in honours and resources can see its lifespan curtailed when heavy malefics converge on fragile timing windows.

- **核心要点**：  
  1. 科权禄拱加左辅右弼，构成高位文臣、富贵双全的典型格局。  
  2. 命局的软肋在于大小二限行入天罗地网并遇擎羊，对酉人尤为不利。  
  3. 此命例展示「位高权重而寿不尽」的结构：荣华可期，长寿未必。

- **叙事素材（narrative_snippets）**：
  - **科权禄拱**："科权禄拱，文学声杨，左辅右弼，尊居八位，富贵双全之命"，王钦若命主以文章与权力并重，位极人臣。
  - **地网擎羊**："大小二限入地网，又遇擎羊，酉人忌之"，地网加擎羊冲命，为高位文臣在特定年份的致命破口。
  - **凶捐其寿**：原文以"必凶捐寿"收束，点出在极佳贵格之下，寿命仍可能被集中压缩在某一阶段。
  - **现代应用**：身在权力核心、尤其出身酉支者，在地网限运遇擎羊冲命之年，宜及早规划权力交接与退休轨迹，避免因政争或健康危机而被迫“交命”。"""
    normalized_text_zh: str = """"""
    subject: str = "王钦若命"
    factor_refs: list = ['pattern_kequanlu_gong', 'pattern_zuofu_youbi', 'metaphor_zunju_bawei', 'timing_daxiao_diwang', 'malefic_qingyang_chongming', 'taboo_youren_jizhi']
    
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
        l1_anchor="zw_v1.0.0_王钦若命_001_L1",
    )
    version: str = "1.0.0"
