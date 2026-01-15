"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101439
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
    semantic_id="smth_v1.0.0_三奇喜忌与综合判断_001",
    book_id="sanming",
    engine_id="bazi"
)
class 三奇喜忌与综合判断(SemanticEntry):
    """
    - **原文（source_text）**：
  凡命遇三奇，主人精神异常，襟怀卓越，好奇尚大，博学多能。带天乙贵者，勋业超群；带天月二德者，凶灾不犯；带六仪者，才智出类；带三合入局者，国家柱石；带官...
    """
    
    original_text: str = """- **原文（source_text）**：
  凡命遇三奇，主人精神异常，襟怀卓越，好奇尚大，博学多能。带天乙贵者，勋业超群；带天月二德者，凶灾不犯；带六仪者，才智出类；带三合入局者，国家柱石；带官符劫煞者，器识宏远；带空亡生旺者，脱尘离俗，富贵不淫，威武不屈。值元辰、咸池、冲破、天罗地网者，为无用。论三奇，太岁不带而月日时带着，孤独。诗曰：「顺十干神乙丙丁，神童及第播声名；日时禄马公卿煞，换武除文佐圣明。」又曰：「顺十干神甲戊庚，兼得长生丙府名；若然无禄兼无马，只是财中蓄积人。」又曰：「三奇须是重逢贵，方是荣华福寿人；只有空奇无贵地，贫穷下贱被欺凌。」又曰：「乙丙丁、甲戊庚，上局相生生复生，不是蓬莱三岛客，也应金殿玉阶行。」又曰：「欲识岩廊官赫奕，名仙多诞癸壬辛，三奇玉藉传消息，轻薄时师莫与评。」

- **分字分词释义**：
  - **带天乙、二德、六仪、三合**：三奇与其他吉星同见时，格局层次显著提高。
  - **值元辰、咸池、冲破、天罗地网**：三奇若被重煞、桃花、冲网等破坏，多成「空奇无贵地」。
  - **神童及第、金殿玉阶**：诗句中对三奇成功样态的形象描述。

- **规范化释义（primary_lang_explained）**：
  最后，原文从人物气质与实际成就两方面描绘三奇：带三奇者多精神异常、胸襟卓越、好大求新、博学多能；若又兼带天乙、天月二德、六仪、三合，则多为国家栋梁；若再叠加官符、劫煞，则有更强的执行力和承压能力；若落空亡而又生旺，则多有「出尘」之气。反之，若与元辰、咸池、天罗地网等重煞同见，则多为「空奇」——有奇名而无贵地，终为贫贱之人。多段歌诀总结了：三奇最好顺布、多重出现、又有禄马等配合，方能成就真正的荣华福寿。

- **核心要点**：
  - 三奇是高阶格局的「加分器」：必须在良好五行与神煞结构之上，才算真奇；若落在重煞与空亡之中，往往只有性格、聪明，却缺乏合适舞台。
  - 在系统中，可将三奇与天乙、二德、禄马等特征联合作为「高潜人才」标签，同时警惕被重煞和不良结构冲破导致的「高智低配」格局。

- **详细解说**：
  1) 在命局特征提取阶段，以三奇指数为起点，叠加天乙、天月德、禄马、六仪、三合等标签，构建一个「高潜结构向量」；
  2) 同时统计元辰、咸池、天罗地网等重煞以及空亡、冲破等破坏性因素，形成「结构阻力向量」，与高潜向量配对使用；
  3) 在人才潜质、发展路径、风险承载能力等任务中，以「高潜 / 高阻」的组合方式给出判读，而不是单向吹捧或贬抑；
  4) 将三奇相关歌诀中关于「神童及第」「金殿玉阶」的描述转译为「容易在早期学习或专业领域脱颖而出」等可验证指标，避免绝对化的官爵承诺。

- 反例与边界：
  - 不宜见三奇就一味宣称「必为神童、必登金殿」，尤其在现实资料显示教育资源有限或职业路径受限时，应强调「潜质」而非必然结果；
  - 若三奇落在强煞与网罗之地，工程上应将其更多视为「个性与能力的尖锐化」而非纯粹吉象，避免对高风险行为做浪漫化美化；
  - 不能忽略时间维度：三奇在少年、青年、晚年不同阶段发用效果有别，模型若只看静态命局而不结合大运流年，会误判阶段性高光与低谷；
  - 反向误区是对「空奇」案例一概否定，忽视其中在艺术、学术、小众领域实现价值的可能，只从传统官场视角评估人生成败。

- 小例（示意）：
  - 某命局三奇顺布且与天乙、二德并临，但现实出身普通，系统会将其解读为「高潜 + 中等资源」的组合，在解释中强调通过教育与长期积累逐步释放潜力，而不是许诺一蹴而就的荣华；
  - 另一命局三奇指数不低，却与元辰、咸池、重煞并见，现实在高波动行业中屡有大起大落，系统则给出「高智高压、高风险高收益」的结构说明，并建议用户在财务与心理层面建立更稳固的缓冲机制。"""
    normalized_text_zh: str = """"""
    subject: str = "三奇喜忌与综合判断"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_state_factor_124', 'bazi_semantic', 'bazi_state_factor_125', 'bazi_semantic', 'bazi_relation_factor_57', 'bazi_semantic', 'bazi_relation_factor_58', 'bazi_semantic', 'bazi_condition_factor_37', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_三奇喜忌与综合判断_001_L1",
    )
    version: str = "1.0.0"
