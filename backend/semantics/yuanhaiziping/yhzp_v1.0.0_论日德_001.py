"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559086
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
    semantic_id="yhzp_v1.0.0_论日德_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论日德(SemanticEntry):
    """
    - **原文（source_text）**：
  日德有五：甲寅、戊辰、丙辰、庚辰、壬戌日是也。其福要多，而忌刑冲破害，恶官星，憎财旺。加临会合，但空亡而忌魁罡。大抵日德，主人性格慈善。日德俱多，福必...
    """
    
    original_text: str = """- **原文（source_text）**：
  日德有五：甲寅、戊辰、丙辰、庚辰、壬戌日是也。其福要多，而忌刑冲破害，恶官星，憎财旺。加临会合，但空亡而忌魁罡。大抵日德，主人性格慈善。日德俱多，福必丰厚，运行身旺，大是奇绝。若旺气已衰，运至魁罡，其死必矣！若有财官加临，别寻他格，正能免非横之祸。

- **分字分词释义**：
  - **日德**：日柱坐德的特殊日子，共五日。
  - **甲寅戊辰丙辰庚辰壬戌**：五个日德日。
  - **福要多**：日德需要福德聚集才能发挥作用。
  - **忌刑冲破害**：日德与日贵一样忌地支四凶。
  - **恶官星憎财旺**：日德忌见官杀和财旺。
  - **空亡而忌魁罡**：日德怕空亡，尤其忌魁罡（辰戌）。
  - **性格慈善**：日德之人的典型性格。
  - **运至魁罡其死必矣**：大运遇魁罡主大凶。

- **规范化释义（primary_lang_explained）**：
  日德有甲寅戊辰丙辰庚辰壬戌五日。日德其福要多，忌刑冲破害，恶官星憎财旺，但空亡忌魁罡。日德主人性格慈善，日德俱多福必丰厚，运行身旺大是奇绝。若旺气已衰运至魁罡其死必矣。若有财官加临别寻他格能免非横之祸。

- **完整对等诠释（secondary_lang_full）**：
  Day Virtue has five days: Jia-Yin, Wu-Chen, Bing-Chen, Geng-Chen, Ren-Xu. Day Virtue needs abundant fortune, yet taboos Punishments, Clashes, Breakages, and Harms; it dislikes Officer Star and detests vigorous Wealth. Additionally meeting combinations, it fears Void-Extinction and especially taboos Kuigang. Generally, Day Virtue owners have benevolent, charitable natures. When Day Virtue occurs abundantly, fortune is certainly substantial; if fortune-running passes through Self-strong regions, it is extraordinarily wonderful. If vigor has already declined and fortune arrives at Kuigang, death is certain! If Wealth and Officer are additionally present, seek another pattern separately; this properly avoids unnatural disasters.

- **核心要点**：
  - 日德有甲寅、戊辰、丙辰、庚辰、壬戌五日
  - 日德其福要多，忌刑冲破害
  - 日德恶官星、憎财旺
  - 日德忌空亡、尤忌魁罡
  - 日德主人性格慈善
  - 运至魁罡主大凶

- **详细解说**：
  本条论述日德的性质与禁忌。日德是日柱坐德的特殊日子，"有五：甲寅、戊辰、丙辰、庚辰、壬戌"。日德的特点是"其福要多"——需要福德聚集才能发挥作用。日德的禁忌与日贵相似："忌刑冲破害"、"但空亡而忌魁罡"——尤其忌魁罡（辰戌）因为日德多为辰日。更特殊的是"恶官星，憎财旺"——日德忌见官杀和财星，与一般格局喜财官不同。日德之人"性格慈善"，与日贵的"仁德"相类。"日德俱多，福必丰厚"——日德多见主福厚。但"若旺气已衰，运至魁罡，其死必矣"——大运遇魁罡是日德的大忌。"若有财官加临，别寻他格"——如果有财官则按财官格论，不必拘泥日德格。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_133]` `[trigger: 日德定义]` `[factor_trigger: day_virtue]` `[role: 主干]` 日德有五：甲寅、戊辰、丙辰、庚辰、壬戌日是也。 → 《渊海子平·论日德》
  - `[ns_yhzp_134]` `[trigger: 日德禁忌]` `[factor_trigger: day_virtue AND punishment]` `[role: 主干依赖]` 其福要多，而忌刑冲破害，恶官星，憎财旺。 → 《渊海子平·论日德》
  - `[ns_yhzp_135]` `[trigger: 日德忌魁罡]` `[factor_trigger: day_virtue AND kuigang]` `[role: 条件分支]` 加临会合，但空亡而忌魁罡。 → 《渊海子平·论日德》
  - `[ns_yhzp_136]` `[trigger: 日德性格]` `[factor_trigger: day_virtue AND cishan_xingge]` `[role: 条件分支]` 大抵日德，主人性格慈善。 → 《渊海子平·论日德》
  - `[ns_yhzp_137]` `[trigger: 日德福厚]` `[factor_trigger: day_virtue AND day_master_strength]` `[role: 条件分支]` 日德俱多，福必丰厚，运行身旺，大是奇绝。 → 《渊海子平·论日德》
  - `[ns_yhzp_138]` `[trigger: 日德运魁罡]` `[factor_trigger: pattern_fortune_arrives_kuigang_proposal]` `[role: 例外处理]` 若旺气已衰，运至魁罡，其死必矣！ → 《渊海子平·论日德》
  - `[ns_yhzp_139]` `[trigger: 日德别格]` `[factor_trigger: day_virtue AND direct_wealth AND direct_officer]` `[role: 总结]` 若有财官加临，别寻他格，正能免非横之祸。 → 《渊海子平·论日德》"""
    normalized_text_zh: str = """"""
    subject: str = "论日德"
    factor_refs: list = ['day_virtue', 'pattern_fortune_arrives_kuigang_proposal']
    
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
        l1_anchor="yhzp_v1.0.0_论日德_001_L1",
    )
    version: str = "1.0.0"
