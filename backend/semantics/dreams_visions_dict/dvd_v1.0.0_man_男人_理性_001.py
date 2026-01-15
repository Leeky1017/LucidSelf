"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396175
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
    semantic_id="dvd_v1.0.0_man_男人_理性_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Man男人理性(SemanticEntry):
    """
    ### Source Text

> **Man**: As an unknown figure, a man typically represents your masculine (animus)...
    """
    
    original_text: str = """### Source Text

> **Man**: As an unknown figure, a man typically represents your masculine (animus) or intellectual side—left-brained, analytical, logical. In ministry, it speaks of a teaching orientation.
> A Known Man: Identify what he means to you. A spiritual father could speak of the Lord.
> Negative: Goliath represents the spirit of fear—your own fears preventing you from moving forward.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Man | 男人 | 理性和阳性面 |
| Animus | 阳性面 | 分析性的一面 |
| Teaching | 教导 | 事工的方向 |
| Goliath | 歌利亚 | 恐惧的灵 |

### English Paraphrase

An unknown man represents your masculine/intellectual side—analytical and logical. In ministry, it speaks of teaching orientation. A known man represents what he means to you—a spiritual father could be the Lord. Goliath represents the spirit of fear preventing you from rising up.

### Chinese Interpretation

陌生的男人代表你阳性/理性的一面——分析性和逻辑性的。在事工中，它象征教导的方向。认识的男人代表他对你的意义——属灵的父亲可能是主。歌利亚代表阻止你兴起的恐惧的灵。

### Core Points

1. **正负皆可**: 男人形象决定含义
2. **理性象征**: 阳性和分析性的一面
3. **教导方向**: 可能是教师的呼召
4. **恐惧警告**: 歌利亚是恐惧的灵

### Narrative Snippets

- `[ns_dav_m003]` `[trigger: man_animus]` `[factor_trigger: dream_man AND dream_animus]` `[role: 主干]` An unknown man represents your masculine side—analytical, logical, and teaching-oriented. → 陌生的男人代表你阳性的一面——分析性的、逻辑性的和教导导向的。
- `[ns_dav_m004]` `[trigger: man_goliath]` `[factor_trigger: dream_man AND dream_fear]` `[role: 警告]` Goliath represents the spirit of fear—your own fears preventing you from rising up. → 歌利亚代表恐惧的灵——你自己的恐惧阻止你兴起。"""
    normalized_text_zh: str = """"""
    subject: str = "Man 男人/理性"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_man_男人_理性_001_L1",
    )
    version: str = "1.0.0"
