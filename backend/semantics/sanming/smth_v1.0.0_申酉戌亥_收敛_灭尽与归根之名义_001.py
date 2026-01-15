"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227614
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
    semantic_id="smth_v1.0.0_申酉戌亥_收敛_灭尽与归根之名义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 申酉戌亥收敛灭尽与归根之名义(SemanticEntry):
    """
    - **原文（source_text）**：
  申者，七月之辰，申阳所为，而己阴至于申，则上下通而人始见，又云：申，身也，言物体皆成。酉者，日入之时，乃阳正中八月也，又云：酉，犹也，万物皆缯缩收敛。...
    """
    
    original_text: str = """- **原文（source_text）**：
  申者，七月之辰，申阳所为，而己阴至于申，则上下通而人始见，又云：申，身也，言物体皆成。酉者，日入之时，乃阳正中八月也，又云：酉，犹也，万物皆缯缩收敛。九月戌，阳未既也，然不能事，潜藏于戌，又云：戌，灭也，万物皆衰灭矣。十月亥，纯阴也，又亥，劾也，言阴气劾杀万物，此地之道也。

- 分字分词释义：
  - **申：身也**：身体既成，主定型与承担；
  - **酉：缯缩收敛**：一切收束、归于紧缩；
  - **戌：灭**：阳尽而灭，象征衰退与终结；
  - **亥：劾**：以阴气劾杀，收拾残余，归于地道。

 - **规范化释义（primary_lang_explained）**：
  申为七月之辰，阳事既成、形体具备，人事进入「有身有责」的阶段；酉则是日入之象，万物紧缩收敛；戌为阳气将尽，表面未全灭，实则已经潜藏，带有终结意味；亥为纯阴之地，以阴气劾杀万物，使一切归于静止与根部。

- **完整对等诠释（secondary_lang_full）**：

  Shen, the seventh month, is where Yang affairs have taken shape: the "body" is formed and responsibilities solidify—one now carries what has been built. You corresponds to sunset; energies contract, assets are gathered in, and activities are pared back. Xu appears while a trace of Yang still remains on the surface, but its force has already retreated inward: it signals decline, closing and withdrawal. Hai is pure Yin, the phase of being called to account and cut back, in which residual forms are dissolved and everything returns to stillness and root. In fate analysis, these four branches describe the late stages of any cycle: from the burden of stewardship and management (Shen), through tightening and conserving (You), to ending and clearing away (Xu), and finally to a deep return and reset (Hai) that prepares the ground for the next turn."""
    normalized_text_zh: str = """"""
    subject: str = "申酉戌亥：收敛、灭尽与归根之名义"
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
        l1_anchor="smth_v1.0.0_申酉戌亥_收敛_灭尽与归根之名义_001_L1",
    )
    version: str = "1.0.0"
