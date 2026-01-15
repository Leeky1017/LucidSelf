"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101415
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
    semantic_id="smth_v1.0.0_天乙贵人与实际判断边界_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天乙贵人与实际判断边界(SemanticEntry):
    """
    - **原文（source_text）**：
  《烛神经》曰：「天乙贵遇生旺，则形貌轩昂，性灵颖悟，理义分明，不喜杂术，纯粹大器，身蕴道德，众人钦爱。死绝，则执拗自是，喜游近贵。与劫煞并，则貌厚有威...
    """
    
    original_text: str = """- **原文（source_text）**：
  《烛神经》曰：「天乙贵遇生旺，则形貌轩昂，性灵颖悟，理义分明，不喜杂术，纯粹大器，身蕴道德，众人钦爱。死绝，则执拗自是，喜游近贵。与劫煞并，则貌厚有威，多谋足计。与官符并，则文翰飘逸，高谈雄辩。与建禄并，则文翰纯实，济惠广游，君子人也。若落天中，或与天中合，或与天中连珠，当有伶伦之态，好呕吟，伎艺人也。」又曰：「天乙贵，三命中最吉之神。若人遇之则荣，功名早达，官禄亦易近。如三命皆乘旺气，终登将相公侯之位。大小运行年至此，亦主迁官进财，一切加临，至此皆为吉兆。」《理愚歌》云：「贵人或落空亡里，禄马背违如不值。」《宝鉴》云：「贵人无气，虽有如无。」《洞玄经》云：「贵人嗔则凶来。」

- **分字分词释义**：
  - **天乙遇生旺 / 死绝**：贵人所处宫位气机生旺则善，死绝则效力大减甚至反生偏执。
  - **与劫煞、官符、建禄并**：贵人与不同神煞并见，呈现出威重、文翰、广游等不同侧面。
  - **贵人无气、落空亡**：贵人虽在名册，但所在宫位无气或入空亡，则当作减分甚至视为无。

- **规范化释义（primary_lang_explained）**：
  《烛神经》与诸书综合，给出对天乙贵人的多维评价：贵人若临于生旺之地，多主形貌轩昂、性情聪悟、讲理重义、不屑杂术，为纯粹大器；若落于死绝之地，则多偏执自是、好游近贵而不自量力。贵人与劫煞、官符、建禄等同临，又会分别显出威仪、文才、广交游等不同面貌。总体而言，天乙贵人是命式中极重要的吉神之一，但前提仍是「有气而不空亡」。若贵人落空亡、与禄马背违，或本身无气，则虽有名号而难以真正护持；若贵人本身气盛却被强煞激怒（「贵人嗔」），亦可能转成凶应。

- **核心要点**：
  - 天乙贵人的作用有强有弱、有正有偏，不能一见贵人便一味报喜；必须结合气机、同宫神煞与用神一并判断。
  - 工程化时，可为天乙贵人设计多个维度：是否在用神宫、是否生旺、是否空亡、是否与重煞或德神同临，让模型能够做细致的权重调整，而不是简单「贵人=吉」。

- **详细解说**：
  1) 在前几节已建立的基础上，为每一贵人实例汇总多维信息：所在宫位、十神属性、生旺衰绝、是否空亡、是否与凶煞或德神同宫、是否合禄马等；
  2) 基于这些信息计算一个分段的 `tianyi_score`，并拆分为「保护力」「资源力」「修饰度」等子维度，而不是单一分值；
  3) 在具体任务中（如职业上限预测、风险评估、关系支持度等），选取与任务最相关的维度参与建模，避免让天乙在所有预测中一刀切地加分；
  4) 在解释层，将「天乙遇生旺」「天乙落死绝」「贵人嗔则凶来」等古语转译为现代语言，如「支持系统稳固/支持系统失效/支持系统被卷入冲突」，并提供相应的实践建议。

- 反例与边界：
  - 不宜在没有观察到现实支持系统的情况下，仅凭天乙标签断定命主「一生安逸、不犯刑盗」，否则容易与现实经历产生严重冲突；
  - 对于带有明显高风险职业或重大创伤经历的命例，即便天乙分数较高，也应在解释中强调其「缓冲与修复」意义，而非否认风险或痛苦的存在；
  - 工程上若忽略「贵人无气」「贵人落空亡」「禄马背违如不值」等边界，只保留正向语句，会系统性高估贵人效果；
  - 反向误区是看到古籍中「贵人嗔则凶来」等说法，就把所有贵人与凶事机械挂钩，而不考虑具体组合与现代场景。

- 小例（示意）：
  - 某命局贵人临日支且与天德月德同宫，现实中虽有几次重大变动，但多能逢凶化吉，系统可解释为「身边稳定的制度与贵人系统在关键时刻提供托底」，同时提醒其珍惜与维护这些支持关系；
  - 另一命局贵人落于死绝且空亡，又与重煞并行，现实中在高压环境中屡遭人际背刺，系统则会将天乙视为「名义上的贵人」而非实在护持，并提示其需要建立更可靠的现实支持网络。"""
    normalized_text_zh: str = """"""
    subject: str = "天乙贵人与实际判断边界"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_state_factor_118', 'bazi_semantic', 'bazi_state_factor_119', 'bazi_semantic', 'bazi_state_factor_120', 'bazi_semantic', 'bazi_relation_factor_55', 'bazi_semantic', 'bazi_condition_factor_34', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_天乙贵人与实际判断边界_001_L1",
    )
    version: str = "1.0.0"
