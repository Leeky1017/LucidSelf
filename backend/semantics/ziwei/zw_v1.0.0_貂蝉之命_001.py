"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699999
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
    semantic_id="zw_v1.0.0_貂蝉之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 貂蝉之命(SemanticEntry):
    """
    - 分字分词释义：

  - **左右加会**：左辅右彼加会命局，本应有助力。
  - **巨门天同俱不得地**：巨门天同二星皆不在得力位置，根基薄弱。
  - **火铃二星冲照**：火星铃星从对宫冲...
    """
    
    original_text: str = """- 分字分词释义：

  - **左右加会**：左辅右彼加会命局，本应有助力。
  - **巨门天同俱不得地**：巨门天同二星皆不在得力位置，根基薄弱。
  - **火铃二星冲照**：火星铃星从对宫冲照命宫，主情欲。
  - **夫星陷背配三夫**：夫妻宫星曜落陷且与命局相背，婚姻不稳。
  - **天刑子息全无**：天刑落子女宫，主无子嗣。
  - **刑死**：以非正常方式死亡。
  - **阳女水二局**：貂蝉命盘的五行局数，水二局主智慧薄命。

- **原文（source_text）**：  
  貂蝉之命。阳女水二局。虽有左右加会，巨门、天同，俱不得地。火铃二星冲照，亦主淫欲。夫星陷背，配三夫，而心不为足，天刑子息全无，又无陀杀冲刑，小限太岁临于丑宫，主𮞸刑死。

- **规范化释义（primary_lang_explained）**：  
  貂蝉之命为阳女水二局，「虽有左右加会」但「巨门、天同，俱不得地」，命局根基不稳。「火铃二星冲照，亦主淫欲」，带来强烈欲望。「夫星陷背，配三夫，而心不为足」，婚姻不稳，三次婚配仍不满足。「天刑子息全无」，无子嗣。最终「小限太岁临于丑宫，主𮞸刑死」，以刑死收场。

- **完整对等诠释（secondary_lang_full）**：  
  Diaochan's chart is that of a Yang Water female. Although Zuo‑You provide support, Ju Men and Tian Tong both fall out of place. Fire and Bell stars strike the Life palace, amplifying desire. The Spouse star is debilitated; she matches with three husbands yet remains unsatisfied. Tian Xing in Children signals no offspring. Eventually, with minor period and Tai Sui on Chou, she dies by punishment.

- **核心要点**：  
  1. 左右加会但巨门天同俱不得地，根基薄弱。  
  2. 火铃冲照主淫欲，夫星陷背配三夫，天刑子息无子。  
  3. 小限太岁临丑宫，最终刑死。"""
    normalized_text_zh: str = """"""
    subject: str = "貂蝉之命"
    factor_refs: list = ['malefic_jumen_tiantong_budedi', 'malefic_huoling_chongzhao', 'malefic_fuxing_xianbei', 'quality_pei_sanfu', 'malefic_tianxing_zixi_wuzi', 'result_xingsi']
    
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
        l1_anchor="zw_v1.0.0_貂蝉之命_001_L1",
    )
    version: str = "1.0.0"
