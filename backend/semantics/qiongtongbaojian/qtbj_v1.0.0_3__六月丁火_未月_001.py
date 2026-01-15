"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596897
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
    semantic_id="qtbj_v1.0.0_3__六月丁火_未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3六月丁火未月(SemanticEntry):
    """
    - **原文（source_text）**：
  六月之丁，阴柔退气，但值三伏生寒，丁弱极矣，专取甲木，壬水次之。
  若得甲出天干，支成木局，见亥中之壬，为木神有根，接引丁火，必然科甲。即不见木局，...
    """
    
    original_text: str = """- **原文（source_text）**：
  六月之丁，阴柔退气，但值三伏生寒，丁弱极矣，专取甲木，壬水次之。
  若得甲出天干，支成木局，见亥中之壬，为木神有根，接引丁火，必然科甲。即不见木局，支见壬水，虽不大贵，亦有凌云之气，无庚不妙。
  或支成水局，见水透干，则湿木性，不能引丁，必为平人，有甲透、亦有才干。有庚透、方无刑伤。若无甲木，假名假利，虽能生财，固执懦夫。
  或年月日时，皆一派丁未之类，此为纯阴，终无大用。

- **分字分词释义**：
  - **阴柔退气**：阴性柔弱气势衰退 / 未月丁火 / 极弱
  - **三伏生寒**：三伏天生起寒气 / 夏末阴生 / 转衰
  - **木神有根**：木的精神有根基 / 亥中壬水 / 吉象
  - **接引丁火**：接续引燃丁火 / 甲木功能 / 生身
  - **凌云之气**：冲上云霄的志气 / 高远 / 贵象
  - **假名假利**：虚假的名利 / 无甲 / 凶象
  - **固执懦夫**：固执的懦夫 / 无印 / 性格缺陷
  - **纯阴**：纯粹的阴性 / 丁未四柱 / 无大用

- **规范化释义（primary_lang_explained）**：
  六月（未月）的丁火，阴柔退气，但正值三伏天生起寒气（阴气生），丁火极弱，专门取甲木（印）生身，壬水（官）次之（滋甲）。
  如果得到甲木透出天干，地支合成木局，见到亥中的壬水（亥卯未木局），使木神有根，接引丁火，必然中科甲。即使不见木局，地支见到壬水（生甲），虽然不大贵，也有凌云的志气，但没有庚金（劈甲）就不妙（木旺需金修剪，或土旺需金泄）。
  如果地支合成水局，见到水透干，就会湿了木性，不能引燃丁火，必定是平人。如果有甲木透出，也有才干。有庚金透出，才没有刑伤。如果没有甲木，只是假名假利，虽然能生财，但是固执的懦夫。
  如果年月日时，都是一派丁未之类，这是“纯阴”（丁未纳音水？或指丁、未皆阴），终究没有大用。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire in the 6th Month (Goat Month): Yin and soft, Qi retreats; with Three Fu Days generating Cold, Ding is extremely weak. Exclusively take Jia Wood, with Ren Water as secondary.
  If Jia is revealed and branches form a Wood frame, seeing Ren in Hai (feeding Wood), Wood spirit is rooted and ignites Ding; Civil Service is certain. Even without a Wood frame, seeing Ren in branches implies ambition reaching the clouds, though not greatly noble; without Geng, it is not good.
  If branches form a Water frame and Water reveals, it wets the Wood nature and cannot ignite Ding; surely an ordinary person. With Jia revealed, one has talent. With Geng revealed, one avoids punishment/injury. Without Jia, fame and profit are fake; though able to generate wealth, one is stubborn and cowardly.
  If Year/Month/Day/Hour are all Ding-Wei, this is Pure Yin, ultimately of no great use.

- **核心要点**：
  - **首要用神**：甲木（引火）。未月火衰土燥，甲木生身制土。
  - **次要用神**：庚金（劈甲/财）。木旺需金。
  - **湿木伤丁**：水局水透，木湿无焰，平常人。
  - **纯阴**：丁未一气，纯阴无阳，无大用。

- **详细解说**：
  - 未月丁火，余火也。
  - 此时最喜甲木，因未为木库，有根。
  - 所谓“三伏生寒”，是指夏至后一阴生，未月二阴生，丁火体弱，故喜生扶。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_279]` `[trigger: 未月丁火]` `[factor_trigger: month_wei AND tiangan_ding AND tiangan_jia AND three_fu_cold]` `[role: 主干]` 六月之丁，阴柔退气，但值三伏生寒，丁弱极矣，专取甲木，壬水次之。 → 《穷通宝鉴·三夏丁火》#17.3
  - `[ns_qttbj_280]` `[trigger: 木神有根]` `[factor_trigger: month_wei AND tiangan_ding AND tiangan_jia AND dizhi_wood_frame AND dizhi_hai AND wood_god_rooted]` `[role: 条件分支]` 甲出天干，支成木局，见亥中之壬，为木神有根，接引丁火，必然科甲。 → 《穷通宝鉴·三夏丁火》#17.3
  - `[ns_qttbj_281]` `[trigger: 纯阴无用]` `[factor_trigger: tiangan_all_yin AND dizhi_all_yin AND pure_yin]` `[role: 例外处理]` 年月日时，皆一派丁未之类，此为纯阴，终无大用。 → 《穷通宝鉴·三夏丁火》#17.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 六月丁火（未月）"
    factor_refs: list = ['pure_yin', 'cloud_ambition']
    
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
        l1_anchor="qtbj_v1.0.0_3__六月丁火_未月_001_L1",
    )
    version: str = "1.0.0"
