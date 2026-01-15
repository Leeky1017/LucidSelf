"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228295
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
    semantic_id="smth_v1.0.0_乙丑金性质_顽矿之金喜火及南方_001",
    book_id="sanming",
    engine_id="bazi"
)
class 乙丑金性质顽矿之金喜火及南方(SemanticEntry):
    """
    - **原文（source_text）**：
  乙丑金、为顽矿，喜火及南方日时，福星华盖正印。

- **分字分词释义**：
  - **顽矿**：顽固的矿石。
  - **喜火及南方**：喜欢火以...
    """
    
    original_text: str = """- **原文（source_text）**：
  乙丑金、为顽矿，喜火及南方日时，福星华盖正印。

- **分字分词释义**：
  - **顽矿**：顽固的矿石。
  - **喜火及南方**：喜欢火以及南方。
  - **日时**：日柱和时柱。
  - **华盖**：华盖星，神煞名。
  - **正印**：正印格，格局名。

- **规范化释义（primary_lang_explained）**：
  乙丑金，是顽固的矿石之金，喜欢火以及南方的日柱和时柱，有福星、华盖星、正印格则吉。

- **完整对等诠释（secondary_lang_full）**：
  Yichou Metal is stubborn ore metal, favoring Fire and southern Day-Hour pillars, auspicious with Fortune Star, Canopy Star, and Proper Seal pattern.

- **核心要点**：
  - 乙丑为海中金，如顽矿
  - 喜火炼、南方暖
  - 喜福星、华盖、正印
  - 需火来锻炼成器

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_196]` `[trigger: 乙丑金性质]` `[factor_trigger: yichou_metal_ore AND favor_fire_south AND canopy_star]` `[role: 主干]` 乙丑金、为顽矿，喜火及南方日时，福星华盖正印。 → 《三命通会》卷一#乙丑金性质

- **详细解说**：
  此条解释乙丑（海中金）的性质。乙丑纳音也是金，但如顽固的矿石，未经锻炼，所以喜欢遇到火来冶炼（火克金反而成器），喜欢南方（火旺之地）的日时配合，遇到福星、华盖星（孤高清贵之星）、正印格（生我之神）则吉。与甲子金不同，乙丑金更需要火的锻炼才能成器。

- **校勘与字词辨析（双语）**：
  - **中文**："顽矿"指未经冶炼的矿石。"南方"属火。"华盖"为孤高清贵之星。"正印"为生我之格局，主文贵。
  - **English**: "Stubborn ore" refers to unrefined mineral. "South" belongs to Fire. "Canopy" is star of lofty solitude and nobility. "Proper Seal" is pattern of what generates me, indicating literary honor."""
    normalized_text_zh: str = """"""
    subject: str = "乙丑金性质：顽矿之金喜火及南方"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_乙丑金性质_顽矿之金喜火及南方_001_L1",
    )
    version: str = "1.0.0"
