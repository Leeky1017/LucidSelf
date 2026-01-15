"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699055
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
    semantic_id="zw_v1.0.0_端木赐命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 端木赐命(SemanticEntry):
    """
    - 分字分词释义：

  - **禄存坐命未宫**：禄存星坐守命宫于未宫，主财禄丰厚。
  - **暗禄会合**：暗禄与命宫会合，增强财禄格局。
  - **兔埋蛇地**：卯年生人入巳亥限运的凶象，生...
    """
    
    original_text: str = """- 分字分词释义：

  - **禄存坐命未宫**：禄存星坐守命宫于未宫，主财禄丰厚。
  - **暗禄会合**：暗禄与命宫会合，增强财禄格局。
  - **兔埋蛇地**：卯年生人入巳亥限运的凶象，生年忌限的典型表述。
  - **丧门忌会**：丧门星与忌星会合命宫，主丧事凶象。
  - **太岁相冲**：流年太岁与命宫相冲，为凶险年份。
  - **富贵之论**：禄存暗禄会合的富贵格局。
  - **阴男土五局**：子贡命盘的五行局数，土五局主厚重商才。

- **原文（source_text）**：  
  端木赐命。阴男土五局。禄存坐命未宫，暗禄会合，为富贵之论。卯生人防于巳亥限，三十五岁，大限入亥，四十一岁，小限入巳，兔埋蛇地，更为凶，太岁相冲，丧门忌会，是以凶也，故死。

- **规范化释义（primary_lang_explained）**：  
  端木赐（子贡）命属阴男土五局，禄存星坐命于未宫，又有暗禄会合，本为富贵之格。然卯年生人须防巳亥限，三十五岁大限入亥、四十一岁小限入巳，"兔埋蛇地"凶象加重，太岁相冲、丧门忌会，遂于此年殁。

- **完整对等诠释（secondary_lang_full）**：  
  Duanmu Ci (Zigong) has a Yin male Earth Fifth Configuration. Salary Keeper occupies Life palace in Wei with hidden salary combinations—a wealth pattern. Mao‑year natives must beware Si and Hai periods. At 35 the major period enters Hai; at 41 minor enters Si—"Rabbit buried in Snake territory". Tai Sui clashes Life, Mourning Gate and taboo converge, leading to death.

- **核心要点**：  
  1. 禄存坐命未宫、暗禄会合，主富贵。  
  2. 卯生人忌巳亥限，"兔埋蛇地"为凶象。  
  3. 太岁冲命、丧门忌会，为寿终应期。

- **叙事素材（narrative_snippets）**：
  - **富贵之格**："禄存坐命未宫，暗禄会合"，子贡命主富贵。
  - **兔埋蛇地**："卯生人防于巳亥限，兔埋蛇地更为凶"，生年忌限的典型凶象。
  - **寿终应期**："太岁相冲，丧门忌会"，诸凶会聚为寿终时点。
  - **现代应用**：富贵格须知生年忌限——某些生年对特定限运有天然忌讳。"""
    normalized_text_zh: str = """"""
    subject: str = "端木赐命"
    factor_refs: list = ['star_lucunzuoming', 'pattern_tumaishedi', 'star_sangmen', 'source_ref', 'rel_duanmu_001', 'star_lucunzuoming', 'rel_duanmu_002', 'pattern_tumaishedi', 'rel_duanmu_003', 'star_sangmen', 'evi_duanmu_001', 'pattern_tumaishedi', 'rule_tumaishedi', 'evi_duanmu_002', 'star_sangmen', 'rule_sangmen_si', 'concept_birth_taboo', 'concept_mourning']
    
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
        l1_anchor="zw_v1.0.0_端木赐命_001_L1",
    )
    version: str = "1.0.0"
