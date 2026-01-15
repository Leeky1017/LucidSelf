"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699949
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
    semantic_id="zw_v1.0.0_富商之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 富商之命(SemanticEntry):
    """
    - 分字分词释义：

  - **科权迭守身命**：科星与权星多重守照命身，本应贵显。
  - **陀罗破局**：陀罗星破坏原有格局结构，贵气受阻。
  - **天府武曲居财帛**：天府与武曲同守财帛...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权迭守身命**：科星与权星多重守照命身，本应贵显。
  - **陀罗破局**：陀罗星破坏原有格局结构，贵气受阻。
  - **天府武曲居财帛**：天府与武曲同守财帛宫，最理想的财星配置。
  - **才入才卿**：财星落入财帛宫，形成财富归位的理想结构。
  - **破军居迁移**：破军星居迁移宫，主奔波劳碌。
  - **不免劳力**：财富需要通过劳动与奔波获取。
  - **阳男金四局**：富商命盘的五行局数，金四局主刚断经商。

- **原文（source_text）**：  
  富商之命。阳男金四局。此科权迭守身命，但嫌陀罗破局，是以不贵。喜天府、武曲居才帛，是谓才入才卿，其富宜矣。但破军居迁移，不免劳力耳。

- **规范化释义（primary_lang_explained）**：  
  富商命为阳男金四局，「科权迭守身命」说明科星与权星多重守照命身，本来是极有可能贵显的高配结构。然而「但嫌陀罗破局」，陀罗星破坏了原有的清贵格局，使得科权之气不能转化成正式官阶，只好导向商业与财富领域。「天府、武曲居财帛」，说明财帛宫由天府与武曲两大财星同守，是「才入才卿」——财星归位于财帛宫——的理想配置，因此命主能在财富上取得极大成功。但「破军居迁移」预示着命主虽富，却需要奔波劳碌。整体命例展示「科权不贵、财星得位 → 以商致富」的路径。

- **完整对等诠释（secondary_lang_full）**：  
  This "Wealthy Merchant" chart for a Yang Metal native has Ke and Quan repeatedly guarding Life and Body—a structure that, unobstructed, would point to high rank. However, Tuo Luo "breaks" the pattern, blocking translation into official status. Instead, the blessing flows into wealth: Tian Fu and Wu Qu together occupy the Wealth palace, forming the ideal "stars of wealth in the palace of wealth." Po Jun in Migration hints that fortune is not earned in comfort: movement and exertion are constant themes.

- **核心要点**：  
  1. 科权迭守但陀罗破局，科名无法转化为官阶，资源向财富领域倾斜。  
  2. 天府武曲居财帛，是「才入才卿」的理想结构，主大富。  
  3. 破军居迁移，富而劳碌，需在奔波中经营财富。"""
    normalized_text_zh: str = """"""
    subject: str = "富商之命"
    factor_refs: list = ['pattern_kequan_dieshou', 'malefic_tuoluo_poju', 'pattern_tianfu_wuqu_caibo', 'quality_cai_ru_caiqing', 'star_pojun_qianyi', 'quality_bumian_laoli']
    
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
        l1_anchor="zw_v1.0.0_富商之命_001_L1",
    )
    version: str = "1.0.0"
