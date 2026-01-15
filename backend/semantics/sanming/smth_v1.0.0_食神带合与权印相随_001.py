"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412530
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
    semantic_id="smth_v1.0.0_食神带合与权印相随_001",
    book_id="sanming",
    engine_id="bazi"
)
class 食神带合与权印相随(SemanticEntry):
    """
    - **原文（source_text）**：

  食神带合：谓甲人见丙有辛合，己人见辛有丙合，乙见丁壬，庚见壬丁，丙见戊癸，辛见癸戊之例，主为官有权印。

- 分字分词释义：

  - **食神带合...
    """
    
    original_text: str = """- **原文（source_text）**：

  食神带合：谓甲人见丙有辛合，己人见辛有丙合，乙见丁壬，庚见壬丁，丙见戊癸，辛见癸戊之例，主为官有权印。

- 分字分词释义：

  - **食神带合**：食神所临之干支，又与他干成合，如丙辛合水、丁壬合木、戊癸合火等。
  - **为官有权印**：合出的气象多与印、官相关，使命主在官场或组织中既有职权，又有凭信。
  - **甲见丙有辛合等例**：列举不同日主对应的食神与合神组合，说明“食神 + 合”的多种形态。

- **规范化释义（primary_lang_explained）**：

  食神本身偏向福寿与才情，当其又与他干成合时，往往象征这份才情被“制度化”“组织化”，转化为可以在官场或组织系统中使用的能力。原文因此以“为官有权印”概括：食神合出印、合出官，使命主既有表现空间，又能获得正式凭信与授权。

- 核心要点：

  - 食神带合，是**才华被制度接纳**的一种象。
  - 合出的五行若偏向印、官，则多主权柄与文凭；若偏向财，则多主以才致富。
  - 忌合煞过多或合出偏印、七煞而身弱，则易在复杂关系中消磨自身。

- 详细解说：

  在现代语境中，可以把食神带合理解为：个人的专业技能、创作能力，恰好与某个组织、制度或权力结构形成良性对接：

  - 例如研究人员的成果被体制采纳，进而获得职称与编制；
  - 艺术工作者的作品被官方机构认可，获得奖项与头衔；
  - 职场人士的专长被上级看重，得到晋升机会与实权岗位。

  若命局中印、官本就为用神，则食神带合往往是“润色与催化”；若印、官为忌，却因食神带合而被放大，则容易在名利场中纠缠过深，反失其本有之从容与自在。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_109]` `[trigger: 食神带合]` `[factor_trigger: shishen_daihe AND quanyin]` `[role: 主干]` 食神带合者，甲人见丙有辛合，主为官有权印。 → 《三命通会》卷六#食神带合与权印相随
  - `[ns_smth_06_110]` `[trigger: 才情制度化]` `[factor_trigger: caiqing_zhidu AND zuzhi_jieshou]` `[role: 主干依赖]` 食神带合，是才华被制度接纳之象，合出印官，使命主有表现空间。 → 《三命通会》卷六#食神带合与权印相随
  - `[ns_smth_06_111]` `[trigger: 带合风险]` `[factor_trigger: hesha_guoduo OR heshen_chongpo]` `[role: 条件分支]` 忌合煞过多或合出偏印七煞而身弱，则易在复杂关系中消磨自身。 → 《三命通会》卷六#食神带合与权印相随
  - `[ns_smth_06_112]` `[trigger: 带合结论]` `[factor_trigger: shishen_daihe AND yinguanweiyong]` `[role: 总结]` 食神带合于印官为用者，是润色与催化；于印官为忌者，易纠缠名利场中。 → 《三命通会》卷六#食神带合与权印相随

- **校勘与字词辨析（双语）**：

  - 原文只简列几组"食神 + 合神"组合，本稿在释义中以“才情被制度接纳”的抽象象义统摄。
  - “为官有权印”在此不必局限于古代官职，可泛指一切需要正式授权的职位与角色。
  - 各干支合化具体五行之细节，若涉复杂合化，本稿留待专业推命时再作展开，此处从略。
  - **English**：
    - Detailed case analysis is deferred to future fate-calculation sections; abbreviated here."""
    normalized_text_zh: str = """"""
    subject: str = "食神带合与权印相随"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_shishen_marker_1', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_hehua_degree_1', 'bazi_semantic', 'bazi_state_degree_10', 'bazi_semantic', 'bazi_condition_factor_167', 'bazi_semantic', 'bazi_condition_shishen', 'bazi_semantic', 'source_ref', 'rel_smth_06_082', 'shishen_daihe_presence', 'rel_smth_06_083', 'hehua_chenggong', 'rel_smth_06_084', 'heshen_chongpo_risk', 'evi_smth_06_082', 'shishen_daihe_presence', 'rule_daihe', 'evi_smth_06_083', 'quanyin_huode', 'rule_quanyin', 'evi_smth_06_084', 'heshen_chongpo_risk', 'rule_chongpo', 'map_smth_06_053', 'map_smth_06_054']
    
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
        l1_anchor="smth_v1.0.0_食神带合与权印相随_001_L1",
    )
    version: str = "1.0.0"
