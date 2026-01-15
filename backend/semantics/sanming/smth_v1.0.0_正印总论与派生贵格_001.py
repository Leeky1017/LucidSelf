"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101522
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
    semantic_id="smth_v1.0.0_正印总论与派生贵格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 正印总论与派生贵格(SemanticEntry):
    """
    - **原文（source_text）**：
  正印，乃五行之正库：金命见乙丑，木命见癸未，火命见甲戌，水土命见壬辰、丙辰是也。《言谈》云：「生逢正印，必拜玉堂。」《妙选》云：「五行入垣，官居五府。...
    """
    
    original_text: str = """- **原文（source_text）**：
  正印，乃五行之正库：金命见乙丑，木命见癸未，火命见甲戌，水土命见壬辰、丙辰是也。《言谈》云：「生逢正印，必拜玉堂。」《妙选》云：「五行入垣，官居五府。」可见得本家正印为贵，本主同德为上，帝座为中，胎月为下。主人重厚魁梧，功名昭著。本家印又得贵格扶之，更妙。若木得水印，火得木印，多兼他权外财。若身克印，或印克身，废而复兴。若水人得火印，火人带水印，次于本家印，然须本主有旺气方吉；若克破别无福救，或落空亡，只作清闲道僧、无成举人，五行有清气，则绝世高人，有煞则贫贱。有贵人夹印，如丙丁火命以甲戌为正印，却得酉亥夹之，酉亥乃丙丁贵人；壬癸水命以壬辰为正印，却得卯巳夹之，卯巳乃壬癸贵人。有华盖印，如亥卯未得癸未之类。有文章印，如戊寅见癸未，辛巳见甲戌，庚申见乙丑，癸亥见丙辰，乙亥见壬辰等，皆纳音克身而干神复制之象。

- **分字分词释义**：
  - **正印为五行正库**：各命局本行在特定支位上的「根本之印」，主血脉、学养与庇护。
  - **本主同德 / 帝座 / 胎月**：印与日主同性同五行为「同德」，居年坐月之要位称「帝座」「胎月」，层次由高到低。
  - **身克印 / 印克身**：身强过印或印强压身，皆主先抑后扬或历经沉浮。
  - **贵人夹印 / 华盖印 / 文章印**：印旁有贵人、华盖或特定纳音结构时，分别偏重官贵、清高与文章才华。

- **规范化释义（primary_lang_explained）**：
  正印被视为五行之正库，是日主本行最根本的依托之地：金命见乙丑、木命见癸未等，皆属本家正印。命中得本家正印且位置得宜，往往主人厚重、身体魁梧、名誉与事业皆有可靠根基。《言谈》《妙选》等书以「拜玉堂」「官居五府」形容其贵。印落在与日主同德之处为最上等，落帝座次之，胎月再次之。若另得「贵人夹印」，如丙丁以甲戌为印又逢酉亥夹拥，或壬癸以壬辰为印又得卯巳夹之，则印格加重，多主荣达受封；「华盖印」则偏向清高孤峻；「文章印」则多与文章才能、学术气质有关。

  同时，正印亦有喜忌：木人得水印、火人得木印，可以兼得外财与权柄，但须身有旺气方能承载；若身克印或印克身，多主经历沉浮，或一度停滞后复起。印若落空亡、受重克而又无他福救，则多成清闲之士或无实权之读书人；有清气而少煞者，可成绝世高人，有煞而混浊者则多见贫贱。

- **完整对等诠释（secondary_lang_full）**：
  Proper Seal is described as the primary treasury of an element, the root store of lineage, learning and protection for the day stem.
  Receiving one own Proper Seal in a fitting place often produces solid character, visible achievements and a reliable safety net, while mixed or overly dominant Seals can either grant extra authority or smother the self depending on balance.
  Derived patterns such as noble flanked Seal, canopy Seal and literary Seal tilt this core symbolism toward high office, aloof purity or scholarly production but do not change its essence as a source of support.
- **核心要点**：
  - 正印是「本源与庇护」的象征：关乎一个人的根基、学养与安全网，既可以成就，也可能压抑；关键在于身印强弱与用忌关系。
  - 贵人夹印、华盖印、文章印等，提供了正印不同侧面的放大镜：夹印偏向权贵、华盖偏向清高、文章印偏向才学输出。
  - 在工程化分析中，应把正印视为「资源与庇护层」，通过其所在宫位、清浊程度、是否空亡与是否被贵人夹拥等指标，评估命主的安全感来源、学业潜质与官印路径，而不是简单将「有印」视为绝对吉象。
 
- **详细解说**：
  1) 在命盘特征工程中，为每一命局标注本家正印、异类印（如木得水印、火得木印）及其所在宫位，形成 `zheng_yin_type` 与 `zheng_yin_positions`；
   2) 计算身印强弱关系，如以日主旺衰与印星多少、位置而得出 `shen_yin_balance_score`，区分「身能任印」「印过于笼罩」「身强克印」等不同状态；
   3) 综合贵人夹印、华盖印、文章印等附加结构，拆分出「官印路径」「清高隐逸倾向」「学术/文章倾向」等二级特征，并与现实中的职业类型、受教育程度、出版或学术成果等变量做对照；
   4) 在解释层，将正印主要用于说明命主获得庇护与资源的方式（家庭、制度、师长等）以及学养与证书的获得路径，而不是简单等同于「一切顺利」。

 - 反例与边界：
   - 不宜只要见印就判为大吉，印过强而身弱时，往往表现为依赖性强、自我主见不足，甚至「无力担当却责任繁重」；
   - 若印星成群而混杂、又多为忌神，现实中可能是制度束缚、关系网沉重，而非单纯贵气；
   - 工程上若仅用「有印/无印」二值特征，会掩盖身印平衡、清浊差异与夹印、华盖等细节，应通过多个维度综合表达；
   - 反向误区是因看到「清闲道僧」「无成举人」等极端描述，就把所有强印命一概视为无用或脱产，忽略现代社会中「研究、顾问、学术型」等非传统仕途路径。

 - 小例（示意）：
   - 某命局本家正印坐用神位，又得贵人夹印而少煞，现实表现为家学深厚、受良师提携、学业顺利，最终在体制内或大型机构中稳步晋升，系统可用「本源稳固 + 制度性庇护」来解释其稳定上升轨迹；
  - 另一命局印星繁多且为忌神，日主偏弱，现实中常感责任重压、难以自我决策，长期处于「被安排的人生」状态，系统则将其解释为「庇护层过厚而压抑主体」，在建议中强调培养独立决策能力与适度减负。"""
    normalized_text_zh: str = """"""
    subject: str = "正印总论与派生贵格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_zhengyin', 'bazi_semantic', 'bazi_state_relation_1', 'bazi_semantic', 'bazi_structure_marker_6', 'bazi_semantic', 'bazi_function_factor_10', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_正印总论与派生贵格_001_L1",
    )
    version: str = "1.0.0"
