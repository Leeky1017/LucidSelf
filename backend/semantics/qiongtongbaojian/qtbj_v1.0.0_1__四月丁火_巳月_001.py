"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596875
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
    semantic_id="qtbj_v1.0.0_1__四月丁火_巳月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1四月丁火巳月(SemanticEntry):
    """
    - **原文（source_text）**：
  四月丁火乘旺，虽取甲引丁，必用庚噼甲。伐甲、方云木火通明。甲多、又取庚为先。但四柱忌见癸水。癸水一见，泄金、湿甲、伤丁，故以癸为病。或癸水藏支，壬水出...
    """
    
    original_text: str = """- **原文（source_text）**：
  四月丁火乘旺，虽取甲引丁，必用庚噼甲。伐甲、方云木火通明。甲多、又取庚为先。但四柱忌见癸水。癸水一见，泄金、湿甲、伤丁，故以癸为病。或癸水藏支，壬水出干制丙，不夺丁光，自是雁塔题名，玉堂清贵。
  或有庚无甲，戊透天干，此为伤官生才，又取戊为用，必主富贵。戊土出干，不见甲乙，又不见水，是伤官伤尽。子平批八字清高，但不大贵，亦不大富。见水多木多，定是常人。
  或四柱多丙，不见壬癸，夺了丁光，此人贫苦。
  或丁年、巳月、丁巳日、丙午时，一丙不夺二丁，即不显达，亦名播四邻。
  故书曰：丁火阴柔一烛灯，太阳相见夺光明；柱中若见甲木透，定许身安福自临。

- **分字分词释义**：
  - **丁火乘旺**：丁火乘坐旺位 / 巳月 / 帝旺
  - **木火通明**：木生火旺光明通透 / 庚劈甲引丁 / 大贵
  - **雁塔题名**：在雁塔上题写名字 / 进士及第 / 大贵
  - **玉堂清贵**：玉堂殿中的清贵之士 / 翰林 / 极贵
  - **伤官生才**：伤官生财 / 戊生庚 / 富
  - **伤官伤尽**：伤官格完全 / 戊透无印杀 / 清高
  - **丙夺丁光**：丙火夺去丁火光芒 / 劫财 / 凶象
  - **一烛灯**：一盏蜡烛灯 / 丁火象义 / 柔弱

- **规范化释义（primary_lang_explained）**：
  四月（巳月）的丁火乘旺（帝旺），虽然取甲木引丁（正印），但必须用庚金劈甲。砍伐甲木，才叫“木火通明”。如果甲木多，也要取庚金为先。但四柱忌讳见到癸水（七杀）。癸水一见，泄了庚金之气，弄湿了甲木，伤害了丁火，所以以癸水为病。如果癸水藏在支中，壬水出干制住丙火（劫财），不夺丁火的光辉，自然是雁塔题名（考中进士），玉堂清贵。
  如果有庚金无甲木，戊土透出天干，这是“伤官生财”，又取戊土为用神，必主富贵。戊土出干，不见甲乙木（印），又不见水（官杀），是“伤官伤尽”。根据子平批八字，这种格局清高，但不大贵，也不大富（丁火伤官伤尽不如金水/木火格局大？此处存疑，通常伤尽为贵，可能指夏火燥土无水则偏枯）。如果见到水多木多，定是常人。
  如果四柱多丙火，不见壬癸水（制劫），夺了丁火的光辉，这人贫苦。
  如果是丁年、巳月、丁巳日、丙午时（两丁一丙），一丙不夺二丁（丁火势众），即使不显达，名声也传遍四邻。
  所以古书说：丁火阴柔像一盏烛灯，太阳（丙）相见会夺去它的光明；柱中如果见到甲木透出，定许诺身安福气自然来临。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire in the 4th Month (Snake Month) is prosperous. Although taking Jia to ignite Ding, one must use Geng to split Jia. Only cutting Jia is called "Wood Fire Bright". If Jia is abundant, prioritize Geng. But the four pillars dread seeing Gui Water. Once Gui appears, it leaks Metal, wets Jia, and harms Ding; thus Gui is the disease. If Gui is hidden and Ren reveals to control Bing, not stealing Ding's light, it is "Name on the Wild Goose Pagoda" (Jinshi degree), pure nobility in the Jade Hall.
  If there is Geng without Jia, and Wu reveals, it is "Hurting Officer Generating Wealth"; taking Wu as Useful God implies wealth and nobility. If Wu reveals without Jia/Yi and without Water, it is "Hurting Officer Exhausted". Ziping comments this as pure and aloof, but not greatly noble or wealthy. Seeing much Water/Wood makes one ordinary.
  If pillars have much Bing without Ren/Gui, stealing Ding's light, the person is poor.
  If Ding Year, Si Month, Ding Si Day, Bing Wu Hour, one Bing cannot steal the light of two Dings; even if not prominent, fame spreads to neighbors.
  The book says: Ding Fire is Yin and soft like a lamp; meeting the Sun (Bing) steals its light. If Jia Wood is revealed in the pillars, it promises safety and fortune.

- **核心要点**：
  - **劈甲引丁**：巳月丁旺，仍喜庚甲配合（木火通明）。
  - **丙夺丁光**：丁怕丙夺光，喜壬水制丙，或甲木引丁（有甲则不畏丙）。
  - **伤官生财/伤尽**：戊庚配合，或戊土伤尽，富贵或清高。
  - **忌癸**：湿木伤丁，泄金气。

- **详细解说**：
  - “雁塔题名”：指考中进士。壬水在此处的作用是“合杀”或“制劫”，保护丁火不被丙夺。
  - 丁火特性是“旺不烈，衰不穷”，但最怕“丙夺丁光”。解决之道有二：一是天黑（生于夜），二是见甲（有根则不畏），三是见壬（制丙）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_273]` `[trigger: 巳月丁火]` `[factor_trigger: month_si AND tiangan_ding AND tiangan_jia AND tiangan_geng AND wood_fire_bright]` `[role: 主干]` 四月丁火乘旺，虽取甲引丁，必用庚噼甲。伐甲、方云木火通明。 → 《穷通宝鉴·三夏丁火》#17.1
  - `[ns_qttbj_274]` `[trigger: 雁塔题名]` `[factor_trigger: month_si AND tiangan_ding AND tiangan_ren AND gui_hidden AND NOT bing_steals_ding_light AND pagoda_name]` `[role: 条件分支]` 癸水藏支，壬水出干制丙，不夺丁光，自是雁塔题名，玉堂清贵。 → 《穷通宝鉴·三夏丁火》#17.1
  - `[ns_qttbj_275]` `[trigger: 丁火一烛灯]` `[factor_trigger: tiangan_ding AND tiangan_jia AND ding_lamp_metaphor]` `[role: 总结]` 丁火阴柔一烛灯，太阳相见夺光明；柱中若见甲木透，定许身安福自临。 → 《穷通宝鉴·三夏丁火》#17.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 四月丁火（巳月）"
    factor_refs: list = ['pagoda_name', 'bing_steals_light', 'wood_fire_bright']
    
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
        l1_anchor="qtbj_v1.0.0_1__四月丁火_巳月_001_L1",
    )
    version: str = "1.0.0"
