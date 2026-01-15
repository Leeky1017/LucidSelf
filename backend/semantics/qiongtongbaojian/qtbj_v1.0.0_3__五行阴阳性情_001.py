"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619679
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
    semantic_id="qtbj_v1.0.0_3__五行阴阳性情_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3五行阴阳性情(SemanticEntry):
    """
    - **原文（source_text）**：
  火为太阳，性炎上。水为太阴，性润下。木为少阳，性腾上而无所止。金为少阴，性沉下而有所止。土无常性，视四时所乘，欲使相济得所，勿令太过弗及。

- **...
    """
    
    original_text: str = """- **原文（source_text）**：
  火为太阳，性炎上。水为太阴，性润下。木为少阳，性腾上而无所止。金为少阴，性沉下而有所止。土无常性，视四时所乘，欲使相济得所，勿令太过弗及。

- **分字分词释义**：
  - **太阳**：阳之极、大阳 / 阳气最盛的状态 / 火之本象
  - **太阴**：阴之极、大阴 / 阴气最盛的状态 / 水之本象
  - **少阳**：阳之初、小阳 / 阳气初生的状态 / 木之本象
  - **少阴**：阴之初、小阴 / 阴气初生的状态 / 金之本象
  - **炎上**：火焰向上 / 火的运动趋势 / 升腾发越之象
  - **润下**：滋润向下 / 水的运动趋势 / 沉降滋养之象
  - **腾上而无所止**：升腾向上且无止境 / 木的无限生发 / 生机勃勃之象
  - **沉下而有所止**：沉降向下且有止境 / 金的收敛有度 / 肃杀成形之象
  - **无常性**：没有固定本性 / 土的可塑性 / 随四时变化
  - **相济得所**：互相调济恰到好处 / 平衡之道 / 不偏不倚

- **规范化释义（primary_lang_explained）**：
  火属于太阳（大阳），本性是炎热向上；水属于太阴（大阴），本性是滋润向下；木属于少阳，本性是升腾向上且无止境；金属于少阴，本性是沉降向下且有止境；土没有固定的性情，要看四季气候的旺衰来定，目的是使五行配合得当，既不要太过也不要不及。

- **完整对等诠释（secondary_lang_full）**：
  Fire is Greater Yang (Taiyang), its nature is to flame upwards. Water is Greater Yin (Taiyin), its nature is to moisten downwards. Wood is Lesser Yang (Shaoyang), its nature is to ascend without limit. Metal is Lesser Yin (Shaoyin), its nature is to sink down with a limit. Earth has no constant nature; it depends on the influence of the four seasons. The goal is to achieve proper balance and coordination, ensuring neither excess nor deficiency.

- **核心要点**：
  - 四象配五行：火太阳，水太阴，木少阳，金少阴。
  - 运动趋势：火上，水下，木腾（无限），金沉（有限）。
  - 土的特殊性：随四时变化，主调节平衡。

- **详细解说**：
  这里引入了四象（太阳太阴少阳少阴）对应四行。值得注意的是木与金的区别：木是“无所止”的生发，金是“有所止”的收敛。土作为中介，没有固定形态，随季节而变，起平衡作用。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_009]` `[trigger: 火性]` `[factor_trigger: xiang_taiyang]` `[role: 主干]` 火为太阳，性炎上，升腾发越。 → 《穷通宝鉴·五行总论》#1.3
  - `[ns_qttbj_010]` `[trigger: 水性]` `[factor_trigger: xiang_taiyin]` `[role: 主干依赖]` 水为太阴，性润下，沉降滋养。 → 《穷通宝鉴·五行总论》#1.3
  - `[ns_qttbj_011]` `[trigger: 木性]` `[factor_trigger: xiang_shaoyang]` `[role: 主干依赖]` 木为少阳，性腾上而无所止，生机无限。 → 《穷通宝鉴·五行总论》#1.3
  - `[ns_qttbj_012]` `[trigger: 金性]` `[factor_trigger: xiang_shaoyin]` `[role: 主干依赖]` 金为少阴，性沉下而有所止，收敛有度。 → 《穷通宝鉴·五行总论》#1.3
  - `[ns_qttbj_013]` `[trigger: 土性]` `[factor_trigger: earth_variable_nature]` `[role: 条件分支]` 土无常性，视四时所乘，主调节平衡。 → 《穷通宝鉴·五行总论》#1.3
  - `[ns_qttbj_014]` `[trigger: 五行平衡]` `[factor_trigger: principle_balance]` `[role: 总结]` 欲使相济得所，勿令太过弗及。 → 《穷通宝鉴·五行总论》#1.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 五行阴阳性情"
    factor_refs: list = ['xiang_taiyang', 'xiang_taiyin', 'xiang_shaoyang', 'xiang_shaoyin', 'fire_flaming_upward', 'water_moisturizing_down']
    
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
        l1_anchor="qtbj_v1.0.0_3__五行阴阳性情_001_L1",
    )
    version: str = "1.0.0"
