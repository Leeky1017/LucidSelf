"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412805
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
    semantic_id="smth_v1.0.0_曲直与木局仁寿之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 曲直与木局仁寿之象(SemanticEntry):
    """
    - **原文（source_text）**：

  甲乙日得亥卯未局，柱中须有亥字带印为入格，若无亥有卯，止是木之本气，却要见金土为贵，既无亥字，又无金土，则木不秀不实，难以言贵。如甲寅日有亥，时见丁...
    """
    
    original_text: str = """- **原文（source_text）**：

  甲乙日得亥卯未局，柱中须有亥字带印为入格，若无亥有卯，止是木之本气，却要见金土为贵，既无亥字，又无金土，则木不秀不实，难以言贵。如甲寅日有亥，时见丁卯劫财、阳刃、伤官，虽贵不全合格。诗曰：甲乙日生亥卯未，局全曲直须荣贵，柱中无亥宜土金，自是生来享福地。又曰：甲乙生人寅卯辰，又名仁寿两堪评，亥卯未全嫌白帝，若逢坎位必身荣。

- 分字分词释义：

  - **曲直**：本为木德之象，既有枝干之“直”，亦有生长舒展之“曲”，引申为仁寿之气既端正而又灵活。
  - **甲乙日得亥卯未局**：日主为甲乙木，地支成亥卯未三合木局，木气成势，仁寿之象备具。
  - **须有亥字带印为入格**：亥为水，水生木，且亥中壬甲有印比之象；局中若见亥，等于为曲直格“接上源头之水”，方为真入格。
  - **无亥有卯，止是木之本气，却要见金土为贵**：仅有卯而无亥，木气虽有根却偏单，需以金官、土财来成其贵用。
  - **既无亥字，又无金土，则木不秀不实**：既无印源，又无财官，木气虽多却浮，难成“秀实”之质，故难言贵。
  - **仁寿两堪评**：仁为木德之本，寿为气脉绵长之象，指此格若得其真，多主品性仁厚而寿算不浅。

- **规范化释义（primary_lang_explained）**：

  曲直格，专就甲乙木日坐亥卯未木局的一类结构而言。甲乙木本主仁恕生发，若地支再会成亥卯未三合木局，则木气曲直相生，不仅有向上之干直，也有向四方舒展之曲枝，故原文以“仁寿两堪评”形容其人之德性与寿元。

  然而，成格的关键在于“亥印为源”：局中有亥字，则水能生木，印能护身，木气不至枯干；若无亥而仅有卯木，则只算木气本旺，还需金土财官来成贵象；若既无亥印，又无金土财官，则木虽多而无所依托，既不“秀”也不“实”，多为空长之木，难言高贵。原文又以甲寅日有亥、时见丁卯之例示意：虽可得贵，却因劫财、阳刃、伤官搅扰，格局不算纯粹。

- 核心要点：

  - 以**甲乙日 + 亥卯未木局**为基础，尤重亥水印星之存在。
  - 有亥印，则木得源头，曲直之气方成仁寿之象；无亥而有金土，则可由财官补其不及。
  - 木多而无印、无财官者，多主虚浮，不宜轻言大贵。

- 详细解说：

  曲直格体现的是“木德之美”在命局中的集中呈现。亥卯未合木局，如同一片林木相连：亥为根源之水与隐伏之根，卯为正旺之干，未为木气所依之土，三者合而成势，则日主之木不再是孤木，而是群林之象。在这种结构下，人多具仁厚、温和、重情的特质，同时也有一定的韧性与弹性。

  但若缺少亥印，则这片“林木”虽盛，却可能水源不足，表现为理想多而承载力有限；若再无金土来化用，便容易出现“有志而乏平台”的状况。原文强调见金土为贵，正是提醒需要通过现实的制度、责任（官星）与物质基础（财星），来承载木德之伸展，这样“曲直”之美才不至于停留在性情层面，而能落实为实际福禄。

- **校勘与字词辨析（双语）**：

  - 原文“甲乙日得亥卯未局，柱中须有亥字带印为入格”一句，本稿在释义中明确区分“真格”（有亥印）与“近格”（仅有卯木）。
  - “仁寿两堪评”“白帝”“坎位”等语，本稿分别理解为木德之仁与寿、金气之白、西方之象，以及坎位所代表之水地，不再逐一做术语式考据。
  - 诗句部分，本稿侧重提炼其“局全则贵、无亥宜金土、得坎位而荣”的结构要点，而非按字面句法逐句翻译。
  - **English**：
    - Meaning-based interpretation; not literal word-by-word translation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_177]` `[trigger: 曲直定义]` `[factor_trigger: quzhi_presence AND haimaowe_muju]` `[role: 主干]` 甲乙日得亥卯未局，柱中须有亥字带印为入格。 → 《三命通会》卷六#曲直
  - `[ns_smth_06_178]` `[trigger: 仁寿之象]` `[factor_trigger: mude_renshou AND changshou]` `[role: 主干依赖]` 又名仁寿两堪评。 → 《三命通会》卷六#曲直
  - `[ns_smth_06_179]` `[trigger: 无亥宜金土]` `[factor_trigger: wuhai_youmao AND jianjintu_weigui]` `[role: 条件分支]` 若无亥有卯，止是木之本气，却要见金土为贵。 → 《三命通会》卷六#曲直
  - `[ns_smth_06_180]` `[trigger: 木不秀不实]` `[factor_trigger: wuhai_wujintu AND mu_buxiu]` `[role: 总结]` 既无亥字，又无金土，则木不秀不实，难以言贵。 → 《三命通会》卷六#曲直"""
    normalized_text_zh: str = """"""
    subject: str = "曲直与木局仁寿之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_44', 'bazi_semantic', 'bazi_structure_wood', 'bazi_semantic', 'bazi_state_hai_degree', 'bazi_semantic', 'bazi_state_wood_degree', 'bazi_semantic', 'bazi_condition_metal_earth_condition', 'bazi_semantic', 'bazi_condition_wood_1', 'bazi_semantic', 'source_ref', 'rel_smth_06_160', 'quzhi_ge_presence', 'rel_smth_06_161', 'haizi_ruge', 'rel_smth_06_162', 'jintu_peihe', 'evi_smth_06_160', 'quzhi_ge_presence', 'rule_quzhi', 'evi_smth_06_161', 'haizi_ruge', 'rule_dahai', 'evi_smth_06_162', 'baidi_kemu_risk', 'rule_jinkemu', 'map_smth_06_107', 'map_smth_06_108']
    
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
        l1_anchor="smth_v1.0.0_曲直与木局仁寿之象_001_L1",
    )
    version: str = "1.0.0"
