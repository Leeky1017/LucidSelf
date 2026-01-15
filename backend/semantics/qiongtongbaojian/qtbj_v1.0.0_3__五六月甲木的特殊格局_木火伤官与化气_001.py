"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619896
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
    semantic_id="qtbj_v1.0.0_3__五六月甲木的特殊格局_木火伤官与化气_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3五六月甲木的特殊格局木火伤官与化气(SemanticEntry):
    """
    - **原文（source_text）**：
  若柱中多金，名曰杀重身轻，先富后贫，运不相扶，非贫即夭。或庚多，有一二丙丁制伏，又有壬癸透干，泄金之气，此又为先贫后富。
  或满柱丙火，又加丁火，不...
    """
    
    original_text: str = """- **原文（source_text）**：
  若柱中多金，名曰杀重身轻，先富后贫，运不相扶，非贫即夭。或庚多，有一二丙丁制伏，又有壬癸透干，泄金之气，此又为先贫后富。
  或满柱丙火，又加丁火，不见官杀，谓之伤官伤尽最为奇，反成清贵，定主才学过人，科甲有望，但岁运不宜见水。若柱中有壬水，运又逢水，必贫夭死。
  但凡木火伤官者，聪明智巧，却是人同心异，多见多疑，虽不生事害人，每抱忌妒之想，女命一理同推。
  时月两透己土，名二土争合，男主奔流，女主淫贱。见二甲则不争矣，亦属平庸之辈。
  若在六月，见辰支，名为逢时化合格。以癸水为妻，丁火为子。

- **分字分词释义**：
  - **杀重身轻**：官杀太重日主太弱 / 金多木弱 / 先富后贫之象
  - **运不相扶**：大运不能扶助 / 行运不济 / 贫夭之因
  - **泄金之气**：泄掉金的气势 / 壬癸化杀 / 救应之法
  - **伤官伤尽**：伤官格中完全不见官星 / 纯粹伤官 / 清贵之格
  - **聪明智巧**：聪明有智慧且机巧 / 木火伤官特征 / 才华之象
  - **人同心异**：表面一致内心不同 / 伪善 / 心性弱点
  - **忌妒**：嫉妒 / 木火伤官心性 / 性格缺陷
  - **二土争合**：两个己土争着合一个甲木 / 争合之象 / 凶格
  - **奔流**：奔波流浪 / 男命争合之象 / 不安定
  - **逢时化合格**：在当令之月成化合格 / 甲己化土 / 变格

- **规范化释义（primary_lang_explained）**：
  如果柱中金多，叫“杀重身轻”，先富后贫，如果大运不扶助，不是贫穷就是夭折。或者庚金多，有一两个丙丁火制伏，又有壬癸水透干泄金气（杀印相生/食神制杀），这又是先贫后富。
  如果满柱丙火，又加丁火，不见官杀（金），这叫“伤官伤尽最为奇”，反而成为清高富贵，定主才学过人，有望登科甲，但岁运不宜见水（破格）。如果柱中有壬水，大运又逢水，必定贫穷夭折而死。
  凡是木火伤官格的人，聪明机智，但是人同心异（表面一套背后一套），多疑心，虽然不主动生事害人，但常怀嫉妒之心，女命也是同样的道理。
  时干月干都透出己土，叫“二土争合”（争合甲木），男命主奔波流浪，女命主淫乱下贱。如果再见一个甲木（二甲合二己）就不争了，但也属于平庸之辈。
  如果在六月（未月），地支见辰（土），这叫“逢时化合格”（甲己化土，生于土月）。以癸水（印）为妻，丁火（生财）为子。

- **完整对等诠释（secondary_lang_full）**：
  If there is much Metal in the pillars, it is "Heavy Killing Weak Body"; one is rich first then poor. If Luck does not support, it means poverty or early death. Or if Geng is numerous, but controlled by one or two Bing/Ding, and Ren/Gui are revealed to leak Metal's Qi, this becomes poor first then rich.
  If the pillars are full of Bing/Ding Fire and no Officer/Killing (Metal) is seen, it is called "Hurting Officer Exhausted, Most Wondrous". It becomes pure nobility, denoting surpassing talent and hope for exams, but the Annual/Luck pillars should not see Water. If there is Ren Water in the pillars and Luck meets Water again, one must die in poverty or prematurely.
  Generally, those with Wood-Fire Hurting Officer pattern are intelligent and clever, but outwardly agreeing while inwardly disagreeing, suspicious and jealous. Although they may not cause trouble to harm others, they always harbor jealousy. Female lives follow the same reasoning.
  If Ji Earth is revealed on both Month and Hour stems, it is "Two Earths Competing to Combine". Men wander, women are lewd. If two Jias are seen, there is no competition, but they are mediocre.
  If in the 6th Month (Goat), and Chen branch is seen, it is "Transformation Pattern in Season" (Jia combines with Ji transforming to Earth). Take Gui Water as Wife and Ding Fire as Child.

- **核心要点**：
  - **杀重身轻**：金多木弱，贫夭。救应：食伤制杀或印化杀。
  - **伤官伤尽**：满盘火无金，变格为贵（从儿/伤官伤尽）。忌见水破格。
  - **木火伤官心性**：聪明但多疑善妒。
  - **争合**：二己合一甲，下格。
  - **化气格**：六月甲己化土，真化格（逢辰未土旺）。

- **详细解说**：
  - 伤官伤尽：通常指金水伤官喜见官，木火伤官宜伤尽（不见官）。这里提到“满柱丙火...不见官杀...岁运不宜见水”，其实是“从儿格”或“炎上格”的变种，此时水是最大的忌神（激怒旺神）。
  - 化土格：甲己合化土，必须生于辰戌丑未月（土旺）。六月（未）正是化气之时。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_123]` `[trigger: 杀重身轻]` `[factor_trigger: (month_wu OR month_wei) AND tiangan_jia AND metal_excessive]` `[role: 主干]` 柱中多金，名曰杀重身轻，先富后贫，运不相扶，非贫即夭。 → 《穷通宝鉴·三夏甲木》#4.3
  - `[ns_qttbj_124]` `[trigger: 先贫后富]` `[factor_trigger: (month_wu OR month_wei) AND tiangan_jia AND tiangan_geng AND (tiangan_bing OR tiangan_ding) AND (tiangan_ren OR tiangan_gui)]` `[role: 条件分支]` 庚多，有丙丁制伏，又有壬癸透干，泄金之气，此又为先贫后富。 → 《穷通宝鉴·三夏甲木》#4.3
  - `[ns_qttbj_125]` `[trigger: 伤官伤尽]` `[factor_trigger: (month_wu OR month_wei) AND tiangan_jia AND fire_excessive AND NOT element_metal]` `[role: 条件分支]` 满柱丙火，又加丁火，不见官杀，谓之伤官伤尽最为奇，反成清贵。 → 《穷通宝鉴·三夏甲木》#4.3
  - `[ns_qttbj_126]` `[trigger: 木火伤官心性]` `[factor_trigger: pattern_wood_fire_hurting_officer]` `[role: 主干依赖]` 木火伤官者，聪明智巧，却是人同心异，多见多疑，每抱忌妒之想。 → 《穷通宝鉴·三夏甲木》#4.3
  - `[ns_qttbj_127]` `[trigger: 二土争合]` `[factor_trigger: tiangan_jia AND ji_double_revealed]` `[role: 例外处理]` 时月两透己土，名二土争合，男主奔流，女主淫贱。 → 《穷通宝鉴·三夏甲木》#4.3
  - `[ns_qttbj_128]` `[trigger: 甲己化土]` `[factor_trigger: month_wei AND tiangan_jia AND dizhi_chen AND pattern_transformation_earth]` `[role: 总结]` 六月见辰支，名为逢时化合格，以癸水为妻，丁火为子。 → 《穷通宝鉴·三夏甲木》#4.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 五六月甲木的特殊格局（木火伤官与化气）"
    factor_refs: list = ['heavy_killing_weak_body', 'pattern_hurting_officer_exhausted', 'outwardly_agreeing_inwardly_disagreeing', 'pattern_transform_earth']
    
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
        l1_anchor="qtbj_v1.0.0_3__五六月甲木的特殊格局_木火伤官与化气_001_L1",
    )
    version: str = "1.0.0"
