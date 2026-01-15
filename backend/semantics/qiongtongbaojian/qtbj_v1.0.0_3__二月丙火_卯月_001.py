"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596682
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
    semantic_id="qtbj_v1.0.0_3__二月丙火_卯月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3二月丙火卯月(SemanticEntry):
    """
    - **原文（source_text）**：
  二月丙火，阳气舒升，耑用壬水。壬透天干，不见丁化，加以庚辛己亦透，壬水有根，定主科甲。
  或无壬水，己土姑用，主有才学，虽不成名，必衣食充足。
  ...
    """
    
    original_text: str = """- **原文（source_text）**：
  二月丙火，阳气舒升，耑用壬水。壬透天干，不见丁化，加以庚辛己亦透，壬水有根，定主科甲。
  或无壬水，己土姑用，主有才学，虽不成名，必衣食充足。
  或一派壬水，见一戊制，虽不科甲，亦有恩庇。或无戊透，则有辰戌丑未之戊，但辰宫癸水，贪合成火，不能制土，此平常衣禄。若支下全无一戊，此系奔流之人，加以金多生水，下贱之命。
  或一派戊土，亦用壬水，运喜行木，见土不祥。行火亦不利。
  或丙子日，辛卯时，乃从化格，但不逢时，贪财坏印，难招祖业。若得一二重丁火破辛，壬水得位，亦主富贵，虽不科甲，亦有异途，名传郡邑。合此格，主妻妾多子。
  或月时见二辛卯，日乃丙子，名为争合，年不透丁制辛，此人昏迷酒色，年透丁火反吉。或支成木局，反因奸得财，因酒得名。

- **分字分词释义**：
  - **阳气舒升**：阳气舒展升发 / 卯月特征 / 丙旺
  - **丁化**：丁壬合化 / 丁壬合木 / 破用
  - **奔流之人**：奔波流浪的人 / 无戊 / 凶象
  - **贪财坏印**：贪恋财星而破坏印星 / 辛克卯 / 凶象
  - **争合**：争相合化 / 二辛争丙 / 凶象
  - **昏迷酒色**：沉溺于酒色 / 丙被二辛争 / 凶象
  - **因奸得财**：因奸情得到财富 / 木局 / 特殊

- **规范化释义（primary_lang_explained）**：
  二月（卯月）的丙火，阳气舒展升发，专用壬水（映照/既济）。壬水透出天干，不见丁火合化（丁壬合木），加上庚辛金或己土也透出（己混壬不佳，此处疑指庚辛生壬或己土卑湿晦火但壬水有源），壬水有根（申子辰），定主科甲。
  如果没有壬水，己土（伤官）暂且使用，主有才学，虽然不能成名，必定衣食充足。
  如果一派壬水（杀重），见到一个戊土制约（食神制杀），虽然不中科甲，也有恩荫庇护。如果没有戊土透干，地支有辰戌丑未中的戊土也可以，但是辰宫有癸水，与戊土贪合化火（戊癸化火？此处原文可能有误，或指辰湿土不能制水），不能制水，这是平常衣禄。如果地支全无一点戊土，这是奔波流浪的人，加上金多生水，是下贱的命。
  如果一派戊土（食伤多），也用壬水（调候/反克），大运喜欢行木地（疏土），见到土不吉利。行火运也不利（生土）。
  如果是丙子日辛卯时，这是“从化格”（丙辛化水），但是不逢时（生于卯月木旺），贪财坏印（辛克卯），难招祖业。如果得到一二重丁火破除辛金（不化），让壬水得位（七杀），也主富贵，虽然不中科甲，也有异途功名，名传郡县。符合此格（丁破辛用壬），主妻妾多子。
  如果月柱时柱都是辛卯，日柱是丙子，叫“争合”（二辛争合一丙），年干不透出丁火制辛，这人昏迷酒色。年干透出丁火反而吉利。或者地支合成木局（印局），反而因奸情得财，因酒色得名。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 2nd Month (Rabbit Month): Yang Qi rises comfortably; exclusively use Ren Water. If Ren is revealed and not combined by Ding, and Geng/Xin/Ji are also revealed with Ren rooted, Civil Service is certain.
  If there is no Ren, Ji Earth can be used tentatively; it implies talent and learning, and though not famous, food and clothing will be sufficient.
  If there is a mass of Ren Water, seeing one Wu to control it implies protection and honors even without Civil Service. If Wu is not revealed, Wu in branches (Chen/Xu/Chou/Wei) is acceptable, but Chen contains Gui which might combine (with Wu) into Fire (or Wet Earth failing to control Water), leading to ordinary sustenance. If there is absolutely no Wu in branches, one is a wanderer; adding abundant Metal generating Water makes a lowly life.
  If there is a mass of Wu Earth, still use Ren Water; Luck favors Wood (to control Earth), seeing Earth is inauspicious. Fire Luck is also unfavorable.
  If Bing-Zi Day Xin-Mao Hour, it is a Transformation Pattern (Bing-Xin to Water), but not in season (Mao Month); greedy for Wealth ruining the Seal, hard to inherit ancestry. If one or two Ding Fires break Xin, and Ren gets position, it implies wealth and nobility via alternative paths. This pattern implies many wives and children.
  If Month and Hour are both Xin-Mao and Day is Bing-Zi, it is "Competing to Combine". If Year does not reveal Ding to control Xin, the person is lost in wine and lust. If Ding is revealed, it is auspicious. Or if branches form a Wood frame, one gains wealth through illicit affairs and fame through wine.

- **核心要点**：
  - **首要用神**：壬水。卯月沐浴，喜壬水既济。
  - **从化失败**：卯月不化水，辛卯时为贪财坏印。需丁火救应。
  - **争合**：二辛争丙，酒色昏迷。丁火制辛解围。
  - **杀重制杀**：壬多喜戊。

- **详细解说**：
  - 卯月丙火，阳气已盛。
  - “贪财坏印”：丙以辛为财，卯为印。辛卯一柱，盖头克印。
  - “因奸得财”：指争合状态下，地支成木局（印旺），印为名誉/母亲/依靠，被财（女人/欲望）所坏，但在特定条件下（如木火通明或格局转清）反而因异性或不正当手段获利。

- **分字分词释义**：
  - **阳气舒升**：阳气舒展升发 / 卯月特征 / 丙旺
  - **丁化**：丁壬合化 / 丁壬合木 / 破用
  - **奔流之人**：奔波流浪的人 / 无戊 / 凶象
  - **贪财坏印**：贪恋财星而破坏印星 / 辛克卯 / 凶象
  - **争合**：争相合化 / 二辛争丙 / 凶象
  - **昏迷酒色**：沉溺于酒色 / 丙被二辛争 / 凶象
  - **因奸得财**：因奸情得到财富 / 木局 / 特殊

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_225]` `[trigger: 卯月丙火]` `[factor_trigger: month_mao AND tiangan_bing AND tiangan_ren AND ren_rooted]` `[role: 主干]` 二月丙火，阳气舒升，耑用壬水。壬透天干，不见丁化，加以庚辛己亦透，壬水有根，定主科甲。 → 《穷通宝鉴·三春丙火》#12.3
  - `[ns_qttbj_226]` `[trigger: 丙辛贪合]` `[factor_trigger: month_mao AND tiangan_bing AND tiangan_xin AND bing_xin_greedy_combine]` `[role: 例外处理]` 辛年辛时，名为贪合，酒色之徒。 → 《穷通宝鉴·三春丙火》#12.3
  - `[ns_qttbj_227]` `[trigger: 杀重身轻]` `[factor_trigger: month_mao AND tiangan_bing AND ren_excessive AND NOT tiangan_wu AND killing_heavy_body_weak]` `[role: 例外处理]` 丙少壬多，而无戊制，名杀重身轻，斯人笑里藏刀，寻非痞棍。 → 《穷通宝鉴·三春丙火》#12.3
  - `[ns_qttbj_228]` `[trigger: 争合酒色]` `[factor_trigger: month_mao AND tiangan_bing AND xin_multiple AND NOT tiangan_ding AND competing_combination_lust]` `[role: 例外处理]` 月时见二辛卯，日乃丙子，名为争合，年不透丁制辛，此人昏迷酒色。 → 《穷通宝鉴·三春丙火》#12.3
  - `[ns_qttbj_229]` `[trigger: 因奸得财]` `[factor_trigger: month_mao AND tiangan_bing AND dizhi_wood_frame AND competing_combination_lust]` `[role: 条件分支]` 支成木局，反因奸得财，因酒得名。 → 《穷通宝鉴·三春丙火》#12.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 二月丙火（卯月）"
    factor_refs: list = ['greedy_wealth_ruining_seal', 'lost_in_wine_lust', 'wanderer']
    
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
        l1_anchor="qtbj_v1.0.0_3__二月丙火_卯月_001_L1",
    )
    version: str = "1.0.0"
