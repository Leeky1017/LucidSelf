"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436336
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
    semantic_id="smth_v1.0.0_五脏六腑与干支病象总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五脏六腑与干支病象总论(SemanticEntry):
    """
    - 原文（source_text）：

  论疾病先知五脏六腑所属干支。

  歌诀：甲胆乙肝，丙小肠，丁心戊胃己脾乡；庚是大肠，辛属肺，壬系膀胱，癸肾藏；三焦亦向壬中寄，包络同归入癸乡。又曰：甲头乙...
    """
    
    original_text: str = """- 原文（source_text）：

  论疾病先知五脏六腑所属干支。

  歌诀：甲胆乙肝，丙小肠，丁心戊胃己脾乡；庚是大肠，辛属肺，壬系膀胱，癸肾藏；三焦亦向壬中寄，包络同归入癸乡。又曰：甲头乙顶丙肩求，丁心戊肋己属腹；庚是脐轮，辛属股，壬胫癸足一身由。又曰：子属膀胱、水道、耳；丑为胞肚及脾乡；寅胆、发、脉并两手；卯本十指内肝方；辰土为皮、肩、胸类；巳面、咽、齿、下鬓、肛；午火精神司眼目；未土胃、腕、膈、脊梁；申金大肠经络肺；酉中精血小肠藏；戌土命门腿踝足；亥水为头及肾囊。若依此法推人病，歧伯、雷公也播扬。又曰：午头，巳未两肩均；左右二膊是辰申；卯酉双肋寅戌腿；丑亥属脚，子为阴。又曰：乾首坤腹坎耳俦，震足巽股艮手留；兑口离目分八卦，凡看疾病此推求。

  夫疾病皆因五行不和，即人身五脏不和也。盖五行通于五脏，六腑通于九窍：凡十干受病属六腑，十二支受病属五脏。丙丁己午火局南离，主病在上；壬癸亥子水局北坎，主病在下；甲乙寅卯属震，主病在左；庚辛申酉属兑，主病在右；戊己辰戌丑未属坤艮，主病在脾胃及中脘。诸风晕掉、眼光日昏、血不调畅、早年落发、筋青瓜枯，属肝家甲乙寅卯木受亏主病故也；诸脓血疮疥、舌苦喑哑者，属心家丙丁巳午火受亏主病故也；浮肿、脚气、黄肿、口臭、翻胃、脾寒膈热者，属脾家戊己辰戌丑未土受亏主病故也；鼻塞酒槁、语蹇气结、咳嗽喘喊者，属肺家庚辛申酉受亏主病故也；白浊白带、霍乱泻痢、疝气小肠者，属肾家壬癸亥子受亏主病故也。

- 分字分词释义：

  - **五脏六腑所属干支**：以十天干、十二地支分别对应五脏六腑、四肢百骸，用以推测疾病所发之处。
  - **三焦、包络**：中医所言三焦、心包，两者在歌诀中分别寄壬水、癸水，以示其与水道、气机的联系。
  - **十干属腑、十二支属脏**：天干着眼于六腑功能失调，地支着眼于五脏亏损与病位。
  - **离坎震兑、坤艮**：以八卦方位配合五行，判断病在上、下、左、右与中宫。

- **规范化释义（primary_lang_explained）**：

  本节是《三命通会》中少见的“占病专篇”。作者用歌诀的方式，把五脏六腑、人体各部位与天干地支逐一对照：既指出“某干得病，多应哪一腑”，也指出“某支受损，多在何脏与何处”。随后又用八卦方位与五行组合，判断疾病偏于头面上部、腰腹中部，或下肢、左右等等，并归纳肝、心、脾、肺、肾五大系统受损时常见的一组症状。

  简言之：若命局某干支受刑冲克害，再配合行运与身体反应，就可以根据本节歌诀大致推测病象所主之脏腑与部位，但这只是古人对身心—五行对应关系的一种经验总结，而非现代医学诊断。

- 核心要点：

  - 通过**干支—脏腑—部位**的三重对应，来辅助判断疾病偏于哪里、属于哪一系统。
  - 十干偏向六腑、十二支偏向五脏，同时结合八卦方位看上下左右与中宫。
  - 各类症状（如眩晕、疮疥、浮肿、咳嗽等）分别归入肝、心、脾、肺、肾五大系统受损。
  - 本节属占病参考，并不等同于现代医学检查与治疗。

- 详细解说：

  在古代占病体系中，“病从何来、病在何处”常与命局、行运以及当下症状互相印证。本节提供的是一种“结构化索引”：

  1. **先定五行受损**  
     - 看命局中某行被严重克伐、刑冲，或行运加重其受损；  
     - 再结合当前症状，判断是肝（木）、心（火）、脾（土）、肺（金）、肾（水）哪一系统偏弱。

  2. **再看干支所落部位**  
     - 以“甲头乙顶丙肩求……”等歌诀，对应头面、肩臂、手足等不同部位；  
     - 若命局中相关干支频见且受制，则该部位易成病灶或旧患。

  3. **辅以方位八卦**  
     - 离为上、坎为下、震为左、兑为右、坤艮为中宫；  
     - 可进一步区分病势偏向头胸还是腰腹、偏左还是偏右。

  在现代视角下，我们可以把这些内容理解为一种“身心地图”：  
  - 木亏者，多见筋骨与情志问题；  
  - 火亏者，多见心血与神志问题；  
  - 土亏者，多见消化与运化问题；  
  - 金亏者，多见呼吸与皮毛问题；  
  - 水亏者，多见泌尿、生殖与骨髓问题。  

  这些归纳与当代中医理论仍有重合之处，但具体病名、病程与治疗仍须交给专业医生处理，不宜以命书取代医疗。

- 校勘与字词辨析：

  - 原文“巳面咽齿下宾肛”之“宾”多作“鬓”，本稿据意作“巳面咽齿、下鬓肛”理解，不另改字，只在断句中予以分开。
  - “血不调畅、早年落发、筋青瓜枯”等语，本稿在白话中归入肝木系统，不逐条对应具体西医病名。
  - “歧伯雷公也播扬”是借《内经》医家之名以自重其法，本稿仅保留为传统用语，不以此作权威背书。
  - **English**：
    - Traditional terminology; not used as authoritative endorsement.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_005]` `[trigger: 干支脏腑总纲]` `[factor_trigger: ganzhi_zangfu_duiying]` `[role: 主干]` 论疾病先知五脏六腑所属干支。 → 《三命通会》卷七#五脏六腑
  - `[ns_smth_07_006]` `[trigger: 十干歌诀]` `[factor_trigger: jia_dan_yi_gan AND bing_xiaochang]` `[role: 主干依赖]` 甲胆乙肝，丙小肠，丁心戊胃己脾乡；庚是大肠，辛属肺，壬系膀胱，癸肾藏。 → 《三命通会》卷七#五脏六腑
  - `[ns_smth_07_007]` `[trigger: 干腑支脏]` `[factor_trigger: shi_gan_shu_fu AND shi_zhi_shu_zang]` `[role: 条件分支]` 凡十干受病属六腑，十二支受病属五脏。 → 《三命通会》卷七#五脏六腑
  - `[ns_smth_07_008]` `[trigger: 歧伯雷公]` `[factor_trigger: qibo_leigong_boyang]` `[role: 总结]` 若依此法推人病，歧伯、雷公也播扬。 → 《三命通会》卷七#五脏六腑"""
    normalized_text_zh: str = """"""
    subject: str = "五脏六腑与干支病象总论"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_unnamed', 'bazi_semantic', 'bazi_structure_gua_1', 'bazi_semantic', 'bazi_state_wuxing_1', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_condition_trigger_condition', 'bazi_semantic', 'bazi_condition_factor_226', 'bazi_semantic', 'source_ref', 'rel_smth_07_001', 'ganzhi_zangfu_yingshe', 'rel_smth_07_002', 'shousun_wuxing_xitong', 'rel_smth_07_003', 'mingju_bingxiang_tiaojian', 'evi_smth_07_001', 'ganzhi_zangfu_yingshe', 'rule_ganzhi_zangfu', 'evi_smth_07_002', 'shousun_wuxing_xitong', 'rule_wuxing_zhengzhuang', 'evi_smth_07_003', 'mingju_bingxiang_tiaojian', 'rule_bingxiang', 'map_smth_07_001', 'map_smth_07_002']
    
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
        l1_anchor="smth_v1.0.0_五脏六腑与干支病象总论_001_L1",
    )
    version: str = "1.0.0"
