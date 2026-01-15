"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699789
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
    semantic_id="zw_v1.0.0_武安王命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 武安王命(SemanticEntry):
    """
    - 分字分词释义：

  - **杀破廉贞**：七杀、破军、廉贞诸星成格，主武职与强势手段。
  - **俱作恶庙而不陷**：诸星皆在恶庙位置但不陷落，仍具强烈能量。
  - **宜掌三军科权**：掌...
    """
    
    original_text: str = """- 分字分词释义：

  - **杀破廉贞**：七杀、破军、廉贞诸星成格，主武职与强势手段。
  - **俱作恶庙而不陷**：诸星皆在恶庙位置但不陷落，仍具强烈能量。
  - **宜掌三军科权**：掌握军权并得科权相辅，主武贵。
  - **贪狼羊刃加临**：贪狼与羊刃同来，主欲望与危险冲动。
  - **午生人有忌**：午年/时生人在午限行运时易触发禁忌与风险。
  - **小限遇刑忌**：小限遇到刑星与忌星，主冲突与损耗。
  - **阳男金四局**：武安王命盘的五行局数，金四局主刚断武贵。

- **原文（source_text）**：  
  武安王命。阳男金四局。杀破廉贞，俱作恶庙而不陷，宜掌三军科权，左右加会，为武职。峥嵘，终嫌贪狼羊刃加临，又大限到午，午生人有忌，小限遇刑忌，卒至凶亡。

- **规范化释义（primary_lang_explained）**：  
  武安王命为阳男金四局，「杀破廉贞」诸星皆在恶庙而不陷，形成强烈的武职星群，适合掌兵权与刚猛之职；再得科权与左右加会，是「掌三军科权、左右扶持」的武贵格，故以「武安王」名之，象征威武而能安边。  
  然而命局终嫌贪狼与羊刃加临，显示贪欲、冲动与锋芒叠加；当大限行至午位，对午生人尤其不利，小限又遇刑星与忌星，是「贪狼羊刃 + 午限忌 + 刑忌同来」的重凶组合。此时权力、锋芒与冲动同被放大，防线薄弱，遂致凶亡。

- **完整对等诠释（secondary_lang_full）**：  
  Wu An Wang’s chart is that of a Yang Metal native in the Fourth Configuration. Sha, Po and Lian Zhen occupy "malefic temples" without falling, giving a powerful martial cluster. With Ke and Quan assisting and Zuo‑You adding support, the pattern suits command of armies and high military office, hence the title "King of Martial Peace"—one who subdues through arms.  
  Yet the chart "ultimately suffers" from Tan Lang and Yang Ren overlaying, bringing desire, risk‑taking and sharp aggression. When the major period reaches Wu—a problematic position for natives born in Wu—and the minor period coincides with Xing and Ji stars, the configuration "Tan‑Yang overlay + Wu‑limit taboo + Xing‑Ji together" arises. Under such conditions the same qualities that grant military success become channels for downfall, leading to a violent death. The case portrays the classic danger of high martial power under volatile transits.

- **核心要点**：  
  1. 杀破廉贞在恶庙不陷，配科权与左右，为典型武安之格。  
  2. 贪狼羊刃加临，大限午位、小限刑忌同来，使锋芒与危险一并放大。  
  3. 命例展现「武功卓著而终因锋芒与凶限叠加致死」的武职命局。"""
    normalized_text_zh: str = """"""
    subject: str = "武安王命"
    factor_refs: list = ['pattern_shapo_lianzhen', 'quality_emiao_buchen', 'pattern_zhang_sanjun_kequan', 'malefic_tanlang_yangren', 'timing_wusheng_youji', 'timing_xiaoxian_xingji']
    
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
        l1_anchor="zw_v1.0.0_武安王命_001_L1",
    )
    version: str = "1.0.0"
