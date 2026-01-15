"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433500
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
    semantic_id="dvd_v1.0.0_oyster_牡蛎_珍珠_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Oyster牡蛎珍珠(SemanticEntry):
    """
    ### Source Text

> **Oyster**: Related to Pearl. An oyster contains something precious inside—speaks...
    """
    
    original_text: str = """### Source Text

> **Oyster**: Related to Pearl. An oyster contains something precious inside—speaks of hidden treasure waiting to be found. If you see a pearl still in the oyster, the Lord is giving you a blessing, but you will need to do something to get it.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Oyster | 牡蛎 | 隐藏的宝贝 |
| Pearl | 珍珠 | 宝贵的东西 |
| Hidden | 隐藏 | 需要发现的 |
| Effort | 努力 | 需要行动 |

### English Paraphrase

An oyster contains something precious inside—hidden treasure waiting to be found. If a pearl is still in the oyster, the Lord is giving you a blessing, but you need to do something to get it—effort is required.

### Chinese Interpretation

牡蛎里面有宝贵的东西——等待被发现的隐藏宝藏。如果珍珠还在牡蛎里，主正在给你祝福，但你需要做些什么才能得到它——需要付出努力。

### Core Points

1. **通常正面**: 牡蛎代表隐藏的祝福
2. **珍珠象征**: 宝贵的东西
3. **需要行动**: 要付出努力
4. **祝福记号**: 神给的礼物

### Narrative Snippets

- `[ns_dav_o010]` `[trigger: oyster_pearl]` `[factor_trigger: dream_oyster AND dream_pearl]` `[role: 主干]` If a pearl is still in the oyster, the Lord is giving you a blessing, but you need to do something to get it. → 如果珍珠还在牡蛎里，主正在给你祝福，但你需要做些什么才能得到它。"""
    normalized_text_zh: str = """"""
    subject: str = "Oyster 牡蛎/珍珠"
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
        l1_anchor="dvd_v1.0.0_oyster_牡蛎_珍珠_001_L1",
    )
    version: str = "1.0.0"
