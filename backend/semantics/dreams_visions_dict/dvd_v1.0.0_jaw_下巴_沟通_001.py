"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429287
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
    semantic_id="dvd_v1.0.0_jaw_下巴_沟通_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Jaw下巴沟通(SemanticEntry):
    """
    ### Source Text

> **Jaw**: Anyone with a broken jaw knows how difficult it is to speak! Your jaw is...
    """
    
    original_text: str = """### Source Text

> **Jaw**: Anyone with a broken jaw knows how difficult it is to speak! Your jaw is a picture of your ability to communicate. It is also a picture of your strengths and wisdom to choose the correct direction. When a nation was going wrong, the Lord said He would put a bridle on their jaw to lead them.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Jaw | 下巴 | 沟通能力 |
| Communication | 沟通 | 说话和表达 |
| Bridle | 嚼环 | 主的引导 |
| Direction | 方向 | 正确的选择 |

### English Paraphrase

The jaw represents your ability to communicate. It also pictures your strengths and wisdom to choose direction. A broken jaw means difficulty speaking. When a nation went wrong, the Lord would put a bridle on their jaw to lead them back.

### Chinese Interpretation

下巴代表你沟通的能力。它也象征你选择方向的力量和智慧。下巴骨折意味着说话困难。当一个国家走错路时，主会在他们下巴上放嚼环来引导他们回来。

### Core Points

1. **正负皆可**: 状态决定含义
2. **沟通象征**: 说话和表达的能力
3. **方向智慧**: 选择正确方向
4. **引导记号**: 主的纠正和引导

### Narrative Snippets

- `[ns_dav_j001]` `[trigger: jaw_communication]` `[factor_trigger: dream_jaw AND dream_communication]` `[role: 主干]` Your jaw is a picture of your ability to communicate and your wisdom to choose direction. → 你的下巴是你沟通能力和选择方向智慧的象征。"""
    normalized_text_zh: str = """"""
    subject: str = "Jaw 下巴/沟通"
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
        l1_anchor="dvd_v1.0.0_jaw_下巴_沟通_001_L1",
    )
    version: str = "1.0.0"
