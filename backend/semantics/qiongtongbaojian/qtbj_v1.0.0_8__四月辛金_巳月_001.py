"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578473
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
    semantic_id="qtbj_v1.0.0_8__四月辛金_巳月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 8四月辛金巳月(SemanticEntry):
    """
    - **原文（source_text）**：
  四月辛金，时逢首夏，忌丙火之燥烈，喜壬水之洗淘。支成金局，水透出干，有木制戊，名一清澈底，科甲功名。癸透壬藏，富真贵假。若壬癸皆藏，戊己亦藏，略富。若...
    """
    
    original_text: str = """- **原文（source_text）**：
  四月辛金，时逢首夏，忌丙火之燥烈，喜壬水之洗淘。支成金局，水透出干，有木制戊，名一清澈底，科甲功名。癸透壬藏，富真贵假。若壬癸皆藏，戊己亦藏，略富。若壬癸俱无，反见火出，必主鳏独。
  或支成火局，有制者吉，无制者凶。凡火旺无水，取土泄之。
  若壬水藏亥，戊不出干，亦主上达。有戊常人。有一甲透，衣禄可求。若有甲无壬癸者，富贵虚浮。所谓羊质虎皮是也。壬、癸、甲、三者全无，又不合格，斯为下品。

- **分字分词释义**：
  - **首夏**：夏季开始 / 巳月 / 火旺
  - **燥烈**：干燥猛烈 / 丙火特点 / 忌象
  - **洗淘**：冲洗淘涤 / 壬水作用 / 喜用
  - **一清澈底**：一片清澈见底 / 金局水透 / 格局名
  - **鳏独**：孤寡独居 / 无水见火 / 凶象
  - **上达**：上达高位 / 壬藏戊不透 / 吉象
  - **羊质虎皮**：本质是羊外皮像虎 / 有甲无水 / 虚浮
  - **下品**：下等品格 / 壬癸甲全无 / 凶象
  - **衣禄可求**：衣食俸禄可得 / 甲透 / 次吉

- **规范化释义（primary_lang_explained）**：
  四月（巳月）辛金时逢首夏忌丙火之燥烈喜壬水之洗淘。支成金局水透出干有木制戊名一清澈底科甲功名。癸透壬藏富真贵假。若壬癸皆藏戊己亦藏略富。若壬癸俱无反见火出必主鳏独。
  或支成火局有制者吉无制者凶。凡火旺无水取土泄之。
  若壬水藏亥戊不出干亦主上达。有戊常人。有一甲透衣禄可求。若有甲无壬癸者富贵虚浮。所谓羊质虎皮是也。壬癸甲三者全无又不合格斯为下品。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 4th Month (Snake Month): time meeting early-summer fear Bing Fire blazing-fierce joy Ren Water washing. Branches form Metal Frame Water revealing有Wood制Wu name one-clear-to-bottom imperial-exam fame. Gui revealing Ren hidden wealthy-true noble-false. If Ren/Gui both hidden Wu/Ji also hidden slightly wealthy. If Ren/Gui both absent conversely見Fire revealing surely main widowed-alone.
  Or branches form Fire Frame having制 auspicious without制 ominous. Generally Fire-prosperous without Water take Earth泄.
  If Ren Water hidden Hai Wu not revealing also main ascending. Having Wu ordinary. Having one Jia revealing food-clothing obtainable. If having Jia without Ren/Gui wealth-nobility虚浮. So-called sheep-essence tiger-skin. Ren/Gui/Jia three all absent also not合格 this為inferior.

- **核心要点**：
  - **首要用神**：壬水（洗淘第一）
  - **忌神**：丙火燥烈
  - **配合**：甲木制土癸水辅助

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_414]` `[trigger: 辛生巳月]` `[factor_trigger: month_si AND tiangan_xin AND tiangan_ren AND avoids_bing_blazing]` `[role: 主干]` 四月辛金，时逢首夏，忌丙火之燥烈，喜壬水之洗淘。 → 《穷通宝鉴·三夏辛金》#34.8
  - `[ns_qttbj_415]` `[trigger: 一清澈底]` `[factor_trigger: month_si AND tiangan_xin AND dizhi_metal_frame AND ren_revealed AND tiangan_jia AND one_clear_to_bottom]` `[role: 条件分支]` 支成金局，水透出干，有木制戊，名一清澈底，科甲功名。 → 《穷通宝鉴·三夏辛金》#34.8
  - `[ns_qttbj_416]` `[trigger: 壬癸俱无]` `[factor_trigger: month_si AND tiangan_xin AND NOT tiangan_ren AND NOT tiangan_gui AND element_fire_revealed]` `[role: 例外处理]` 若壬癸俱无，反见火出，必主鳏独。 → 《穷通宝鉴·三夏辛金》#34.8
  - `[ns_qttbj_417]` `[trigger: 羊质虎皮]` `[factor_trigger: month_si AND tiangan_xin AND tiangan_jia AND NOT tiangan_ren AND NOT tiangan_gui AND sheep_tiger]` `[role: 例外处理]` 若有甲无壬癸者，富贵虚浮，所谓羊质虎皮是也。 → 《穷通宝鉴·三夏辛金》#34.8"""
    normalized_text_zh: str = """"""
    subject: str = "8. 四月辛金（巳月）"
    factor_refs: list = ['status', 'one_clear_to_bottom', 'sheep_tiger']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_8__四月辛金_巳月_001_L1",
    )
    version: str = "1.0.0"
