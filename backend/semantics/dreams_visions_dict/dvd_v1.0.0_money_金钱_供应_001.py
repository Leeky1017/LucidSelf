"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396205
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
    semantic_id="dvd_v1.0.0_money_金钱_供应_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Money金钱供应(SemanticEntry):
    """
    ### Source Text

> **Money**: In a positive light, money speaks of provision for your need. Dreaming...
    """
    
    original_text: str = """### Source Text

> **Money**: In a positive light, money speaks of provision for your need. Dreaming of receiving money is encouragement that the Lord desires to meet your need—but requires faith and love to bring it to pass.
> Negative: A black hand holding money is a picture of a spirit of theft. The love of money is the root of temporal values that can destroy you.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Money | 金钱 | 财务供应 |
| Provision | 供应 | 需要被满足 |
| Theft | 偷窃 | 仇敌的工作 |
| Love of money | 贪财 | 暂时价值观的根 |

### English Paraphrase

Money positively represents provision for your needs. Dreaming of receiving money encourages that the Lord will provide—but requires faith. A black hand holding money pictures a spirit of theft. The love of money is the root of temporal values that destroy.

### Chinese Interpretation

金钱正面代表对你需要的供应。梦见收到钱鼓励说主会供应——但需要信心。黑手拿着钱象征偷窃的灵。贪财是导致毁灭的暂时价值观的根。

### Core Points

1. **正负皆可**: 金钱来源决定含义
2. **供应象征**: 需要被满足
3. **偷窃警告**: 黑手是仇敌
4. **贪财警告**: 爱钱是万恶之根

### Narrative Snippets

- `[ns_dav_m009]` `[trigger: money_provision]` `[factor_trigger: dream_money AND dream_provision]` `[role: 主干]` Money positively speaks of provision for your need—the Lord desires to meet it. → 金钱正面象征对你需要的供应——主渴望满足它。
- `[ns_dav_m010]` `[trigger: money_theft]` `[factor_trigger: dream_money AND dream_theft]` `[role: 警告]` A black hand holding money is a picture of a spirit of theft stealing your blessing. → 黑手拿着钱象征偷窃的灵偷窃你的祝福。"""
    normalized_text_zh: str = """"""
    subject: str = "Money 金钱/供应"
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
        l1_anchor="dvd_v1.0.0_money_金钱_供应_001_L1",
    )
    version: str = "1.0.0"
