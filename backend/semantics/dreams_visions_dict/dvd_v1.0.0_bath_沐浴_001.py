"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424470
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
    semantic_id="dvd_v1.0.0_bath_沐浴_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Bath沐浴(SemanticEntry):
    """
    ### Source Text

> Bath = complete cleansing (unlike basin). **Positive**: Total cleansing, sins was...
    """
    
    original_text: str = """### Source Text

> Bath = complete cleansing (unlike basin). **Positive**: Total cleansing, sins washed (Ezek 16:9; Acts 22:16). **Negative**: Dirty bath water = past hurts not free from.

### English Paraphrase

Bath = total cleansing. **Positive**: Sins washed. **Negative**: Dirty water = past hurts unresolved.

### Chinese Interpretation（完整对等诠释）

沐浴 = 完全洁净。**正面**：罪被洗净。**负面**：脏水 = 过去伤害未解决。

### Narrative Snippets

- `[ns_dav_b026]` `[trigger: 梦沐浴]` `[factor_trigger: dream_symbol_bath]` `[role: 主干]` Bath = total cleansing—clean water = forgiveness, dirty = past hurts. → Dreams Dictionary #Bath"""
    normalized_text_zh: str = """"""
    subject: str = "Bath 沐浴"
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
        l1_anchor="dvd_v1.0.0_bath_沐浴_001_L1",
    )
    version: str = "1.0.0"
