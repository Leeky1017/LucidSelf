"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578294
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
    semantic_id="qtbj_v1.0.0_3__三月庚金_辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3三月庚金辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  三月庚金，戊土司令，无生金之理，有埋金之忧，故先甲后丁，不用庚噼甲。
  三月之庚，土旺金顽，顽金宜丁，旺土须甲，乏甲不能立业，乏丁焉能成名。二者少一...
    """
    
    original_text: str = """- **原文（source_text）**：
  三月庚金，戊土司令，无生金之理，有埋金之忧，故先甲后丁，不用庚噼甲。
  三月之庚，土旺金顽，顽金宜丁，旺土须甲，乏甲不能立业，乏丁焉能成名。二者少一，富贵不真。
  庚金无火，非夭则贫。身弱才多，富贵不久。
  得丁甲两透，不见比肩，科甲之命，但要好运相催。甲透丁藏，采芹拾芥。甲藏丁透，异路功名。丁甲俱藏，不受庚制，富中取贵，刀笔起家。有甲无丁，平常之辈。有丁无甲，迂儒腐儒。丁甲两无，下贱之流。
  或一甲、无丁、有丙，由行伍而得官职，须不见壬癸为妙。
  或支成土局，无木，贫贱僧道；见乙、奸诈小人。
  或支成火局，癸水透，富贵。有丙丁出干，见壬制之、方吉。无制、残疾之人。

- **分字分词释义**：
  - **三月**：辰月 / 农历三月 / 戊土司令
  - **戊土司令**：戊土当令 / 印绶旺 / 土气厚重
  - **埋金之忧**：土多埋金 / 印多身弱 / 凶象
  - **土旺金顽**：土气旺金变顽钝 / 养地 / 需火炼
  - **立业**：建立事业 / 成就 / 功名基础
  - **成名**：获得名声 / 科举 / 功名
  - **采芹拾芥**：容易中秀才 / 功名易得 / 吉象
  - **迂儒腐儒**：迂腐的读书人 / 有才无用 / 凶象
  - **刀笔起家**：文职起家 / 书吏 / 富贵来源
  - **行伍**：军队 / 武职 / 异路功名
  - **土局**：辰戌丑未合土 / 土旺 / 地支成局

- **规范化释义（primary_lang_explained）**：
  三月（辰月）的庚金，戊土（偏印）司令，没有生金的道理（土太厚），有埋金的忧虑（土重金埋），所以先用甲木（疏土），后用丁火（炼金），不用庚金劈甲（甲木疏土为主，怕庚劫财）。
  三月的庚金，土旺金顽（土生金，金气转实），顽金适宜丁火锻炼，旺土须要甲木疏通。缺乏甲木不能立业，缺乏丁火怎能成名。二者少一个，富贵不真。
  庚金无火，不是夭折就是贫穷（顽钝无用）。身弱财多（甲多），富贵不久。
  得到丁甲两透，不见比肩（争财），科甲之命，但要好运相催。甲木透出丁火藏支，采芹拾芥（容易中秀才）。甲木藏支丁火透出，异路功名。丁甲都藏支，不受庚金制约，富中取贵，刀笔（文职）起家。有甲无丁，平常之辈。有丁无甲，迂儒腐儒（有才无用，被土埋）。丁甲两无，下贱之流。
  如果一个甲木、无丁火、有丙火，由行伍（军队）而得官职，必须不见壬癸水（克火）为妙。
  如果地支合成土局，无木疏通，贫贱僧道；见乙木（无力疏土），奸诈小人。
  如果地支合成火局（杀重），癸水透出（制杀），富贵。有丙丁出干，见壬水制约，才吉利。无制，残疾之人。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 3rd Month (Dragon Month): Wu Earth commands; logic is not generating Metal but worrying about burying Metal. Thus first Jia, then Ding; do not use Geng to split Jia.
  3rd Month Geng: Earth is prosperous, Metal is stubborn. Stubborn Metal fits Ding; Prosperous Earth needs Jia. Lacking Jia, one cannot establish a career; lacking Ding, how to gain fame? Missing one, wealth/nobility is not true.
  Geng Metal without Fire is either dead or poor. Weak Body with Abundant Wealth implies fleeting wealth.
  Obtaining Ding/Jia both revealed, seeing no Parallels, is a Civil Service destiny, but needs good Luck. Jia revealed Ding hidden, easily a Xiucai. Jia hidden Ding revealed, alternative fame. Ding/Jia both hidden, uncontrolled by Geng, implies nobility amidst wealth, rising via pen/knife. With Jia no Ding, ordinary. With Ding no Jia, a pedantic/rotten scholar. Without Ding/Jia, lowly.
  If one Jia, no Ding, but Bing, implies office via military, best without Ren/Gui.
  If branches form an Earth Frame without Wood, poor/monk; seeing Yi implies treacherous person.
  If branches form a Fire Frame, and Gui reveals, wealth/nobility. With Bing/Ding revealed, seeing Ren to control is auspicious. Without control, disabled.

- **核心要点**：
  - **首要用神**：甲木（疏土）、丁火（炼金）。
  - **忌讳**：土重埋金（无甲）、火多销金（无水）。
  - **不用庚劈**：辰月甲木疏土为重，怕庚金克甲。

- **详细解说**：
  - 辰月庚金养地，土气重。
  - 关键在于"顽"。土厚金顽，必须用甲疏土，丁炼金，方成器皿。
  - "迂儒腐儒"：有丁无甲，丁火生土，土更厚，金更埋，虽有学问（丁）但无用武之地（甲）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_330]` `[trigger: 庚生辰月]` `[factor_trigger: month_chen AND tiangan_geng AND tiangan_jia AND tiangan_ding]` `[role: 主干]` 三月庚金，戊土司令，无生金之理，有埋金之忧，故先甲后丁。 → 《穷通宝鉴·三春庚金》#30.3
  - `[ns_qttbj_331]` `[trigger: 顽金宜丁]` `[factor_trigger: month_chen AND tiangan_geng AND stubborn_metal AND likes_jia_ding]` `[role: 主干依赖]` 三月之庚，土旺金顽，顽金宜丁，旺土须甲，乏甲不能立业，乏丁焉能成名。 → 《穷通宝鉴·三春庚金》#30.3
  - `[ns_qttbj_332]` `[trigger: 丁甲两透]` `[factor_trigger: month_chen AND tiangan_geng AND jia_revealed AND ding_revealed AND NOT shishen_parallel]` `[role: 条件分支]` 得丁甲两透，不见比肩，科甲之命。 → 《穷通宝鉴·三春庚金》#30.3
  - `[ns_qttbj_333]` `[trigger: 有丁无甲]` `[factor_trigger: month_chen AND tiangan_geng AND tiangan_ding AND NOT tiangan_jia]` `[role: 例外处理]` 有丁无甲，迂儒腐儒。丁甲两无，下贱之流。 → 《穷通宝鉴·三春庚金》#30.3
  - `[ns_qttbj_334]` `[trigger: 土局无木]` `[factor_trigger: month_chen AND tiangan_geng AND dizhi_earth_frame AND NOT element_wood]` `[role: 例外处理]` 或支成土局，无木，贫贱僧道。 → 《穷通宝鉴·三春庚金》#30.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 三月庚金（辰月）"
    factor_refs: list = ['pedantic_scholar', 'stubborn_metal']
    
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
        l1_anchor="qtbj_v1.0.0_3__三月庚金_辰月_001_L1",
    )
    version: str = "1.0.0"
