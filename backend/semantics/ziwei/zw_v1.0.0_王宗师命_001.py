"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699830
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
    semantic_id="zw_v1.0.0_王宗师命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 王宗师命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫相朝垣**：紫微与天相朝向官垣，主高阶清贵官职。
  - **曲昌加会**：文曲与文昌加会命局，主文学声扬。
  - **刑妻无子**：对配偶与子女宫位形成刑克或虚...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫相朝垣**：紫微与天相朝向官垣，主高阶清贵官职。
  - **曲昌加会**：文曲与文昌加会命局，主文学声扬。
  - **刑妻无子**：对配偶与子女宫位形成刑克或虚耗，使婚姻与子嗣不美。
  - **大限㬍衰**：大限气势衰退，主晚年能量不足。
  - **太岁刑忌相并**：太岁与刑星、忌星同临，主该年冲突与阻碇叠加。
  - **天空败绝之地**：天空落于败绝宫位，主能量虚空、事功难成。
  - **阳男火六局**：王宗师命盘的五行局数，火六局主明亮宗师。

- **原文（source_text）**：  
  王宗师命。阳男火六局。此为紫相朝垣，曲昌加会，文学声扬，但刑妻无子，终身享高爵厚禄，寿至七一八，大限㭩衰，太岁刑忌相并，小限入天空败绝之地，故死。

- **规范化释义（primary_lang_explained）**：  
  王宗师命为阳男火六局，「紫相朝垣，曲昌加会」，主紫微与天相朝向官垣，文曲、文昌同来会照，是显赫文学声名与高阶官职之格。「宗师」二字点出其在学术或礼乐体系中的权威地位。  
  命局同时带「刑妻无子」之象，指婚姻与子嗣方面多有亏欠；虽然「终身享高爵厚禄」，但私生活并不圆满。原文「寿至七一八」疑为七十余岁的记法，可视作高寿。至大限气势衰退之时，太岁刑忌相并，小限又入天空败绝之地，是「刑忌叠加 + 虚空败绝」的晚年重凶组合，于是于此阶段死亡。

- **完整对等诠释（secondary_lang_full）**：  
  Wang Zongshi’s chart is that of a Yang Fire native in the Sixth Configuration. With Zi Wei and Tian Xiang facing the court and Wen Chang/Wen Qu converging, the "Zixiang with Chang‑Qu" pattern denotes literary brilliance and high office; his title "Grand Master" reflects institutional authority in scholarship or ritual.  
  The chart, however, carries signatures of "punishing the wife and lacking sons," indicating strain or loss in marriage and lineage. Despite "enjoying high rank and rich stipends throughout life," his private sphere is incomplete. The text records longevity "into the seventies" (the phrase "seven‑one‑eight" is likely a textual variant). As the major period declines, Tai Sui combines刑 and Ji, and the minor period enters a "Tian Kong defeat" sector. This overlay—late‑life weakening, punitive Ji‑influenced Tai Sui and void‑defeat minor periods—marks the time of death. The case illustrates public success with private incompleteness. 

- **核心要点**：  
  1. 紫相朝垣并得曲昌加会，是文学与官职兼隆的宗师格。  
  2. 命带刑妻无子，一生在婚姻与子嗣层面多有欠缺。  
  3. 高寿晚年在大限衰退、太岁刑忌并临、小限入天空败绝之地时死亡。"""
    normalized_text_zh: str = """"""
    subject: str = "王宗师命"
    factor_refs: list = ['pattern_zixiang_chaoyuan', 'pattern_quchang_jiahui', 'malefic_xingqi_wuzi', 'timing_daxian_shuai', 'timing_taisui_xingji', 'malefic_tiankong_baijue']
    
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
        l1_anchor="zw_v1.0.0_王宗师命_001_L1",
    )
    version: str = "1.0.0"
