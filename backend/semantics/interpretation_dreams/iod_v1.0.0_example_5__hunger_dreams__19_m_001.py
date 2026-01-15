"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460954
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
    semantic_id="iod_v1.0.0_example_5__hunger_dreams__19_m_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class Example5HungerDreams19M(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Hallucinatory Satisfaction | Sensory experience of wish | Most primitive level |
| Primary Process | Wish→sensory image direct | Infantile mode |
| Regression | Adult returns to infantile | Sleep mechanism |
| Ownership Declaration | "Anna Freud" = mine | Possession wish |

**Source Text** (Freud's youngest daughter after day of fasting):
"Anna Feud, strawberry, huckleberry, omelette, pap!" (called out in sleep)

**Analysis**:
- **Stimulus**: Vomited, kept without food entire day (hunger)
- **Dream response**: Hallucinatory feast of desired foods
- **Name usage**: "Anna Feud" = expressing **ownership** of feast
- **Repetition**: Berries twice = **revenge** against nurse who blamed berries for illness
- **Mechanism**: **Hallucinatory wish-fulfillment** at most primitive level

**Key Mechanism**: **Hallucinatory Satisfaction** (幻觉满足)
- Dream provides **sensory experience** of satisfaction when real satisfaction unavailable
- Primitive mental apparatus: Cannot distinguish hallucination from reality
- **Primary process thinking**: Direct transformation of wish into sensory image
- Sleep regression: Adult dreams return to this infantile mode

**Complete Chinese Interpretation (Secondary Language)**:

“饥饿梦”发生在弗洛伊德最小的女儿 Anna 身上：在呕吐之后，她被迫整日禁食，入睡后在梦中呼喊“Anna Freud，草莓、蓝莓、煎蛋、粥！”这里几乎没有任何复杂剧情，只有一连串她平日喜爱的食物名称，以及把自己名字放在最前面、仿佛在宣布“这一切都属于我”。

这个梦极为清楚地展示了所谓**幻觉满足**的机制：在现实中，进食被严格禁止，欲望完全无法通过行动得到满足；在梦里，心灵便通过声音与想象性的味觉/视觉体验，构造出一场内在的“盛宴”，让主体仿佛已经重新获得那些被剥夺的食物。对于尚未建立稳定现实检验能力的婴儿来说，这种幻觉体验与真实进食在当下的感受上几乎没有差别。

同时，梦中对草莓的重复与强调，也可以被读作对责怪草莓“导致生病”的保姆的一种**报复性修正**：在梦里，她不仅重新拿回草莓，而且强化其存在，好像在说“我依然要吃”。在这一层意义上，饥饿梦不仅满足了口欲，也悄然扭转了权威他人对欲望施加的限制。对成年人而言，许多看似复杂的梦，实质上也是在这种原始模式上发生的**退行**——通过幻觉性场景，临时弥补现实中无法满足或被禁止的需求，这便是原初过程思维在睡眠中的再现。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Hunger Dream (Anna Freud): Most primitive hallucinatory satisfaction. 19-month-old lists desired foods in sleep. Primary process: direct wish→sensory image. Revenge component (berries repeated despite blame).
- **中文**: 饥饿梦(Anna Freud):最原始的幻觉满足。19个月婴儿在睡眠中列出想要的食物。原初过程:直接愿望→感官图像。复仇成分(尽管被责怪仍重复草莓)。

**Narrative Snippets**:
- `[ns_freud_ex_013]` `[trigger: hallucinatory_satisfaction]` `[factor_trigger: infant_dreams]` `[role: 主干]` Hunger Dream: most primitive hallucinatory satisfaction; direct wish→sensory image. → Core
- `[ns_freud_ex_014]` `[trigger: primary_process]` `[factor_trigger: infant_dreams AND mental_apparatus]` `[role: 条件分支]` Primary process: cannot distinguish hallucination from reality; infantile mode. → Mechanism
- `[ns_freud_ex_015]` `[trigger: sleep_regression]` `[factor_trigger: infant_dreams AND adult_dreams]` `[role: 条件分支]` Sleep regression: adult dreams return to this primitive hallucinatory mode. → Theory"""
    normalized_text_zh: str = """"""
    subject: str = "Example 5: Hunger Dreams (19-month-old Anna Freud)"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_example_5__hunger_dreams__19_m_001_L1",
    )
    version: str = "1.0.0"
