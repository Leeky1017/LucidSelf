"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636795
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
    semantic_id="zw_v1.0.0_父母宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 父母宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

父母宫诸星论。凡看父母，先看父母宫星曜庙旺、落陷，并以太阳为父、太阴为母，以定父母双全与否、刑克早晚；次看羊陀火铃空劫等煞星会合，以辨弃祖、退祖、重拜父母、过房入赘、寄养等...
    """
    
    original_text: str = """#### 原文（断句）：

父母宫诸星论。凡看父母，先看父母宫星曜庙旺、落陷，并以太阳为父、太阴为母，以定父母双全与否、刑克早晚；次看羊陀火铃空劫等煞星会合，以辨弃祖、退祖、重拜父母、过房入赘、寄养等特殊情况；又兼看日夜生时与太阳、太阴在命盘中的位置，细分先克父、先克母或虽有刑而得贵人延生。

#### 分字分词释义：

- **父母宫**：十二宫之一，主父母缘分、养育关系、成长环境与上辈荫庇。
- **刑克**：古义为对父母有克害或生离死别之象，现代可宽解为缘分浅薄、离别较早或关系失和。
- **重拜父母**：非亲生父母抚养，或多次变更监护人，现代可包括过继、继父母、寄养等情形。
- **弃祖 / 退祖**：远离祖业与族群，或因环境原因无法承接祖业。
- **过房 / 入赘**：过房指入他姓为嗣，入赘指男方入女方家中成婚，古代常见于父母宫煞重格局。

#### 规范化释义（primary_lang_explained）：

父母宫专门论命主与父母的缘分深浅、养育过程的顺逆，以及父母能否给予稳定的庇护。判断时，首先以太阳为父、太阴为母：

- 太阳、太阴在庙旺地且不受重煞冲破，多主父母双全、养育有依；
- 若太阳在陷地又多煞，主先克父或父缘薄；太阴在陷地多煞，则主先克母或母缘薄；
- 二星俱陷，则需配合日夜生判断：日生者父存母先逝之象减轻，夜生者母存父先逝之象减轻，仍需看全盘吉凶综合。

其次看父母宫主星与羊陀火铃空劫等煞星组合：吉星多而煞少者，多主父母平安、虽有小灾亦可安度；煞星重而无制，则易有弃祖、过房、入赘、寄养、二姓延生等象。现代应用时，可将这些理解为童年家庭结构的变化，如离异、重组家庭、外祖父母抚养等，而不必拘泥于古代名词。

#### 完整对等诠释（secondary_lang_full·11父母宫）：

The Parents Palace focuses on how parental figures and the original family setting shape a person’s early life and long‑term emotional script. When the Sun and the Moon are strong and relatively unharmed, they point to parents who are broadly present and capable of providing a recognisable home base, even if circumstances are not ideal. When one of them is weakened and heavily afflicted, the symbolism shifts toward thinner affinity with that side of the family: physical absence, early loss, prolonged separation, illness, or an enduring difficulty in understanding and being understood. When both lights are damaged, the chart is less about inevitable tragedy and more about a fragile or changeable family framework in which the native must learn resilience earlier than most.

Afflictions in the Parents Palace also describe changes in who actually plays the parenting role: step‑parents, grandparents, foster carers or other adults who assume responsibility for raising the native. Classical statements about leaving one clan and joining another can be re‑read today as adoption, blended families, living with relatives or growing up far from the original hometown. Benefic stars soften these shifts, indicating that, even if the form of the family is unusual, there are still people who care and protect. In modern consultation, this palace is best used to support understanding and healing around one’s family of origin: to see early hardship as context rather than curse, to recognise both the gifts and wounds inherited from parents, and to claim the freedom to build chosen family where the birth family could not fully provide.

#### 核心要点（整理）：

1. **刑克判断**：区分无克、轻克与重克，避免一律理解为"必然丧亲"。
2. **双全与否**：通过太阳、太阴与父母宫主星状态，判断父母是否双全，以及哪一方缘分较薄。
3. **特殊家庭结构**：弃祖、过房、入赘、寄养、二姓延生等，本质是家庭结构的变动与抚养关系的转移。
3. **特殊家庭结构**：弃祖、过房、入赘、寄养等，本质是家庭结构的变动与抚养关系的转移。
4. **日夜生差异**：日生偏重父方，夜生偏重母方，配合太阳、太阴的庙陷吉凶细判。
5. **现代重释**：从"刑克"转向"缘分深浅"与"原生家庭环境差异"的理解，避免宿命化解读。

#### 校勘与字词辨析：

- **刑克**：现代不宜直译为"克死父母"，可理解为缘分薄、分离早或关系紧张。
- **二姓延生**：指通过过房、入赘等方式延续香火，现代可理解为收养、重组家庭等形式的血脉/家庭延续。
- **退祖二姓安居**：离开原来宗族体系，在他姓或外地安家落户。

#### 详细解说：

父母宫是紫微斗数中专论原生家庭与亲缘的宫位，古人侧重于"刑克"与"双全"的判断，现代则可理解为命主与父母的关系模式、养育环境与早年家庭结构。

**判断逻辑有三层**：
1. **日月为父母象征**：太阳为父、太阴为母，是判断父母缘分的核心。太阳庙旺无煞，父缘深；太阴庙旺无煞，母缘深。日月俱陷或受煞冲，则父母缘分皆薄。
2. **父母宫主星定结构**：紫微、天府守父母宫，多主父母有地位或能力；天同、太阴守之，多主父母慈爱温和；七杀、破军守之，多主与父母关系紧张或早年分离。
3. **日夜生配合细判**：日生者（白天出生）太阳为用，父缘较重；夜生者（夜间出生）太阴为用，母缘较重。配合日月的庙陷，可细分"先克父"或"先克母"的倾向。

**特殊家庭结构的现代理解**：
- **弃祖**：离开原生家庭环境，在外地或他人家中成长。
- **过房**：被收养或寄养于他人家中。
- **入赘**：男方入女方家庭，在女方家族体系中生活。
- **二姓延生**：通过收养、重组家庭等方式延续家族。
- **重拜父母**：多次变更监护人或抚养者。

这些古代术语在现代可理解为：离异家庭、重组家庭、外祖父母抚养、寄宿学校、早年留学等各种童年家庭结构的变化。

**现代应用**：
父母宫不应被用来恐吓当事人"必克父母"，而应作为理解原生家庭印记的工具。煞重者可能在情感依附、安全感与自我价值感上有更多功课；吉多者则更多得到父母的支持与示范。关键在于看清起点，选择如何与过去和解并走向独立人生。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："太阳太阴俱庙旺，父母双全寿且昌，左右昌曲相扶助，荫庇终身福泽长。"此句常用于日月吉象的父母双全格局描述。
- **反面叙事**："日陷先克父，月陷先克母，二星俱陷更加煞，弃祖过房二姓住。"此句为原文中的核心口诀，警示日月俱陷的家庭结构变动风险。
- **现代转化**：某命主父母宫太阳太阴同宫庙旺，父母恩爱，家庭和睦，命主从小在稳定环境中成长，验证"日月同宫主双全"。另一命主父母宫破军擎羊同宫，幼年父母离异，由外祖母抚养长大，成年后与父母关系疏远，验证"煞重主弃祖、缘薄"的特性，但命主通过心理成长逐渐与原生家庭和解。"""
    normalized_text_zh: str = """"""
    subject: str = "父母宫诸星论"
    factor_refs: list = ['palace_parents', 'pattern_xingke', 'pattern_chongbai', 'pattern_guofangruzui', 'pattern_erxingyansheng', 'source_ref', 'rel_fumu_001', 'star_ziwei', 'rel_fumu_002', 'star_taiyang', 'rel_fumu_003', 'group_liusha', 'evi_fumu_001', 'star_ziwei', 'rule_fumu_ziwei', 'evi_fumu_002', 'group_liusha', 'rule_fumu_sha', 'concept_parents', 'concept_origin']
    
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
        l1_anchor="zw_v1.0.0_父母宫诸星论_001_L1",
    )
    version: str = "1.0.0"
