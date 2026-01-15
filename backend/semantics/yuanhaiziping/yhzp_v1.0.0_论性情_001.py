"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558772
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
    semantic_id="yhzp_v1.0.0_论性情_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论性情(SemanticEntry):
    """
    - **原文（source_text）**：性情者，乃喜怒哀乐爱恶欲之所发，仁义礼智信之所布，父精母血而成形；皆金木水火土之关系也。且如木曰曲直，味酸，主仁。恻隐之心、慈祥恺悌、济物利民、恤孤念寡、恬...
    """
    
    original_text: str = """- **原文（source_text）**：性情者，乃喜怒哀乐爱恶欲之所发，仁义礼智信之所布，父精母血而成形；皆金木水火土之关系也。且如木曰曲直，味酸，主仁。恻隐之心、慈祥恺悌、济物利民、恤孤念寡、恬静清高、人物清秀、体长、面色青白，故云：'木盛多仁'。太过则折，执物性偏；不及少仁、心生妒意。

- **分字分词释义**：
  - **性情**：先天禀赋所形成的情绪与人格特征，受五行影响。
  - **喜怒哀乐爱恶欲**：七情，人类基本情绪反应。
  - **仁义礼智信**：儒家五常，与五行一一对应。
  - **曲直**：木的特性，能曲能直，象征仁德柔韧。
  - **恻隐之心**：同情怜悯之心，木主仁的核心表现。
  - **慈祥恺悌**：慈爱祥和、和乐恭敬，木旺者的性格特征。
  - **济物利民**：帮助万物、造福百姓，木旺者的行为倾向。
  - **太过/不及**：五行过旺或不足，都会导致性格偏差。

- **规范化释义（primary_lang_explained）**：性情源于五行禀赋。木主仁，木旺者有恻隐之心、慈祥恺悌，济物利民，体长面色青白；太过则性偏固执，不及则少仁心生妒意。（火土金水类推）

- **完整对等诠释（secondary_lang_full）**：Temperament stems from Five-Element endowments. Wood governs benevolence—Wood-prosperous individuals possess compassion, kindness, generosity, benefiting people, tall physique with pale-greenish complexion. Excess brings rigidity and bias; deficiency brings unkindness and jealousy. (Similarly for Fire, Earth, Metal, Water)

- **核心要点**：
  - 性情由五行禀赋决定
  - 木主仁：恻隐之心、慈祥恺悌、济物利民
  - 火主礼、土主信、金主义、水主智（类推）
  - 五行过旺则性格偏执，不及则美德不足
  - 中和为贵，过与不及皆非佳

- **详细解说**：  
  本条论述五行与性情的对应关系，是儒家"五常"与阴阳五行相结合的产物。性情源于"父精母血"所成的先天禀赋，本质上是金木水火土五行在人体中的分布与平衡。木主仁，具体表现为恻隐之心、慈祥恺悌、济物利民、恤孤念寡等美德，外貌上呈现体长、面色青白的特征。但任何五行都忌太过与不及：木太过则"折"（性格偏执固执），木不及则"少仁、心生妒意"。火主礼（热情有礼）、土主信（诚信厚重）、金主义（果断刚正）、水主智（聪慧机变），各有其太过与不及的表现。此条是子平断性格的理论基础，也是"命理心理学"的雏形。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_034]` `[trigger: 性情根源]` `[factor_trigger: five_element_generation]` `[role: 主干]` 性情者，乃喜怒哀乐爱恶欲之所发，仁义礼智信之所布。 → 《渊海子平·论性情》
  - `[ns_yhzp_035]` `[trigger: 五行主性]` `[factor_trigger: element_temperament]` `[role: 主干依赖]` 皆金木水火土之关系也。 → 《渊海子平·论性情》
  - `[ns_yhzp_036]` `[trigger: 木主仁]` `[factor_trigger: element_temperament]` `[role: 条件分支]` 木曰曲直，味酸，主仁。恻隐之心、慈祥恺悌、济物利民。 → 《渊海子平·论性情》
  - `[ns_yhzp_037]` `[trigger: 木旺特征]` `[factor_trigger: day_master_strength]` `[role: 条件分支]` 木盛多仁，人物清秀、体长、面色青白。 → 《渊海子平·论性情》
  - `[ns_yhzp_038]` `[trigger: 木太过]` `[factor_trigger: day_master_strength AND element_imbalance_temperament]` `[role: 条件分支]` 太过则折，执物性偏。 → 《渊海子平·论性情》
  - `[ns_yhzp_039]` `[trigger: 木不及]` `[factor_trigger: day_master_strength]` `[role: 条件分支]` 不及少仁、心生妒意。 → 《渊海子平·论性情》"""
    normalized_text_zh: str = """"""
    subject: str = "论性情"
    factor_refs: list = ['element_temperament', 'five_virtues', 'element_temperament']
    
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
        l1_anchor="yhzp_v1.0.0_论性情_001_L1",
    )
    version: str = "1.0.0"
