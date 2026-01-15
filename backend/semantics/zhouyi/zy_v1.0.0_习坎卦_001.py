"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899959
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
    semantic_id="zy_v1.0.0_习坎卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 习坎卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  习坎。有孚，维心亨；行有尚。

  【彖传】
  《彖》曰：“习坎”，重险，也。水流而不盈，行险而不失其信，维心亨，乃以刚中也；“行有...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  习坎。有孚，维心亨；行有尚。

  【彖传】
  《彖》曰：“习坎”，重险，也。水流而不盈，行险而不失其信，维心亨，乃以刚中也；“行有尚”，往有功也。“天险不可升也，地险山川丘陵也，王公设险以守其国：险之时用大矣哉！”

  【象传】
  《象》曰：水瀳至，习坎；君子以常德行，习教事。

  【爻辞】
  初六，习坎，入于坎窞，凶。
  九二，坎有险，求小得。
  六三，来之坎坎，险且枕，入于坎窞，勿用。
  六四，樽酒，簋贰，用缶，纳约自牖，终无咎。
  九五，坎不盈，祇既平，无咎。
  上六，系用徽𬙊，置于丛棘，三岁不得，凶。

- 分字分词释义：

  - **习坎**：习，为反复练习、经历；坎，为坑陷、险阻。习坎即“反复处在险中”，既指客观环境多险，也指主观逐渐“习惯风险”。
  - **有孚，维心亨**：在险中仍保持诚信与可信赖性，以此维系内心的通达。
  - **行有尚**：在险中行事，仍有可称道之处，强调在艰险境遇里完成值得尊敬的行动。
  - **重险，也**：险象层叠，不是一重可过，而是连番的坎坷与深坑。
  - **水流而不盈**：水不断流入却不漫溢，比喻在重重压力之下仍能保持边界，不至于失控泛滥。
  - **坎窞**：深坑、地窟，象征难以自拔的困境。
  - **樽酒，簋贰，用缶，纳约自牖**：简陋而真诚的祭祀供献，从窗牖递入，比喻在艰险之中以朴素方式表达诚意。
  - **坎不盈，祇既平**：险坑尚未填满，小丘已经铲平，象征在危险尚存时过早“抹平高地”，隐藏潜在风险。
  - **系用徽𬙊，置于丛棘，三岁不得**：以精细的绳索捆绑，囚于荆棘丛中，良久不得解脱，象征长期被困于复杂约束之中。

- **规范化释义（primary_lang_explained）**：

  习坎卦描写的是“长期处于高风险环境中的生存之道”。卦辞：“习坎。有孚，维心亨；行有尚。”——不断经历坎坷险阻，只要内心保持诚信与可靠，就仍可维持内在的通达与稳定；在这样的险境中，能坚持完成一些值得称道的行动，本身就是可贵之处。

  彖传指出：习坎是“重险”，但像水流不盈一样，即便处处是坑，仍可以控制流量与边界，不让险势溢出失控；关键在于“刚中”与“有孚”：既要有内在的刚健中心，又要在对人对事上保持可信与守信。

  象传“水瀳至，习坎；君子以常德行，习教事”强调的是“在险中依然有常”：水不断涌来，形成连绵不绝的坎险，但君子在德行上保持恒常，在教化与实践上持续训练与习得，而不被环境完全塑形。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Xi Kan, "The Abysmal (Water)" or "Repeated Danger", portrays situations of recurring peril and difficulty. The Judgment, "Xi Kan: if there is sincerity, the heart penetrates; practice brings success", teaches that in the midst of danger, maintaining inner integrity and repeated practice allow one to navigate through.

- 核心要点：

  - 习坎卦的核心是**“在长期危险中保持诚信与纪律”**，而非期待迅速脱险。
  - “维心亨”提示：外境或许久不得亨通，但内在可以先行建立一条通道，使心不被险境完全淹没。
  - 爻辞显示从“陷落深坑”到“在险中求小得”“以简约祭祀维系关系”，再到“坎不盈”与长期被系缚的过程，是对“风险惯性”的全景展示。

- 详细解说：

  卦象为上坎下坎，坎重而又重，是“习坎”的结构根源。不同于一时之险，习坎是“险成为常态”的局面：人可能会对风险产生麻木，或在不断应对中消耗殆尽。卦辞强调“有孚”与“维心亨”，意在提醒：真正的出路首先在心，不在外境立刻好转。

  初六“习坎，入于坎窞，凶”是最典型的“危险惯性”：一开始就深陷坑窞，缺乏高度，很难看见出路；九二“坎有险，求小得”则转向现实：既然难以全身而退，就先在险中求取小小的收获，不强求大功，以避免更大的损失。

  六三“来之坎坎，险且枕，入于坎窞，勿用”形容往来之间皆是险阻，甚至将危险当作枕席一般习以为常，此时任何妄动只会加深困境，因此“勿用”；六四“樽酒，簋贰，用缶，纳约自牖，终无咎”则展示一种在险中修复关系、保持礼数的方式：即便条件简陋，以真诚与节制保持连接，最终可以无咎。

  九五“坎不盈，祇既平，无咎”提示一种微妙状态：危险尚未完全填平，但局势已基本稳定；若能在此时保持中道而不自满，就可无咎。上六“系用徽𬙊，置于丛棘，三岁不得，凶”则是对“长期被困”的写照：过度精细而复杂的束缚（制度、契约、关系）加上外在环境如荆棘般纠缠，使人久久不得解脱，终为凶局。"""
    normalized_text_zh: str = """"""
    subject: str = "习坎卦（䷜）"
    factor_refs: list = ['zhouyi_gua_xikan', 'zhouyi_weixin_heng', 'zhouyi_ruyu_kandan']
    
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
        l1_anchor="zy_v1.0.0_习坎卦_001_L1",
    )
    version: str = "1.0.0"
