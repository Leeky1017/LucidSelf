"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101343
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
    semantic_id="smth_v1.0.0_驿马数理与四局分布_001",
    book_id="sanming",
    engine_id="bazi"
)
class 驿马数理与四局分布(SemanticEntry):
    """
    - **原文（source_text）**：
  论驿马。所谓驿马者，乃先天三合数也。先天寅七、午九、戌五，合数二十有一，故自子顺至申，凡二十有一，而为火局之驿马。亥卯未之数，四、六与八合为十八，故自...
    """
    
    original_text: str = """- **原文（source_text）**：
  论驿马。所谓驿马者，乃先天三合数也。先天寅七、午九、戌五，合数二十有一，故自子顺至申，凡二十有一，而为火局之驿马。亥卯未之数，四、六与八合为十八，故自子顺至巳，凡十八，而为木局之驿马。木、火，阳局也，从子一阳顺行；金、水，阴局也，从午一阴逆行。甲子辰之数，七、九与五合，为二十有一，故自午逆至寅，凡二十有一，而为水局之驿马。巳酉丑之数，四、六与八合为十八，故自午至亥，凡十有八，而为金局之驿马。此法之所由立也。

- **分字分词释义**：
  - **驿马**：原指邮驿所用之马，在命理中象征迁移、奔波与变动机会。
  - **先天三合数**：以三合局地支的数值相加推导出驿马位置的数理方法。
  - **阳局 / 阴局**：木火为阳局，自子顺行；金水为阴局，自午逆行。

- **规范化释义（primary_lang_explained）**：
  作者从数理入手，说明驿马不是任意指定，而是由先天三合局的数字推导出来：寅午戌三支数和为二十一，自子顺数二十一位至申为火局驿马；亥卯未之数为十八，自子顺至巳为木局驿马。木火属阳，自子顺行；金水属阴，自午逆行：甲子辰为水局，数和二十一，自午逆至寅为水局之马；巳酉丑为金局，数和十八，自午至亥为金局之马。此构成四局驿马分布的通法。

- **完整对等诠释（secondary_lang_full）**：
  The Post Horse star is not arbitrary travel but is derived from the numerical sums of each triad bureau.
  For Fire and Wood as yang bureaux the sums are counted forward from Zi, and for Metal and Water as yin bureaux they are counted backward from Wu, so that each bureau obtains a specific horse branch where movement is concentrated.
  In practice this branch marks where change, relocation and mobility are most likely to occur, and should be encoded as the dynamic point of the bureau rather than confused with fortune itself.
- **核心要点**：
  - 驿马的本质是「局中动点」，随三合局的方位而定，不应固定理解为某支等同「马」。
  - 阳局自子顺行、阴局自午逆行，是数理层面对阴阳流行的刻画，工程化时可直接编码为序列运算。
 
- **详细解说**：
  1) 根据命局地支确定所属三合局（寅午戌、申子辰、巳酉丑、亥卯未），并标记每局的「本局驿马位」；
  2) 使用统一的「子→丑→…→亥」索引，将三合局数值和映射为驿马所在支，或直接用预先计算好的映射表（如寅午戌局马在申等）以降低计算成本；
  3) 在特征工程中，为命局中年、月、日、时是否落在本局驿马位分别打标签（如 `year_horse`, `day_horse`），并与大运、流年对该位的触发情况建立时间序列特征；
  4) 在下游任务中，将驿马特征主要用于与「迁居/出差/岗位轮换/行业切换」等事件的相关性建模，而不是直接用来判断「好命/坏命」。

- 反例与边界：
  - 不宜混用多套不同来源的驿马取法（如另行取年马、日马），在同一系统内应统一使用一套数理定义，避免特征自相矛盾；
  - 驿马本身不分贵贱，只表「动」，若命局与现实变量显示命主职业本就高度固定，过度放大驿马的影响会削弱模型的现实贴合度；
  - 工程上如果直接把「见驿马」当作迁移事件的充分条件，忽略户籍、教育、行业等现实约束，会导致预测虚高；
  - 反向误区是将驿马一律理解为奔波辛劳，而忽略很多现代迁移实际上带来的是教育与机会扩展。

- 小例（示意）：
  - 某命局属申子辰局，驿马在寅，命中日支寅、时支又见寅，系统可标记为「核心生活圈驿马位重」，在职业路径上优先考虑跨城市、跨部门轮岗的可能性；
  - 另一命局虽有驿马，但全落在年支且与现实条件（如重本地依赖行业）不符，系统则弱化其权重，仅在解释中保留「迁移潜在意向」的提示。"""
    normalized_text_zh: str = """"""
    subject: str = "驿马数理与四局分布"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_yima', 'bazi_semantic', 'bazi_factor_45', 'bazi_semantic', 'bazi_factor_46', 'bazi_semantic']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_驿马数理与四局分布_001_L1",
    )
    version: str = "1.0.0"
