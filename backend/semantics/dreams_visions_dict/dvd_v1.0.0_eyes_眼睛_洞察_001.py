"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.409512
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
    semantic_id="dvd_v1.0.0_eyes_眼睛_洞察_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Eyes眼睛洞察(SemanticEntry):
    """
    ### Source Text

> **Eyes**: A picture of spiritual sight and discernment.
> Positive: To have your ...
    """
    
    original_text: str = """### Source Text

> **Eyes**: A picture of spiritual sight and discernment.
> Positive: To have your eyes anointed speaks of receiving spiritual insight. The eyes are the windows of the soul—seeing clearly speaks of understanding. Eyes wide open represent revelation.
> Negative: Blind eyes speak of spiritual blindness—unable to see the truth. Wandering eyes speak of lust and covetousness.
> Ephesians 1:18 "The eyes of your understanding being enlightened; that you may know what is the hope of his calling..."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Eyes | 眼睛 | 属灵的看见 |
| Discernment | 洞察 | 辨别的能力 |
| Enlightened | 光照 | 悟性被开启 |
| Blind | 瞎眼 | 看不见真理 |

### English Paraphrase

Eyes represent spiritual sight and discernment. Anointed eyes receive spiritual insight—seeing clearly means understanding. Eyes wide open represent revelation. Blind eyes speak of spiritual blindness. Wandering eyes indicate lust. The eyes of understanding being enlightened reveals God's hope and calling.

### Chinese Interpretation

眼睛代表属灵的看见和洞察。被膏抹的眼睛接受属灵的洞见——看得清楚意味着理解。大睁的眼睛代表启示。瞎眼象征属灵的瞎眼。游移的眼睛表示情欲。悟性的眼睛被光照揭示神的盼望和呼召。

### Core Points

1. **正负皆可**: 眼睛状态决定含义
2. **属灵看见**: 洞察真理的能力
3. **启示窗口**: 眼睛是灵魂之窗
4. **瞎眼警告**: 看不见真理是危险的

### Narrative Snippets

- `[ns_dav_e011]` `[trigger: eyes_enlightened]` `[factor_trigger: dream_eyes AND dream_enlightened]` `[role: 主干]` The eyes of your understanding being enlightened—that you may know the hope of His calling. → 你们悟性的眼睛被光照——使你们知道祂呼召的盼望。
- `[ns_dav_e012]` `[trigger: eyes_blind]` `[factor_trigger: dream_eyes AND dream_blind]` `[role: 警告]` Blind eyes speak of spiritual blindness—unable to see the truth or discern the Lord's will. → 瞎眼象征属灵的瞎眼——看不见真理也辨别不出主的旨意。"""
    normalized_text_zh: str = """"""
    subject: str = "Eyes 眼睛/洞察"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="dvd_v1.0.0_eyes_眼睛_洞察_001_L1",
    )
    version: str = "1.0.0"
