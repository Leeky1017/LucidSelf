"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429299
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
    semantic_id="dvd_v1.0.0_jesus_耶稣_主_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Jesus耶稣主(SemanticEntry):
    """
    ### Source Text

> **Jesus**: In dreams, someone close to you will be symbolic of Jesus—often your s...
    """
    
    original_text: str = """### Source Text

> **Jesus**: In dreams, someone close to you will be symbolic of Jesus—often your spouse. In visions, to have a face-to-face relationship with Jesus is available to every believer.
> Negative: I have often seen a picture of the Lord Jesus as in religious artistic portrayals. When I see this in the spirit, I know the person is bound by legalism. The Lord Jesus is accepting and loving—if you feel fear or guilt in His presence, reject it as deception.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Jesus | 耶稣 | 主和救主 |
| Spouse | 配偶 | 梦中代表主 |
| Legalism | 律法主义 | 宗教束缚 |
| Loving | 慈爱 | 主的性情 |

### English Paraphrase

In dreams, someone close to you (often your spouse) symbolizes Jesus. In visions, a face-to-face relationship with Jesus is available to every believer. Religious artistic portrayals indicate legalism. The Lord is accepting and loving—fear or guilt in His presence is deception.

### Chinese Interpretation

在梦中，与你亲近的人（常是配偶）象征耶稣。在异象中，每个信徒都可以与耶稣面对面。宗教艺术形象表示律法主义。主是接纳和慈爱的——在祂面前感到恐惧或内疚是迷惑。

### Core Points

1. **通常正面**: 主的形象是祝福
2. **梦中代表**: 配偶常代表主
3. **面对面**: 每个信徒都可以
4. **律法警告**: 宗教形象是束缚

### Narrative Snippets

- `[ns_dav_j002]` `[trigger: jesus_spouse]` `[factor_trigger: dream_jesus AND dream_spouse]` `[role: 主干]` In dreams, someone close to you—often your spouse—symbolizes Jesus and your relationship with Him. → 在梦中，与你亲近的人——常是配偶——象征耶稣和你与祂的关系。
- `[ns_dav_j003]` `[trigger: jesus_legalism]` `[factor_trigger: dream_jesus AND dream_legalism]` `[role: 警告]` Religious artistic portrayals of Jesus indicate legalism—He is accepting and loving, not fearful. → 宗教艺术对耶稣的描绘表示律法主义——祂是接纳和慈爱的，不是可怕的。"""
    normalized_text_zh: str = """"""
    subject: str = "Jesus 耶稣/主"
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
        l1_anchor="dvd_v1.0.0_jesus_耶稣_主_001_L1",
    )
    version: str = "1.0.0"
