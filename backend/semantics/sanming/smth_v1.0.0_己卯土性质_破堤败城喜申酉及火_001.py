"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228406
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
    semantic_id="smth_v1.0.0_己卯土性质_破堤败城喜申酉及火_001",
    book_id="sanming",
    engine_id="bazi"
)
class 己卯土性质破堤败城喜申酉及火(SemanticEntry):
    """
    - **原文（source_text）**：
  己卯土，破堤败城，喜申酉及火进神短夭。九丑阙字曲脚悬针。

- **分字分词释义**：
  - **破堤败城**：破损的堤坝败坏的城墙。
  - **...
    """
    
    original_text: str = """- **原文（source_text）**：
  己卯土，破堤败城，喜申酉及火进神短夭。九丑阙字曲脚悬针。

- **分字分词释义**：
  - **破堤败城**：破损的堤坝败坏的城墙。
  - **喜申酉及火**：喜欢申酉和火。
  - **进神**：进神吉神。
  - **短夭**：短夭煞。
  - **九丑**：九丑煞。

- **规范化释义（primary_lang_explained）**：
  己卯土，是破损的堤坝败坏的城墙，喜欢申酉和火，有进神则吉，遇短夭煞、九丑煞、阙字煞、曲脚煞、悬针煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Jimao Earth is broken dike-ruined rampart earth, favoring Shen-You and Fire, auspicious with Advancing Spirit, inauspicious with Short-Life sha, Nine-Ugly sha, Gap-Character sha, Curved-Foot sha, and Suspended-Needle sha.

- **核心要点**：
  - 己卯为城头土，如破堤败城
  - 喜申酉（金修补）、火（重生）
  - 喜进神
  - 忌多种凶煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_210]` `[trigger: 己卯土性质]` `[factor_trigger: jimao_earth_ruined AND favor_shen_you_fire AND advancing_spirit]` `[role: 主干]` 己卯土，破堤败城，喜申酉及火进神短夭。九丑阙字曲脚悬针。 → 《三命通会》卷一#己卯土性质

- **详细解说**：
  此条解释己卯（城头土）的性质。己卯纳音也是土，但如破损的堤坝败坏的城墙，需要修复，喜欢申酉（金可以修补加固）和火（火生土重生），有进神则吉，但忌短夭煞、九丑煞、阙字煞、曲脚煞、悬针煞等多种凶煞。破败之土需要修复才能重新发挥作用。

- **校勘与字词辨析（双语）**：
  - **中文**："破堤败城"指破损败坏的土建工程。"申酉"属金，可修补。"九丑"为九丑煞，大凶。
  - **English**: "Broken dike-ruined rampart" refers to damaged earthworks. "Shen-You" belong to Metal, can repair. "Nine-Ugly" is Nine-Ugly sha, extremely inauspicious."""
    normalized_text_zh: str = """"""
    subject: str = "己卯土性质：破堤败城喜申酉及火"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_己卯土性质_破堤败城喜申酉及火_001_L1",
    )
    version: str = "1.0.0"
