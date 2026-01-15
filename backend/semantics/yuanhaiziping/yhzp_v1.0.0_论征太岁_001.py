"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558736
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
    semantic_id="yhzp_v1.0.0_论征太岁_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论征太岁(SemanticEntry):
    """
    - **原文（source_text）**：征者，战也；如臣触其君，乃下犯上之意。日干支冲克太岁曰征，运支干伤冲太岁亦曰征，太岁干支冲日干支者亦曰征；但看八字有无救助。日干支合太岁干支曰晦，岁运合岁干...
    """
    
    original_text: str = """- **原文（source_text）**：征者，战也；如臣触其君，乃下犯上之意。日干支冲克太岁曰征，运支干伤冲太岁亦曰征，太岁干支冲日干支者亦曰征；但看八字有无救助。日干支合太岁干支曰晦，岁运合岁干亦然；遇此者主晦气，一年反复、欲速不达。

- **分字分词释义**：
  - **征**：征战、攻伐，指日干支与太岁之间的冲克关系，如臣触犯君王。
  - **冲**：地支相对位置的冲突，如子午冲、卯酉冲，力量对峙激烈。
  - **克**：五行相克，如木克土、土克水，为制约关系。
  - **晦**：晦暗不明，指日干支与太岁相合反而形成晦气，事事不顺。
  - **救助**：命中有化解冲克的五行配置，可转凶为吉。
  - **反复**：事情反反复复，难以顺遂推进。
  - **欲速不达**：想快反而达不到目的，形容晦气年的特征。

- **规范化释义（primary_lang_explained）**：征即战斗。日干支冲克太岁为征，大运冲克太岁亦为征，太岁冲日干支也为征，需看命中有无救应。日干支合太岁为"晦"，主晦气，一年反复不顺。

- **完整对等诠释（secondary_lang_full）**：Zheng means combat/warfare. Day Stem-Branch clashing/controlling Tai Sui constitutes Zheng; Major Cycle clashing Tai Sui also constitutes Zheng; Tai Sui clashing Day Stem-Branch equally constitutes Zheng—examine natal chart for rescue. Day Stem-Branch combining Tai Sui creates Hui (dimness), bringing obscurity and yearly reversals.

- **核心要点**：
  - 征即战斗，日干支与太岁冲克为征
  - 大运冲克太岁亦为征
  - 太岁冲克日干支也为征
  - 日干支合太岁为"晦"，主晦气反复
  - 征太岁需看命中有无救助

- **详细解说**：  
  本条承上条"论太岁吉凶"，进一步细化"征太岁"的概念。"征"字取征战之意，形容日干支与太岁之间的冲克关系如同战场上的对抗。征太岁有三种情形：一是日干支冲克太岁；二是大运干支冲克太岁；三是太岁反冲日干支。无论哪种情形，都需要看命中有无救助之神来判断最终吉凶。本条还提出"晦"的概念：当日干支与太岁相合时，反而形成晦暗不明的状态，主一年反复、欲速不达。这提示我们：太岁关系不只是冲克为凶、合为吉的简单逻辑，合而不化、合而受困同样可能带来负面影响。此条与上条合观，构成完整的太岁论断体系。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_653]` `[trigger: 征太岁定义]` `[factor_trigger: zheng_taisui_def]` `[role: 主干]` 征者，战也；如臣触其君，乃下犯上之意。 → 《渊海子平·论征太岁》
  - `[ns_yhzp_654]` `[trigger: 日干支冲太岁]` `[factor_trigger: ri_ganzhi_chong_taisui]` `[role: 主干依赖]` 日干支冲克太岁曰征。 → 《渊海子平·论征太岁》
  - `[ns_yhzp_655]` `[trigger: 大运冲太岁]` `[factor_trigger: dayun_chong_taisui]` `[role: 条件分支]` 运支干伤冲太岁亦曰征。 → 《渊海子平·论征太岁》
  - `[ns_yhzp_656]` `[trigger: 太岁冲日柱]` `[factor_trigger: taisui_chong_rizhu]` `[role: 条件分支]` 太岁干支冲日干支者亦曰征。 → 《渊海子平·论征太岁》
  - `[ns_yhzp_657]` `[trigger: 合太岁为晦]` `[factor_trigger: he_taisui_hui AND huiqi_zhuangtai]` `[role: 条件分支]` 日干支合太岁干支曰晦，主晦气，一年反复、欲速不达。 → 《渊海子平·论征太岁》
  - `[ns_yhzp_658]` `[trigger: 晦气特征]` `[factor_trigger: hui_qi_trait]` `[role: 总结]` 遇晦者主晦气，一年反复、欲速不达。 → 《渊海子平·论征太岁》"""
    normalized_text_zh: str = """"""
    subject: str = "论征太岁"
    factor_refs: list = ['new_candidate', 'new_candidate']
    
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
        l1_anchor="yhzp_v1.0.0_论征太岁_001_L1",
    )
    version: str = "1.0.0"
