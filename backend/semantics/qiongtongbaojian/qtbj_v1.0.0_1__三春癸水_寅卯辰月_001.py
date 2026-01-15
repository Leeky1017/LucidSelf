"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578649
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
    semantic_id="qtbj_v1.0.0_1__三春癸水_寅卯辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三春癸水寅卯辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  **正月癸水**，值三阳之候，雨露之精，其性至柔，先用辛金，生癸水之源，次用丙火照暖，名阴阳和合，万物发生。辛丙两透，金榜有名。
  或支成火局，辛金...
    """
    
    original_text: str = """- **原文（source_text）**：
  **正月癸水**，值三阳之候，雨露之精，其性至柔，先用辛金，生癸水之源，次用丙火照暖，名阴阳和合，万物发生。辛丙两透，金榜有名。
  或支成火局，辛金受伤，有壬出救者、富贵。无壬者、贫穷。或丙出天干，辛在酉丑，亦有衣衿。若辛丙皆无，贫寒下格。
  或戊透月上、坐辰时，不见比劫，丙丁出干，此为化合，定主腰金。
  **二月癸水**，不刚不柔，乙木司令，泄弱元神，专以庚金为用，辛金次之。庚辛俱透，无丁出干者，贵由科甲。无庚辛者常人。或庚透辛藏，荣封有准。庚藏辛透，亦有衣衿。
  或支成木局，月时又见木者，为泄水太过，定主贫困多灾。即运入西方，亦属无用。
  **三月癸水**，要分清明谷雨。清明后、火气未炽，专用丙火，为阴阳合谐。谷雨后，虽用丙火，尚宜辛甲佐之。
  三月癸水，从化者多，得化者荣禄。不化者平常。或支成水局，又见己土、无木，乃假杀格，有甲出者、常人。或支坐四库，又得甲透，可谓显达名扬。无甲者僧道孤苦。
  三月癸水，辛甲皆酌用。下半月，土妻金子。

- **分字分词释义**：
  - **三阳之候**：立春三阳 / 阳气初升 / 正月时节
  - **雨露之精**：雨露精华 / 癸水本性 / 至柔至阴
  - **阴阳和合**：阴阳相配 / 辛丙配合 / 吉象
  - **金榜有名**：科举高中 / 进士 / 吉象
  - **腰金**：系金腰带 / 高官 / 吉象
  - **泄弱元神**：泄弱精气 / 木泄水 / 凶象
  - **泄水太过**：泄气过重 / 木多水弱 / 凶象
  - **清明谷雨**：节气区分 / 三月分前后 / 用神变化
  - **从化**：从戊化火 / 变格 / 戊癸合化
  - **假杀格**：假从杀格 / 似从非从 / 格局名

- **规范化释义（primary_lang_explained）**：
  **正月（寅月）癸水**：值三阳之候（立春），雨露之精，其性至柔。先用辛金生癸水之源，次用丙火照暖，名"阴阳和合"，万物发生。辛丙两透，金榜有名。或支成火局，辛金受伤，有壬出救者富贵。
  **二月（卯月）癸水**：不刚不柔。乙木司令，泄弱元神，专以庚金为用（制木生水），辛金次之。庚辛俱透，无丁出干者，贵由科甲。或支成木局，为"泄水太过"，定主贫困多灾。
  **三月（辰月）癸水**：要分清明谷雨。清明后火气未炽，专用丙火（暖局）。谷雨后虽用丙火，尚宜辛甲佐之（辛生甲疏）。三月癸水从化者多（从戊土化火），得化者荣禄。不化者平常。或支成水局，又见己土无木，乃"假杀格"。

- **完整对等诠释（secondary_lang_full）**：
  **1st Month (Tiger) Gui Water**: Time of Three Yangs (Spring start), essence of rain/dew, nature very soft. First use Xin Metal (generate source), next Bing Fire (warm). "Yin Yang Harmonious", all things grow. Xin/Bing revealing, exam fame.
  **2nd Month (Rabbit) Gui Water**: Not hard not soft. Yi Wood commands, draining weak spirit. Focus on Geng Metal (use), Xin next. Geng/Xin revealing, no Ding, noble via exams. If Wood Frame, draining Water too much, poverty/disaster.
  **3rd Month (Dragon) Gui Water**: Distinguish Qingming/Guyu terms. After Qingming, Fire not blazing, focus Bing. After Guyu, use Bing, also Xin/Jia assist. Many Transform patterns (combining Wu), if transformed glory. If Water Frame, see Ji Earth no Wood, "Fake Killing Pattern".

- **核心要点**：
  - **正月**：喜辛金发源，丙火调候。
  - **二月**：乙木当令泄气，首重庚金制木生水。
  - **三月**：上半月专用丙，下半月用丙辛甲。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_391]` `[trigger: 癸生寅月]` `[factor_trigger: month_yin AND tiangan_gui AND tiangan_xin AND tiangan_bing]` `[role: 主干]` 正月癸水，值三阳之候，雨露之精，其性至柔，先用辛金，次用丙火照暖，名阴阳和合。 → 《穷通宝鉴·论癸水》#37.1
  - `[ns_qttbj_392]` `[trigger: 癸生卯月]` `[factor_trigger: month_mao AND tiangan_gui AND tiangan_geng]` `[role: 主干]` 二月癸水，不刚不柔，乙木司令，泄弱元神，专以庚金为用。 → 《穷通宝鉴·论癸水》#37.1
  - `[ns_qttbj_393]` `[trigger: 癸生辰月]` `[factor_trigger: month_chen AND tiangan_gui AND tiangan_bing]` `[role: 主干]` 三月癸水，要分清明谷雨。清明后火气未炽，专用丙火。 → 《穷通宝鉴·论癸水》#37.1
  - `[ns_qttbj_394]` `[trigger: 泄水太过]` `[factor_trigger: tiangan_gui AND dizhi_wood_frame AND drain_water_excess]` `[role: 例外处理]` 或支成木局，月时又见木者，为泄水太过，定主贫困多灾。 → 《穷通宝鉴·论癸水》#37.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三春癸水（寅卯辰月）"
    factor_refs: list = ['yinyang_harmony', 'drain_water_excess', 'fake_killing_pattern']
    
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
        l1_anchor="qtbj_v1.0.0_1__三春癸水_寅卯辰月_001_L1",
    )
    version: str = "1.0.0"
