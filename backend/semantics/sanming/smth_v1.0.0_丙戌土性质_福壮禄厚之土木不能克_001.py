"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228456
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
    semantic_id="smth_v1.0.0_丙戌土性质_福壮禄厚之土木不能克_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙戌土性质福壮禄厚之土木不能克(SemanticEntry):
    """
    - **原文（source_text）**：
  丙戌土、福壮禄厚之土，木不能克，忌见生旺之金，若遇火盛，则贵不可言。

- **分字分词释义**：
  - **福壮禄厚**：福分壮大禄位厚重。
  ...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙戌土、福壮禄厚之土，木不能克，忌见生旺之金，若遇火盛，则贵不可言。

- **分字分词释义**：
  - **福壮禄厚**：福分壮大禄位厚重。
  - **木不能克**：木不能克制。
  - **生旺之金**：生旺的金。
  - **火盛**：火旺盛。
  - **贵不可言**：非常尊贵。

- **规范化释义（primary_lang_explained）**：
  丙戌土，是福分壮大禄位厚重的土，木不能克制，忌讳见到生旺的金，如果遇到火旺盛，则非常尊贵。

- **完整对等诠释（secondary_lang_full）**：
  Bingxu Earth is fortune-robust salary-abundant earth, Wood cannot overcome, avoids seeing flourishing Metal, if encountering Fire prosperity, then nobility beyond words.

- **核心要点**：
  - 丙戌为屋上土，福壮禄厚
  - 木不能克
  - 忌生旺之金
  - 喜火盛则贵

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_217]` `[trigger: 丙戌土性质]` `[factor_trigger: bingxu_earth_fortune_abundant AND wood_cannot_overcome AND favor_fire_prosperity]` `[role: 主干]` 丙戌土、福壮禄厚之土，木不能克，忌见生旺之金，若遇火盛，则贵不可言。 → 《三命通会》卷一#丙戌土性质

- **详细解说**：
  此条解释丙戌（屋上土）的性质。丙戌纳音为土，是福分壮大禄位厚重的土，木不能克制（因为戌中含火，火能泄木生土），忌讳生旺的金（金泄土气），如果遇到火旺盛（火生土），则非常尊贵。强土喜火生不畏木克。

- **校勘与字词辨析（双语）**：
  - **中文**："福壮"指福分强大。"禄厚"指禄位深厚。"生旺之金"指处于生旺状态的金。"贵不可言"指极其尊贵。
  - **English**: "Fortune-robust" means great fortune. "Salary-abundant" means deep emolument. "Flourishing Metal" means Metal in prosperous state. "Nobility beyond words" means extremely noble."""
    normalized_text_zh: str = """"""
    subject: str = "丙戌土性质：福壮禄厚之土木不能克"
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
        l1_anchor="smth_v1.0.0_丙戌土性质_福壮禄厚之土木不能克_001_L1",
    )
    version: str = "1.0.0"
