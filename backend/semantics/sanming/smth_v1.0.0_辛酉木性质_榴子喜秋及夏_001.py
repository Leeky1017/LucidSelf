"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228487
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
    semantic_id="smth_v1.0.0_辛酉木性质_榴子喜秋及夏_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辛酉木性质榴子喜秋及夏(SemanticEntry):
    """
    - **原文（source_text）**：
  辛酉木、榴子喜秋及夏，建禄交神，九丑八专，悬针聋哑。

- **分字分词释义**：
  - **榴子**：石榴果实。
  - **喜秋及夏**：喜欢秋...
    """
    
    original_text: str = """- **原文（source_text）**：
  辛酉木、榴子喜秋及夏，建禄交神，九丑八专，悬针聋哑。

- **分字分词释义**：
  - **榴子**：石榴果实。
  - **喜秋及夏**：喜欢秋季和夏季。
  - **交神**：交神煞。
  - **九丑**：九丑煞。

- **规范化释义（primary_lang_explained）**：
  辛酉木，是石榴果实，喜欢秋季和夏季，有建禄则吉，遇交神煞、九丑煞、八专煞、悬针煞、聋哑煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Xinyou Wood is pomegranate fruit, favors autumn and summer, auspicious with Establishing-Salary, inauspicious with Crossing-Spirit sha, Nine-Ugly sha, Eight-Exclusive sha, Suspended-Needle sha, Deaf-Mute sha.

- **核心要点**：
  - 辛酉为石榴木，如榴子（果实）
  - 喜秋季（结果）、夏季（成熟）
  - 有建禄吉
  - 忌多种凶煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_221]` `[trigger: 辛酉木性质]` `[factor_trigger: xinyou_wood_pomegranate_fruit AND favor_autumn_summer AND establishing_salary]` `[role: 主干]` 辛酉木、榴子喜秋及夏，建禄交神，九丑八专，悬针聋哑。 → 《三命通会》卷一#辛酉木性质

- **详细解说**：
  此条解释辛酉（石榴木）的性质。辛酉纳音也是木，如石榴果实，喜欢秋季（结果时节）和夏季（生长成熟），有建禄则吉，但忌交神煞、九丑煞、八专煞、悬针煞、聋哑煞等多种凶煞。果实需要夏秋两季才能完成从开花到结果的过程。

- **校勘与字词辨析（双语）**：
  - **中文**："榴子"指石榴果实。"喜秋及夏"，夏季开花，秋季结果。"九丑"为九丑煞，大凶。
  - **English**: "Pomegranate fruit" refers to fruit of pomegranate. "Favors autumn and summer"—summer for flowering, autumn for fruiting. "Nine-Ugly" is Nine-Ugly sha, extremely inauspicious."""
    normalized_text_zh: str = """"""
    subject: str = "辛酉木性质：榴子喜秋及夏"
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
        l1_anchor="smth_v1.0.0_辛酉木性质_榴子喜秋及夏_001_L1",
    )
    version: str = "1.0.0"
