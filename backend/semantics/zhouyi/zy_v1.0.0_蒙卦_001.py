"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899722
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
    semantic_id="zy_v1.0.0_蒙卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 蒙卦(SemanticEntry):
    """
    - **原文（source_text）**：
  【卦辞】
  蒙：亨。匪我求童蒙，童蒙求我。初筮告，以再三渎，渎则不告。利贞。

  【爻辞】
  初六，发蒙，利用刑人，用说桎梏；以往吝。
  九二...
    """
    
    original_text: str = """- **原文（source_text）**：
  【卦辞】
  蒙：亨。匪我求童蒙，童蒙求我。初筮告，以再三渎，渎则不告。利贞。

  【爻辞】
  初六，发蒙，利用刑人，用说桎梏；以往吝。
  九二，包蒙，吉；纳妇，吉；子克家。
  六三，勿用取女；见金夫，不有躬；无攸利。
  六四，困蒙，吝。
  六五，童蒙，吉。
  上九，击蒙；不利为寇，利御寇。

  【彖传】
  《彖》曰：蒙，山下出泉，蒙。君子以果行育德。
  蒙亨，以亨行时中也。
  “匪我求童蒙，童蒙求我”，志应也。
  “初筮告，以再三渎，渎则不告”，渎蒙也。
  蒙以养正，圣功也。

  【象传】
  《象》曰：山下出泉，蒙；君子以果行育德。

- 分字分词释义：

  - 蒙：卦名，本义为蒙昧、未启之状态，也指被覆盖、未开化。卦象为山下有泉，象征资质未开、需启发教化。
  - 童蒙：幼童之蒙，指心智未开、尚处学习初期之人。
  - 匪我求童蒙，童蒙求我：不是我主动去求蒙童，而是蒙童主动来求教，强调“求学者主动、授业者被动”的原则。
  - 初筮告：第一次占问便给予答复。
  - 再三渎，渎则不告：反复占问为渎慢之举，渎慢则不再告知，强调占问须诚敬节制。
  - 发蒙：启发蒙昧、开导愚昧之人。
  - 利用刑人，用说桎梏：以有所刑罚之人作为示警，使其脱去枷锁；通过正当的刑罚与教化解除束缚。
  - 包蒙：包容蒙昧，以宽厚之德容纳、引导之。
  - 纳妇吉，子克家：接纳妇人、建立家庭而吉，子嗣能承担家业，比喻德行能在家内落地。
  - 勿用取女：不可娶此女为妻，指其品行或缘分不宜。
  - 见金夫，不有躬：见到富有或强壮之人便失去自守，不保其身。
  - 困蒙：困于蒙昧之中，难以自拔。
  - 击蒙：以击打、纠正之方式对待蒙昧之人，象征严厉教诲或制裁。
  - 不利为寇，利御寇：不宜成为侵害他人的“寇”，而宜抵御“寇”之侵扰。
  - 山下出泉：下卦坎为水，上卦艮为山，泉水自山下涌出，象征资质潜藏、待人疏导。
  - 果行育德：行为果决、践行所学，以此培育德性。
  - 养正：在童蒙之时养成正确的方向与习惯。

- **规范化释义（primary_lang_explained）**：

  蒙卦描写的是人处在“启蒙阶段”的状态：资质未开、认知有限，如山下之泉，水源虽清却未成川流。卦辞“蒙：亨”说明在蒙昧之中仍藏有通达之机，但前提是要有正确的教化与学习路径。“匪我求童蒙，童蒙求我”强调学习以求道者主动为本，老师并不主动去追逐学生；“初筮告，以再三渎，渎则不告”则说明占问天地、请教老师之时，应持敬畏之心，不可反复试探、戏谑。

  六爻描绘了不同蒙昧状态下的教化策略：初六“发蒙，利用刑人，用说桎梏；以往吝”，强调启蒙之初可以通过刑罚与解除枷锁的对比来示人，以警戒与解放并用，但若启蒙者自身不谨慎，以此继续前往则易招致羞吝；九二“包蒙，吉；纳妇，吉；子克家”表现出以宽厚包容承接蒙昧者，通过家庭与日常生活来落实德行；六三“勿用取女；见金夫，不有躬；无攸利”警示：对一个容易被财富或权势迷惑而失其本心的人，不宜轻率结为终身伴侣；六四“困蒙，吝”则呈现长期滞留在蒙昧而不学的状态，自招困窘；六五“童蒙，吉”表明真正的“童蒙”是谦逊、乐于接受教导者，故吉；上九“击蒙；不利为寇，利御寇”指出，对顽固不化的蒙昧需以严厉方式矫正，但应立足于“御寇”，而非“为寇”，即以防御与护正为本，而非成为压迫与伤害他人的暴力。

  彖传以“山下出泉，蒙；君子以果行育德”概括蒙卦的图景：泉水象征潜在的才智与可能，若无引导，则只是被山石覆盖的水源；君子当以果决的行动与真实的修行来培养德性，而不仅停留在抽象说教上。“蒙亨，以亨行时中也”表明蒙昧能通达，在于行事合乎时中，不偏不倚；“蒙以养正，圣功也”更是指出，教化童蒙、在早期养成正确的方向，是圣人之大功。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Meng, "Youthful Folly" or "Inexperience", addresses how to enlighten and educate when understanding is not yet developed and cognition is limited. The Judgment "Meng: success; it is not I who seek the young and foolish, but the young and foolish who seek me" establishes the principle that the seeker should be active while the teacher remains cautious, preventing base entreaty for fame or casual instruction. The Image "a spring emerging below the mountain, Meng; the noble person thereby nurtures virtue through resolute action" indicates that like a spring covered by mountain stones, latent intelligence and potential require guidance to emerge; the noble person should use decisive action and genuine cultivation to develop virtue, not merely remain in abstract preaching.

- 核心要点：

  - 蒙卦的核心是“启蒙与教化”：如何在资质未开、认知受限的阶段，建立正确的师生关系与学习路径。
  - “匪我求童蒙，童蒙求我”确立了求道者主动、授业者慎重的原则，防止卑辞邀名或随意开示。
  - 六爻分别从启蒙方式、包容引导、择偶与自守、困而不学、童真可教、严厉纠偏等角度，刻画蒙昧世界中的多种形态。
   蒙卦提示：在任何学习与成长的起点，“养正”比单纯“求知”更重要，早期偏差若不纠正，将来更难挽回。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "蒙卦（䷃）"
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_蒙卦_001_L1",
    )
    version: str = "1.0.0"
