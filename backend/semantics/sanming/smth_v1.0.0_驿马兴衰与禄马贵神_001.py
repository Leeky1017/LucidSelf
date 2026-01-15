"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101362
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
    semantic_id="smth_v1.0.0_驿马兴衰与禄马贵神_001",
    book_id="sanming",
    engine_id="bazi"
)
class 驿马兴衰与禄马贵神(SemanticEntry):
    """
    - **原文（source_text）**：
  凡柱中驿马，若不值空亡、破败、交退、伏神，须荣贵。互禄共天乙贵神，同其马位，更得诸煞相并，官秉大权，贵居廊庙：时为上贵，日为中贵，月为常庶。库马主少年...
    """
    
    original_text: str = """- **原文（source_text）**：
  凡柱中驿马，若不值空亡、破败、交退、伏神，须荣贵。互禄共天乙贵神，同其马位，更得诸煞相并，官秉大权，贵居廊庙：时为上贵，日为中贵，月为常庶。库马主少年之喜，旺马资壮岁之荣，生马老方得遂而官卑任远矣，如木生亥旺卯库未，余仿此。《珞子》云：「生马未必有马，背禄未必无禄，看其旺库，不问背生；妙在消息盈虚也。」又曰：驿马者，三命中发用、喜庆之神。若人遇之，君子常居荣位，小人主丰赡。大小运行年至此，主得官及迁改之喜；小运及行年合驿马，并主迁官得禄，如甲子人驿马在寅，小运及太岁至亥，亥与寅合之类是也。

- **分字分词释义**：
  - **空亡、破败、交退、伏神**：驿马被空亡或败气、退气、伏藏神所占，动象受阻。
  - **库马 / 旺马 / 生马**：驿马在库地、旺地、生地，各主少年、壮年与老年的不同荣誉模式。
  - **生马未必有马，背禄未必无禄**：强调不能单看表面「背禄」或「生马」，仍需回到旺库与调候整体判断。

- **规范化释义（primary_lang_explained）**：
  这里给出驿马的一般判断原则：柱中有驿马且不逢空亡、破败、交退、伏神，多主荣贵与迁动喜事；驿马若与禄位、天乙贵人同宫或互见，再兼他吉煞，则官权更重、位阶更高，且发应于不同时柱（时>日>月）。同时区分库马、旺马与生马：库马多主少年喜事，旺马主壮年荣名，生马则多在老年出头但官职不高。引用《珞子》之言，再度提醒要从旺库与盈虚处着眼，而非拘泥表面「有马/无马、背禄/不背」。

- **核心要点**：
  - 驿马不是单纯的「奔波星」，更是「发用与喜庆之神」，关键在于其是否有力、得地、不被破坏。
  - 工程中应为驿马设计「动量 + 资源 + 时段」三个维度的特征：是否动、动时是否有资源、在哪个阶段最易显效。
 
- **详细解说**：
  1) 计算命局中各柱是否落在驿马位，并评估其所处状态（旺、库、生、绝等），形成「驿马动量」指标；
  2) 检查驿马是否与禄位、天乙贵人等同宫或互照，若有则在「资源与贵助」维度加权，形成「禄马贵」复合特征；
  3) 将驿马所落宫位对应到人生阶段（少年、壮年、老年）与现实领域（家乡/外地、基层/高层岗位），构建「时段与场景」映射；
  4) 在预测迁移、职位调整或重大项目变更时，综合上述指标判断属于「有资源支撑的良性变动」还是「被动奔波」。

- 反例与边界：
  - 不宜把任何驿马都解释为「频繁搬家」或「离乡背井」，尤其在远程工作、在线协作盛行的时代，动象可能仅表现为行业或角色切换；
  - 若命局中驿马被空亡、破败、交退重重压制，却在现实数据中显示稳定居住与就业，系统应适当下调古籍中对「必动」的强调；
  - 不能因见「禄马贵神」就断为必然高官厚禄，更多时候只是说明在变动中更容易获得制度与贵人支持；
  - 工程上若忽视行运对驿马位的周期性触发，只按命局静态判定变动时机，会导致时间预测偏差。

- 小例（示意）：
  - 某命局驿马落在旺地且与禄位同宫，行运再逢官印旺时，系统可解释为「带着资源和职位进行迁移或轮岗」，宜鼓励把握调任、外派机会；
  - 另一命带库马于少年位、但多被空亡交退交叠，系统则提示「早年虽有变动意向但难以真正落实」，现实建议是不要过度押注少年时期的频繁跳槽，而应利用时间积累技能等待中年旺马期。"""
    normalized_text_zh: str = """"""
    subject: str = "驿马兴衰与禄马贵神"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_state_factor_108', 'bazi_semantic', 'bazi_state_factor_109', 'bazi_semantic', 'bazi_state_factor_110', 'bazi_semantic', 'bazi_relation_factor_50', 'bazi_semantic', 'bazi_condition_factor_30', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_驿马兴衰与禄马贵神_001_L1",
    )
    version: str = "1.0.0"
