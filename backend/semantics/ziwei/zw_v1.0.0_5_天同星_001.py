"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725547
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
    semantic_id="zw_v1.0.0_5_天同星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 5天同星(SemanticEntry):
    """
    - 原文（source_text）：

  问：天同星所主若何？

  答曰：天同星属水金，南斗第四星也，为福德宫之主宰。后云化福，最喜遇吉曜，助福添祥。为人廉洁，貌禀清奇。有机谋，无亢激，不怕七杀相...
    """
    
    original_text: str = """- 原文（source_text）：

  问：天同星所主若何？

  答曰：天同星属水金，南斗第四星也，为福德宫之主宰。后云化福，最喜遇吉曜，助福添祥。为人廉洁，貌禀清奇。有机谋，无亢激，不怕七杀相侵，不怕诸杀同缠。限若逢之，一生得地，十二宫中皆曰福，无破定为祥。

- 原注（原文注解，可无则省略小节）：

  希夷先生曰：天同、南斗益算保生之星。化禄为善，逢吉为祥。身命值之，主为人谦逊，禀性温和，心慈耿直，文墨精通，有奇志，无凶激。不忌七杀相侵，不畏诸凶同度，十二宫中皆为福论。遇左右、昌、梁贵显。喜壬、乙生人，巳亥得地，不宜六庚生人，居酉地终身不守。会四杀，居巳亥为陷，残疾孤克。女人逢杀冲破，刑夫克子，梁月冲破，合作偏房。僧道宜之，主享福。

- 分字分词释义：

  - **化福 / 化禄为善**：将原本中性的福禄之气转化为具体的福报与善行回馈，强调“享福而不失善念”。
  - **不畏七杀诸凶**：七杀等杀星临命本应多凶，天同却能部分化解，使之不至于演化为极端灾祸。
  - **壬乙生人、巳亥得地**：特指壬水、乙木日主在巳亥宫位遇天同时，多主福厚寿长、环境较为宽和安稳。
  - **居酉终身不守**：天同居酉且配合六庚生人时，象征福德漂浮不定，难以长久守成。
  - **梁月冲破作偏房**：女命遇天同与天梁、太阴等组合失衡时，容易以偏房、再婚等形式进入关系。

- 规范化释义（primary_lang_explained）：

  本条将天同描绘为福德宫的主宰，是一颗“化福为善”的温和之星。它本身并不以激烈扩张见长，而更像一股润物细无声的背景福泽：落在福德、命身等宫位，多主性情谦逊温和、内心仁厚，读书有悟而不炫耀，愿意在关系中做“润滑剂”。即便命盘同时带有七杀等重杀，只要天同得地、又有左右、昌梁等吉星相会，往往可以缓和冲突，使许多潜在的凶险化为可承受的波折。

  文中也提出了天同的边界条件：壬、乙生人在巳亥遇天同，多主福厚长寿，适合走稳定、温和的发展路径；若是六庚生人而天同居酉，则容易出现“心不安住”“环境难以久守”的状态，福德像流沙一样难以抓牢。女命当天同与天梁、太阴等组合受损，特别是“梁月冲破”时，较易以偏房、再婚、长期暧昧等形式进入亲密关系；若再逢杀星重冲，则有刑夫克子、情感受创的高风险。整体而言，天同并非“永恒好运”的符号，而是提示：福德的稳固来自温和、节制与善意的长期累积，一旦环境与自身选择偏离这一轨道，其福气也会快速流失。

- 完整对等诠释（secondary_lang_full）：

  This section presents Tiantong as the patron of blessings and ease, a gentle star that rules the Fortune palace. Rather than promising spectacular breakthroughs, Tiantong describes a background field of support: when dignified and well‑aspected, it gives people a soft temperament, a sincere heart, and the capacity to enjoy life without constantly fighting for survival. Even when harsh stars such as Qisha are present, Tiantong can dilute their edge so that crises are experienced more as challenges to be managed than as absolute catastrophes.

  The text also notes important boundaries. Charts where Tiantong is well placed for Ren or Yi Day Masters in Si or Hai often show lives that, while not necessarily dazzling, are stable, protected and able to harvest the fruits of steady effort. By contrast, combinations like Tiantong in You for people born on Geng days are said to correlate with difficulty “staying put”: jobs, places and relationships may all feel hard to hold, and the person must consciously cultivate discipline to avoid drifting. In women’s charts, damaged combinations involving Tiantong, Tianliang and the Moon—especially when “broken by beams and moon”—can manifest as long‑term involvement in secondary or ambiguous partnerships, or as repeated strain in marriage and motherhood when further struck by killing stars. Overall, Tiantong invites us to see blessing not as random luck, but as the cumulative result of gentle character, ethical choices and environments that support rather than erode these qualities。

- 核心要点：

  1. **天同化福**：福德宫主宰，化禄为善，主享福添祥。
  2. **性温机深**：为人谦逊温和、心慈耿直，有机谋无亢激。
  3. **不畏杀星**：不怕七杀相侵、不畏诸凶同度，十二宫皆福论。
  4. **壬乙生人**：喜壬乙生人，巳亥得地；不宜六庚生人酉地。
  5. **女命偏房**：女人梁月冲破，合作偏房；杀冲则刑夫克子。

- 叙事素材（narrative_snippets）：

  - **天同化福**："天同乃福德宫，主化福为善"，天同为福德宫主宰。
  - **不畏杀星**："不怕七杀相侵，不畏诸凶同度"，天同可化解杀星凶性。
  - **壬乙得地**："喜壬乙生人，巳亥得地"，特定生年与宫位的最佳配置。
  - **梁月偏房**："女人梁月冲破，合作偏房"，女命天同配合失衡的风险。
  - **现代应用**：天同可作为评估"福德稳定性"的指标——福气来自温和善意的长期累积。"""
    normalized_text_zh: str = """"""
    subject: str = "5 天同星"
    factor_refs: list = ['star_tiantong', 'concept_huafu', 'trait_buwei_sha', 'combo_renyi_sihai', 'combo_liangyue_chongpo']
    
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
        l1_anchor="zw_v1.0.0_5_天同星_001_L1",
    )
    version: str = "1.0.0"
