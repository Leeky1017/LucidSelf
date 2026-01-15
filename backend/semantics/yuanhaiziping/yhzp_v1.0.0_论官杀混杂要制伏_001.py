"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558933
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
    semantic_id="yhzp_v1.0.0_论官杀混杂要制伏_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论官杀混杂要制伏(SemanticEntry):
    """
    - **原文（source_text）**：官星要纯，不要杂。假如甲木用辛金为官，若年是辛，月是酉，时上亦是辛官，虽多尽不妨，盖纯一尽好；若有庚或庚申，则混杂为杀，以伤其身。要行火乡制伏，则发福也。馀...
    """
    
    original_text: str = """- **原文（source_text）**：官星要纯，不要杂。假如甲木用辛金为官，若年是辛，月是酉，时上亦是辛官，虽多尽不妨，盖纯一尽好；若有庚或庚申，则混杂为杀，以伤其身。要行火乡制伏，则发福也。馀仿此也。

- **分字分词释义**：
  - **官杀混杂**：正官与七杀同现于命局，为格局大忌。
  - **官星要纯**：正官格要求官星纯一，不掺杂七杀。
  - **纯一尽好**：官星虽多但皆为同一性质（都是正官），反而是好的。
  - **辛金为官**：甲木日主以辛金（阴金）为正官。
  - **庚金为杀**：甲木日主以庚金（阳金）为七杀。
  - **混杂为杀**：官杀混杂时，七杀的凶性会显现伤身。
  - **行火乡**：行火运以火克金，制伏七杀。

- **规范化释义（primary_lang_explained）**：官星要纯粹不要混杂。如甲木日主用辛金为正官，若年月时都是辛金或酉金，虽多但纯一无杂反而好。若既有辛金正官又有庚金七杀，则构成官杀混杂伤害日主，需行火运制伏庚金才能发福。其他日主类推。

- **完整对等诠释（secondary_lang_full）**：Officer Stars must be pure, not mixed. For example, if Jia Wood Day Master uses Xin Metal as Proper Officer, with year-month-hour all Xin Metal or You Metal—though numerous, purely unified is actually favorable. If contains both Xin Metal Proper Officer and Geng Metal Seven Killings, constitutes Officer-Killing mixed harming Day Master, requires Fire luck to control-suppress Geng Metal for prosperity. Other Day Masters follow similar principles.

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 官杀混杂 | Officer-Killing Mixed | 正官与七杀同现 | Proper Officer and Seven Killings coexist | officer_killing_mixed | existing |
| 纯一尽好 | Purely Unified Favorable | 官星虽多但纯一反好 | Officers numerous but unified is favorable | state_pure_unified_favorable_proposal | new_candidate |
| 制伏 | Control-Suppression | 用克制之神制服过强者 | Use controlling elements to suppress excessive | method_control_suppression_proposal | new_candidate |

- **核心要点**：
  - 官星要纯，不要杂
  - 官星虽多但纯一无杂反而好（纯一尽好）
  - 官杀混杂则伤害日主，为格局大忌
  - 化解之法：行火乡制伏七杀
  - 其他日主类推此理
- **详细解说**：  
  本条论述官杀混杂的危害与化解。"官星要纯，不要杂"是正官格的核心法则。以甲木日主为例：若命中年月时都是辛金（正官）或酉金（酉中藏辛），虽然官星数量多，但"纯一尽好"——都是同一性质的正官，反而是清贵格局。但若命中既有辛金正官又有庚金七杀，则构成"官杀混杂"——正官代表的约束与七杀代表的攻击同时存在，性质相冲，七杀的凶性会"以伤其身"。化解之法是"行火乡制伏"——以火克金，制伏七杀庚金（火克庚但不克辛，因丁火合壬而非克），使官星纯化。"馀仿此"说明此法则适用于所有日主。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_085]` `[trigger: 官要纯]` `[factor_trigger: officer_killing_mixed AND officer_purity]` `[role: 主干]` 官星要纯，不要杂。 → 《渊海子平·论官杀混杂要制伏》
  - `[ns_yhzp_086]` `[trigger: 纯一尽好]` `[factor_trigger: officer_killing_mixed]` `[role: 主干依赖]` 虽多尽不妨，盖纯一尽好。 → 《渊海子平·论官杀混杂要制伏》
  - `[ns_yhzp_087]` `[trigger: 官杀混杂]` `[factor_trigger: officer_killing_mixed AND hunza]` `[role: 条件分支]` 若有庚或庚申，则混杂为杀，以伤其身。 → 《渊海子平·论官杀混杂要制伏》
  - `[ns_yhzp_088]` `[trigger: 火制金杀]` `[factor_trigger: method_fire_controls_metal_killing_proposal AND bing_ding_fire AND method_fire_controls_metal]` `[role: 总结]` 要行火乡制伏，则发福也。 → 《渊海子平·论官杀混杂要制伏》"""
    normalized_text_zh: str = """"""
    subject: str = "论官杀混杂要制伏"
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
        l1_anchor="yhzp_v1.0.0_论官杀混杂要制伏_001_L1",
    )
    version: str = "1.0.0"
