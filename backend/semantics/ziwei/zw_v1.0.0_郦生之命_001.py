"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699253
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
    semantic_id="zw_v1.0.0_郦生之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 郦生之命(SemanticEntry):
    """
    - 分字分词释义：

  - **科权夹贵**：化科化权夹贵人星，本为美命。
  - **空劫夹垣**：地劫天空夹守命宫，使福禄打折。
  - **文昌与贪狼廉贞同立**：文昌与贪狼廉贞同宫，主奔波劳...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权夹贵**：化科化权夹贵人星，本为美命。
  - **空劫夹垣**：地劫天空夹守命宫，使福禄打折。
  - **文昌与贪狼廉贞同立**：文昌与贪狼廉贞同宫，主奔波劳碌。
  - **小船不堪重载**：比喻命主承载之责过重，超出格局所能负荷。
  - **太岁天伤**：流年太岁行至天伤宫位，主凶险。
  - **小限天空**：小限行至天空宫位，与太岁天伤叠加主凶。
  - **阴男土五局**：郦生命盘的五行局数，土五局主厚重辩才。

- **原文（source_text）**：  
  郦生之命。阴男土五局。科权夹贵之格，本为美命，只嫌空劫工夹垣，且文昌不宜，与贪狼、廉贞同立，生奔波劳碌。三十六，太岁天伤，小限天空，戊禄化吉，小舡不堪重载，是以凶也。

- **规范化释义（primary_lang_explained）**：  
  郦生命属阴男土五局，科权夹贵之格本为美命，然空劫夹垣、文昌与贪狼廉贞同立，主奔波劳碌。三十六岁太岁天伤、小限天空，小船不堪重载，故凶而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Li Sheng's Yin male Earth Fifth chart has Academic‑Authority flanking Noble—a fine destiny. But Void‑Robbery flank court; Wenchang with Tan Lang‑Lian Zhen indicates toil. At 36 Tai Sui at Wound, minor at Void. Small boat cannot bear heavy load. Death.

- **核心要点**：  
  1. 科权夹贵为美命，然空劫夹垣。  
  2. 文昌与贪狼廉贞同立，主奔波。  
  3. 太岁天伤、小限天空，为凶亡应期。

- **叙事素材（narrative_snippets）**：
  - **美命夹贵**："科权夹贵之格，本为美命"，郦生命主才名出众、本应前程光明。
  - **空劫夹垣**："只嫌空劫工夹垣"，空劫夹守命垣，使福禄打折、多有反复奔波。
  - **小船重载**："戊禄化吉，小舡不堪重载，是以凶也"，比喻命主承载之责过重，超出格局所能负荷。
  - **现代应用**：才华出众却背负过重责任者，在天伤天空之年宜学会止损与减负，避免“好命装太多事”而压垮自己。"""
    normalized_text_zh: str = """"""
    subject: str = "郦生之命"
    factor_refs: list = ['pattern_kequanjiagui', 'pattern_kongjiejiayuan', 'metaphor_xiaochuanzhongzai', 'source_ref', 'rel_lisheng_001', 'pattern_kequanjiagui', 'rel_lisheng_002', 'pattern_kongjiejiayuan', 'rel_lisheng_003', 'result_xiongwang', 'evi_lisheng_001', 'pattern_kongjiejiayuan', 'rule_kongjiejiayuan', 'concept_noble_flank', 'concept_void_robbery']
    
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
        l1_anchor="zw_v1.0.0_郦生之命_001_L1",
    )
    version: str = "1.0.0"
