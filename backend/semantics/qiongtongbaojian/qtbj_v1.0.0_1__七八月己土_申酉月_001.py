"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597117
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
    semantic_id="qtbj_v1.0.0_1__七八月己土_申酉月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1七八月己土申酉月(SemanticEntry):
    """
    - **原文（source_text）**：
  三秋己土，万物收藏之际，外虚内实，寒气渐升，须丙火温之，癸水润之，不特此也，且癸能泄金，丙能制金，补土精神，则秋生之物咸茂矣。癸先丙后。
  丙癸两透...
    """
    
    original_text: str = """- **原文（source_text）**：
  三秋己土，万物收藏之际，外虚内实，寒气渐升，须丙火温之，癸水润之，不特此也，且癸能泄金，丙能制金，补土精神，则秋生之物咸茂矣。癸先丙后。
  丙癸两透，雁塔题名。或无癸，有两丙透者，异途显达。或武职权高。或有丙火，不见壬癸，为假道斯文，终无诚实。或有壬癸无丙者，衣食充足，才能而已。
  或支成金局，癸透有根，此人家畜万缗，富中取贵。
  或支四库，甲透者富。乏甲者孤贫。或甲出无癸乏金，积德可全科甲。
  或丙透癸藏，遇金颇有选援，加一壬辅，富贵慷慨，有贤声。见戊透者，主遭凶厄且贫。
  八月支成金局，无丙丁出救，此人零丁孤苦。如得丙透丁藏，生己元神，此人名魁天下，五福完人。

- **分字分词释义**：
  - **万物收藏**：万物收获储藏 / 秋季特点 / 金旺
  - **外虚内实**：外表虚弱内部实在 / 秋己土性 / 需丙癸
  - **补土精神**：补充土的精气神 / 丙制金癸泄金 / 生土
  - **雁塔题名**：在雁塔上题写名字 / 进士 / 吉象
  - **假道斯文**：假装斯文有礼 / 有丙无水 / 次凶
  - **家畜万缗**：家产万贯 / 金局癸透 / 极富
  - **选援**：选拔推荐 / 丙透遇金 / 吉象
  - **零丁孤苦**：孤独无依 / 金局无火 / 凶象
  - **名魁天下**：名列天下第一 / 丙丁配金局 / 极贵
  - **五福完人**：五福俱全的完人 / 极贵极福 / 吉象

- **规范化释义（primary_lang_explained）**：
  秋季（申酉戌月）的己土，万物收藏的时候，外虚内实（己土秋天泄气，故虚？原文作外虚内实，可能是指地表凉内部暖，或指土质松软），寒气逐渐上升，必须用丙火温暖它，用癸水滋润它。不仅如此，而且癸水能泄金（金生水，泄金气），丙火能制金（克金），补足土的精神（生土），那么秋天生长的万物都茂盛了。癸水先，丙火后（先润后暖，或金旺先泄）。
  丙火癸水两透，雁塔题名（进士）。或者无癸水，有两个丙火透出，异途显达，或者武职权高（印制食伤）。如果有丙火，不见壬癸水，是“假道斯文”，终究没有诚实（燥土不生金，无水润金）。或者有壬癸水无丙火，衣食充足，有才能而已（有财无印）。
  如果地支合成金局（食伤旺），癸水（财）透出有根（食伤生财），这人家畜万缗（极富），富中取贵。
  如果地支全四库（辰戌丑未），甲木透出者富（疏土）。缺乏甲木者孤贫（稼穑？不，四库杂气需疏）。或者甲木出干无癸水缺乏金，积德可以保全科甲。
  如果丙火透出癸水藏支，遇到金（食伤）颇有选拔推荐（选援），加上一个壬水辅助，富贵慷慨，有贤名。见到戊土透出（夺财），主遭遇凶厄而且贫穷。
  八月（酉月）地支合成金局（伤官），没有丙丁火（印）出干救应，这人零丁孤苦（泄气太重）。如果得到丙火透出丁火藏支，生扶己土元神，这人名魁天下，五福完人。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth in the Three Autumn Months: Time of harvest/storage; hollow outside, solid inside; Cold Qi rises. Must use Bing to warm, Gui to moisten. Not only that, Gui leaks Metal, Bing controls Metal, replenishing Earth's spirit; then autumn things flourish. Gui first, then Bing.
  If Bing and Gui are both revealed, one passes the exams. Without Gui but with two Bings, alternative fame or high military power. With Bing but no Ren/Gui, "Pretending to be Cultured", lacking honesty. With Ren/Gui but no Bing, sufficient food/clothing, merely talented.
  If branches form a Metal Frame, and Gui reveals with root, the family has ten thousand strings of cash (great wealth), obtaining nobility amidst wealth.
  If branches are Four Treasuries (Earth), Jia revealed implies wealth. Lacking Jia implies loneliness/poverty.
  If Bing reveals and Gui hides, meeting Metal implies support/selection; adding Ren to assist implies generous wealth/nobility and virtuous reputation. Seeing Wu reveal implies disaster and poverty.
  In the 8th Month, if branches form a Metal Frame without Bing/Ding to save, one is lonely/poor. If Bing reveals and Ding hides, generating Ji's Source Spirit, one ranks first under heaven, a perfect man of Five Blessings.

- **核心要点**：
  - **首要用神**：丙（暖/制金）、癸（润/泄金）。
  - **金旺泄气**：秋土怕金多泄气，喜印（丙丁）生身制食伤。
  - **食伤生财**：金局透癸，大富。
  - **四库喜甲**：土重需疏。

- **详细解说**：
  - 申酉月己土病死之地（土长生在申？通论土寄生于火，故申酉为病死；若寄生于水，申酉为长生沐浴。穷通此处论“金泄身寒”，明显采土生金泄气之说）。
  - “名魁天下，五福完人”：指伤官配印格（金局配丙丁），极贵。
  - “假道斯文”：秋土无水，金不出，土燥，故有名无实。"""
    normalized_text_zh: str = """"""
    subject: str = "1. 七八月己土（申酉月）"
    factor_refs: list = ['selection_support', 'ten_thousand_strings', 'five_blessings']
    
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
        l1_anchor="qtbj_v1.0.0_1__七八月己土_申酉月_001_L1",
    )
    version: str = "1.0.0"
