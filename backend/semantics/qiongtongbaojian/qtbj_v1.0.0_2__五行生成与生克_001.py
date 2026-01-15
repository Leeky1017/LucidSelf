"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619665
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
    semantic_id="qtbj_v1.0.0_2__五行生成与生克_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2五行生成与生克(SemanticEntry):
    """
    - **原文（source_text）**：
  北方阴极而生寒，寒生水。南方阳极而生热，热生火。东方阳散以泄而生风，风生木。西方阴止以收而生燥，燥生金。中央阴阳交而生温，温生土。其相生也所以相维，其...
    """
    
    original_text: str = """- **原文（source_text）**：
  北方阴极而生寒，寒生水。南方阳极而生热，热生火。东方阳散以泄而生风，风生木。西方阴止以收而生燥，燥生金。中央阴阳交而生温，温生土。其相生也所以相维，其相克也所以相制，此之谓有伦。

- **分字分词释义**：
  - **阴极**：阴气达到极致 / 阴寒之极 / 北方之象
  - **阳极**：阳气达到极致 / 阳热之极 / 南方之象
  - **阳散以泄**：阳气发散宣泄 / 生机外发 / 东方春生之象
  - **阴止以收**：阴气收敛凝止 / 肃杀收藏 / 西方秋收之象
  - **阴阳交**：阴阳二气交感 / 调和中正 / 中央之位
  - **相生**：互相滋生 / 生养维护之功 / 木火土金水循环生
  - **相克**：互相克制 / 制约平衡之用 / 木土水火金循环克
  - **伦**：伦理、次序 / 有序的规律 / 生克关系的法则

- **规范化释义（primary_lang_explained）**：
  北方阴气极盛产生寒冷，寒冷化生水；南方阳气极盛产生炎热，炎热化生火；东方阳气散发宣泄产生风，风化生木；西方阴气收敛凝止产生燥，燥化生金；中央阴阳交感产生温和之气，温和化生土。五行相生是为了互相维持，五行相克是为了互相制约，这就叫做有伦理次序。

- **完整对等诠释（secondary_lang_full）**：
  In the North, Yin reaches its peak generating Cold, which produces Water. In the South, Yang reaches its peak generating Heat, which produces Fire. In the East, Yang disperses and releases generating Wind, which produces Wood. In the West, Yin stops and contracts generating Dryness, which produces Metal. In the Center, Yin and Yang intersect generating Warmth, which produces Earth. Their mutual generation maintains the system, while their mutual control restricts excess; this is called the Ethical Order.

- **核心要点**：
  - 五行源于方位与阴阳二气的消长。
  - 水火木金土分别对应寒热风燥温。
  - 相生维持存在，相克维持平衡（伦序）。

- **详细解说**：
  此段阐述了五行的生成机制。水火是阴阳之极，木金是阴阳之变（散与收），土是阴阳之和。相生相克不是简单的爱恨，而是系统维持稳态的必要机制——“维”与“制”。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_004]` `[trigger: 五行生成]` `[factor_trigger: direction_north_water AND direction_south_fire]` `[role: 主干]` 北方阴极生寒，寒生水；南方阳极生热，热生火。 → 《穷通宝鉴·五行总论》#1.2
  - `[ns_qttbj_005]` `[trigger: 五行生成]` `[factor_trigger: direction_east_wood AND direction_west_metal]` `[role: 主干依赖]` 东方阳散以泄生风，风生木；西方阴止以收生燥，燥生金。 → 《穷通宝鉴·五行总论》#1.2
  - `[ns_qttbj_006]` `[trigger: 五行生成]` `[factor_trigger: direction_center_earth]` `[role: 主干依赖]` 中央阴阳交而生温，温生土。 → 《穷通宝鉴·五行总论》#1.2
  - `[ns_qttbj_007]` `[trigger: 五行相生]` `[factor_trigger: interaction_generation]` `[role: 总结]` 相生是为了互相维持，相克是为了互相制约。 → 《穷通宝鉴·五行总论》#1.2
  - `[ns_qttbj_008]` `[trigger: 五行生克]` `[factor_trigger: interaction_generation AND interaction_control]` `[role: 总结]` 水火是阴阳之极，木金是阴阳之变，土是阴阳之和。 → 《穷通宝鉴·五行总论》#1.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 五行生成与生克"
    factor_refs: list = ['yin_extreme', 'yang_extreme', 'interaction_generation', 'interaction_control', 'ethical_order']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_2__五行生成与生克_001_L1",
    )
    version: str = "1.0.0"
