"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559168
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
    semantic_id="yhzp_v1.0.0_论小儿_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论小儿(SemanticEntry):
    """
    - **原文（source_text）**：凡小儿命，见财多，必庶出螟蛉，克父母也；若幼年行运于财旺之乡亦然。夫小儿命，大要身旺，最喜印绶生之，无财克之，则易生灾少。不要官星七杀、阳刃伤官太旺，身旺亦...
    """
    
    original_text: str = """- **原文（source_text）**：凡小儿命，见财多，必庶出螟蛉，克父母也；若幼年行运于财旺之乡亦然。夫小儿命，大要身旺，最喜印绶生之，无财克之，则易生灾少。不要官星七杀、阳刃伤官太旺，身旺亦多灾；身弱则难养。

- **分字分词释义**：
  - **小儿命**：专指子女尚在幼年阶段的命局判断，以能否平安长大为首要目标。
  - **见财多**：命局或大运中财星数量多、力量重，凌驾于印绶或日主之上。
  - **庶出螟蛉**：庶出指非正室所生；螟蛉本指养子，这里泛指寄人篱下、继嗣收养的子女。
  - **克父母**：通过财星克制印绶，象征对父母身体、精力与资源形成损耗，使其难以安心养育。
  - **行运于财旺之乡**：幼年行大运或流年落在财星旺地，使财星之力进一步增强。
  - **身旺**：日主得令有根，并得比劫印绶扶助，代表体质充足、抗风险能力强。
  - **印绶生之**：印绶生日主，象征长辈庇护与资源供给，小儿安稳成长。
  - **财克印**：财星克制印绶，削弱庇护力量，父母为财务奔波，对小儿照料与投入不足。
  - **官星七杀太旺**：官杀过多过旺，对柔弱之身形成过度约束与压制，易有病灾惊险。
  - **阳刃伤官太旺**：阳刃、伤官力量过强，小儿好动好强，易惹是非招致外伤与意外。
  - **身弱难养**：日主力量不足，稍遇病灾关煞或家庭环境不稳即难以承受，象征养育困难乃至夭折风险。

- **规范化释义（primary_lang_explained）**：小儿命以身旺为吉，喜印绶生身无财克印，则易养灾少。忌财多（主庶出克父母）、官杀多（身弱难养）、阳刃伤官太旺（多灾）。财多必庶出螟蛉；身弱难养多夭折。

- **完整对等诠释（secondary_lang_full）**：Children's fate favors strong Self—Seal generating Self without Wealth controlling Seal brings easy raising with few disasters. Taboos abundant Wealth (illegitimate birth harming parents), excessive Officer/Killing (weak Self difficult to raise), Yang Blade/Injuring Officer too prosperous (many disasters). Abundant Wealth necessarily brings illegitimate birth; weak Self brings difficulty raising with early death.

- **核心要点**：小儿喜身旺印绶生身；忌财多官杀阳刃；财多主庶出克父母；身弱难养

- **详细解说**：  本条从“小儿命”这一特殊阶段出发，强调早年判断的首要问题不是富贵高低，而是能否平安长大。结构上首先划分“身旺”与“身弱”：小儿身旺，如同先天体质良好，再配合印绶生日主，象征有长辈悉心照料与资源供给，是“易养、少灾”的基础格局；反之身弱，就像体质羸弱，任何外界冲克与环境波动都更难承受。原文又以“见财多，必庶出螟蛉，克父母也；若幼年行运于财旺之乡亦然”点出财星对小儿的双重含义：一方面，财多常指家庭中围绕资源分配的复杂关系，映射为庶出、养子等非典型出身；另一方面，财克印又象征父母被经济压力和现实事务牵制，对子女的看护与投入被削弱，于是被概括为“克父母”。官星七杀与阳刃伤官在成年命中有时可以视作权力、才华或冲劲，但放在小儿阶段，多半转化为过度约束、严苛环境与外伤风险：日主弱而官杀、刃伤太旺，就像幼弱之身背负过重的责任与冲突，自然“难养”。因此，本条的小儿命总纲可以浓缩为：身旺配印绶且财官适度，为易养配置；身弱而财官刃过旺，则是养育困难与夭折高危信号。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_201]` `[trigger: 小儿身旺易养]` `[factor_trigger: children_strong_self AND seal_generating_self]` `[role: 主干]` 小儿身旺，又得印绶生身，无财克印，则易养而少灾。 → 《渊海子平·论小儿》
  - `[ns_yhzp_202]` `[trigger: 财多庶出螟蛉]` `[factor_trigger: abundant_wealth_illegitimate AND wealth_harms_seal_parents]` `[role: 条件分支]` 凡小儿命，见财多，必庶出螟蛉，克父母也。 → 《渊海子平·论小儿》
  - `[ns_yhzp_203]` `[trigger: 幼年行运财旺]` `[factor_trigger: abundant_wealth_illegitimate AND major_cycle]` `[role: 条件分支]` 若幼年行运于财旺之乡，财星加重，亦主克父母、养育多波折。 → 《渊海子平·论小儿》
  - `[ns_yhzp_204]` `[trigger: 小儿忌官杀太旺]` `[factor_trigger: has_gates_obstacles]` `[role: 条件分支]` 日主弱而官星七杀太旺，小儿多病多惊，难以安养。 → 《渊海子平·论小儿》
  - `[ns_yhzp_205]` `[trigger: 阳刃伤官多灾]` `[factor_trigger: yang_blade AND injuring_officer]` `[role: 条件分支]` 阳刃伤官太旺，性情好动好强，易招外伤与意外灾祸。 → 《渊海子平·论小儿》
  - `[ns_yhzp_206]` `[trigger: 身弱难养]` `[factor_trigger: children_strong_self]` `[role: 主干依赖]` 身弱则难养，稍逢病灾关煞，即有夭折之虞。 → 《渊海子平·论小儿》
  - `[ns_yhzp_207]` `[trigger: 身旺印绶护身]` `[factor_trigger: children_strong_self AND seal_generating_self]` `[role: 主干依赖]` 身旺又得印绶护身，即使遇财官，亦能较易度过幼年关煞。 → 《渊海子平·论小儿》
  - `[ns_yhzp_208]` `[trigger: 小儿判断纲领]` `[factor_trigger: children_strong_self AND seal_generating_self]` `[role: 总结]` 夫小儿命，大要身旺，最喜印绶生之，无财克之，则易生灾少。 → 《渊海子平·论小儿》

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 小儿身旺 | Children Strong Self | 小儿命以日主旺为佳易养 | Children's fate with strong Day Master easy to raise | children_strong_self | existing |
| 财多庶出 | Abundant Wealth Illegitimate | 财星过多主庶出螟蛉 | Excessive Wealth brings illegitimate/adopted birth | abundant_wealth_illegitimate | existing |
| 印绶生身 | Seal Generating Self | 印绶生日主利小儿 | Seal generating Day Master benefits children | seal_generating_self | existing |"""
    normalized_text_zh: str = """"""
    subject: str = "论小儿"
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论小儿_001_L1",
    )
    version: str = "1.0.0"
