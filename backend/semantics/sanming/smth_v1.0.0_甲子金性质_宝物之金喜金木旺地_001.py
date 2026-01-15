"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228288
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
    semantic_id="smth_v1.0.0_甲子金性质_宝物之金喜金木旺地_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲子金性质宝物之金喜金木旺地(SemanticEntry):
    """
    - **原文（source_text）**：
  甲子金、为宝物，喜金木旺地进神，喜福星平头，悬针破字。

- **分字分词释义**：
  - **宝物**：珍宝之物。
  - **金木旺地**：金和...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲子金、为宝物，喜金木旺地进神，喜福星平头，悬针破字。

- **分字分词释义**：
  - **宝物**：珍宝之物。
  - **金木旺地**：金和木都旺盛的地方。
  - **进神**：进入旺神之地。
  - **福星**：吉祥之星。
  - **平头**：平头煞，神煞名。
  - **悬针**：悬针煞，神煞名。
  - **破字**：破字煞，神煞名。

- **规范化释义（primary_lang_explained）**：
  甲子金，是宝物之金，喜欢金和木都旺盛的地方以及进神，喜欢遇到福星，不喜欢平头煞、悬针煞、破字煞。

- **完整对等诠释（secondary_lang_full）**：
  Jiazi Metal is precious treasure metal, favoring locations where Metal and Wood both flourish and Advancing Spirit, favoring Fortune Star, avoiding Level-Head sha, Suspended-Needle sha, and Broken-Character sha.

- **核心要点**：
  - 甲子为海中金，如宝物
  - 喜金木旺地、进神
  - 喜福星
  - 忌平头、悬针、破字等煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_195]` `[trigger: 甲子金性质]` `[factor_trigger: jiazi_metal_treasure AND favor_metal_wood_flourish AND advancing_spirit]` `[role: 主干]` 甲子金、为宝物，喜金木旺地进神，喜福星平头，悬针破字。 → 《三命通会》卷一#甲子金性质

- **详细解说**：
  此条解释甲子（海中金）的性质。甲子纳音为金，在海中孕育如宝物，喜欢金木都旺的环境（金旺则本身强，木旺则有财可取），喜进神（从弱到强的转化），喜福星相助。但忌讳平头煞（干支相同）、悬针煞（天干地支相冲）、破字煞（天干地支相破）等凶煞。这是命理实践中判断甲子命格吉凶的依据。

- **校勘与字词辨析（双语）**：
  - **中文**："宝物"指海中金如珠宝。"进神"指五行从衰到旺。"平头、悬针、破字"是命理中的神煞名称，为凶煞。
  - **English**: "Precious treasure" refers to ocean metal like pearls and gems. "Advancing Spirit" means Five Elements transitioning from weak to strong. "Level-Head, Suspended-Needle, Broken-Character" are sha (malevolent spirits) names in fate calculation, considered inauspicious."""
    normalized_text_zh: str = """"""
    subject: str = "甲子金性质：宝物之金喜金木旺地"
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
        l1_anchor="smth_v1.0.0_甲子金性质_宝物之金喜金木旺地_001_L1",
    )
    version: str = "1.0.0"
