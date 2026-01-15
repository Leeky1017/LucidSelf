"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101558
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
    semantic_id="smth_v1.0.0_论孤辰寡宿_001",
    book_id="sanming",
    engine_id="bazi"
)
class 论孤辰寡宿(SemanticEntry):
    """
    - **原文（source_text）**：
  论孤辰寡宿。先贤有云：老而无夫曰寡，幼而无父曰孤，此其义也。辰谓星辰，宿谓星宿，指其神也。人命犯此星辰，则孤寡如是。如亥子丑逐方三位，进前一辰见寅为孤...
    """
    
    original_text: str = """- **原文（source_text）**：
  论孤辰寡宿。先贤有云：老而无夫曰寡，幼而无父曰孤，此其义也。辰谓星辰，宿谓星宿，指其神也。人命犯此星辰，则孤寡如是。如亥子丑逐方三位，进前一辰见寅为孤，退后一辰见戌为寡，又过角为孤，退角为寡，其余三方皆依此推，乃阴阳惆怅之义。且夫寅为春始，辰为春末，巳为夏始，未为夏末，申为秋始，戌为秋末，亥为冬始，丑为冬末，皆阴阳支离之神，四时代谢之方。《三车》云：造物中以生我者为母，克我者为夫，我克者为妻。亥子丑属北方水位，水用金为母，金绝于寅，是母绝也；用火为妻，火墓为戌，是妻墓也。巳午未，南方火位，火用木为母，木绝在申；用水为夫，水墓在辰。寅卯辰属东方木位，木用水为母，水绝在巳；用金为夫，金墓在丑，是取母绝为孤辰，夫墓、妻墓为寡宿，其义尤切。《烛神经》云：「凡人命犯孤寡，主形孤骨露，面无和气，不利六亲。生旺稍可，死绝尤甚。驿马并，放荡他乡；空亡并，幼小无倚；丧吊并，父母相继而亡。一生多逢重丧叠祸，骨肉伶仃，单寒不利。入贵格，赘婿妇家；入贱格，移流未免。」

- **分字分词释义**：
  - **孤 / 寡**：以无父、无夫之象引申为亲缘淡薄、情感孤立之义。
  - **进前一辰为孤、退后一辰为寡**：以三方局前后一辰与隔角等方式取孤寡位置，体现「母绝、夫墓、妻墓」等象。
  - **阴阳支离之神**：指四季始末之支，气机交替之处，易生离散之象。

- **规范化释义（primary_lang_explained）**：
  孤辰寡宿主要反映亲缘与婚姻层面的孤寂：通过三方局（亥子丑、寅卯辰、巳午未、申酉戌）向前或向后取一辰，或隔角取位，来标定「孤」「寡」的宫位，其理论基础源自母绝、夫墓、妻墓等结构。命中犯孤寡者，多主与父母、配偶或子女之间的关系不稳，或身在群体而心多孤独。若再与驿马同见，则常漂泊他乡；与空亡同见，则幼年无倚；与丧吊同见，则多逢重丧叠祸。入贵格者，往往有赘婿、入赘、婚姻结构非常规等情况；入贱格者，则多为移徙漂泊之命。

- **完整对等诠释（secondary_lang_full）**：
  Yang Ren, the Goat Blade, is the label for a stem standing at its point of absolute strength where Lu has tipped over into cutting edge.
  It can grant tremendous drive, courage and capacity to break through resistance when guided by sound structures such as officials and seals, but becomes dangerous when mixed with many uncontrolled Sha or when the person lacks inner regulation.
  Modern reading should therefore distinguish between disciplined high energy configurations and genuinely volatile ones, treating Yang Ren as a double edged indicator of extreme activation.
- **核心要点**：
  - 孤辰寡宿是「关系网络疏离」的标签：并非必然绝嗣绝配，而是提示在家庭与伴侣关系上更需主动经营与修补。
  - 工程化时，可将其建模为亲密关系与家庭支持度的风险因子：对涉及婚姻稳定、家庭纽带与社会支持网络的预测，应适度提高波动与断裂的概率，但同时允许其他吉神结构对其进行修正。

- **详细解说**：
  1) 按三方局与前后取位规则，为命局标注 `gu_chen_flag` 与 `gua_su_flag`，并记录其是否落在命宫、父母宫、夫妻宫、子女宫等关键关系宫位；
   2) 在亲密关系与家庭支持相关任务中，将孤寡结构作为「关系疏离倾向」特征使用，结合驿马、空亡、丧吊等结构综合评估支持网络的稳固度；
   3) 在时间维度上，当大运、流年触发孤寡所在宫位时，提高关系波动与情绪孤独感的预测权重，同时检查是否有贵人、合象等修复性结构出现；
   4) 在解释层用「需要更多主动维护与沟通」等语言替代「必孤必寡」之类绝对化判断，避免心理暗示带来的次生伤害。

 - 反例与边界：
   - 不宜把孤辰寡宿视为「注定无婚无子」的标志，现实中大量带孤寡结构者依然拥有稳定家庭，只是更需刻意经营；
   - 若命主所处文化与社会环境本就鼓励单身或延迟婚育，孤寡的外显形式可能是选择性独身，而非被迫孤立；
   - 工程上若将孤寡直接映射为「情感失败」标签，会强化污名，应更多把它视作对支持网络强度和关系维护难度的提示；
   - 反向误区是完全忽略孤寡，使系统难以解释「关系易疏离、情绪易落单」的体验。

 - 小例（示意）：
   - 某命局孤辰落在命宫、寡宿落在夫妻宫，但同时有天喜、红鸾与贵人同见，现实中虽恋爱与婚姻起步较晚，却最终建立起互相理解的伴侣关系，系统可用「孤寡 + 喜贵修复」解释其先难后成的路径；
  - 另一命局孤寡重叠且与驿马、空亡并见，现实表现为长期异地工作、与原生家庭互动较少，亲密关系多次中断，系统则在解释中提醒其主动建设稳定的支持网络，并在需要时寻求专业帮助。"""
    normalized_text_zh: str = """"""
    subject: str = "论孤辰寡宿"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_chen', 'bazi_semantic', 'bazi_structure_factor_63', 'bazi_semantic', 'bazi_state_strength_10', 'bazi_semantic', 'bazi_function_relation', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_论孤辰寡宿_001_L1",
    )
    version: str = "1.0.0"
