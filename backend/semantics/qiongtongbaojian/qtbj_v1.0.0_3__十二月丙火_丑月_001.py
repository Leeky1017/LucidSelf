"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596831
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
    semantic_id="qtbj_v1.0.0_3__十二月丙火_丑月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3十二月丙火丑月(SemanticEntry):
    """
    - **原文（source_text）**：
  十二月丙火，气进二阳，侮雪欺霜，喜壬为用。己土司令，土多又不可少甲。
  壬甲两透，科甲堪宜，甲藏则秀才而已。或无甲得一壬透，富中取贵。
  如见一派...
    """
    
    original_text: str = """- **原文（source_text）**：
  十二月丙火，气进二阳，侮雪欺霜，喜壬为用。己土司令，土多又不可少甲。
  壬甲两透，科甲堪宜，甲藏则秀才而已。或无甲得一壬透，富中取贵。
  如见一派己土，不见甲乙，名为假伤官，聪明性傲，名利虚浮。
  或一派癸水，得己出干，必自主创业。若制伏太过，又取辛金作用。得见癸透。此人即不成名，必清雅文墨士。

- **分字分词释义**：
  - **气进二阳**：气机进入二阳 / 丑月特征 / 阳气增
  - **侮雪欺霜**：侮慢冰雪欺凌霜寒 / 丙火功能 / 驱寒
  - **己土司令**：己土掌管时令 / 丑月 / 土旺
  - **壬甲两透**：壬水甲木都透出 / 最佳配置 / 科甲
  - **假伤官**：假的伤官格 / 己多无甲 / 虚浮
  - **清雅文墨士**：清雅的文学士人 / 癸透 / 文贵

- **规范化释义（primary_lang_explained）**：
  十二月（丑月）的丙火，气进二阳（二阳进气），能够侮雪欺霜，喜欢壬水为用神（映照）。此时己土（伤官）司令，土多就不可少了甲木（疏土）。
  壬水和甲木都透出，科甲功名适宜，甲木藏支则只是秀才。如果无甲木但得到一个壬水透出，富中取贵。
  如果见到一派己土，不见甲乙木（印），叫"假伤官格"，其人聪明性格傲慢，名利虚浮。
  如果一派癸水（官杀），得到己土出干（伤官制杀），必自主创业。如果制伏太过（土多水少），又取辛金（财）作用（泄土生水）。如果能见到癸水透出，此人即使不成名，也必定是清雅的文墨之士。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 12th Month (Ox Month): Qi advances to Two Yangs; it defies snow and frost. It likes Ren as Useful God. Ji Earth commands; if Earth is abundant, Jia Wood cannot be lacking.
  If Ren and Jia are both revealed, Civil Service is suitable; if Jia is hidden, only a Xiucai. Without Jia but obtaining one Ren revealed, wealth with some nobility.
  If a mass of Ji Earth is seen without Jia/Yi, it is "Fake Hurting Officer"; the person is intelligent and arrogant, but fame and profit are hollow.
  If a mass of Gui Water appears and Ji reveals to control it, one will certainly start their own business. If control is excessive, take Xin Metal to act. If Gui is revealed, even if this person doesn't become famous, they will be a refined literary scholar.

- **核心要点**：
  - **气进二阳**：丑月丙火更有力。
  - **首要用神**：壬水（映照）。
  - **配合用神**：甲木（疏己土）。
  - **假伤官**：己土多无印，聪明傲慢虚浮。

- **详细解说**：
  - 丑月是湿土，晦火最甚。甲木是去晦的关键。
  - "气进二阳"：指临卦，阳气增长，丙火渐旺，故喜壬水。
  - "假伤官"：丙以己为伤官，丑月己土当令，伤官气旺，无印制约，故性傲空虚。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_260]` `[trigger: 丑月丙火]` `[factor_trigger: month_chou AND tiangan_bing AND tiangan_ren AND tiangan_jia AND qi_two_yang]` `[role: 主干]` 十二月丙火，气进二阳，侮雪欺霜，喜壬为用。己土司令，土多又不可少甲。 → 《穷通宝鉴·三冬丙火》#15.3
  - `[ns_qttbj_261]` `[trigger: 假伤官]` `[factor_trigger: month_chou AND tiangan_bing AND ji_multiple AND NOT tiangan_jia AND NOT tiangan_yi AND fake_hurting_officer]` `[role: 例外处理]` 见一派己土，不见甲乙，名为假伤官，聪明性傲，名利虚浮。 → 《穷通宝鉴·三冬丙火》#15.3
  - `[ns_qttbj_262]` `[trigger: 清雅文墨士]` `[factor_trigger: month_chou AND tiangan_bing AND tiangan_gui AND literary_scholar]` `[role: 条件分支]` 得见癸透，此人即不成名，必清雅文墨士。 → 《穷通宝鉴·三冬丙火》#15.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 十二月丙火（丑月）"
    factor_refs: list = ['fake_hurting_officer', 'qi_two_yang', 'literary_scholar']
    
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
        l1_anchor="qtbj_v1.0.0_3__十二月丙火_丑月_001_L1",
    )
    version: str = "1.0.0"
