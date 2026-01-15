"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.049555
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
    semantic_id="bot_v1.0.0_the_hebrew_and_pagan_systems___001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TheHebrewAndPaganSystems(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Hebrew System | Linear creation | Beginning → End |
| Pagan System | Circular wheel | Eternal cycle |
| The Wheel | Rotation of YHVH | Fortune's turning |
| Daughter Rising | Princess → Queen | Cycle renewal |

**Source Text**:
> "The Hebrew system is straightforward and irreversible; it postulates Father and Mother from whose union issue Son and Daughter. There an end. ... The Pagan system is circular, self-generated, self-nourished, self-renewed. It is a wheel on whose rim are Father-Mother-Son-Daughter; they move about the motionless axis of Zero; they unite at will; they transform one into another; there is neither Beginning nor End to the Orbit; none is higher or lower than another. The Equation 'Naught=Many=Two=One=All=Naught' is implicit in every mode of the being of the System."

**English Paraphrase**:

Crowley identifies **two models** underlying the Tarot:

**Hebrew System (Linear)**:
- **Beginning**: Father + Mother
- **Process**: Union produces Son + Daughter
- **End**: Daughter is the terminal manifestation
- **Character**: Irreversible, hierarchical, causality-based

**Pagan System (Circular)**:
- **Wheel**: Father-Mother-Son-Daughter rotate on the rim
- **Center**: Zero—the motionless axis
- **Character**: Self-generating, self-renewing, no beginning or end
- **Equation**: 0=∞=2=1=All=0 (all states are equivalent)

**The Synthesis**:
The **Daughter rises to the throne of the Mother**. In the linear view, the Daughter is the end; in the circular view, she becomes the new Mother and the cycle repeats. This is the secret of the **Wheel of Fortune** (Atu X).

**完整中文诠释**：

Crowley识别出塔罗背后的**两种模型**：

**希伯来系统（线性）**：
- **开始**：父亲 + 母亲
- **过程**：结合产生儿子 + 女儿
- **结束**：女儿是终点显化
- **特征**：不可逆、等级制、基于因果

**异教系统（循环）**：
- **轮子**：父-母-子-女在轮缘上旋转
- **中心**：零——静止的轴心
- **特征**：自我生成、自我更新、无始无终
- **方程**：0=∞=2=1=一切=0（所有状态等价）

**综合**：
**女儿升至母亲的宝座**。在线性观点中，女儿是终点；在循环观点中，她成为新的母亲，循环重复。这是**命运之轮**（Atu X）的秘密。

#### Core Points

- **Hebrew System**: Linear creation from Father-Mother to Son-Daughter—has beginning and end.
- **Pagan System**: Circular wheel where all four figures rotate around Zero—no hierarchy, eternal return.
- The **Daughter's ascension** to Mother's throne is the **key to cyclic renewal**.
- The **Wheel of Fortune** (Atu X) embodies this eternal rotation.
- **0=∞=2=1=All=0**: The fundamental equation of the Pagan/Thelemic worldview.

**Narrative Snippets**:
- `[ns_thoth_theory_011]` `[trigger: hebrew_pagan]` `[factor_trigger: tarot_philosophy AND tarot_cycle]` `[role: 主干]` Hebrew system is linear (Beginning→End); Pagan system is circular (eternal wheel around Zero). → English Paraphrase
- `[ns_thoth_theory_012]` `[trigger: daughter_rise]` `[factor_trigger: tarot_wheel AND tarot_renewal]` `[role: 主干依赖]` The Daughter rises to the throne of the Mother, renewing the cycle—the secret of the Wheel of Fortune. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "The Hebrew and Pagan Systems (希伯来与异教系统)"
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_the_hebrew_and_pagan_systems___001_L1",
    )
    version: str = "1.0.0"
