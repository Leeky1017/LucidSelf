"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405325
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
    semantic_id="dvd_v1.0.0_pregnant_怀孕_新事_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Pregnant怀孕新事(SemanticEntry):
    """
    ### Source Text

> **Pregnant**: The beginning of something new not yet visible. We conceive things ...
    """
    
    original_text: str = """### Source Text

> **Pregnant**: The beginning of something new not yet visible. We conceive things in our spirits—some blessings, some from fear or sin. Dreaming of pregnancy means something new is manifesting. Miscarriage that doesn't concern you means God prevented something not of Him.
> Negative: Pregnant with someone negative's baby means conceiving something not of God. A concerning miscarriage means the enemy is stealing your blessing.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Pregnant | 怀孕 | 新事的开始 |
| Conceive | 孕育 | 在灵里怀的 |
| Blessing | 祝福 | 神的给予 |
| Miscarriage | 流产 | 失去祝福 |

### English Paraphrase

Pregnancy represents the beginning of something new not yet visible. We conceive in our spirits—some blessings, some from fear or sin. Pregnancy means something new is manifesting. A non-concerning miscarriage means God prevented what wasn't of Him. A concerning miscarriage means the enemy is stealing.

### Chinese Interpretation

怀孕代表尚未可见的新事的开始。我们在灵里孕育——有些是祝福，有些来自恐惧或罪。怀孕意味着新事正在显现。不令人担忧的流产意味着神阻止了不属于祂的东西。令人担忧的流产意味着仇敌在偷窃。

### Core Points

1. **正负皆可**: 怀孕内容决定含义
2. **新事象征**: 尚未可见的开始
3. **祝福记号**: 神的新给予
4. **流产警告**: 可能是仇敌偷窃

### Narrative Snippets

- `[ns_dav_p015]` `[trigger: pregnant_new]` `[factor_trigger: dream_pregnant AND dream_new]` `[role: 主干]` Pregnancy represents the beginning of something new—about to manifest in your life. → 怀孕代表新事的开始——即将在你生命中显现。
- `[ns_dav_p016]` `[trigger: pregnant_miscarry]` `[factor_trigger: dream_pregnant AND dream_miscarry]` `[role: 警告]` A concerning miscarriage means the enemy is trying to steal the blessing God has given you. → 令人担忧的流产意味着仇敌正试图偷窃神给你的祝福。"""
    normalized_text_zh: str = """"""
    subject: str = "Pregnant 怀孕/新事"
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
        l1_anchor="dvd_v1.0.0_pregnant_怀孕_新事_001_L1",
    )
    version: str = "1.0.0"
