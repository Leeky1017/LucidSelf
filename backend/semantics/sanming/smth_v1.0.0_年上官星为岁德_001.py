"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458215
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
    semantic_id="smth_v1.0.0_年上官星为岁德_001",
    book_id="sanming",
    engine_id="bazi"
)
class 年上官星为岁德(SemanticEntry):
    """
    - **原文（source_text）**：
  取年上干支官为岁德，喜忌与月令正官同论。遇此必生宦族，或荫袭祖父之职，若月居财官分野，运向财官旺地，日主健旺，贵无疑矣。凡年干遇官，福气最重，发达必早...
    """
    
    original_text: str = """- **原文（source_text）**：
  取年上干支官为岁德，喜忌与月令正官同论。遇此必生宦族，或荫袭祖父之职，若月居财官分野，运向财官旺地，日主健旺，贵无疑矣。凡年干遇官，福气最重，发达必早。如癸酉、庚申、丙子、丙申，年上官星，柱中会官局，归禄日下，丙克申酉金为财官双美，二丙身旺，十七八运行戊午，虽午冲子，申子会局，冲不能动，日主并旺，及第早发。
  
  古歌云：年中正禄是根芽，必主生身富贵家，运气喜逢身旺地，财生印助福无涯。又：年上官星为岁德，喜逢财印旺身宫，不逢七煞偏官位，富贵荣华莫与京。

- 分字分词释义：
  - **岁德**：以年柱天干或地支上所见官星为"岁德"，主一生命之根芽与家世根基。
  - **宦族**：世代为官之家族，非一代偶然之贵。
  - **荫袭祖父之职**：因祖上功德、爵位而承袭官职，属带荫之贵。
  - **财官分野**：月令与行运所处之方位、五行，与财星官星得地与否有关。
  - **归禄日下**：官星会局而归于日主之禄地，日主得以完全承受其官禄之福。

- **规范化释义（primary_lang_explained）**：
  岁德正官格，是指年柱上出现正官星。因为年柱象征家世、根基和早年环境，故年上见官，多主出身宦族，或承祖父之荫袭而得官。若再配合月令居于财官分野、行运向财官旺地，且日主健旺能胜其官，则几乎可以断为贵命。如癸酉、庚申、丙子、丙申等造，年上官星，命局中又会成官局，官星归禄于日主之下，且丙火身旺，行运在十七八岁便入戊午之地，虽午冲子，然申子会局，冲不破局，反使火土更旺，于是少年即能登第发达。

- **完整对等诠释（secondary_lang_full）**：
  The "Year-Virtue Proper Official" pattern arises when a proper official star stands on the year pillar. The year pillar represents family line, roots and early environment, so an official there often points to being born into an official or privileged clan, or benefiting from ancestral protection and inherited status. When this year-official is backed by a month branch that lies in wealth-and-official territories, by fortune cycles that move into wealth-and-official lands, and by a day-master strong enough to carry what the official implies, the configuration almost inevitably inclines toward nobility and early success. Classical verses sum this up by saying that a proper salary in the year pillar is like the bud and root of a life, giving birth in a wealthy and honourable household, and that when fortune later meets lands where the body is strong, with wealth generating Seal and Seal assisting the self, blessings seem inexhaustible.


- 核心要点：
  - 年上官星为岁德，重在"根芽"：多主家世有官、祖荫深厚，或出身富贵之家。
  - 喜日主健旺、月令财官得地、行运再向财官旺地，则贵无疑，多见少年登科、早立功名。
  - 忌七煞、偏官混杂其间，或日主太弱、不能胜任，则易成"有名无实"之虚贵，甚至受官星所累。

- 详细解说：
  若以正官格比作个人修为与责任匹配之结构，则岁德正官格更强调"出身"与"机会"的部分。年柱在四柱之中位置最先，象征先天环境、祖业与早年际遇，年上见官，往往意味着命主一出生便置身于与权力、制度相近的环境之中，如生于仕宦之家、军政世家等。在这种情况下，只要日主不过分羸弱，月令与行运稍有扶助，即可以较少代价获得官位与名声。
  
  然而，岁德虽好，也需防"官星过重而身不能胜"之弊。若年上官星根深力重，而日主羸弱无依，或又兼七煞、偏官来混，则容易形成"身轻官重"的局面：一方面现实中责任压力过大，另一方面身体与心性难以承受，古书所谓"福气最重"与"发达必早"，也可能转化为过早耗损与坎坷。故判此格时，应一并审视日主强弱、印绶扶身与财星分量，不可因年上见官而一味乐观。

- 校勘与字词辨析：
  - **"年中正禄是根芽"**："根芽"比喻一生命运之根基与初发，年柱为"根"，日柱为"干"，时柱为"花果"，此句强调年上禄、官的重要性。
  - **"莫与京"**："京"指京师，亦泛指天下之极致，此处意为"富贵荣华之盛，难以与之相比"。
  - 本节所举癸酉、庚申、丙子、丙申等例，皆为年上官星、会官局、归禄日下的典型，可视作岁德正官格的代表命局。
  - **English**：
    - Considered representative chart for Year-Virtue Direct-Official pattern.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_017]` `[trigger: 岁德定义]` `[factor_trigger: suide_zhengguan_presence]` `[role: 主干]` 取年上干支官为岁德，遇此必生宦族，或荫袭祖父之职。 → 《三命通会》卷五#岁德正官
  - `[ns_smth_05_018]` `[trigger: 根芽之象]` `[factor_trigger: nian_zhu_guanxing AND zu_yin_support]` `[role: 主干依赖]` 年中正禄是根芽，必主生身富贵家。 → 《三命通会》卷五#岁德正官
  - `[ns_smth_05_019]` `[trigger: 早发条件]` `[factor_trigger: ri_zhu_jianwang AND cai_guan_fenye]` `[role: 条件分支]` 月居财官分野，运向财官旺地，日主健旺，贵无疑矣。 → 《三命通会》卷五#岁德正官
  - `[ns_smth_05_020]` `[trigger: 发达必早]` `[factor_trigger: nian_zhu_guanxing AND fu_qi_chong]` `[role: 总结]` 凡年干遇官，福气最重，发达必早。 → 《三命通会》卷五#岁德正官"""
    normalized_text_zh: str = """"""
    subject: str = "年上官星为岁德"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'suide_zhengguan_presence', 'bazi_semantic', 'nianshang_guanxing_config', 'bazi_semantic', 'genya_genji_score', 'bazi_semantic', 'zaonian_fada_score', 'bazi_semantic', 'zuyin_chengxi_condition', 'bazi_semantic', 'shenqing_guanzhong_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_013', 'suide_zhengguan_presence', 'rel_smth_05_014', 'genya_genji_score', 'rel_smth_05_015', 'shenqing_guanzhong_risk', 'evi_smth_05_013', 'genya_genji_score', 'rule_genya', 'evi_smth_05_014', 'zuyin_chengxi_condition', 'rule_zuyin', 'evi_smth_05_015', 'zaonian_fada_score', 'rule_zaofada', 'map_smth_05_009', 'map_smth_05_010']
    
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
        l1_anchor="smth_v1.0.0_年上官星为岁德_001_L1",
    )
    version: str = "1.0.0"
