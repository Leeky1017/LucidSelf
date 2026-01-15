"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227665
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
    semantic_id="smth_v1.0.0_纳音细目_诸金_001",
    book_id="sanming",
    engine_id="bazi"
)
class 纳音细目诸金(SemanticEntry):
    """
    - **原文（source_text）**：
  纳音之法，同类娶妻，隔八生子，律吕相生之法也。甲子，金之仲，同位娶乙丑，隔八下生壬申；金之孟壬申，同位娶癸酉，隔八上生庚辰；金之季庚辰，同位娶辛已，隔...
    """
    
    original_text: str = """- **原文（source_text）**：
  纳音之法，同类娶妻，隔八生子，律吕相生之法也。甲子，金之仲，同位娶乙丑，隔八下生壬申；金之孟壬申，同位娶癸酉，隔八上生庚辰；金之季庚辰，同位娶辛已，隔八下生戊子。火之仲戊子，娶己丑，生丙申；火之孟丙申，娶丁酉，生甲辰；火之季甲辰，娶乙已，生壬子。木之仲如是左行，至于丁已，中吕之宫。五音一终，复自甲午金之仲，娶乙未，隔八生壬寅，一如甲子之法，终于癸亥。自子至于已为阳，故自黄钟至于仲吕皆下生；自午至于亥为阴，故自林钟至于应钟皆上生。夫上下生者，正谓天气下降，地气上升。

- 分字分词释义：
  - **同类娶妻**：同一五行类别之间相配，形成一个律吕系统中的「家族」。
  - **隔八生子**：隔八位再生出新的纳音，模拟律吕相生的节奏变化。
  - **下生/上生**：下生指音律自高而下，象天气下降；上生指自低而上，象地气上升。

- **规范化释义（primary_lang_explained）**：
  本段详细说明纳音在数学和音律上的生成方式：以同一五行为「同类娶妻」，每隔八位生出新的纳音，构成一个循环。金、火、木各有「仲、孟、季」三段，通过娶配与隔八生子的方式排满六十甲子。自子至巳属阳，因此这一段的律吕为「下生」；自午至亥属阴，因此为「上生」，恰好对应「天气下降、地气上升」的象。

- **完整对等诠释（secondary_lang_full）**：

  This subsection looks at the Metal Nayin family as a whole. Within the sixty Jiazi, Metal is divided into three segments—middle, elder and younger—and through "same‑class marriages" and births at the eighth interval these segments generate a chain of related images: Metal in the Sea, Foil Metal, White Wax Metal, Metal in the Sand, Sword‑Edge Metal and Hairpin‑and‑Bracelet Metal. Taken together they sketch a progression from Metal still hidden and unformed, through thin surface plating and metal in the furnace, to hardened tools and weapons, and finally to jewellery and ornament. In destiny reading this means that a "Metal life" can manifest as buried resources, as raw material under refinement, as cutting edge, or as enjoyment and polish at the surface. The interpreter’s work is to see where along this internal Metal spectrum a given Nayin stands, and to read that position together with the whole chart instead of treating all Metal as a single, undifferentiated label."""
    normalized_text_zh: str = """"""
    subject: str = "纳音细目（诸金）"
    factor_refs: list = ['source_ref']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_纳音细目_诸金_001_L1",
    )
    version: str = "1.0.0"
