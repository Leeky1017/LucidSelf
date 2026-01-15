"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008003
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
    semantic_id="lt_v1.0.0_the_emperor__皇帝_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheEmperor皇帝(SemanticEntry):
    """
    **Source Text** (Lines 3716-3784):
> **Keywords**: Fathering • Structure • Authority • Regulation
>
...
    """
    
    original_text: str = """**Source Text** (Lines 3716-3784):
> **Keywords**: Fathering • Structure • Authority • Regulation
>
> **Actions**:
> - **Fathering**: establishing a family line, setting direction and tone, protecting and defending, guiding growth, bringing security and comfort, offering explanations
> - **Emphasizing Structure**: creating order out of chaos, categorizing, being systematic, providing shape and form, being organized, applying reason, coordinating, sticking to a plan
> - **Exercising Authority**: taking a leadership role, commanding, exerting control, representing the establishment, being in a position of strength, coming in contact with officials, setting direction
> - **Regulating**: establishing law and order, operating from sound principles, applying rules or guidelines, working within the legal system, setting standards of behavior, following a regimen
>
> **Description**: The Emperor represents structure, order, and regulation—forces to balance the free-flowing, lavish abundance of the Empress. He advocates a four-square world where trains are on time, games are played by rules, and commanding officers are respected.

**Key Term Analysis**:
- **The Emperor (4)**: `structure, order, regulation` / `balance the Empress` / `four-square world`
- **Fathering**: `establishing family line` / `protecting and defending` / `guiding growth`
- **Structure**: `order out of chaos` / `systematic` / `shape and form`
- **Authority**: `leadership role` / `commanding` / `position of strength`
- **Regulation**: `law and order` / `rules and guidelines` / `standards of behavior`

**English Paraphrase (Primary Language)**:
**The Emperor (Card 4)** represents "structure, order, and regulation—forces to balance the free-flowing, lavish abundance of the Empress." He forms a **polarity pair** with the Empress (Card 3):
- **Empress**: Abundance, creativity, nurturing, flowing
- **Emperor**: Structure, discipline, authority, regulated

**Four domains**:
1. **Fathering**: Protection, guidance, establishing direction—"archetypal Father"
2. **Structure**: Order from chaos, systematic organization, applying reason
3. **Authority**: Leadership, command, representing establishment
4. **Regulation**: Laws, rules, standards, working within systems

**Reading implication**: "In chaotic situations, the Emperor can indicate the need for organization... In situations that are already over-controlled, he suggests the confining effect of those constraints."

**Complete Chinese Interpretation (Secondary Language)**:
**皇帝（第4号牌）**代表"结构、秩序和规范——平衡皇后自由流动、慷慨丰盛的力量"。他与皇后（第3号牌）形成**极性配对**：
- **皇后**：丰盛、创造力、滋养、流动
- **皇帝**：结构、纪律、权威、规范

**四个领域**：
1. **父性**：保护、指导、确立方向——"原型父亲"
2. **结构**：从混乱中建立秩序、系统化组织、运用理性
3. **权威**：领导力、命令、代表建制
4. **规范**：法律、规则、标准、在系统内工作

**解读含义**："在混乱情境中，皇帝可以指示需要组织……在已经过度控制的情境中，他暗示这些约束的限制效应。"

**Core Points**:
- Card 4 = structure, order, regulation balancing Empress
- Polarity pair with Empress (Card 3)
- Fathering: protection, guidance, direction
- Structure: order from chaos, systematic, reason-based
- Authority: leadership, command, establishment
- Regulation: laws, rules, standards, systems

**Narrative Snippets**:
- `[ns_ltt_033]` `[trigger: emperor_card]` `[factor_trigger: tarot_emperor AND structure]` `[role: 主干]` The Emperor represents structure, order, and regulation—forces to balance the free-flowing, lavish abundance of the Empress. → L3774-3775
- `[ns_ltt_034]` `[trigger: emperor_balance]` `[factor_trigger: tarot_emperor AND tarot_tarot_empress AND authority]` `[role: 主干依赖]` Emperor and Empress form a polarity pair—Empress is nurturing abundance, Emperor is structured authority. → L3774-3776
- `[ns_ltt_035]` `[trigger: emperor_context]` `[factor_trigger: tarot_emperor AND tarot_situation]` `[role: 条件分支]` In chaotic situations, Emperor indicates need for organization; in over-controlled situations, he suggests confining constraints. → L3777-3780"""
    normalized_text_zh: str = """"""
    subject: str = "The Emperor (皇帝)"
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_the_emperor__皇帝_001_L1",
    )
    version: str = "1.0.0"
