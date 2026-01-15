"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535990
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
    semantic_id="acu_v1.0.0_295_297_神圣婚姻与对立统一_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 295297神圣婚姻与对立统一(SemanticEntry):
    """
    **原文** (¶295-297, 行5010-5059):

> [295] The idea of the coniunctio of male and female, which became ...
    """
    
    original_text: str = """**原文** (¶295-297, 行5010-5059):

> [295] The idea of the coniunctio of male and female, which became almost a technical term in Hermetic philosophy, appears in Gnosticism as the mysterium iniquitatis. Such things are hinted at by the quotation from the Gospel according to the Egyptians: "When the two shall be one, the outside as the inside, and the male with the female neither male nor female." The primordial image of the hieros gamos was sublimated in Church mysticism, while in Hermetic philosophy the coniunctio was performed in the abstract theory of the coniugium solis et lunae (marriage of sun and moon).
>
> [296] The primordial image of the hermaphrodite reappears in modern psychology as the male-female antithesis—male consciousness and personified female unconscious. The new psychology acknowledges the existence of an autonomous female psyche where a feminine consciousness confronts a masculine personification of the unconscious (the animus rather than anima).
>
> [297] Originally this archetype played its part entirely in the field of fertility magic as a purely biological phenomenon. But the symbolical meaning increased. The Church severed the coniunctio from the physical realm, and natural philosophy turned it into an abstract theoria. These developments meant the gradual transformation of the archetype into a psychological process—a combination of conscious and unconscious processes.

**英文释义**：
- Coniunctio = 男女结合 → 赫尔墨斯哲学术语
- 诺斯底主义中 = mysterium iniquitatis (邪恶奥秘)
- 埃及福音书："当二合一，外如内，男与女非男非女"
- 神圣婚姻在教会神秘主义中升华
- 赫尔墨斯哲学中 = 日月婚姻抽象理论
- 现代心理学：雌雄同体 → 男性意识 + 女性无意识人格化
- 女性心理学：女性意识 + 男性无意识（阿尼姆斯）
- 原型演变：生育魔法 → 象征意义增加 → 心理过程

**中文诠释**：
- 结合（coniunctio）= 赫尔墨斯哲学核心术语
- 诺斯底主义理解为"邪恶奥秘"（mysterium iniquitatis）
- 古代经文："二合一，外如内，男女非男非女"
- 教会神秘主义：神圣婚姻升华为精神层面
- 赫尔墨斯哲学：抽象化为日月结合理论
- 现代心理学转化：男性意识 + 阿尼玛（女性无意识）
- 新发现：女性意识 + 阿尼姆斯（男性无意识）
- 历史演变：从生育魔法 → 象征 → 心理过程（意识与无意识结合）

**Narrative Snippets**:
- `[ns_cw9i_IV_295]` `[trigger: coniunctio]` `[factor_trigger: jung_opposites AND jung_gnosis]` `[role: 主干]` Coniunctio in Gnosticism as mysterium iniquitatis; Gospel of Egyptians: "When two shall be one, male with female neither male nor female." → ¶295
- `[ns_cw9i_IV_296]` `[trigger: hermaphrodite]` `[factor_trigger: jung_anima AND jung_animus]` `[role: 主干依赖]` Hermaphrodite in modern psychology = male-female antithesis; woman has animus (masculine unconscious), man has anima. → ¶296
- `[ns_cw9i_IV_297]` `[trigger: archetype_evolution]` `[factor_trigger: jung_archetype AND jung_development]` `[role: 条件分支]` Archetype evolved from fertility magic → symbolic meaning → psychological process combining conscious and unconscious. → ¶297"""
    normalized_text_zh: str = """"""
    subject: str = "¶295-297 神圣婚姻与对立统一"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_295_297_神圣婚姻与对立统一_001_L1",
    )
    version: str = "1.0.0"
