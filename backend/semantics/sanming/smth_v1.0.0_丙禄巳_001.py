"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101283
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
    semantic_id="smth_v1.0.0_丙禄巳_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙禄巳(SemanticEntry):
    """
    - **原文（source_text）**：
  丙禄巳。见己巳，九天库禄，主吉。辛巳，截路空亡。癸巳，伏贵神禄，半吉半凶。乙巳，旺马禄。丁巳，库禄，俱吉。

- **分字分词释义**：
  - **...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙禄巳。见己巳，九天库禄，主吉。辛巳，截路空亡。癸巳，伏贵神禄，半吉半凶。乙巳，旺马禄。丁巳，库禄，俱吉。

- **分字分词释义**：
  - **九天库禄**：禄位兼有库象，资源既多且能积蓄。
  - **伏贵神禄**：贵气潜伏于下，需时机方显。
  - **旺马禄**：禄中带马，主奔忙中发达。

- **规范化释义（primary_lang_explained）**：
  丙火禄在巳。见己巳为「九天库禄」，火土相生，巳为火库，主资源丰厚且能储蓄，多为上等禄象。辛巳带截路空亡，有被阻断、道路中绝之象，偏凶。癸巳为「伏贵神禄」，贵气潜藏，机遇来时方能显达，故吉凶参半。乙巳为「旺马禄」，火木相生，动象甚强，适合在奔走与迁移中求发展。丁巳为单纯库禄，火势充足而有蓄，多主稳健之贵。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire has its Lu in Si. When it meets Ji-Si, Fire and Earth reinforce one another and Si acts as a Fire storehouse, forming the "Nine-Heaven Storage Lu", a superior Lu that shows abundant resources which can also be accumulated.
  Xin-Si, by contrast, is tied to the "Cut-Path Void" pattern: the road is chopped off and development is easily blocked, so it is regarded as inauspicious. Gui-Si produces the "Hidden Noble-Spirit Lu", where noble help lies concealed beneath the surface; when timing opens the configuration the person can suddenly rise, hence the mixture of auspicious and inauspicious tendencies.
  Yi-Si is the "Prosperous-Horse Lu"; Wood and Fire support one another and movement is very strong, so success is sought through travel, mobility and changes of place. Ding-Si gives a pure "Storage Lu", with vigorous Fire that can be stored and used steadily, pointing toward solid, contained forms of success.
- **核心要点**：
  - 丙禄巳的关键在于「火库」与「贵伏」：看其是否能在合适时机开启资源与贵气。
  - 九天库禄偏重长期积累与厚实根基，旺马禄侧重短期冲刺与迁移机会，两者用法不同。
  - 在建模时，可将「库禄」标记为高储蓄能力、「马禄」标记为高流动性，以备后续分析调用。

- **详细解说**：
  1) 判日主为丙火后，检查命局中是否见巳支：区分日坐巳与他柱巳，以标记「根基在身」或「资源在外」；
  2) 根据巳上天干（己、辛、癸、乙、丁）分类为九天库禄、截路空亡、伏贵神禄、旺马禄、库禄，在系统中拆解为「资源量」「可动性」「贵人显隐」三种维度；
  3) 结合季节与整个火局强弱，判断库中之火是「可长期蓄积」还是「易因过旺而泄」，以此影响理财方式、职业节奏等建议；
  4) 在行运推演中，当运支再次触发巳或相关火土局时，将「资源释放/贵气显现/奔波变动」等事件作为重点观察点。

- 反例与边界：
  - 不宜把「库禄」简单理解为钱库，机械断为大富，而不看格局是否允许顺利积累与守成；
  - 不能把「旺马禄」一律视为好动、爱折腾，忽略其在部分命局中承担着「通过迁移打开上升通道」的正向功能；
  - 工程上若未分解「库/马/贵伏」等子象，只以「有巳禄」概括，会导致模型对不同发展路径区分度不足；
  - 反向误区是惧怕「截路空亡」标签，遇之便全面否定，反而忽略局部受阻背后可能带来的结构转向机会。

- 小例（示意）：
  - 某丙日命日坐巳、年见己巳，系统解读为「自带火库 + 九天库禄」，在资产模型中偏向「集中持有、长期深耕」类型，并提示适宜在熟悉领域持续累积而非频繁跳槽；
  - 另一丙日命，命中仅见乙巳旺马禄且行多地迁移之运，系统则提示其「在流动中累积经验与人脉」，更适合项目制、外派型工作，但需设立休整周期防止透支。"""
    normalized_text_zh: str = """"""
    subject: str = "丙禄巳"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_bing_si', 'bazi_semantic', 'bazi_state_marker_6', 'bazi_semantic', 'bazi_state_marker_7', 'bazi_semantic', 'bazi_state_marker_8', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_丙禄巳_001_L1",
    )
    version: str = "1.0.0"
