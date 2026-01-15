"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578658
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
    semantic_id="qtbj_v1.0.0_1__三夏癸水_巳午未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三夏癸水巳午未月(SemanticEntry):
    """
    - **原文（source_text）**：
  **四月癸水**，喜辛金为用，无辛用庚。若辛高透，不见丁火，加以壬透，主科名荣贵，声播四夷。若有丁破格，贫无立锥，有壬可免。辛藏无丁，贡监衣衿。
  ...
    """
    
    original_text: str = """- **原文（source_text）**：
  **四月癸水**，喜辛金为用，无辛用庚。若辛高透，不见丁火，加以壬透，主科名荣贵，声播四夷。若有丁破格，贫无立锥，有壬可免。辛藏无丁，贡监衣衿。
  或一派火土乏辛，即有己庚，亦不能生水。又无比肩羊刃，必至熬干癸水，损目无疑。若庚壬两透，泄制火土，名劫印化晋，极贵之造。
  **五月癸水**，至弱无根，必须庚辛为生身之本。丁火司权，金难敌火，安能滋养癸水，宜见比劫，方得辛金之用。庚辛壬参酌并用可也。
  如庚辛透干，又见壬癸者，定主钟鼎名家。或有金透，支见申子辰者，亦主金榜挂名。故曰：金水会夏天，富贵永无边。
  **六月癸水**，有上下月之分。下半月庚辛有气，上半月庚辛休囚。上半月火气炎烈，宜比劫助身，可云富贵。下半月庚辛有气，即无比劫亦可。

- **分字分词释义**：
  - **辛金为用**：以辛金为用神 / 发源 / 首要用神
  - **科名荣贵**：科举取名荣耀富贵 / 辛壬透 / 极贵
  - **熬干癸水**：把癸水烘干 / 火土太旺 / 凶象
  - **损目**：损伤眼睛 / 水枯火炎 / 病象
  - **劫印化晋**：比劫印星化解 / 庚壬透 / 大贵
  - **至弱无根**：极其虚弱无根气 / 午月癸水 / 身弱
  - **金水会夏天**：金水相会于夏季 / 诗诀 / 吉象
  - **钟鼎名家**：显赫世家 / 庚辛壬癸透 / 极贵

- **规范化释义（primary_lang_explained）**：
  四月（巳月）癸水，喜用辛金为用神，无辛用庚。若辛金高透，不见丁火冲克，加上壬水透出，主科名荣贵。若有丁火破格，贫无立锥，有壬水可免。
  若一派火土而缺辛金，即使有己庚，也不能生水。又无比肩羊刃，必至熬干癸水，损目无疑。若庚壬两透，泄制火土，名"劫印化晋"，极贵之造。
  五月（午月）癸水，至弱无根，必须庚辛为生身之本。丁火司权，金难敌火，宜见比劫，方得辛金之用。庚辛壬参酌并用。如庚辛透干，又见壬癸者，定主钟鼎名家。故曰："金水会夏天，富贵永无边。"
  六月（未月）癸水，有上下月之分。下半月庚辛有气，上半月庚辛休囚。上半月火气炎烈，宜比劫助身；下半月庚辛有气，即无比劫亦可。

- **完整对等诠释（secondary_lang_full）**：
  4th Month Gui Water: Likes Xin Metal for use. If Xin highly reveals without Ding breaking, plus Ren reveals, implies exam fame and glory. If fire/earth excessive without Xin, even with Ji/Geng, cannot generate Water; must dry up Gui Water, eye damage certain. If Geng/Ren both reveal, named "Rob/Seal Transform to Jin", supreme nobility.
  5th Month Gui Water: Extremely weak without root. Must have Geng/Xin for life source. Ding commands; Metal hard to defeat Fire. Need Parallels to use Xin. If Geng/Xin reveal and Ren/Gui seen, certainly a famous house. "Metal Water meet Summer, wealth nobility never ends."
  6th Month Gui Water: Divided into upper/lower half. Lower half Geng/Xin have Qi; upper half Geng/Xin retire. Upper half fire blazing needs Parallels; lower half even without Parallels is okay.

- **核心要点**：
  - **四月**：专用辛金，庚壬配合。忌丁破辛。
  - **五月**：至弱须印（庚辛），比劫助身。金水会夏天为极贵。
  - **六月**：分上下半月，上半需比劫，下半庚辛可用。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_400]` `[trigger: 癸生巳月]` `[factor_trigger: month_si AND tiangan_gui AND tiangan_xin]` `[role: 主干]` 四月癸水，喜辛金为用，无辛用庚。辛高透不见丁，主科名荣贵。 → 《穷通宝鉴·三夏癸水》#38.1
  - `[ns_qttbj_401]` `[trigger: 癸生午月]` `[factor_trigger: month_wu AND tiangan_gui AND tiangan_geng AND tiangan_xin]` `[role: 主干]` 五月癸水，至弱无根，必须庚辛为生身之本。 → 《穷通宝鉴·三夏癸水》#38.1
  - `[ns_qttbj_402]` `[trigger: 金水会夏天]` `[factor_trigger: summer_month AND tiangan_gui AND metal_water_revealed]` `[role: 条件分支]` 金水会夏天，富贵永无边。 → 《穷通宝鉴·三夏癸水》#38.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三夏癸水（巳午未月）"
    factor_refs: list = ['jieyin_huajin', 'jinshui_xiatian']
    
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
        l1_anchor="qtbj_v1.0.0_1__三夏癸水_巳午未月_001_L1",
    )
    version: str = "1.0.0"
