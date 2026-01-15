"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997289
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
    semantic_id="dts_v1.0.0_上下贵乎情协_002",
    book_id="dts",
    engine_id="bazi"
)
class 上下贵乎情协(SemanticEntry):
    """
    - **原文（source_text）**：
  始其所始，终其所终，富贵福寿，永乎无穷。

 - 原注（原文注解）：
 　　年月为始，日时不反悖之，日时为终，年月不妒忌之。
 　　凡局中所之神，本于...
    """
    
    original_text: str = """- **原文（source_text）**：
  始其所始，终其所终，富贵福寿，永乎无穷。

 - 原注（原文注解）：
 　　年月为始，日时不反悖之，日时为终，年月不妒忌之。
 　　凡局中所之神，本于年支，有所渊源，引于时支，有所归者，皆为始终得所，则富贵福寿，永乎无穷矣。

 - 分字分词释义：
  - 始/终：发端与归宿（年月为始，日时为终）。
  - 反悖/妒忌：上下相反相妒，皆为不美.

 - **规范化释义（primary_lang_explained）**：
  命局贵在始终有序：由年起、归于时；上下不相悖、不相妒，事功方可久长.
- **次语种完整诠释（secondary_lang_full）**:  
  A chart's beginning and end must align in order to achieve lasting prosperity and good fortune. The year and month represent the starting point, while the day and hour represent the conclusion. If the day and hour do not contradict the year and month, and the year and month do not envy the day and hour, then the chart is considered to be in harmony. This harmony is essential for achieving wealth, honour, blessings, and longevity that can last forever.

- **核心要点**：
  - 年月为始、日时为终，始终有序则命局稳固；
  - 上下不反悖、不妒忌，路径通畅则事功久长；
  - 富贵福寿的持续，取决于始终关系是否连贯、无断裂.

- **详细解说**：
  此条强调命局的"路径视角"：从年月到日时，如同一段故事从开端到结局。年月为渊源、背景与起点，日时为落实、归宿与终局。若日时不反悖年月，年月不妒忌日时，则整条路径顺畅，福禄得以延续。

  断命时，应将四柱视作一条发展路径，看其是否首尾呼应、中途无断裂与强烈冲害。很多命局的"虎头蛇尾"或"中途反复"，正是因为始终关系不顺、年时相悖所致.

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_166]` `[trigger: 年月日时首尾呼应无反悖]` `[factor_trigger: shizhong_youxu_coherent]` `[role: 主干]` 始其所始、终其所终，命局首尾呼应者，多主福禄延续、事功久长. → 《滴天髓·地支论》#始终有序
  - `[ns_dts_167]` `[trigger: 年时之间无冲害刑妒]` `[factor_trigger: nianshi_harmony]` `[role: 主干依赖]` 年时不相悖妒，路径通畅，往往应在事业家庭的长期稳定与顺遂. → 《滴天髓·地支论》#始终有序
  - `[ns_dts_168]` `[trigger: 年时相冲相害]` `[factor_trigger: nianshi_clash_risk]` `[role: 条件分支]` 年时相冲相害、始终相悖者，多见虎头蛇尾、中途反复，难以善终. → 《滴天髓·地支论》#始终有序
  - `[ns_dts_169]` `[trigger: 路径断裂或反复]` `[factor_trigger: lujing_duanlie]` `[role: 例外处理]` 始终路径断裂或反复者，须另觅贵人或调解之神以弥合首尾. → 《滴天髓·地支论》#始终有序
  - `[ns_dts_170]` `[trigger: 始终有序总则]` `[factor_trigger: shizhong_youxu_rule]` `[role: 总结]` 始其所始、终其所终，始终有序则福禄久长，始终相悖则反复难安. → 《滴天髓·地支论》#始终有序"""
    normalized_text_zh: str = """"""
    subject: str = "上下贵乎情协."
    factor_refs: list = ['shizhong_youxu', 'fanbei', 'duji', 'mingju_path', 'path_integrity']
    
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
        l1_anchor="dts_v1.0.0_上下贵乎情协_002_L1",
    )
    version: str = "1.0.0"
