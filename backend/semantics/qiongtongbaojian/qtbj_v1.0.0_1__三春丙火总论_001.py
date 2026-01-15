"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596657
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
    semantic_id="qtbj_v1.0.0_1__三春丙火总论_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三春丙火总论(SemanticEntry):
    """
    - **原文（source_text）**：
  三春丙火，秉象至威，阳回大地，侮雪欺霜，耑用壬水为扶阳，名曰天和地润，既济功成。
  正月用壬，庚辛为助。二月耑用壬水。三月土重晦光，取甲佐之为妙。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  三春丙火，秉象至威，阳回大地，侮雪欺霜，耑用壬水为扶阳，名曰天和地润，既济功成。
  正月用壬，庚辛为助。二月耑用壬水。三月土重晦光，取甲佐之为妙。
  癸丙春生，不晴不雨之天。丙日春生，时月出癸，云雾迷濛，不显不达，非若壬水辅丙也。

- **分字分词释义**：
  - **秉象至威**：承载意象极为威严 / 春丙特征 / 阳气升
  - **阳回大地**：阳气回转大地 / 春季 / 温暖
  - **侮雪欺霜**：侮慢冰雪欺凌霜寒 / 丙火功能 / 驱寒
  - **扶阳**：扶助阳气 / 壬水功能 / 既济
  - **天和地润**：天地和润 / 丙壬配 / 最贵
  - **云雾迷濛**：云雾迷蒙 / 癸遮丙 / 凶象
  - **不显不达**：不显赫不发达 / 癸丙配 / 平常

- **规范化释义（primary_lang_explained）**：
  春天的丙火，气象极为威严，阳气回转大地，能够侮慢冰雪、欺凌霜寒。专门用壬水来扶持阳气（水火既济/映照太阳），这叫“天和地润”，既济之功告成。
  正月（寅月）用壬水，庚金辛金作为辅助（发水源）。二月（卯月）专用壬水。三月（辰月）土重晦暗丙火的光芒，取甲木（疏土）辅助最为妙。
  癸水配合丙火生于春季，是不晴不雨的天气。丙日生于春天，时干或月干透出癸水，好比云雾迷蒙（癸为云雾），不显赫也不发达，不如壬水（江河/大海）辅佐丙火那样壮丽。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the Three Spring Months possesses majestic imagery; Yang returns to the Earth, defying snow and frost. It exclusively uses Ren Water to support Yang, called "Heaven Harmonious and Earth Moist", achieving the merit of "Completion" (Ji Ji).
  In the 1st Month, use Ren, with Geng/Xin as assistance. In the 2nd Month, exclusively use Ren Water. In the 3rd Month, heavy Earth obscures the light; taking Jia Wood to assist is wondrous.
  Gui and Bing born in Spring create "Weather neither sunny nor rainy". If a Bing Day Master is born in Spring and Gui appears in the Month/Hour stems, it is like misty clouds; one is neither prominent nor distinguished. It is not like Ren Water assisting Bing.

- **核心要点**：
  - **首要用神**：壬水（映照/既济）。
  - **忌讳**：癸水（云雾遮日/不晴不雨）。
  - **辅助**：庚辛（生壬），甲（三月疏土）。

- **详细解说**：
  - 丙火为太阳，最喜壬水（江河湖海）映照，所谓"日照江河，气象万千"。
  - 癸水为雨露云雾，见丙火为"云雾遮日"，令太阳失色，故不贵。
  - 春天阳气回升，丙火渐旺，需要水来既济，否则阳气太过（亢龙有悔）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_223]` `[trigger: 三春丙火]` `[factor_trigger: season_spring AND tiangan_bing AND bing_likes_ren]` `[role: 主干]` 三春丙火，秉象至威，阳回大地，侮雪欺霜，耑用壬水为扶阳，名曰天和地润。 → 《穷通宝鉴·三春丙火》#12.1
  - `[ns_qttbj_224]` `[trigger: 丙忌癸]` `[factor_trigger: season_spring AND tiangan_bing AND tiangan_gui AND bing_fears_gui]` `[role: 例外处理]` 癸丙春生，不晴不雨之天。丙日春生，时月出癸，云雾迷濛，不显不达。 → 《穷通宝鉴·三春丙火》#12.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三春丙火总论"
    factor_refs: list = ['heaven_earth_moist', 'misty_clouds', 'supporting_yang']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__三春丙火总论_001_L1",
    )
    version: str = "1.0.0"
