"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228281
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
    semantic_id="smth_v1.0.0_释六十甲子性质吉凶总说_001",
    book_id="sanming",
    engine_id="bazi"
)
class 释六十甲子性质吉凶总说(SemanticEntry):
    """
    - **原文（source_text）**：
  释六十甲子性质吉凶：

- **规范化释义（primary_lang_explained）**：
  解释六十甲子每一个的性质和吉凶：

- **完整...
    """
    
    original_text: str = """- **原文（source_text）**：
  释六十甲子性质吉凶：

- **规范化释义（primary_lang_explained）**：
  解释六十甲子每一个的性质和吉凶：

- **完整对等诠释（secondary_lang_full）**：
  Explaining the nature and auspiciousness-inauspiciousness of each of the Sixty Jiazi:

- **核心要点**：
  - 开始逐一解释六十甲子
  - 每个甲子有其独特性质
  - 详述喜忌与吉凶

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_194]` `[trigger: 六十甲子性质吉凶总说]` `[factor_trigger: sixty_jiazi_detailed AND nature_auspiciousness]` `[role: 主干]` 释六十甲子性质吉凶。 → 《三命通会》卷一#六十甲子性质吉凶总说

- **详细解说**：
  此为章节标题，标明接下来将对六十甲子中的每一个进行详细的性质和吉凶分析。这是命理实践的重要内容，每个甲子纳音都有其特定的喜忌、神煞、格局等，是推断命运的具体依据。"""
    normalized_text_zh: str = """"""
    subject: str = "释六十甲子性质吉凶总说"
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
        l1_anchor="smth_v1.0.0_释六十甲子性质吉凶总说_001_L1",
    )
    version: str = "1.0.0"
