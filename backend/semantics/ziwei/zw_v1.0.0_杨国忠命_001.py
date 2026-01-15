"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699451
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
    semantic_id="zw_v1.0.0_杨国忠命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 杨国忠命(SemanticEntry):
    """
    - 分字分词释义：

  - **府相朝垣格**：紫府、天相等贵星朝拱命宫，主位极人臣的宰相格局。
  - **食禄千钟**：享受极高俸禄的象征。
  - **禄合格局**：禄星与多吉星形成合格局，主...
    """
    
    original_text: str = """- 分字分词释义：

  - **府相朝垣格**：紫府、天相等贵星朝拱命宫，主位极人臣的宰相格局。
  - **食禄千钟**：享受极高俸禄的象征。
  - **禄合格局**：禄星与多吉星形成合格局，主财禄有坚实支撑。
  - **廉贪二星空劫冲被**：廉贞、贪狼与空劫冲击命宫，使富贵基础被掘空。
  - **禄倒马倒**：俸禄与权位在关键限运中同时崩塔的象征。
  - **大限廉贪陷地**：大限行至廉贞贪狼落陷之地，主耗损风险大增。
  - **阳男土五局**：杨国忠命盘的五行局数，土五局主厚重权谋。

- **原文（source_text）**：  
  杨国忠命。阳男土五局。真正府相朝垣格，食禄千钟，虽然作得禄合格局，又忌廉贪二星，空劫冲被，不得富贵绵远。大限落于廉贪陷地，小限在寅，对冲太岁，为禄倒马倒之论。

- **规范化释义（primary_lang_explained）**：  
  杨国忠为阳男土五局，命局成「府相朝垣格」，科禄权贵齐集，象征能食「禄千钟」的高阶宰辅之命。本可凭藉禄合格局与权势支持，享长久富贵；但命宫同时受廉贞、贪狼二星与空劫冲击，形成表面华美、内里掏空的结构。原文以「不得富贵绵远」点出此局难以长保。  
  时运层面，大限落入廉贞、贪狼落陷之地，小限行至寅宫，对冲当年太岁，构成「禄倒马倒」：象征俸禄倒塌、权马翻覆，一旦激活便易在权力斗争与形势逆转中骤然失势，甚至以身殉国事。此命例展示的是「极盛而难久」的宰相命——前半生荣华至极，后期因结构弱点被时运放大，而急转直下。

- **完整对等诠释（secondary_lang_full）**：  
  Yang Guozhong is portrayed as a Yang Earth native whose chart forms the "Minister‑at‑Court" pattern: the Life palace is encircled by stipend and authority, befitting a grand councillor who "receives a thousand measures of grain." On the surface this Lu‑combination structure suggests long‑lasting wealth and power. Yet the same palace is entangled with Lian Zhen, Tan Lang and void‑robber stars, hollowing out the foundation beneath the splendour. The text notes that such fortune cannot remain enduring.  
  In timing, the major period falls into a region where Lian Zhen and Tan Lang are in debility, while the minor period in Yin clashes directly with Tai Sui. This configuration is summarised as "stipend overturned, horse overturned": stipends collapse and the career horse is thrown. When these factors converge, the native is prone to abrupt loss of office, violent political reversal or even death in the midst of upheaval. The case epitomises a prime ministerial fate that rises to dazzling heights yet cannot secure a peaceful old age.

- **核心要点**：  
  1. 府相朝垣与禄合格局，成就极高层级的宰相命。  
  2. 廉贪二星与空劫冲被，使格局「外实内虚」，富贵难以绵远。  
  3. 大限廉贪陷地、小限寅冲太岁，形成「禄倒马倒」，一旦触发往往急转直下。

- **叙事素材（narrative_snippets）**：
  - **府相朝垣**："真正府相朝垣格，食禄千钟"，杨国忠命主位极人臣、享受厚禄，为典型宰相命。
  - **外实内虚**："虽然作得禄合格局，又忌廉贪二星，空劫冲被，不得富贵绵远"，廉贪与空劫冲击，使华贵背后暗藏掏空之势。
  - **禄倒马倒**："大限落于廉贪陷地，小限在寅，对冲太岁，为禄倒马倒之论"，一点明权禄与仕途在关键岁运内同时翻覆。
  - **现代应用**：身居权要者若格局有「外实内虚」之象，在权力高峰时更应重视制度制衡与团队稳定，不可只见当下声势而忽略结构风险，以免一朝风向逆转即从云端坠落。"""
    normalized_text_zh: str = """"""
    subject: str = "杨国忠命"
    factor_refs: list = ['pattern_fuxiang_chaoyuan', 'pattern_luhe_geju', 'star_liantan_erxing', 'malefic_kongjie_chongbei', 'malefic_liantan_xiandi', 'result_ludao_madao']
    
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
        l1_anchor="zw_v1.0.0_杨国忠命_001_L1",
    )
    version: str = "1.0.0"
