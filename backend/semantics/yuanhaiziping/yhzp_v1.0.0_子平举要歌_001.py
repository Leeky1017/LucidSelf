"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559284
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
    semantic_id="yhzp_v1.0.0_子平举要歌_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 子平举要歌(SemanticEntry):
    """
    - **原文（source_text）**：造化先须详日主，坐官坐印衰旺取；天时月令号提纲，元有元无旺重举。大抵官星要纯粹，正偏杂乱反无情；露官藏杀方为福，露杀藏官是祸胎。

- **分字分词释义**...
    """
    
    original_text: str = """- **原文（source_text）**：造化先须详日主，坐官坐印衰旺取；天时月令号提纲，元有元无旺重举。大抵官星要纯粹，正偏杂乱反无情；露官藏杀方为福，露杀藏官是祸胎。

- **分字分词释义**：
  - **造化先须详日主**：论命首先要详细分析日主（日干）的强弱。
  - **坐官坐印衰旺取**：根据日主所坐的官星或印绶来判断日主的衰旺。
  - **天时月令号提纲**：月令（月支）为四柱提纲，决定格局与用神。
  - **元有元无旺重举**：月令中有无某十神、该十神旺衰如何，需逐一考量。
  - **官星要纯粹**：官星以纯正单一为佳，忌官杀混杂。
  - **正偏杂乱反无情**：正官与七杀混杂，则格局不清，反为无情凶象。
  - **露官藏杀方为福**：天干透官星而地支藏七杀，官杀不混，为吉配。
  - **露杀藏官是祸胎**：天干透七杀而地支藏官星，杀先官后，为凶配。

- **规范化释义（primary_lang_explained）**：论命首看日主强弱与月令提纲。官星要纯粹不杂，露官藏杀为福，露杀藏官为祸。官杀混杂则取财，官旺忌刑冲，官轻喜财。伤官用财为福，贪合忘官/杀各有宜忌。

- **完整对等诠释（secondary_lang_full）**：Fate analysis begins with Day Master strength and Month Command. Officer Star requires purity without mixture—exposed Officer with hidden Killing brings fortune, exposed Killing with hidden Officer brings calamity. Officer-Killing mixed取Wealth; prosperous Officer fears punishments, weak Officer favors Wealth. Injuring Officer using Wealth brings fortune; greedy combination forgetting Officer/Killing each has proper applications.

- **核心要点**：日主为先月令提纲；官星要纯粹；露官藏杀吉露杀藏官凶；官杀混杂取财；伤官用财为福

- **详细解说**：  《子平举要歌》是子平法论命的核心纲要，以歌诀形式总结论命要点。"造化先须详日主"开篇点明论命的第一步：分析日主强弱。"天时月令号提纲"则强调月令为四柱提纲，决定格局成败与用神取舍。在官杀配置上，本篇提出"官星要纯粹"的核心原则：正官与七杀不宜同见，"正偏杂乱反无情"。更进一步区分"露官藏杀"与"露杀藏官"的吉凶差异：前者天干见官、地支藏杀，官为主杀为辅，主福；后者天干见杀、地支藏官，杀先官后，主祸。这一"露藏"理论是子平法判断官杀格局的精髓所在。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_285]` `[trigger: 造化详日主]` `[factor_trigger: lunming AND rizhu_xiangqiang AND zuoguan_zuoyin AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干]` 造化先须详日主，坐官坐印衰旺取；论命首看日主强弱。 → 《渊海子平·子平举要歌》
  - `[ns_yhzp_286]` `[trigger: 月令提纲]` `[factor_trigger: yueling AND tigang AND geju_yongshen AND geju]` `[role: 主干依赖]` 天时月令号提纲，元有元无旺重举；月令决定格局用神。 → 《渊海子平·子平举要歌》
  - `[ns_yhzp_287]` `[trigger: 官星纯粹]` `[factor_trigger: guanxing_chuncui AND guansha_ji_hunza]` `[role: 条件分支]` 大抵官星要纯粹，正偏杂乱反无情；官杀忌混杂。 → 《渊海子平·子平举要歌》
  - `[ns_yhzp_288]` `[trigger: 露官藏杀]` `[factor_trigger: luguan_cangsha AND ji]` `[role: 条件分支]` 露官藏杀方为福；天干透官地支藏杀为吉配。 → 《渊海子平·子平举要歌》
  - `[ns_yhzp_289]` `[trigger: 露杀藏官]` `[factor_trigger: lusha_cangguan AND xiong]` `[role: 例外处理]` 露杀藏官是祸胎；天干透杀地支藏官为凶配。 → 《渊海子平·子平举要歌》
  - `[ns_yhzp_290]` `[trigger: 子平举要纲领]` `[factor_trigger: ziping_juyao AND rizhu_yueling AND gangling]` `[role: 总结]` 子平举要歌以日主月令为纲，官星纯粹露藏有序为论命核心要诀。 → 《渊海子平·子平举要歌》

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 日主 | Day Master | 四柱日干代表命主本人 | Day Stem represents fate owner | day_master | existing |
| 月令提纲 | Month Command | 月支为命局提纲最重要 | Month Branch as most important pillar element | month_command | existing |
| 露官藏杀 | Exposed Officer Hidden Killing | 天干见官地支藏杀为吉 | Heavenly Stem shows Officer while Earthly Branch hides Killing | exposed_officer_hidden_killing | existing |
| 官杀混杂 | Officer-Killing Mixed | 官星七杀同时显露为忌 | Officer and Seven Killings both exposed as taboo | officer_killing_mixed | existing |"""
    normalized_text_zh: str = """"""
    subject: str = "子平举要歌"
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
        l1_anchor="yhzp_v1.0.0_子平举要歌_001_L1",
    )
    version: str = "1.0.0"
