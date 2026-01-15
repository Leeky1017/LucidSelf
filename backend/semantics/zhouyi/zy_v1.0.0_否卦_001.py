"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899802
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
    semantic_id="zy_v1.0.0_否卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 否卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  否之匪人，不利，君子贞；大往，小来。

  【彖传】
  《彖》曰：否之匪人，不利，君子贞，大往，小来。
  则是天地不交，而万物不通...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  否之匪人，不利，君子贞；大往，小来。

  【彖传】
  《彖》曰：否之匪人，不利，君子贞，大往，小来。
  则是天地不交，而万物不通也；
  上下不交，而天下无邦也。
  内阴而外阳，内柔而外刚；
  内小人而外君子；
  小人道长，君子道消也。

  【象传】
  《象》曰：天地不交，否；
  君子以俭德辟难，不可荣以禄。

  【爻辞】
  初六，拔茅茹，以其汇，贞吉，亨。
  六二，包承，小人吉；大人否，亨。
  六三，包羞。
  九四，有命，无咎，畴离祉。
  九五，休否，大人吉；其亡，其亡，系于苞桑。
  上九，倾否，先否后喜。

- 分字分词释义：

  - 否：卦名，闭塞、不通之意，与泰相对。
  - 匪人：非其人，指不合于道的小人或奸人。
  - 君子贞：君子在否时仍须守贞，不为环境所移。
  - 大往，小来：大者（君子）离去，小者（小人）趋来，象局势之逆转。
  - 天地不交：乾坤不交感，阴阳阻隔。
  - 俭德辟难：以俭约、收敛之德避开灾难。
  - 拔茅茹，以其汇：同泰初爻，但在否时偏向“拔出同类以自保”。
  - 包承：包容承载，多指小人互相包藏承接其事。
  - 否：于爻辞中有“否定小人之道”的含义。
  - 包羞：包容羞耻、以羞为累，暗示纵容而不敢直面过失。
  - 有命，无咎：有所受命，故免于责咎。
  - 畴离祉：同类得福，禀受祉福而相聚。
  - 休否：否运将休，闭塞将解。
  - 其亡其亡，系于苞桑：多次告诫“将亡”，须像系于丛生而牢固的桑树那样自保。
  - 倾否：使否局倾覆，闭塞被打破。
  - 先否后喜：先经历否塞，终得喜乐。

- **规范化释义（primary_lang_explained）**：

  否卦与泰卦成对：泰是天地交、上下通，君子进用；否则天地不交、上下阻隔，小人道长、君子道消。卦辞“否之匪人，不利，君子贞，大往，小来”说明：在否塞之世，掌局者多非其人，局势整体不利；君子只能坚守贞道，大者离去，小者趋附。彖传从“天地不交”“上下不交”“内阴外阳、内柔外刚、内小人外君子”等结构描绘出一个“内场被小人占据、君子被排挤到外”的格局。

  六爻则给出否世中不同层位的处境与选择：初六“拔茅茹，以其汇，贞吉，亨”与泰初相似，却更强调在否中仍可与同类相牵，以贞固之志互相扶持而得吉；六二“包承，小人吉；大人否，亨”表明在否世中，小人互相包容承载而暂得其利，然而“大人否”——大人应当否定小人之道、与之保持距离，才能自获亨通。六三“包羞”则是对“纵容羞耻”的批评：身处不当之位，包藏羞辱与过失，只会加重否塞。

  九四“有命，无咎，畴离祉”象征在上升位置的阳刚者，若能顺天命行事，既可免咎，又可使同类得福；九五“休否，大人吉；其亡，其亡，系于苞桑”是全卦转机：否运将休，大人可吉，但须时时自警“其亡其亡”，像系于粗壮的桑树那样牢固根基，方可免于覆亡。上九“倾否，先否后喜”则宣告否局倾覆，闭塞解除，先前的困厄为之后的喜乐铺垫。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Pi, "Obstruction" or "Stagnation", stands opposite to Tai. Where Tai shows Heaven and Earth communicating and the noble in power, Pi shows Heaven and Earth cut off from one another, upper and lower blocked, petty people flourishing and the noble declining. The Judgment says, "Pi of those who are not the right people; unfavorable; for the noble person, steadfastness; the great depart, the small come." In a time of Pi, those who hold the center are often "not the right people"; the overall situation is unfavorable. The noble can do little but hold fast to correctness, while the truly great withdraw and the petty gather. The Tuan describes a structure in which Heaven and Earth do not meet, inner is Yin and outer Yang, inside is softness and pettiness while the noble are pushed outside. The forms of communication and correction still exist but are hollowed out.

  The six lines show different positions within such an obstructed world and the choices available there. The first line, "pulling up the grasses, with their roots entangled; steadfast and auspicious; success", echoes Tai but with a different emphasis: even in obstruction, like-minded people can still cling to one another, sustaining mutual steadfastness and thus finding a measure of good fortune. The second line, "embracing and bearing; for the petty person, good fortune; for the great person, obstruction; success", states that in Pi, petty people who cover and carry each other may enjoy short-term benefit, while great people must negate the petty way and keep their distance in order to remain truly successful. The third line, "embracing shame", criticizes those who, placed wrongly, choose to wrap themselves in shame and compromise rather than facing wrongs openly, thus deepening the obstruction.

  The fourth and fifth lines show points at which Yang energy can intervene. The fourth, "having mandate; no blame; companions share in blessing", indicates that someone in a rising position who truly follows the mandate—his rightful duty and the larger trend—can both avoid blame and become a source of blessing for his kind. The fifth, "resting obstruction; the great person is fortunate; 'it may perish, it may perish'; it is bound to a clump of mulberry trees", marks the turning point: the obstructed situation begins to ease, and the great person can be blessed, but only if he repeatedly warns himself that everything may yet be lost and anchors his roots as firmly as mulberry trees in clumped growth. The top line, "overturning obstruction; first obstruction, afterward joy", declares that Pi does not last forever: obstruction is finally overturned, and earlier hardships become the preparation for later joy.

- 核心要点：

  - 否卦是泰卦的反面，反映的是结构性闭塞与价值失位：小人居内、君子在外。
  - 在否世之中，君子的要务不在于一味抗争，而是守贞、自警、结同类、养根基，等待“休否”“倾否”之机。
  - 小人之“包承”“包羞”虽一时得利，但终难长久；真正的转机来自九五、上九处的结构性调整，而非局部争斗。

- 详细解说：

  卦象上乾下坤：与泰卦恰好倒置，天上地下却不交感；表面看似仍有上下秩序，实则气机隔绝，形成“形在而神不交”的局面。内阴外阳、内小人外君子，使得既有制度被小人占据，君子被排斥在外，所有沟通与修正机制变得迟缓甚至失效。

  初六与六二身处下卦阴位，代表“否世中的基层与中层阴柔”：若只是彼此包容、互相承接（包承），但不正视结构问题，只会使否运延长。六三“包羞”处下卦之中，更点明此类状态的羞耻性：既知其非，又不愿公开承担，只能在羞耻中维持局面。

  九四与九五则是阳刚介入的关键点：九四“有命，无咎，畴离祉”说明当局者若真能按“命”——即职责与大势——去做，而非随波逐流，就可以在否世中成为福源；九五“休否，大人吉；其亡，其亡，系于苞桑”则揭示否局缓解的条件：必须有大人处于中正之位，且时刻自警，知其“可亡”，才不会真的灭亡。上九最终以“倾否”结束全卦，说明否局不会永远持续，但其倾覆的方式与时机，与前面层层选择直接相关。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "否卦（䷋）"
    factor_refs: list = []
    
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
        l1_anchor="zy_v1.0.0_否卦_001_L1",
    )
    version: str = "1.0.0"
