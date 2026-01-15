"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.008930
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
    semantic_id="dts_v1.0.0_丁火_001",
    book_id="dts",
    engine_id="bazi"
)
class 丁火(SemanticEntry):
    """
    - 原文（source_text）：
  丁火柔中，内性昭融，抱乙而考，合壬而忠，旺而不烈，衰而不穷，如有嫡母，可秋可冬。

- 原注（原文注解）：
  　　丁为温暖之火，其性虽烈而属阴，则柔而得其中...
    """
    
    original_text: str = """- 原文（source_text）：
  丁火柔中，内性昭融，抱乙而考，合壬而忠，旺而不烈，衰而不穷，如有嫡母，可秋可冬。

- 原注（原文注解）：
  　　丁为温暖之火，其性虽烈而属阴，则柔而得其中矣，外柔顺而内文明，岂不昭融乎，乙乃丁之母，畏辛而丁抱之，不若丙抱甲而反能焚甲也，不若己抱丁而反能晦丁也，其孝异乎人矣，壬为丁之君，壬所畏者戊，外则抚恤戊土，使土不来欺壬也，内则暗化木神，使戊不能抗壬也，其忠异乎人矣，生于夏合，其焰不至于烈，生于秋冬，得一甲木，虽衰不至于穷，故曰可秋可冬，皆柔道也。

- 分字分词释义：
  - 丁：阴火，灯烛之火，柔和内敛。
  - 柔中：柔和而得中道，不偏不倚。
  - 昭融：光明融和，外柔内明。
  - 抱乙而孝：乙木为丁之印母，丁火护乙不使辛金克伤，显孝道。
  - 合壬而忠：壬水为丁之君（正官），丁与壬合化木，护壬不使戊土克水，显忠节。
  - 旺而不烈：即使身旺也不过于猛烈焚物。
  - 衰而不穷：即使身衰有甲木助之亦不至于穷困。
  - 嫡母：指甲木，正印生丁。
  - 可秋可冬：秋冬寒令有甲木印星可行，不畏时令之衰。

- 规范化释义（primary_lang_explained）：
  丁火如灯烛之光，柔和而内明，不像丙火那般猛烈外放。它的特点在于"柔中有道"：对母（乙木）有护持之孝，护乙不使辛金来克；对君（壬水）有扶助之忠，合壬化木使戊土不能欺壬。旺时温和不烈，衰时有甲木印星相助亦不至于穷困。秋冬寒令只要有嫡母甲木透出，便能借木生火、延续光明，这便是"可秋可冬"的柔道之妙。

- **次语种完整诠释（secondary_lang_full）**：  
  Ding Fire is the image of candlelight or lamplight—gentle, warm, and inwardly luminous. Unlike Bing Fire which blazes outward, Ding maintains a "soft centrality" (Rou Zhong): externally yielding yet internally bright and clear. Its character reveals itself in two key relationships. First, toward its mother Yi Wood: Ding shelters Yi from Xin Metal's attack, demonstrating filial devotion without consuming the resource as Bing would consume Jia. Second, toward its ruler Ren Water: Ding combines with Ren to transform into Wood, thereby protecting Ren from Wu Earth's control—an act of loyalty that works through transformation rather than direct confrontation. Even when strong, Ding does not burn destructively; even when weak, it does not become helpless as long as Jia Wood (the "legitimate mother") is present to provide generative support. Thus in autumn and winter when fire naturally weakens, Ding can still function if Jia is available—this is the "flexible way" (Rou Dao) that allows adaptation across seasons through proper resource alignment.

- **核心要点**：
  - 丁为阴火，如灯烛之光，柔和内明
  - 柔中之道：外柔顺而内文明，不偏不倚
  - 抱乙而孝：护母乙木不使辛金克伤
  - 合壬而忠：与壬合化，护君不使戊土欺壬
  - 旺而不烈：丁火身旺时温和不焚
  - 衰而不穷：有甲木印星相助则不至穷困
  - 可秋可冬：秋冬寒令有嫡母甲木则可行

- **详细解说**：
  丁火为阴火之代表，如灯烛星火，性在内明而外柔。与丙火的"猛烈外放"形成对照，丁火的精髓在于"柔中"——既不过刚也不过弱，恰到好处。本条特别点出丁火的两大美德：一是"孝"，乙木为丁之印母，本畏辛金来克，丁火护持乙木使辛不敢妄动，这种护母之情与丙火焚甲、己土晦丁不同，故称"其孝异乎人"；二是"忠"，壬水为丁之正官（君），壬畏戊土克制，丁与壬合化木气，一方面使戊土不能直接克壬，另一方面暗化木神护壬，这种忠节同样异于常情。判断丁火命局时，关键看是否有乙木、甲木印星相扶，以及是否与壬水形成有情之合。秋冬寒令丁火本衰，但只要有甲木嫡母透出，便能借木生火、延续光明。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_034]` `[trigger: 日主=丁火]` `[factor_trigger: tiangan_ding]` `[role: 主干]` 丁火如灯烛之光，柔中有道，贵在内明而不烈。 → 《滴天髓·天干论》#丁火
  - `[ns_dts_035]` `[trigger: 丁火见乙木]` `[factor_trigger: ding_yi_protection]` `[role: 主干依赖]` 丁火护乙不使辛克，抱乙而孝，母子相依有情。 → 《滴天髓·天干论》#丁火
  - `[ns_dts_036]` `[trigger: 丁火见壬水]` `[factor_trigger: ding_ren_combination]` `[role: 主干依赖]` 丁与壬合化木，护壬不使戊欺，合壬而忠。 → 《滴天髓·天干论》#丁火
  - `[ns_dts_119]` `[trigger: 丁火秋冬]` `[factor_trigger: ding_jia_support]` `[role: 条件分支]` 秋冬丁火得甲木嫡母相扶，虽衰不穷，可秋可冬。 → 《滴天髓·天干论》#丁火
  - `[ns_dts_120]` `[trigger: 旺而不烈]` `[factor_trigger: ding_intensity_balance]` `[role: 例外处理]` 丁火身旺亦不如丙火猛烈焚物，柔道使然。 → 《滴天髓·天干论》#丁火"""
    normalized_text_zh: str = """"""
    subject: str = "丁火"
    factor_refs: list = ['tiangan_ding_rou_zhong', 'ding_zhaorong', 'ding_baoyi_xiao', 'ding_heren_zhong', 'new_candidate', 'ding_keqiu_kedong']
    
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
        l1_anchor="dts_v1.0.0_丁火_001_L1",
    )
    version: str = "1.0.0"
