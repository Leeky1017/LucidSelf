"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227642
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
    semantic_id="smth_v1.0.0_干支合而纳音生_001",
    book_id="sanming",
    engine_id="bazi"
)
class 干支合而纳音生(SemanticEntry):
    """
    - **原文（source_text）**：
  数之所合，变之所由出也。乾为天，坤为地，乾坤合而为泰；德为父，红为母，德红合而为东；干为君，支为臣，干支合而纳音生。是故甲乙为君，子丑为臣，子丑甲乙合...
    """
    
    original_text: str = """- **原文（source_text）**：
  数之所合，变之所由出也。乾为天，坤为地，乾坤合而为泰；德为父，红为母，德红合而为东；干为君，支为臣，干支合而纳音生。是故甲乙为君，子丑为臣，子丑甲乙合而为金。盖五行之在天下，各有气性，有材位，或相济或相克，若成器未成器，旺中受绝，绝中受气，惟相配而取之为不同耳。此金之数之所以难同而又有海中沙中之异。

- 分字分词释义：
  - **数之所合，变之所由出**：一切变化都源于数理的组合与会合。
  - **干为君，支为臣**：干在上、支在下，象君臣之分，合则成事。
  - **海中金/沙中金等差别**：强调同为金，其象因配位不同而有本质差异。

 - **规范化释义（primary_lang_explained）**：
  这一段把纳音置于更大的理数框架中：乾坤合泰、父母合而为东，类比到「干为君、支为臣」，干支相合才生出纳音之象。同属金者，因为干支组合不同，就有「海中金」「沙中金」等差别——或在包藏未形之中，或已成器在外。故纳音不是简单的「金就是金」，而是通过干支配位来细分其气性、材质与成器程度。

- **完整对等诠释（secondary_lang_full）**：

  Here Nayin is placed inside a broader framework of number and change. Just as Qian and Kun combine to form the hexagram Tai, or father and mother combine to generate the East, so too "the stem is ruler, the branch is minister": only when they join does a specific Nayin image arise. Charts that all belong to Metal on the Five‑Element level will still differ sharply depending on which stem–branch pair they use. The same Metal can appear as "Metal in the Sea", "Metal in the Sand", "Sword‑Edge Metal", "Hairpin‑and‑Bracelet Metal" and so on—sometimes still hidden and unformed, sometimes already forged, sometimes turned to ornament. Nayin is therefore not a crude statement that "this is Metal", but a way of grading the temperament, material quality and degree of completion that a given stem–branch combination gives to its element."""
    normalized_text_zh: str = """"""
    subject: str = "干支合而纳音生"
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
        l1_anchor="smth_v1.0.0_干支合而纳音生_001_L1",
    )
    version: str = "1.0.0"
