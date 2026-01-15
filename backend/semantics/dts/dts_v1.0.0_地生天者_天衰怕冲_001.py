"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997260
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
    semantic_id="dts_v1.0.0_地生天者_天衰怕冲_001",
    book_id="dts",
    engine_id="bazi"
)
class 地生天者天衰怕冲(SemanticEntry):
    """
    - **原文（source_text）**：
  地生天者，天衰怕冲。

- 原注（原文注解）：
  　　如甲子，丙寅，丁卯，己巳，皆支生日，如日主衰弱，而支逄冲，则根拔矣。

- 分字分词释义：
 ...
    """
    
    original_text: str = """- **原文（source_text）**：
  地生天者，天衰怕冲。

- 原注（原文注解）：
  　　如甲子，丙寅，丁卯，己巳，皆支生日，如日主衰弱，而支逄冲，则根拔矣。

- 分字分词释义：
  - 地生天：地支所含之神生天干。
  - 天衰：天干本身衰弱。
  - 怕冲：忌再遭冲动拔根。

- **规范化释义（primary_lang_explained）**：
  当地支生天干而天干自衰，若再被冲，根拔而难立。

- **次语种完整诠释（secondary_lang_full）**:  
  When the earth branch is the only root that gives life to a weakened heavenly stem, the whole pattern depends on that single support. If the branch that feeds the stem is then struck by a clash, the root is pulled and the stem cannot stand. This configuration therefore marks a high‑risk dependency: as long as the root branch is stable, the chart can function, but once that place is disturbed the loss is sudden and hard to repair. The correct attitude is to recognise where the true root lies, protect it from direct clashes, and where possible create secondary supports, so that a weak heaven is not left hanging from one fragile point.

- **核心要点**：
  - 地支为天干之根，天干衰弱时此根尤为关键；
  - 根位一旦遭冲，衰弱之天干失去唯一支撑，如树根被拔；
  - 处此局者宜护根、分散依赖，勿将全部生命重心系于一处.

- **详细解说**：
  地生天而天衰之局，就像一个人本身气力不足，却勉强依托某一处根基维持生机：可能是唯一的资源来源、唯一的关系支点或唯一的地位根基.平时看似还能勉强运转，一旦这处根位受伤或被冲击，整体便迅速失衡，难以支撑.

  因此古书说"天衰怕冲"：怕的不是一般之冲，而是冲在唯一的根位上.断此条时，要先找出天干真正的根在何处，再看该根是否稳固、是否有辅根、行运是否直冲此处.应对之道，在于提前加固根基或另立支撑，使生命结构不至于单点失守.

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_088]` `[trigger: 命局地生天且天干自衰]` `[factor_trigger: dizhi_root_supports_tiangan_pattern & tiangan_intrinsic_strength=弱]` `[role: 主干]` 地生天而天干自衰，多主命局高度依赖某一根位，平时须自觉识别并珍惜此处支撑. → 《滴天髓·地支论》#地生天者天衰怕冲
  - `[ns_dts_089]` `[trigger: 天衰地生天行运恰逢根位被冲]` `[factor_trigger: root_clash_risk_flag=on]` `[role: 主干依赖]` 天衰地生天而行运冲破根支，常见原有依托突然动摇或中断，易有“根拔难立”之感. → 《滴天髓·地支论》#地生天者天衰怕冲
  - `[ns_dts_090]` `[trigger: 天衰地生天另有辅根或调解之神]` `[factor_trigger: root_protection_strategy=补根/通关]` `[role: 条件分支]` 若天衰地生天而同时有辅根或调解之神，纵有冲动根位，其凶亦可缓解为波折调整，而非全盘崩塌. → 《滴天髓·地支论》#地生天者天衰怕冲
  - `[ns_dts_155]` `[trigger: 根位无辅被冲]` `[factor_trigger: root_clash_risk_flag=on & root_removal_consequence=严重]` `[role: 例外处理]` 天衰地生天而唯一根位被冲无辅，根拔则天无所依，凶象骤至. → 《滴天髓·地支论》#地生天者天衰怕冲
  - `[ns_dts_156]` `[trigger: 护根总则]` `[factor_trigger: root_protection_strategy]` `[role: 总结]` 地生天而天衰，护根为第一要务，根稳则天安，根动则天摇. → 《滴天髓·地支论》#地生天者天衰怕冲"""
    normalized_text_zh: str = """"""
    subject: str = "地生天者，天衰怕冲."
    factor_refs: list = ['dishengtian', 'tianshuai', 'pachong', 'genba', 'muzi', 'shigen']
    
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
        l1_anchor="dts_v1.0.0_地生天者_天衰怕冲_001_L1",
    )
    version: str = "1.0.0"
