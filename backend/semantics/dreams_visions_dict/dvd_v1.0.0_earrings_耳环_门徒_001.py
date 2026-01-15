"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.409469
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
    semantic_id="dvd_v1.0.0_earrings_耳环_门徒_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Earrings耳环门徒(SemanticEntry):
    """
    ### Source Text

> **Earrings**: A picture of being given to your master and committed to him—bound ...
    """
    
    original_text: str = """### Source Text

> **Earrings**: A picture of being given to your master and committed to him—bound as a bond slave to hear his voice.
> When an Israelite slave had completed 7 years of service, he could go free. If he loved his master, he could commit to serving him forever—his master would pierce his ear with an awl at the doorpost.
> Exodus 21:6 "...his master shall bore his ear through with an awl; and he shall serve him forever."
> Negative: Gold earrings used to make the golden calf—idolatry.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Earrings | 耳环 | 顺服和委身 |
| Bond slave | 仆人 | 甘心服事 |
| Commitment | 委身 | 终生的奉献 |
| Idolatry | 偶像崇拜 | 负面时代表 |

### English Paraphrase

Earrings represent being given to your master—committed as a bond slave to hear his voice forever. In Israel, a slave who loved his master had his ear pierced at the doorpost. Negatively, gold earrings were used to make the golden calf, representing idolatry.

### Chinese Interpretation

耳环代表委身给你的主人——作仆人终生听从他的声音。在以色列，爱主人的仆人在门框穿耳。负面而言，金耳环被用来制作金牛犊，代表偶像崇拜。

### Core Points

1. **正负皆可**: 使用目的决定含义
2. **甘心委身**: 选择终生服事
3. **听从声音**: 穿耳代表听从主人
4. **偶像警告**: 可能代表偶像崇拜

### Narrative Snippets

- `[ns_dav_e003]` `[trigger: earrings_slave]` `[factor_trigger: dream_earrings AND dream_servant]` `[role: 主干]` Earrings speak of being committed as a bond slave—given to your master to hear his voice forever. → 耳环象征作仆人委身——终生听从主人的声音。
- `[ns_dav_e004]` `[trigger: earrings_idol]` `[factor_trigger: dream_earrings AND dream_idol]` `[role: 警告]` Gold earrings were used to make the golden calf—representing idolatry and false worship. → 金耳环被用来制作金牛犊——代表偶像崇拜和虚假敬拜。"""
    normalized_text_zh: str = """"""
    subject: str = "Earrings 耳环/门徒"
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
        l1_anchor="dvd_v1.0.0_earrings_耳环_门徒_001_L1",
    )
    version: str = "1.0.0"
