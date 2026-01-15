"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042568
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
    semantic_id="smth_v1.0.0_乙木为风_001",
    book_id="sanming",
    engine_id="bazi"
)
class 乙木为风(SemanticEntry):
    """
    - **原文（source_text）**：
  乙木为风。乙木长生在午，败在巳。在午而生者，盖乙为山林活木，至夏来而畅茂，诗所谓「千章夏木青」是也。其败巳云何？巳乃巽地，巽为风，木盛风生也，风生于木...
    """
    
    original_text: str = """- **原文（source_text）**：
  乙木为风。乙木长生在午，败在巳。在午而生者，盖乙为山林活木，至夏来而畅茂，诗所谓「千章夏木青」是也。其败巳云何？巳乃巽地，巽为风，木盛风生也，风生于木而反摧木，犹之火生于木而反焚木，其取败也固宜，所谓乙木为风者，木其所自生云尔。如人乙日建生者，在秋令大吉，秋令金旺，乙木能化能从而盘根错节，非利器无所裁成；逢亥必死，其落叶归根之时耶？

- **分字分词释义**：
  - **乙木为风**：以风喻阴木的柔曲与流动性。
  - **长生在午、败在巳**：午火下活木畅茂，巳风中木反被摧折。
  - **木盛风生而反摧木**：气盛反成自伤，比喻环境过度放大本性而致其败。

- **规范化释义（primary_lang_explained）**：
  乙木多象山林活木、枝叶藤萝，性柔而善动，如风中之木. 夏月午火当令时，乙木得阳光温暖而繁茂，是其长生之地；到巳位，风起于木，风虽由木生，却反过来摧折枝叶，如同火虽由木出，终又焚木。故乙木虽为风象，也最怕风势过盛。乙日生于秋令，金旺之时，反而有利：金如刀剪，使木盘根错节，成材有用；遇亥则为落叶归根之处，气尽而亡。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood is compared to living forest trees and climbing vines, soft yet constantly in motion like branches whipped by the wind. In Wu month, under full summer Fire, this Wood finds the warmth and light it needs to grow luxuriantly: that is its place of long life. In Si, however, the text warns that “Wood is strong, wind is born, yet the wind turns back to break the Wood”: the very movement that arises from Wood’s own nature becomes too fierce and begins to tear at it, just as Fire, originally fed by Wood, can in the end burn its source. Yi‑day charts therefore fear environments of excessive agitation and stimulation even when these look like “following the trend”. When Yi is born in autumn Metal, by contrast, the sharpness of Metal works like a careful pruning tool, helping the Wood take shape and become usable timber; meeting Hai marks the stage of leaves returning to the root and qi spending itself. In practice this passage urges us to see Yi not only as gentle and adaptable, but as highly sensitive to the strength of the surrounding winds: it flourishes when guided and trimmed, and is damaged when left to be thrashed about by uncontrolled forces."""
    normalized_text_zh: str = """"""
    subject: str = "乙木为风"
    factor_refs: list = []
    
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
        l1_anchor="smth_v1.0.0_乙木为风_001_L1",
    )
    version: str = "1.0.0"
