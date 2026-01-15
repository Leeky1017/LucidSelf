"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.008981
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
    semantic_id="dts_v1.0.0_庚金_001",
    book_id="dts",
    engine_id="bazi"
)
class 庚金(SemanticEntry):
    """
    - 原文（source_text）：
  庚金带煞，刚强为最，得水而清，得火而锐，土润则生，土干则脆，能胜甲兄，输于乙妹。

- 原注（原文注解）：
  　　庚乃阳金，是太白之精，带煞而刚健，健而得水...
    """
    
    original_text: str = """- 原文（source_text）：
  庚金带煞，刚强为最，得水而清，得火而锐，土润则生，土干则脆，能胜甲兄，输于乙妹。

- 原注（原文注解）：
  　　庚乃阳金，是太白之精，带煞而刚健，健而得水，则气流而清，刚而得火，则气纯而粹，有水之土，能全其生，有火之土，能使其脆，甲木虽强，力足伐之，乙木虽柔，合而输之。

- 分字分词释义：
  - 庚：阳金，太白之精，带煞刚健。
  - 带煞：含杀伐之气，刚猛有力。
  - 刚强为最：阳金之刚健为诸干之最。
  - 得水而清：水能泄金之锐气，使其清润不燥。
  - 得火而锐：火能锻金成器，使其锋利。
  - 土润则生：湿润之土能生金而不脆。
  - 土干则脆：干燥之土生金反使金脆弱。
  - 能胜甲兄：庚金能克制甲木（甲为兄，庚为弟）。
  - 输于乙妹：庚金遇乙木则合化，反被乙所制（乙为妹）。

- 规范化释义（primary_lang_explained）：
  庚金如太白之精，带杀伐之气，刚健为十干之最。其特点在于"刚而能化"：得水则气流清润、锐气不燥；得火则经锻炼成器、锋芒毕露；土润能生金而全其质，土干则生金反脆其身。庚金与木的关系颇有深意：对甲木刚对刚，庚能克胜；对乙木刚遇柔，乙庚相合反使庚金受制——此即"能胜甲兄，输于乙妹"的柔克刚之理。

- **次语种完整诠释（secondary_lang_full）**：  
  Geng Metal is the image of Taibaijing—the essence of the evening star Venus in its martial aspect—carrying an inherent killing edge and standing as the most unyielding among the ten stems. Its nature is "hard but transformable" under the right conditions. When it meets Water, the rigid sharpness flows out and becomes clear, refined, and less brittle—like a hot blade quenched to perfect temper. When it meets Fire, it undergoes forging: the heat purifies impurities and brings out its cutting edge, making it sharp and effective as a tool. Earth's role is nuanced: moist earth nourishes metal properly, allowing it to develop full strength; dry earth generates metal that is brittle and prone to breaking. The Wood relationships reveal a paradox of strength and weakness. Jia Wood, though sturdy, can be chopped down by Geng—hard against hard, the metal axe wins. But Yi Wood, soft and yielding, combines with Geng through heavenly stem combination (Yi-Geng He), and in this union Geng "loses" to the softer party—demonstrating that unyielding force can be neutralized by flexible adaptation.

- **核心要点**：
  - 庚为阳金，太白之精，带煞刚健
  - 刚强为最：阳金之刚健为十干之最
  - 得水而清：水泄金锐使其清润
  - 得火而锐：火锻金使其成器
  - 土润则生：湿土生金全其质
  - 土干则脆：干土生金反脆弱
  - 能胜甲兄：庚能克胜甲木
  - 输于乙妹：乙庚相合反使庚受制

- **详细解说**：
  庚金为阳金之代表，如太白之精，带杀伐之气而刚健无比。其精髓在于"刚而能化"——虽为最刚之金，却能在适当条件下转化为清润锋利的利器。得水则锐气流通而不燥，清润可用；得火则经锻炼而成器，锋芒毕露。土对庚金的作用更为微妙：湿润之土能全其生，干燥之土反使其脆——这说明庚金虽刚，仍需适当的滋养环境。最值得玩味的是庚金与木的关系：对甲木刚对刚，庚金力足伐之；对乙木刚遇柔，乙庚相合反使庚金受制。这揭示了"刚不可久"与"柔能克刚"的深层命理。判断庚金命局时，关键看水火土的配置：有水清、有火锐、土润则全，三者兼得则庚金成器可用。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_043]` `[trigger: 日主=庚金]` `[factor_trigger: tiangan_geng]` `[role: 主干]` 庚金如太白之精，带煞刚健，阳金之刚强为十干之最。 → 《滴天髓·天干论》#庚金
  - `[ns_dts_044]` `[trigger: 庚金见水]` `[factor_trigger: geng_water_clarity]` `[role: 主干依赖]` 庚金得水则气流清润，锐气不燥，成清秀之格。 → 《滴天髓·天干论》#庚金
  - `[ns_dts_045]` `[trigger: 庚金见火]` `[factor_trigger: geng_fire_tempering]` `[role: 主干依赖]` 庚金得火则经锻炼成器，锋芒毕露，利于建功。 → 《滴天髓·天干论》#庚金
  - `[ns_dts_125]` `[trigger: 庚金遇乙木]` `[factor_trigger: geng_yi_combination]` `[role: 条件分支]` 乙庚相合，刚遇柔则输，柔能克刚之理。 → 《滴天髓·天干论》#庚金
  - `[ns_dts_126]` `[trigger: 土润土干]` `[factor_trigger: geng_earth_quality]` `[role: 例外处理]` 湿土生金全其质，干土生金反脆弱，土质对庚金影响甚大。 → 《滴天髓·天干论》#庚金"""
    normalized_text_zh: str = """"""
    subject: str = "庚金"
    factor_refs: list = ['source_ref']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_庚金_001_L1",
    )
    version: str = "1.0.0"
