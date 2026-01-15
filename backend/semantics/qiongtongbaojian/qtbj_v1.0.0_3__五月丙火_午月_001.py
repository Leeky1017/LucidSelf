"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596741
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
    semantic_id="qtbj_v1.0.0_3__五月丙火_午月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3五月丙火午月(SemanticEntry):
    """
    - **原文（source_text）**：
  五月丙火，得壬高透，方为上命。或一壬无庚，亦主贡监，犹防戊己出干，丁壬化合，则为平人。
  即不透庚壬，或有申宫长生之水，济之坐禄之金，至妙，必入词林...
    """
    
    original_text: str = """- **原文（source_text）**：
  五月丙火，得壬高透，方为上命。或一壬无庚，亦主贡监，犹防戊己出干，丁壬化合，则为平人。
  即不透庚壬，或有申宫长生之水，济之坐禄之金，至妙，必入词林。又怕戊己杂乱，则为异路。
  或成火局，不见滴水者，乃僧道鳏独之命。即有一二癸水，多遇火土，用之无力，瞽目之人。得戊己透泄火气，亦主刑克孤寡，行北运多凶，何也？所谓燥烈水激反凶！
  或成炎上格，柱运不见庚辛，多见甲乙者，反主大富贵，然亦不可见水运。
  或有庚癸透者，衣禄充足。支火轻，无目疾。支见水者，异途。
  或成土局，又为泄太过，得壬滋甲出干，土被制而火得生扶，此必富贵寿考之格也。

- **分字分词释义**：
  - **壬高透**：壬水高透天干 / 用神有力 / 吉象
  - **贡监**：贡生监生 / 小贵 / 次吉
  - **词林**：翰林院 / 大贵 / 吉象
  - **僧道鳏独**：僧人道士孤寡独居 / 无水 / 凶象
  - **瞽目**：瞎眼 / 火旺克水 / 凶象
  - **燥烈水激**：干燥猛烈被水激怒 / 微水激火 / 凶象
  - **炎上格**：火炎上升格 / 火局无水 / 变格
  - **坐禄之金**：坐禄位的金 / 庚在申 / 用神
  - **寿考**：长寿 / 壬甲配合 / 吉象
  - **异路**：非正途 / 武职 / 次吉

- **规范化释义（primary_lang_explained）**：
  五月（午月）的丙火，得到壬水高透，才是上等命。如果有一个壬水而没有庚金（水源），也主贡监（小贵），但还怕戊己土出干（克水），或丁壬化合（化木不化水），就是平人。
  即使不透出庚壬，如果有申宫长生之水（壬水），加上坐禄之金（庚金），也非常妙，必入词林（翰林）。又怕戊己土杂乱，则是异路功名。
  如果地支合成火局，不见一点水，是僧道鳏寡孤独的命。即使有一两个癸水，但遇到很多火土，癸水无力，是瞎眼（瞽目）的人。如果得到戊己土透出泄火气，也主刑克孤寡，行北方水运多凶险，为什么呢？所谓“燥烈水激反凶”！
  如果构成“炎上格”，柱中和运中不见庚辛金，多见甲乙木的，反而主大富贵，但也绝对不可见水运（破格）。
  如果有庚金癸水透出，衣禄充足。地支火轻，没有眼病。地支见水，异途出身。
  如果地支合成土局，又是泄气太过，得到壬水滋润甲木出干（甲制土生身），土被制约而火得到生扶，这必定是富贵长寿的格局。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 5th Month (Horse Month): Obtaining high Ren revealed makes a superior life. One Ren without Geng implies Gongjian (small nobility); still, guard against Wu/Ji revealing or Ding combining with Ren, which makes one ordinary.
  Even if Geng/Ren are not revealed, having Water in Shen (Birth Place) assisted by Metal in Lu (Shen), is extremely wondrous; one enters the Hanlin Academy. Again, fear Wu/Ji mixing, which leads to alternative paths.
  If a Fire Frame is formed without a drop of Water, it is a life of monks/Taoists/loners. Even with one or two Gui Waters, if met with much Fire/Earth, the Water is powerless, leading to blindness. If Wu/Ji reveal to leak Fire, it still implies punishment and loneliness; North Luck brings disaster. Why? "Scorching heat agitated by Water becomes ominous!"
  If it forms "Inflamed Upward Pattern" (Yan Shang), and pillars/Luck see no Geng/Xin but much Jia/Yi, it implies great wealth and nobility, but Water Luck must not be seen.
  If Geng and Gui are revealed, food and clothing are sufficient. If Branch Fire is light, no eye disease. If branches see Water, alternative path.
  If an Earth Frame is formed (leaking excessively), obtaining Ren to nourish Jia revealed (controlling Earth and generating Fire), this is certainly a structure of wealth, nobility, and longevity.

- **核心要点**：
  - **首要用神**：壬水（调候）。午月阳刃，最喜杀（壬）制。
  - **炎上格**：火局无水，喜木运，忌水运（激怒旺神）。
  - **燥烈水激**：火土燥极，见微水激怒，反凶。
  - **土局**：泄气太过，喜甲木（制土生身）。

- **详细解说**：
  - 午月丙火，阳刃秉令。
  - “燥烈水激反凶”：这是命理学重要原则。旺极之火，若无足够的水（壬水汪洋）来制，只用一点癸水或小水，反而激起火的怒气，导致灾祸。
  - “炎上格”在午月最易成，此时切忌见水，宜顺势（木火土）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_239]` `[trigger: 午月丙火]` `[factor_trigger: month_wu AND tiangan_bing AND tiangan_ren AND ren_high_reveal]` `[role: 主干]` 五月丙火，得壬高透，方为上命。丁多、兼看癸水。 → 《穷通宝鉴·三夏丙火》#13.3
  - `[ns_qttbj_240]` `[trigger: 燥烈水激]` `[factor_trigger: month_wu AND tiangan_bing AND gui_weak AND scorching_heat_agitated]` `[role: 例外处理]` 燥烈水激反凶！所谓旺极之火，见微水激怒。 → 《穷通宝鉴·三夏丙火》#13.3
  - `[ns_qttbj_241]` `[trigger: 炎上格]` `[factor_trigger: month_wu AND tiangan_bing AND dizhi_fire_frame AND NOT tiangan_geng AND NOT tiangan_xin AND pattern_inflamed_upward]` `[role: 条件分支]` 或成炎上格，柱运不见庚辛，多见甲乙者，反主大富贵，然亦不可见水运。 → 《穷通宝鉴·三夏丙火》#13.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 五月丙火（午月）"
    factor_refs: list = ['scorching_agitated', 'pattern_yanshang', 'hanlin_academy']
    
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
        l1_anchor="qtbj_v1.0.0_3__五月丙火_午月_001_L1",
    )
    version: str = "1.0.0"
