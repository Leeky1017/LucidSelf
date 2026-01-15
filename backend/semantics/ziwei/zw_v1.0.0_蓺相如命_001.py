"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699292
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
    semantic_id="zw_v1.0.0_蓺相如命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 蓺相如命(SemanticEntry):
    """
    - 分字分词释义：

  - **左右加会**：左辅右彼同会命宫，主辅佐之力。
  - **科禄紫府**：化科化禄与紫微天府会合，为最良格局。
  - **限行美地**：限运行到美地，一生名利安康。
...
    """
    
    original_text: str = """- 分字分词释义：

  - **左右加会**：左辅右彼同会命宫，主辅佐之力。
  - **科禄紫府**：化科化禄与紫微天府会合，为最良格局。
  - **限行美地**：限运行到美地，一生名利安康。
  - **子生人不宜寅申限**：子年生人逢寅申限有特定禁忌。
  - **丙申岁限**：六十九岁丙申年为命亡应期。
  - **名利安康**：左右科禄紫府格局的主要效应。
  - **阳男金四局**：蓺相如命盘的五行局数，金四局主刚断辩才。

- **原文（source_text）**：  
  蓺相如命。阳男金四局。左右加会，终为吉，科禄紫府最为良。且兼限行美地，一生名利得安康。大限申宫，子生人不宜寅申限，六十九岁，丙申岁限，是以命亡。

- **规范化释义（primary_lang_explained）**：  
  蔺相如命属阳男金四局，左右加会、科禄紫府为良格，限行美地，一生名利安康。然大限申宫，子生人不宜寅申限，六十九岁丙申岁限，故命亡。

- **完整对等诠释（secondary_lang_full）**：  
  Lin Xiangru's Yang male Metal Fourth chart has Left‑Right converge, Academic‑Salary Ziwei‑Tianfu—excellent pattern. Periods in fine positions, lifelong fame and wealth. Major at Shen—Zi natives shouldn't have Yin‑Shen periods. At 69 bing‑shen year period. Death.

- **核心要点**：  
  1. 左右加会、科禄紫府，一生名利安康。  
  2. 子生人不宜寅申限。  
  3. 六十九岁丙申岁限，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **名利安康**："左右加会，终为吉，科禄紫府最为良，且兼限行美地，一生名利得安康"，蔺相如命主一生功成名就而较少大波折。
  - **子生忌寅申**："大限申宫，子生人不宜寅申限"，点明子年生人逢寅申限的先天气机不顺。
  - **丙申岁限**："六十九岁，丙申岁限，是以命亡"，在整体平顺格局下，仍需关注特定岁限的隐性风险。
  - **现代应用**：事业平顺型命局，在生年忌限到来之年，应审慎做出重大迁徙、转职或权力交接决定，以免在看似平稳之时暗中折寿。"""
    normalized_text_zh: str = """"""
    subject: str = "蓺相如命"
    factor_refs: list = ['taboo_zishengyinshen', 'pattern_keluzifu', 'pattern_xianxingmeidi', 'source_ref', 'rel_linxiangru_001', 'pattern_zuoyoukelu', 'rel_linxiangru_002', 'taboo_zishengyinshen', 'rel_linxiangru_003', 'year_bingshen', 'evi_linxiangru_001', 'taboo_zishengyinshen', 'rule_zisheng_yinshen', 'concept_birth_taboo', 'concept_smooth_life']
    
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
        l1_anchor="zw_v1.0.0_蓺相如命_001_L1",
    )
    version: str = "1.0.0"
