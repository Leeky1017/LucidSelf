"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558977
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
    semantic_id="yhzp_v1.0.0_论比肩劫财_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论比肩劫财(SemanticEntry):
    """
    - **原文（source_text）**：比肩者，同我之神也，阴见阴，阳见阳。劫财者，阴见阳，阳见阴，同为同类。比肩主克父、克妻、争财、兄弟不和。劫财主克父、克妻、破财、兄弟姐妹争夺。比肩劫财皆不利...
    """
    
    original_text: str = """- **原文（source_text）**：比肩者，同我之神也，阴见阴，阳见阳。劫财者，阴见阳，阳见阴，同为同类。比肩主克父、克妻、争财、兄弟不和。劫财主克父、克妻、破财、兄弟姐妹争夺。比肩劫财皆不利财星、不利六亲，但利身旺。身弱喜比劫帮身，身旺则比劫争财为祸。

- **分字分词释义**：
  - **比肩**：同类且阴阳相同者，如甲木见甲木。
  - **劫财**：同类且阴阳相异者，如甲木见乙木。
  - **同我之神**：与日主同五行的十神，帮扶日主。
  - **克父克妻**：比劫克财，财为父为妻，故有克父克妻之象。
  - **争财**：比劫与日主争夺财星，破坏财运。
  - **兄弟不和**：比劫代表兄弟姐妹，多则争斗不和。
  - **利身旺**：比劫帮身，使日主旺相有力。
  - **比劫争财为祸**：身旺时比劫不需帮身，反与日主争财为祸。

- **规范化释义（primary_lang_explained）**：比肩是同类且阴阳相同者，劫财是同类且阴阳相异者。比肩劫财主克父克妻、兄弟不和、争财破财。身弱喜比劫帮身，身旺忌比劫争财。比劫多者兄弟姐妹多但多争斗，不利财星婚姻。

- **完整对等诠释（secondary_lang_full）**：Shoulder/Parallel is same-category with same polarity; Rob Wealth is same-category with opposite polarity. Shoulder and Rob Wealth indicate harming father/wife, sibling discord, competing for wealth. Weak Self favors Shoulder/Rob helping Self; strong Self taboos Shoulder/Rob competing for wealth. Abundant Shoulder/Rob brings many siblings but much strife, unfavorable for Wealth Star and marriage.

- **核心要点**：
  - 比肩是同类且阴阳相同，劫财是同类且阴阳相异
  - 比劫为同我之神，帮扶日主
  - 比劫主克父、克妻、争财、兄弟不和
  - 身弱喜比劫帮身，身旺忌比劫争财
  - 比劫皆不利财星、不利六亲

- **详细解说**：  
  本条论述比肩与劫财的性质与两面性。比肩是同类且阴阳相同者（如甲木见甲木），劫财是同类且阴阳相异者（如甲木见乙木），两者都是"同我之神"——与日主同五行。比劫的凶象是"克父、克妻、争财、兄弟不和"——比劫克财，财为父为妻，故克父克妻；比劫与日主同类，争夺财星，故争财；比劫代表兄弟姐妹，多则争斗不和。但比劫有两面性："身弱喜比劫帮身"——日主弱时需要比劫帮扶增强力量；"身旺则比劫争财为祸"——日主已旺不需帮扶，比劫反与日主争财为患。故比劫的吉凶取决于日主强弱。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_105]` `[trigger: 比肩定义]` `[factor_trigger: parallel AND parallel_heavy]` `[role: 主干]` 比肩者，同我之神也，阴见阴，阳见阳。 → 《渊海子平·论比肩劫财》
  - `[ns_yhzp_106]` `[trigger: 劫财定义]` `[factor_trigger: rob_wealth]` `[role: 主干]` 劫财者，阴见阳，阳见阴，同为同类。 → 《渊海子平·论比肩劫财》
  - `[ns_yhzp_107]` `[trigger: 比肩凶象]` `[factor_trigger: parallel AND direct_wealth]` `[role: 主干依赖]` 比肩主克父、克妻、争财、兄弟不和。 → 《渊海子平·论比肩劫财》
  - `[ns_yhzp_108]` `[trigger: 劫财凶象]` `[factor_trigger: rob_wealth AND direct_wealth]` `[role: 主干依赖]` 劫财主克父、克妻、破财、兄弟姐妹争夺。 → 《渊海子平·论比肩劫财》
  - `[ns_yhzp_109]` `[trigger: 比劫不利]` `[factor_trigger: parallel AND rob_wealth]` `[role: 条件分支]` 比肩劫财皆不利财星、不利六亲，但利身旺。 → 《渊海子平·论比肩劫财》
  - `[ns_yhzp_110]` `[trigger: 身弱喜比劫]` `[factor_trigger: parallel AND rob_wealth AND day_master_strength]` `[role: 条件分支]` 身弱喜比劫帮身。 → 《渊海子平·论比肩劫财》
  - `[ns_yhzp_111]` `[trigger: 身旺忌比劫]` `[factor_trigger: parallel AND rob_wealth AND day_master_strength]` `[role: 例外处理]` 身旺则比劫争财为祸。 → 《渊海子平·论比肩劫财》"""
    normalized_text_zh: str = """"""
    subject: str = "论比肩劫财"
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论比肩劫财_001_L1",
    )
    version: str = "1.0.0"
