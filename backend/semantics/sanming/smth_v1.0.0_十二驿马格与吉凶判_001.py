"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101370
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
    semantic_id="smth_v1.0.0_十二驿马格与吉凶判_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十二驿马格与吉凶判(SemanticEntry):
    """
    - **原文（source_text）**：
  又马有十二：一曰款段，谓巳酉丑人得壬亥，亥卯未人得丙巳，申子辰人得甲寅，寅午戌人得戊申。二曰蹶蹄，谓四柱虽带驿马而生日值空亡之神。三曰折足，谓胎月带驿...
    """
    
    original_text: str = """- **原文（source_text）**：
  又马有十二：一曰款段，谓巳酉丑人得壬亥，亥卯未人得丙巳，申子辰人得甲寅，寅午戌人得戊申。二曰蹶蹄，谓四柱虽带驿马而生日值空亡之神。三曰折足，谓胎月带驿马而日时带沐浴者是；申子辰全见寅为马，是三人骑一马，谓之折足。若亥卯未全见马，总有官贵，终成下贱；若一辰坐者，少年虽泰，后还穷。四曰无粮，谓生日值马，马食太岁；如甲子人得壬寅日而时更落在空亡者是。五曰不出厅厩，谓胎月带马，不见贵及不见禄堂及入空亡者是。六曰嘶风。七曰趋途，谓驿马虽有禄，在空亡。八曰驮尸，十二驿马惟驮尸最凶，见禄即尸。甲子旬中，巳酉丑生人马在亥，乙丑人丁亥，己巳人乙亥，癸酉人癸亥；乙丑人得亥马，忌寅月日时；己巳人得亥马，忌申月日时；癸酉人得亥马，亦忌寅月日时，有一在此，名曰驮尸。亦如亥卯未是甲午旬中，乙未人辛巳，己亥人己巳，癸卯人丁巳；乙未人得巳马，忌寅月日时；己亥人得巳马，忌申月日时；癸卯人得巳马，亦忌寅月日时，皆驮尸也，余旬准此。九曰食刍，谓驿马克其时，假令驿马属金，生时得木，此类谓之食刍。十曰乘轩，谓胎月生日带禄马；假令甲申人得庚寅、甲寅时及庚寅胎月是。十一曰乘轺，谓有天地得合见太岁，生月日时见贵人驿马；假令丁亥生人四月壬寅日己酉时，月坐马，酉系贵人是。十二曰无辔，谓贵神空亡，禄在绝乡者是。

- **分字分词释义**：
  - **款段 / 蹶蹄 / 折足 / 无粮 / 不出厅厩 / 噘风 / 趋途 / 驮尸 / 食刍 / 乘轩 / 乘轺 / 无辔**：十二种驿马状态名目，用以细分动象的吉凶与可用程度。
  - **驮尸**：尤为凶险，驿马与特定干支、月日时组合时，形成「驮官而亡」之象。

- **规范化释义（primary_lang_explained）**：
  本段详细列出十二种驿马格局，从平平的款段，到动而不利的蹶蹄、折足、无粮、不出厅厩，再到最凶的驮尸，以及相对吉利的食刍、乘轩、乘轺等。尤其指出驮尸格的判定方法：在特定旬中，某些命造见某驿马，加上特定月日时组合，即构成「驮尸」，主得官即亡等极端情形。作者强调，这些名目需要「以意消息」，结合命局整体与行运来判断，不可机械套用。

- **核心要点**：
  - 十二驿马格是对驿马状态的进一步细分，反映一个人「动、任、权、险」的不同组合；尤其驮尸格需要严肃对待。
  - 工程化时，可将十二种状态编码为分类特征，并在训练中学习其与实际人生事件（迁移、升职、事故等）的统计关联。
 
- **详细解说**：
  1) 按原文规则为每一命局识别是否落入十二驿马格中的某一类，并编码为 `horse_pattern` 特征（如 KUANDUAN、JUETI、TUOSHI 等）；
  2) 对于被判定为「驮尸」「折足」「无粮」「不出厅厩」等状态的命局，在模型中分别提高「动中受阻」「动中损耗」与「动而难行」等风险指标，而不是一味标记为「大凶」；
  3) 对「乘轩」「乘轺」等偏吉状态，则在与迁职、晋级、荣誉相关的预测任务中适度加权，同时结合五行与现实变量验证其统计有效性；
  4) 对于判定规则极其复杂或样本极稀有的状态，可先作为解释层标签使用，在数据积累后再逐步引入核心决策层。

- 反例与边界：
  - 不宜把「驮尸」等极端名目直接向用户输出为字面含义，现代语境中应转译为「在权位或变动中存在较高的健康/安全/舆情风险」，并辅以缓和表达；
  - 不能因为古书说「终成下贱」「破祖」等，就在人群级预测中照搬结论，应以现代样本的实证结果校正这些描述；
  - 工程上如果把十二格全部当作硬规则，而不允许数据对其权重进行修正，会导致模型对少数模式过度敏感；
  - 反向误区则是因为规则复杂、实现成本高而彻底放弃这套细分，使驿马只剩「有/无」的粗粒度信息。

- 小例（示意）：
  - 某命局被判定为「款段」，现实职业为公务系统中规整稳定的调任路径，系统可把该模式视为「动而有序」，在解释中说明其取向偏向安全、徐缓的变动；
  - 另一命局落「驮尸」规则且现实从事高危行业（如矿业、军警、极限运动），行运再激发驿马位时，系统在风险管理模块中应明显提高对安全、健康事件的预警权重。"""
    normalized_text_zh: str = """"""
    subject: str = "十二驿马格与吉凶判"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_state_factor_111', 'bazi_semantic', 'bazi_state_factor_112', 'bazi_semantic', 'bazi_state_factor_113', 'bazi_semantic', 'bazi_state_factor_114', 'bazi_semantic', 'bazi_condition_factor_31', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_十二驿马格与吉凶判_001_L1",
    )
    version: str = "1.0.0"
