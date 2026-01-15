"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227396
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
    semantic_id="smth_v1.0.0_命禀清浊与人定胜天_001",
    book_id="sanming",
    engine_id="bazi"
)
class 命禀清浊与人定胜天(SemanticEntry):
    """
    - **原文（source_text）**：
  夫命禀于阴阳，有生之初，非人所能移，莫之为而为，非我所能必。于是有生而富、生而贵者，有生而寿、生而夭者，有生而贫、生而贱者，有生而富贵双夫巍巍人上者，...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫命禀于阴阳，有生之初，非人所能移，莫之为而为，非我所能必。于是有生而富、生而贵者，有生而寿、生而夭者，有生而贫、生而贱者，有生而富贵双夫巍巍人上者，有生而贫贱兼、有落落人下者。有生而宜寿而反夭阏，有生而宜夭而反长年之数者，谓由于所积而然与？亦由于所性而然与？谓由于所积，则贫可以致富，贱可以致贵，夭可以致寿，古之所谓人能胜天者也。谓由于所性，以得乎富贵者终于富贵，贫贱者终于贫贱，寿夭者终于寿夭，古之所谓命不可移也。夫谓之积，则不可专以为命；夫谓之性，则不可专以为人。将以付之于所积与？未知命之所禀，富贵寿夭、贫贱何如也？将以付之于所性与？未有富贵寿夭、贫贱可坐待者，而人为似不可缺也。或曰：命禀有生之初，诚哉是言也。何人生天地之中，有五行八字相同，而富贵、贫贱、寿夭之不一，其故何也？答曰：阴阳二气交感之时，受真精妙合之气，凝结为胎，成男成女，得天地父母一时气候，是以禀其清者为智为贤，禀其浊者为愚为不肖。智者贤者，由是或富或贵或寿，必有所得，所谓德足以获福也；愚者不肖者不能自奋，日益昏蔽，则贫贱与夭有不能免，所谓下愚不移是也。其富贵两全者，原禀清轻之气，生逢得令之时，兼以财官亨通，禄马旺相，其运与限，甚吉甚祥，纵有少晦，不系驳杂。其贫贱兼有者，原禀重浊之气，生逢失令之时，刑冲驳杂，无些顺美，虽无祸患侵扰，未免蹇滞不前。又有富而贫，贫而富，贵而贱、贱而贵，寿而天，夭而寿者；又有为贤为智而反贫贱，为愚不肖而反富贵者。天地间之人，万有不齐，此亦四时五行徧正得失向背浅深之气之所致也。故当时元气虽禀轻清，然而生于衰败之时，行休囚之运，富者损失财源，贵者剥官退位，寿者夭阏不禄。其元气虽禀重浊，其人生中和之令，行旺相之运，贫不终贫而为富，贱不终贱而为贵，夭不终夭而为寿。虽然修为在人，人定胜天。命禀中和，性加积善，岂但一身享福已哉，而子子孙孙荣昌利达，理宜然也。命值徧枯，性加积恶，非惟自身值祸已也，而子子孙孙落落人下，得非报与？由前言之，虽系于命，亦在于人之积与不积耳。易曰：积善之家必有余庆，积不善之家，必有余殃，殆此之谓欤！

- **规范化释义（primary_lang_explained）**：
  命是人在有生之初所受的阴阳五行之气，先天已定，人不能在出生前选择自己的命局，所以有富贵贫贱、寿夭贤愚的种种差别。若只从「所积」看，似乎修为足以逆转一切；若只从「所性」看，又似乎一切皆不可移。作者在两者之间取中道：命有定数，但人仍有作为之地。受清轻之气、得令之时、行旺相之运者，容易富贵寿考；受重浊之气、失令之时、行休囚之运者，多见贫贱蹇滞。然行运可变、德行可积，故「人定胜天」不是空话：命禀中和而能积善，则禄及子孙；命值偏枯而又积恶，则祸延后代。

- **完整对等诠释（secondary_lang_full）**：

  This section asks how much of fate is fixed and how much can be changed. At birth each person receives a particular mixture of yin–yang and Five‑Element qi; this original endowment largely sets the range of wealth or poverty, status or obscurity, longevity or early death. If we looked only at later "accumulation"—deeds, effort, merit—it would seem that anyone could completely overturn their lot; if we looked only at inborn "nature", it would seem that nothing could ever change. The author takes a middle position: destiny contains fixed parameters, yet human action still matters. Those who receive pure, light qi, are born in season and travel through supportive cycles of luck more easily attain wealth, rank and long life. Those endowed with heavy, turbid qi, born out of season and pushed through weakening cycles more often meet poverty and blockage. But rhythms of fortune shift, and virtue can be accumulated; "human overcoming heaven" is not empty rhetoric. A balanced chart combined with long‑term goodness can extend blessing to descendants, whereas a skewed chart compounded by wrongdoing can transmit harm to later generations.

- **分字分词释义**：
  - **禀清/禀浊**：所受先天气机之清纯或混浊，决定资质高下。
  - **所积/所性**：后天积累（德行、努力）与先天禀赋（命数），二者互动。
  - **人定胜天**：人的修为可以在命局框架内调整走向，非绝对宿命。
  - **下愚不移**：禀气极浊且不自奋者，难以改变。

- **详细解说**：
  命是人在有生之初所受的阴阳五行之气，先天已定。禀清轻之气者，易成智贤；禀重浊之气者，多为愚不肖。然而「所积」与「所性」并重：命有定数，但人仍有作为之地。行运可变、德行可积，故「人定胜天」不是空话。同一八字，因元气清浊、得令与否、运程迟速不同，而有富贵贫贱、寿夭贤愚之分。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_022]` `[trigger: 清浊定性]` `[factor_trigger: clarity_turbidity=wisdom_or_folly]` `[role: 主干]` 禀其清者为智为贤，禀其浊者为愚为不肖。 → 《三命通会》卷一#命禀清浊条
  - `[ns_smth_023]` `[trigger: 人定胜天]` `[factor_trigger: human_overcoming_heaven=effort_adjusts_fate]` `[role: 主干依赖]` 古之所谓人能胜天者也。 → 《三命通会》卷一#命禀清浊条
  - `[ns_smth_024]` `[trigger: 下愚不移]` `[factor_trigger: clarity_turbidity=unchangeable_low]` `[role: 边界条件]` 所谓下愚不移是也。 → 《三命通会》卷一#命禀清浊条
  - `[ns_smth_025]` `[trigger: 德足获福]` `[factor_trigger: accumulation=virtue_brings_fortune]` `[role: 条件分支]` 所谓德足以获福也。 → 《三命通会》卷一#命禀清浊条
  - `[ns_smth_650]` `[trigger: 财旺官生在位]` `[factor_trigger: caiwang_guansheng]` `[role: 条件分支]` 财旺官生主富贵。 → 《三命通会》卷一
  - `[ns_smth_651]` `[trigger: 财旺生官有无]` `[factor_trigger: caiwang_shengguan_presence]` `[role: 条件分支]` 财旺生官主显贵。 → 《三命通会》卷一
  - `[ns_smth_652]` `[trigger: 财星破印]` `[factor_trigger: caixin_poyin]` `[role: 条件分支]` 财星破印主破学。 → 《三命通会》卷一
  - `[ns_smth_653]` `[trigger: 财星长生]` `[factor_trigger: caixing_changsheng]` `[role: 条件分支]` 财星长生主财源不断。 → 《三命通会》卷一
  - `[ns_smth_654]` `[trigger: 财星建禄]` `[factor_trigger: caixing_jianlu]` `[role: 条件分支]` 财星建禄主富且贵。 → 《三命通会》卷一
  - `[ns_smth_655]` `[trigger: 财星生扶]` `[factor_trigger: caixing_shengfu]` `[role: 条件分支]` 财星生扶主有助。 → 《三命通会》卷一
  - `[ns_smth_656]` `[trigger: 财印交错]` `[factor_trigger: caiyin_jiaocuo]` `[role: 条件分支]` 财印交错主两难。 → 《三命通会》卷一
  - `[ns_smth_657]` `[trigger: 财印调和配置]` `[factor_trigger: caiyin_tiaohe_config]` `[role: 条件分支]` 财印调和配置主平衡。 → 《三命通会》卷一
  - `[ns_smth_658]` `[trigger: 财印相碍]` `[factor_trigger: caiyin_xiangai]` `[role: 条件分支]` 财印相碍主不顺。 → 《三命通会》卷一
  - `[ns_smth_659]` `[trigger: 财印相扶]` `[factor_trigger: caiyin_xiangfu]` `[role: 条件分支]` 财印相扶主两全。 → 《三命通会》卷一
  - `[ns_smth_660]` `[trigger: 财印支持]` `[factor_trigger: caiyin_zhichi]` `[role: 条件分支]` 财印支持主稳定。 → 《三命通会》卷一
  - `[ns_smth_661]` `[trigger: 财运配合]` `[factor_trigger: caiyun_peihe]` `[role: 条件分支]` 财运配合主发财时机。 → 《三命通会》卷一
  - `[ns_smth_662]` `[trigger: 藏库开合]` `[factor_trigger: cangku_kaihe]` `[role: 条件分支]` 藏库开合主财库动静。 → 《三命通会》卷一
  - `[ns_smth_663]` `[trigger: 残疾风险]` `[factor_trigger: canji_fengxian]` `[role: 条件分支]` 残疾风险高主体弱。 → 《三命通会》卷一
  - `[ns_smth_664]` `[trigger: 长生学堂]` `[factor_trigger: changsheng_xuetang]` `[role: 条件分支]` 长生学堂主学业。 → 《三命通会》卷一
  - `[ns_smth_665]` `[trigger: 长生之地]` `[factor_trigger: changsheng_zhidi]` `[role: 条件分支]` 长生之地主生发。 → 《三命通会》卷一
  - `[ns_smth_666]` `[trigger: 超八字干扰]` `[factor_trigger: chaobazi_ganrao]` `[role: 条件分支]` 超八字干扰主额外因素。 → 《三命通会》卷一
  - `[ns_smth_667]` `[trigger: 成败参半]` `[factor_trigger: chengbai_canban]` `[role: 条件分支]` 成败参半主中等。 → 《三命通会》卷一
  - `[ns_smth_668]` `[trigger: 成败反复]` `[factor_trigger: chengbai_fanfu]` `[role: 条件分支]` 成败反复主波折。 → 《三命通会》卷一
  - `[ns_smth_669]` `[trigger: 成气程度]` `[factor_trigger: chengqi_chengdu]` `[role: 条件分支]` 成气程度高主有力。 → 《三命通会》卷一
  - `[ns_smth_670]` `[trigger: 成气评分]` `[factor_trigger: chengqi_score]` `[role: 条件分支]` 成气评分高主强旺。 → 《三命通会》卷一
  - `[ns_smth_671]` `[trigger: 辰戌对冲风险]` `[factor_trigger: chenxu_duichong_risk]` `[role: 条件分支]` 辰戌对冲有风险。 → 《三命通会》卷一
  - `[ns_smth_672]` `[trigger: 持时有利]` `[factor_trigger: chishi_youli]` `[role: 条件分支]` 持时有利主得势。 → 《三命通会》卷一
  - `[ns_smth_673]` `[trigger: 冲禄源]` `[factor_trigger: chong_luyuan]` `[role: 条件分支]` 冲禄源主破禄。 → 《三命通会》卷一
  - `[ns_smth_674]` `[trigger: 冲出合权评分]` `[factor_trigger: chongchu_hequan_score]` `[role: 条件分支]` 冲出合权评分定吉凶。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "命禀清浊与人定胜天"
    factor_refs: list = ['clarity_turbidity', 'endowment', 'accumulation', 'human_overcoming_heaven', 'inferior_folly_unchangeable']
    
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
        l1_anchor="smth_v1.0.0_命禀清浊与人定胜天_001_L1",
    )
    version: str = "1.0.0"
