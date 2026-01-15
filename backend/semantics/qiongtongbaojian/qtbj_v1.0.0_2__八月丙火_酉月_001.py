"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596787
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
    semantic_id="qtbj_v1.0.0_2__八月丙火_酉月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2八月丙火酉月(SemanticEntry):
    """
    - **原文（source_text）**：
  八月丙火，日近黄昏，丙火之余光，存于光湖，仍用壬水辅映。
  四柱多丙，一壬高透为奇，定主登科及第。富贵双全。一壬藏支，亦主秀才。或戊多困水则假作斯文...
    """
    
    original_text: str = """- **原文（source_text）**：
  八月丙火，日近黄昏，丙火之余光，存于光湖，仍用壬水辅映。
  四柱多丙，一壬高透为奇，定主登科及第。富贵双全。一壬藏支，亦主秀才。或戊多困水则假作斯文。若无壬水，癸亦可用，但功名不久。
  或见辛透，不能从化，贫苦到老。或见一丁制辛，为人奸诈，不识高低。女命合此，长舌淫贱。
  或成金局，无辛出干，此非从才，乃朱门饿莩。如辛出干，不见比劫，此从才格，反主富贵，亲戚提拔，妻贤内助。
  用水者，金妻水子。从才者，水妻木子。

- **分字分词释义**：
  - **日近黄昏**：太阳接近黄昏 / 酉月特征 / 火死
  - **余光存于光湖**：余光保存在光亮湖面 / 壬映丙 / 贵象
  - **一壬高透为奇**：一个壬水高透最奇妙 / 多丙用壬 / 最贵
  - **假作斯文**：假装斯文有学问 / 戊困水 / 才华被困
  - **朱门饿莩**：富贵人家的饿死鬼 / 假从财 / 凶象
  - **妻贤内助**：妻子贤惠帮助内务 / 从财 / 吉象

- **规范化释义（primary_lang_explained）**：
  八月（酉月）的丙火，太阳接近黄昏，丙火的余光，保存在光亮的湖面上，仍然用壬水辅助映照。
  四柱多丙火（比劫帮身），一个壬水高透最为奇妙，定主登科及第，富贵双全。一个壬水藏支，也主秀才。如果戊土多困住水，则是假装斯文。如果没有壬水，癸水也可以用，但功名不长久。
  如果见到辛金透出，又不能从化（因为有比劫或根气），贫苦到老。如果见到一个丁火制辛金（劫财夺财），为人奸诈，不知高低。女命符合此格（贪财坏印/比劫争财），长舌且淫贱。
  如果地支合成金局，没有辛金出干，这不是从财格，而是“朱门饿莩”（富贵人家的饿死鬼，富屋贫人）。如果辛金出干，不见比劫，这是“从财格”，反而主富贵，有亲戚提拔，妻子贤惠内助。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 8th Month (Rooster Month): The Sun nears twilight; its residual light remains in the shining lake. Still use Ren Water to reflect.
  If pillars have much Bing, one high Ren revealed is marvelous; certainly passing exams, with complete wealth and nobility. One Ren hidden implies a Xiucai. If Wu is abundant trapping Water, one pretends to be cultured. Without Ren, Gui is usable, but fame is not lasting.
  If Xin is revealed but cannot Follow Transformation, one is poor until old age. If one Ding appears to control Xin, the person is treacherous and ignorant of propriety. For females, this implies being a gossip and lewd.
  If a Metal Frame is formed without Xin revealed, it is not Follow Wealth, but "Starving in a Vermilion Gate" (Rich House Poor Man). If Xin is revealed without Parallel/Rob Wealth, it is Follow Wealth Pattern, implying wealth and nobility, promotion by relatives, and a virtuous wife.

- **核心要点**：
  - **日近黄昏**：酉月丙火死地。
  - **一壬高透**：身弱喜印比，但此书特重壬水映照，即使在酉月，若比劫多（身转旺），仍首取壬。
  - **从财真假**：辛透无劫为真从（贵）；金局无辛或见劫为假从（朱门饿莩）。
  - **丁制辛**：酉月辛旺，丁火劫财见之，不仅不能制，反而表现为奸诈（劫财的心性）。

- **详细解说**：
  - “朱门饿莩”：形象地描述了财多身弱且格局不清（似从非从）的状态，守着金山银山却无福消受。
  - 丙辛在酉月虽相合，但若不化水（需水局/化神），则为绊住，加上丁火克辛，局势混乱，故主奸诈。
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_248]` `[trigger: 酉月丙火]` `[factor_trigger: month_you AND tiangan_bing AND tiangan_ren AND sun_on_lake]` `[role: 主干]` 八月丙火，日近黄昏，丙火之余光，存于光湖，仍用壬水辅映。 → 《穷通宝鉴·三秋丙火》#14.2
  - `[ns_qttbj_249]` `[trigger: 一壬高透]` `[factor_trigger: month_you AND bing_multiple AND tiangan_ren AND many_bing_one_ren]` `[role: 条件分支]` 四柱多丙，一壬高透为奇，定主登科及第，富贵双全。 → 《穷通宝鉴·三秋丙火》#14.2
  - `[ns_qttbj_250]` `[trigger: 朱门饿莩]` `[factor_trigger: month_you AND tiangan_bing AND dizhi_metal_frame AND NOT tiangan_xin AND starving_in_rich_house]` `[role: 例外处理]` 成金局，无辛出干，此非从才，乃朱门饿莩。 → 《穷通宝鉴·三秋丙火》#14.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 八月丙火（酉月）"
    factor_refs: list = ['starving_vermilion', 'pretend_cultured']
    
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
        l1_anchor="qtbj_v1.0.0_2__八月丙火_酉月_001_L1",
    )
    version: str = "1.0.0"
