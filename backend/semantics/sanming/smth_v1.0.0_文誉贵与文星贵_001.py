"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101486
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
    semantic_id="smth_v1.0.0_文誉贵与文星贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 文誉贵与文星贵(SemanticEntry):
    """
    - **原文（source_text）**：
  有文誉贵，如甲子人见壬戌、丙寅，禄前禄后一般神，必作公卿冠世人：立性天聪，名誉播，富贵荣华，事业新。有文星贵：甲马乙蛇丙戊猴，酉台丁己亥辛求；庚逢戌狗...
    """
    
    original_text: str = """- **原文（source_text）**：
  有文誉贵，如甲子人见壬戌、丙寅，禄前禄后一般神，必作公卿冠世人：立性天聪，名誉播，富贵荣华，事业新。有文星贵：甲马乙蛇丙戊猴，酉台丁己亥辛求；庚逢戌狗，逢虎；十位文星癸兔游。

- **分字分词释义**：
  - **文誉贵**：偏重「名誉与社会声望」之贵，尤其与禄前禄后之神同见时更显。
  - **文星贵**：更偏向文采与才华本身，对文字与思维的敏捷度有加持。

- **规范化释义（primary_lang_explained）**：
  文誉贵强调的是名声与社会评价：如甲子人见壬戌、丙寅之类，禄前禄后皆有吉神相应，多主天性聪明、名誉远播，富贵兼备。文星贵则通过另一套口诀列出十位文星所在，对应各日主可能获得的文章才华之资。二者皆属「文贵」，但文誉贵偏外在评价，文星贵偏内在文才。

- **完整对等诠释（secondary_lang_full）**：
  Literary Fame Noble stresses public reputation and the broadcasting of name, especially when linked with stems and branches around the Lu position before and after.
  Literary Star Noble points more to inner literary talent and quickness of thought, defining positions where the mind readily turns ideas into text.
  In evaluation these can be separated into a fame axis and a talent axis so that a person may have deep skill without wide renown, or high visibility without equivalent depth.
- **核心要点**：
  - 文誉贵与文星贵的吉凶，取决于是否落在用神之地、是否受克冲破坏；在工程化时，可分别建模为「社会声望」与「文才潜力」两个维度。
  - 当与太极贵、天乙、三奇等同见时，往往指向「文臣型高位」的格局，在高层职业路径预测中权重可适度提高。
 
- **详细解说**：
  1) 在特征工程中，将文誉贵位置编码为 `fame_nodes`，文星贵位置编码为 `talent_nodes`，分别记录其所落宫位、十神属性与是否为用神；
   2) 基于现实数据，构建两个相对独立的评分：`fame_score`（社会声望维度）与 `literary_talent_score`（文才潜力维度），并与职业类型、公开曝光度等变量对照；
   3) 当文誉、文星与太极贵、天乙、三奇等同见时，在「高层文职/知识精英」相关任务中适度提高上限预测，同时在解释中说明这是一种「条件上限」，仍需后天轨迹匹配；
   4) 在解释输出中区分「作品质量」「社会知名度」与「职位层级」三个维度，避免将文贵结构简单等同于任何一个单一指标。

 - 反例与边界：
   - 不宜把文誉贵直接解读为「必然网红/明星」，也不应将文星贵简单视为「必然成为作家」，应根据命主实际行业与行为路径调整解释；
   - 若文誉贵落在忌神宫或被严重冲破，可能表现为「名声与能力不匹配」「高调易招非议」，工程上应允许文誉特征在负向维度上发挥作用；
   - 对于仅有文星贵而无配套格局支持的命局，不能一味许以高位，更多是「才华内向化」或在小众领域发光，需要在推荐中强调合适的舞台与载体；
   - 反向误区是只看职位与收入，不建模文誉与文才维度，使系统难以解释「低调高能」「高调低配」这类现实类型。

 - 小例（示意）：
   - 某命局文誉贵坐用神位，又与天乙、三奇同见，现实中既有高质量著作又在公共领域具有一定影响力，系统可将其解读为「文职高层潜力型」，在职业建议中偏向学术、传媒或政策研究等路径；
  - 另一命局文星贵强而文誉贵弱，现实中在专业领域颇有造诣却名声有限，系统则强调其「深度文才」而非「广泛名望」，并建议选择重内容、轻曝光的职业与发展策略。"""
    normalized_text_zh: str = """"""
    subject: str = "文誉贵与文星贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_3', 'bazi_semantic', 'bazi_structure_factor_54', 'bazi_semantic', 'bazi_function_factor_6', 'bazi_semantic', 'bazi_function_factor_7', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_文誉贵与文星贵_001_L1",
    )
    version: str = "1.0.0"
