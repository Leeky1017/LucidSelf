"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228827
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
    semantic_id="smth_v1.0.0_大林木_枝干撼风与艮土为源_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大林木枝干撼风与艮土为源(SemanticEntry):
    """
    - **原文（source_text）**：
  戊辰、己巳大林木。大林木者，枝干撼风，柯条撑月，耸壑昂霄之德，凌云蔽日之功。此木生居东南，春夏之交，长养成林，全假艮土为源。癸丑为山，三命无破陷，最为...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊辰、己巳大林木。大林木者，枝干撼风，柯条撑月，耸壑昂霄之德，凌云蔽日之功。此木生居东南，春夏之交，长养成林，全假艮土为源。癸丑为山，三命无破陷，最为福厚权贵。戊辰为上，己巳次之，土遇路傍为负载。戊辰见辛未为贵，己巳见庚午为禄，主福。壁屋二土，再得剑金，则大林之木取为栋梁，成格最吉。无此乃山间之茂木也。此木无论死活，皆欲见土。如己人见甲，虽云化土，然不如辰戌丑未土局纯全为妙。若此木已死在山之下，见甲戌、乙亥烧之，主凶夭。灯火就位相生，乙巳不如甲辰更吉。霹雳、太阳二火皆能长育，运中遇之亦吉。然二火𭒡并见持胜，须有士为根基方可。水见天河，戊辰见丁未为带贵，虽无土与山，亦主有衣食，即灵槎入天河格也。生秋冬，死绝，方是溪海。二水重见，主贫夭。有山稍得妙选，有苍龙驾海格是。戊辰见癸亥为贵，涧下丁丑最吉，丙子不如，诸金俱不宜见海中有乙丑为山，剑锋，得屋壁为本，余金无用，逄之，主夭贱。木喜桑柘，惟癸丑最妙。平地还须得路傍土，谓之平林在野。

- **规范化释义（primary_lang_explained）**：
  戊辰、己巳为大林木。大林木枝干撼风、柯条撑月，高耸山壑、蔽日凌云，是成片森林之象。此木居东南，生于春夏交界，全赖艮位厚土为源：癸丑为山，若命局三柱无破陷，则福厚权贵；戊辰为上品根基，己巳次之，路傍土则为负载之地。戊辰见辛未主贵，己巳见庚午主禄，皆有福。壁上土、屋上土再得剑锋金，则大林木可被裁为栋梁之材，成格最吉；若无厚土与金裁成，则只是山间茂林，不入人间大用。此木无论生死皆喜见土，以辰戌丑未等四库土纯全为妙。若已成死木伏于山下，再见甲戌乙亥等烧山之火，则主凶夭。覆灯火就位相生，以甲辰为佳，乙巳次之；霹雳火与太阳火亦能长养大林木，运中遇之主吉，但若二火并见持胜而无厚土，则反成焚林之危。水以天河为上，戊辰见丁未有"带贵"之象，即使暂缺土山仍主有衣食，为"灵槎入天河"之格；秋冬生人则木气死绝，多应溪水、海水之象，若二水重见，主贫夭。有山则稍得妙选，如"苍龙驾海格"；戊辰见癸亥为贵，涧下水以丁丑最吉，丙子次之。诸金总体不宜见大海水，惟海中金有乙丑为山可论；剑锋金得屋上、壁上等土为本可助裁成，余金多无用，反主夭贱。大林木喜见桑柘木，癸丑为山最妙；平地木还须路傍土相辅，形成"平林在野"之象。

- **完整对等诠释（secondary_lang_full）**：
  Wuchen and Jisi belong to Great-Forest Wood. Great-Forest Wood has branches that shake in the wind and limbs that prop up the moon, towering over ravines and rising into the sky, capable of overshadowing the sun—symbolizing expansive forests. Residing in the southeast at the junction of spring and summer, it entirely depends on Gen-direction Earth as its source: Guichou serves as mountain; if three pillars in the chart are free from breakage and collapse, thick fortune and authority follow. Wuchen Earth is best, Jisi next, while Roadside Earth acts as load-bearing terrain. Wuchen meeting Xinwei indicates nobility; Jisi meeting Gengwu grants stipend—both promising blessings. Wall-Top and Roof-Top Earths, when combined with Sword-Edge Metal, allow Great-Forest Wood to be cut and shaped into beams, forming an excellent configuration; without such Earth and Metal, it remains merely lush mountain forest, not harnessed for human use. This Wood, whether alive or dead, desires Earth, especially the complete Chen-Xu-Chou-Wei Earth vaults. If it has already died beneath the mountain and then encounters Jiaxu or Yihai fires burning the mountain, misfortune and early death result. Covered-Lamp Fire at Jiachen position is especially favorable; at Yisi somewhat less so. Thunder-Bolt and Sunlight Fires both can nurture its growth, and encountering them in luck cycles is auspicious—but when both Fires dominate simultaneously, only with substantial Earth roots can the forest avoid being scorched. Water from Heavenly River is preferred; Wuchen meeting Dingwei brings "belted nobility"—even without soil or mountains, this still promises sustenance, forming the "Spirit-Raft Entering the Heavenly River" pattern. Those born in autumn or winter see the Wood qi dead or exhausted and thus align with brook or ocean waters; should two waters recur, poverty and short life are indicated. With mountains some refinement appears, as in the "Azure Dragon Riding the Sea" pattern. Wuchen meeting Guihai is noble; among stream-below waters Dingchou is best and Bingzi inferior. Metals generally should not see Ocean Water; only Sea-Center Metal with Yichou as mountain is somewhat admissible. Sword-Edge Metal, able to carve and trim, combined with Wall-Top Earth and Pine-Cypress support, indicates nobility. Great-Forest Wood with wind and Willow Wood meeting Fire both interact strongly; among Woods, Mulberry-Zelkova is what Pine-Cypress most dislikes. Guichou as mountain can help it. Pomegranate, as Xinyou Metal, reverses into dead wood and may form a "transform-body" pattern—paradoxically favorable. Wonderful-Selection's "Evergreen Pine in Winter" pattern values births in the three winter months; additional patterns involving day-stem meeting Xinmao and month at Gengyin, even with Wuwu or Jiwei present, still prize these two Woods most.

- **核心要点**：
  - 大林木象征成片森林，重在艮土厚根与成材裁用
  - 癸丑、戊辰等厚土为源，配剑锋金与屋壁高土可裁为栋梁
  - 死木再遇烧山之火主夭折，火多而土薄则成焚林之灾
  - 天河水与带贵、灵槎入天河等格局强调"山林入世"之转化

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_110]` `[trigger: 大林木]` `[factor_trigger: wuchen_jisi AND dalin_mu]` `[role: 主干]` 大林木者，枝干撼风，柯条撑月，耸壑昂霄之德，凌云蔽日之功。此木生居东南，春夏之交，长养成林，全假艮土为源。 → 《三命通会》卷一#大林木

- **详细解说**：
  大林木与松柏木同为大木格，但更强调"群体"与"环境"：不是一株担当，而是一片林——有可能被整体纳入人间秩序，也可能永远留在山间。艮土、路傍土与剑锋金构成从"山林"到"梁栋"的技术路径；天河水、霹雳火与太阳火则构成生长与危险的气候环境。实务中看戊辰己巳命局时，需特别分辨：
  - 是"有根有裁"的大林（可为栋梁），还是"无根多火"的焚林之象；
  - 是"灵槎入天河"的出世入世转化，还是"二水重见"的贫夭漂泊。

- **校勘与字词辨析（双语）**：
  - **中文**："耸壑昂霄"形容林木高出山壑直入云霄；"灵槎入天河"源自乘木槎入银河的典故，比喻山林之气入于天界。
  - **English**: "Towering over ravines and rising into the sky" emphasizes great height; "spirit-raft entering the Heavenly River" alludes to a raft ascending into the Milky Way, metaphor for forest qi entering celestial realms."""
    normalized_text_zh: str = """"""
    subject: str = "大林木：枝干撼风与艮土为源"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_大林木_枝干撼风与艮土为源_001_L1",
    )
    version: str = "1.0.0"
