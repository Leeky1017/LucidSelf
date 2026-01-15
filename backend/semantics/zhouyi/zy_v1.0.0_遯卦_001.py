"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919226
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
    semantic_id="zy_v1.0.0_遯卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 遯卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  遯：亨。小利贞。

  【彖传】
  《彖》曰：“遯，亨”，遯而亨也。刚当位而应，与时行也。“小利贞”，浸而长也。遯之时义大矣哉！

...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  遯：亨。小利贞。

  【彖传】
  《彖》曰：“遯，亨”，遯而亨也。刚当位而应，与时行也。“小利贞”，浸而长也。遯之时义大矣哉！

  【象传】
  《象》曰：天下有山，遯；君子以远小人，不恶而严。

  【爻辞】
  初六，遯尾，厉，勿用有攸往。
  六二，执之用黄牛之革，莫之胜说。
  九三，系遯，有疾厉，畜臣妾吉。
  九四，好遯，君子吉，小人否。
  九五，嘉遯，贞吉。
  上九，肥遯，无不利。

- 分字分词释义：

  - **遯**：退隐、退避之意，并非消极逃跑，而是知时而退、保全其道。
  - **亨。小利贞**：以退为进，顺时遯藏则可通达；所利者为“小”，宜小处守正，而非图大功。
  - **刚当位而应，与时行也**：阳刚之爻居其当位，并能与时相应，选择合时的退避方式。
  - **浸而长也**：渐进而长久，指小处守正、细水长流的积累。
  - **天下有山**：山立于地上，象征屏障与止步之处，提示“知止不前”即为遯。
  - **远小人，不恶而严**：远离小人，不必心存仇恶，却要在原则上保持严正，不与之同流合污。
  - **遯尾**：退得太晚，只剩尾部可退，象征时机已过。
  - **执之用黄牛之革，莫之胜说**：以黄牛皮绳系之，谁也难以解开，比喻坚定执守、不可轻脱。
  - **系遯，有疾厉**：仍被牵系，不能全退，因而有病、有厉。
  - **好遯 / 嘉遯 / 肥遯**：从“喜好及时退隐”到“善美之遯”“丰足无碍之退”，显示遯的层级。

- **规范化释义（primary_lang_explained）**：

- 核心要点：

  - 遯卦核心是**“明知不可而退，以保其道与其身”**，区别于恐惧逃避。
  - 卦辞强调“小利贞”：在退的阶段，重心在于保小正，而非图大功。
  - 爻辞展示从“退晚为尾”到“被系而遯”“好遯”“嘉遯”“肥遯”的演进，是对退隐成熟度的刻画。

- 详细解说：

  卦象为上乾下艮：天在上、山在下，山止于天下，象征前路受阻、阳刚之气受限。与上经的艮、乾不同，此处的组合给出的是“知止而退”的图景：上有天之势，下有山之阻，中间之人必须选择如何退。

  初六“遯尾，厉，勿用有攸往”描绘的是迟迟不退、退在队尾的局面：到该退的时刻仍不肯离场，终致危险，因此不宜再往前行。六二“执之用黄牛之革，莫之胜说”则代表一种稳固的自我约束：用黄牛皮革牢牢系住退路与志向，不被外物轻易牵回险地。

  九三“系遯，有疾厉，畜臣妾吉”说明：身在险境却牵挂过多，退隐受阻，以致身心俱疲；此时适宜“畜臣妾”——缩小生活与责任的范围，不宜图谋大业。九四“好遯，君子吉，小人否”则点出“好遯”的分野：君子能欣然择退，以退为守道之机；小人只重眼前利害，不愿退步，反而不吉。

  九五"嘉遯，贞吉"是最理想的遯：在尊位仍能于时势不利时主动退让，守正而遯，为后人保留空间；上九"肥遯，无不利"则描绘退隐已成丰足之境：退得及时、退得从容，因此没有不利之处。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_299]` `[trigger: 卦=遯 AND 卦辞=亨小利贞]` `[factor_trigger: zhouyi_gua_dun AND zhouyi_guaci]` `[role: 主干]` 遯，亨，小利贞：退隐之时，小处守正为宜。 → 《周易·遯卦·卦辞》
  - `[ns_zhouyi_300]` `[trigger: 卦=遯 AND 彖传]` `[factor_trigger: zhouyi_gua_dun AND zhouyi_tuan AND zhouyi_tuiyin_chengdu AND zhouyi_shishi_tuirang]` `[role: 主干依赖]` 亨。刚当位而应，与时行也。 → 《周易·遯卦·彖传》
  - `[ns_zhouyi_301]` `[trigger: 卦=遯 AND 象传=天下有山]` `[factor_trigger: zhouyi_gua_dun AND zhouyi_xiang]` `[role: 主干依赖]` 天下有山，遯；君子以远小人，不恶而严：远离小人，不怀恶意却保持严正。 → 《周易·遯卦·象传》
  - `[ns_zhouyi_302]` `[trigger: 卦=遯 AND 初六=遯尾]` `[factor_trigger: zhouyi_gua_dun]` `[role: 例外处理]` 遯尾，厉，勿用有攸往：退得太晚，危险，勿再前往。 → 《周易·遯卦·爻辞》
  - `[ns_zhouyi_303]` `[trigger: 卦=遯 AND 六二=执之用黄牛之革]` `[factor_trigger: zhouyi_gua_dun]` `[role: 条件分支]` 执之用黄牛之革，莫之胜说：坚定守持，不可轻易脱离。 → 《周易·遯卦·爻辞》
  - `[ns_zhouyi_304]` `[trigger: 卦=遯 AND 九三=系遯]` `[factor_trigger: zhouyi_gua_dun]` `[role: 例外处理]` 系遯，有疾厉，畜臣妾吉：被牵系而退，身心俱疲，宜缩小范围。 → 《周易·遯卦·爻辞》
  - `[ns_zhouyi_305]` `[trigger: 卦=遯 AND 九四=好遯]` `[factor_trigger: zhouyi_gua_dun]` `[role: 条件分支]` 好遯，君子吉，小人否：欣然择退，君子吉，小人不能。 → 《周易·遯卦·爻辞》
  - `[ns_zhouyi_306]` `[trigger: 卦=遯 AND 九五=嘉遯]` `[factor_trigger: zhouyi_gua_dun]` `[role: 主干依赖]` 嘉遯，贞吉：善美之退，守正则吉。 → 《周易·遯卦·爻辞》
  - `[ns_zhouyi_307]` `[trigger: 卦=遯 AND 上九=肥遯无不利]` `[factor_trigger: zhouyi_gua_dun]` `[role: 总结]` 肥遯，无不利：从容丰足而退，无所不利。 → 《周易·遯卦·爻辞》
  - **中文**：
  - 卦辞"遯：亨。小利贞"依通行王弼本；"遯"为退隐，乾天在上、艮山在下。
  - "天下有山"谓艮山止于乾天之下，前路受阻，宜知时而退。
  - "不恶而严"谓远离小人不必心怀憎恶，但在原则上保持严正距离。
  - "遯尾"之"尾"释为队尾、末端，退得太晚则有危厉。
  - "黄牛之革"为坚韧之物，以喻坚定执守、不可轻脱。
  - "系遯"谓仍被牵系而不能全退，"畜臣妾"谓缩小范围自保。
  - "好遯/嘉遯/肥遯"三层渐进，从喜好退隐、善美之退，到丰足无碍之退。
  - **English**: Based on Wang Bi commentary edition. "遯" means strategic retreat. "天下有山" shows mountain blocking path. "不恶而严" means maintaining strictness without hatred. "遯尾" warns of retreating too late. "好遯/嘉遯/肥遯" show progressive levels of retreat mastery."""
    normalized_text_zh: str = """"""
    subject: str = "遯卦（䷠）"
    factor_refs: list = ['zhouyi_gua_033', 'symbol_mountain_under_heaven_proposal', 'principle_firm_without_hatred_proposal', 'state_prosperous_retreat_proposal', 'warning_late_retreat_proposal']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_遯卦_001_L1",
    )
    version: str = "1.0.0"
