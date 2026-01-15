"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699957
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
    semantic_id="zw_v1.0.0_秀才之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 秀才之命(SemanticEntry):
    """
    - 分字分词释义：

  - **破军得地**：破军星落于得力之地，锐气可用。
  - **禄存而解**：禄存星化解焕星锐气，使格局温和可用。
  - **文武双全**：命主兼具文才与武略。
  - ...
    """
    
    original_text: str = """- 分字分词释义：

  - **破军得地**：破军星落于得力之地，锐气可用。
  - **禄存而解**：禄存星化解焕星锐气，使格局温和可用。
  - **文武双全**：命主兼具文才与武略。
  - **火星冲照**：火星从对宫冲照命宫，带来烈性与冲击。
  - **羊陀夹命**：擎羊与陀罗分列命宫两侧，形成凶星夹制。
  - **若非则当大贵**：若非凶星干扰，本可大贵。
  - **阳男水二局**：秀才命盘的五行局数，水二局主智慧文武。

- **原文（source_text）**：  
  秀才之命。阳男水二局。此破军得地之星，喜禄存而解。其狂主人文武双全，三十以上，宜食廪出贡，致富大才耳。若非火星冲照，羊陀夹命，则又当大贵矣。

- **规范化释义（primary_lang_explained）**：  
  秀才命为阳男水二局，「破军得地之星，喜禄存而解」，说明破军虽为煞星，但落于得地之处并有禄存来化解其锐气，形成「煞星得化」的结构。「其狂主人文武双全」，破军的刚猛与原有的文星配合，使命主兼具文才与武略，三十岁以上进入成熟期后，「宜食廪出贡」，可以成为廪生或贡生。然而「若非火星冲照，羊陀夹命，则又当大贵矣」，说明火星冲照与羊陀夹命压制了本可大贵的潜力，使之只能停留在秀才、廪生的层级。

- **完整对等诠释（secondary_lang_full）**：  
  This "Xiucai" chart for a Yang Water native features Po Jun in a favourable sector, softened by Lu Cun. The combination produces a person "of both letters and arms." After thirty, the native is suited to receive stipends and advance as a tribute student. Yet the chart's ceiling is lowered by Huo Xing opposing and Yang‑Tuo flanking the Life palace. Without these malefics, he would have become "greatly noble." As it stands, he remains a talented but contained scholar—stuck at xiucai level.

- **核心要点**：  
  1. 破军得地并有禄存化解，形成文武双全的秀才格。  
  2. 三十岁后进入成熟期，可食廪出贡，致富于学识与才干。  
  3. 火星冲照、羊陀夹命，限制了本可大贵的上限，止步中层功名。"""
    normalized_text_zh: str = """"""
    subject: str = "秀才之命"
    factor_refs: list = ['star_pojun_dedi', 'pattern_lucun_erjie', 'quality_wenwu_shuangquan', 'malefic_huoxing_chongzhao', 'malefic_yangtuo_jiaming', 'quality_ruofei_dagui']
    
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
        l1_anchor="zw_v1.0.0_秀才之命_001_L1",
    )
    version: str = "1.0.0"
