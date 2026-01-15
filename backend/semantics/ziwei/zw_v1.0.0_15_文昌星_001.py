"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725642
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
    semantic_id="zw_v1.0.0_15_文昌星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 15文昌星(SemanticEntry):
    """
    - 原文（source_text）：

  问：文昌星所主若何？

  答曰：文昌主科甲，守身命，主人闲雅儒秀，清秀魁梧，博文广记，机变异常，一举成名，披绯衣紫，福寿双全。纵四杀冲破，不为下贱。女人加...
    """
    
    original_text: str = """- 原文（source_text）：

  问：文昌星所主若何？

  答曰：文昌主科甲，守身命，主人闲雅儒秀，清秀魁梧，博文广记，机变异常，一举成名，披绯衣紫，福寿双全。纵四杀冲破，不为下贱。女人加吉得地，衣禄充足；四杀冲破，偏房。僧道宜之，加权禄重厚，有师号。

- 原注（原文注解，可无则省略小节）：

  歌曰：文昌主科甲，辰巳是旺地。眉目定分明，相貌极俊丽。喜于金生人，富贵双全美。先难而后易，中晚有声名。太阳荫福集，传胪第一名。

- 分字分词释义：

  - **文昌主科甲**：以科举功名、文章声誉为主轴的吉星，关乎读书成名与仕途登第。
  - **辰巳旺地**：辰巳等宫位能使文昌得地，象征文才易发挥、机会平台充足。
  - **先难后易**：早年多经辛勤与挫折，历练之后方能在中晚年一举扬名。
  - **披绯衣紫**：取得正式功名与官阶，获得朝廷赐予的荣誉与服色，象征入仕成功。
  - **四杀不贱**：即便与四杀同度冲破，因文昌有文名与气质加持，仍不至于沦为卑贱之命。

- 规范化释义（primary_lang_explained）：

  本条将文昌刻画成典型的“科甲文星”：它主读书、文章与考试成绩，落在命宫或身宫时，往往代表命主气质清雅、举止斯文、外貌端正而带几分书卷之气。原文说“守身命”“闲雅儒秀”“博文广记，机变异常”，说明这颗星既带来记忆力、理解力与表达力的优势，也赋予应变与机智，使人在应试、写作、演说、策划等场景中易有亮眼表现。若再结合适当的时运与宫位结构，则有“一举成名，披绯衣紫”的象征——通过一次关键考试或机会，迅速建立起社会认可与声望。

  歌诀中的“辰巳是旺地”“先难而后易，中晚有声名”，进一步指出文昌的时间与空间条件：辰巳等宫位使其星力得地，金局生人又为其文气加油，多主才华有舞台可用；但往往需要经历一定的早年困难，如家境一般、起点不高或求学道路曲折，才能在中晚年迎来真正的发力期。即便遭遇四杀冲破，文昌仍有“气质保底”的一面——不至于完全跌入卑贱粗鄙之境，只是可能在现实层面出现偏房、支线发展或以副业、僧道等身份承载其文才。整体来看，文昌重点不在权势，而在“以文入世”：用知识、文字与品格，为自己打开一条较为体面、渐进上升的人生路径。

- 完整对等诠释（secondary_lang_full）：

  This passage presents Wenchang as the archetypal star of scholarship and examination success. When it guards the Life or Body palaces, it often describes someone with a naturally refined demeanour, clear features and a gentle, cultivated presence. Phrases such as "wide learning and excellent memory" and "exceptional adaptability" point to a capacity not only for absorbing information but also for shaping it—writing, speaking, planning and responding under pressure. In charts where circumstances and timing cooperate, Wenchang supports the classic image of "rising through the examinations": a single pivotal test or opportunity that brings official recognition, public honour and a stable platform from which to live out one’s talents.

  The verse emphasises that this academic blessing is not purely effortless luck. Being strong in the Chen and Si positions and especially in metal‑born charts provides fertile ground, but the motif of "difficult at first, easy later" suggests early years marked by effort, limitation or humble beginnings. Over time, perseverance and habit of study mature into visible reputation, particularly in middle and later life, when the Sun’s protective light gathers around Wenchang. Even when challenged by the Four Killings, the star retains a baseline of dignity: a person may be pushed into side paths—secondary positions, supporting roles, or religious and teaching vocations—but does not entirely lose cultural polish or the potential for respect. Ultimately, Wenchang asks how intellectual ability, aesthetic sense and disciplined learning can be translated into a life that is both respectable and quietly influential, rather than merely chasing rank for its own sake.

- 核心要点：

  1. **文昌科甲**：主科甲文章，守身命儒雅清秀，一举成名。
  2. **辰巳旺地**：辰巳是旺地，金生人富贵双全美。
  3. **披绯衣紫**：博文广记机变异常，披绯衣紫福寿双全。
  4. **四杀不贱**：纵四杀冲破不为下贱，女命偏房僧道有师号。
  5. **中晚声名**：先难而后易，中晚有声名，太阳荫福传胪第一。

- 叙事素材（narrative_snippets）：

  - **科甲文章**："文昌主科甲，守身命，主人闲雅儒秀"，文昌主读书应试与文章声誉。
  - **辰巳旺地**："辰巳是旺地，眉目定分明，相貌极俊丽"，辰巳宫位使文才与气质易于展现。
  - **先难后易**："先难而后易，中晚有声名"，多见早年辛勤，中晚年才真正扬名。
  - **披绯衣紫**："一举成名，披绯衣紫"，以一次关键考试或机会获得官阶与荣誉。
  - **四杀不贱**："纵四杀冲破，不为下贱"，即便有凶星冲击亦保留气质与体面。
  - **现代应用**：文昌可作为评估"学业/考试路径"的指标——看才华如何通过制度化考核得到认可。"""
    normalized_text_zh: str = """"""
    subject: str = "15 文昌星"
    factor_refs: list = ['star_wenchang', 'concept_kejia', 'state_chensi_wangdi', 'pattern_xiannan_houyi', 'ritual_chuanlu']
    
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
        l1_anchor="zw_v1.0.0_15_文昌星_001_L1",
    )
    version: str = "1.0.0"
