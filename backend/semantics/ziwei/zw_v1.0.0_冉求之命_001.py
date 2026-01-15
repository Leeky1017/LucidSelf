"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699084
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
    semantic_id="zw_v1.0.0_冉求之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 冉求之命(SemanticEntry):
    """
    - 分字分词释义：

  - **禄存守垣**：禄存星守命宫，主财禄丰厚。
  - **紫府加会**：紫微天府加会命宫，主终身福厚。
  - **卯生人忌巳**：卯年生人于巳宫限运有特定禁忌。
  -...
    """
    
    original_text: str = """- 分字分词释义：

  - **禄存守垣**：禄存星守命宫，主财禄丰厚。
  - **紫府加会**：紫微天府加会命宫，主终身福厚。
  - **卯生人忌巳**：卯年生人于巳宫限运有特定禁忌。
  - **丧门天虚冲命**：丧门天虚二凶星冲照命宫，主丧事虚耗。
  - **劫空白虎天哭**：多重凶星齐聚命宫，诸凶难逃。
  - **终身福厚**：禄存紫府格局的主要效应，一生福泽深厚。
  - **阴男土五局**：冉求命盘的五行局数，土五局主厚重稳健。

- **原文（source_text）**：  
  冉求之命。阴男土五局。禄存守垣，紫府加会，终身福厚。大限天伤，小限到巳，卯生人忌之，丧门、天虚冲命，劫空，合拱太岁、白虎、天哭在命，故此难逃也。

- **规范化释义（primary_lang_explained）**：  
  冉求命属阴男土五局，禄存守命垣、紫府加会，主终身福厚。然大限行天伤之地，小限到巳宫，卯生人于巳有忌；丧门、天虚、劫空、白虎、天哭齐聚于命，诸凶难逃而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Ran Qiu's Yin male Earth Fifth chart has Salary Keeper guarding court with Ziwei‑Tianfu convergence—lifelong blessings. Major period in Celestial Wound; minor at Si—Mao natives face taboos. Mourning Gate, Void, Robbery, White Tiger, Crying converge on Life. Inescapable malefics caused death.

- **核心要点**：  
  1. 禄存守垣、紫府加会，主终身福厚。  
  2. 卯生人忌巳限，大限天伤加重凶象。  
  3. 多重凶星齐聚，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **福厚之格**："禄存守垣，紫府加会，终身福厚"，冉求命主福厚。
  - **多凶齐聚**："丧门天虚冲命，劫空白虎天哭在命"，多重凶星齐聚难逃。
  - **生年忌限**："卯生人忌巳限"，卯年生人忌巳宫限运。
  - **现代应用**：福厚之命亦难逃多重凶星叠加——凶星数量与强度是关键风险指标。"""
    normalized_text_zh: str = """"""
    subject: str = "冉求之命"
    factor_refs: list = ['star_lucunshouyuan', 'pattern_zifujiahui', 'star_baihu', 'source_ref', 'rel_ranqiu_001', 'star_lucunshouyuan', 'rel_ranqiu_002', 'pattern_duochongxiong', 'rel_ranqiu_003', 'taboo_maoshengji', 'evi_ranqiu_001', 'pattern_duochongxiong', 'rule_duochongxiong', 'evi_ranqiu_002', 'taboo_maoshengji', 'rule_maoshengji', 'concept_multiple_malefics', 'concept_fuhou_pattern']
    
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
        l1_anchor="zw_v1.0.0_冉求之命_001_L1",
    )
    version: str = "1.0.0"
