"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559308
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
    semantic_id="yhzp_v1.0.0_看命入式_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 看命入式(SemanticEntry):
    """
    - **原文（source_text）**：
  五行提纲，凡看命排下八字，以日干为主。
  取年为根，为上祖财产，知世运之盛衰。
  取月为苗，为父母，则知亲荫之有无。
  日干为己身，日支为妻妾，...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行提纲，凡看命排下八字，以日干为主。
  取年为根，为上祖财产，知世运之盛衰。
  取月为苗，为父母，则知亲荫之有无。
  日干为己身，日支为妻妾，则知妻妾之贤淑。
  时为花实，为子息，方知嗣续之所归。
  法分月气深浅，得令不得令。
  年时露出财官，须要身旺；如身衰财旺，但多反破财伤妻。
  身旺财多财亦旺，财多称意。
  若无财官，次看印绶得何局式，吉凶断之。
  学者不可拘执，而不知通变也。

- **规范化释义（primary_lang_explained）**：
  论命之法，首先排定八字，确立以日干为主的分析核心。
  年柱为根，代表祖上基业与财产，可推知世运的盛衰；
  月柱为苗，代表父母宫，可推知能否得到长辈荫庇；
  日干代表命主自己，日支为配偶宫（妻妾），可推知配偶是否贤淑；
  时柱为花实（果实），代表子女宫，可推知子嗣后代的归宿。
  分析法则首重月令气机的深浅，判断日主是否得令。
  若年时两柱透出财星官星，必须日主身旺方能胜任；若身衰而财旺，反而主破财伤妻。
  唯有身旺且财多财旺，方能称心如意。
  倘若八字无财官，则次看印绶成何格局，以此推断吉凶。
  学习命理者不可拘泥执着，必须懂得通权达变。

- **完整对等诠释（secondary_lang_full）**：
  **Method of Fate Analysis**:
  The framework of the Five Elements requires first arranging the Eight Characters, taking the Day Stem as the primary master (Day Master).
  - **Year Pillar** serves as the **root**, representing ancestral property and the rise/fall of generational fortune.
  - **Month Pillar** serves as the **sprout**, representing parents, indicating the presence or absence of parental protection.
  - **Day Stem** represents the **self**; **Day Branch** represents the **spouse/concubine**, revealing their virtue or lack thereof.
  - **Hour Pillar** serves as the **flower/fruit**, representing children, indicating the destiny of descendants.
  The method distinguishes the depth of Monthly Qi—whether the Day Master is **in command** (Commanding Season) or out of command.
  If Wealth and Officer stars appear in the Year or Hour pillars, the **Self must be strong**; if the Self is weak while Wealth is prosperous, it conversely indicates financial loss and harm to the spouse.
  Only when the **Self is strong** and Wealth is abundant/prosperous can one achieve satisfaction.
  If there are no Wealth or Officer stars, next examine what pattern the **Seal/Ribbon** forms to determine fortune or misfortune.
  Scholars must not be rigid but understand how to adapt to changes.

- **核心要点**：
  - **四柱定位**：年根（祖）、月苗（父母）、日花（身/偶）、时果（子息）
  - **首重月令**：判断气机深浅与得令与否
  - **身财平衡**：财官露需身旺，身衰财旺反受其害
  - **无财看印**：无财官时取印绶成格论吉凶

- **详细解说**：  《看命入式》是子平法入门的总纲，确立了"以日为主"的核心原则和"根苗花果"的宫位象义。"年为根"象征祖上基业与世运盛衰；"月为苗"代表父母宫与亲荫有无；"日干为己身，日支为妻妾"确立了日柱的双重功能；"时为花实"则代表子息与后代归宿。在分析法则上，"法分月气深浅，得令不得令"强调月令为判断日主旺衰的关键。更重要的是"身财平衡"观念："年时露出财官，须要身旺"——财官虽好，若身弱不能胜任，反为祸患（破财伤妻）。"若无财官，次看印绶"则展示了取用的灵活性。末句"学者不可拘执，而不知通变也"更是点睛之笔，强调论命需通权达变。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_600]` `[trigger: 日干为主]` `[factor_trigger: rigan_weizhu AND lunming_hexin]` `[role: 主干]` 凡看命排下八字，以日干为主；日干为论命核心。 → 《渊海子平·看命入式》
  - `[ns_yhzp_601]` `[trigger: 根苗花果]` `[factor_trigger: sizhu_gongwei AND gen_miao_hua_guo AND gen]` `[role: 主干依赖]` 取年为根，取月为苗，日干为己身，时为花实；四柱宫位定义。 → 《渊海子平·看命入式》
  - `[ns_yhzp_602]` `[trigger: 月气深浅]` `[factor_trigger: yueqi_shenqian AND deling_budeling]` `[role: 条件分支]` 法分月气深浅，得令不得令；月令判断日主旺衰。 → 《渊海子平·看命入式》
  - `[ns_yhzp_603]` `[trigger: 身旺财官]` `[factor_trigger: shenwang AND caiguan_shengren]` `[role: 条件分支]` 年时露出财官，须要身旺；身旺方能胜任财官。 → 《渊海子平·看命入式》
  - `[ns_yhzp_604]` `[trigger: 身衰财旺凶]` `[factor_trigger: shenruo_caiwang AND pocai_shangqi]` `[role: 例外处理]` 如身衰财旺，但多反破财伤妻；身弱财旺反受其害。 → 《渊海子平·看命入式》
  - `[ns_yhzp_605]` `[trigger: 无财看印]` `[factor_trigger: wucaiguan AND qu_yinshou AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 若无财官，次看印绶得何局式；无财官时取印绶成格。 → 《渊海子平·看命入式》
  - `[ns_yhzp_606]` `[trigger: 通变不拘]` `[factor_trigger: tongquan_dabian AND lunming_linghuoxing]` `[role: 总结]` 学者不可拘执，而不知通变也；论命需通权达变。 → 《渊海子平·看命入式》

- **校勘与字词辨析**：
  - **五行提纲**：指论命的总纲领。
  - **花实**：意指花与果实，比喻子嗣结果。"""
    normalized_text_zh: str = """"""
    subject: str = "看命入式"
    factor_refs: list = ['fate_analysis_method', 'four_pillars_metaphor', 'commanding_season', 'self_wealth_balance']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_看命入式_001_L1",
    )
    version: str = "1.0.0"
