"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997215
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
    semantic_id="dts_v1.0.0_暗冲暗会尤为喜_彼冲我兮皆冲起_001",
    book_id="dts",
    engine_id="bazi"
)
class 暗冲暗会尤为喜彼冲我兮皆冲起(SemanticEntry):
    """
    - **原文（source_text）**：
  暗冲暗会尤为喜，彼冲我兮皆冲起.

- 原注（原文注解）：
  　　如柱中所无，局取多者冲会暗神，比明冲明会尤佳，如子去冲午，柱中有寅与戌会者是也，日...
    """
    
    original_text: str = """- **原文（source_text）**：
  暗冲暗会尤为喜，彼冲我兮皆冲起.

- 原注（原文注解）：
  　　如柱中所无，局取多者冲会暗神，比明冲明会尤佳，如子去冲午，柱中有寅与戌会者是也，日干为我，提纲为彼，提纲为我，年时为彼，四柱为我，岁月为彼，我寅彼申，是彼冲（克）我，我子彼午，是我冲（克）彼.

- 分字分词释义：
  - 暗冲/暗会：非显见于四柱明位，而在局结构中成立之冲会.
  - 尤为喜：更为可取（对成局有益）.
  - 我/彼：以日干或主位为“我”，对位为“彼”.

- **规范化释义（primary_lang_explained）**：
  冲会不独在明位，暗中成立者更显灵动；判“我冲彼”或“彼冲我”，需以日主/提纲/岁月之位次分判.

- **次语种完整诠释（secondary_lang_full）**:  
  Hidden clashes and hidden meetings are often more effective than those that appear openly. Three-harmony frames and assemblies can create invisible forces even when the relevant branches are not written directly in the four pillars. Whether “they clash me” or “I clash them” is judged by the relative positions of the Day Master, the key pillar and the yearly or monthly charts. In practice, these hidden structures frequently move matters more flexibly than obvious surface clashes, because they operate through the underlying pattern of the chart rather than through what is immediately visible.

- **核心要点**：
  - 暗冲暗会多在结构中成立，其力常胜于表面明冲.
  - 查暗神须结合会局、三合与岁运位置，不可只看四柱明位.
  - 判“彼冲我”或“我冲彼”前，必须先分清谁是“我”、谁是“彼”.
  - 暗局发动时，常在不显处推动关键转折，易被粗看者忽略.

- **详细解说**：
  暗冲暗会所说的“暗”，并非凭空臆测，而是指通过三合、三会、半合等结构性组合，在四柱表层看不见、却在整体局势中真实存在的冲会关系。这类暗神一旦被岁运触发，往往比明冲更具灵动与穿透力，因为它依托的是全局结构而非单一明位。判断时，首先要确认暗局是否真正成立，其次要分清谁是“我”、谁是“彼”：可取日干为我、提纲为彼，或四柱为我、岁运为彼。方向一旦搞错，就会把本为“我冲彼”的主动出击误读成“彼冲我”的被动受伤，使吉凶判断完全反转。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_070]` `[trigger: 命局存在三合三会暗局]` `[factor_trigger: dizhi_hidden_structure_profile IN {三合, 三会, 半合形成暗冲会} AND hidden_effectiveness==暗强于明]` `[role: 主干]` 暗冲暗会不显于四柱明位，却在结构中推事，往往比明冲更灵动有力。 → 《滴天髓·地支论》#暗冲暗会
  - `[ns_dts_071]` `[trigger: 判定我冲彼或彼冲我]` `[factor_trigger: me_them_position IN {日主vs月, 四柱vs年运} AND clash_direction IN {我冲彼, 彼冲我}]` `[role: 主干依赖]` 先定日主与岁运谁为我谁为彼，再断是我冲彼还是彼冲我。 → 《滴天髓·地支论》#暗冲暗会
  - `[ns_dts_072]` `[trigger: 岁运触发暗神]` `[factor_trigger: dizhi_hidden_structure_profile EXISTS AND hidden_force_level==高]` `[role: 条件分支]` 岁运引动暗神时，多在不显处激活关键变化，须重点追踪。 → 《滴天髓·地支论》#暗冲暗会
  - `[ns_dts_141]` `[trigger: 暗局未成]` `[factor_trigger: dizhi_hidden_structure_profile NOT COMPLETE OR hidden_boundary==on]` `[role: 例外处理]` 暗局若缺位或被破，则暗冲暗会之力大减，不可强论。 → 《滴天髓·地支论》#暗冲暗会
  - `[ns_dts_142]` `[trigger: 我彼方向错判]` `[factor_trigger: clash_direction MISMATCHED OR me_them_position MISPLACED]` `[role: 总结]` 我彼定位一错，冲之主被动全反，吉凶判断完全逆转。 → 《滴天髓·地支论》#暗冲暗会

- **校勘与字词辨析（textual_criticism）**：
  - 中文：无版本差异 / N/A  
  - English: No known textual variants / N/A"""
    normalized_text_zh: str = """"""
    subject: str = "暗冲暗会尤为喜，彼冲我兮皆冲起."
    factor_refs: list = ['anchong', 'anhui', 'bichongwo', 'wochongbi', 'anshen', 'lingdong']
    
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
        l1_anchor="dts_v1.0.0_暗冲暗会尤为喜_彼冲我兮皆冲起_001_L1",
    )
    version: str = "1.0.0"
