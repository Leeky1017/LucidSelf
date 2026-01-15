"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778581
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
    semantic_id="zw_v1.0.0_10__诸星得地富贵论与失陷贫贱论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 10诸星得地富贵论与失陷贫贱论(SemanticEntry):
    """
    - 分字分词释义：

  - **诸星得地**：各星曜落入适宜的宫位，得其地利。
  - **富贵论**：论述富贵格局的条件。
  - **失陷贫贱**：星曜落入不利宫位，主贫贱。
  - **丑未巨...
    """
    
    original_text: str = """- 分字分词释义：

  - **诸星得地**：各星曜落入适宜的宫位，得其地利。
  - **富贵论**：论述富贵格局的条件。
  - **失陷贫贱**：星曜落入不利宫位，主贫贱。
  - **丑未巨机值福**：巨门天机在丑未二宫为值福地。
  - **卯酉羊刃**：卯酉二宫不喜逢擎羊陀罗。
  - **辰戌紫破朝罗网**：紫微破军在辰戌二宫如入罗网。
  - **贪杀巳亥陷地**：贪狼七杀在巳亥二宫为陷地。
  - **破军卯酉不清**：破军在卯酉二宫不清不贵。
  - **六畜之命**：最低等的命格，如牲畜一般劳碌。
  - **旺地发福远大**：星入旺地，福禄远大持久。
  - **陷地峥嵘到底倾**：陷地虽暂时崛起，终究倾覆。

#### 9.1 诸星得地富贵论

- 核心要点：（与第7条十二宫得地合格诀内容重复，为总结性论述）
  - 星入庙旺+三方吉拱=富贵
  - 需看生年配合
  - 重视禄马权科等吉曜

#### 10.1 诸星失陷贫贱论

- 原文（断句）：

  丑未巨机为值福，失陷以月福湏轻。卯酉不喜逢羊刃，辰戌紫破朝罗网。辰休戌囚贪贞陷，午宫阴巨不堪称。申宫贪武为下格酉逢机巨日无精。卯辰巳午逢阴宿，戌亥逢阳亦不荣。贪杀巳亥居陷地，破军卯酉不为清。加杀遇劫为奸盗，此是刑邪不必论。贪狼化禄居四墓，纵然遇吉亦中平。命缠弱地休逢忌，空劫擎羊加火铃。若非夭折主下贱，六畜之命不可评。旺地发福终远大，陷地峥嵘到底倾。

- 规范化释义（primary_lang_explained）：

  丑未巨机为值福失陷以月福湏轻。卯酉不喜逢羊刃辰戌紫破朝罗网。辰休戌囚贪贞陷午宫阴巨不堪称。申宫贪武为下格酉逢机巨日无精。卯辰巳午逢阴宿戌亥逢阳亦不荣。贪杀巳亥居陷地破军卯酉不为清。加杀遇劫为奸盗此是刑邪不必论。贪狼化禄居四墓纵然遇吉亦中平。命缠弱地休逢忌空劫擎羊加火铃。若非夭折主下贱六畜之命不可评。旺地发福终远大陷地峥嵘到底倾。

- 核心要点：
  - 陷地失辉+加杀化忌=贫贱
  - 贪狼化禄四墓宫亦不吉
  - 旺地发福远大，陷地到底倾

- 完整对等诠释（secondary_lang_full）：

  The discourse on stellar strength and loss gathers scattered formulas into a unified view of how stars gain or lose power across the twelve palaces. It distinguishes between temple-prosperity, ordinary strength, weakness and full debilitation, and then shows how additional malefics or auspicious transformations modify, but do not overturn, this basic ranking.
  When stars such as Jumen and Tianji occupy blessing palaces like Chou and Wei yet are themselves in weak or fallen states, the chart carries seeds of loss: what looks like opportunity easily becomes burden. Positions where the Life or Body palace is struck by sharp stars, where benefics are hidden or imprisoned, or where important function stars such as Tanlang, Wuqu or Pojun fall into their least dignified places, repeatedly give results of poverty, criminal entanglement or beast‑like toil, even if transformations to Examination, Authority or Salary appear. Conversely, when the same stars stand in their own temples or in supportive triads, their virtues unfold over long periods as stable resources, rank, reputation and real power.
  The verses therefore stress that star meanings cannot be read in isolation from placement. The same Tanlang that in a dignified position with proper support produces charisma, resourcefulness and material luck, when trapped in tomb palaces or attacked by many malefics, becomes greed, criminality and self‑destruction. The same Ziwei that in an imperial seat brings true command, when confined or opposed in net‑like patterns, produces only nominal dignity with hollow results. Overall, the teaching is summed up in the contrast that prosperity brings broad and lasting fortune, while debilitation leads sooner or later to collapse: intrinsic alignment between star and palace always outweighs momentary favorable aspects.

- 叙事素材（narrative_snippets）：

  - **庙旺如大树扎根**：星曜入庙得垣、三方吉拱时，仿佛大树深扎沃土，风雨虽至，仍能枝叶扶疏。
  - **失陷如屋架在沙**：同一颗星落入败绝、囚地，再被凶煞围困，就像在流沙上搭屋，刚起高楼便已隐伏倾覆之势。
  - **贪狼一念之差**：得地有吉拱则是机敏多才、财路灵活；陷地加杀化忌时，则成贪婪、投机、甚至刑邪之象。
  - **紫微真龙与纸上皇帝**：紫微居帝座且配辅弼魁钺，为真权在手；若被网格困住或落陷地，则只剩虚名而权力空心。
  - **旺地发福终远大，陷地峥嵘到底倾**：一生的高低，不在一时化吉，而在星曜终究是立在高台，还是久居危墙之上。"""
    normalized_text_zh: str = """"""
    subject: str = "10. 诸星得地富贵论与失陷贫贱论"
    factor_refs: list = ['state_miaowangxianruo', 'principle_wangdifafu', 'principle_xiandidaoqing', 'position_simu', 'state_xingxie', 'result_liuchuzhiming', 'source_ref', 'rel_deshi_001', 'xingyao_miaowang', 'rel_deshi_002', 'xingyao_miaowang', 'rel_deshi_003', 'gongxing_shipei', 'evi_deshi_001', 'principle_wangdifafu', 'rule_wangdi_xiandi', 'evi_deshi_002', 'position_simu', 'rule_tanlang_simu', 'concept_dignity_system', 'concept_long_term', 'concept_palace_star']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_10__诸星得地富贵论与失陷贫贱论_001_L1",
    )
    version: str = "1.0.0"
