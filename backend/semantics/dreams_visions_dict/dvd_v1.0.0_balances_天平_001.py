"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424310
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
    semantic_id="dvd_v1.0.0_balances_天平_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Balances天平(SemanticEntry):
    """
    ### Source Text

> Balances = justice, judgment. **Positive**: Swung in favor = answer coming. **Neg...
    """
    
    original_text: str = """### Source Text

> Balances = justice, judgment. **Positive**: Swung in favor = answer coming. **Negative**: Against you = sin, odds (Dan 5:27). Cheated = spirit of theft.

### English Paraphrase

Balances = justice. **Positive**: In favor = blessing coming. **Negative**: Against = judgment. Cheated = theft stealing finances.

### Chinese Interpretation（完整对等诠释）

天平 = 公义。**正面**：倾斜有利 = 祝福将至。**负面**：不利 = 审判。被欺骗 = 偷窃财务。

### Narrative Snippets

- `[ns_dav_b010]` `[trigger: 梦天平]` `[factor_trigger: dream_symbol_balances]` `[role: 主干]` Balances = justice—in favor = blessing, against = judgment. → Dreams Dictionary #Balances"""
    normalized_text_zh: str = """"""
    subject: str = "Balances 天平"
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
        l1_anchor="dvd_v1.0.0_balances_天平_001_L1",
    )
    version: str = "1.0.0"
