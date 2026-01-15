"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101456
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
    semantic_id="smth_v1.0.0_二德化凶与天月德合_001",
    book_id="sanming",
    engine_id="bazi"
)
class 二德化凶与天月德合(SemanticEntry):
    """
    - **原文（source_text）**：
  盖日月照临之宫，凡天曜地煞尽可制服，故可回凶作吉。阎东叟云：「贵神在位，诸煞伏藏；二德扶持，众凶解散。」凡命中带凶煞，得此二德扶化，凶不为甚；须要日上...
    """
    
    original_text: str = """- **原文（source_text）**：
  盖日月照临之宫，凡天曜地煞尽可制服，故可回凶作吉。阎东叟云：「贵神在位，诸煞伏藏；二德扶持，众凶解散。」凡命中带凶煞，得此二德扶化，凶不为甚；须要日上见，时上不犯克冲刑破方吉。凡人得之，一生安逸，不犯刑，不逢盗，纵遇凶祸，自然消散。与三奇、天乙贵同并，尤为吉庆。或财官、印绶、食神、变德，各随所变，更加一倍之福。入贵格，主登科甲，得君宠任；或承祖荫，亦得显达。入贱格，一生温饱，福寿两全；纵有蹇滞，亦能守分固穷，不失为君子。女命得之，多为贵人之妻。《三命铃》云：「天德者，五行福德之辰，若人遇之，主登台辅之位，更有月德并者尤好；纵有凶煞，亦主清显。」《子平赋》云：「印绶得同天德，官刑不犯，至老无殃。」是天德胜月德也。考大统历，有天月德合，乃五行相契之辰：月备合，如正月丙与辛合，二月甲与己合，三月壬与丁合，四月庚与乙合，余照此；天德合，如正月丁与壬合，二月坤与巽合，三月壬与丁合，四月辛与丙合，余照此。

- **分字分词释义**：
  - **二德扶持，众凶解散**：天德、月德同时出现，可以显著削弱命中凶煞的实际应验程度。
  - **天月德合**：天德所主之干与月德所主之干在特定月份相合，为五行相契之辰。

- **规范化释义（primary_lang_explained）**：
  原文明确指出，日月光照之处，众凶煞多可被制服，故天德、月德所在宫位常常成为「化煞中心」。阎东叟说贵神在位、二德扶持，则诸煞伏藏，众凶解散；命中若凶煞甚多而又得二德相助，往往只是「有名无实」的凶，不至于极端。进一步区分贵格与贱格：有德星加持者，不论贫富，人生多平稳安逸、福寿双全。天德相较月德更为有力；二者合临（天月德合）之时，为五行相契之辰，尤为可贵。

- **完整对等诠释（secondary_lang_full）**：
  When both virtue stars operate together, the palace they touch becomes a centre of transformation and malefics there often manifest only in name while outcomes remain within safe bounds.
  Charts heavy in Sha but strongly supported by Heaven Virtue and Moon Virtue tend to show lives with pressure and risk that nonetheless repeatedly turn away from extremes.
  The configuration called Heaven Moon Virtue Combination further enhances this buffering effect and is best understood as a powerful risk reduction field, not as a blanket promise of high office.
- **核心要点**：
  - 天月二德的功能类似加强版「风险缓释器」，尤其适合用于解释「命盘多煞而现实人生并不极端」的情形。
  - 建模时，可以针对含有大型凶煞组合的命局，检查是否同时含有天德、月德，并在预测输出中适当降低极端负面事件的概率，提升「有惊无险」类结果权重。

- **详细解说**：
  1) 在规则层中定义「二德扶持」与「天月德合」的触发条件，如：命局中某一宫位同时为天德、月德所在，或天德干、月德干在特定月份相合；
  2) 对于满足触发条件且同时存在大型凶煞组合的命局，在风险评分模型中对极端事件（重刑、恶死、破产等）的基线概率进行降权，并同步提升「有惊无险、逢凶化吉」类型的结果权重；
  3) 在输出解释时，将这种调整表述为「存在缓冲与修复机制」，而不是否认风险本身，保持对用户经历的尊重；
  4) 对于贵格样本（如官印清纯、二德同临），可在职业与社会地位预测中增加上限，但仍需考虑教育、时代等现实变量。

- 反例与边界：
  - 不宜把任何带二德的命局都视为「一生无大祸」，更不宜用「有德星」去否定已经发生的严重负面事件；
  - 若命局几乎不见凶煞，却硬要强调二德化凶，反而会让解释显得牵强，应回到五行与十神的基本结构来说明人生平顺的原因；
  - 工程上若将「天月德合」设计成过于苛刻或过于宽松的触发条件，都会导致模型对二德作用的估计失真，需要通过实证数据校正；
  - 反向误区是只用「有/无二德」粗标签，而不区分一德、二德同临、德合等层次，失去对缓冲强度的细致刻画。

- 小例（示意）：
  - 某命局七煞遍布且行运多见刑冲，但日支为天德、月支为月德，现实中虽有官非与健康危机却多能转危为安，系统可解释为「高风险 + 强缓冲」的结构，并建议持续经营支持网络与健康管理；
  - 另一命局仅有月德而无天德，凶煞组合相对温和，现实表现为「偶有波折但整体平顺」，系统则将月德视作次一级缓冲，用于解释轻度风险被柔化的现象。"""
    normalized_text_zh: str = """"""
    subject: str = "二德化凶与天月德合"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_1', 'bazi_semantic', 'bazi_function_factor_3', 'bazi_semantic', 'bazi_state_factor_126', 'bazi_semantic']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_二德化凶与天月德合_001_L1",
    )
    version: str = "1.0.0"
