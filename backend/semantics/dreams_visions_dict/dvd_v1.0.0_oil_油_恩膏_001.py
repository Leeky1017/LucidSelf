"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433472
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
    semantic_id="dvd_v1.0.0_oil_油_恩膏_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Oil油恩膏(SemanticEntry):
    """
    ### Source Text

> **Oil**: Anointing, healing, cleansing, beautifying, softening, the Holy Spirit, ...
    """
    
    original_text: str = """### Source Text

> **Oil**: Anointing, healing, cleansing, beautifying, softening, the Holy Spirit, restoration, prosperity, placement in ministry office.
> Positive: Oil poured over the head speaks of anointing for ministry and being made the Lord's beautiful bride. Oil applied to specific body parts speaks of healing and restoration.
> Negative: Spoiled oil means the anointing has been tainted with sin—the enemy gaining a stronghold.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Oil | 油 | 恩膏和医治 |
| Anointing | 恩膏 | 圣灵的膏抹 |
| Healing | 医治 | 身体的恢复 |
| Spoiled | 败坏 | 被污染的 |

### English Paraphrase

Oil represents anointing, healing, cleansing, beautifying, the Holy Spirit, restoration, prosperity, and ministry office placement. Oil poured over the head speaks of ministry anointing and being the Lord's bride. Oil on specific body parts speaks of healing. Spoiled oil means the anointing has been tainted with sin.

### Chinese Interpretation

油代表恩膏、医治、洁净、美化、圣灵、恢复、昌盛和事工职分的安置。倒在头上的油象征事工的恩膏和成为主的新娘。抹在特定身体部位的油象征医治。败坏的油意味着恩膏被罪污染了。

### Core Points

1. **正负皆可**: 油的状态决定含义
2. **恩膏象征**: 圣灵的膏抹
3. **医治记号**: 身体的恢复
4. **败坏警告**: 恩膏可能被污染

### Narrative Snippets

- `[ns_dav_o004]` `[trigger: oil_anointing]` `[factor_trigger: dream_oil AND dream_anointing]` `[role: 主干]` Oil poured over your head speaks of anointing for ministry and being made the Lord's beautiful bride. → 倒在你头上的油象征事工的恩膏和成为主美丽的新娘。
- `[ns_dav_o005]` `[trigger: oil_spoiled]` `[factor_trigger: dream_oil AND dream_spoiled]` `[role: 警告]` Spoiled oil means the anointing has been tainted with sin—the enemy gaining a stronghold. → 败坏的油意味着恩膏被罪污染——仇敌得到了据点。"""
    normalized_text_zh: str = """"""
    subject: str = "Oil 油/恩膏"
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
        l1_anchor="dvd_v1.0.0_oil_油_恩膏_001_L1",
    )
    version: str = "1.0.0"
