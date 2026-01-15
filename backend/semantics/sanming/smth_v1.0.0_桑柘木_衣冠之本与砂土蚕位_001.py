"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228806
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
    semantic_id="smth_v1.0.0_桑柘木_衣冠之本与砂土蚕位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 桑柘木衣冠之本与砂土蚕位(SemanticEntry):
    """
    - **原文（source_text）**：
  壬子癸丑桑柘木。桑柘木者，缯彩镃基，绮罗根本，士民飘飘之袂，圣贤楚楚之衣。此木供蚕为弧，其用甚大。最爱砂土以为根基。又以辰巳为蚕食之地，不宜刑冲互破路...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬子癸丑桑柘木。桑柘木者，缯彩镃基，绮罗根本，士民飘飘之袂，圣贤楚楚之衣。此木供蚕为弧，其用甚大。最爱砂土以为根基。又以辰巳为蚕食之地，不宜刑冲互破路傍大。驿二土次吉，余土无益。水喜天河，为雨露之滋，长流溪涧、井泉诸水，皆可相依，亦须先得土为基，更加禄贵为妙。沧海水漂泛无定，无土主夭。见火灯头最吉，亦以辰巳之中为蚕位故也。炉中位居寅卯，木之旺地，天上霹雳二火，与此木干支有合化之情，有坎离交搆之妙，俱吉。但诸火不宜叠见，以金言之，砂中第一，剑锋能修整，此木为次。钗泊二金，须得土为基，如逢冲破，又凶。术喜庚寅、辛卯，为以弱就强，以小变大。作贵格论，纵无砂土亦吉。平地柏榴，无土则凶。大林乃东南蚕食之位，有土资生，主大贵。遇杨柳为桑柳成林，亦是贵格，须生春夏方吉。

- **规范化释义（primary_lang_explained）**：
  壬子、癸丑为桑柘木。桑柘木是缯彩绮罗之根本，支撑士民、圣贤之衣冠，是衣食文明的物质来源，因为供蚕食叶、吐丝结茧，其用极大。此木最爱砂中土为根基，路傍土、大驿土次之，余土多无所益。辰巳为蚕食之地，不宜刑冲互破。水以天河为上，象征雨露滋桑；长流水、溪涧、井泉等清水亦可资生，但须先有土基，再叠加贵人禄马方成富贵之象。沧海水漂泛无定，如无土基，多主漂泊与夭折。火以覆灯火最吉，对应辰巳中之蚕位；炉中火在寅卯木旺之地、天上火与霹雳火若与此木干支合化，如坎离交构，也可成吉，但诸火不可叠见过多，以免焚伤蚕桑。金中以砂中金为第一良配，剑锋金次之，可修整成材；钗金与泊金须得土基，否则逢冲破则凶。命局见庚寅、辛卯则有"以弱就强、以小变大"之象，宜作贵格看待，即使缺少砂土，若整体结构得宜亦可为吉。若配平地木与石榴木而无土基则凶；配大林木有东南蚕食之位及土气资生，则主大贵；遇杨柳木则成桑柳成林之象，春夏生人尤吉。

- **完整对等诠释（secondary_lang_full）**：
  Renzi and Guichou belong to Mulberry-Zelkova Wood. Mulberry-Zelkova Wood is the base of silks and brocades, root of fine garments—supporting the fluttering sleeves of commoners and the proper robes of sages—because it feeds silkworms whose cocoons become cloth. It most loves Sand-Center Earth as foundation, with Roadside and Grand-Post Earth as secondary; other Earths add little. Chen-Si mark the silkworm-feeding ground and should not suffer punishments or clashes. Water is best as Heavenly-River, symbolizing rain and dew nourishing mulberry; Long-Flowing Water, streams, and wells also suffice, but only after firm Earth foundations are present and further aided by noble stars and stipend-horse. Ocean Water, drifting with no fixed seat, without soil beneath, brings wandering and early death. Among Fires, Covered-Lamp Fire is most auspicious, corresponding to silkworm positions in Chen-Si; Furnace Fire in Yin-Mao, where Wood is strong, and Heavenly and Thunder-Bolt Fires that combine with this Wood into Kan-Li interlocking patterns are also good—yet multiple Fires stacked together are dangerous, scorching mulberry. Among Metals, Sand-Center Metal ranks first, with Sword-Edge Metal next, trimming and shaping this Wood; Hairpin-Gold and Foil-Metal must rest on soil or else clashes turn them harmful. Charts with Gengyin or Xinmao show the weak submitting to the strong and the small turning great, fitting noble configurations; even lacking sand-earth, such charts may still be judged fortunate when the whole structure supports it. Without soil, combinations with Flat-Earth Wood and Pomegranate Wood become inauspicious; with Great-Forest Wood at the southeastern silkworm-feeding sector and Earth sustaining it, great nobility arises. Meeting Willow Wood creates the image of mulberry-willow forests and is also a noble pattern, especially for spring-summer births.

- **核心要点**：
  - 桑柘木为衣冠布帛之本，象征衣食与文化根基
  - 喜砂土、路傍、大驿等土为基，再配天河与清水
  - 火需温和不叠见，覆灯、炉中、霹雳、天上皆可点化
  - 金以砂金、剑锋金修整成材，忌无土而逢冲破

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_108]` `[trigger: 桑柘木]` `[factor_trigger: renzi_guichou AND sangzhe_mu]` `[role: 主干]` 桑柘木者，缯彩绮罗之根本，士民之衣冠。最爱砂中土为根基，路傍土、大驿土次之。辰巳为蚕食之地，不宜刑冲互破。 → 《三命通会》卷一#桑柘木

- **详细解说**：
  桑柘木的核心是"蚕桑—衣冠—文明"链条：若有稳固砂土为根，再得雨露滋润与适度火温，则能支撑整套衣食礼制；若根基不稳、遇海水漂泊或重火焚灼，则供养体系崩解。原文又强调与其他木土金火的交互：
  - 与大林木、杨柳木形成桑柳成林，可视为文化生态的繁盛。
  - 与砂金、剑锋金的关系，类似工匠修剪雕琢，使原材更精致。
  - 与庚寅、辛卯的组合则体现格局放大，从小农经济跃升为贵族丝绸体系。

- **校勘与字词辨析（双语）**：
  - **中文**："缯彩镃基"指丝织与彩帛的物质根基；"蚕食之地"特指辰巳方位，象征蚕食桑叶之处。
  - **English**: "Foundation of silks and brocades" underscores the textile basis; "silkworm-feeding ground" refers to Chen-Si sectors where silkworms consume mulberry leaves."""
    normalized_text_zh: str = """"""
    subject: str = "桑柘木：衣冠之本与砂土蚕位"
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
        l1_anchor="smth_v1.0.0_桑柘木_衣冠之本与砂土蚕位_001_L1",
    )
    version: str = "1.0.0"
