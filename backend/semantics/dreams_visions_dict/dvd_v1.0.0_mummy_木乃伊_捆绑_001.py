"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396269
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
    semantic_id="dvd_v1.0.0_mummy_木乃伊_捆绑_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Mummy木乃伊捆绑(SemanticEntry):
    """
    ### Source Text

> **Mummy**: To see someone wrapped up in mummy clothing indicates they are 'tied u...
    """
    
    original_text: str = """### Source Text

> **Mummy**: To see someone wrapped up in mummy clothing indicates they are 'tied up' and in spiritual bondage—from the enemy's work or trying to hide away from something. Unlike a cocoon where something wonderful is happening, being wrapped as a mummy speaks of slow death meant to suffocate your spiritual life.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Mummy | 木乃伊 | 捆绑和束缚 |
| Bondage | 捆绑 | 属灵的束缚 |
| Tied up | 被绑住 | 无法行动 |
| Suffocate | 窒息 | 属灵生命的死亡 |

### English Paraphrase

A mummy indicates being 'tied up' in spiritual bondage—from the enemy's work or hiding. Unlike a cocoon where growth happens, being wrapped as a mummy speaks of slow death meant to suffocate your spiritual life.

### Chinese Interpretation

木乃伊表示被"绑住"在属灵的捆绑中——来自仇敌的工作或躲藏。不像茧中有美好的事情发生，被包成木乃伊象征慢性死亡，旨在窒息你的属灵生命。

### Core Points

1. **始终负面**: 木乃伊是捆绑
2. **束缚象征**: 属灵的捆绑
3. **死亡过程**: 慢性窒息
4. **与茧不同**: 茧是成长，木乃伊是死亡

### Narrative Snippets

- `[ns_dav_m021]` `[trigger: mummy_bondage]` `[factor_trigger: dream_mummy AND dream_bondage]` `[role: 警告]` Being wrapped as a mummy speaks of slow death meant to suffocate your spiritual life. → 被包成木乃伊象征旨在窒息你属灵生命的慢性死亡。"""
    normalized_text_zh: str = """"""
    subject: str = "Mummy 木乃伊/捆绑"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_mummy_木乃伊_捆绑_001_L1",
    )
    version: str = "1.0.0"
