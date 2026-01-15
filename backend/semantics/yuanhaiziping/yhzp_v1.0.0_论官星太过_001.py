"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558884
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
    semantic_id="yhzp_v1.0.0_论官星太过_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论官星太过(SemanticEntry):
    """
    - **原文（source_text）**：  
  如壬癸生人，四柱是辰戌丑未巳午，天干不露官星与杀，则官杀暗藏于中为多。若四柱元有为好；若无制伏，须行木运，与三合木局亦好。大凡官星多则杂，务要除而...
    """
    
    original_text: str = """- **原文（source_text）**：  
  如壬癸生人，四柱是辰戌丑未巳午，天干不露官星与杀，则官杀暗藏于中为多。若四柱元有为好；若无制伏，须行木运，与三合木局亦好。大凡官星多则杂，务要除而清之，乃可发福。若官星多又行官运，亦不济事。

- **分字分词释义**：
  - **官星太过**：官杀数量过多，超过命局所能承受。
  - **壬癸生人**：壬水或癸水日主的命造。
  - **辰戌丑未巳午**：四墓库加巳午火土之地，对水日主而言皆为官杀之根。
  - **官杀暗藏**：官杀不透天干，藏于地支之中。
  - **除而清之**：去除多余官杀，使格局清纯。
  - **行木运**：木能克土，行木运可制土官，疏导过旺官杀。
  - **三合木局**：亥卯未三合木局，增强木力制土。

- **规范化释义（primary_lang_explained）**：  
  壬癸日主若四柱地支多土（辰戌丑未巳午），天干不露官杀，则官杀暗藏支中过多。若原局有制化则好，若无制需行木运或木局以木克土疏导。官星过多则杂乱，务必除去多余使之清纯才能发福。若官星已多再行官运，反而不利无济于事。

- **完整对等诠释（secondary_lang_full）**：  
  If Ren-Gui Day Master has Four Pillars with excessive Earth branches (Chen-Xu-Chou-Wei-Si-Wu) while Heavenly Stems don't reveal Officers-Killings, then Officers-Killings hidden in branches become excessive. If original structure has control-transformation it's favorable; lacking control requires Wood luck or Wood bureau using Wood to restrain Earth. Excessive Officers bring chaos, must remove excess to achieve purity for prosperity. If Officers already excessive then meet Officer luck, becomes disadvantageous and ineffective.

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 官星太过 | Excessive Officers | 官星数量过多导致杂乱 | Officers excessive causing chaos | pattern_excessive_officers_proposal | new_candidate |
| 官杀暗藏 | Hidden Officer-Killing | 官杀不透干藏于支 | Officer-Killing hidden in branches | pattern_hidden_officer_killing_proposal | new_candidate |
| 除而清之 | Remove to Purify | 去除多余使之清纯 | Remove excess to achieve purity | method_remove_to_purify_officers_proposal | new_candidate |

- **核心要点**：
  - 官星过多则杂乱，不以吉论
  - 壬癸日主若地支多土，官杀暗藏过多
  - 无制需行木运，以木克土疏导
  - 三合木局（亥卯未）亦可制官
  - 官星已多再行官运，不济事

- **详细解说**：  
  本条专论官星太过的问题。以壬癸水日主为例：若四柱地支多见辰戌丑未（四墓库皆含土）或巳午（火土旺地），天干虽不露官杀，但官杀暗藏支中已然过多。"官星多则杂"是核心论断——官星代表压力与约束，过多则压力过大难以承受，反成凶象。对治之法是"除而清之"——行木运以木克土，减少官杀之力；或遇三合木局（亥卯未）增强木力制土。特别警告"若官星多又行官运，亦不济事"——官已过多再遇官运，官上加官更增压力，反而不利。此条揭示了"物极必反"的命理原则。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_081]` `[trigger: 官星太过]` `[factor_trigger: pattern_excessive_officers_proposal]` `[role: 主干]` 大凡官星多则杂，务要除而清之，乃可发福。 → 《渊海子平·论官星太过》
  - `[ns_yhzp_082]` `[trigger: 官杀暗藏]` `[factor_trigger: pattern_hidden_officer_killing_proposal AND pattern_hidden_officer_killing]` `[role: 主干依赖]` 天干不露官星与杀，则官杀暗藏于中为多。 → 《渊海子平·论官星太过》
  - `[ns_yhzp_083]` `[trigger: 木运制官]` `[factor_trigger: method_wood_controls_earth_officer_proposal]` `[role: 条件分支]` 若无制伏，须行木运，与三合木局亦好。 → 《渊海子平·论官星太过》
  - `[ns_yhzp_084]` `[trigger: 官多行官]` `[factor_trigger: pattern_excessive_officers_proposal AND direct_officer AND dayun_officer AND excessive_officers]` `[role: 例外处理]` 若官星多又行官运，亦不济事。 → 《渊海子平·论官星太过》"""
    normalized_text_zh: str = """"""
    subject: str = "论官星太过"
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
        l1_anchor="yhzp_v1.0.0_论官星太过_001_L1",
    )
    version: str = "1.0.0"
