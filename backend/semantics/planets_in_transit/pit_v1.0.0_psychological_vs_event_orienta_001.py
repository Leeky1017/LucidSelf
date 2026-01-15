"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251443
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
    semantic_id="pit_v1.0.0_psychological_vs_event_orienta_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PsychologicalVsEventOrienta(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Modern astrology emphasizes psychological growth opportu...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Modern astrology emphasizes psychological growth opportunities rather than external event prediction. Transits indicate appropriate times for actions and inner development, not inevitable external events. The focus shifts from 'What will happen?' to 'What am I being invited to become?'"

**English Paraphrase (Primary Language)**:
The shift from **event orientation** (traditional fortune-telling) to **psychological orientation** (modern humanistic astrology) is fundamental to Hand's approach. Traditional astrology asks: "When will I marry? When will I get money? When will disaster strike?" This treats the person as passive, subject to external planetary forces. Modern psychological astrology asks: "What growth opportunity is this transit presenting? What inner work is being invited? How can I cooperate with this energy for my development?" This reframes transits as **invitations to growth** rather than **predictions of fate**. A difficult transit (Saturn square, Pluto conjunction) becomes not a threat but a **developmental opportunity**—a time when the universe is supporting your maturation if you engage consciously.

**Complete Chinese Interpretation (Secondary Language)**:
从**事件取向**（传统算命）到**心理取向**（现代人本占星）的转变是汉德方法的基础。传统占星问："我何时结婚？何时有钱？何时会灾难？"这把人当作被动的，受行星力量支配的对象。现代心理占星问："这个行运呈现什么成长机会？邀请什么内在工作？我如何有意识地与这能量合作以促进发展？"这把行运从**命运预测**重构为**成长邀请**。一个困难的行运（土星四分、冥王合相）不是威胁而是**发展机会**——宇宙在支持你的成熟，如果你有意识地参与。

**Key Term Analysis**:
- **Event Orientation**: `external prediction` / `passive victim` / `fortune-telling`
- **Psychological Orientation**: `inner growth` / `active participation` / `developmental opportunity`
- **Appropriate Times**: `timing for action` / `readiness markers` / `not inevitabilities`

**Core Points** (decomposed, no upper limit):
- Modern approach emphasizes psychological growth vs external event prediction
- Transits indicate appropriate times for actions and inner development
- Shifts focus from "What will happen?" to "What am I invited to become?"
- Difficult transits become developmental opportunities, not threats
- Person shifts from passive victim to active participant
- Empowerment through recognizing growth invitations
- Cooperation with energy rather than submission to fate

**Detailed Explanation**:
This orientation change has profound practical implications. In event-oriented astrology, a client hears "Pluto is coming to your Sun—prepare for crisis." In psychological astrology, the same transit becomes "Pluto is inviting deep transformation of your core identity—what needs to die and be reborn?" The first creates anxiety; the second creates engagement. The astrologer's role shifts from predictor to guide, helping clients recognize and cooperate with growth opportunities.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_008]` `[trigger: psychological_orientation]` `[factor_trigger: astro_psychological_orientation]` `[role: 主干]` Modern astrology emphasizes psychological growth opportunities rather than external event prediction. → Source Text
- `[ns_hand_pit_009]` `[trigger: growth_invitation]` `[factor_trigger: astro_growth_invitation]` `[role: 主干依赖]` Transits indicate appropriate times for actions and inner development, not inevitable external events. → Source Text
- `[ns_hand_pit_010]` `[trigger: active_participation]` `[factor_trigger: astro_active_participation]` `[role: 总结]` The shift from passive victim to active participant in one's own development. → English Paraphrase
- `[ns_pit_pgo]` `[trigger: psych_growth_opportunity]` `[factor_trigger: psych_growth_opportunity]` `[role: 效果]` Psychological growth opportunity arises when transits activate areas requiring conscious development. → PIT Foundation
- `[ns_pit_pgr]` `[trigger: psych_growth_readiness]` `[factor_trigger: psych_growth_readiness]` `[role: 条件分支]` Psychological growth readiness determines how constructively transit energy is utilized. → PIT Foundation
- `[ns_pit_ped]` `[trigger: psych_ego_development]` `[factor_trigger: psych_ego_development]` `[role: 条件分支]` Ego development stage influences how Sun and 1st house transits are experienced. → PIT Foundation
- `[ns_pit_pcd]` `[trigger: psych_childhood_development]` `[factor_trigger: psych_childhood_development]` `[role: 条件分支]` Childhood development patterns are activated by Moon and 4th house transits. → PIT Foundation
- `[ns_pit_pac]` `[trigger: psych_authenticity_crisis]` `[factor_trigger: psych_authenticity_crisis]` `[role: 效果]` Authenticity crisis may arise during Uranus and Pluto transits challenging false self-structures. → PIT Foundation
- `[ns_pit_pic]` `[trigger: psych_individuation_crisis]` `[factor_trigger: psych_individuation_crisis]` `[role: 效果]` Individuation crisis occurs when transits demand separation from collective patterns. → PIT Foundation
- `[ns_pit_ppf]` `[trigger: psych_personality_filter]` `[factor_trigger: psych_personality_filter]` `[role: 条件分支]` Personality filter shapes how transit energy is perceived and expressed. → PIT Foundation
- `[ns_pit_ir]` `[trigger: individual_responsibility]` `[factor_trigger: individual_responsibility]` `[role: 效果]` Individual responsibility for growth is emphasized in psychological approach to transits. → PIT Foundation
- `[ns_pit_lg]` `[trigger: life_goals]` `[factor_trigger: life_goals]` `[role: 条件分支]` Life goals are examined during 10th house and Saturn transits. → PIT Foundation
- `[ns_pit_pi]` `[trigger: protective_instinct]` `[factor_trigger: protective_instinct]` `[role: 条件分支]` Protective instinct is activated during Moon and 4th house transits. → PIT Foundation
- `[ns_pit_sp]` `[trigger: spiritual_practice]` `[factor_trigger: spiritual_practice]` `[role: 条件分支]` Spiritual practice supports constructive use of Neptune and 12th house transits. → PIT Foundation
- `[ns_pit_mj]` `[trigger: mental_journey]` `[factor_trigger: mental_journey]` `[role: 效果]` Mental journey or intellectual exploration is stimulated by Mercury and 3rd/9th house transits. → PIT Foundation
- `[ns_pit_pt]` `[trigger: physical_travel]` `[factor_trigger: physical_travel]` `[role: 效果]` Physical travel is indicated by 9th house and Jupiter transits. → PIT Foundation
- `[ns_pit_nh9]` `[trigger: ninth_house_foreign]` `[factor_trigger: ninth_house_foreign]` `[role: 条件分支]` Ninth house foreign affairs include travel, higher education, and philosophical expansion. → PIT Foundation
- `[ns_pit_md]` `[trigger: mercury_domain]` `[factor_trigger: mercury_domain]` `[role: 条件分支]` Mercury domain includes communication, learning, short travel, and mental processing. → PIT Foundation

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Hand's psychological orientation aligns with Jungian psychology and humanistic astrology, representing a major paradigm shift in 20th-century astrology.
- **中文**: Hand的心理取向与荣格心理学和人本占星相一致，代表20世纪占星学的重大范式转变。"""
    normalized_text_zh: str = """"""
    subject: str = "Psychological vs Event Orientation (心理vs事件取向)"
    factor_refs: list = ['astro_psychological_orientation', 'astro_growth_invitation', 'astro_active_participation', 'astro_developmental_opportunity']
    
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
        l1_anchor="pit_v1.0.0_psychological_vs_event_orienta_001_L1",
    )
    version: str = "1.0.0"
