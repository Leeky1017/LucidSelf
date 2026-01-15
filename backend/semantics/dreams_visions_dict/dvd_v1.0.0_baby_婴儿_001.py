"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424261
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
    semantic_id="dvd_v1.0.0_baby_婴儿_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Baby婴儿(SemanticEntry):
    """
    ### Source Text

> Babies have twofold meaning: new responsibility + trust/vulnerability/innocence. ...
    """
    
    original_text: str = """### Source Text

> Babies have twofold meaning: new responsibility + trust/vulnerability/innocence. In negative light, immaturity.

**Positive**: New life/ministry. Boy = teaching/leadership; Girl = prophetic/creative. Twins = twofold ministry.
**Negative**: Lost baby = neglected spiritual promotion. Neglecting baby = unused gifts.

### English Paraphrase

Baby = new responsibility + trust/vulnerability. **Positive**: Boy = teaching; Girl = prophetic. **Negative**: Lost = neglected promotion.

### Chinese Interpretation（完整对等诠释）

婴儿 = 新责任 + 信任/脆弱。**正面**：男孩 = 教导；女孩 = 先知。**负面**：丢失 = 忽视晋升。

### Narrative Snippets

- `[ns_dav_b002]` `[trigger: 梦婴儿]` `[factor_trigger: dream_symbol_baby]` `[role: 主干]` Baby = new responsibility—boy = teaching, girl = prophetic. → Dreams Dictionary #Baby
- `[ns_dav_b003]` `[trigger: 丢失婴儿]` `[factor_trigger: dream_symbol_baby AND baby_gender]` `[role: 条件分支]` Lost baby = neglected spiritual promotion. → Dreams Dictionary #Baby"""
    normalized_text_zh: str = """"""
    subject: str = "Baby 婴儿"
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
        l1_anchor="dvd_v1.0.0_baby_婴儿_001_L1",
    )
    version: str = "1.0.0"
