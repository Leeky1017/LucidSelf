"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619839
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
    semantic_id="qtbj_v1.0.0_6__二月甲木_卯月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 6二月甲木卯月(SemanticEntry):
    """
    - **原文（source_text）**：
  二月甲木，庚金得所，名阳刃驾杀，可云小贵，异途显达，或主武职，但要财资之。柱中逢才，英雄独压万人。
  若见癸水，困了才杀，主为光棍，重刃必定遭凶。性...
    """
    
    original_text: str = """- **原文（source_text）**：
  二月甲木，庚金得所，名阳刃驾杀，可云小贵，异途显达，或主武职，但要财资之。柱中逢才，英雄独压万人。
  若见癸水，困了才杀，主为光棍，重刃必定遭凶。性情凶暴。
  书曰：木旺宜火之光辉，秋闱可试。木向春生，处世安然有寿。日主无依，却喜运行才地。

- **分字分词释义**：
  - **庚金得所**：庚金得到适当位置 / 杀有力 / 有根气能制刃
  - **阳刃驾杀**：以羊刃格用七杀制衡 / 刃杀平衡 / 武贵之格
  - **异途显达**：非正统途径获得富贵 / 武职或吏职 / 非科举出身
  - **财资之**：用财来资助杀 / 土生金 / 财滋弱杀
  - **英雄独压万人**：英雄气概压倒众人 / 阳刃驾杀极品 / 将帅之材
  - **困了才杀**：困住财星和杀星 / 印泄杀克财 / 癸水为忌
  - **光棍**：无妻无子的男人 / 或指流氓 / 孤独贫贱
  - **重刃**：羊刃太重 / 比劫多 / 凶暴之象
  - **秋闱可试**：秋季科举考试可以一试 / 木火通明主文 / 文贵之象

- **规范化释义（primary_lang_explained）**：
  二月（卯月）的甲木，正如日中天（阳刃当权）。如果庚金（七杀）得地有力，这叫“阳刃驾杀”格，可说是小贵，往往由异途（非科举）显达，或者主武职，但必须要有财（土）来生助庚金。如果柱中遇到财星滋杀，便是英雄独压万人。
  如果见到癸水，泄金生木，困住了财星和杀星，主此人为光棍（无妻无子），阳刃太重必定遭遇凶灾。性情也会凶恶残暴。
  古书说：木旺适宜见火的光辉（木火通明），科举考试可以一试。木向春生（春木），若得火泄秀，处世安然且长寿。如果日主无依（无根气），反而喜欢运行财地（从财）。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 2nd Month (Rabbit Month) is at its peak (Yang Edge). If Geng Metal (Seven Killings) is well-placed, it is called "Yang Edge Driving Killings" (Yang Ren Jia Sha), denoting minor nobility, often achieving prominence through alternative paths or military career, but it requires Wealth (Earth) to assist the Metal. If Wealth appears in the pillars to nourish the Killing, one becomes a hero suppressing ten thousand people alone.
  If Gui Water appears, entrapping the Wealth and Killing (by leaking Metal and generating Wood), it denotes being a "bare stick" (bachelor/rogue); heavy Yang Edge ensures disaster. The temperament will be ferocious and violent.
  The book says: Prosperous Wood suits the brilliance of Fire, promising success in Autumn exams. Wood born in Spring, if properly vented, lives peacefully with longevity. If the Day Master has no reliance (roots), it delights in running through Wealth lands (Abandon Life Follow Wealth).

- **核心要点**：
  - **核心格局**：阳刃驾杀（Yang Edge Driving Killings）。
  - **用神**：首取庚金（制刃），次取戊土（财滋杀）。
  - **忌神**：癸水（困杀生刃）。
  - **变格**：木火通明（用丙丁泄秀）。

- **详细解说**：
  卯月甲木，羊刃当权，木气极旺。
  - 必须用“杀”来制“刃”，所谓“杀无刃不显，刃无杀不威”。
  - “庚金得所”指庚金有根（如坐申、酉、巳、丑），且有土生。
  - 这里的“英雄独压万人”是对阳刃驾杀格极高的评价。
  - 反之，若见癸水印星，泄杀生刃，则杀无力制刃，刃气太重，反主凶暴孤贫。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_098]` `[trigger: 阳刃驾杀]` `[factor_trigger: month_mao AND tiangan_jia AND tiangan_geng AND pattern_yang_edge_driving_killings]` `[role: 主干]` 二月甲木，庚金得所，名阳刃驾杀，可云小贵，异途显达。 → 《穷通宝鉴·三春甲木》#3.6
  - `[ns_qttbj_099]` `[trigger: 阳刃驾杀]` `[factor_trigger: pattern_yang_edge_driving_killings AND element_earth]` `[role: 主干依赖]` 柱中逢才，英雄独压万人。 → 《穷通宝鉴·三春甲木》#3.6
  - `[ns_qttbj_100]` `[trigger: 卯月忌癸]` `[factor_trigger: month_mao AND tiangan_jia AND tiangan_gui AND pattern_yang_edge]` `[role: 例外处理]` 若见癸水，困了才杀，主为光棍，重刃必定遭凶。 → 《穷通宝鉴·三春甲木》#3.6
  - `[ns_qttbj_101]` `[trigger: 木火通明]` `[factor_trigger: month_mao AND tiangan_jia AND element_fire AND pattern_wood_fire_bright]` `[role: 条件分支]` 木旺宜火之光辉，秋闱可试。 → 《穷通宝鉴·三春甲木》#3.6
  - `[ns_qttbj_102]` `[trigger: 春木寿]` `[factor_trigger: season_spring AND element_wood AND element_fire]` `[role: 总结]` 木向春生，处世安然有寿。 → 《穷通宝鉴·三春甲木》#3.6"""
    normalized_text_zh: str = """"""
    subject: str = "6. 二月甲木（卯月）"
    factor_refs: list = ['pattern_yang_edge_driving_killings', 'prominence_via_alternative_paths', 'bare_stick_bachelor', 'entrapped_wealth_and_killing']
    
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
        l1_anchor="qtbj_v1.0.0_6__二月甲木_卯月_001_L1",
    )
    version: str = "1.0.0"
