"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596886
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
    semantic_id="qtbj_v1.0.0_2__五月丁火_午月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2五月丁火午月(SemanticEntry):
    """
    - **原文（source_text）**：
  五月丁火，时归建禄，不宜乱用甲木。
  遇年透隔位之壬，不贪丁合者，忠而且厚。
  或支成火局，干见火出，得庚壬两透者，科甲定然。土透制壬，常人。即壬...
    """
    
    original_text: str = """- **原文（source_text）**：
  五月丁火，时归建禄，不宜乱用甲木。
  遇年透隔位之壬，不贪丁合者，忠而且厚。
  或支成火局，干见火出，得庚壬两透者，科甲定然。土透制壬，常人。即壬藏支中，亦非白丁，但要运行西北，方可发达。得一癸透，名独杀当权，出人头地。
  若见寅辰亥卯字，化木生火，平常人物，丰衣足食，中年富，但刑克子息，劳而无功。
  或丙午月、丁未日、辛亥时，亥中有壬制丙，不致贫苦。若丙午时，则滴水难救炎火，必主僧道。若年支见子，虽不科甲，亦有衣衿。
  若干支无火局，有水透干，须用甲木，又要庚噼甲方明。木火通明，主大富贵。或木少火多，焚其木性，不能光透九霄，荣华不久。
  或生月是禄，支皆生旺合局，加以火出，无滴水解炎，乃身旺无依，孤贫之格。女必为尼。即运北地，反主凶危。

- **分字分词释义**：
  - **时归建禄**：时令归于建禄 / 午月 / 丁火极旺
  - **隔位之壬**：隔开位置的壬水 / 年干壬 / 不合
  - **独杀当权**：独一七杀掌握权力 / 一癸透 / 贵
  - **出人头地**：超出众人之上 / 独杀格 / 大贵
  - **刑克子息**：刑克子女 / 木化火局 / 凶象
  - **身旺无依**：身体太旺无依靠 / 满盘火 / 孤贫
  - **光透九霄**：光芒穿透九重天 / 木火通明 / 大贵
  - **焚其木性**：烧光木的本性 / 火多木少 / 凶象

- **规范化释义（primary_lang_explained）**：
  五月（午月）的丁火，建禄（归禄）在午，火势极旺，不适宜乱用甲木（生火太甚）。
  如果遇到年干透出隔位的壬水（官星），不贪图与日主丁火合化（丁壬合），为人忠厚。
  如果地支合成火局，天干有火透出，得到庚金壬水两透（财官相生/财滋弱杀），定主科甲。如果有土透出制约壬水，常人。即使壬水藏在地支中，也不是白丁，但要大运走西北金水地，才能发达。如果得到一个癸水透出（七杀），叫“独杀当权”，出人头地。
  如果见到寅辰亥卯等字，化木生火（印局），是平常人物，丰衣足食，中年富裕，但刑克子息，劳而无功。
  如果是丙午月、丁未日、辛亥时，亥中有壬水制约丙火，不致于贫苦。如果是丙午时，那么滴水（辛亥之水？）难救炎火，必主僧道。如果年支见到子水（冲午），虽不中科甲，也有秀才。
  如果干支没有火局，有水透干（官杀重），必须用甲木（化杀），又要庚金劈甲（劈甲引丁）才光明。这叫“木火通明”，主大富贵。如果木少火多，烧光了木性，不能光透九霄，荣华不久。
  如果生月是禄（午），地支都是生旺合局（火局），加上火出干，没有一点水来解炎，这是“身旺无依”，孤苦贫穷的格局。女命必为尼姑。即使运走北方水地（激怒旺神），反而主凶险危难。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire in the 5th Month (Horse Month) is at Jianlu (Return to Lu); do not use Jia Wood indiscriminately.
  Meeting Ren separated on the Year stem, not greedy to combine with Ding, implies loyalty and generosity.
  If branches form a Fire Frame and Fire reveals, obtaining both Geng and Ren revealed ensures Civil Service. If Earth reveals to control Ren, ordinary. Even if Ren is hidden, one is not a commoner, but must run Northwest Luck to develop. Obtaining one Gui revealed is "Unique Killing Holding Power", standing out from the crowd.
  If Yin/Chen/Hai/Mao appear, transforming Wood to generate Fire, one is ordinary; well-fed and clothed, rich in middle age, but harming children and toiling without merit.
  If Bing-Wu Month, Ding-Wei Day, Xin-Hai Hour, Ren in Hai controls Bing, preventing poverty. If Bing-Wu Hour, a drop of water cannot save the blazing fire; certainly a monk/Taoist. If Year branch sees Zi, though not Civil Service, one has a degree.
  If no Fire Frame exists, and Water reveals, one must use Jia, and need Geng to split Jia for brightness. "Wood Fire Bright" implies great wealth and nobility. If Wood is scarce and Fire abundant, burning the Wood nature, the light cannot penetrate the Nine Heavens; glory is not lasting.
  If Month is Lu, branches are all prosperous/combined, plus Fire reveals, without a drop of water to relieve the heat, it is "Prosperous Body without Reliance", a lonely and poor pattern. Women must be nuns. Even entering North Luck implies danger.

- **核心要点**：
  - **首要用神**：壬水（官/杀）。建禄喜财官。
  - **独杀当权**：癸水七杀一位，主贵。
  - **炎上/身旺无依**：火局无水，孤贫。
  - **木火通明**：水多用甲庚，大贵。

- **详细解说**：
  - 午月丁火最忌“身旺无依”。火太旺无水济，又无土泄，孤阳不长。
  - 壬水是第一救星。年透壬水，名为“正官”，不合日主（隔位），主忠厚得贵。
  - “运北地反主凶危”：针对的是极旺的火局（炎上变种），若无根之水激怒旺火，必灾。但若有根之水（壬申/癸亥），则为既济。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_276]` `[trigger: 午月丁火]` `[factor_trigger: month_wu AND tiangan_ding AND year_tiangan_ren AND ren_separated_no_combine]` `[role: 主干]` 五月丁火，时归建禄，不宜乱用甲木。遇年透隔位之壬，不贪丁合者，忠而且厚。 → 《穷通宝鉴·三夏丁火》#17.2
  - `[ns_qttbj_277]` `[trigger: 独杀当权]` `[factor_trigger: month_wu AND tiangan_ding AND tiangan_gui_single AND unique_killing]` `[role: 条件分支]` 得一癸透，名独杀当权，出人头地。 → 《穷通宝鉴·三夏丁火》#17.2
  - `[ns_qttbj_278]` `[trigger: 身旺无依]` `[factor_trigger: month_wu AND tiangan_ding AND dizhi_fire_frame AND NOT tiangan_ren AND NOT tiangan_gui AND prosperous_body_no_reliance]` `[role: 例外处理]` 生月是禄，支皆生旺合局，加以火出，无滴水解炎，乃身旺无依，孤贫之格。女必为尼。 → 《穷通宝鉴·三夏丁火》#17.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 五月丁火（午月）"
    factor_refs: list = ['unique_killing', 'body_no_reliance', 'harming_children']
    
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
        l1_anchor="qtbj_v1.0.0_2__五月丁火_午月_001_L1",
    )
    version: str = "1.0.0"
