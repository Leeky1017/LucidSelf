"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535976
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
    semantic_id="acu_v1.0.0_294_雌雄同体转化为自性象征_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 294雌雄同体转化为自性象征(SemanticEntry):
    """
    **原文** (¶294, 行4998-5008):

> [294] As civilization develops, the bisexual primordial being turns in...
    """
    
    original_text: str = """**原文** (¶294, 行4998-5008):

> [294] As civilization develops, the bisexual primordial being turns into a symbol of the unity of personality, a symbol of the self, where the war of opposites finds peace. In this way the primordial being becomes the distant goal of man's self-development, having been from the very beginning a projection of his unconscious wholeness. Wholeness consists in the union of the conscious and the unconscious personality. Just as every individual derives from masculine and feminine genes, and the sex is determined by the predominance of the corresponding genes, so in the psyche it is only the conscious mind, in a man, that has the masculine sign, while the unconscious is by nature feminine. The reverse is true in the case of a woman. All I have done in my anima theory is to rediscover and reformulate this fact.

**英文释义（主语言）**:

**雌雄同体转化为自性象征**：
随着文明发展，双性原初存在转化为**人格统一的象征——自性的象征**，在此对立面的战争找到和平。

**原初存在 = 自我发展的遥远目标**：
原初存在成为人自我发展的**遥远目标**，从一开始就是其无意识整体性的投射。

**整体性的定义**：
整体性在于**意识人格与无意识人格的统一**。

**心理学的性别对位**：
- 每个个体都来自男性和女性基因，性别由相应基因的优势决定
- 心灵中，男性的意识心智具有男性标志，而无意识天生是女性的
- 女性则相反
- 荣格的阿尼玛理论只是重新发现和重新表述了这个事实

**完整中文诠释（次语言）**:

**从雌雄同体到自性象征**：
随着文明发展，双性原初存在转化为**人格统一的象征——自性的象征**，在此对立面的战争找到和平。原初存在因此成为人自我发展的**遥远目标**，从一开始就是其无意识整体性的投射。

**整体性的核心定义**：
整体性在于**意识人格与无意识人格的统一**。

**心理学的性别互补原理**：
正如每个个体都来自男性和女性基因，性别由相应基因的优势决定，心灵中也是如此：
- 男性的意识心智具有男性标志，而无意识天生是女性的
- 女性则相反：女性的意识心智是女性的，无意识是男性的

荣格指出，他的阿尼玛理论只是重新发现和重新表述了这个古已有之的事实。

**核心要点**:
- 双性原初存在 → 人格统一象征 = 自性象征
- 在自性中对立面的战争找到和平
- 原初存在 = 自我发展的遥远目标 = 无意识整体性的投射
- 整体性 = 意识 + 无意识人格的统一
- 男性：意识=男性，无意识=女性（阿尼玛）
- 女性：意识=女性，无意识=男性（阿尼姆斯）

**叙事片段**:
- `[ns_cw9i_IV_294_001]` `[trigger: hermaphrodite_self]` `[factor_trigger: jung_hermaphrodite AND jung_self]` `[role: 主干]` 双性原初存在转化为自性象征——对立面战争找到和平，成为自我发展的遥远目标。→ ¶294
- `[ns_cw9i_IV_294_002]` `[trigger: anima_animus]` `[factor_trigger: jung_anima AND jung_animus]` `[role: 主干依赖]` 男性无意识天生女性（阿尼玛），女性无意识天生男性（阿尼姆斯）——整体性=意识+无意识统一。→ ¶294"""
    normalized_text_zh: str = """"""
    subject: str = "¶294 雌雄同体转化为自性象征"
    factor_refs: list = ['engine_id', 'hermaphrodite_to_self', 'psych_semantic', 'distant_goal', 'psych_semantic', 'wholeness', 'psych_semantic', 'anima_animus', 'psych_semantic']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_294_雌雄同体转化为自性象征_001_L1",
    )
    version: str = "1.0.0"
