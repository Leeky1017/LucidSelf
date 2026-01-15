"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578667
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
    semantic_id="qtbj_v1.0.0_1__三秋癸水_申酉戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三秋癸水申酉戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  **七月癸水**，正母旺子相之时，癸虽死申，殊不知申中有庚生之，名死处逢生，弱中复强。必取丁火为用。或丁透有甲，名有焰之火，必主科甲。或丁透无甲，又无...
    """
    
    original_text: str = """- **原文（source_text）**：
  **七月癸水**，正母旺子相之时，癸虽死申，殊不知申中有庚生之，名死处逢生，弱中复强。必取丁火为用。或丁透有甲，名有焰之火，必主科甲。或丁透无甲，又无壬癸，即有一二庚金，亦有生监。
  或一丁坐午，名独才格，主金玉满堂，富中取贵。或柱见二戌二未，又得丙丁藏支，干见甲出、无水，亦作富贵而推。
  **八月癸水**，辛金虚灵，非顽金可比，正金白水清，故取辛金为用，丙火佐之。名水暖金温。如丙与辛隔位同透，主科甲功名。
  **九月癸水**，失令无根，戊土司权，克制太过，专用辛金发水之源，要比肩滋甲制戊方妙。或辛甲两透，支见子癸，定主平步青云。

- **分字分词释义**：
  - **死处逢生**：死绝之处遇生机 / 申中庚生癸 / 吉象
  - **弱中复强**：从弱转强 / 印生身 / 格局变化
  - **有焰之火**：有火焰的火 / 丁透有甲 / 用神有力
  - **独才格**：独立的财星格局 / 丁坐午 / 格局名
  - **金白水清**：金光水净 / 辛金透 / 吉象
  - **水暖金温**：水暖金暖 / 丙辛配合 / 吉象
  - **失令无根**：失时无根气 / 戌月癸水 / 身弱
  - **发水之源**：发起水的源头 / 辛金生水 / 用神

- **规范化释义（primary_lang_explained）**：
  七月（申月）癸水，正是母旺子相之时。癸虽死于申，但申中有庚金生之，名"死处逢生，弱中复强"。必取丁火为用。丁透有甲，名"有焰之火"，必主科甲。
  一丁坐午，名"独才格"，主金玉满堂，富中取贵。
  八月（酉月）癸水，辛金虚灵，非顽金可比，正金白水清。取辛金为用，丙火佐之，名"水暖金温"。丙辛隔位同透，主科甲功名。
  九月（戌月）癸水，失令无根，戊土司权，克制太过。专用辛金发水之源，要比肩滋甲制戊方妙。辛甲两透，支见子癸，定主平步青云。

- **完整对等诠释（secondary_lang_full）**：
  7th Month Gui Water: Mother prosperous child healthy time. Though Gui "dies" in Shen, Geng in Shen generates it, named "Meeting Life at Death Place, Weak becoming Strong". Must use Ding. Ding revealed with Jia, named "Fire with Flame", surely Civil Service.
  8th Month Gui Water: Xin Metal is subtle spirit, not like stubborn Metal. True "Metal White Water Clear". Take Xin for use, Bing assists. Named "Water Warm Metal Warm". Bing/Xin revealing together implies exam fame.
  9th Month Gui Water: Lost command no root. Wu Earth commands, controlling too much. Exclusively use Xin to source Water; Parallels nourishing Jia to control Wu is wondrous.

- **核心要点**：
  - **七月**：死处逢生（庚生癸），用丁火，甲引丁。
  - **八月**：金白水清，辛丙配合，水暖金温。
  - **九月**：辛金发源，甲制戊土，比肩滋助。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_405]` `[trigger: 癸生申月]` `[factor_trigger: month_shen AND tiangan_gui AND tiangan_ding]` `[role: 主干]` 七月癸水，死处逢生，弱中复强，必取丁火为用。 → 《穷通宝鉴·三秋癸水》#39.1
  - `[ns_qttbj_406]` `[trigger: 癸生酉月]` `[factor_trigger: month_you AND tiangan_gui AND tiangan_xin AND tiangan_bing]` `[role: 主干]` 八月癸水，金白水清，取辛金为用，丙火佐之，名水暖金温。 → 《穷通宝鉴·三秋癸水》#39.1
  - `[ns_qttbj_407]` `[trigger: 癸生戌月]` `[factor_trigger: month_xu AND tiangan_gui AND tiangan_xin AND tiangan_jia]` `[role: 主干]` 九月癸水，失令无根，专用辛金发水之源。 → 《穷通宝鉴·三秋癸水》#39.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三秋癸水（申酉戌月）"
    factor_refs: list = ['death_meeting_life', 'metal_white_water_clear', 'water_warm_metal_warm']
    
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
        l1_anchor="qtbj_v1.0.0_1__三秋癸水_申酉戌月_001_L1",
    )
    version: str = "1.0.0"
