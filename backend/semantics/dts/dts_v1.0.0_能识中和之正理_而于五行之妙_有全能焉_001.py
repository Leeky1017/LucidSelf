"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997488
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
    semantic_id="dts_v1.0.0_能识中和之正理_而于五行之妙_有全能焉_001",
    book_id="dts",
    engine_id="bazi"
)
class 能识中和之正理而于五行之妙有全能焉(SemanticEntry):
    """
    - **原文（source_text）**：
  能识中和之正理，而于五行之妙，有全能焉。

- 原注（原文注解）：
  　　中而且和，子平之要法，虽曰有病方为贵，无伤不是奇，然毕竟云：格中如去病，财...
    """
    
    original_text: str = """- **原文（source_text）**：
  能识中和之正理，而于五行之妙，有全能焉。

- 原注（原文注解）：
  　　中而且和，子平之要法，虽曰有病方为贵，无伤不是奇，然毕竟云：格中如去病，财禄两相随，则又中和矣，是必归于中和，乃为至贵，若身弱而财官旺也，取富贵不必于中也，用神强，亦取富贵不必于和也，偏气古怪，亦取富贵不必于中且和也，则以天下之财官，止有此数，而天下之人才，最邪巧也。

- 分字分词释义：
  - 中：不偏不倚之位；
  - 和：冲突调停之后的协调状态；
  - 有病方为贵：以“病”为用，借偏胜成奇；
  - 去病复中：祛其病处而返于中和之贵。

- **规范化释义（primary_lang_explained）**：
  子平之道，终归“中和”。虽有“以病为贵”“偏气亦贵”等特例，但那只是在有限资源下的权宜之计。若格局能先去其病，而财禄齐来，终归“中而且和”，是为至贵之局。身弱财官旺者、用神特强者、偏气古怪者皆可成贵，但其贵多偏、难全；惟能返于中和者，方堪称“五行之妙”之全能。

| 有病方为贵 | Disease brings Nobility | 以病为用 | Using defect as advantage | youbing_weigui | new_candidate |
| 去病 | Remove Disease | 去除病神 | Remove the offending element | qu_bing | new_candidate |
| 偏气 | Biased Qi | 气势偏一方 | Qi biased to one side | pian_qi | new_candidate |
| 全能 | All Capable | 五行圆满 | Fully capable via 5-elements | quan_neng | new_candidate |
| 至贵 | Ultimate Nobility | 最高贵气 | Highest nobility | zhi_gui | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Zhong-He (Middle-Harmony) is the ultimate principle. Although using "Disease" (Bing) or "Bias" (Pian) can bring nobility, true nobility returns to Zhong-He. If "remove disease" (Qu-Bing) leads to wealth/status, it is because it restores harmony. Biased nobility is limited; Balanced nobility is all-capable (全能)."""
    normalized_text_zh: str = """"""
    subject: str = "能识中和之正理，而于五行之妙，有全能焉。"
    factor_refs: list = []
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_能识中和之正理_而于五行之妙_有全能焉_001_L1",
    )
    version: str = "1.0.0"
