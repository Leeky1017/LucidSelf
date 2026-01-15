"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699865
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
    semantic_id="zw_v1.0.0_常国公命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 常国公命(SemanticEntry):
    """
    - 分字分词释义：

  - **命宫虽无正曜**：命宫内无主星坐守，按常规标准不理想。
  - **三方吉拱**：三方宫位皆有吉星拱照，主格局有基本支撑。
  - **公侯承荫**：因家族为公侯而享...
    """
    
    original_text: str = """- 分字分词释义：

  - **命宫虽无正曜**：命宫内无主星坐守，按常规标准不理想。
  - **三方吉拱**：三方宫位皆有吉星拱照，主格局有基本支撑。
  - **公侯承荫**：因家族为公侯而享有世袭与荫补。
  - **帝胄之命**：具帝室或宗室血统，其命运高度受制度保障。
  - **不必合格**：不必完全符合常规成格标准。
  - **因人而论**：解命时须结合身份与阶层背景，而非一味套格局。
  - **阴男火六局**：常国公命盘的五行局数，火六局主明亮承袭。

- **原文（source_text）**：  
  常国公命。阴男火六局。命宫虽无正曜，但得三方吉拱，富贵必矣。况公侯承荫祖宗，即如帝胄之命，不必合格，但得吉星扶持是矣。故看命数者，又当因人而论。

- **规范化释义（primary_lang_explained）**：  
  常国公命为阴男火六局，命宫本身「无正曜」，按一般斗数标准并非理想；然而三方多吉星拱照，仍主富贵。更关键的是，「公侯承荫祖宗，即如帝胄之命」，说明命主本身出身于公侯乃至帝室旁支，享有极强的世袭与家世加成——这种命局「不必合格」，只要得到吉星扶持，便能享受高贵身份与荣华。  
  原文最后一句「故看命数者，又当因人而论」，点出技术上的重要提醒：对于帝胄、公侯等特权阶层，不能完全照搬普通人命格的成败标准，血统与制度位置本身就是强大的结构因素。此命因此成为「世袭国公」类型的代表。

- **完整对等诠释（secondary_lang_full）**：  
  Chang Guogong’s chart is that of a Yin Fire native in the Sixth Configuration. Although the Life palace "lacks principal stars," the surrounding tri‑palaces are rich in benefics, guaranteeing wealth and rank. More importantly, the text stresses that he "inherits as a duke" and that his fate is "like that of imperial offspring": he does not need to "meet the pattern" in the usual technical sense; as long as benefic stars offer some support, nobility is assured.  
  The closing remark—"those who read fates must also judge according to the person"—is almost a methodological instruction: charts of princes and hereditary nobles cannot be read by the same yardstick as commoners, because institutional privilege, lineage and precedent fundamentally shape their life path. This case thus exemplifies a lineage‑driven destiny rather than an exam‑ or merit‑driven one.

- **核心要点**：  
  1. 命宫无正曜但三方吉拱，配合公侯承荫，使富贵几成既定事实。  
  2. 命例强调「帝胄、公侯命不必合格」，凸显血统与制度加成的力量。  
  3. 原文以「当因人而论」警示术者：解命须结合阶层与背景，而非只看格局。"""
    normalized_text_zh: str = """"""
    subject: str = "常国公命"
    factor_refs: list = ['quality_wuzheng_yao', 'pattern_sanfang_jigong', 'quality_gonghou_chengyin', 'quality_dizhou_zhi_ming', 'principle_bubi_hege', 'principle_yinren_erlun']
    
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
        l1_anchor="zw_v1.0.0_常国公命_001_L1",
    )
    version: str = "1.0.0"
