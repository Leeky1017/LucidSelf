"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.524037
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
    semantic_id="zpzq_v1.0.0_相神的定义与作用_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 相神的定义与作用(SemanticEntry):
    """
    - **原文（source_text）**：
  月令既得用神，则别位亦必有相，若君之有相，辅者是也.如官逢财生，则官为用，财为相；财旺生官，则财为用，官为相；煞逢食制，则煞为用，食为相.然此乃一定之...
    """
    
    original_text: str = """- **原文（source_text）**：
  月令既得用神，则别位亦必有相，若君之有相，辅者是也.如官逢财生，则官为用，财为相；财旺生官，则财为用，官为相；煞逢食制，则煞为用，食为相.然此乃一定之法，非通变之妙.要而言之，凡全局之格，赖此一字而成者，均谓之相也.

  伤用神甚于伤身，伤相甚于伤用.如甲用酉官，透丁逢壬，则合伤存官以成格者，全赖壬之相；戊用子财，透甲并己，则合煞存财以成格者，全赖己之相；乙用酉煞，年丁月癸，时上逢戊，则合去癸印以使丁得制煞者，全赖戊之相.

  癸生亥月，透丙为财，财逢月劫，而卯未来会，则化水为木而转劫以生财者，全赖于卯未之相.庚生申月，透癸泄气，不通月令而金气不甚灵，子辰会局，则化金为水而成金水相涵者，全赖于子辰之相.如此之类，皆相神之紧要也.

  相神无破，贵格已成；相神相伤，立败其格.如甲用酉官，透丁逢癸印，制伤以护官矣，而又逢戊，癸合戊而不制丁，癸水之相伤矣；丁用酉财，透癸逢己，食制煞以生财矣，而又透甲，己合甲而不制癸，己土之相伤矣.是皆有情而化无情，有用而成无用之格也.

  凡八字排定，必有一种议论，一种作用，一种弃取，随地换形，难以虚拟，学命者，其可忽诸？

- 原注（原文注解）：
  　　本章在前面“用神成败、格局高低、因成得败因败得成”的基础上，再引入一个关键概念：**相神**.相神之于用神，如同“君之有相”，是辅佐格局成败的关键一字.
  - 首先说明相神的基本定义：
    - 月令既定用神之后，别宫必有相神：
      - 官逢财生：官为用，财为相；
      - 财旺生官：财为用，官为相；
      - 煞逢食制：煞为用，食为相；
    - 这些是“固定搭配”的例子，但作者强调，这只是一定之法，并非全部通变之妙.
  - 接着，作者给出一个更宽泛的定义：
    - 凡全局之格，“赖此一字而成者”，皆可称为相；
    - 换言之，相神并不限于财、官、食等类别，而是指任何一个“关键支点之字”。
  - 中段通过具体命例说明：
    - 甲用酉官，透丁逢壬，以合伤存官成格，全赖壬水之相；
    - 戊用子财，透甲并己，以合煞存财成格，全赖己土之相；
    - 乙用酉煞，年丁月癸、时上逢戊，以合去癸印而使丁得制煞，全赖戊土之相.
  - 再举癸亥、庚申两例：
    - 癸生亥月，透丙为财，财逢月劫，若卯未会局，化水为木、转劫生财，全赖卯未为相；
    - 庚生申月，透癸泄气不通月令，金气不灵，若子辰会局，化金为水成金水相涵，全赖子辰为相.
  - 最后指出：
    - 相神不破，则贵格已成；
    - 相神受伤，则格局立败：
      - 甲用酉官，丁制伤而癸印护官，若再逢戊土，癸合戊不制丁，是癸水之相被伤；
      - 丁用酉财，癸食制煞生财，若再透甲，己合甲不制癸，是己土之相被伤.
    - 这些都是“有情而化无情，有用而成无用”的典型——格局败在相神.

- 分字分词释义：
  - 相神：辅佐用神、使格局得以成立的关键一字，如宰相辅佐君主.
  - 若君之有相：用政事中的“君—相”比喻“用神—相神”的关系.
  - 赖此一字而成者：整局之贵赖其存在，一去则格局不成.
  - 伤用神甚于伤身：打击用神，比直接损伤日主更严重.
  - 伤相甚于伤用：损伤相神，往往比打击用神更快破坏格局.
  - 合伤存官：以合去伤官，使官星得以保全.
  - 合煞存财：以合去煞神，使财星不受侵害.
  - 合去癸印：通过合化，使印不再牵制制煞之丁火.
  - 转劫以生财：把原本劫财之力转为生财之用.
  - 金水相涵：金水互相涵养、刚柔相济之象.
  - 相神无破 / 相神相伤：相神完好或受伤断裂，对格局影响极大.
  - 有情而化无情：原本生克关系和谐，后因相神受伤而变得矛盾无情.
  - 有用而成无用：原本有用之神因相神受伤而失去发挥空间.

- **规范化释义（primary_lang_explained）**：
  作者提出：在月令用神已经确定的前提下，还必须寻找“相神”——那个“让格局真正成型的一字”.相神就像宰相之于君主，有时甚至比君主更关键：
  - 没有相神，用神虽好，也未必真正能落地；
  - 相神一旦被伤，用神再好，也可能立刻破局.

  书中先以官、财、煞、食的固定组合说明：官逢财生、财旺生官、煞逢食制，都是常见“用—相”关系，但作者随即指出，这只是最基础的一层.真正的相神判断，要看整局中“哪一字不但帮用神办事，而且一去格局就散”.

  接下来列举的几个命例，都是这种“关键一字”的示范：
  - 甲用酉官，本有丁火伤官，若壬水透出与丁合，既去其伤，又存其官，全局贵在“合伤存官”这一步，所以壬为相；
  - 戊用子财，本有煞来冲财，若甲己并透，以甲己合煞而存财，格局贵在“合煞存财”，所以己为相；
  - 乙用酉煞，本有丁火制煞，却又有癸印牵扯丁火，若时支再透戊土合去癸印，使丁得以专制煞，则戊为相神.

  癸亥、庚申两例，则说明相神可以是支上会局之字：
  - 癸亥透丙为财，若无卯未会局，财多受月劫牵扯，一旦卯未成局，便能“化水为木、转劫生财”，卯未即为相；
  - 庚申透癸泄气，若无子辰会局，金气不灵，一旦子辰会成水局化金为水，使成“金水相涵”，子辰即为相.

  最后，作者特别强调“相神无破则贵格已成，相神相伤则立败其格” ：
  - 甲用酉官，丁制伤、癸护官，若再逢戊土，癸合戊而不制丁，癸之相位被伤，则原本“合伤存官”的格局立刻破坏；
  - 丁用酉财，癸食制煞生财，若再透甲，己合甲而不制癸，己土之相被伤，也是从有情转为无情，从有用变成无用.
  这也是本章最核心的一句话：“伤用神甚于伤身，伤相甚于伤用”.

- **完整对等诠释（secondary_lang_full）**：  
 Auxiliary God (xiang shen) is the pivotal supporting spirit that allows the chosen Useful God to function in real life rather than remaining a mere formal label. Once the month command and the Useful God have been fixed, we must still identify that one stem or branch whose presence makes the entire pattern truly workable: when it is present, Wealth, Officer or other beneficial functions can be protected and activated; when it is missing, the same configuration immediately becomes hollow and collapses.
 Seen in this light, injuring the Day Master is serious, injuring the Useful God is even more damaging, and injuring the Auxiliary is the most fatal blow: the whole pattern rests on this single pivot. When the Auxiliary is rooted, linked and well protected, noble status and concrete outcomes can be realised and sustained; when the Auxiliary is clashed, combined away or starved in luck, a chart that once promised nobility quickly loses its force and falls apart.

  - 相神观念，是在“用神—格局—成败”的基础上，进一步寻找那条最脆弱、也最关键的“命脉”：
    - 用神是格局之主体；
    - 相神是成格之命脉；
    - 伤身固然可惜，伤用更重，而伤相则往往是“一击致命”.
  - 真正高阶的断命，不止在于能认出格局，还在于能找到那个“赖此一字而成者”，并以此来评估格局稳定度.
  - 在实际运程中，相神一旦受岁运冲合破害，往往立见高低转折：
    - 相神得护、得用，往往是“格局兑现”的关键年份；
    - 相神受伤，多半伴随原有格局的滑落与反转.

- 核心要点：
  - 三层重要性次序：身 < 用神 < 相神（就格局成败而言）.
  - 寻找相神的步骤：
    1) 先定月令用神与格局大纲；
    2) 再看全局中“哪一字”对成格起决定性作用；
    3) 记下此字在干支中的位置、强弱、受制情况，作为观察成败的关键指标.
  - 相神无破，则贵格易成且能久；相神屡受冲合，则贵格多有反复甚至陨落.

- **详细解说**：
  相神是辅佐用神的关键角色。用神虽为格局之核心，但若孤立无援、或遭忌神克害，则格局难成。相神的作用在于"护用"与"去病"：或以印护官、或以食制煞、或以劫护财。相神得力，则用神愈清、格局愈高；相神缺失或被伤，则用神势孤，格局打折。断命时须同时观察用神与相神的配合情况。

- 应用推演：
  1) 解析命局时，在确定格局后，专门找出“赖此一字而成”的相神；
  2) 检查原局中相神是否有根、有护、有制、有用；
  3) 排岁运时，标记凡是与相神同气、相合、相冲之年份或大运，作为重点观察期；
  4) 在实际建议中，提醒命主：
     - 在相神得助之运宜积极进取；
     - 在相神受伤之运宜谨慎保守，避免做出“伤相”的重大决策.

- 反例与边界：
  - 只看日主强弱与格局名称，而不寻找相神，导致对成败转折年份判断模糊；
  - 误把任何“帮助用神的字”都当作相神，而不分“是否赖此字而成格”；
  - 把相神绝对化，忽略其他结构的影响，以为相神受伤必然全盘皆输.

- 小例（示意）：
  - 一命以官为用，局中“合伤存官”全赖一壬水相神，行运壬年壬运往往是“贵格兑现”之时；而若逢戊运癸被戊合，便需特别警惕官名与事业的动摇；
  - 另一命以财为用，全局赖己土一字合煞存财而成格，己土既是相神，行运土旺而不见破，财格多能稳定；一旦岁运来合去己土，原有财格立受影响.

- 校勘与字词辨析：
  - “伤用神甚于伤身，伤相甚于伤用”一语虽未明写成对仗句式，本精校根据本段意脉，将其整理为一条核心命题，以便理解；
  - 文中例命“甲用酉官”“戊用子财”“乙用酉煞”等，与全书前后呼应，建议与“用神格局高低”一章对照阅读，以明相神与用神之分工.

---

## 十六．论杂气如何取用




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_306]` `[trigger: 相神紧要]` `[factor_trigger: xiangshen_fuyong AND geju_yuqing_yugao]` `[role: 主干]` 相神辅用，格局愈清愈高。 → 《子平真诠》#上卷
  - `[ns_zpzy_307]` `[trigger: 从格之论]` `[factor_trigger: congge_xu_zhencong AND zhen_ze_fugui]` `[role: 主干]` 从格须真从，真则富贵。 → 《子平真诠》#上卷
  - `[ns_zpzy_308]` `[trigger: 忌神来犯]` `[factor_trigger: jishen_laifan=true AND result=zaihuo_nanmian]` `[role: 主干]` 忌神来犯，灾祸难免。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "相神的定义与作用"
    factor_refs: list = ['zaqi', 'simu', 'tougan', 'huizhi', 'zaerbuza', 'engine_id', 'zaqi_quyong', 'bazi_rule_engine', 'tougan_youqing', 'bazi_rule_engine', 'zaqi_cengji', 'bazi_rule_engine', 'zaqi_qingzhuo', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_127', 'zaqi_quyong', 'rel_zpzq_128', 'tougan_youqing', 'rel_zpzq_129', 'zaqi_cengji', 'evi_zpzq_115', 'zaqi_quyong', 'rule_zaqi_quqing', 'evi_zpzq_116', 'tougan_youqing', 'rule_tougan_youqing', 'concept_complexity', 'concept_clarity', 'concept_harmony']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_相神的定义与作用_001_L1",
    )
    version: str = "1.0.0"
