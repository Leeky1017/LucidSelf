"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443785
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
    semantic_id="dvd_v1.0.0_key_钥匙_权柄_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Key钥匙权柄(SemanticEntry):
    """
    ### Source Text

> **Key**: A key speaks of license, authority and calling. Every believer has been ...
    """
    
    original_text: str = """### Source Text

> **Key**: A key speaks of license, authority and calling. Every believer has been given a key to salvation. When you became born again, you were given the name of Jesus to use against the enemy—the license to loose and to bind.
> Golden key: Prophetic training. Large jewel-encrusted key: Apostolic release. Brass key: Teaching Ministry.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Key | 钥匙 | 权柄和呼召 |
| Authority | 权柄 | 捆绑和释放的能力 |
| Calling | 呼召 | 事工的方向 |
| License | 许可 | 使用耶稣名的权利 |

### English Paraphrase

A key represents license, authority and calling. Every believer has the key to salvation—the name of Jesus to loose and bind. Different keys indicate different callings: golden key for prophetic, jewel-encrusted for apostolic, brass for teaching ministry.

### Chinese Interpretation

钥匙代表许可、权柄和呼召。每个信徒都有救恩的钥匙——耶稣的名来释放和捆绑。不同的钥匙表示不同的呼召：金钥匙是先知的，镶宝石的是使徒的，铜钥匙是教导事工的。

### Core Points

1. **通常正面**: 钥匙代表权柄
2. **权柄象征**: 捆绑和释放的能力
3. **呼召记号**: 不同钥匙不同呼召
4. **事工方向**: 先知/使徒/教师

### Narrative Snippets

- `[ns_dav_k001]` `[trigger: key_authority]` `[factor_trigger: dream_key AND dream_authority]` `[role: 主干]` A key speaks of authority and calling—the license to loose and bind in Jesus' name. → 钥匙象征权柄和呼召——奉耶稣的名释放和捆绑的许可。
- `[ns_dav_k002]` `[trigger: key_calling]` `[factor_trigger: dream_key AND dream_calling]` `[role: 主干]` Different keys indicate different callings: golden for prophetic, jeweled for apostolic, brass for teaching. → 不同的钥匙表示不同的呼召：金的是先知的，镶宝石的是使徒的，铜的是教导的。"""
    normalized_text_zh: str = """"""
    subject: str = "Key 钥匙/权柄"
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
        l1_anchor="dvd_v1.0.0_key_钥匙_权柄_001_L1",
    )
    version: str = "1.0.0"
