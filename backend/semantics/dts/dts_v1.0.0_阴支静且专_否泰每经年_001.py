"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997180
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
    semantic_id="dts_v1.0.0_阴支静且专_否泰每经年_001",
    book_id="dts",
    engine_id="bazi"
)
class 阴支静且专否泰每经年(SemanticEntry):
    """
    - **原文（source_text）**：
  阴支静且专，否泰每经年。

- 原注（原文注解）：
  　　丑，卯，巳，未，酉，亥，阴也。其性静，其气专，其否泰之验，每经年而始见。

- 分字分词释...
    """
    
    original_text: str = """- **原文（source_text）**：
  阴支静且专，否泰每经年。

- 原注（原文注解）：
  　　丑，卯，巳，未，酉，亥，阴也。其性静，其气专，其否泰之验，每经年而始见。

- 分字分词释义：
  - 阴支：地支之阴者（丑、卯、巳、未、酉、亥）。
  - 静：静守、缓慢.
  - 专：专一、专注，气机较为“定”.
  - 否泰：否为不通，泰为通达，指吉凶盛衰.
  - 每经年：往往要一年以上方见其效验.

- **规范化释义（primary_lang_explained）**：
  阴性地支偏静偏专，变化较慢，吉凶应期多延后，常以年为单位去观察转化。

- **次语种完整诠释（secondary_lang_full）**:  
  Yin branches are the six quiet Earthly Branches (Chou, Mao, Si, Wei, You, Hai). Their qi prefers stillness, accumulation and concentration rather than sudden release. Fortune and misfortune under their control usually need full yearly cycles to become clear, often taking shape slowly in the background before they can be judged. In timing work, structures that lean on Yin branches should therefore be read as slow, deep patterns of change: they describe what ripens through patience, long-term effort and structural adjustment, rather than short, dramatic events.

- **核心要点**：
  - 阴支六位：丑、卯、巳、未、酉、亥，性静气专
  - 阴静迟显：以慢与深为特征，应期多经年
  - 否泰每经年：吉凶盛衰多看完整年度的积累与转折
  - 取用策略：以缓图之，重长期结构调整而非短期激进操作

- **详细解说**：
  阴支是地支中偏静偏专的六位（丑卯巳未酉亥），气机倾向于内敛、积蓄与专注，不喜骤然大起大落。其应事特点在于缓慢而深：吉凶多在整年甚至跨年度的过程中渐进显化，而非立刻爆发。断运断流年时，涉及阴支的结构更适合从长期趋势、结构调整与耐心经营的角度来把握，而不宜以阳支那种速达思维急断。否泰每经年，提醒命理师与命主：阴支主的变化，往往要经历完整年度的沉淀与检验，才看得出真正的好坏转折。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_058]` `[trigger: 命局阴支偏多]` `[factor_trigger: yinzhi_stability==静专 AND event_gradual_index==以年计]` `[role: 主干]` 阴支主静主专，事态发展缓慢，否泰多以年计而非月计。 → 《滴天髓·地支论》#阴支
  - `[ns_dts_059]` `[trigger: 岁运作用于阴支]` `[factor_trigger: yinzhi_trigger==被岁运合冲但响应慢 AND event_gradual_index==以年计]` `[role: 主干依赖]` 阴支受岁运冲合时，变化常在整年渐进显现，不宜急于下结论。 → 《滴天髓·地支论》#阴支
  - `[ns_dts_060]` `[trigger: 阴阳支交织]` `[factor_trigger: (yinzhi_stability==静专 OR yangzhi_momentum==强动) AND (event_gradual_index==以年计 OR event_speed_index==以月季计)]` `[role: 条件分支]` 阴支与阳支交织时，可以阳速阴缓折中判断应期，短中长期并看。 → 《滴天髓·地支论》#阴支
  - `[ns_dts_135]` `[trigger: 阴支静守有成]` `[factor_trigger: yinzhi_stability==静专 AND yinzhi_accumulation==高]` `[role: 主干依赖]` 阴支静专而有积蓄，以年计之吉凶多主稳定成就。 → 《滴天髓·地支论》#阴支
  - `[ns_dts_136]` `[trigger: 阴支被强冲]` `[factor_trigger: yinzhi_trigger==被岁运合冲但响应慢 AND yinzhi_boundary==on]` `[role: 例外处理]` 阴支虽静，强冲亦能激动，但动后仍归于缓，不若阳支骤变。 → 《滴天髓·地支论》#阴支"""
    normalized_text_zh: str = """"""
    subject: str = "阴支静且专，否泰每经年。"
    factor_refs: list = ['dizhi_yinzhi_group', 'yinzhi_jing_zhuan', 'pitai', 'jingnian_yingqi']
    
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
        l1_anchor="dts_v1.0.0_阴支静且专_否泰每经年_001_L1",
    )
    version: str = "1.0.0"
