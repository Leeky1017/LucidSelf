"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042736
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
    semantic_id="smth_v1.0.0_卦气节令与农时大纲_001",
    book_id="sanming",
    engine_id="bazi"
)
class 卦气节令与农时大纲(SemanticEntry):
    """
    - **原文（source_text）**：
  卦气正月为泰，天气下降，当为雨水；二月大壮，雷在天上，当为惊蛰：先雨水而后惊蛰，亦宜也。惊蛰者，万物出乎震，震为雷也。清明者，万物齐乎巽，巽为风也，巽...
    """
    
    original_text: str = """- **原文（source_text）**：
  卦气正月为泰，天气下降，当为雨水；二月大壮，雷在天上，当为惊蛰：先雨水而后惊蛰，亦宜也。惊蛰者，万物出乎震，震为雷也。清明者，万物齐乎巽，巽为风也，巽洁齐而曰清明，清明乃洁齐之义。谷雨三月中，自雨水后土膏脉动，至此又雨，则土脉生物，所以滋五谷之种也。小满四月中，先儒云：小雪后阳一日生一分，积三十日，生三十分而成一昼，为冬至；小满后阴生亦然。至若三月中谷雨，五月中芒种，此二气独指谷麦言：谷必原其生之始，谷种于春，得木之气，成于秋，金克木也；麦必要其成之终，麦种于秋，得金之气，成于夏，火克金也。六月节小暑，六月中大暑：六月中暑之极，故谓大，然未至于大则犹为小也。七月中处暑，七月暑之终，寒之始，大火西流，暑气于是乎处矣；处者，隐也，藏伏之义也。白露八月节，寒露九月节。秋木属金，金色白，金气寒，白者露色，寒者露之气：先白而气始寒，故有渐也。九月中霜降，露寒始结为霜也。立冬后曰小雪、大雪：寒气始于露，中于霜，终于雪；霜之前为露，霜由白而始寒；霜之后为雪，雪由小而至大，皆有渐也。至小寒、大寒，《幽风》云：「一之日徉发，二之日栗烈。」徉发，风寒也，故十一月之余为小寒；栗烈，气寒也，故十二月之终为大寒也。

- **分字分词释义**：
  - **卦气正月为泰**：以易卦配节气，泰卦象天地交泰，正月气象舒和。
  - **惊蛰 / 清明 / 谷雨**：分别对应雷动、风清、雨润三种春季关键现象。
  - **处暑之处**：处为止藏之意，指暑气止而藏伏。
  - **露、霜、小雪、大雪**：同属寒湿现象，分别标志寒气由浅入深的各阶段。

- **规范化释义（primary_lang_explained）**：
  本段依易卦与节气，将一岁节令从雨水、惊蛰、清明、谷雨、小满、芒种、小暑、大暑、处暑、白露、寒露、霜降、小雪、大雪、小寒、大寒依次串起，说明四时气候的渐变：
  春季由雨水滋润大地，经雷动唤醒万物，经风清气朗至清明，再由谷雨加深土脉生机，完成五谷下种的准备；
  夏季由小满提示阴气萌生，经芒种定谷麦之时，再由小暑、大暑推向暑气极盛之顶点；
  秋季从处暑暑气渐藏，至白露、寒露、霜降，寒意由露色之白而至霜凝之寒；
  冬季经小雪、大雪、小寒、大寒，寒气由浅入深，至大寒而极。

- **完整对等诠释（secondary_lang_full）**：
  This section uses the Changes and the twenty‑four solar terms to thread the agricultural year into a single narrative. It walks through the sequence from Rain Water and Awakening of Insects, through Clear and Bright, Grain Rain, Lesser Fullness, Grain in Ear, Lesser Heat and Greater Heat, then on to Limit of Heat, White Dew, Cold Dew and Frost Descent, followed by Lesser Snow, Greater Snow, Lesser Cold and Greater Cold. Together they describe how the qi of the year gradually shifts. In spring, Rain Water moistens the earth, thunder at Awakening of Insects stirs life, Clear and Bright brings clear skies and ordered growth, and Grain Rain deepens the movement of sap so the soil is ready to receive seeds. In summer, Lesser Fullness signals yin beginning to rise within yang; Grain in Ear fixes the timing for sowing and ripening grains; Lesser and Greater Heat push warmth to its peak. In autumn, heat withdraws at Limit of Heat, then dew appears and grows colder until it congeals as frost. In winter, snow and then deeper cold show the yin qi thickening step by step until it reaches its height at Greater Cold. The emphasis is on graded change, not sudden jumps: each term is a marker on a continuous curve of seasonal qi.

- **核心要点**：
  - 节气不是孤立的时间点，而是一条连续的「气机梯度」，每一节只标志一个转折或极点。
  - 命理论用神、调候，离不开对节气真实气候的理解：春主生、夏主长、秋主收、冬主藏，各节只是细分节点。
  - 工程上，可将 24 节气建模为一条连续参数曲线，而不是 24 个离散标签，使「调候」可以与真实气象数据对接。

- **详细解说**：
  1) 在历法模块中，将公历时间先映射到节气坐标（如全年从 0 到 1 的连续值），而非仅记录节气名称；
  2) 调候判断时，以该连续坐标确定所处「气机梯度」：接近雨水/谷雨一段偏湿偏温，接近小寒/大寒一段偏寒偏燥，据此修正五行寒温；
  3) 在命理分析中，将关键节气（如雨水、惊蛰、清明、芒种、处暑、霜降等）视为拐点：同为春生，雨水前后、谷雨前后用神取舍可以不同；
  4) 在工程实现层，将 24 节气、平均温度、湿度等气象数据融合，构建真实的「调候参数」，而不是停留在文字层面。

- 反例与边界：
  - 不宜只看「某人立春生」就简单断为春木旺，而不考虑该年的实际气候是否偏寒或偏暖；
  - 不能把 24 节气当作完全离散、互不连续的 24 个档位，忽略其本质是连续变化曲线上的刻度；
  - 工程上若只用节气名而不用时间坐标与气象数据，模型对调候的刻画会非常粗糙；
  - 反向误区是完全抛弃传统节气，只用现代气象指标，导致无法与经典命理话语体系对齐，难以解释模型行为。

- 小例（示意）：
  - 某命局生于清明前两日，节气坐标仍偏近惊蛰，系统可解释为「虽入清明前夕，但雷动之象仍重，木气未完全齐整」，因此在用神上仍需稍加火与土以扶持生发；
  - 另一命局生于大雪之后不久，气候数据提示该年寒潮较弱，系统则在「严寒」标签上适当降权，避免过度判为极寒格局。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_02_guaqi_001]` `[trigger: 卦气节令]` `[factor_trigger: guaqi_jieqi AND yili_peihe]` `[role: 主干]` 卦气正月为泰，天气下降，当为雨水；二月大壮，雷在天上，当为惊蛰。 → 《三命通会》卷二#卦气节令
  - `[ns_smth_02_guaqi_002]` `[trigger: 四时渐变]` `[factor_trigger: sishi_jianbian AND qiji_tidu]` `[role: 主干依赖]` 节气不是孤立的时间点，而是一条连续的气机梯度。 → 《三命通会》卷二#卦气节令
  - `[ns_smth_02_guaqi_003]` `[trigger: 露霜雪递]` `[factor_trigger: lushuangxue_dijin AND hanqi_youqianrushen]` `[role: 条件分支]` 寒气始于露，中于霜，终于雪，皆有渐也。 → 《三命通会》卷二#卦气节令
  - `[ns_smth_02_guaqi_004]` `[trigger: 调候根基]` `[factor_trigger: tiaohou_genqi AND zhenshi_qihou]` `[role: 总结]` 命理论用神、调候，离不开对节气真实气候的理解。 → 《三命通会》卷二#卦气节令"""
    normalized_text_zh: str = """"""
    subject: str = "卦气节令与农时大纲"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_卦气节令与农时大纲_001_L1",
    )
    version: str = "1.0.0"
