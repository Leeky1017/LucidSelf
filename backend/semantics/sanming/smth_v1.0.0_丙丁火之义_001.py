"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227935
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
    semantic_id="smth_v1.0.0_丙丁火之义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙丁火之义(SemanticEntry):
    """
    - **原文（source_text）**：
  丙丁其位，火，行夏之令，丙乃阳上而阴下，阴内而阳外。阳丁其强，适能与阴气相丁。又云：丙，炳也，万物皆炳然著见而强大。

- **分字分词释义**：
 ...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙丁其位，火，行夏之令，丙乃阳上而阴下，阴内而阳外。阳丁其强，适能与阴气相丁。又云：丙，炳也，万物皆炳然著见而强大。

- **分字分词释义**：
  - **行夏之令**：主管夏季的时令。
  - **阳上而阴下**：阳气在上，阴气在下。
  - **阴内而阳外**：阴气在内，阳气在外。
  - **阳丁其强**：阳气到丁时最强。
  - **相丁**：相遇、相抵。
  - **炳然**：光明显著的样子。
  - **著见**：显著可见。

- **规范化释义（primary_lang_explained）**：
  丙丁的位置属火，主管夏季的时令。丙是阳气在上阴气在下，阴气在内阳气在外。到了丁时，阳气正强盛，恰好能与阴气相遇抗衡。又说：丙就是"炳"，万物都光明显著、强盛可见。

- **完整对等诠释（secondary_lang_full）**：
  Bing and Ding occupy the Fire position, commanding Summer's decree. Bing represents yang qi above with yin qi below, yin qi within and yang qi without. When yang reaches Ding, it is at peak strength, precisely able to meet and counterbalance yin qi. It is also said: Bing means "brilliant"—myriad things become brightly manifest and robust.

- **核心要点**：
  - 丙丁属火，主夏季
  - 丙火：阳上阴下，阴内阳外
  - 丁火：阳气最强，与阴气相抵
  - 丙为"炳"，万物炳然著见

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_150]` `[trigger: 丙丁火之义]` `[factor_trigger: bing_fire AND ding_fire AND element_fire]` `[role: 主干]` 丙乃阳上而阴下，阴内而阳外。阳丁其强，适能与阴气相丁。丙，炳也，万物皆炳然著见而强大。 → 《三命通会》卷一#丙丁火之义

- **详细解说**：
  此条详解丙丁火之义。丙火为阳火，夏初之时阳气上升到顶端，阴气在下方，阳气展现于外而阴气藏于内，如同正午烈日炽盛。丁火为阴火，阳气发展到最强盛的阶段，恰好能与开始萌动的阴气相遇抗衡，如同午后阳极阴生的转折点。"丙，炳也"从字义训诂，"炳"指光明显著，形容万物在夏日阳光下都显得明亮、强壮、可见。这体现了丙丁火从炽盛（丙）到阳极（丁）的两个阶段，对应夏季由盛转极的过程。

- **校勘与字词辨析（双语）**：
  - **中文**："炳然"形容光明显著。"相丁"的"丁"指遇、抵。"阳丁其强"表示阳气到丁位时最强盛。
  - **English**: "炳然" (brilliant) describes bright and manifest; "相丁" means "to meet/counterbalance"; "yang at Ding peak" indicates yang qi reaches maximum strength at Ding position."""
    normalized_text_zh: str = """"""
    subject: str = "丙丁火之义"
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
        l1_anchor="smth_v1.0.0_丙丁火之义_001_L1",
    )
    version: str = "1.0.0"
