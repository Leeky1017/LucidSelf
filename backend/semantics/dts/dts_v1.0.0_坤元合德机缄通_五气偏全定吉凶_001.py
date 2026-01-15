"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.932668
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
    semantic_id="dts_v1.0.0_坤元合德机缄通_五气偏全定吉凶_001",
    book_id="dts",
    engine_id="bazi"
)
class 坤元合德机缄通五气偏全定吉凶(SemanticEntry):
    """
    - 原文（source_text）：
  坤元合德机缄通，五气偏全定吉凶。

- 原注（原文注解）：
  　　地有刚柔，故五行布于东西南北，与天合德，而神其机缄，赋于人者，有偏全之不一，故吉凶定焉。
...
    """
    
    original_text: str = """- 原文（source_text）：
  坤元合德机缄通，五气偏全定吉凶。

- 原注（原文注解）：
  　　地有刚柔，故五行布于东西南北，与天合德，而神其机缄，赋于人者，有偏全之不一，故吉凶定焉。

- 分字分词释义：
  - 坤元：地道、地气（坤为地）。
  - 合德：与天合德，阴阳相应（地与天之德相合）。
  - 机缄：机括与机要之处（运行的枢纽、开合之机）。
  - 通：贯通、流行无碍。
  - 五气：五行之气（木火土金水）。
  - 偏：偏颇、不均、失衡。
  - 全：纯全、完备、得其中和之度。
  - 定：决定、裁定。
  - 吉凶：祸福得失之判。

- 规范化释义（primary_lang_explained）：
  地道若能与天道相合，运转的枢纽就能畅通。人在所受的五行之气上，若偏颇或纯全，将据此决定吉凶祸福。言下之意：判断命局，不可只看天，不可只看人，地之运行（地支、方局、位次）同样重要；偏全之度，实为吉凶关键。

- **次语种完整诠释（secondary_lang_full）**：  
  When Earth's Foundation (Kunyuan: the terrain formed by the Four Branches) aligns in virtue with Heaven's Principle, the pivotal mechanisms (Jixian: the hubs formed by Trine combinations, Directional formations, and storage reservoirs) can flow unobstructed. The biased or complete distribution pattern of the Five Qi (Wuqi Pianquan: whether Metal-Wood-Water-Fire-Earth are concentrated or balanced) then determines auspiciousness or inauspiciousness. However, bias or completeness alone does not dictate fortune—what truly matters is whether Earth's structure harmonizes with Heaven's mandate. When biased yet aligned with Virtue, specialized patterns emerge as strengths; when complete yet misaligned, structural afflictions accumulate as weaknesses. Therefore, destiny judgment requires examining the Branch layout, the connectivity of pivotal hubs, and the Heaven-Earth virtue alignment, rather than merely counting elemental presence or absence.

- **核心要点**：
  - 坤元指地支所代表的地道、地气与方位结构
  - 合德指地支局与天干用神相生相扶的状态
  - 机缄指三合、方局、库地等能量进出的枢纽
  - 偏全不以多少论，以合德与否论
  - 偏而合德可成专旺之格，全而违德反成病
  - 只看五行数量齐全与否而不看用神与格局，判断将失准

- **详细解说**：
  本条承接首条总纲，深入论述地支布局与五行偏全的判断法则。"坤元"喻地支之局面，"合德"指地支与天干用神形成相生相扶的和谐关系，"机缄"则是三合、方局、库地等形成的能量枢纽——气能否在此通行无阻，是判断局面健康与否的关键。"五气偏全"指五行分布的偏颇或齐全状态，但偏全本身不决定吉凶，关键在于是否"合德"：偏而合德，可成专旺格局；全而违德，反成结构病灶。实占时，先审地支之局（三合、方局、库地、生地、败地），次看干支情义（生合有情或冲克无情），最后察偏全之度（是否失中、用神能否达位）。

 - **narrative_snippets（叙事片段）**：
  - `[ns_dts_004]` `[trigger: 五行偏枯]` `[factor_trigger: wuxing_bias_pattern]` `[role: 主干]` 五行偏枯而合德有情，可成专旺之格，不以偏为病。 → 《滴天髓·通天论》#第2条
  - `[ns_dts_005]` `[trigger: 三合方局无情]` `[factor_trigger: jijian_hub_flow]` `[role: 条件分支]` 地支成三合方局而与日干无情时，虽全亦病，机缄不通。 → 《滴天髓·通天论》#第2条
  - `[ns_dts_006]` `[trigger: 五气流通]` `[factor_trigger: jijian_hub_flow]` `[role: 主干依赖]` 五气若能流通无滞，纵有偏缺亦可运化，关键在枢纽畅达。 → 《滴天髓·通天论》#第2条
  - `[ns_dts_099]` `[trigger: 偏全判吉凶]` `[factor_trigger: hede_alignment]` `[role: 总结]` 偏全不以五行多少论，关键在地支合德与否，偏而合德可成专旺，全而违德反成病。 → 《滴天髓·通天论》#第2条
  - `[ns_dts_100]` `[trigger: 判断顺序]` `[factor_trigger: kunyuan_earth_layout]` `[role: 主干依赖]` 断局须先审地支局势与机缄通否，再看干支情义与偏全之度。 → 《滴天髓·通天论》#第2条"""
    normalized_text_zh: str = """"""
    subject: str = "坤元合德机缄通，五气偏全定吉凶。"
    factor_refs: list = ['kunyuan_earth_layout', 'hede_alignment', 'jijian_hub_flow', 'wuqi_elements', 'wuxing_bias_pattern']
    
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
        l1_anchor="dts_v1.0.0_坤元合德机缄通_五气偏全定吉凶_001_L1",
    )
    version: str = "1.0.0"
