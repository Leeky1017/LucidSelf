"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228837
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
    semantic_id="smth_v1.0.0_大林木_枝干撼风与艮土为源_002",
    book_id="sanming",
    engine_id="bazi"
)
class 大林木枝干撼风与艮土为源(SemanticEntry):
    """
    - **原文（source_text）**：
  壬午、癸未，杨柳木。杨柳木者，隋堤袅娜，汉苑轻盈，万缕不蚕之丝，千条不针之带。午未术之死墓，壬癸木之滋润。此木根基，惟喜砂土，见艮山则依倚。摇金遇寅卯...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬午、癸未，杨柳木。杨柳木者，隋堤袅娜，汉苑轻盈，万缕不蚕之丝，千条不针之带。午未术之死墓，壬癸木之滋润。此木根基，惟喜砂土，见艮山则依倚。摇金遇寅卯，则东方得地。辛丑有山，庚子不如。戊寅虽吉，巳卯尤胜。丙辰、丁巳，却嫌戌亥对冲，若见大驿，有丑为山边之驿，稍可。无丑独见此土，主夭贱。路傍就位，复值死墓，日时遇之，主人卑弱。屋土壬午见丁亥，丁壬合化则吉。丙戌不如水，见井泉长流大溪涧下皆吉，中间又分合化旺位尤吉。丙午、丁未，丙丁真火，午未亦火，此木至午未。已死壬午，见之大凶。癸庶几有别水济之，无害。此木午未已自有火，更见别火，恐引起伤寿。灯头乙巳有风，木折主凶。炉中寅卯本位木旺，反吉。霹火如壬午见己丑，癸未见戊子，阴阳交遇，更有砂土为基，主贵。若子午丑未对冲，则不为吉。金见本无造化，钗钏金泊，却喜成功。海镴剑砂虽忌见之，其间轻重，当以禄贵德煞参详。见松柏木，为脱体化神之格也，主贵。桑柘癸丑为山，作倚傍成林，主吉。庚申辛酉，木既死绝，又逄金克，以弱遇小，其人必贱。

- **规范化释义（primary_lang_explained）**：
  壬午、癸未为杨柳木。杨柳木如隋堤垂柳、汉苑轻枝，万缕不蚕之丝、千条不针之带，姿态柔美飘逸。午未为壬癸木之死墓，杨柳木在此地气中本已衰绝，却仍需壬癸之水润养其柔姿。其根基最喜砂中土，再见艮山则可依倚；遇寅卯配金则得东方之地：辛丑为山优于庚子，戊寅虽吉而巳卯更佳。丙辰、丁巳二土因戌亥对冲而多忌，若见大驿土而有丑为山边之驿尚可；无丑而独见大驿，则多主夭贱。路傍土就位又值死墓，日时遇之主性情卑弱。屋上土配壬午见丁亥，丁壬合化尚吉，丙戌则逊。水以井泉、长流水、大溪、涧下诸清水为佳，其中合化旺位尤吉。午未本为火旺之地，丙午、丁未真火叠加则杨柳木已至死墓，壬午再见此火尤凶，唯癸水略见方可济之。此木午未本自有火，再见别火则多引起折伤与寿限之忧。灯头火配乙巳有风主折枝凶象；炉中火居寅卯本位则因木旺反成吉。霹雳火如壬午见己丑、癸未见戊子，阴阳交遇，再有砂土为基，反主贵显。若子午丑未对冲，则吉象削弱。金本与杨柳木多无造化，钗钏金与泊金在成功后尚可点缀；海中、白镴、剑锋、砂金等虽多忌见，仍须结合禄、贵、德、煞等综合判断。见松柏木时，有"脱体化神"之格，主贵；桑柘木配癸丑为山，可依傍成林主吉。庚申辛酉时木气死绝又逢金克，以弱遇强，多主卑贱。

- **完整对等诠释（secondary_lang_full）**：
  Renwu and Guiwei belong to Willow Wood. Willow Wood conjures images of drooping willows along Sui embankments and light branches in Han gardens—countless strands like unsilkened threads, thousands of boughs like unstitched sashes—graceful and floating. Wu-Wei are the tomb phases for Ren-Gui Wood; although the Wood qi is exhausted there, willow still requires Ren-Gui Water to keep its softness alive. Its foundation favors Sand-Center Earth above all, with Gen-mountain providing further support. When shaken by Metal at Yin-Mao, it gains footing in the eastern direction: Xinchou as mountain surpasses Gengzi; Wuyin is auspicious and Simao even better. Bingchen and Dingsi Earths are disfavored due to clashes from Xu-Hai; seeing Grand-Post Earth with Chou as wayside station by a mountain is somewhat acceptable, but without Chou such Earth alone suggests lowly and short life. Roadside Earth at position plus tomb phases in day-hour generates weakness. Roof-Top Earth with Renwu meeting Dinghai, where Ding-Ren transform, is fortunate; Bingxu is inferior. Water from wells, long-flowing rivers, great streams, and stream-below sources all benefit willow, with transformative prosperous placements best. Wu-Wei inherently host Fire; Bingwu and Dingwei as genuine Fires atop tomb-phase willow are dangerous; Renwu meeting such Fire is dire unless Guishui alleviates it. Since willow already contains Fire in Wu-Wei, further Fires invite injury and shortened life. Covered-Lamp Fire at Yisi with wind breaks branches; Furnace Fire in Yin-Mao, willow’s own Wood seat, becomes beneficial. Thunder-Bolt Fire such as Renwu meeting Jichou or Guiwei meeting Wuzi, where yin and yang meet with Sand Earth as base, can signal nobility. Yet Zi-Wu and Chou-Wei clashes reduce auspiciousness. Metals naturally have little constructive effect here; Hairpin-Gold and Foil-Metal can ornament success, while Ocean-, White-Tin-, Sword-Edge-, and Sand-Metals are mostly unfavorable unless mediated by stipend, nobility, virtue, and other stars. Meeting Pine-Cypress Wood forms a "transform-body" pattern and is noble; Mulberry-Zelkova Wood with Guichou as mountain allows willow to lean and form forests, also fortunate. Under Gengshen or Xinyou, Wood is dead and further clashed by Metal—weak confronting small but sharp—so the person is usually of low station.

- **核心要点**：
  - 杨柳木象征柔美飘逸之木，生于午未死墓，仍赖壬癸润养
  - 喜砂土与艮山为基，配清泉长流之水更显柔姿
  - 畏大驿、路傍死墓无山，多主卑弱夭贱
  - 午未多火与灯头有风主折枝伤寿，霹雳火配砂土则反有贵象

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_111]` `[trigger: 杨柳木]` `[factor_trigger: renwu_guiwei AND yangliu_mu]` `[role: 主干]` 杨柳木者，隋堤袅娜，汉苑轻盈，万缕不蚕之丝，千条不针之带。午未木之死墓，壬癸木之滋润。此木根基，惟喜砂土，见艮山则依倚。 → 《三命通会》卷一#杨柳木

- **详细解说**：
  杨柳木的核心难题是"柔木居死墓"：环境本身偏燥、偏死，仍要保持柔美与生机。原文通过土、水、火、金、他木的组合展示不同命运：
  - 有砂土与艮山为根，再加清水为润，便是堤边垂柳、园林佳景；
  - 若落于大驿、路傍而无山辅，或多火而少水，则成风折枝、命途多舛之象；
  - 与霹雳火、松柏木、桑柘木等的组合，则显示在风雨、雷鸣与他木扶持中，柔木亦可成贵。

- **校勘与字词辨析（双语）**：
  - **中文**："隋堤袅娜"源自古诗，形容杨柳之姿态；"死墓"为命理术语，指某行在支上的死绝之地。
  - **English**: "Willows along the Sui embankment" is a classical poetic image; "tomb phase" denotes the branch where an element’s qi is exhausted."""
    normalized_text_zh: str = """"""
    subject: str = "大林木：枝干撼风与艮土为源"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_大林木_枝干撼风与艮土为源_002_L1",
    )
    version: str = "1.0.0"
