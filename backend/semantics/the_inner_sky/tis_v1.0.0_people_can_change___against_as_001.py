"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134198
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
    semantic_id="tis_v1.0.0_people_can_change___against_as_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class PeopleCanChangeAgainstAs(SemanticEntry):
    """
    **Source Text**:
People change. Yet one assumption runs like a virus through most astrological writi...
    """
    
    original_text: str = """**Source Text**:
People change. Yet one assumption runs like a virus through most astrological writing: people do not change.
“Scorpios are sexy, but cannot be trusted; Capricorns are industrious; Pisceans are cosmic, but too spacy to balance their checkbooks.”
From Ptolemy right up through Linda Goodman, the astrological symbols have been interpreted as pieces of psychological machinery. We are blessed or cursed with them at birth and stuck with them until we die. It is a lie.
There is an indeterminacy, an unpredictable element in life. This wild card may be a thorn in the side of the fortune-tellers, but it is the keystone of any positive, evolutionary approach to astrology.
...
There may be an Everest of inertia within us, but it is to that single atom of mutability that astrology must speak. It must address the life in us, not the stasis.

**Key Term Analysis**:
- `fatalism`: the belief that birth configurations lock personality into a fixed pattern that cannot be changed.
- `indeterminacy / wild card`: the unpredictable, open element in life that makes genuine change and growth possible.
- `inertia vs mutability`: the contrast between heavy psychological habit and the small but real capacity to choose new responses.
- `evolutionary astrology`: an approach that speaks to the mutable, growing part of the person instead of reinforcing static labels.

**English Paraphrase (Primary Language)**:
Traditional astrology often assumes that people are fixed, as if their character were a machine assembled at birth and left to run unchanged until death. Forrest directly rejects this view. He begins by asserting that human beings do, in fact, change. The popular sun‑sign clichés—"Scorpios are sexy but untrustworthy," "Capricorns are industrious," "Pisceans are spacey"—only reinforce the illusion that personality is frozen and predetermined. Even more sophisticated texts often slide back into the same fatalistic tone, treating a difficult Venus aspect as a life sentence of promiscuity, or a heavy Saturn placement as an unchangeable burden.

Forrest calls that stance a lie. At the heart of real life there is always an unpredictable element—a wild card of indeterminacy. That wild card is not an embarrassment to good astrology; it is precisely what makes growth and evolution possible. A chart may show powerful habits and deep‑seated patterns, an "Everest of inertia," but there is always at least a single atom of mutability, a point where conscious choice can enter. Growth‑oriented astrology must deliberately speak to that living, changing core in a person, not to the frozen mask of habit. Its task is to awaken the part of us that can respond creatively, rather than to confirm a story of permanent limitation.

**Complete Chinese Interpretation (Secondary Language)**:
传统占星往往假定「人是不会变的」，好像人格是一部在出生时就被组装完成的机器，此后只会按照原有程序运行到死亡。Forrest 一上来就否定这种立场，他的第一句话就是：人会改变。流行的太阳星座陈词滥调——「天蝎很性感但不可靠」「摩羯勤奋上进」「双鱼很空灵但不接地气」——只会进一步制造一种幻觉：人格是被写死的、无法更改的脚本。即便是较为进阶的占星教材，也常常不自觉地滑回同样的宿命论语气，把某个紧张的金星相位当成终身放荡不羁的宣判，把沉重的土星结构当成无法拆解的终生枷锁。

Forrest 直接把这种态度称为「谎言」。现实生命的中心，总是存在一个无法被完全预测的成分——一种「不确定性的外卡」。对江湖式的算命来说，这个外卡也许很刺眼，但对任何以成长为导向的占星来说，它反而是整套系统的基石。命盘当然会揭示出强大的惯性与深层模式，那些看起来像是一座「内在的珠穆朗玛峰」。但在那座山体内部，总还保留着一个最微小的可变点——那个允许我们做出不一样选择的原子。所谓成长型占星，必须刻意地对准这个「可变的原子」说话，而不是对着旧习性和固化的标签反复背诵。它的任务是唤醒人内在那一块仍然活着、仍然能作出新回应的部分，而不是替「一生注定」的故事盖章。

**Core Points**:
- Forrest rejects the idea that astrological symbols describe fixed, unchangeable traits.
- Popular sun‑sign clichés reinforce a false belief in psychological machinery.
- Life always contains an unpredictable element that makes growth possible.
- Astrology must address the living, mutable core in a person, not their inertia.

**Detailed Explanation**:
This opening move sets the ethical and philosophical tone for the entire book. Forrest does not simply tweak traditional interpretations; he attacks the underlying assumption that charts equal fate. By framing fatalism as a lie, he obliges the reader to reconsider any interpretation that sounds like a life sentence. The existence of indeterminacy means that astrological symbols map tendencies, potentials, and default reactions—not guaranteed outcomes. When astrologers forget this, they easily harden living symbols into rigid labels that can actually block growth.

Speaking to the "single atom of mutability" means that every reading must leave room for choice, experiment, and evolution. A responsible astrologer describes the terrain and the gravity of old habits, but never confuses those with destiny. The purpose of interpretation becomes helping a client recognize where they still have leverage—where new responses are possible—rather than confirming that they are doomed to enact the same pattern forever. This redefinition moves astrology away from fortune‑telling and toward a collaborative growth practice.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Forrest's text explicitly contrasts the long historical line "from Ptolemy right up through Linda Goodman" with his own evolutionary approach. The wording "It is a lie" is unusually blunt, underscoring a polemical break with fatalistic traditions. The metaphor of an "Everest of inertia" versus a "single atom of mutability" is kept as‑is because it sharply conveys both the weight of habit and the tiny but real opening for change.
- **中文**：原文用「from Ptolemy right up through Linda Goodman」把古典占星与现代流行书连成一条宿命论谱系，本译文保留这一历史跨度，但不细分流派，只突出他与「把人当机器」的传统划清界限。「It is a lie」直译会显得过于口语化，这里译为「是一种谎言」以保留尖锐语气。「Everest of inertia / single atom of mutability」保留为「惯性的珠穆朗玛峰 / 可变的原子」，用比喻强化「惯性极大但并非绝对」这一核心意象。

**Narrative Snippets**:
- `[ns_innersky_001]` `[trigger: client_feels_trapped_by_chart]` `[factor_trigger: human_resolution]` `[role: 主干]` People change—the assumption that they do not is a lie running through most astrological writing. → Source Text para 1
- `[ns_innersky_002]` `[trigger: fatalistic_sun_sign_cliche]` `[factor_trigger: psychological_machinery]` `[role: 主干依赖]` "Scorpios are sexy but untrustworthy; Capricorns are industrious"—these labels freeze personality into machinery. → Source Text para 1
- `[ns_innersky_003]` `[trigger: difficult_aspect_reading]` `[factor_trigger: indeterminacy]` `[role: 条件分支]` There is an indeterminacy, a wild card in life—this is the keystone of any positive, evolutionary approach. → Source Text para 1
- `[ns_innersky_004]` `[trigger: heavy_saturn_placement]` `[factor_trigger: inertia]` `[role: 条件分支]` There may be an Everest of inertia within us, but astrology must speak to that single atom of mutability. → Source Text para 1
- `[ns_innersky_005]` `[trigger: growth_oriented_reading]` `[factor_trigger: awakening]` `[role: 条件分支]` Astrology must address the life in us, not the stasis—the living core that can still respond creatively. → English Paraphrase
- `[ns_innersky_006]` `[trigger: client_self_doubt]` `[factor_trigger: mutability]` `[role: 总结]` A chart shows powerful habits, but there is always at least one point where conscious choice can enter. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "People Can Change – Against Astrological Fatalism"
    factor_refs: list = ['fatalism', 'indeterminacy']
    
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
        l1_anchor="tis_v1.0.0_people_can_change___against_as_001_L1",
    )
    version: str = "1.0.0"
