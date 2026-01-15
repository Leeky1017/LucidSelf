"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101515
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
    semantic_id="smth_v1.0.0_学堂会贵与官星学堂_001",
    book_id="sanming",
    engine_id="bazi"
)
class 学堂会贵与官星学堂(SemanticEntry):
    """
    - **原文（source_text）**：
  有生处见克，如甲乙人辛亥，丙丁人壬寅，戊己人甲申，庚辛人丁巳，谓之官星学堂，主登科甲，入侍从。有纳音见帝旺之位而逢天乙贵处其上，如己酉人得丙子、庚子日...
    """
    
    original_text: str = """- **原文（source_text）**：
  有生处见克，如甲乙人辛亥，丙丁人壬寅，戊己人甲申，庚辛人丁巳，谓之官星学堂，主登科甲，入侍从。有纳音见帝旺之位而逢天乙贵处其上，如己酉人得丙子、庚子日时，壬午人得辛卯日时之类，谓之学堂会贵，主清贵。凡学堂词馆，切不要犯空亡及冲破，支干纳音不要见克，方为得用。《祝胜经》云：「甲辰丙寅，学堂不真；或止富荫，官职卑贫；读书修学，空有虚名。」此言学堂怕落空也。《三车》云：「学堂无气，惟利师儒。」此言学堂要乘旺也。《理愚歌》云：「学堂如更朝驿马，位极勋高压天下。」此言学堂要有马也。又云：「生来禄马真学堂，若同词馆主文章；遇中不遇人谁会，不遇冲克福禄昌。」又云：「文星聚处人中瑞，声华独冠英雄辈；降生不遇真学堂，才学岂能为拔萃。」此言学堂怕冲破受克也。

- **分字分词释义**：
  - **官星学堂**：学堂与官星结构相连，主登科入仕。
  - **学堂会贵**：学堂再遇天乙等贵神，主清贵高品。
  - **学堂不真 / 学堂无气 / 学堂落空**：指学堂位置被空亡、受克或失旺，格局名不副实。

- **规范化释义（primary_lang_explained）**：
  最后一段集中说明了学堂词馆的得用与忌讳：
  - 生处见克、官星学堂者，多主有科甲与侍从之机；
  - 学堂见天乙等贵神，为学堂会贵，多指清贵而不俗；
  - 但若学堂落空亡、被冲破或无气，则多成虚名，只利小范围师儒之职，不足以大用；
  - 若又配驿马、禄马，则位极勋高；反之被冲破受克，则才学难以拔萃。

- **核心要点**：
  - 学堂词馆格要「真、有气、得贵、得马」方为上品：真在位置不虚，有气在得旺不空，得贵在有高品加持，得马在有实际施展空间。
  - 在工程化分析中，应根据学堂所在宫位的气势、是否空亡、是否与官星、禄马、贵人等同见，给出一个「学业与文章转换力」评分，而不能只看有无学堂标签。
 
- **详细解说**：
  1) 在特征工程中额外标注 `xuetang_true_flag`（是否落在真实长生位且不空亡）、`xuetang_qi_score`（是否乘旺、有无刑冲）、`xuetang_meets_gui`（是否会天乙等贵神）、`xuetang_meets_ma`（是否会驿马、禄马）；
   2) 将上述特征组合成一个「学堂可用度」评分，用于区分「名实相符的学堂」与「虚名学堂」，并与学历质量、职业平台大小等现实指标对照；
   3) 对于官星学堂、学堂会贵等结构，在职业预测任务中主要影响「入仕/进入大机构」的概率，而在其他任务中权重适当降低，避免过度泛化；
   4) 在解释输出时，将「学堂不真」「学堂无气」翻译成「学习环境或平台有限」「路径中存在断档」等现代语言，避免造成宿命化的心理负担。

 - 反例与边界：
   - 不宜把任何带学堂词馆结构的命局都视为「必然高官高位」，更多是对学习与平台的结构性描述，而非对最终成就的绝对承诺；
   - 若现实中命主已在小范围师儒或教育岗位上稳定发展，即便学堂无气也不必断为失败，工程上应允许「低调但稳定」这一结果类别；
   - 工程实现上若只用 `xuetang_flag` 一项粗标签，而不区分真/假、有气/无气、会贵/会马，容易丢失大量结构信息；
   - 反向误区是因少数虚名案例就完全否定学堂体系，使模型对教育路径与平台差异失去刻画能力。

 - 小例（示意）：
   - 某命局学堂真而有气，又会贵会马，现实中在重点高校深造并进入大型机构核心岗位，系统可用「真学堂 + 贵马」结构解释其教育与职业路径的连贯性；
  - 另一命局学堂名存实亡，仅利师儒，现实表现为在基层教学岗位长期稳定但难以晋升管理层，系统则以中性语气说明这是「平台规模与资源分布」的结果，而非个人能力不足。"""
    normalized_text_zh: str = """"""
    subject: str = "学堂会贵与官星学堂"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_58', 'bazi_semantic', 'bazi_structure_factor_59', 'bazi_semantic', 'bazi_state_factor_135', 'bazi_semantic', 'bazi_state_factor_136', 'bazi_semantic', 'bazi_relation_factor_60', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_学堂会贵与官星学堂_001_L1",
    )
    version: str = "1.0.0"
