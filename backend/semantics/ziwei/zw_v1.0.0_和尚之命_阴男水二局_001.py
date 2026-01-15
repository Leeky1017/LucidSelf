"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699746
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
    semantic_id="zw_v1.0.0_和尚之命_阴男水二局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 和尚之命阴男水二局(SemanticEntry):
    """
    - 分字分词释义：

  - **巨机酉上化吉**：巨门、天机在酉宫得吉化，主聪慧与财官机缘。
  - **不终俗人发达**：命主不在俗世仕途中终老，而是转向出世道路。
  - **终天空门享福**：...
    """
    
    original_text: str = """- 分字分词释义：

  - **巨机酉上化吉**：巨门、天机在酉宫得吉化，主聪慧与财官机缘。
  - **不终俗人发达**：命主不在俗世仕途中终老，而是转向出世道路。
  - **终天空门享福**：以出家、修行的形式承受福报，而非俗世荣华。
  - **大限遇擎羊**：大限行至擎羊之位，主刚烈突发之冲击。
  - **空劫并夹**：空、劫等星并夹命垣或关键宫位，主根基被抽空。
  - **是以主死**：多重凶象叠加，故主死亡。
  - **阴男水二局**：此和尚命盘的五行局数，水二局主智慧出世。

- **原文（source_text）**：  
  和尚之命。阴男水二局。巨机酉上化吉者，便有财官也，不终俗人发达，终夭空门享福曹隆。五十一岁，大限遇擎羊，小限到命垣，太岁在空劫并夹之地，是以主死。

- **规范化释义（primary_lang_explained）**：  
  此命为阴男水二局，「巨机酉上化吉」意指巨门、天机在酉位得吉化，本可成就财官之职，有相当才干与资源；但命例明示其「不终俗人发达，终夭空门」，说明命主并非在俗世仕途、财官体系中终老，而是转入空门为僧，在出世道路上享受另一种福分。  
  五十一岁时，大限遇擎羊，小限又到命垣，太岁行于空劫并夹之地，是「擎羊 + 空劫夹命」的重凶组合：擎羊主刚烈突发之冲，空劫夹命则有根基被抽空、气数被拔除之象。于是命主于此岁死亡，完成「俗世未竟、空门享福而终」的人生轨迹。

- **完整对等诠释（secondary_lang_full）**：  
  This monk’s chart is that of a Yin Water native in the Second Configuration. With Ju Men and Tian Ji in You receiving benefic transformation, the pattern "Ju‑Ji in You turning auspicious" could have supported a life of wealth and office. Yet the text states that he "does not complete secular advancement" but dies within the monastic life, "enjoying blessings in the empty gate"—a shift from worldly career to a religious path.  
  At fifty‑one the major period meets Qing Yang, the minor period reaches the Life palace, and Tai Sui falls in a region where Kong and Jie form a clamp. This mix of Blade‑type force with an emptiness‑and‑robbery clamp—"Yang plus empty‑robbery surrounding Life"—indicates a sharp, terminal disruption of vitality. The chart thus describes a person whose latent capacity for worldly success is ultimately expressed through monastic existence, ending in a year of heavy affliction.

- **核心要点**：  
  1. 巨机酉上化吉，本可成就财官，却转而以出家为主要人生路径。  
  2. 五十一岁大限擎羊、小限命垣、太岁空劫夹命，构成终结性重凶。  
  3. 命例呈现「俗缘未竟而终夭空门」的出世型命局。"""
    normalized_text_zh: str = """"""
    subject: str = "和尚之命（阴男水二局）"
    factor_refs: list = ['pattern_juji_you_huaji', 'quality_buzhong_suren', 'quality_kongmen_xiangfu', 'timing_daxian_qingyang', 'malefic_kongjie_bingjia', 'result_shiyi_zhusi']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_和尚之命_阴男水二局_001_L1",
    )
    version: str = "1.0.0"
