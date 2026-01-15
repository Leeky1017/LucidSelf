"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008015
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
    semantic_id="lt_v1.0.0_the_hierophant__教皇_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheHierophant教皇(SemanticEntry):
    """
    **Source Text** (Lines 3785-3849):
> **Keywords**: Education • Belief Systems • Conformity • Group I...
    """
    
    original_text: str = """**Source Text** (Lines 3785-3849):
> **Keywords**: Education • Belief Systems • Conformity • Group Identification
>
> **Actions**:
> - **Getting an Education**: pursuing knowledge, becoming informed, increasing understanding, studying and learning, seeking a deeper meaning, finding out more
> - **Having a Belief System**: sharing a cultural heritage, learning a religious tradition, honoring ritual and ceremony, identifying a world view, following a discipline, knowing where to put your faith
> - **Conforming**: following the rules, taking an orthodox approach, staying within conventional bounds, adapting to the system, fitting in, going along with the program, doing what's expected, being part of the Establishment
> - **Identifying with a Group**: being committed to a cause, devoting energy to a group, joining an organization, working as part of a team, feeling loyal to others, being in an institutionalized setting
>
> **Description**: The Hierophant represents all structured groups with rules and assigned roles... Such environments emphasize belief systems—facts, rules, procedures, and ritual. Members are rewarded for following conventions.

**Key Term Analysis**:
- **The Hierophant (5)**: `structured groups` / `rules and assigned roles` / `belief systems`
- **Education**: `pursuing knowledge` / `studying and learning` / `deeper meaning`
- **Belief Systems**: `cultural heritage` / `religious tradition` / `ritual and ceremony`
- **Conformity**: `following rules` / `orthodox approach` / `conventional bounds`
- **Group Identification**: `committed to a cause` / `team` / `institutionalized setting`

**English Paraphrase (Primary Language)**:
**The Hierophant (Card 5)** represents "structured groups with rules and assigned roles"—churches, schools, companies, societies. He is the **counterpoint to the Lovers (Card 6)**:
- **Hierophant**: Group beliefs, conformity, tradition, institution
- **Lovers**: Personal beliefs, individual choice, own standards

**Four domains**:
1. **Education**: Formal learning, pursuing knowledge, seeking deeper meaning
2. **Belief Systems**: Religion, tradition, ritual, world view—shared frameworks
3. **Conformity**: Following rules, orthodox approach, fitting in, doing what's expected
4. **Group Identification**: Teams, organizations, causes—belonging to something larger

**Reading implication**: "The Hierophant can show that you are struggling with a force that is not innovative, free-spirited, or individual. Groups can be enriching or stifling, depending on circumstances."

**Complete Chinese Interpretation (Secondary Language)**:
**教皇（第5号牌）**代表"有规则和分配角色的结构化群体"——教会、学校、公司、社会。他是**恋人（第6号牌）的对照**：
- **教皇**：群体信仰、顺从、传统、制度
- **恋人**：个人信仰、个人选择、自己的标准

**四个领域**：
1. **教育**：正式学习、追求知识、寻求更深意义
2. **信仰系统**：宗教、传统、仪式、世界观——共享框架
3. **顺从**：遵守规则、正统方法、融入、按预期行事
4. **群体认同**：团队、组织、事业——属于更大的东西

**解读含义**："教皇可以显示你正在与一种不创新、不自由、不个人的力量斗争。群体可以丰富或窒息，取决于情况。"

**Core Points**:
- Card 5 = structured groups, rules, assigned roles
- Counterpoint to Lovers (Card 6) = group vs personal beliefs
- Education: formal learning, knowledge, deeper meaning
- Belief Systems: religion, tradition, ritual, shared world view
- Conformity: following rules, orthodox, fitting in
- Group Identification: teams, organizations, belonging

**Narrative Snippets**:
- `[ns_ltt_036]` `[trigger: hierophant_card]` `[factor_trigger: tarot_hierophant AND conformity AND group_identity]` `[role: 主干]` The Hierophant represents structured groups with rules and assigned roles—churches, schools, companies, societies. → L3838-3840
- `[ns_ltt_037]` `[trigger: hierophant_belief]` `[factor_trigger: tarot_hierophant AND tarot_belief]` `[role: 主干依赖]` Such environments emphasize belief systems—facts, rules, procedures, and ritual. Members are rewarded for following conventions. → L3840-3842
- `[ns_ltt_038]` `[trigger: hierophant_tension]` `[factor_trigger: tarot_hierophant AND tarot_conflict]` `[role: 条件分支]` The Hierophant can show you are struggling with a force that is not innovative, free-spirited, or individual—groups can be enriching or stifling. → L3847-3849"""
    normalized_text_zh: str = """"""
    subject: str = "The Hierophant (教皇)"
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
        l1_anchor="lt_v1.0.0_the_hierophant__教皇_001_L1",
    )
    version: str = "1.0.0"
