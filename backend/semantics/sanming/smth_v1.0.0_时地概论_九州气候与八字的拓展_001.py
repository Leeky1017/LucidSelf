"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288913
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
    semantic_id="smth_v1.0.0_时地概论_九州气候与八字的拓展_001",
    book_id="sanming",
    engine_id="bazi"
)
class 时地概论九州气候与八字的拓展(SemanticEntry):
    """
    - **分字分词释义**：
  - **二气**：阴阳二气，主宰四时变化的根本动力。
  - **五行 / 五气**：金木水火土五种基本气机，在地上具体落实。
  - **时 / 地**：时为春夏秋冬...
    """
    
    original_text: str = """- **分字分词释义**：
  - **二气**：阴阳二气，主宰四时变化的根本动力。
  - **五行 / 五气**：金木水火土五种基本气机，在地上具体落实。
  - **时 / 地**：时为春夏秋冬与节气，地为九州方隅与地域气候。
  - **方隅**：冀、青、兖、徐、扬、荆、梁、雍、豫等区域性格局，可抽象为「地域因子」。
  - **得时 / 得地**：五行之气在时令与地域上皆相应和适，气机顺畅。
  - **昼夜阴晴 / 寒暖**：同一日中光照、温度与天气的差别，也是具体气机。
  - **生克制化、抑扬轻重**：五行之间相互生克与调节的全过程。

- 规范化释义（primary_lang_explained）：
  原文先引王氏与朱子的说法，将命理中的「二气」「五行」与「时」「地」系统合在一起：天以阴阳行于四时，地以五行具于九州，人便在这一套「时—地—气」体系中出生与生活。因此，只看阴阳五行而不看方隅、节候与昼夜阴晴，就会出现年、月、日、时完全相同而贵贱寿夭迥异的情况，误以为五行无据。作者强调：人生天地之间，无法逃出五行；但九州分疆，风气与寒暖又各不相同，每个人所受之气自然有差异，不能用同一套八字模板把一切人硬套在一起。最后举例说明：木、火、土、金、水各有得地得时之处，若只从八字文字，不顾所处方位与时令，就会误读命局。

- 核心要点：
  - 命理判断不只看「字面八字」，还要看「时空坐标」：出生节令、地域与气候皆入参考。
  - 同一五行在不同地域、不同季节，表现强弱与吉凶会明显不同，需建模为独立特征。
  - 「贵贱寿夭难以八字拘」并非否定八字，而是要求把八字放入更大的气机框架中理解。

- 应用推演（操作顺序）：
  1) 在数据层，将出生日期映射为「节气/季节标签」，并将出生地点映射为「区域气候因子」。
  2) 判盘时先标记五行得时、得地与失时、失地的情况，为后续用神与格局判断提供权重基础。
  3) 在模型中，对同样的八字结构，在不同地域、不同节令环境下，允许输出不同的「预期轨迹」与置信度。
  4) 行运分析时，将运势所指向的时地（如南方火土、北方水寒）与原局的得时得地情况并行考虑。

- 反例与边界：
  - 不宜把地域差异机械化成简单「南=火旺、北=水旺」等单一标签，而忽略真实气候与时代变迁。
  - 不可据此否定八字体系本身，只因看到「同八字不同人生」就草率说命理无用。
  - 工程实现中若完全忽略地域与节气，只用干支字面做推理，等同违背本节核心精神。
  - 反向误区是把「地域/气候因子」看得过重，以至于淹没了命局结构本身的差异。

- 小例（示意）：
  - 某甲木命局在兖、青地区春生，木得时又得地，同一八字在模型中可被标记为「环境顺势」型，更看重个人选择与努力的差异。
  - 另一命局同样为甲木春生，却在严寒地区且长期夜班工作，系统则在能量调节与健康风险上加权，提醒「气机不尽相同，不宜与前者简单类比」。"""
    normalized_text_zh: str = """"""
    subject: str = "时地概论：九州气候与八字的拓展"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'time_place_dual_territory', 'bazi_semantic', 'season_quarter_label', 'bazi_semantic', 'region_nine_territories', 'bazi_semantic', 'diurnal_weather_profile', 'bazi_semantic', 'gain_time_gain_place', 'bazi_semantic', 'source_ref', 'rel_smth_04_052', 'time_place_dual_territory', 'rel_smth_04_053', 'region_nine_territories', 'rel_smth_04_054', 'diurnal_weather_profile', 'evi_smth_04_052', 'time_place_dual_territory', 'rule_time_place', 'evi_smth_04_053', 'region_nine_territories', 'rule_region', 'evi_smth_04_054', 'diurnal_weather_profile', 'rule_diurnal', 'map_smth_04_035', 'map_smth_04_036']
    
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
        l1_anchor="smth_v1.0.0_时地概论_九州气候与八字的拓展_001_L1",
    )
    version: str = "1.0.0"
