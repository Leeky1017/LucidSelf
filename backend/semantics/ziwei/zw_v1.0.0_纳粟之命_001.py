"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699933
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
    semantic_id="zw_v1.0.0_纳粟之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 纳粟之命(SemanticEntry):
    """
    - 分字分词释义：

  - **太阳坐命**：太阳星坐守命宫，主光明与权势。
  - **太阴拱照**：太阴星拱照命宫，主财富与阴柔。
  - **日月争耀**：太阳太阴同时对命宫产生强势影响，主富...
    """
    
    original_text: str = """- 分字分词释义：

  - **太阳坐命**：太阳星坐守命宫，主光明与权势。
  - **太阴拱照**：太阴星拱照命宫，主财富与阴柔。
  - **日月争耀**：太阳太阴同时对命宫产生强势影响，主富贵全美。
  - **干化忌**：天干带来化忌之星，主波折与阻滞。
  - **地劫在垣**：地劫同宫，削弱格局根基。
  - **纳粟县佐**：通过捐纳粮食换取县佐之位。
  - **阳男木三局**：纳粟命盘的五行局数，木三局主生发财富。

- **原文（source_text）**：  
  纳粟之命。阳男木三局。太阳坐命，太阴拱照，为日月争耀，富贵全美。但干化忌，虽在辰垣入庙，巳时生人，正旺不合，又逢地劫在垣，故不能大贵而得大富，止于纳粟县佐之位而已。

- **规范化释义（primary_lang_explained）**：  
  纳粟之命为阳男木三局，「太阳坐命，太阴拱照」，日月两大光体形成「日月争耀」的格局，「富贵全美」本应既富且贵。然而「但干化忌」，天干带来化忌之星；「虽在辰垣入庙，巳时生人，正旺不合」，说明虽然某些星曜在辰宫入庙，但对巳时生人而言并不完全契合；「又逢地劫在垣」，地劫同宫进一步削弱格局。最终「故不能大贵而得大富，止于纳粟县佐之位而已」——命主虽不能取得大官大贵，却能以捐纳粟米换取功名，成为县佐（县级副职）。此命例展示「日月争耀被化忌与地劫压制，贵路受阻转向财富型功名」的纳粟路径。

- **完整对等诠释（secondary_lang_full）**：  
  This "Contribution‑Purchase Official" chart for a Yang Wood native has Tai Yang on Life and Tai Yin facing it—"Sun and Moon vying for brilliance," a pattern of double luminaries that normally secures both wealth and status. Yet a Hua Ji transformation interferes; although certain stars are in Chen (their temple), the Si‑hour birth creates a mismatch; and Di Jie sits in the same palace. All these factors cap the nobility path. The native instead becomes wealthy but only attains the position of a county assistant by "contributing grain"—the practice of buying a lower official title through donation.

- **核心要点**：  
  1. 太阳坐命太阴拱照，日月争耀本是富贵全美格局。  
  2. 化忌加地劫在垣，且巳时生人不合，压制了大贵路径。  
  3. 最终以纳粟方式获取县佐之位，呈现「贵路受阻转向捐官」的命理路径。"""
    normalized_text_zh: str = """"""
    subject: str = "纳粟之命"
    factor_refs: list = ['star_taiyang_zuoming', 'star_taiyin_gongzhao', 'pattern_riyue_zhengyao', 'malefic_gan_huaji', 'malefic_dijie_zaiyuan', 'result_nasu_xianzuo']
    
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
        l1_anchor="zw_v1.0.0_纳粟之命_001_L1",
    )
    version: str = "1.0.0"
