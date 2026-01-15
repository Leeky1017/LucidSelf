"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412127
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
    semantic_id="dvd_v1.0.0_father_父亲_权柄_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Father父亲权柄(SemanticEntry):
    """
    ### Source Text

> **Father**: Your father in dreams represents authority, leadership, and often spe...
    """
    
    original_text: str = """### Source Text

> **Father**: Your father in dreams represents authority, leadership, and often speaks of God the Father.
> Positive: A positive father figure represents godly authority and protection. Negative: A negative father figure represents false authority, abuse, or wounds from earthly father.
> In internal dreams, your earthly father may represent your relationship with God the Father.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Father | 父亲 | 权柄和保护 |
| Authority | 权柄 | 领导的能力 |
| Protection | 保护 | 遮盖和安全 |
| Wounds | 伤害 | 来自父亲的创伤 |

### English Paraphrase

Father represents authority, leadership, and often God the Father. A positive father figure represents godly authority and protection. A negative one represents false authority, abuse, or wounds. Your earthly father in dreams may reflect your relationship with God the Father.

### Chinese Interpretation

父亲代表权柄、领导，常常象征天父。正面的父亲形象代表敬虔的权柄和保护。负面的代表错误的权柄、虐待或伤害。梦中你地上的父亲可能反映你与天父的关系。

### Core Points

1. **正负皆可**: 父亲形象决定含义
2. **天父象征**: 常代表与神的关系
3. **权柄代表**: 领导和保护的能力
4. **伤害反映**: 可能暴露父亲创伤

### Narrative Snippets

- `[ns_dav_f003]` `[trigger: father_authority]` `[factor_trigger: dream_father AND dream_authority]` `[role: 主干]` Father represents authority and leadership—often reflecting your relationship with God the Father. → 父亲代表权柄和领导——常常反映你与天父的关系。
- `[ns_dav_f004]` `[trigger: father_wounds]` `[factor_trigger: dream_father AND dream_wounds]` `[role: 警告]` A negative father figure represents wounds and false authority—need healing from father issues. → 负面的父亲形象代表伤害和错误权柄——需要从父亲问题中得医治。"""
    normalized_text_zh: str = """"""
    subject: str = "Father 父亲/权柄"
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
        l1_anchor="dvd_v1.0.0_father_父亲_权柄_001_L1",
    )
    version: str = "1.0.0"
