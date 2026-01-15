"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699522
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
    semantic_id="zw_v1.0.0_安禄山命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安禄山命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府加会双禄朝垣**：紫微天府加会，双禄星同向命宫来朝，主极高权财与富贵潜力。
  - **紫破辰戌铃星寅方**：紫微破军居辰戌轴，铃星在寅方同位，主结构不稳、叛逆之...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府加会双禄朝垣**：紫微天府加会，双禄星同向命宫来朝，主极高权财与富贵潜力。
  - **紫破辰戌铃星寅方**：紫微破军居辰戌轴，铃星在寅方同位，主结构不稳、叛逆之象。
  - **为臣不忠**：超越臣子边界，有僭越与反叛之心。
  - **流年羊行酉地**：流年羊刃行至酉宫，主权势倾覆与冲突。
  - **巨门化忌**：巨门星化为忌星，主口舌是非、疑忌与暗中毁誉。
  - **天伤天刑**：天伤与天刑同会，主身体伤损或司法刑戴、兵戈诛戴。
  - **阴男火六局**：安禄山命盘的五行局数，火六局主热情执行与躁动。

- **原文（source_text）**：  
  安禄山命。阴男火六局。紫府加会，双禄朝垣，左右拱照，无不富贵。只嫌紫破，居于辰戌，铃星同位寅方见方忌，主为臣不忠。流年羊行酉地，流年巨门又化忌，小限天伤天刑，主凶亡。

- **规范化释义（primary_lang_explained）**：  
  安禄山命为阴男火六局，命宫紫微、天府加会，又有双禄朝垣，左右同来拱照，是极厚的富贵权势格局，一旦得时得地，权财并至，位极显赫。然而原文以「只嫌紫破，居于辰戌，铃星同位寅方见方忌」点出其内在隐患：紫破辰戌本多主结构不稳、臣道不守，铃星在寅方同位，更添躁动与叛逆之象，显示其为臣不忠的倾向。  
  行运至流年羊刃在酉地，又逢流年巨门化忌，小限再遇天伤、天刑等重凶，形成「羊刃 + 忌化巨门 + 天伤天刑」的多重冲击，一方面象征权势倾覆、风评逆转，一方面暗示身处兵戈、诛戮或刑戮之中，终以凶亡收场。此命例即以安禄山为代表，呈现「极富贵之权臣，终以叛乱与重凶运相会而身死名裂」的轨迹。

- **完整对等诠释（secondary_lang_full）**：  
  An Lushan’s chart is described as that of a Yin Fire native of the Sixth Configuration. Zi Wei and Tian Fu converge on the Life palace, joined by a pair of Lu stars "facing the court" and flanked by Left and Right Assistants. This is an exceptionally potent pattern for wealth and rank, promising high office and abundant resources when circumstances align. Yet the text immediately points out the hidden flaw: Zi Wei with Po Jun located on the Chen‑Xu axis, together with the bell star Ling appearing in the Yin direction—"a tabooed position for the bell"—indicates deep structural instability and disloyalty in the role of a subject.  
  In the fateful years, the flowing Yang Blade passes through You, while the transiting Ju Men star turns into Ji; the minor period at the same time encounters Tian Shang and Tian Xing. This combination of Blade, malefic transformation and punitive stars forms a configuration of violent upheaval: power collapsing, reputation reversing, and the body exposed to war, suppression or execution. The case takes An Lushan as its exemplar: a minister raised to extreme favour and authority, whose betrayal of the throne and collision with severe transits end in a notorious and violent death.

- **核心要点**：  
  1. 紫府加会、双禄朝垣、左右拱照，构成极高权财与富贵潜力的权臣格局。  
  2. 紫破辰戌并见铃星寅方，象征臣道不忠、结构不稳，内里潜藏叛逆因子。  
  3. 流年羊行酉地、巨门化忌，小限天伤天刑同会，形成叛乱失败与凶亡收场的高危运段。

- **叙事素材（narrative_snippets）**：
  - **极盛权势**："紫府加会，双禄朝垣，左右拱照，无不富贵"，安禄山命主得紫府双禄与左右辅弼同来，一度权倾一时。
  - **臣道不忠**："只嫌紫破，居于辰戌，铃星同位寅方见方忌，主为臣不忠"，紫破辰戌配铃星寅方，将其推向僭越与反叛之路。
  - **叛乱凶年**："流年羊行酉地，流年巨门又化忌，小限天伤天刑，主凶亡"，羊刃、化忌巨门与天伤天刑叠加，为叛乱失败、身死名裂的岁运组合。
  - **现代应用**：对拥有巨大组织资源却缺乏自我约束的人而言，一旦命局又带紫破、铃星等不稳结构，在关键年份里「以身试法」往往引来的是系统性清算，而非侥幸过关。"""
    normalized_text_zh: str = """"""
    subject: str = "安禄山命"
    factor_refs: list = ['pattern_zifu_jiahui', 'pattern_shuanglu_chaoyuan', 'pattern_zipo_chenxu', 'malefic_lingxing_yinfang', 'malefic_jumen_huaji', 'malefic_tianshang_tianxing']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_安禄山命_001_L1",
    )
    version: str = "1.0.0"
