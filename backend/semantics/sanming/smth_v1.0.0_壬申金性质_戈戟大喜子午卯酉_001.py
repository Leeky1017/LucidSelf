"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228350
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
    semantic_id="smth_v1.0.0_壬申金性质_戈戟大喜子午卯酉_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬申金性质戈戟大喜子午卯酉(SemanticEntry):
    """
    - **原文（source_text）**：
  壬申金、戈戟大喜，子午卯酉，平头大败，妨害□哑，破字悬针。

- **分字分词释义**：
  - **戈戟**：兵器戈和戟。
  - **大喜**：非...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬申金、戈戟大喜，子午卯酉，平头大败，妨害□哑，破字悬针。

- **分字分词释义**：
  - **戈戟**：兵器戈和戟。
  - **大喜**：非常喜欢。
  - **子午卯酉**：四正方位。
  - **大败**：大败煞，凶煞名。
  - **妨害**：妨害煞。

- **规范化释义（primary_lang_explained）**：
  壬申金，是戈戟兵器之金，非常喜欢子午卯酉四正方位，忌讳平头煞、大败煞、妨害煞、聋哑煞、破字煞、悬针煞。

- **完整对等诠释（secondary_lang_full）**：
  Renshen Metal is halberd-spear weaponry metal, greatly favoring Zi-Wu-Mao-You four cardinal positions, avoiding Level-Head sha, Great-Defeat sha, Harm sha, Deaf-Mute sha, Broken-Character sha, and Suspended-Needle sha.

- **核心要点**：
  - 壬申为剑锋金，如戈戟
  - 大喜子午卯酉四正
  - 忌多种凶煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_203]` `[trigger: 壬申金性质]` `[factor_trigger: renshen_metal_weapons AND favor_four_cardinals AND great_defeat_sha]` `[role: 主干]` 壬申金、戈戟大喜，子午卯酉，平头大败，妨害□哑，破字悬针。 → 《三命通会》卷一#壬申金性质

- **详细解说**：
  此条解释壬申（剑锋金）的性质。壬申纳音为金，如戈戟兵器，锋利刚强，喜欢子午卯酉四正方位（正位显威），但忌讳平头煞、大败煞、妨害煞、聋哑煞、破字煞、悬针煞等多种凶煞。剑锋金为金之极盛，需要合适的位置才能显威。

- **校勘与字词辨析（双语）**：
  - **中文**："戈戟"为古代兵器，代表刚强锋利。"子午卯酉"为四正方位。"大败"为大败煞，主失败。
  - **English**: "Halberd-spear" are ancient weapons, representing strength and sharpness. "Zi-Wu-Mao-You" are four cardinal positions. "Great-Defeat" is Great-Defeat sha, indicating failure."""
    normalized_text_zh: str = """"""
    subject: str = "壬申金性质：戈戟大喜子午卯酉"
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
        l1_anchor="smth_v1.0.0_壬申金性质_戈戟大喜子午卯酉_001_L1",
    )
    version: str = "1.0.0"
