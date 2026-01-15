"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228795
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
    semantic_id="smth_v1.0.0_山头火_燎原落日与山木风水_001",
    book_id="sanming",
    engine_id="bazi"
)
class 山头火燎原落日与山木风水(SemanticEntry):
    """
    - **原文（source_text）**：
  甲戌乙亥山头火。山头火者，野焚燎原，延烧极目，依稀天际斜辉，仿佛山头落日，此乃九月烧荒衰草尽𦶟之火也。大槩宜山木与风木，喜大林松柏，以辰巳有风，寅卯归...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲戌乙亥山头火。山头火者，野焚燎原，延烧极目，依稀天际斜辉，仿佛山头落日，此乃九月烧荒衰草尽𦶟之火也。大槩宜山木与风木，喜大林松柏，以辰巳有风，寅卯归禄，臾得癸丑为山上木，主贵。无山则木无所依，火无所见，纵有风，亦不光显。余木无用，只以禄马看。水宜涧下，名为交泰，主吉。井泉清水，有木助之亦吉。大溪甲戊见甲寅，乙亥见乙卯，却真禄俱吉。天上须有雨露，而火到午未得地，再得清水济之，不至于燥，主福，不然则夭。大海就位，相克最凶。有山逢之，稍得日时，见金为财，须有山木助之则吉，无则凶。见士惟砂中有巽，能扬此火，别土无益。大凡此火无木见土，多是下贱之命。见火炉中太炎，霹火卤害，太阳昏蒙，山下战刑，皆所不宜。命带二三火，如限数逢木，主祸生不测，或夭。大都此火大怕刑冲。

- **规范化释义（primary_lang_explained）**：
  甲戌、乙亥为山头火。山头火如野火烧山、燎原延烧，远望如天边斜阳、山头落日，是九月烧荒、枯草尽焚之象。此火最宜山木与风木，喜大林木与松柏作依托，以辰巳为风、寅卯为归禄，再得癸丑为山上之木，则主贵显。有山则木有所依托、火有所映照；无山则木无所依、火光不著，即便有风亦难显赫。余木只可就禄马而论，不成主体。水方面，以涧下清水为最佳，名为"交泰"，主吉；井泉清水得木助亦佳；大溪水若甲戌见甲寅、乙亥见乙卯，真禄齐备，格局为吉。山头火若得天上雨露、午未得地，再加清水济之，则不致过燥，可主福寿；否则多主夭折。大海水就位与山头火相克最凶，若有山木辅佐尚可少减。土以砂中土带巽风可扬此火，余土无益；无木而多土，多主下贱劳苦之命。见炉中火则过炎，霹雳火则狠烈，太阳火使其失明，山下火与之战刑，皆凶象。命局若带二三重火、运限又逢木，多主横祸不测或夭折，且此火最怕刑冲破坏其山木格局。

- **完整对等诠释（secondary_lang_full）**：
  Jiaxu and Yihai belong to Mountain-Top Fire. Mountain-Top Fire is like wild flames burning hillsides, spreading across the slopes; from afar it resembles slanting rays at heaven’s edge, like a sunset over peaks—fire used in the ninth month to burn withered grasses. This Fire broadly favors mountain-wood and wind-wood, delighted in Great-Forest Wood and Pine-Cypress: Chen-Si provide wind, Yin-Mao grant stipend positions, and further gaining Guichou as mountain-top wood brings nobility. With mountains, Wood has support and Fire has surfaces to shine on; without mountains, Wood lacks anchorage and Fire cannot be seen, so even with wind its brilliance is limited. Other Woods mainly matter for stipend-horse rather than as core supports. Regarding Water, stream-below water is best and is called "Jiao-Tai" (Interpenetrating-Exchange), signifying auspicious harmony; clear well water with Wood assistance is also good. Great-Stream Water, where Jiaxu meets Jiayin and Yihai meets Yi-Mao, forms true stipend and is highly fortunate. Heavenly Fire must receive dew; when this Fire reaches Wu-Wei (its earthly seat) and then meets clear Water, dryness is moderated and blessings arise; otherwise early death is feared. Ocean Water at strength clashes most fiercely; only when mountains and Wood assist can some good remain. Among Earths only Sand-Center Earth with Xun-wind can lift this Fire; other Earths add little. Generally, when this Fire meets Earth without Wood, it often marks lowly, toil-filled lives. Encountering Furnace Fire overheats it; Thunder-Bolt Fire scorches; Sunlight Fire clouds over; Hillside-Beneath Fire forms battling punishments—all inauspicious. If the fate carries two or three Fires and time periods further bring Wood, sudden disasters or early death are likely; Mountain-Top Fire deeply fears punishments and clashes that break its mountain-wood configuration.

- **核心要点**：
  - 山头火如山巅烧荒与落日余辉，气势大而易燥
  - 成格关键在山木与风木：有山有木有风水为贵，无山多土则卑贱
  - 水以涧下、井泉、大溪真禄为佳，大海水就位为最凶
  - 忌多火叠见与刑冲，易致祸福极端与夭折

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_107]` `[trigger: 山头火]` `[factor_trigger: jiaxu_yihai AND shantou_huo]` `[role: 主干]` 山头火者，野焚燎原，延烧极目，依稀天际斜辉，仿佛山头落日，此乃九月烧荒衰草尽𦶟之火也。 → 《三命通会》卷一#山头火

- **详细解说**：
  山头火兼具"自然野火"与"山头夕照"两层意象，一方面代表外显、耀目的能量，一方面暗含消耗与无常。原文通过山、木、风、水、土、金、火诸要素描绘其成败：
  - 有山木为体、辰巳之风为用，再得癸丑山上木与清水为济，则火势得以展现而不至焚尽，成贵显之象。
  - 若无山而多土，则火焰无处映照，只成下贱劳苦之命。
  - 水若为涧下与井泉，则火水交泰而成福；若为大海水就位，则火被冲克殆尽，主大凶。
  - 多火叠见、再逢木运，则火势失控，轻则祸事横生，重则短寿夭折。
  因此，山头火的关键在于"有山可依、有木可焚、有风可扬、有水可济"，并严防火势与刑冲失控。

- **校勘与字词辨析（双语）**：
  - **中文**："交泰"本为坤上乾下之卦名，象征天地交合，此处借指火水和合之吉象；"燎原"指野火烧原野，喻火势极广。
  - **English**: "Jiao-Tai" derives from a hexagram meaning heaven and earth interpenetrating, here applied to harmonious Fire-Water exchange; "spreading wildfire" highlights vast, uncontrolled flames."""
    normalized_text_zh: str = """"""
    subject: str = "山头火：燎原落日与山木风水"
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
        l1_anchor="smth_v1.0.0_山头火_燎原落日与山木风水_001_L1",
    )
    version: str = "1.0.0"
