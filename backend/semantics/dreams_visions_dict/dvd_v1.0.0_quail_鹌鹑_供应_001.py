"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405368
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
    semantic_id="dvd_v1.0.0_quail_鹌鹑_供应_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Quail鹌鹑供应(SemanticEntry):
    """
    ### Source Text

> **Quail**: The Lord provided quails for the Children of Israel in the desert. The...
    """
    
    original_text: str = """### Source Text

> **Quail**: The Lord provided quails for the Children of Israel in the desert. They speak not only of having your needs provided, but your desires as well. See also 'Meat' for more detail.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Quail | 鹌鹑 | 供应和满足 |
| Provision | 供应 | 神的给予 |
| Desires | 渴望 | 超过需要的 |
| Desert | 旷野 | 干旱之地 |

### English Paraphrase

Quail represents the Lord's provision in the desert—providing not only for needs but also desires. The Israelites received quails when they desired meat—God provided beyond necessity.

### Chinese Interpretation

鹌鹑代表主在旷野的供应——不仅供应需要也供应渴望。以色列人渴望肉时收到了鹌鹑——神供应超过必需的。

### Core Points

1. **通常正面**: 鹌鹑代表供应
2. **供应象征**: 神的丰富给予
3. **渴望满足**: 超过基本需要
4. **旷野记号**: 在干旱处供应

### Narrative Snippets

- `[ns_dav_q001]` `[trigger: quail_provision]` `[factor_trigger: dream_quail AND dream_provision]` `[role: 主干]` Quails speak of God providing not only for your needs but also your desires. → 鹌鹑象征神不仅供应你的需要也供应你的渴望。"""
    normalized_text_zh: str = """"""
    subject: str = "Quail 鹌鹑/供应"
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
        l1_anchor="dvd_v1.0.0_quail_鹌鹑_供应_001_L1",
    )
    version: str = "1.0.0"
