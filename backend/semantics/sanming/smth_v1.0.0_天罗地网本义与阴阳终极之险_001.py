"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101565
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
    semantic_id="smth_v1.0.0_天罗地网本义与阴阳终极之险_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天罗地网本义与阴阳终极之险(SemanticEntry):
    """
    - **原文（source_text）**：
  论天罗地网。罗网之说，其义甚明。然何以戌亥为天罗，辰巳为地网？盖天倾西北，戌亥者六阴之终也；地陷东南，辰巳者六阳之终也。阴阳终极，则暗昧不明，如人之在...
    """
    
    original_text: str = """- **原文（source_text）**：
  论天罗地网。罗网之说，其义甚明。然何以戌亥为天罗，辰巳为地网？盖天倾西北，戌亥者六阴之终也；地陷东南，辰巳者六阳之终也。阴阳终极，则暗昧不明，如人之在罗网，此其义也。《壶中子》云：「龙蛇混杂，偏不利于辰生；猪犬侵凌，但独嫌于亥字。」龙为辰，蛇为巳：辰人得巳，巳人得辰，皆曰龙蛇混杂；男命则不妨，惟女命破婚害子，薄命抱疾。辰人得巳重，巳人得辰轻，谓龙生蛇穴者退，蛇生龙穴者进。猪为亥，犬为戌：戌人得亥，亥人得戌，皆曰猪犬侵凌；女命则不妨，惟男命则滞龃龉龆，妨祖克妻。戌人得亥轻，亥人得戌重，谓犬入猪群则进，猪入犬群则伤。《诸书》亦云：「龙蛇混杂，常防妇女忧危；猪犬侵凌，每虑丈夫厄难。」是男怕天罗，女怕地网。中间又分火命人有天罗，水、土命人有地网，余金木二命无之。人命带此，多主蹇滞，更加恶煞相并、五行无气者，必主恶死；行运至此，亦如之。假如戌年戌月初一日生者，犯一年天罗；十五日生者，犯十五年天罗；若更生时是戌，增成三十年天罗；或戌年亥月，或亥时戌日，交互见之，谓之重犯，则灾不能歇。地网如上说。

- **分字分词释义**：
  - **戌亥为天罗、辰巳为地网**：分别取六阴终极与六阳终极之位，象征气机穷尽、易陷罗网。
  - **龙蛇混杂、猪犬侵凌**：以辰巳、戌亥互见形容婚姻与人事上的纠缠感与压迫感。
  - **男怕天罗、女怕地网**：点出性别与命局类型在受煞方式上的差异。

- **规范化释义（primary_lang_explained）**：
  天罗地网以阴阳终极之地来象征人生中难以摆脱的困局：天罗在戌亥，重于男命；地网在辰巳，重于女命。命局中若见辰巳互临，或戌亥互临，更与恶煞同见而五行无气者，多主蹇滞与恶死之忧。原文通过「龙蛇混杂」「猪犬侵凌」比喻男女在婚姻、家族与身体健康上所受的纠缠与侵害，指出同一结构在男女命中的侧重点不同。行运再犯天罗地网，尤需慎防长时段的隐性风险。

- **完整对等诠释（secondary_lang_full）**：
  Tian Luo and Di Wang, the Heavenly Net and Earthly Snare, are assigned to Xu Hai and Chen Si as the ultimate ends of yin and yang, places where light and order fade into confusion.
  The imagery suggests being caught in a mesh at the very edge of a cycle, so traditional texts associate these positions with entanglement, obstruction and in severe cases fatal traps, especially when combined with other harsh stars.
  In contemporary work they are better understood as markers of environments that are opaque, over constrained or hard to exit, raising the need for caution and structural support rather than guaranteeing catastrophe.
- **核心要点**：
  - 天罗地网是「长期困局」与「边缘极端状态」的象征，比一般单一事件煞更侧重环境与结构性的压迫感。
  - 在工程化分析中，可将其建模为「高难度环境因子」：当与其他重煞、五行失衡同见时，提高恶性事件与长时间困顿的权重；当有贵人、德星、空亡等缓冲结构时，则更多解释为「高压环境中仍有转圜」。

- **详细解说**：
  1) 依据性别、命局五行类型与干支组合，为命局标注 `tian_luo_flag` 与 `di_wang_flag`，并记录其落在年、月、日、时以及命宫、夫妻宫、疾厄宫等关键宫位的分布；
   2) 计算 `luo_wang_overlap_score`：当天罗地网与羊刃、劫煞、灾煞等重煞、以及五行失衡结构重叠时提高其权重，与德秀、天德、贵人、印绶同见时则相应下调；
   3) 在长期风险与环境难度建模中，将天罗地网视为「结构性高难度环境」因子，用于提高「长期慢性压力」「难以脱身的约束」等情形的先验概率，而非单一年份的灾祸；
   4) 在解释输出中，结合实际职业与社会环境，将天罗地网描述为「所处环境规则更苛刻、转身空间更窄」，并提示寻找支持系统与可行的调整路径。

 - 反例与边界：
   - 不宜见一处天罗或地网就断「必有恶死」，原文本身也强调必须与恶煞、五行无气等多重条件叠加才为大凶；
   - 若现实中命主拥有良好的社会支持网络、稳定制度保障（如健全的医疗与法律体系），则天罗地网多体现为「压力与束缚感较强」，不必对应极端灾难事件；
   - 工程上若将 `tian_luo_flag`、`di_wang_flag` 直接当作致命风险标签，会极大夸大其作用，应更多视为环境难度修正因子；
   - 反向误区是完全忽略天罗地网，使模型在解释「长期被困感、反复受限」的体验时缺乏结构性变量支撑。

 - 小例（示意）：
   - 某男命多重天罗叠见官符与灵煞，现实中长期处于高压体制环境，既要应对严格纪律又难以自我调适，建议寻找外部心理支持。"""
    normalized_text_zh: str = """"""
    subject: str = "天罗地网本义与阴阳终极之险"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_64', 'bazi_semantic', 'bazi_structure_factor_65', 'bazi_semantic', 'bazi_state_factor_141', 'bazi_semantic', 'bazi_function_factor_15', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_天罗地网本义与阴阳终极之险_001_L1",
    )
    version: str = "1.0.0"
