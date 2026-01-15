"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.096830
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
    semantic_id="tis_v1.0.0_gemini___the_witness__mutable__001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class GeminiTheWitnessMutable(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Mutable Air | Changeable...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Mutable Air | Changeable mind | Element |
| Witness Consciousness | Observe without clinging | Gift |
| Variety Drive | Diverse experience | Core need |
| Integrative Thread | Unifying idea | Challenge |

#### Source Text

"The Twins. Two personalities coexisting—conscious versatility. To witness life without attachment, experience full human spectrum without being trapped by single perspective. The endpoint is not mastery of subject, but mastery of art of learning itself. Gemini strategy: gather experience rapidly in variety."

#### English Paraphrase

**Gemini** = **Mutable Air** sign embodying **versatility, communication, and eternal curiosity**. The Twins archetype: conscious dual perspective, sampling all life offers without attachment to any single view.

**Core Drives**:
- **Gather Experience**: Rapidly, in succession—taste all flavors possible
- **Variety**: Multiple interests, friendships, skills (boredom = enemy, routine = poison)
- **Communicate**: Talk, write, teach, share—processing experience through expression
- **Movement**: Physical (trips, errands), mental (reading, puzzles), social (parties, calls)
- **Follow Curiosity**: No plan, no strategy—pure insatiable interest

**Geminian Strengths**:
- **Adaptability**: Fit anywhere, talk to anyone, learn anything (chameleon flexibility)
- **Quick Intelligence**: Fast, agile mind making connections others miss (wit, cleverness)
- **Communication Skills**: Convey ideas/feelings with clarity (words, gestures, charm)
- **Curiosity**: Unquenchable thirst keeping them young, vital, engaged

**Shadow Manifestations**:
- **Scattered**: Flit without going deep, never committing ("All tactics, no strategy")
- **Superficiality**: Learn little about everything, master nothing (dozens acquaintances, no deep friends)
- **Inconsistency**: Change mind so often no one takes seriously (say opposite tomorrow)
- **Nervous Exhaustion**: Restless mind never stops (anxiety, insomnia, mental fatigue)

**Evolutionary Challenge**:
"The horse needs a rider." Harness natural versatility toward coherent end. Not giving up variety, but finding thread connecting all diverse interests. Go deep while remaining curious.

#### Complete Chinese Interpretation

**双子座**=**变动风象**星座体现**多才、沟通和永恒好奇**。双胞胎原型：有意识双重视角、品尝生活提供的所有而不执着任何单一观点。

**核心驱力**：收集经验(快速、连续——品尝所有可能味道)；多样性(多兴趣、友谊、技能-无聊=敌人、常规=毒药)；沟通(谈、写、教、分享——通过表达处理经验)；运动(物理-旅行、差事；心智-阅读、谜题；社交-派对、电话)；跟随好奇(无计划、无策略——纯粹不可满足兴趣)

**双子优势**：适应性(任何地方适应、与任何人谈、学任何事-变色龙灵活)；快速智能(快速敏捷思维做他人错失连接-机智、聪明)；沟通技能(清晰传达想法/感觉-言语、手势、魅力)；好奇心(不可止渴使他们年轻、活力、参与)

**阴影显化**：分散(飞来飞去不深入、从不承诺-"所有战术无战略")；肤浅(学万事一点、不精通任何-几十个熟人、无深友)；不一致(常改主意无人认真对待-明天说反话)；神经耗竭(不安思维不停-焦虑、失眠、心智疲劳)

**进化挑战**："马需要骑手。"利用天然多才向连贯目标。非放弃多样、而是找连接所有不同兴趣的线。保持好奇同时深入。

#### Core Points

- Mutable Air: versatile communication through witnessing
- Archetype: dual Twins sampling without attachment
- Resources: adaptability, quick intelligence, communication, curiosity
- Shadow: scattered, superficial, inconsistent, nervous
- Challenge: harness versatility toward coherence
- East parallel: 双子↔庚金阳刚/比肩交流 (yang metal communication)

#### Detailed Explanation

Gemini is **Mutable Air**—adapting mental energy through versatile communication. The archetype is the **Twins**: experiencing life from multiple perspectives, sampling all life offers without clinging to any single viewpoint. Gemini has come to **witness**.

Gemini's resources include **adaptability, quick intelligence, communication, and insatiable curiosity**—the ability to hold multiple perspectives simultaneously, conscious duality as a gift.

**Dysfunction** appears as being scattered (no center to the versatility), superficial (knowing a little about everything, nothing deeply), inconsistent (unreliable because always changing), or nervous (mind racing without rest). The evolutionary challenge is to **harness versatility toward coherence**—finding the thread connecting all different interests, staying curious while also going deep.

#### Narrative Snippets

- `[ns_innersky_gemini_001]` `[trigger: sign_gemini]` `[factor_trigger: sign_gemini AND element_air]` `[role: 主干]` The Twins. Gemini has come into the world to witness—experiencing life from multiple perspectives, tasting all life has to offer without clinging to any single viewpoint. → The Inner Sky Ch.4 #Gemini
- `[ns_innersky_gemini_002]` `[trigger: sign_gemini AND astro_strength]` `[factor_trigger: astro_sign_gemini]` `[role: 主干依赖]` The endpoint is conscious duality—ability to hold multiple perspectives simultaneously. Adaptability, quick intelligence, communication, curiosity as insatiable thirst. → The Inner Sky Ch.4 #Gemini
- `[ns_innersky_gemini_003]` `[trigger: sign_gemini AND astro_shadow]` `[factor_trigger: astro_sign_gemini AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: scattered (flitting without depth, never committing—"all tactics no strategy"), superficial (jack of all trades), inconsistent (change mind so often no one takes seriously), nervous exhaustion. → The Inner Sky Ch.4 #Gemini
- `[ns_innersky_gemini_004]` `[trigger: sign_gemini AND astro_challenge]` `[factor_trigger: astro_sign_gemini]` `[role: 总结]` 'The horse needs a rider.' Harness natural versatility toward coherent end. Not giving up variety, but finding thread connecting all diverse interests. Go deep while remaining curious. → The Inner Sky Ch.4 #Gemini"""
    normalized_text_zh: str = """"""
    subject: str = "Gemini - The Witness (Mutable Air)"
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
        l1_anchor="tis_v1.0.0_gemini___the_witness__mutable__001_L1",
    )
    version: str = "1.0.0"
