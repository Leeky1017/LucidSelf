"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559107
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
    semantic_id="yhzp_v1.0.0_论金神_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论金神(SemanticEntry):
    """
    - **原文（source_text）**：
  夫金神者，止有三时：癸酉、己巳、乙丑。金神乃破败之神，要制伏，入火乡为胜。如四柱中更带七杀阳刃，真贵人也。大抵威猛者，以强暴为能。太刚必折，不有以制之...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫金神者，止有三时：癸酉、己巳、乙丑。金神乃破败之神，要制伏，入火乡为胜。如四柱中更带七杀阳刃，真贵人也。大抵威猛者，以强暴为能。太刚必折，不有以制之，则宽猛不济。其人有刚断明敏之才，倔强不可驯伏之志。运行火乡，四柱有火局，便为贵命；惧水乡，则非福矣！

- **分字分词释义**：
  - **金神**：癸酉己巳乙丑三时为金神。
  - **破败之神**：金神属凶神，主破败。
  - **入火乡为胜**：金神需火制伏才能成格。
  - **七杀阳刃**：金神配七杀阳刃主大贵。
  - **威猛强暴**：金神主性格威猛。
  - **太刚必折**：过刚则折，需制化调和。
  - **刚断明敏**：金神之人的才能特点。
  - **倔强不可驯伏**：金神之人的性格特点。

- **规范化释义（primary_lang_explained）**：
  金神有癸酉己巳乙丑三时，乃破败之神，要制伏入火乡为胜。如四柱更带七杀阳刃真贵人也。金神主威猛强暴，太刚必折需制之。其人有刚断明敏之才，倔强不可驯伏之志。运行火乡四柱有火局便为贵命，惧水乡则非福。

- **完整对等诠释（secondary_lang_full）**：
  Metal Spirit has only three hours: Gui-You, Ji-Si, Yi-Chou. Metal Spirit is a destruction spirit, requiring subjugation; entering Fire regions is victorious. If Four Pillars additionally contain Seven Killings and Yang Blade, it is truly a noble person. Generally, those with fierce, powerful natures take violence as their capability. Extreme rigidity necessarily breaks; without something to subdue it, severity and leniency cannot be balanced. Such persons have talents of decisive sharpness and keen intelligence, with stubborn, unconquerable wills. When fortune-running enters Fire regions and Four Pillars contain Fire formations, it becomes a noble fate; fearing Water regions, there is no fortune!

- **核心要点**：
  - 金神有癸酉、己巳、乙丑三时
  - 金神乃破败之神，需火制伏
  - 金神配七杀阳刃主大贵
  - 金神主威猛刚断
  - 太刚必折需制化
  - 金神喜火乡忌水乡

- **详细解说**：
  本条论述金神的性质与制化。金神"止有三时：癸酉、己巳、乙丑"。金神的本质是"破败之神"——属凶神，但"要制伏，入火乡为胜"——需要火来制伏才能化凶为吉。金神的配合是"如四柱中更带七杀阳刃，真贵人也"——金神配七杀阳刃构成大贵格局，凶神相配反成大贵。金神之人的性格是"威猛者，以强暴为能"、"有刚断明敏之才，倔强不可驯伏之志"——刚毅果决、倔强不屈。但"太刚必折，不有以制之，则宽猛不济"——过刚则折，需要适当的制化才能成材。金神的行运要求是"运行火乡，四柱有火局，便为贵命；惧水乡，则非福矣"——喜火运忌水运，与金神需火制的原理一致。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_147]` `[trigger: 金神定义]` `[factor_trigger: metal_spirit]` `[role: 主干]` 夫金神者，止有三时：癸酉、己巳、乙丑。 → 《渊海子平·论金神》
  - `[ns_yhzp_148]` `[trigger: 金神破败]` `[factor_trigger: metal_spirit AND method_fire_luck_controls_metal_spirit_proposal AND bing_ding_fire]` `[role: 主干依赖]` 金神乃破败之神，要制伏，入火乡为胜。 → 《渊海子平·论金神》
  - `[ns_yhzp_149]` `[trigger: 金神配杀刃]` `[factor_trigger: metal_spirit AND seven_killings AND yang_blade]` `[role: 条件分支]` 如四柱中更带七杀阳刃，真贵人也。 → 《渊海子平·论金神》
  - `[ns_yhzp_150]` `[trigger: 金神威猛]` `[factor_trigger: metal_spirit]` `[role: 条件分支]` 大抵威猛者，以强暴为能。 → 《渊海子平·论金神》
  - `[ns_yhzp_151]` `[trigger: 太刚必折]` `[factor_trigger: metal_spirit]` `[role: 例外处理]` 太刚必折，不有以制之，则宽猛不济。 → 《渊海子平·论金神》
  - `[ns_yhzp_152]` `[trigger: 金神性格]` `[factor_trigger: metal_spirit AND trait_decisive_astute_proposal]` `[role: 条件分支]` 其人有刚断明敏之才，倔强不可驯伏之志。 → 《渊海子平·论金神》
  - `[ns_yhzp_153]` `[trigger: 金神行运]` `[factor_trigger: metal_spirit AND method_fire_luck_controls_metal_spirit_proposal AND major_cycle AND bing_ding_fire]` `[role: 总结]` 运行火乡，四柱有火局，便为贵命；惧水乡，则非福矣！ → 《渊海子平·论金神》"""
    normalized_text_zh: str = """"""
    subject: str = "论金神"
    factor_refs: list = ['metal_spirit', 'method_fire_luck_controls_metal_spirit_proposal', 'trait_decisive_astute_proposal']
    
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
        l1_anchor="yhzp_v1.0.0_论金神_001_L1",
    )
    version: str = "1.0.0"
