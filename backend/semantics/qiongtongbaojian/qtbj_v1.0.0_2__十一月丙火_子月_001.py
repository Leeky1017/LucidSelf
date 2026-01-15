"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596821
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
    semantic_id="qtbj_v1.0.0_2__十一月丙火_子月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2十一月丙火子月(SemanticEntry):
    """
    - **原文（source_text）**：
  十一月丙火，冬至一阳生，弱中复强，壬水为最，戊土佐之。
  壬戊两透，科甲可许，无戊见己，异路功名。或无壬水，有癸出干得金滋无伤，又有丙透以解冻，可许...
    """
    
    original_text: str = """- **原文（source_text）**：
  十一月丙火，冬至一阳生，弱中复强，壬水为最，戊土佐之。
  壬戊两透，科甲可许，无戊见己，异路功名。或无壬水，有癸出干得金滋无伤，又有丙透以解冻，可许衣衿。
  或一派壬，则耑用戊土，此人虽不成名，文章迈众，但名利虚浮。何也？因戊晦光，又须甲木为药也。或无壬水，癸亦可用，但不甚显。
  或四柱多壬无甲，乃作弃命从杀，亦有云路。
  或水多、有甲、无戊，却非从杀，宜用己土浊壬，十一月丙火，与十月颇同。

- **分字分词释义**：
  - **冬至一阳生**：冬至节一阳开始复生 / 子月气机 / 转进
  - **弱中复强**：弱势中恢复强气 / 丙火进气 / 转机
  - **壬戊两透**：壬水戊土都透出 / 最佳配置 / 科甲
  - **衣衿**：衣服衿领 / 秀才代称 / 小功名
  - **文章迈众**：文章超越众人 / 戊制壬 / 才华
  - **名利虚浮**：名利不实际 / 戊晦光 / 缺陷
  - **云路**：青云之路 / 从杀格 / 高官

- **规范化释义（primary_lang_explained）**：
  十一月（子月）的丙火，冬至一阳生，丙火在弱中恢复强气（气机），壬水为最重要（映照/既济），戊土辅佐（制水/护火）。
  壬水和戊土两透，可以许诺科甲。没有戊土见到己土，异路功名。如果无壬水，有癸水出干且得到金滋润而无伤，又有丙火透出解冻（暖局），可以许诺衣衿（秀才）。
  如果一派壬水，就专门用戊土（食神制杀），这人虽然不成名（科举），文章超越众人，但名利虚浮。为什么呢？因为戊土晦暗丙火的光芒，又必须用甲木作为药（疏土）。如果无壬水，癸水也可以用，但不显赫。
  如果四柱多壬水而无甲木，当作“弃命从杀”，也有云路（高官）。
  如果水多、有甲木、无戊土，就不是从杀，适宜用己土混浊壬水。十一月丙火，与十月颇为相同。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 11th Month (Rat Month): Winter Solstice brings One Yang; strength returns within weakness. Ren Water is best, with Wu Earth assisting.
  If Ren and Wu are both revealed, Civil Service is promised. Without Wu but seeing Ji, alternative fame. Without Ren, if Gui is revealed and nourished by Metal, and Bing is revealed to unfreeze, a scholarly degree is promised.
  If there is a mass of Ren, exclusively use Wu Earth. Though not famous via exams, this person's essays surpass the crowd, yet fame/profit are hollow. Why? Because Wu obscures the Light; Jia Wood is needed as medicine. Without Ren, Gui is usable but not prominent.
  If pillars have much Ren and no Jia, it is "Abandon Life Follow Killing", also leading to a high path.
  If Water is abundant, with Jia, and without Wu, it is not Follow Killing; use Ji to muddy the Ren. 11th Month Bing is quite similar to the 10th Month.

- **核心要点**：
  - **冬至一阳生**：子月虽寒，但丙火气机转进。
  - **首要用神**：壬水（映照）。
  - **制杀**：壬多用戊。但戊晦光，需甲疏。
  - **从杀**：壬多无甲。

- **详细解说**：
  - 子月水最旺。
  - 壬水映照是丙火本性，但子月水太旺易灭火，故需戊土堤坝。
  - 这里的矛盾在于：戊土既能制水（好），又能晦火（坏）。解决矛盾的钥匙是甲木（疏土/化杀）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_257]` `[trigger: 子月丙火]` `[factor_trigger: month_zi AND tiangan_bing AND tiangan_ren AND tiangan_wu AND one_yang_born]` `[role: 主干]` 十一月丙火，冬至一阳生，弱中复强，壬水为最，戊土佐之。 → 《穷通宝鉴·三冬丙火》#15.2
  - `[ns_qttbj_258]` `[trigger: 戊晦光]` `[factor_trigger: month_zi AND tiangan_bing AND ren_multiple AND tiangan_wu AND wu_obscures_light]` `[role: 例外处理]` 一派壬，则耑用戊土，此人虽不成名，文章迈众，但名利虚浮。何也？因戊晦光。 → 《穷通宝鉴·三冬丙火》#15.2
  - `[ns_qttbj_259]` `[trigger: 云路]` `[factor_trigger: month_zi AND tiangan_bing AND ren_multiple AND NOT tiangan_jia AND pattern_abandon_life_follow_killing]` `[role: 条件分支]` 四柱多壬无甲，乃作弃命从杀，亦有云路。 → 《穷通宝鉴·三冬丙火》#15.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 十一月丙火（子月）"
    factor_refs: list = ['cloud_path', 'yi_jin']
    
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
        l1_anchor="qtbj_v1.0.0_2__十一月丙火_子月_001_L1",
    )
    version: str = "1.0.0"
