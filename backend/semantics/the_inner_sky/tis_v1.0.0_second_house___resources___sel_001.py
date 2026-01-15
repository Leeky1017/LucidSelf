"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.093973
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
    semantic_id="tis_v1.0.0_second_house___resources___sel_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class SecondHouseResourcesSel(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Self-Worth | Inner evalu...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Self-Worth | Inner evaluation | Core crisis |
| Values | What matters | Foundation |
| Concrete Achievement | Proof of worth | Resolution |
| Money as Red Herring | Not real issue | Deeper meaning |

#### Source Text

"Second-house influences create a crisis of self-respect. The way we choose to resolve that insecurity becomes a key life theme. Successful navigation always involves proving oneself to oneself. We compensate for inner doubts through disciplined effort and concrete accomplishment. The real issue: How we evaluate our own worth. Money is just a red herring."

#### English Paraphrase

The **Second House** is the arena of **values, resources, and self-worth**. While traditionally called the "House of Money," its deeper meaning is **self-respect**.

**The Core Crisis**:
- **Insecurity**: We all doubt our worth. The Second House shows where we feel inadequate.
- **Compensation**: We try to prove our worth through what we have or what we can do.

**Manifestations**:
- **Materialism**: Trying to solve inner insecurity with outer objects (money, cars, status symbols).
- **Possessions**: Tools to say "I exist, I matter."
- **Body Image**: Treating the body as an object to be perfected or displayed.

**True Success**:
- **Proving Oneself to Oneself**: Not impressing others, but building genuine competence and self-reliance.
- **Concrete Accomplishment**: Doing things that make us feel capable and valuable.
- **Values**: Defining what truly matters to us, independent of social pressure.

**Money's Role**:
Money is a symbol of energy and value. How we handle money reflects how we handle our own life energy and self-esteem.

#### Complete Chinese Interpretation

**第二宫**是**价值观、资源和自我价值**的领域。虽然传统上称为"财帛宫"，其更深层含义是**自尊**。

**核心危机**：
- **不安全感**：我们都怀疑自己的价值。第二宫显示了我们感到不足的地方。
- **补偿**：我们试图通过我们拥有的或我们能做的来证明我们的价值。

**显化**：
- **物质主义**：试图用外在物品（金钱、车、地位象征）解决内在不安全感。
- **所有物**：用来表达"我存在，我重要"的工具。
- **身体形象**：将身体视为需要完美化或展示的物体。

**真正的成功**：
- **向自己证明自己**：不是为了取悦他人，而是建立真正的能力和自力更生。
- **具体成就**：做那些让我们感到有能力和有价值的事情。
- **价值观**：定义对我们真正重要的事情，独立于社会压力。

**金钱的角色**：
金钱是能量和价值的象征。我们如何处理金钱反映了我们如何处理自己的生命能量和自尊。

#### Core Points

- Crisis of self-respect and self-worth (not just money).
- Proving oneself to oneself through concrete ability.
- Materialism is a symptom of inner insecurity.
- True wealth is confidence in one's own resources.
- East parallel: 财帛宫/身宫/禄 (Wealth Palace, Body Palace, Prosperity).

#### Detailed Explanation

The Second House is fundamentally about **self-worth**, not money. Forrest calls money a "red herring"—the real issue is how we evaluate our own value. Financial behaviors are symptoms, not causes. Compulsive materialism signals inner insecurity; sustainable wealth emerges from genuine self-confidence.

The developmental task is **proving oneself to oneself**. This is different from impressing others or accumulating status symbols. It means developing real competence, building genuine skills, and knowing that one can handle life's demands. This inner confidence then manifests as healthy resource management.

A busy Second House can be either the weakest or strongest chart structure. **Unsuccessful navigation** produces compulsive materialism—trying to fill inner emptiness with outer possessions. **Successful navigation** transforms insecurity into drive, using self-doubt as fuel for genuine accomplishment and growth.

#### Narrative Snippets

- `[ns_innersky_h2_001]` `[trigger: house_2_general]` `[factor_trigger: astro_house_2]` `[role: 主干]` Second-house influences create a crisis of self-respect. And the way we choose to resolve that insecurity becomes a key life theme. → The Inner Sky Ch.7 #2H
- `[ns_innersky_h2_002]` `[trigger: house_2_dysfunction]` `[factor_trigger: astro_house_2 AND astro_state_dysfunction]` `[role: 条件分支]` If we respond negatively, a compulsive kind of materialism warps our consciousness. We seek to alleviate our self-doubts through the manipulation of physical circumstances. → The Inner Sky Ch.7 #2H
- `[ns_innersky_h2_003]` `[trigger: house_2_mastery]` `[factor_trigger: astro_house_2 AND astro_state_success]` `[role: 条件分支]` A successful navigation of second-house terrain always involves proving oneself to oneself. We compensate for inner doubts through disciplined effort and concrete accomplishment. → The Inner Sky Ch.7 #2H
- `[ns_innersky_h2_004]` `[trigger: house_2_potential]` `[factor_trigger: astro_house_2]` `[role: 主干依赖]` Properly harnessed, personal insecurity can drive a person to reach toward the limits of growth. A busy second house can be the weakest possible astrological structure or the most resilient. → The Inner Sky Ch.7 #2H
- `[ns_innersky_h2_005]` `[trigger: house_2_money]` `[factor_trigger: astro_house_2]` `[role: 总结]` How we evaluate our own worth is the real issue. Money is just a red herring. → The Inner Sky Ch.7 #2H"""
    normalized_text_zh: str = """"""
    subject: str = "Second House - Resources & Self-Worth"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_second_house___resources___sel_001_L1",
    )
    version: str = "1.0.0"
