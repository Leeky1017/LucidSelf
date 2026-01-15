"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755754
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
    semantic_id="zw_v1.0.0_论大限十年祸福何如_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论大限十年祸福何如(SemanticEntry):
    """
    - 分字分词释义：

  - **大限十年**：紫微斗数中以十年为一个周期的主要运程单位，决定该阶段人生走向。
  - **宫分星缠全吉**：大限所到的宫位及三方四正星曜皆为吉曜，且无恶杀冲破。
  ...
    """
    
    original_text: str = """- 分字分词释义：

  - **大限十年**：紫微斗数中以十年为一个周期的主要运程单位，决定该阶段人生走向。
  - **宫分星缠全吉**：大限所到的宫位及三方四正星曜皆为吉曜，且无恶杀冲破。
  - **庙旺得地**：星曜在其旺位或庙位，力量充沛，吉性得以发挥。
  - **擎羊陀罗火铃空劫**：六大恶杀，若与大限同守或冲照，则主十年不安、成败不一。
  - **十年安静，人财全美**：大限宫位吉星云集、无杀无破时的典型吉象。
  - **流年恶杀凑合**：在大限不佳的基础上，流年太岁再度叠加恶杀，使凶象进一步放大。
  - **官灾死亡立见**：大限落陷、凶杀重叠、流年小限皆凶时的极端凶象。
  - **夹限格局**：天伤、天使、空劫、羊陀等凶杀前后包夹某宫或岁限，使吉星难以发挥。
  - **寿星可解**：紫微、天同、天梁、贪狼等具解厄续寿性质的星曜，可在恶限中减轻冲击。

- 原文（断句）：

  论大限十年祸福何如？

  宫分星缠全吉，庙旺得地，无擎羊、陀罗、火铃、空劫者，主十年安静，人财全美。若限内有擎羊、陀罗、火铃、空劫忌星为伴，成败不一。如宫分星缠陷地，值擎羊、陀罗、火铃、空劫忌星，又加流年恶杀凑合，及小限巡逢凶杀，则官灾死亡立见。大限将出，有吉星众者无灾悔，少者灾多，损人破财不利。

  凡行至寅、申、巳、亥、子、午宫，遇紫微、天府、天同、太阳、太阴、昌曲、禄存、禄主吉星，主主人财兴旺，添丁进口之庆。行至辰、戌、丑、未、卯、酉宫，遇恶杀、廉贞、天使、擎羊、陀罗、火铃、空劫忌星，主人酒色荒迷，贫乏死生。遇左右昌曲，仕宦迁官加职，士民生子发财，妇人喜事，僧道亦利，商贾得益。凡大小二限及太岁，怕行天伤、天使夹地，怕行天空、地劫之地，怕行擎羊、陀罗之地，及羊陀冲照，怕脱凶限，怕逢凶限，又怕天伤、天使、劫空、羊陀并夹岁限。如天伤在子，天使在寅，岁限在丑宫，乃并夹也。羊陀命尚且无用，况夹限乎？若逃得过，须看寿星、紫微、天同、天梁、贪狼坐命可解，更须看月值恶杀、日值恶杀，加凑大小岁月日时五者，参详吉凶推断。

- 规范化释义（primary_lang_explained）：

  本条从「大限十年」的整体视角，说明如何综合星曜组合与宫位得失来判断一段十年祸福。第一段先给出最基本的框架：若大限所到之宫星曜同宫、三方四正多为吉曜，并且星在庙旺得地，又不见擎羊、陀罗、火星、铃星、空劫等凶杀同守，则可论其十年大致安静，人财两美。反之，若大限宫本身落陷，又被上述恶杀重重守照，再叠加流年恶杀、小限巡行皆来凑合，则官灾、疾病、死亡等大祸容易集中在这一大限中爆发。大限将要结束时，若宫中吉星众多，往往能带着「收尾平稳」离开；如吉少而凶多，则多见损人破财、尾声不利。

  第二段把空间维度进一步细化：当大限行至寅、申、巳、亥、子、午等宫位，若会紫微、天府、天同、太阳、太阴、昌曲、禄存等吉曜，多主财气兴隆、家门添人、喜事临门；行至辰、戌、丑、未、卯、酉等宫位，却与廉贞、天使及羊陀火铃空劫等恶杀会合，则易见酒色荒迷、贫乏病殃甚至生死之忧。又特别提出一类「夹限」格局：如天伤、天使、天空、地劫、羊陀等凶杀把某宫前后包围，或与岁限形成三重夹击，即便本命或大限内原有可用之星，也极难发挥作用，需依赖寿星、紫微、天同、天梁、贪狼等具解厄与续寿性质的星曜来减轻冲击。最后强调，真正准确的判断，还必须把大限、小限、太岁以及年月日时的值星综合成五重时间坐标，而不可只凭一处吉凶就下结论。

- 完整对等诠释（secondary_lang_full）：

  This section explains how to read a ten-year major period by looking at the
  house it occupies and the stars involved. When the period falls in a house
  with dignified benefics and few or no malefics such as Qingyang, Tuoluo,
  Huoxing, Lingxing or Kongjie, the text says the decade is broadly calm and
  prosperous, with both people and wealth kept in good condition. If the house
  is in a fallen position and packed with such malefics, and if annual and minor
  periods also bring hostile stars to bear, lawsuits, illness and even death can
  appear suddenly within that ten-year frame. As a period draws to a close,
  having strong benefics in place helps it end cleanly; when benefics are few
  and malefics many, the closing years tend to be marked by losses and regrets.

  The text further distinguishes paths through different houses. Major periods
  moving through Yin, Shen, Si, Hai, Zi or Wu and meeting the likes of Ziwei,
  Tianfu, Tiantong, the Sun, the Moon, Changqu and Lu stars often bring
  flourishing finances, new family members and good news. Periods in Chen, Xu,
  Chou, Wei, Mao or You that are crowded with Lianzhen, Tianshi and the harsh
  stars Qingyang, Tuoluo, Huoxing, Lingxing and Kongjie incline toward indulgence,
  poverty and even life-and-death crises. Especially dangerous are "encircled"
  configurations where Tianshang, Tianshi, Tian-kong, Di-jie and Yang-Tuo hem in
  a house from different sides or combine tightly with the annual ruler. In such
  cases even a decent natal chart struggles to perform unless supported by
  longevity and saving stars like Shouxing, Ziwei, Tiantong, Tianliang or
  Tanlang. The author urges practitioners to read the ten-year picture only
  after weighing major and minor periods, the annual ruler and the month, day
  and hour as five interconnected time axes.

- 核心要点：

  1. 大限十年的整体祸福，首看所到宫位星曜是否庙旺、吉多凶少，并远离擎羊、陀罗、火铃、空劫等恶杀。
  2. 若大限宫落陷，又被恶杀重重守照，再叠加流年与小限同来冲凑，则十年内大灾风险明显上升。
  3. 寅申巳亥子午配吉曜，多主兴隆与添丁；辰戌丑未卯酉逢恶杀，则多主荒迷、贫困甚至生死之忧。
  4. 「夹限」格局（天伤、天使、天空、地劫、羊陀等把宫位前后包围）是大凶征象，常须仰赖寿星与紫微、天同、天梁、贪狼等解厄星来缓和。
  5. 大限、小限、太岁及年月日时需一并参看，从「五重时间轴」综合推断，才能较准确地评估十年走向。"""
    normalized_text_zh: str = """"""
    subject: str = "论大限十年祸福何如"
    factor_refs: list = ['system_daxian', 'group_esha', 'pattern_jiaxian', 'group_shouxing', 'system_wuzhongshijian', 'source_ref', 'rel_daxian_001', 'system_daxian', 'rel_daxian_002', 'pattern_jiaxian', 'rel_daxian_003', 'group_shouxing', 'evi_daxian_001', 'system_daxian', 'rule_daxian_ji', 'evi_daxian_002', 'pattern_jiaxian', 'rule_daxian_jiaxian', 'concept_major_period', 'concept_encircled']
    
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
        l1_anchor="zw_v1.0.0_论大限十年祸福何如_001_L1",
    )
    version: str = "1.0.0"
