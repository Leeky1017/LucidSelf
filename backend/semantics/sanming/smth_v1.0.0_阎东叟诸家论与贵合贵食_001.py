"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101407
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
    semantic_id="smth_v1.0.0_阎东叟诸家论与贵合贵食_001",
    book_id="sanming",
    engine_id="bazi"
)
class 阎东叟诸家论与贵合贵食(SemanticEntry):
    """
    - **原文（source_text）**：
  阎东叟云：论天乙贵，须就五行喜忌。如甲人有戊有庚，得癸未、乙丑，遇二吉而带印为上，遁见丁丑、辛未者次之，乃三阴喜在印库。乙人得戊申、庚子生旺之土，己人...
    """
    
    original_text: str = """- **原文（source_text）**：
  阎东叟云：论天乙贵，须就五行喜忌。如甲人有戊有庚，得癸未、乙丑，遇二吉而带印为上，遁见丁丑、辛未者次之，乃三阴喜在印库。乙人得戊申、庚子生旺之土，己人得甲申、丙子生旺之水，此阴木阴土喜于财旺。丙丁得丁酉、乙亥，壬癸得乙卯、癸巳，此水火不嫌死绝。六辛得丙寅、丙午，此阴金不嫌鬼胜，得二为上，得一次之。《紫虚局》以此为贵人入庙，遇者主金紫之贵。又曰：贵神在位，诸煞伏藏；二德扶持，众凶解散。凡命中带凶煞，得此二德扶化，凶不为甚；须要日上见，时上不犯克冲刑破方吉。凡人得之，一生安逸，不犯刑，不逢盗，纵遇凶祸，自然消散。与三奇、天月二德同并，尤为吉庆。

- **分字分词释义**：
  - **贵人入庙**：天乙所临之位既合五行喜用，又不受克破，贵气得以完全发挥。
  - **贵合 / 贵食**：贵人与合神、食神交织成局，分别增强名位与禄食。
  - **二德扶持**：天德、月德与天乙同临，能大幅削弱凶煞效力。

- **规范化释义（primary_lang_explained）**：
  阎东叟强调，论天乙贵人必须结合五行喜忌，而不能只看贵人入命与否。甲人若有戊庚，再得癸未、乙丑之印库，相当于贵入印庙，为上等；乙人与己人则喜见财旺之土或水；丙丁、壬癸、六辛各有不同的合贵、贵食配置。总的原则是：贵人临于喜用之地且不受冲破，才称「入庙」，主金紫之贵。进一步指出，若命中带凶煞而又有天乙与二德（天德、月德）扶持，多能化凶为轻或不显；且须贵德在日上见、时上不受刑冲，方为纯粹。

- **核心要点**：
  - 单看「有无天乙」是不够的，还要看贵人所在宫位是否符合日主喜忌、是否与印、财、官、食等形成良性结构。
  - 在系统中，应为每一贵人实例计算一个「入庙度」，综合位置、用神关系与克冲情况，而非一律加分。

- **详细解说**：
  1) 依据阎东叟等人的规则，为每一日干预先标定「喜见的贵位组合」（如甲日喜戊庚并见、贵入印库等），在规则库中编码为条件集合；
  2) 在具体命局中，逐一检查天乙所在宫位是否同时满足：落在喜用之地、与印/财/官/食等形成良性结构、且不受严重刑冲破害，并据此计算 `ru_miao_score`；
  3) 对于与合神、食神形成的「贵合」「贵食」，在职业与资源维度上分别给予不同偏重：贵合偏向名位与身份，贵食偏向禄食与生活质量；
  4) 在整体评分中，将天乙入庙度与二德（天德、月德）同临情况叠加，构成一个「贵德保护指数」，主要用于下调凶煞权重，而不是直接上调财富或官位预测。

- 反例与边界：
  - 不宜仅凭「有天乙 + 有二德」就推断必定金紫之贵，现代社会中更多表现为「在关键节点有人支持、事不过分走极端」；
  - 若贵人虽在喜用宫位但被强冲、重合耗泄严重，工程上应相应降低入庙度，而不是生搬「贵人入庙」之名；
  - 不能在没有验证的情况下，简单将某些古代偏见（如对性别、出身的刻板印象）编码进贵合、贵食解释中；
  - 反向误区是只做「有/无天乙」的粗标签，而不区分入庙与失位，使得贵人相关特征在模型中失去区分度。

- 小例（示意）：
  - 某甲日命，天乙落在未土印库，且未为用神，又与日主成良性生扶结构，系统可给出较高入庙度，并在解释中说明其在学习与专业发展上容易得到制度与师长的支持；
  - 另一命局虽有天乙，但落在忌神之地且被刑冲严重，系统则仅标记为「名册中有贵」而不在关键结论中倚重，避免输出与实际履历严重不符的「贵命」判断。"""
    normalized_text_zh: str = """"""
    subject: str = "阎东叟诸家论与贵合贵食"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_state_factor_117', 'bazi_semantic', 'bazi_relation_factor_52', 'bazi_semantic', 'bazi_relation_factor_53', 'bazi_semantic', 'bazi_relation_factor_54', 'bazi_semantic', 'bazi_condition_factor_33', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_阎东叟诸家论与贵合贵食_001_L1",
    )
    version: str = "1.0.0"
