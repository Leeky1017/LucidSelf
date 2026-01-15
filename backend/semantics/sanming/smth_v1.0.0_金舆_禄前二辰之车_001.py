"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101335
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
    semantic_id="smth_v1.0.0_金舆_禄前二辰之车_001",
    book_id="sanming",
    engine_id="bazi"
)
class 金舆禄前二辰之车(SemanticEntry):
    """
    - **原文（source_text）**：
  论金舆。舆者，车也；金者，贵之义也。譬之君子居官得禄，须坐车以载之，故金舆常居禄前二辰。如甲子人禄在寅，辰为金舆是也。此煞乃禄命之旄旗，三才之节钺。主...
    """
    
    original_text: str = """- **原文（source_text）**：
  论金舆。舆者，车也；金者，贵之义也。譬之君子居官得禄，须坐车以载之，故金舆常居禄前二辰。如甲子人禄在寅，辰为金舆是也。此煞乃禄命之旄旗，三才之节钺。主人性柔貌愿，举止温克；妇人逢之，不富即贵；男子得之，多妻妾，阴福相扶持。生日、生时遇之为佳，骨肉平生安泰，得贤妻妾，子孙茂盛。如皇族多带此煞，常格得之，身在无气中生，主作赘。紫虚局云：「禄前二辰号金舆，遇此之人福最殊。偏主聪明多富贵，一生清泰亦无虞。」

- **分字分词释义**：
  - **金舆**：象征贵车，喻禄位之前二辰所具的承载与尊贵功能。
  - **禄前二辰**：以日主之禄为基，向前数二辰所至之地支为金舆位。
  - **旄旗、节钺**：古代军礼与权力象征，暗示金舆与权势、仪仗相关。

- **规范化释义（primary_lang_explained）**：
  金舆之「舆」为车，「金」为贵，整体象征贵人所乘之车。以甲子人为例，其禄在寅，向前数二辰至辰，即为金舆。原文称金舆为禄命之旄旗、三才之节钺，提示此煞常与身份与礼制有关。命带金舆者，多性情温柔、举止端庄：妇人命中见之，多主不富即贵；男子则多得妻妾之助，有阴福相扶持。生日、时柱见金舆更佳，主骨肉和顺、贤内助与子孙繁盛。若皇族之命多带此煞，即使出身无气之地，也往往以赘婿等方式入贵门。紫虚局歌诀进一步强调：禄前二辰之金舆，多主聪明富贵，一生清泰无忧。

- **完整对等诠释（secondary_lang_full）**：
  Jinyu, the golden carriage, is the branch two steps ahead of a stem Lu position and represents the vehicle that carries rank and livelihood.
  When it is active the person tends to have gentle manners, a presentable public image and solid support from spouse and family, so that blessings are borne and displayed rather than left bare.
  It strengthens stability, domestic help and social packaging more than it creates rank by itself, and should be read as an auxiliary to an already sound Lu structure.
- **核心要点**：
  - 金舆的核心象是「承载禄位之车」，在结构上多与婚姻、家庭与身份包装相关。
  - 取金舆必须先定禄，再推前二辰，工程化时可以将其视为「相对位置」而非绝对坐标。
  - 在系统中，金舆可作为增强「社会地位、婚姻助力、生活稳定度」的辅助因子使用，而不宜单独作为贵格判定依据。
 
- **详细解说**：
  1) 判定日主与其本禄位（如甲禄寅、乙禄卯等），在系统中记录禄支 `lu_branch`；
  2) 在地支循环序列中（子→丑→…→亥→子）自禄支向前顺数两位，得到金舆所在支 `jinyu_branch`，并为四柱中落在该支的位置打上「金舆」标签；
  3) 区分生日、时柱、年柱等不同落点：日、时上的金舆权重更高，可标记为「核心生活圈金舆」，年柱上的则偏向「家族/出身层金舆」；
  4) 在高层建模中，将金舆特征主要用于刻画「生活稳定度、婚姻与伴侣支持、社会身份包装」维度，而不是简单当作财富或官位标签。

- 反例与边界：
  - 不宜把金舆视为「一见必贵」，尤其不能机械套用古书对皇族、赘婿等情形的描述到现代个体；
  - 金舆偏重「承载与包装」，若命局本身五行失衡或煞重，金舆更多提供缓冲与修饰，而非根本改变格局；
  - 工程实现中，若只以「有/无金舆」二值特征直接推导婚姻或财富结论，容易造成过拟合，应与禄位、贵人、财官等特征联合建模；
  - 反向误区是完全忽略金舆，只看禄马等结构，从而丢失关于「家庭/伴侣助力」「仪态与体面」这类软性变量的信息。

- 小例（示意）：
  - 某甲日命，甲禄寅、金舆在辰，命局年支辰、时支亦见辰，系统可标为「家族与晚年生活均有金舆加持」，在解释中偏向「家庭生活较安稳、伴侣与子女在物质和情感上都有一定承载力」；
  - 另一命局禄位清纯但金舆全不入命，系统会提示「自身资源根基尚可，但在配偶与家庭支撑上不占明显优势」，以免对婚姻与生活质量做出过度乐观预期。"""
    normalized_text_zh: str = """"""
    subject: str = "金舆：禄前二辰之车"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_metal', 'bazi_semantic', 'bazi_state_metal_marker', 'bazi_semantic', 'bazi_function_metal', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_金舆_禄前二辰之车_001_L1",
    )
    version: str = "1.0.0"
