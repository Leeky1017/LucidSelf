"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450566
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
    semantic_id="dvd_v1.0.0_hell_地狱_折磨_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Hell地狱折磨(SemanticEntry):
    """
    ### Source Text

> **Hell**: Hell is never a positive picture—represents torment and the work of the...
    """
    
    original_text: str = """### Source Text

> **Hell**: Hell is never a positive picture—represents torment and the work of the enemy. If you keep having dreams and visions of hell, you may have opened your heart to an influence not of the Lord. We serve a God of faith, hope and love—if dreams leave you confused, guilty or fearful, they are not of the Lord.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Hell | 地狱 | 折磨和仇敌的工作 |
| Torment | 折磨 | 痛苦和恐惧 |
| Deception | 迷惑 | 不是出于神的 |
| Fear | 恐惧 | 负面的属灵状态 |

### English Paraphrase

Hell is never positive—it represents torment and the enemy's work. Repeated dreams of hell may indicate opening your heart to wrong influences. We serve a God of faith, hope and love. Dreams leaving you confused, guilty or fearful are not of the Lord.

### Chinese Interpretation

地狱永远不是正面的——它代表折磨和仇敌的工作。反复梦见地狱可能表示向错误的影响敞开了心。我们服事的是信、望、爱的神。让你困惑、内疚或恐惧的梦不是出于主的。

### Core Points

1. **始终负面**: 地狱没有正面含义
2. **仇敌工作**: 代表撒但的领域
3. **迷惑警告**: 可能表示受了错误影响
4. **恐惧分辨**: 使人恐惧的不是出于神

### Narrative Snippets

- `[ns_dav_h011]` `[trigger: hell_negative]` `[factor_trigger: dream_hell AND dream_torment]` `[role: 警告]` Hell is never positive—it represents torment and the work of the enemy bringing deception. → 地狱永远不是正面的——它代表折磨和仇敌带来迷惑的工作。"""
    normalized_text_zh: str = """"""
    subject: str = "Hell 地狱/折磨"
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
        l1_anchor="dvd_v1.0.0_hell_地狱_折磨_001_L1",
    )
    version: str = "1.0.0"
