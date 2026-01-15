"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523867
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
    semantic_id="zpzq_v1.0.0_会合不能解刑冲_亦有以刑冲而解刑冲者_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 会合不能解刑冲亦有以刑冲而解刑冲者(SemanticEntry):
    """
    - **原文（source_text）**：
  又有刑冲而会合不能解者，何也？假如子年午月，日坐丑位，丑与子合，可以解冲，而时逢巳酉，则丑与巳酉会，而子复冲午；子年卯月，日坐戌位，戌与卯合，可以解刑...
    """
    
    original_text: str = """- **原文（source_text）**：
  又有刑冲而会合不能解者，何也？假如子年午月，日坐丑位，丑与子合，可以解冲，而时逢巳酉，则丑与巳酉会，而子复冲午；子年卯月，日坐戌位，戌与卯合，可以解刑，而或时逢寅午，则戌与寅午会，而卯复刑子，是会合而不能解刑冲也.更有刑冲而可以解刑者，何也？盖四柱之中，刑冲俱不为美，而刑冲用神，尤为破格，不如以另位之刑冲，解月令之刑冲矣.假如丙生子月，卯以刑子，而支又逢酉，则又与酉冲，不刑月令之官.甲生酉月，卯日冲之，而时逢子立，则卯与子刑，而月令官星，冲之无力.虽于别宫刑冲，六亲不无刑克，而月官犹在，其格不破.是所谓以刑冲而解刑冲也.如此之类，在人之变化而已.

- 原注（原文注解）：
  　　本段说明两种进阶情形：
  - 会合有时不能解刑冲，甚至只把问题“挪位”；
  - 反过来，另一个刑冲结构反而可以削弱原本对用神的刑冲，使格局得以保存.

- 分字分词释义：
  - 子年午月，日坐丑位：子在年支、午在月支、丑在日支.
  - 丑与子合，可以解冲：子丑六合，本可解子午冲.
  - 时逢巳酉，则丑与巳酉会，而子复冲午：丑被巳酉牵入会局，不再与子合，子午冲恢复.
  - 以另位之刑冲解月令之刑冲：用别处产生的刑冲，分散或削弱原本落在月令（用神）上的刑冲力度.

- **规范化释义（primary_lang_explained）**：
  有些时候，会合原本可以解冲解刑，但由于新的会局出现，原来的合局被“抽走”，导致冲刑恢复甚至移位.比如：子年午月，日坐丑位，子丑六合，本可以解子午冲；但若时支再见巳、酉，丑与巳酉会局，这时丑被拉走，子又失去合伴，恢复对子午的冲.同理，子年卯月，日坐戌位，本来戌卯合可解子卯刑；若时支再见寅午，戌与寅午会局，卯又转回来刑子，于是“会合不能解刑冲”.

-  另一方面，当用神所在的月令受到刑冲破害时，反而可以利用另一个位置上的刑冲来"分担压力".例如：丙火生子月，卯支刑子，子为官星所在之宫，此为"伤官刑官"；若命局中再有酉支出现，卯与酉相冲，卯的刑子之力被分散到酉上，月令之子所受之刑反而变轻了.又如甲生酉月，卯日冲酉，本为日冲月令官星；若时支再见子，卯子成刑，卯的力量部分转向与子之刑，反使其冲酉之力变弱，于是"月令官星虽受冲，而格局不破".作者称之为"以刑冲而解刑冲".

- **完整对等诠释（secondary_lang_full）**：  
  Sometimes a meeting or combination fails to resolve a clash or punishment. In the first example, Zi in the year and Wu in the month are in direct opposition; at first Chu in the day branch can combine with Zi and thus ease the Zi–Wu clash. But when additional branches such as Si and You appear and draw Chu into a separate meeting configuration, Chu is pulled away from Zi and can no longer serve as its partner; the original Zi–Wu clash then springs back into force. This illustrates that a potential resolving combination is only effective for as long as its members remain attached to the branches they are meant to protect.

  The second part of the paragraph shows the opposite move: using one clash to offset another. When the Month branch that carries the Useful God is under direct punishment, it may be safer to allow another clash elsewhere in the chart to absorb part of that pressure. Thus, if Bing Fire is born in Zi month and Mao branch punishes Zi (a classic "Hurting Officer punishing Officer" situation), the appearance of You branch lets Mao turn and clash with You instead, so that the blow to Zi is less severe. Or if Jia is born in You month and Mao day branch clashes You, a further appearance of Zi allows Mao to form a punishment with Zi and splits its force between two targets, weakening the original clash with You. In both cases the purpose is to protect the Month Officer or other key star: the configuration is still tense, but the core of the pattern is preserved by diverting part of the impact away from the main pivot.

- 详细解说：
  - 会合与刑冲之间的关系是动态的：会合可以解冲，但也可能因新的会合而解散旧合，使冲刑重新出现或转移.
  - 对格局核心用神（如月令官星）而言，关键在于“这一下刑冲落在谁身上”：若能通过别处的冲刑分担压力，格局可保.
  - 判断刑冲之凶，必须细看其落点与力度，而不仅仅是“有无刑冲”这四个字.

- 核心要点：
  - 会合能解冲刑，但要防“合伴被拉走”导致旧冲复现；
  - 另一个刑冲结构可以分流本来集中于用神位置的冲击，是“以毒攻毒”的思路；
  - 关键在于保护月令、日主等枢纽位置，使其不受致命破坏.

- 应用推演：
  1) 标出命局中所有刑冲结构，特别是落在月令用神与日主上的；
  2) 查有无会合可解，注意会合是否稳定，是否会被新局抽走；
  3) 若用神受刑冲，寻找是否有别处的刑冲可以“替身”承受部分冲击；
  4) 最终判断格局是否“破坏到核心”，还是“外围有伤而中枢尚存”.

- 反例与边界：
  - 只要见刑冲落在月令或日主，就武断断“格破”，不看会合与其他刑冲对其力度的调节；
  - 把任何刑冲都视为“可用来解刑冲”，不分其落点与对象，反而容易将问题扩大.

- 小例（示意）：
  - 丙日生子月，支有卯刑子，后运再遇酉，卯酉相冲，子受刑之力减轻，官星仍可用，此为“以冲解刑”的一类；
  - 甲日生酉月，卯日冲酉，时支见子，卯子成刑，冲酉之力减弱，月官尚在，仍可论官格.

- 校勘与字词辨析：
  - “如此之类，在人之变化而已”一句，本精校作“在于人之变化而已”，强调“具体如何运用，要看断命者如何活看变化”，不拘成法."""
    normalized_text_zh: str = """"""
    subject: str = "会合不能解刑冲，亦有以刑冲而解刑冲者"
    factor_refs: list = ['huihe_bunengji', 'xingchong_jie_xingchong', 'heban_beichou', 'geju_bupo']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_会合不能解刑冲_亦有以刑冲而解刑冲者_001_L1",
    )
    version: str = "1.0.0"
