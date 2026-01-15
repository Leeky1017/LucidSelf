"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778527
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
    semantic_id="zw_v1.0.0_太微赋注解_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 太微赋注解(SemanticEntry):
    """
    #### 3.1 核心原则系列

##### 3.1.1 禄逢冲破，吉处藏凶

- 原文（断句）：

  禄逢冲破，吉处藏凶；假如身命宫逢禄存，或三合有禄，却被忌来冲破，反为凶兆。如限步到于禄位，凶星...
    """
    
    original_text: str = """#### 3.1 核心原则系列

##### 3.1.1 禄逢冲破，吉处藏凶

- 原文（断句）：

  禄逢冲破，吉处藏凶；假如身命宫逢禄存，或三合有禄，却被忌来冲破，反为凶兆。如限步到于禄位，凶星同聚，亦以为凶也。

- 分字分词释义：

  - **禄逢冲破**：禄存被化忌或凶星冲击破坏。
  - **吉处藏凶**：表面吉利的配置中暗藏凶险。
  - **三合有禄**：三方四正有禄存守照。
  - **忌来冲破**：化忌星来冲克破坏。
  - **限步到禄位**：大限小限行到禄存所在宫位。
  - **凶星同聚**：多颗凶星同宫聚集。
  - **马遇空亡**：天马遇到空亡位置。
  - **终身奔走**：一生奔波劳碌，四处奔走。
  - **截路空亡**：根据生年计算的空亡位置。
  - **生逢败地**：命主出生时五行落在败绝之地。
  - **发也虚花**：即使发达也不实在、难以持久。
  - **四生四绝**：寅申巳亥四宫，既是长生之地也是绝地。
  - **庙旺陷弱**：星曜在不同宫位的力量状态。
  - **制化之理**：五行相生相克的制约转化原理。
  - **墓库**：辰戌丑未四宫为墓库之地。

- 规范化释义（primary_lang_explained）：

  禄逢冲破吉处藏凶。假如身命宫逢禄存或三合有禄却被化忌来冲破反为凶兆。如限步到于禄位凶星同聚亦以为凶也。

- 核心要点：
  - 禄存本吉，但被化忌冲破则反凶
  - 吉处藏凶，不可只看表面吉星
  - 限运到禄位遇凶星同聚，亦为凶兆

##### 3.1.2 马遇空亡，终身奔走

- 原文（断句）：

  马遇空亡，终身奔走，假如甲生人，正截路空亡在申，傍空在酉，若安命在申，主人终身奔走，宜僧道。

- 规范化释义（primary_lang_explained）：

  马遇空亡终身奔走。假如甲生人正截路空亡在申傍空在酉，若安命在申主人终身奔走宜僧道。

- 核心要点：
  - 天马遇空亡，主奔波劳碌
  - 终身奔走，宜僧道九流
  - 需根据生年判断空亡位置

##### 3.1.3 生逢败地，发也虚花

- 原文（断句）：

  生逢败地，发也虚花。假如土水人安命在巳为绝地，却得金生在巳，生水不绝，为母来救子之理。凡寅申巳亥为四绝，又为四生。

- 规范化释义（primary_lang_explained）：

  生逢败地发也虚花。假如土水人安命在巳为绝地却得金生在巳生水不绝，为母来救子之理。凡寅申巳亥为四绝又为四生。

- 核心要点：
  - 命坐败绝之地，发财亦为虚花不实
  - 五行相生可解，如金生水救绝地
  - 寅申巳亥为四生四绝

##### 3.1.4 星临庙旺，再观生克；命坐强宫，细察制化

- 原文（断句）：

  星临庙旺，再观生克之机；命坐强宫，细察制化之理。假如水土生人，墓库在辰，若与财帛同度，为财库；与官禄同为官库；与禄存同为天库，耗杀同为空库，迁移同为破库。凡辰、戌丑未为四墓库，此亦属纳音而论。

- 规范化释义（primary_lang_explained）：

  星临庙旺再观生克之机，命坐强宫细察制化之理。假如水土生人墓库在辰，若与财帛同度为财库，与官禄同为官库，与禄存同为天库，耗杀同为空库，迁移同为破库。凡辰戌丑未为四墓库此亦属纳音而论。

- 核心要点：
  - 星入庙旺仍需观察生克关系
  - 四墓库的性质取决于所配星曜
  - 财库、官库、天库、空库、破库之分

---

#### 3.2 日月禄马系列

##### 3.2.1 日月最嫌反背

- 原文（断句）：

  日月最嫌反背，假如日在酉戌亥子丑，月在卯辰巳午未，皆为反背，仍看上弦、下弦。月在上弦遇日吉，下弦晦日凶。若日月同垣，便看人生时日喜太阳月喜太阴方可论祸福。

- 规范化释义（primary_lang_explained）：

  日月最嫌反背。假如日在酉戌亥子丑月在卯辰巳午未皆为反背，仍看上弦下弦。月在上弦遇日吉下弦晦日凶。若日月同垣便看人生时日喜太阳月喜太阴方可论祸福。

- 核心要点：
  - 太阳西没、太阴东升为反背
  - 需分上弦下弦、日生夜生论吉凶
  - 日月同垣需看生时配合

##### 3.2.2 禄马最喜交驰

- 原文（断句）：

  禄马最喜交驰，假如甲禄在寅，而申子辰马亦在寅，遇此得地，谓之禄马交驰。

- 规范化释义（primary_lang_explained）：

  禄马最喜交驰。假如甲禄在寅而申子辰马亦在寅，遇此得地谓之禄马交驰。

- 核心要点：
  - 禄存与天马同宫为禄马交驰
  - 主富贵荣华，财官双美
  - 需看禄马是否得地

##### 3.2.3 空亡定要得用

- 原文（断句）：

  空亡定要得用，天空最为紧要。假如身命宫惟金空则鸣，火空则发，二限逢之，反为福论。若水空则泛，木空则折，土空则陷，为祸矣。

- 规范化释义（primary_lang_explained）：

  空亡定要得用天空最为紧要。假如身命宫惟金空则鸣火空则发二限逢之反为福论。若水空则泛木空则折土空则陷为祸。

- 核心要点：
  - 空亡需看五行配合
  - 金空鸣、火空发为吉
  - 水空泛、木空折、土空陷为凶

---

#### 3.3 格局应用系列

##### 3.3.1 紫微天府，全依辅弼之功

- 原文（断句）：

  紫微天府，全依辅弼之功；假如命遇紫府，又得辅弼守照，终身富贵。

- 规范化释义（primary_lang_explained）：

  紫微天府全依辅弼之功。假如命遇紫府又得辅弼守照终身富贵。

- 核心要点：
  - 紫微天府需辅弼方显威
  - 有相佐则终身富贵
  - 无相助则孤君无力

##### 3.3.2 七杀破军，专依羊铃之虐

- 原文（断句）：

  七杀破军，专依羊铃之虐。假如身、命遇七杀、破军，又会羊、铃守照，有制，反可。

- 规范化释义（primary_lang_explained）：

  七杀破军专依羊铃之虐。假如身命遇七杀破军又会羊铃守照有制反可。

- 核心要点：
  - 凶星需凶星制化
  - 七杀破军得羊铃有制反吉
  - 体现"以毒攻毒"原理

##### 3.3.3 辅弼夹帝为上品，桃花犯主为至淫

- 原文（断句）：

  辅弼夹帝为上品，桃花犯主为至淫。假如身命紫微，与贪狼同垣，男女邪淫奸诈，巧计施机，若得辅弼夹帝，贪狼受制，则不拘此论。

- 规范化释义（primary_lang_explained）：

  辅弼夹帝为上品桃花犯主为至淫。假如身命紫微与贪狼同垣男女邪淫奸诈巧计施机，若得辅弼夹帝贪狼受制则不拘此论。

- 核心要点：
  - 辅弼夹紫微为上品格局
  - 紫微贪狼同宫主淫邪
  - 辅弼可制贪狼之恶

---

- 完整对等诠释（secondary_lang_full）：

  The Taiwei Verse commentary turns the dense, poetic lines of the original Taiwei text into operational rules for judgement. It focuses on how salary and action stars, voids, tomb houses and luminaries actually behave in charts, so that a practitioner can move from abstract praise or blame to concrete evaluation.
  One group of teachings concerns Lucun and Tianma. When the salary star is strong but struck by harsh transformations or heavy malefics, an apparently lucky configuration in fact hides risk, creating situations where wealth is gained at the price of anxiety, lawsuits or later loss. When the horse star repeatedly meets void or destructive stars, life becomes a story of running without anchoring: movement is constant, but results are thin, and such charts are often better suited to wandering or religious paths than to fixed worldly careers. Another group discusses being born in defeated or exhausted ground: when the Life palace or key stars stand in places that inherently cannot sustain them, temporary auspicious aspects create only short-lived blossoms unless there is strong elemental support. Even stars in temple dignity must be checked for how they generate, control or clash with surrounding elements and whether they sit in wealth, official, storage or empty houses.
  The commentary also refines the reading of the Sun and Moon. It explains when they truly shine together, when they lose light by facing away from each other, and how their effects differ for daytime and nighttime births. It shows how salary and horse mutually reinforcing one another in good positions can produce both rank and resources, while the same pairing in weak or stressed positions brings strain. Throughout, the emphasis is on discerning when a configuration is genuinely stable versus merely impressive on the surface, and on recognising that many apparently good patterns contain hidden conditions that must be met before their promise can fully unfold.

- 叙事素材（narrative_snippets）：

  - **禄逢冲破**："禄逢冲破，吉处藏凶"，薪禄星表面吉利，却被化忌或重杀冲击时，往往先富后忧、暗藏风险。
  - **马遇空亡**："马遇空亡，终身奔走"，天马一再与空亡相遇，多见四处奔波、动多静少，更适合游历或出家之路，而非安稳仕途。
  - **生逢败地**："生逢败地，发也虚花"，身命或要星落在败绝之地，即便一时走强，若无强力生扶，终究难以长久。
  - **禄马交驰**："禄马最喜交驰"，禄存与天马得地同宫时，才是真正能同时带来地位与资源的配置，行运顺时尤验。
  - **日月反背**："日月最嫌反背"，太阳西沉、太阴东升背向而行，再好的外在光华也容易难以持续，须细看生时与弦位。
  - **吉象成局条件**：太微注解反复提醒：星在庙旺仍需看生克制化，格局要稳定，必须同时满足位置、五行与限运三重条件。"""
    normalized_text_zh: str = """"""
    subject: str = "太微赋注解"
    factor_refs: list = ['state_lufengchongpo', 'principle_jichucangxiong', 'combo_lumajiaochi', 'position_simuku', 'principle_jinkongzeming', 'combo_fubijiadi', 'principle_yidugongdu', 'source_ref', 'rel_taiwei_001', 'chongpo_guanxi', 'rel_taiwei_002', 'zhihua_guanxi', 'rel_taiwei_003', 'lumajiaochi', 'evi_taiwei_001', 'state_lufengchongpo', 'rule_lufengchongpo', 'evi_taiwei_002', 'star_tianma', 'rule_mayukongwang', 'evi_taiwei_003', 'principle_yidugongdu', 'rule_qishayiling', 'concept_hidden_risk', 'concept_control_principle', 'concept_synergy_pattern']
    
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
        l1_anchor="zw_v1.0.0_太微赋注解_001_L1",
    )
    version: str = "1.0.0"
