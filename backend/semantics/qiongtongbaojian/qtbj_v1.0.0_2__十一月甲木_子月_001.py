"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619995
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
    semantic_id="qtbj_v1.0.0_2__十一月甲木_子月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2十一月甲木子月(SemanticEntry):
    """
    - **原文（source_text）**：
  十一月甲木，木性生寒，丁先庚后，丙火佐之。癸水司权，为火金之病。
  庚丁两透，支见巳寅，科甲有准，风水不及，选拔有之。若癸透伤丁，无戊己辅救，残疾之...
    """
    
    original_text: str = """- **原文（source_text）**：
  十一月甲木，木性生寒，丁先庚后，丙火佐之。癸水司权，为火金之病。
  庚丁两透，支见巳寅，科甲有准，风水不及，选拔有之。若癸透伤丁，无戊己辅救，残疾之人。
  或壬水重出，丁火全无者，庸人也，得丙方妙。
  或支成水局，加以壬透，名为水泛木浮，死无棺木。
  总之十一月甲木，为寒枝，不比春木清茂，耑取庚丁。透壬无丙，不过刀笔异途，武职有验。

- **分字分词释义**：
  - **木性生寒**：木的本性变得寒冷 / 子月特征 / 无生机
  - **丁先庚后**：先用丁火后用庚金 / 用神次序 / 暖木优先
  - **癸水司权**：癸水当权主事 / 子中藏癸 / 忌神
  - **火金之病**：火和金的病根 / 癸克火泄金 / 大忌
  - **寒枝**：寒冷的枝条 / 子月甲木状态 / 无生气
  - **水泛木浮**：水泛滥木漂浮 / 极凶格 / 死无棺木
  - **刀笔异途**：刀笔吏或异途出身 / 非正途 / 武职

- **规范化释义（primary_lang_explained）**：
  十一月（子月）的甲木，木性寒冷，先用丁火（暖/炼），后用庚金（辟甲），丙火作为佐助（调候）。癸水当权（子中癸水），是火和金的病（克火泄金）。
  如果庚金和丁火都透出，地支见巳（庚长生/丙禄）寅（甲禄/丙长生），科甲功名有准，即使风水不及，也是选拔人才。如果癸水透出伤害丁火，没有戊己土辅助救应，是残疾人（火灭金寒木冻）。
  如果壬水重重透出，完全没有丁火，是庸俗之人，必须得到丙火才妙（丙火不怕壬水）。
  如果地支合成水局，加上壬水透出，这叫“水泛木浮”，死无棺木（凶死）。
  总之十一月甲木，是寒枝，比不上春木的清秀茂盛，专门取庚金和丁火。如果透出壬水而没有丙火，不过是刀笔吏或异途出身，或者武职灵验。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 11th Month (Rat Month) is cold in nature. First use Ding, then Geng, with Bing assisting. Gui Water holds authority, which is the disease for Fire and Metal.
  If both Geng and Ding are revealed, and branches see Si/Yin, Civil Service is assured; even with poor Feng Shui, one is a selected talent. If Gui is revealed to hurt Ding, without Wu/Ji to assist/save, one becomes disabled.
  If Ren Water appears heavily and there is absolutely no Ding Fire, one is a mediocre person; obtaining Bing would be wondrous.
  If branches form a Water frame and Ren is revealed, it is "Water Flooding Wood Floating", implying death without a coffin.
  In summary, Jia Wood in the 11th Month is a "Cold Branch", not lush like Spring Wood; exclusively take Geng and Ding. If Ren is revealed without Bing, it is merely a clerk's path or alternative career, often verified in military posts.

- **核心要点**：
  - **首要用神**：丁火（暖/炼）。
  - **配合用神**：庚金（劈甲引丁）。
  - **佐助**：丙火（调候，尤其见壬时）。
  - **忌讳**：癸水（伤丁），壬水（泛木）。
  - **象义**：寒枝（Cold Branch）。

- **详细解说**：
  子月是冬至所在，一阳初生，但气候极寒。
  - 甲木此时无生机，全是寒气。必须火来解冻。
  - 丁火配合庚金（劈甲引丁）是最佳方案，能生火取暖。
  - 丙火虽然暖，但不及丁庚配合有力，但在见壬水时，丙火优于丁火（丙乃太阳，不怕江河；丁乃灯烛，怕水）。
  - 支见巳寅很重要，因为巳含丙庚，寅含甲丙，是火金的根基。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_161]` `[trigger: 子月甲木]` `[factor_trigger: month_zi AND tiangan_jia AND tiangan_ding AND tiangan_geng]` `[role: 主干]` 十一月甲木，木性生寒，丁先庚后，丙火佐之，癸水司权，为火金之病。 → 《穷通宝鉴·三冬甲木》#6.2
  - `[ns_qttbj_162]` `[trigger: 寒枝]` `[factor_trigger: month_zi AND tiangan_jia AND likes_ding_geng_combo]` `[role: 主干依赖]` 十一月甲木，为寒枝，不比春木清茂，耑取庚丁。 → 《穷通宝鉴·三冬甲木》#6.2
  - `[ns_qttbj_163]` `[trigger: 水泛木浮]` `[factor_trigger: month_zi AND tiangan_jia AND dizhi_water_frame AND ren_revealed]` `[role: 例外处理]` 支成水局，加以壬透，名为水泛木浮，死无棺木。 → 《穷通宝鉴·三冬甲木》#6.2
  - `[ns_qttbj_164]` `[trigger: 子月残疾]` `[factor_trigger: month_zi AND tiangan_jia AND gui_revealed AND tiangan_ding AND NOT (tiangan_wu OR tiangan_ji)]` `[role: 例外处理]` 若癸透伤丁，无戊己辅救，残疾之人。 → 《穷通宝鉴·三冬甲木》#6.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 十一月甲木（子月）"
    factor_refs: list = ['cold_branch', 'selection']
    
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
        l1_anchor="qtbj_v1.0.0_2__十一月甲木_子月_001_L1",
    )
    version: str = "1.0.0"
