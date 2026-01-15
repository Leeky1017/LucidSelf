"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523947
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
    semantic_id="zpzq_v1.0.0_何谓败_成中有败_败中有成_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 何谓败成中有败败中有成(SemanticEntry):
    """
    - **原文（source_text）**：
  何谓败？官逢伤克刑冲，官格败也；财轻比重，财透七煞，财格败也；印轻逢财，或身强印重而透煞，印格败也；食神逢枭，或生财露煞，食神格败也；七煞逢财无制，七...
    """
    
    original_text: str = """- **原文（source_text）**：
  何谓败？官逢伤克刑冲，官格败也；财轻比重，财透七煞，财格败也；印轻逢财，或身强印重而透煞，印格败也；食神逢枭，或生财露煞，食神格败也；七煞逢财无制，七煞格败也；伤官非金水而见官，或生财生带煞，或佩印而伤轻身旺，伤官格败也；阳刃无官煞，刃格败也；建禄月劫，无财官，透煞印，建禄月劫之格败也。成中有败，必是带忌；败中有成，全凭救应。何谓带忌？如正官逢财而又逢伤；透官而又逢合；财旺生官而又逢伤逢合；印透食以泄气，而又遇财露；透煞以生印，而又透财，以去印存煞；食神带煞印而又逢财；七煞逢食制而又逢印；伤官生财而财又逢合；佩印而印又遭伤，透财而逢煞，是皆谓之带忌也。

- 原注（原文注解）：
  　　本段指出：
  - 各类格局的“败象”，多半源于用神受克、被合、被夺；
  - “带忌”是成格中潜藏败象的标志；
  - 败局中亦可有可救之处，要看“救应”是否到位。

- 分字分词释义：
  - 官逢伤克刑冲：官星受伤官克制或受刑冲破坏。
  - 财轻比重：财弱比劫多。
  - 印轻逢财：印弱而财旺，印被财泄。
  - 食神逢枭：食神被偏印克制。
  - 七煞逢财无制：煞星既旺又有财生，而无制伏。
  - 伤官非金水而见官：非金水伤官格，却露官星，形成“伤官见官”。
  - 阳刃无官煞：刃旺而缺乏官煞制衡。
  - 带忌：在成格结构中，夹杂了忌神破坏路线。

- **规范化释义（primary_lang_explained）**：
  本段先列出各种“败格”的典型情况：
  - 官格若遇伤官克制、刑冲破害，官格自然破败；
  - 财格若财轻比重、或又逢七煞无制，财格难成；
  - 印格若印轻逢财，或身强印重而另透煞星，则印格有失；
  - 食神格若逢枭神夺食，或食生财而又露煞，则食神之秀难保；
  - 七煞格若遇财生煞而无制，则从凶不从贵；
  - 伤官格若非金水伤官而又见官，或生财又带煞，或佩印而伤浅身旺，皆为败象；
  - 阳刃格无官煞制伏，则刃失其用；
  - 建禄月劫格无财官、反透煞印，亦为败格。

  接着作者指出:"成中有败，必是带忌；败中有成，全凭救应。"所谓"带忌"，就是在成格的结构中夹杂忌神：正官逢财又逢伤、官星透出又被合、财旺生官而又逢伤与合、印透食又遇财露、煞生印又透财去印存煞、食神带煞印又逢财、七煞逢食制又逢印、伤官生财而财又被合、佩印而印又遭伤、透财而逢煞，这些都是"带忌"的情况。成格中一旦带忌，就为后文败象埋下伏笔；反之，败中若有救应，仍可能起转机。

- **完整对等诠释（secondary_lang_full）**：  
  This passage explains in concrete terms what it means for a pattern to "fail". An Officer pattern fails when the Officer star is attacked by Hurting Officer or broken by punishments and clashes, so that upright authority cannot stand. A Wealth pattern fails when Wealth is light while Rob Wealth is heavy, or when exposed Wealth is tied directly to strong Seven Killings and ends up feeding danger instead of support. A Resource pattern fails when weak Resource is drained by strong Wealth, or when the Day Master is already strong and heavy Resource is further pierced by exposed Killings, turning protection into pressure. A Food-God pattern fails when Food is seized by the Owl (the devouring form of Resource), or when Food generates Wealth while at the same time exposing Killings, so that what should have expressed talent instead invites harm. A Seven-Killings pattern fails when Killings are further strengthened by Wealth and left without any control, becoming pure malefic force. A Hurting-Officer pattern fails when it is not the proper Metal–Water structure yet still meets Officer, when it both generates Wealth and simultaneously carries Killings, or when it is accompanied by seals but the Hurting Officer itself is shallow while the body is too strong; in these cases, its sharpness turns reckless. A Yang-Blade pattern fails when the Blade is strong but there is no Officer or Killing to restrain it. A Establishment-and-Robbing (Jianlu–Yuejie) pattern fails when there is no Wealth or Officer but only exposed Killings and Resource, so that rivalry and pressure dominate.

  On this basis, the author adds the idea that "within success there is failure, within failure there is success". "Success that already carries failure" always involves hidden malefic threads inside an apparently completed pattern: a proper Officer that is simultaneously pulled by Wealth and attacked by Hurting Officer; Officer that is exposed and then bound away by combinations; Wealth that vigorously feeds Officer while at the same time being injured by Hurting Officer or stolen by combinations; Resource that appears to support the body but is secretly leaked by Food and then further drained by exposed Wealth; Killings that were meant to give birth to Resource but are left behind when Wealth removes the seal and leaves the Killing naked; Food-God that is tied up with Killing and Resource and then further enticed by Wealth; Seven Killings that are already checked by Food but then are reinforced again by Resource; Hurting Officer that generates Wealth, only for that Wealth to be combined away; seals that are supposed to protect the body but are themselves injured, or Wealth that is exposed only to be attacked by Killings. All of these are examples of "carrying malefics". Once such threads are woven into a seemingly successful pattern, they lay the groundwork for future failure. Conversely, in a chart that appears to be broken, if there is timely "rescue and response" – through seals, combinations, meetings, control or transformation arriving in the right place and time – genuine turning points can still arise, and failure can be steered back toward usable order.

- 详细解说：
  - 用神成败，不在某一颗星是否出现，而在整体结构是“纯”还是“杂”：
    - 纯：互用而两相得；
    - 杂：互用而两不相谋，夹带忌神。
  - “带忌”是格局中最大的隐患，往往决定最终高低。
  - 败中若能见“解法线”（救应），则未必真败。

- 核心要点：
  - 成中有败：格局表面成，但内部有“带忌”的破局路线。
  - 败中有成：格局表面似败，但救应到位，则可起死回生。
  - 识别“带忌”和“救应”，是高阶断命的关键。

- 应用推演：
  1) 在判成格后，再检视是否存在“带忌”的破局线；
  2) 对带忌的局，评估忌神力量与位置，判断其破坏程度；
  3) 在败象中，寻找是否有印、合、会、制、化等救应存在；
  4) 将“成/败/带忌/救应”综合后，给出整体格局评价，而非只贴“成格/败格”的标签。

- 反例与边界：
  - 只根据“格名”判断好坏，不看是否带忌或有救应。

- 小例（示意）：
  - 一命官格成，但官逢财又逢伤，为“成中有败”；若岁运再助伤财，则败象易显。

- 校勘与字词辨析：
  - 本段中“劫才”“枭神”等词，本精校统一释义为“劫财”“偏印”，但保留原文用字。

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_288]` `[trigger: 成败救应]` `[factor_trigger: (chengzhong_youbai AND yizi_kejiu) OR (baizhong_youcheng AND yizi_kepo)]` `[role: 主干]` 成中有败一字可救，败中有成一字可破。 → 《子平真诠》#上卷
  - `[ns_zpzy_289]` `[trigger: 格局清纯]` `[factor_trigger: geju_qingchun AND guiqi_tiancheng]` `[role: 主干]` 格局清纯，贵气天成。 → 《子平真诠》#上卷
  - `[ns_zpzy_290]` `[trigger: 太过不及]` `[factor_trigger: (taiguo=true OR buji=true) AND result=fei_zhonghe]` `[role: 主干]` 太过不及，皆非中和。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "何谓败？成中有败，败中有成"
    factor_refs: list = ['chengge', 'baige', 'daiji', 'chengzhongyoubai', 'baizhongyoucheng', 'engine_id', 'daiji_luxian', 'bazi_rule_engine', 'yongji_zuoyong', 'bazi_rule_engine', 'baixiang_qiangdu', 'bazi_rule_engine', 'baixiang_suiyun', 'bazi_rule_engine', 'jiuying_yudi', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_097', 'daiji_luxian', 'rel_zpzq_098', 'yongji_zuoyong', 'rel_zpzq_099', 'baixiang_suiyun', 'evi_zpzq_094', 'daiji_luxian', 'rule_guange_daiji', 'evi_zpzq_095', 'daiji_luxian', 'rule_caige_daiji', 'concept_hidden_crack', 'concept_trigger']
    
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
        l1_anchor="zpzq_v1.0.0_何谓败_成中有败_败中有成_001_L1",
    )
    version: str = "1.0.0"
