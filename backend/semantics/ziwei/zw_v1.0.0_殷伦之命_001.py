"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699677
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
    semantic_id="zw_v1.0.0_殷伦之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 殷伦之命(SemanticEntry):
    """
    - 分字分词释义：

  - **府相朝垣**：天府与天相朝向官垣，主高阶官职与财官双美。
  - **科禄昌曲加会**：科星、禄星与昌曲同会，主功名与文才兼备。
  - **财官双美**：财帛与官禄...
    """
    
    original_text: str = """- 分字分词释义：

  - **府相朝垣**：天府与天相朝向官垣，主高阶官职与财官双美。
  - **科禄昌曲加会**：科星、禄星与昌曲同会，主功名与文才兼备。
  - **财官双美**：财帛与官禄二宫皆佳，主一生富贵殷实。
  - **火所天伤之地**：与火性及天伤凶曜同构的宫位，主火性伤害与事故。
  - **小限重逢**：小限再度遇到同一凶地或凶曜，主风险加倍。
  - **太岁地劫为殃**：太岁与地劫同临，主突发损耗与根基被夺。
  - **阳男火六局**：殷伦命盘的五行局数，火六局主热情财官。

- **原文（source_text）**：  
  殷伦之命。阳男火六局。府相朝垣，科禄昌曲加会，财官双美，富贵之命。大限行于火所天伤之地，小限五十三岁，亦重逢。在彼太岁地劫为殃，其死无疑。

- **规范化释义（primary_lang_explained）**：  
  殷伦命为阳男火六局，「府相朝垣」配合科星、禄星、文昌、文曲同会，是「府相朝垣、科禄昌曲加会」之格，一生财官双美，位高而家底殷实。  
  但大限行至「火所天伤之地」，即火性与天伤凶曜交织之宫位，对阳火格局构成强烈消耗；五十三岁小限再度重逢同一凶地，且彼时太岁地劫并起，是「火所天伤 + 重逢 + 地劫」的叠加结构。此组合一方面削弱财官根基，另一方面对身体与生命力造成重击，故于五十三岁死亡。

- **完整对等诠释（secondary_lang_full）**：  
  Yin Lun’s chart is that of a Yang Fire native in the Sixth Configuration. With Fu and Xiang facing the court, and Ke, Lu, Wen Chang and Wen Qu converging, the "Fu‑Xiang with Ke‑Lu‑Chang‑Qu" pattern grants high office and solid wealth—"both wealth and office are excellent."  
  However, the major period moves into a sector described as "the place of Tian Shang associated with fire," where fiery tendencies and the wounding star reinforce one another. At age fifty‑three the minor period again meets this same region, and in that year Tai Sui is accompanied by Di Jie, adding further harm. This triple combination—fire’s Tian Shang, repetition at fifty‑three and Di Jie under Tai Sui—erodes both status and physical vitality, making death in that year virtually certain. The case shows a richly endowed chart whose life ends when repeated wounding‑and‑earth‑robbery influences converge.

- **核心要点**：  
  1. 府相朝垣、科禄昌曲加会，是财官双美、富贵殷实的命格。  
  2. 大限行火所天伤之地，小限于五十三岁重逢，加之太岁地劫为殃。  
  3. 命例呈现「富贵厚重而折于火伤与地劫叠加」的中晚年节点。"""
    normalized_text_zh: str = """"""
    subject: str = "殷伦之命"
    factor_refs: list = ['pattern_fuxiang_chaoyuan', 'pattern_keluchangqu_jiahui', 'quality_caiguan_shuangmei', 'malefic_huosuo_tianshang', 'timing_xiaoxian_chongfeng', 'malefic_taisui_dijie']
    
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
        l1_anchor="zw_v1.0.0_殷伦之命_001_L1",
    )
    version: str = "1.0.0"
