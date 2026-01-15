"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251649
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
    semantic_id="pit_v1.0.0_uranus_cycle__84_years___天王星周期_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusCycle84Years天王星周期(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Uranus's 84-year orbital period spans most of a human li...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Uranus's 84-year orbital period spans most of a human lifetime. Most people experience Uranus opposition (around age 42) rather than return. Uranus rules revolutionary change, liberation, awakening, and individuation. The Uranus cycle represents the mid-life crisis archetype and the need for authentic self-expression."

**English Paraphrase (Primary Language)**:
The **Uranus cycle** (84 years) is astrology's **revolutionary and individuation cycle**, spanning most of a human lifetime. Uranus symbolizes **liberation principle**: revolutionary change, awakening, individuation, authenticity, rebellion against limitations, breakthrough. Unlike Saturn (maturation) or Jupiter (expansion), Uranus **disrupts and liberates**. The 84-year cycle is so long that most people never experience a Uranus return (which would occur around age 84). Instead, the most significant Uranus transit is the **opposition** (around age 42)—when transiting Uranus opposes its natal position. Hand emphasizes that the Uranus opposition is the **mid-life crisis archetype**: a moment of awakening when you ask "Is this all there is? Am I living authentically?" This often triggers rebellion against limitations, need for authentic self-expression, and life restructuring. The Uranus cycle represents the **individuation process**—becoming your true self rather than conforming to others' expectations. Revolutionary change, liberation from false identities, and breakthrough into authenticity are Uranus's gifts.

**Complete Chinese Interpretation (Secondary Language)**:
**天王星周期**（84 年）是占星学的**革命和个体化周期**，跨越大部分人类一生。天王星象征**解放原则**：革命性改变、觉醒、个体化、真实性、反抗限制、突破。与土星（成熟）或木星（扩展）不同，天王星**破坏和解放**。84 年周期太长，大多数人永远不会经历天王星回归（大约 84 岁时发生）。相反，最重要的天王星行运是**对冲**（大约 42 岁）——当行运天王星与其本命位置相对时。汉德强调天王星对冲是**中年危机原型**：一个觉醒时刻，你问"就这样了吗？我在真实地生活吗？"这常常触发反抗限制、需要真实自我表达和生活重组。天王星周期代表**个体化过程**——成为你的真实自我而不是符合他人期望。革命性改变、从虚假身份的解放和突破到真实性是天王星的礼物。

**Key Term Analysis**:
- **Uranus Cycle**: `84-year orbit` / `liberation principle` / `individuation process`
- **Uranus Opposition**: `age 42` / `mid-life crisis` / `awakening moment`
- **Revolutionary Change**: `liberation` / `authenticity` / `breakthrough`

**Core Points** (decomposed, no upper limit):
- Uranus cycle = 84-year orbital period
- Spans most of human lifetime
- Most experience opposition (~age 42) not return
- Revolutionary change, liberation, awakening themes
- Mid-life crisis archetype
- Uranus opposition marks major awakening
- "Is this all there is?" moment
- Rebellion against limitations
- Need for authentic self-expression
- Life restructuring and individuation
- Breakthrough into authenticity

**Detailed Explanation**:
The Uranus cycle is about becoming yourself. While Saturn teaches through limitation and Jupiter through expansion, Uranus teaches through disruption and liberation. The Uranus opposition around age 42 is often experienced as a crisis—a sudden need to break free from false identities, outdated patterns, and inauthentic living. This is not destruction for its own sake but liberation toward authenticity.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_053]` `[trigger: uranus_cycle]` `[factor_trigger: astro_uranus_cycle]` `[role: 主干]` Uranus cycle spans 84 years—most experience opposition (~42) not return. → Source Text
- `[ns_hand_pit_054]` `[trigger: liberation_principle]` `[factor_trigger: astro_liberation_principle]` `[role: 主干依赖]` Uranus rules revolutionary change, liberation, awakening, individuation. → Source Text
- `[ns_hand_pit_055]` `[trigger: midlife_crisis]` `[factor_trigger: astro_midlife_crisis AND astro_uranus_opposition]` `[role: 条件分支]` Uranus opposition (~42) is mid-life crisis archetype and awakening moment. → Source Text
- `[ns_hand_pit_056]` `[trigger: authenticity_breakthrough]` `[factor_trigger: astro_authenticity_breakthrough AND astro_individuation_process]` `[role: 总结]` Uranus brings revolutionary change and breakthrough into authenticity. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). The Uranus cycle and opposition are standard in modern predictive astrology.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。天王星周期和对冲在现代预测占星中是标准的。"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Cycle (84 Years) (天王星周期)"
    factor_refs: list = ['astro_uranus_cycle', 'astro_liberation_principle', 'astro_uranus_opposition', 'astro_authenticity_breakthrough', 'astro_individuation_process']
    
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_uranus_cycle__84_years___天王星周期_001_L1",
    )
    version: str = "1.0.0"
