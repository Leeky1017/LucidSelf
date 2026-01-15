"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042702
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
    semantic_id="smth_v1.0.0_亥为悬河_001",
    book_id="sanming",
    engine_id="bazi"
)
class 亥为悬河(SemanticEntry):
    """
    - **原文（source_text）**：
  亥为悬河。天河之水，奔流不回，故曰悬河。亥即天门，又属水，非悬河之象乎？亥年建生，日时见寅、辰二字，是乃水拱雷门。

- **分字分词释义**：
  ...
    """
    
    original_text: str = """- **原文（source_text）**：
  亥为悬河。天河之水，奔流不回，故曰悬河。亥即天门，又属水，非悬河之象乎？亥年建生，日时见寅、辰二字，是乃水拱雷门。

- **分字分词释义**：
  - **悬河**：高处倾泻而下之水，如银河倒挂，喻水势迅猛不返。
  - **天门属水**：亥为天门，属水，统摄众水归向。
  - **水拱雷门**：亥水与寅辰相互呼应，形成水雷相激之象。

- **规范化释义（primary_lang_explained）**：
  亥被比为悬河：如天河之水，自上而下，奔流不回，势大而急。亥为天门，又属水，正合此象。亥年生而日时见寅、辰，如水拱雷门：亥水承接寅木雷门与辰龙宫之气，形成强烈的动能与表达势头。

- **完整对等诠释（secondary_lang_full）**：
  Hai is compared to a suspended river, like the Milky Way pouring down from the sky: water that rushes forward without turning back, its force great and its drop steep. As the heavenly gate and a Water branch, Hai gathers many streams and releases them in a single direction. When a Hai year birth meets Yin and Chen in the day and hour, this is called “water arching around the thunder gate”: Hai Water joins the thunder door of Yin Wood and the dragon palace of Chen Earth, creating a configuration of strong motion and outspoken energy. In life reading, Hai‑as‑suspended‑river marks patterns of large‑scale movement—overseas ventures, mass communication, capital flows, emotional outpourings—that are hard to reverse once set in motion. Its potential is tremendous reach; its danger is that without good banks and valves, what pours out may be lost or overwhelm the structures meant to channel it."""
    normalized_text_zh: str = """"""
    subject: str = "亥为悬河"
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
        l1_anchor="smth_v1.0.0_亥为悬河_001_L1",
    )
    version: str = "1.0.0"
