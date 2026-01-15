"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559097
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
    semantic_id="yhzp_v1.0.0_论魁罡_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论魁罡(SemanticEntry):
    """
    - **原文（source_text）**：
  魁罡有庚辰、庚戌、壬辰、戊戌四日是也。魁罡者，辰为天罡，戌为河魁，乃阴阳灭没之地，故名。其日，有纯一而贵者，有重犯而贵者。大抵主为人性格聪明，文章振发...
    """
    
    original_text: str = """- **原文（source_text）**：
  魁罡有庚辰、庚戌、壬辰、戊戌四日是也。魁罡者，辰为天罡，戌为河魁，乃阴阳灭没之地，故名。其日，有纯一而贵者，有重犯而贵者。大抵主为人性格聪明，文章振发，临事有断。惟不利于处世立身，与人寡合。运行身旺，发福百端，一见财官，祸患立至。若魁罡重叠而有情，主贵极。

- **分字分词释义**：
  - **魁罡**：辰戌为魁罡，庚辰庚戌壬辰戊戌四日为魁罡日。
  - **辰为天罡戌为河魁**：天罡地煞之说，辰戌为阴阳灭没之地。
  - **纯一而贵**：魁罡单见主贵。
  - **重犯而贵**：魁罡重叠亦主贵。
  - **聪明文章振发**：魁罡主人聪明，文采斐然。
  - **临事有断**：处事果决有判断力。
  - **与人寡合**：性格孤傲，与人难合。
  - **一见财官祸患立至**：魁罡最忌财官，见之立刻生祸。

- **规范化释义（primary_lang_explained）**：
  魁罡有庚辰庚戌壬辰戊戌四日。辰为天罡戌为河魁，乃阴阳灭没之地。魁罡有纯一而贵者，有重犯而贵者。魁罡主人聪明文章振发临事有断，惟与人寡合。运行身旺发福百端，一见财官祸患立至。魁罡重叠而有情主贵极。

- **完整对等诠释（secondary_lang_full）**：
  Kuigang has four days: Geng-Chen, Geng-Xu, Ren-Chen, Wu-Xu. Chen is Tiangang (Heavenly Barrier), Xu is Hekui (River Chief), being places where Yin-Yang extinguishes, hence the name. Such days include those noble through singularity and those noble through repetition. Generally, owners have intelligent, bright natures, flourishing literary ability, and decisive judgment in affairs. However, they are disadvantaged in worldly conduct and personal establishment, being difficult to get along with others. When fortune-running passes through Self-strong regions, fortune emerges in countless ways; once Wealth or Officer appears, disaster arrives immediately. If Kuigang overlaps with affinity, it indicates extreme nobility.

- **核心要点**：
  - 魁罡有庚辰、庚戌、壬辰、戊戌四日
  - 辰为天罡戌为河魁，阴阳灭没之地
  - 魁罡有纯一而贵、重犯而贵两种
  - 魁罡主聪明文章振发临事有断
  - 魁罡与人寡合，性格孤傲
  - 魁罡最忌财官，运行身旺发福

- **详细解说**：
  本条论述魁罡的性质与特点。魁罡日有四："庚辰、庚戌、壬辰、戊戌"。名称来源是"辰为天罡，戌为河魁，乃阴阳灭没之地"——天罡地煞之说，辰戌为阴阳交替之际。魁罡成格有两种情况："有纯一而贵者，有重犯而贵者"——单见和重叠都可成格。魁罡之人的性格特点是"聪明，文章振发，临事有断"——才智聪颖、文采斐然、决断有力。但"不利于处世立身，与人寡合"——性格孤傲，人际关系差。魁罡的行运禁忌是"运行身旺，发福百端，一见财官，祸患立至"——喜身旺运，最忌财官。"魁罡重叠而有情，主贵极"——魁罡多见反主大贵，这与一般神煞怕重叠不同。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_140]` `[trigger: 魁罡定义]` `[factor_trigger: kuigang]` `[role: 主干]` 魁罡有庚辰、庚戌、壬辰、戊戌四日是也。 → 《渊海子平·论魁罡》
  - `[ns_yhzp_141]` `[trigger: 魁罡名由]` `[factor_trigger: kuigang]` `[role: 主干依赖]` 魁罡者，辰为天罡，戌为河魁，乃阴阳灭没之地，故名。 → 《渊海子平·论魁罡》
  - `[ns_yhzp_142]` `[trigger: 魁罡成格]` `[factor_trigger: pattern_kuigang_overlapping_proposal AND pattern_kuigang_overlapping]` `[role: 条件分支]` 其日，有纯一而贵者，有重犯而贵者。 → 《渊海子平·论魁罡》
  - `[ns_yhzp_143]` `[trigger: 魁罡性格]` `[factor_trigger: kuigang]` `[role: 条件分支]` 大抵主为人性格聪明，文章振发，临事有断。 → 《渊海子平·论魁罡》
  - `[ns_yhzp_144]` `[trigger: 魁罡寡合]` `[factor_trigger: kuigang AND congming_guhe]` `[role: 例外处理]` 惟不利于处世立身，与人寡合。 → 《渊海子平·论魁罡》
  - `[ns_yhzp_145]` `[trigger: 魁罡喜忌]` `[factor_trigger: kuigang AND direct_wealth AND direct_officer]` `[role: 条件分支]` 运行身旺，发福百端，一见财官，祸患立至。 → 《渊海子平·论魁罡》
  - `[ns_yhzp_146]` `[trigger: 魁罡重叠]` `[factor_trigger: pattern_kuigang_overlapping_proposal]` `[role: 总结]` 若魁罡重叠而有情，主贵极。 → 《渊海子平·论魁罡》"""
    normalized_text_zh: str = """"""
    subject: str = "论魁罡"
    factor_refs: list = ['kuigang', 'pattern_kuigang_overlapping_proposal']
    
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
        l1_anchor="yhzp_v1.0.0_论魁罡_001_L1",
    )
    version: str = "1.0.0"
