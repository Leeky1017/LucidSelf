"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.519993
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
    semantic_id="acu_v1.0.0_第三_1节_理性与眼睛_劣势功能与自性___539_544_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第三1节理性与眼睛劣势功能与自性539544(SemanticEntry):
    """
    **原文** (¶539-544, 行8429-8498):

> [539-540] The picture's form was not unreservedly welcome to the p...
    """
    
    original_text: str = """**原文** (¶539-544, 行8429-8498):

> [539-540] The picture's form was not unreservedly welcome to the patient's conscious mind. She discovered two factors: reason and the eyes. Reason wanted the picture as it "ought to be"; but the eyes held fast to their vision. For anyone with a personalistic view (Freudian), this looks like repression—but the repression was manoeuvred by the unconscious from the start. The unconscious goes straight for its goal: allowing an individual to become whole.
>
> [541] Lightning = intuition. Miss X was a sensation type; her "inferior" function would be intuition—the releasing or "redeeming" function. The inferior function compensates and balances the "superior" function. It is not at the disposal of consciousness, never loses its autonomy. Its role is that of a deus ex machina. It depends on the self, not the ego. It thrusts the ego aside for the totality of a person (conscious + unconscious). This self was always present but sleeping, like Nietzsche's "image in the stone."
>
> [542-544] The circle = mandala, the psychological expression of the totality of the self. These pictures are genuine creations of the unconscious. The sphere signifies the self; other spheres in the picture must represent her intimate friends. The pyramids are unconscious contents "pushing up" into consciousness. Gold expresses sunlight, value, divinity—the aurum philosophicum.

**英文释义**：
- 理性想要画作"应该"的样子；眼睛坚持其视觉
- 这不是意识的压抑——是无意识从一开始就操纵的
- 无意识直接朝向目标：让个体变得完整
- 闪电 = 直觉 = 劣势功能 = 释放/救赎功能
- 劣势功能补偿/平衡优势功能
- 它不受意识支配，角色是deus ex machina
- 它将自我推开，为人的整体性（意识+无意识）腾出空间
- 自性一直存在但沉睡（尼采："石中之像"）
- 圆 = 曼陀罗 = 自性整体的心理表达
- 金色 = 阳光/价值/神性 = 哲人金

**中文诠释**：
- 理性vs眼睛：理性想要"应该的样子"；眼睛坚持视觉
- 压抑不是意识所为——无意识从一开始操纵
- 无意识直接朝向目标：让个体变得完整
- 闪电 = 直觉 = 劣势功能 = 释放/救赎功能
- 劣势功能补偿优势功能；不受意识支配
- 角色 = deus ex machina；依赖自性非自我
- 劣势功能将自我推开，为整体性腾出空间
- 自性一直存在但沉睡——尼采"石中之像"
- 曼陀罗 = 自性整体的心理表达
- 金色 = 阳光/价值/神性 = aurum philosophicum

**Narrative Snippets**:
- `[ns_cw9i_IX_540]` `[trigger: unconscious_goal]` `[factor_trigger: jung_unconscious AND jung_wholeness]` `[role: 主干]` The unconscious goes straight for its goal: allowing an individual to become whole—not a personal imbroglio. → ¶540
- `[ns_cw9i_IX_541]` `[trigger: inferior_function]` `[factor_trigger: jung_function AND jung_self]` `[role: 主干依赖]` Inferior function = deus ex machina, depends on self not ego; thrusts ego aside for totality. Self was always present but sleeping. → ¶541
- `[ns_cw9i_IX_543]` `[trigger: gold_symbol]` `[factor_trigger: jung_gold AND jung_consciousness]` `[role: 条件分支]` Gold = sunlight, value, divinity—the aurum philosophicum. Pyramids = unconscious contents pushing up into consciousness. → ¶543"""
    normalized_text_zh: str = """"""
    subject: str = "第三.1节：理性与眼睛、劣势功能与自性 (¶539-544)"
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
        l1_anchor="acu_v1.0.0_第三_1节_理性与眼睛_劣势功能与自性___539_544_001_L1",
    )
    version: str = "1.0.0"
