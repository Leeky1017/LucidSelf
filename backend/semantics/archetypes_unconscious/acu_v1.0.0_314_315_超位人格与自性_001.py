"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.552729
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
    semantic_id="acu_v1.0.0_314_315_超位人格与自性_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 314315超位人格与自性(SemanticEntry):
    """
    **原文** (§314-315, 行5284-5321):

> [314] The "supraordinate personality" is the total man, i.e., man ...
    """
    
    original_text: str = """**原文** (§314-315, 行5284-5321):

> [314] The "supraordinate personality" is the total man, i.e., man as he really is, not as he appears to himself. To this wholeness the unconscious psyche also belongs, which has its requirements and needs just as consciousness has...
>
> [315] I usually describe the supraordinate personality as the "self," thus making a sharp distinction between the ego, which, as is well known, extends only as far as the conscious mind, and the whole of the personality, which includes the unconscious as well as the conscious component. The ego is thus related to the self as part to whole. To that extent the self is supraordinate. Moreover, the self is felt empirically not as subject but as object... The human figures are father and son, mother and daughter, king and queen, god and goddess. Theriomorphic symbols are the dragon, snake, elephant, lion, bear, and other powerful animals, or again the spider, crab, butterfly, beetle, worm, etc. Plant symbols are generally flowers (lotus and rose). These lead on to geometrical figures like the circle, the sphere, the square, the quaternity, the clock, the firmament, and so on.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Supraordinate personality | 超位人格 | 自性 | 整体人格 |
| Self (自性) | 自我 | 意识+无意识整体 | 个体化目标 |
| Ego (自我) | 我 | 意识中心 | 部分 |
| Theriomorphic (兽形) | 动物形态 | 本能层面 | 象征 |

**英文释义（主语言）**:

**超位人格的定义**：
"超位人格"是**完整的人**，即人真正的样子，而非他自以为的样子。这个整体性也包括无意识心灵，后者有其自身的要求和需要，正如意识一样。

**自性的定义**：
荣格通常将超位人格描述为**"自性"(self)**，从而在**自我(ego)**——众所周知只延伸到意识心智——与**整体人格**——包括无意识和意识成分——之间做出**明确区分**。

**自我与自性的关系**：
自我与自性的关系是**部分与整体**的关系。在这个意义上自性是超位的。此外，自性在经验上**不是作为主体而是作为客体**被感受到。

**自性的象征**：
由于无意识成分，自性只能**部分地**被人类形象表达；其余部分必须由客观的、抽象的象征表达：
- **人类形象**：父与子、母与女、国王与王后、神与女神
- **兽形象征**：龙、蛇、象、狮、熊等强大动物，或蜘蛛、蟹、蝴蝶、甲虫、虫等
- **植物象征**：通常是花（莲花和玫瑰）
- **几何形象**：圆、球、方、四位一体、钟表、天穹等

**完整中文诠释（次语言）**:

**超位人格=完整的人**：
"超位人格"是**完整的人**，即人真正的样子，而非他自以为的样子。这个整体性也包括无意识心灵，后者有其自身的要求和需要，正如意识一样。荣格不想个人主义地解释无意识，比如断言上述幻想图像是压抑造成的"愿望满足"。这些图像本身从未是意识的，因此不可能被压抑。

**自性=整体人格**：
荣格通常将超位人格描述为"自性"，从而在自我——只延伸到意识心智——与整体人格——包括无意识和意识成分——之间做出明确区分。自我与自性的关系是**部分与整体**的关系。在这个意义上自性是超位的。此外，自性在经验上不是作为主体而是作为客体被感受到，这是因为其无意识成分只能通过投射间接进入意识。

**自性的多层象征表达**：
由于无意识成分的不确定范围，对人格的全面描述是不可能的。因此，无意识用从动物到神圣的活形象补充这个画面——作为人之外的两个极端——并通过添加植物和无机抽象把动物极端圆满为一个微观宇宙。

**核心要点**:
- 超位人格 = 完整的人 = 人真正的样子
- 自性 = 整体人格（意识+无意识）
- 自我与自性 = 部分与整体
- 自性作为客体而非主体被经验
- 自性象征：人类形象、兽形、植物、几何形象
- 无意识用多层象征补充人格描述

**叙事片段**:
- `[ns_cw9i_V_314_001]` `[trigger: supraordinate]` `[factor_trigger: jung_self AND jung_wholeness]` `[role: 主干]` 超位人格=完整的人=真正的人——包括无意识心灵及其要求和需要。→ §314
- `[ns_cw9i_V_315_001]` `[trigger: self_symbols]` `[factor_trigger: jung_self AND jung_symbols]` `[role: 主干依赖]` 自性象征：人类形象、兽形、植物、几何形象——从动物到神圣补充人格描述。→ §315"""
    normalized_text_zh: str = """"""
    subject: str = "§314-315 超位人格与自性"
    factor_refs: list = ['engine_id', 'supraordinate_total', 'psych_semantic', 'ego_self_relation', 'psych_semantic', 'self_as_object', 'psych_semantic', 'four_symbol_levels', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_314_315_超位人格与自性_001_L1",
    )
    version: str = "1.0.0"
