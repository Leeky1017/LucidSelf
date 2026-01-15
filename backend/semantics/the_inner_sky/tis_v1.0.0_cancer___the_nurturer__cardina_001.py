"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.104845
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
    semantic_id="tis_v1.0.0_cancer___the_nurturer__cardina_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class CancerTheNurturerCardina(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Hard Shell | Protective ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Hard Shell | Protective exterior | Crab archetype |
| Emotional Sanctuary | Safety/belonging | Goal |
| Ancestral Memory | Roots/tradition | Connection |
| Nurturing Instinct | Care impulse | Core drive |

#### Source Text

"The Crab. A creature with a hard shell protecting a soft interior. Cancer has come into the world to create sanctuary—to build a place of safety, nurturing, and belonging. The endpoint is emotional home: a felt sense of 'this is where I belong.'"

#### English Paraphrase

**Cancer** = **Cardinal Water** sign embodying **emotional security, nurturing, and sanctuary creation**. The Crab archetype: hard protective shell over vulnerable interior, carrying home wherever it goes.

**Core Drives**:
- **Nurture & Protect**: Create safety for self and loved ones
- **Build Sanctuary**: Physical and emotional home-making
- **Memory & Tradition**: Connect to past, ancestry, roots
- **Emotional Bonding**: Form deep, loyal attachments

**Cancerian Strengths**:
- **Emotional Intelligence**: Reads feelings, knows what others need
- **Nurturing Capacity**: Instinctive caretaking, creates safe spaces
- **Intuition**: Gut-knowing, feeling-sense beyond logic
- **Tenacity**: Loyal persistence, doesn't abandon loved ones
- **Protective Fierceness**: Warrior defending those under care

**Shadow Manifestations**:
- **Dependency/Smothering**: Security needs become controlling
- **Moodiness**: Lunar emotional fluctuations without explanation
- **Living in Past**: Nostalgia prevents adaptation to present
- **Passive Aggression**: Withdrawal and sulking instead of direct communication

**Evolutionary Challenge**:
Nurture without smothering, protect without controlling, remember without clinging. Show vulnerable interior, be emotionally courageous beneath protective shell.

#### Complete Chinese Interpretation

**巨蟹座**=**基本水象**星座体现**情感安全、养育和庇护所创造**。螃蟹原型：脆弱内在上的坚硬保护壳，无论去哪都携带家。

**核心驱力**：养育与保护(为自己和爱人创造安全)；建立庇护所(物质和情感造家)；记忆与传统(连接过去、祖先、根源)；情感联结(形成深厚忠诚依附)

**巨蟹优势**：情商(读懂感觉、知道他人需要)；养育能力(本能照顾、创造安全空间)；直觉(超逻辑肚肠知觉)；韧性(忠诚坚持、不放弃爱人)；保护凶猛(守护照顾者的战士)

**阴影显化**：依赖/窒息(安全需要变控制)；情绪化(月亮情感波动无解释)；活在过去(怀旧阻碍适应现在)；被动攻击(撤回闷气而非直接沟通)

**进化挑战**：不窒息地养育、不控制地保护、不执着地记忆。展示脆弱内在、在保护壳下情感勇敢。

#### Core Points

- Cardinal Water: emotional security through sanctuary creation
- Archetype: nurturing Crab with hard shell, soft interior
- Resources: emotional intelligence, intuition, protective fierceness
- Shadow: dependency, moodiness, living in past
- Challenge: nurture without smothering
- East parallel: 巨蟹↔癸水阴柔/正印养育 (yin water nurturing)

#### Detailed Explanation

Cancer is **Cardinal Water**—initiating emotional security through creating sanctuary. The Crab archetype captures the essence: hard protective shell outside, soft vulnerable interior within. Cancer has come into the world to **build a place of safety, nurturing, and belonging**.

Cancer's resources include **emotional intelligence, intuition, and protective fierceness**—the Crab's claws that defend what it loves. The endpoint is "emotional home": a felt sense of belonging, being where one fits.

**Dysfunction** appears as dependency (clinging to others for security), moodiness (ruled by emotional tides), or living in the past (unable to release memories). The evolutionary challenge is to **nurture without smothering**—to protect without controlling, to remember without becoming trapped.

#### Narrative Snippets

- `[ns_innersky_cancer_001]` `[trigger: sign_cancer]` `[factor_trigger: sign_cancer]` `[role: 主干]` The Crab. A creature with a hard shell protecting a soft interior. Cancer has come into the world to create sanctuary—to build a place of safety, nurturing, and belonging. → The Inner Sky Ch.4 #Cancer
- `[ns_innersky_cancer_002]` `[trigger: sign_cancer AND astro_strength]` `[factor_trigger: element_water]` `[role: 主干依赖]` The endpoint is emotional home: a felt sense of 'this is where I belong.' Cancer's gift is nurturing capacity—instinctive caretaking that creates safe spaces. → The Inner Sky Ch.4 #Cancer
- `[ns_innersky_cancer_003]` `[trigger: sign_cancer AND astro_shadow]` `[factor_trigger: planet_moon]` `[role: 条件分支]` Shadow: security needs become controlling (smothering), lunar emotional fluctuations without explanation (moodiness), nostalgia prevents adaptation to present. → The Inner Sky Ch.4 #Cancer
- `[ns_innersky_cancer_004]` `[trigger: sign_cancer AND astro_challenge]` `[factor_trigger: sign_cancer]` `[role: 总结]` Evolutionary challenge: nurture without smothering, protect without controlling, remember without clinging. Show vulnerable interior, be emotionally courageous beneath protective shell. → The Inner Sky Ch.4 #Cancer"""
    normalized_text_zh: str = """"""
    subject: str = "Cancer - The Nurturer (Cardinal Water)"
    factor_refs: list = ['new_candidate', 'sign_cancer', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tis_v1.0.0_cancer___the_nurturer__cardina_001_L1",
    )
    version: str = "1.0.0"
