"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228310
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
    semantic_id="smth_v1.0.0_丁卯火性质_炉烟之火喜巽地及秋冬_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丁卯火性质炉烟之火喜巽地及秋冬(SemanticEntry):
    """
    - **原文（source_text）**：
  丁卯火、为炉烟喜巽地及秋冬，平头截路悬针。

- **分字分词释义**：
  - **炉烟**：炉中的烟。
  - **巽地**：东南方。
  - *...
    """
    
    original_text: str = """- **原文（source_text）**：
  丁卯火、为炉烟喜巽地及秋冬，平头截路悬针。

- **分字分词释义**：
  - **炉烟**：炉中的烟。
  - **巽地**：东南方。
  - **秋冬**：秋季和冬季。
  - **截路**：截路煞，凶煞名。

- **规范化释义（primary_lang_explained）**：
  丁卯火，是炉中烟火，喜欢东南方以及秋冬季节，忌讳平头煞、截路煞、悬针煞。

- **完整对等诠释（secondary_lang_full）**：
  Dingmao Fire is furnace smoke fire, favoring southeastern direction and autumn-winter seasons, avoiding Level-Head sha, Road-Blocking sha, and Suspended-Needle sha.

- **核心要点**：
  - 丁卯为炉中火，如炉烟
  - 喜巽地（东南）、秋冬
  - 忌平头、截路、悬针

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_198]` `[trigger: 丁卯火性质]` `[factor_trigger: dingmao_fire_smoke AND favor_southeast_autumn_winter AND road_blocking_sha]` `[role: 主干]` 丁卯火、为炉烟喜巽地及秋冬，平头截路悬针。 → 《三命通会》卷一#丁卯火性质

- **详细解说**：
  此条解释丁卯（炉中火）的性质。丁卯纳音也是火，但如炉中升起的烟，喜欢东南方（巽位属风，风助火势），喜欢秋冬（显其用），但忌讳平头煞、截路煞、悬针煞等凶煞。炉烟需要风向配合才能不被压抑。

- **校勘与字词辨析（双语）**：
  - **中文**："炉烟"指炉火产生的烟。"巽地"指东南方，八卦巽位属风。"截路"为截路煞，阻碍前程。
  - **English**: "Furnace smoke" refers to smoke from furnace fire. "Southeastern direction" refers to Xun position in Eight Trigrams, belonging to Wind. "Road-Blocking" is Road-Blocking sha, obstructing advancement."""
    normalized_text_zh: str = """"""
    subject: str = "丁卯火性质：炉烟之火喜巽地及秋冬"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_丁卯火性质_炉烟之火喜巽地及秋冬_001_L1",
    )
    version: str = "1.0.0"
