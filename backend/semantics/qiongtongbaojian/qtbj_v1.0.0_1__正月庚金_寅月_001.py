"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578267
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
    semantic_id="qtbj_v1.0.0_1__正月庚金_寅月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1正月庚金寅月(SemanticEntry):
    """
    - **原文（source_text）**：
  正月庚金，木旺之际，有土皆死，不能生金，且金之寒气未除，先用丙暖庚性，又虑土厚埋金，须甲疏泄。丙甲两透，科甲显荣。二者透一，亦有生监。丙藏甲透，异路功...
    """
    
    original_text: str = """- **原文（source_text）**：
  正月庚金，木旺之际，有土皆死，不能生金，且金之寒气未除，先用丙暖庚性，又虑土厚埋金，须甲疏泄。丙甲两透，科甲显荣。二者透一，亦有生监。丙藏甲透，异路功名。
  或柱中土多，甲透者贵；甲藏者富，庚出则否。
  或丁火出干，加以戊己而无水者，又主富贵，名官星有气，才旺生扶，故以富贵推之。
  如火多则用土。用土者，火妻土子。
  或支成火局，壬透、有根者，大富贵。无根者、小富贵。乏水者、残疾之人。
  或木被金伤，无丙丁出制，支无丁火，此系平人。或丙遭癸困，无戊制者亦然。
  总之，正月庚金，丙甲为上，丁火次之。春金多火，不夭则贫。阳金最喜火炼，煅炼太过，反主奔流。

- **分字分词释义**：
  - **正月**：寅月 / 农历一月 / 木气初旺
  - **木旺之际**：木气正旺时 / 甲乙木当令 / 寅月特点
  - **有土皆死**：土处死地 / 木克土 / 印星无力
  - **丙暖庚性**：丙火温暖庚金 / 调候 / 偏财用神
  - **甲疏泄**：甲木疏通土气 / 财星作用 / 防土埋金
  - **科甲显荣**：科举登第 / 功名显达 / 吉象
  - **异路功名**：非正途功名 / 武职或捐官 / 次吉
  - **官星有气**：丁火官星得力 / 官印相生 / 吉格
  - **火局**：巳午戌合火局 / 火旺 / 地支成局
  - **壬透**：壬水透干 / 食神制杀 / 救应
  - **煅炼太过**：火太多熔金 / 身弱杀重 / 凶象
  - **奔流**：漂泊流离 / 无定所 / 凶象

- **规范化释义（primary_lang_explained）**：
  正月（寅月）的庚金，木旺的时候，土都处于死地（木克土），不能生金，而且金的寒气未除（余寒），先用丙火暖庚金的性情，又担心土太厚埋没金（如果有土），必须用甲木疏泄。丙火甲木两透，科甲显耀荣耀。二者透出一个，也有生员监生。丙火藏支甲木透出，异路功名。
  如果柱中土多，甲木透出者贵（疏土养金）；甲木藏支者富，庚金透出（克甲）就不好了（破财/坏印）。
  如果丁火（官）出干，加上戊己土（印）而无水（伤官），又主富贵，这叫“官星有气，财旺生扶”（财生官，官生印），所以推断为富贵。
  如果火多则用土（泄火生身）。用土的人，火为妻土为子。
  如果地支合成火局（杀重），壬水（食神）透出、有根者，大富贵（食神制杀）。无根者，小富贵。缺乏水者，残疾之人（金被火熔）。
  如果木被金伤（比劫争财），无丙丁火出干制约，地支无丁火，这是平人。或者丙火遭到癸水困住（伤官见官），没有戊土制约水，也是这样。
  总之，正月庚金，丙甲为上（财滋弱杀/暖局），丁火次之。春金多火，不夭则贫（身弱杀重）。阳金最喜火炼，但锻炼太过，反主奔流。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 1st Month (Tiger Month): Time of prosperous Wood; all Earth is dead (controlled by Wood) and cannot generate Metal. Also, Metal's coldness remains. First use Bing to warm Geng; fear thick Earth burying Metal, so need Jia to dredge. If Bing and Jia are both revealed, Civil Service is glorious. If one reveals, a Student/Monitor. Bing hidden and Jia revealed implies alternative fame.
  If Earth is abundant in pillars, Jia revealed implies nobility; Jia hidden implies wealth; Geng revealing (clashing Jia) is not good.
  If Ding (Officer) reveals, adding Wu/Ji (Seal) without Water, it implies wealth and nobility, called "Officer Star has Qi, Wealth Prosperous generates Support".
  If Fire is abundant, use Earth. Using Earth takes Fire as Wife, Earth as Child.
  If branches form a Fire Frame, and Ren reveals with root, it implies great wealth/nobility. Without root, small wealth/nobility. Lacking Water implies disability.
  If Wood is damaged by Metal, without Bing/Ding to control, and no Ding in branches, one is an ordinary person. Or if Bing is trapped by Gui without Wu to control, same.
  In summary, for 1st Month Geng, Bing/Jia are superior, Ding is secondary. Spring Metal with much Fire means early death or poverty. Yang Metal likes Fire smelting, but excessive smelting implies wandering.

- **核心要点**：
  - **首要用神**：丙火（暖）、甲木（财/疏土）。
  - **忌讳**：土多埋金（喜甲疏）、火多销金（喜土泄或水制）。
  - **格局**：
    - **财滋弱杀**：丙甲两透。
    - **杀印相生**：丁戊配合。
    - **食神制杀**：火局透壬。

- **详细解说**：
  - 寅月庚金绝地（土金皆绝），气弱。
  - 所谓“阳金喜火炼”，但在绝地不能受强火，故喜丙火（太阳）暖局，胜于丁火（炉冶）锻炼。
  - 除非支成火局，才需壬水制杀，否则不喜水寒。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_321]` `[trigger: 庚生寅月]` `[factor_trigger: month_yin AND tiangan_geng AND tiangan_bing]` `[role: 主干]` 正月庚金，木旺之际，有土皆死，不能生金，且金之寒气未除，先用丙暖庚性。 → 《穷通宝鉴·三春庚金》#30.1
  - `[ns_qttbj_322]` `[trigger: 丙甲两透]` `[factor_trigger: month_yin AND tiangan_geng AND bing_revealed AND jia_revealed]` `[role: 条件分支]` 丙甲两透，科甲显荣。二者透一，亦有生监。 → 《穷通宝鉴·三春庚金》#30.1
  - `[ns_qttbj_323]` `[trigger: 火局透壬]` `[factor_trigger: month_yin AND tiangan_geng AND dizhi_fire_frame AND ren_revealed]` `[role: 条件分支]` 或支成火局，壬透、有根者，大富贵。无根者、小富贵。 → 《穷通宝鉴·三春庚金》#30.1
  - `[ns_qttbj_324]` `[trigger: 火多无水]` `[factor_trigger: month_yin AND tiangan_geng AND fire_excessive AND NOT element_water]` `[role: 例外处理]` 乏水者、残疾之人。 → 《穷通宝鉴·三春庚金》#30.1
  - `[ns_qttbj_325]` `[trigger: 阳金喜火]` `[factor_trigger: tiangan_geng AND likes_fire_smelt AND fire_excessive_wandering]` `[role: 总结]` 阳金最喜火炼，煅炼太过，反主奔流。 → 《穷通宝鉴·三春庚金》#30.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 正月庚金（寅月）"
    factor_refs: list = ['officer_star_qi', 'wandering']
    
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
        l1_anchor="qtbj_v1.0.0_1__正月庚金_寅月_001_L1",
    )
    version: str = "1.0.0"
