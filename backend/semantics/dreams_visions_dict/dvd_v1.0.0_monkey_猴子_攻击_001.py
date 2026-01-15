"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396215
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
    semantic_id="dvd_v1.0.0_monkey_猴子_攻击_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Monkey猴子攻击(SemanticEntry):
    """
    ### Source Text

> **Monkey**: Irritation, mischief and a work of the enemy in your life. More often...
    """
    
    original_text: str = """### Source Text

> **Monkey**: Irritation, mischief and a work of the enemy in your life. More often than not, when I see a monkey in the spirit, it is representative of a power demon and an attack in your life.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Monkey | 猴子 | 烦扰和攻击 |
| Mischief | 恶作剧 | 仇敌的捣乱 |
| Power demon | 权势邪灵 | 仇敌的工作 |
| Attack | 攻击 | 属灵的争战 |

### English Paraphrase

A monkey represents irritation, mischief and the enemy's work in your life. When seen in the spirit, it is representative of a power demon and an attack against you.

### Chinese Interpretation

猴子代表烦扰、恶作剧和仇敌在你生命中的工作。在灵里看见时，它代表权势邪灵和对你的攻击。

### Core Points

1. **始终负面**: 猴子代表仇敌的工作
2. **烦扰象征**: 恶作剧和捣乱
3. **邪灵警告**: 权势邪灵的代表
4. **攻击提示**: 需要属灵争战

### Narrative Snippets

- `[ns_dav_m011]` `[trigger: monkey_demon]` `[factor_trigger: dream_monkey AND dream_demon]` `[role: 警告]` A monkey in the spirit represents a power demon and an attack in your life. → 灵里的猴子代表权势邪灵和对你生命的攻击。"""
    normalized_text_zh: str = """"""
    subject: str = "Monkey 猴子/攻击"
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
        l1_anchor="dvd_v1.0.0_monkey_猴子_攻击_001_L1",
    )
    version: str = "1.0.0"
