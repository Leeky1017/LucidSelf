"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429163
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
    semantic_id="dvd_v1.0.0_ice_冰_冷漠_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ice冰冷漠(SemanticEntry):
    """
    ### Source Text

> **Ice**: In any culture ice represents cold, hard and unmoving. I see this often ...
    """
    
    original_text: str = """### Source Text

> **Ice**: In any culture ice represents cold, hard and unmoving. I see this often when praying for people who have closed their hearts off to others. If you dream of being surrounded by ice, perhaps this is a picture of how you have closed your heart off and become distant.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Ice | 冰 | 冷漠和封闭 |
| Cold | 冷 | 无感情的 |
| Hard | 硬 | 不愿改变的 |
| Heart | 心 | 被封闭的 |

### English Paraphrase

Ice represents cold, hard and unmoving—people who have closed their hearts off to others. Being surrounded by ice shows you have become distant and closed. Ice around the heart indicates refusing to open to others and the Lord.

### Chinese Interpretation

冰代表冷漠、坚硬和不动——那些对他人封闭内心的人。被冰包围显示你变得疏远和封闭。心周围的冰表示拒绝向他人和主敞开。

### Core Points

1. **始终负面**: 冰代表冷漠和封闭
2. **心的状态**: 封闭的心
3. **疏远象征**: 与他人和神疏远
4. **需要敞开**: 让主进来带来改变

### Narrative Snippets

- `[ns_dav_i001]` `[trigger: ice_heart]` `[factor_trigger: dream_ice AND dream_heart]` `[role: 警告]` Ice around the heart indicates a person who has closed off their feelings and refuses to open. → 心周围的冰表示一个人封闭了感受，拒绝敞开。"""
    normalized_text_zh: str = """"""
    subject: str = "Ice 冰/冷漠"
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
        l1_anchor="dvd_v1.0.0_ice_冰_冷漠_001_L1",
    )
    version: str = "1.0.0"
