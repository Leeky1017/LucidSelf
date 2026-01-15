"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238090
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
    semantic_id="ap_v1.0.0_entry_3__angular__succedent__c_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3AngularSuccedentC(SemanticEntry):
    """
    **Source Text** (Lines 7297-7355):
> This will be supplemented by an interpretation of the signs on ...
    """
    
    original_text: str = """**Source Text** (Lines 7297-7355):
> This will be supplemented by an interpretation of the signs on the cusps of the other houses. The "succedent" houses (second, fifth, eighth, eleventh) signify the reaction to the action expressed in the "angular" houses (first, fourth, seventh, tenth)...
>
> The "cadent" houses... face either the result of the loss implied in the succedent houses or the workings and expression of the psychological mode of operation (angular) after it has been focalized (succedent)...
>
> The twelfth house signifies negatively the vanishing of our social ideals and our hopes... Or else it signifies the closing chapter of a period well lived and the transition to a new birth at a higher level of selfhood.

**Key Term Analysis**:
- **Angular houses (1,4,7,10)**: `action` / `four basic psychological modes` / `dharma of native`
- **Succedent houses (2,5,8,11)**: `reaction to angular` / `consolidation or loss` / `focalization`
- **Cadent houses (3,6,9,12)**: `result of succedent` / `expression or disintegration` / `transition`

**English Paraphrase (Primary Language)**:
Three house types:
- **Angular (1,4,7,10)**: Basic action, four psychological modes (intuition/feeling/sensation/thinking)
- **Succedent (2,5,8,11)**: Reaction—consolidation OR astro_loss of angular matters
- **Cadent (3,6,9,12)**: Result—expression/working-out OR astro_disintegration/transition

The 12th house = "vanishing of ideals" or "closing chapter and transition to new birth at higher level."

**Complete Chinese Interpretation (Secondary Language)**:
三种宫位类型：
- **始宫（1,4,7,10）**：基本行动，四种心理模式（直觉/感受/感官/思维）
- **续宫（2,5,8,11）**：反应——巩固或失去始宫事务
- **果宫（3,6,9,12）**：结果——表达/运作或解体/过渡

第12宫="理想的消失"或"一个阶段的结束章节和向更高自性层次的新生过渡。"

**Narrative Snippets**:
- `[ns_aop_159]` `[trigger: angular_succedent_cadent]` `[factor_trigger: astro_house_types AND house_types]` `[role: 主干]` Three house types: Angular (action), Succedent (reaction), Cadent (result). → L7297-7323
- `[ns_aop_160]` `[trigger: twelfth_house]` `[factor_trigger: astro_house_12]` `[role: 总结]` 12th house: vanishing of ideals OR astro_transition to higher birth. → L7349-7355"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Angular, Succedent, Cadent Houses"
    factor_refs: list = ['houses_angular', 'houses_succedent', 'houses_cadent']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_3__angular__succedent__c_001_L1",
    )
    version: str = "1.0.0"
