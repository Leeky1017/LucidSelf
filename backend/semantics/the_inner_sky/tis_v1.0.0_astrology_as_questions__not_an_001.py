"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134274
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
    semantic_id="tis_v1.0.0_astrology_as_questions__not_an_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class AstrologyAsQuestionsNotAn(SemanticEntry):
    """
    **Source Text**:
Slowly it dawned on me: astrological forces present us not with answers but with qu...
    """
    
    original_text: str = """**Source Text**:
Slowly it dawned on me: astrological forces present us not with answers but with questions. The answers we give are our own. Those astrologers who for centuries have been trying to determine our behavior from our birthcharts have been barking up the wrong tree. Astrology supplies the terrain. How we navigate it is our own business.
...
Astrology can help us in only three ways. It can vividly portray the happiest life available to us. It can tell us what tools we have available for the job and how best to employ them. And it can warn us in advance about how our lives will look when we are getting off the mark.

**Key Term Analysis**:
- `questions not answers`: astrology frames issues and possibilities, but does not dictate specific decisions or behaviors.
- `astrological terrain`: the symbolic life landscape described by the birthchart, including challenges, resources, and directions.
- `tools for the job`: inner and outer resources (talents, drives, circumstances) that can be consciously used.
- `off the mark`: recognizable life patterns indicating we are drifting away from the chart’s optimal growth line.

**English Paraphrase (Primary Language)**:
From Forrest’s perspective, astrology is not an oracle that hands down definite answers. Instead, it poses incisive questions about how we are living and where we might go. The sky describes the terrain; it does not dictate our route. Our actual answers—our choices, attitudes, and actions—remain entirely our own responsibility. For centuries, many astrologers have treated charts as if they could directly predict behavior. Forrest argues that this is the wrong tree to bark up, because it mistakes a symbolic map for a behavioral script.

He narrows astrology’s legitimate functions to three. First, it can sketch the happiest and most fulfilling life pattern that is realistically available to us, given who we are. Second, it can inventory our tools—talents, drives, needs, and sensitivities—and suggest how to use them more effectively. Third, it can offer early warnings by showing what our life tends to look like when we drift away from that optimal pattern. Beyond those three tasks, astrology has no business telling us exactly what to do. Its proper role is to sharpen our questions and illuminate options, not to remove the burden of choice.

**Complete Chinese Interpretation (Secondary Language)**:
在 Forrest 的视角里，占星绝不是一个替我们给出「标准答案」的神谕，而是一套会不断追问「你究竟要怎样活」的问题机器。天象所描绘的，是一整片存在的地形图，却并不会为任何人画好唯一的路线图。真正的答案——也就是我们做出的决定、采取的态度与行动——始终只能由自己负责。几百年来，许多占星师都试图从命盘直接推演「你会怎样做事、会发生什么事」，Forrest 认为这等于把象征地图误当成行为剧本，是完全搞错了对象。

因此，他把占星的正当功能压缩成三件事。第一，占星可以勾勒出「在现实条件之内，你所能活出的最快乐、最充实的人生轨迹」，给出一幅可能性的上限图。第二，它可以清点我们手里真正握着哪些工具——天赋、驱力、需求、敏感点——并提示如何更好地运用这些资源。第三，它可以提前发出预警：当我们偏离这条最优轨迹时，生活通常会出现哪些可识别的「跑偏征象」。除此之外，占星不该越俎代庖，替我们做出任何细节决定。它真正的职责，是把问题问得更锐利，让道路更清晰，而不是帮我们卸掉选择的责任。

**Core Points**:
- Astrology offers questions about life, not pre‑packaged answers.
- The chart is a map of terrain, not a script that dictates behavior.
- Legitimate uses: portray optimal life pattern, list available tools, and warn when we drift off course.
- Responsibility for choices and actions always remains with the individual.

**Detailed Explanation**:
By redefining astrology as a question‑generating language, Forrest dramatically reduces the scope of what astrologers claim to do while deepening the quality of their contribution. If the chart provides only the landscape, then the astrologer’s role shifts from prediction to orientation. This prevents dependency dynamics in which clients wait for an external authority to decide for them. Instead, the reading becomes a structured conversation about possibilities, resources, and consequences.

The three functions Forrest names also map cleanly onto engine design: one module can describe the "optimal" configuration of the chart, another can inventory resources, and a third can detect deviation patterns. Crucially, none of these functions replaces free will. They simply make the inner and outer consequences of different choices more visible. In this sense, astrology amplifies self‑reflection rather than competing with it.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The phrase "astrological forces present us not with answers but with questions" is central and is preserved almost verbatim. The triad "portray happiest life / list tools / warn when off the mark" is slightly normalized, but the underlying structure is unchanged.
- **中文**：为避免把占星描述成「万能导航」，译文刻意强调「地形图」而非「路线图」的比喻，以对应原文的 "supplies the terrain"。原文对占星可做的三件事提法较口语，这里在中文中压缩为「最优轨迹 / 工具清单 / 跑偏预警」三个关键词，以便后续在引擎侧对应具体模块。

**Narrative Snippets**:
- `[ns_innersky_019]` `[trigger: client_seeks_prediction]` `[factor_trigger: astro_chart_interpretation]` `[role: 主干]` Astrological forces present us not with answers but with questions—the answers we give are our own. → Source Text
- `[ns_innersky_020]` `[trigger: chart_reading_purpose]` `[factor_trigger: astro_zodiac_framework]` `[role: 主干依赖]` Astrology supplies the terrain; how we navigate it is our own business. → Source Text
- `[ns_innersky_021]` `[trigger: optimal_life_guidance]` `[factor_trigger: chart_resolution]` `[role: 条件分支]` Astrology can vividly portray the happiest life available to us—a map of optimal possibilities. → Source Text
- `[ns_innersky_022]` `[trigger: talent_inventory]` `[factor_trigger: birth_time_accuracy]` `[role: 总结]` Astrology tells us what tools we have available for the job and how best to employ them. → Source Text
- `[ns_innersky_023]` `[trigger: warning_signs]` `[factor_trigger: development]` `[role: 主干]` Astrology warns us in advance about how our lives look when we are getting off the mark. → Source Text
- `[ns_innersky_024]` `[trigger: responsibility_reminder]` `[factor_trigger: direction]` `[role: 主干依赖]` Those astrologers trying to determine behavior from birthcharts have been barking up the wrong tree. → Source Text"""
    normalized_text_zh: str = """"""
    subject: str = "Astrology as Questions, Not Answers"
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
        l1_anchor="tis_v1.0.0_astrology_as_questions__not_an_001_L1",
    )
    version: str = "1.0.0"
