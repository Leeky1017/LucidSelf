"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396251
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
    semantic_id="dvd_v1.0.0_mouse_老鼠_偷窃_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Mouse老鼠偷窃(SemanticEntry):
    """
    ### Source Text

> **Mouse**: Attack on your daily provision. Mice are completely negative in Script...
    """
    
    original_text: str = """### Source Text

> **Mouse**: Attack on your daily provision. Mice are completely negative in Scripture. They speak of a spirit of theft that is nibbling away at your blessing. Mice came in plagues and destroyed everything in their path.
> A rat is similar but depicts greater destruction and disease (black plague)—speaking of something unclean.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Mouse | 老鼠 | 日常供应的攻击 |
| Theft | 偷窃 | 蚕食祝福 |
| Rat | 大老鼠 | 更大的毁灭 |
| Unclean | 不洁 | 疾病和污秽 |

### English Paraphrase

A mouse represents attack on your daily provision. Mice are completely negative—a spirit of theft nibbling away blessings. They came in plagues destroying everything. A rat depicts greater destruction and disease—something unclean.

### Chinese Interpretation

老鼠代表对你日常供应的攻击。老鼠完全是负面的——偷窃的灵蚕食祝福。它们如瘟疫来临毁灭一切。大老鼠代表更大的毁灭和疾病——不洁的东西。

### Core Points

1. **始终负面**: 老鼠是偷窃的灵
2. **偷窃象征**: 蚕食祝福的仇敌
3. **供应攻击**: 针对日常供应
4. **疾病警告**: 大老鼠代表不洁

### Narrative Snippets

- `[ns_dav_m018]` `[trigger: mouse_theft]` `[factor_trigger: dream_mouse AND dream_theft]` `[role: 警告]` Mice represent a spirit of theft nibbling away at your blessing and daily provision. → 老鼠代表偷窃的灵蚕食你的祝福和日常供应。"""
    normalized_text_zh: str = """"""
    subject: str = "Mouse 老鼠/偷窃"
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
        l1_anchor="dvd_v1.0.0_mouse_老鼠_偷窃_001_L1",
    )
    version: str = "1.0.0"
