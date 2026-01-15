"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.401946
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
    semantic_id="dvd_v1.0.0_darkness_黑暗_迷惑_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Darkness黑暗迷惑(SemanticEntry):
    """
    ### Source Text

> **Darkness**: Opposite to everything light. Is a picture of sin, deception, confu...
    """
    
    original_text: str = """### Source Text

> **Darkness**: Opposite to everything light. Is a picture of sin, deception, confusion and all the works of the enemy.
> To walk in darkness means to be led astray or to be confused. As believers we are called to walk in the light. Darkness never has a positive picture as it is the opposite of light—which is the very essence of God!
> 1 John 2:11 "But he that hates his brother is in darkness, and walks in darkness, and knows not where he goes, because that darkness has blinded his eyes."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Darkness | 黑暗 | 罪和迷惑 |
| Deception | 迷惑 | 被引入歧途 |
| Confusion | 混乱 | 不知方向 |
| Enemy | 仇敌 | 撒但和邪灵的领域 |

### English Paraphrase

Darkness is opposite to light, representing sin, deception, confusion, and enemy's works. To walk in darkness means being led astray. Satan and demons dwell in darkness. Light, life, and love are interchangeable in Scripture; darkness, hate, and death are their opposites.

### Chinese Interpretation

黑暗是光的对立面，代表罪、迷惑、混乱和仇敌的工作。行走在黑暗中意味着被引入歧途。撒但和邪灵住在黑暗中。圣经中光、生命、爱是互换的；黑暗、仇恨、死亡是它们的对立面。

### Core Points

1. **始终负面**: 黑暗没有正面含义
2. **罪的象征**: 与神的本质相反
3. **迷惑状态**: 不知道往哪里去
4. **仇敌领域**: 撒但和邪灵的居所

### Narrative Snippets

- `[ns_dav_d003]` `[trigger: darkness_sin]` `[factor_trigger: dream_darkness AND dream_sin]` `[role: 主干]` Darkness is the opposite of light—representing sin, deception, confusion and all works of the enemy. → 黑暗是光的对立面——代表罪、迷惑、混乱和仇敌的一切工作。
- `[ns_dav_d004]` `[trigger: darkness_blind]` `[factor_trigger: dream_darkness AND dream_blindness]` `[role: 警告]` He that walks in darkness knows not where he goes—darkness has blinded his eyes. → 行走在黑暗中的人不知道往哪里去——黑暗蒙蔽了他的眼睛。"""
    normalized_text_zh: str = """"""
    subject: str = "Darkness 黑暗/迷惑"
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
        l1_anchor="dvd_v1.0.0_darkness_黑暗_迷惑_001_L1",
    )
    version: str = "1.0.0"
