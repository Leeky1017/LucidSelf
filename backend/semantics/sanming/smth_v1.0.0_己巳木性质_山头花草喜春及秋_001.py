"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228326
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
    semantic_id="smth_v1.0.0_己巳木性质_山头花草喜春及秋_001",
    book_id="sanming",
    engine_id="bazi"
)
class 己巳木性质山头花草喜春及秋(SemanticEntry):
    """
    - **原文（source_text）**：
  己巳木、山头花草，喜春及秋。禄库八专，□字曲脚。

- **分字分词释义**：
  - **山头花草**：山顶的花草。
  - **喜春及秋**：喜欢...
    """
    
    original_text: str = """- **原文（source_text）**：
  己巳木、山头花草，喜春及秋。禄库八专，□字曲脚。

- **分字分词释义**：
  - **山头花草**：山顶的花草。
  - **喜春及秋**：喜欢春季和秋季。
  - **八专**：八专煞，神煞名。
  - **曲脚**：曲脚煞，神煞名。

- **规范化释义（primary_lang_explained）**：
  己巳木，是山头的花草，喜欢春季和秋季，有禄库、八专，忌讳某字煞、曲脚煞。

- **完整对等诠释（secondary_lang_full）**：
  Jisi Wood is flowers and grass on mountain peaks, favoring spring and autumn seasons, having Salary-Storage and Eight-Exclusive, avoiding certain character sha and Curved-Foot sha.

- **核心要点**：
  - 己巳为大林木，如山头花草
  - 喜春季（生发）、秋季（成熟）
  - 有禄库、八专
  - 忌某字、曲脚煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_200]` `[trigger: 己巳木性质]` `[factor_trigger: jisi_wood_flowers AND favor_spring_autumn AND eight_exclusive]` `[role: 主干]` 己巳木、山头花草，喜春及秋。禄库八专，□字曲脚。 → 《三命通会》卷一#己巳木性质

- **详细解说**：
  此条解释己巳（大林木）的性质。己巳纳音也是木，但如山头的花草，娇嫩美丽，喜欢春季（生长时节）和秋季（结实成熟），有禄库、八专（专禄）等吉神，但忌某字煞、曲脚煞等凶煞。山头花草需要适合的季节才能繁茂。

- **校勘与字词辨析（双语）**：
  - **中文**："山头花草"指山顶生长的花草。"八专"指八专日，主专禄。"曲脚"为曲脚煞，主身体残疾。
  - **English**: "Flowers and grass on peaks" refers to flora growing on mountain tops. "Eight-Exclusive" refers to Eight-Exclusive days, indicating exclusive salary. "Curved-Foot" is Curved-Foot sha, indicating physical disabilities."""
    normalized_text_zh: str = """"""
    subject: str = "己巳木性质：山头花草喜春及秋"
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
        l1_anchor="smth_v1.0.0_己巳木性质_山头花草喜春及秋_001_L1",
    )
    version: str = "1.0.0"
