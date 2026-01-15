"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433445
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
    semantic_id="dvd_v1.0.0_numbers_数字_含义_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Numbers数字含义(SemanticEntry):
    """
    ### Source Text

> **Numbers**: Be wary of interpreting every number as a 'sign.' Some clear biblica...
    """
    
    original_text: str = """### Source Text

> **Numbers**: Be wary of interpreting every number as a 'sign.' Some clear biblical numbers: One=unity, Two=balance, Three=Trinity/death, Five=man/Fivefold Ministry, Seven=completion, Twelve=maturity, Thirty=redemption, Three Hundred=ministry teams.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Numbers | 数字 | 圣经中的含义 |
| Unity | 合一 | 一的含义 |
| Completion | 完成 | 七的含义 |
| Maturity | 成熟 | 十二的含义 |

### English Paraphrase

Be wary of interpreting every number as a sign—ensure each has root in the Word. Biblical numbers: One=unity, Two=balance, Three=Trinity/death, Five=man/Fivefold Ministry, Seven=completion, Twelve=maturity, Thirty=redemption, Three Hundred=ministry teams.

### Chinese Interpretation

警惕把每个数字都解释为征兆——确保每个都根植于话语中。圣经数字：一=合一，二=平衡，三=三位一体/死，五=人/五重事工，七=完成，十二=成熟，三十=救赎，三百=事工团队。

### Core Points

1. **中性象征**: 数字本身是中性的
2. **圣经根基**: 需要话语的支持
3. **特定含义**: 不同数字有特定意义
4. **谨慎解释**: 不要过度解读

### Narrative Snippets

- `[ns_dav_n013]` `[trigger: numbers_biblical]` `[factor_trigger: dream_numbers AND dream_biblical]` `[role: 主干]` Seven is the number of completion—representing the end of a season and entering into rest. → 七是完成的数字——代表一个季节的结束和进入安息。
- `[ns_dav_n014]` `[trigger: numbers_caution]` `[factor_trigger: dream_numbers AND dream_caution]` `[role: 主干]` Ensure every number interpretation has its root in the Word—not myths and traditions. → 确保每个数字解释都根植于话语中——而非神话和传统。"""
    normalized_text_zh: str = """"""
    subject: str = "Numbers 数字/含义"
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
        l1_anchor="dvd_v1.0.0_numbers_数字_含义_001_L1",
    )
    version: str = "1.0.0"
