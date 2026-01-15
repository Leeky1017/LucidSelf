"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228636
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
    semantic_id="smth_v1.0.0_乙巳覆灯火_临官之火纯阳巽发_001",
    book_id="sanming",
    engine_id="bazi"
)
class 乙巳覆灯火临官之火纯阳巽发(SemanticEntry):
    """
    - **原文（source_text）**：
  乙巳临官之火，水不能克，盖水绝于巳，得水济之，则为纯粹，若得二三火助之亦佳。五行要论云：乙巳火含纯阳巽发之气，光辉充实，春冬向吉，夏秋向凶。

- *...
    """
    
    original_text: str = """- **原文（source_text）**：
  乙巳临官之火，水不能克，盖水绝于巳，得水济之，则为纯粹，若得二三火助之亦佳。五行要论云：乙巳火含纯阳巽发之气，光辉充实，春冬向吉，夏秋向凶。

- **分字分词释义**：
  - **临官之火**：临官位的火。
  - **水绝于巳**：水在巳位绝灭。
  - **得水济之**：得到水来帮助。
  - **纯粹**：纯净完美。
  - **纯阳巽发**：纯阳之气从巽方发出。
  - **光辉充实**：光辉充实饱满。
  - **春冬向吉**：春冬季节趋向吉利。

- **规范化释义（primary_lang_explained）**：
  乙巳是临官的火，水不能克制它，因为水在巳位绝灭。如果得到水来帮助，就会纯净完美，如果得到两三个火来帮助也很好。五行要论说：乙巳火包含纯阳之气从巽方发出，光辉充实饱满，春冬季节趋向吉利，夏秋季节趋向凶险。

- **完整对等诠释（secondary_lang_full）**：
  Yisi is official-position fire, Water cannot overcome, since water extinct at Si. Obtaining Water assisting, then pure-perfect. If obtaining two-three Fires assisting also excellent. Five Elements Essential Discourse says: Yisi Fire contains pure-yang Xun-manifesting energy, radiance full-substantial, spring-winter toward-auspicious, summer-autumn toward-inauspicious.

- **核心要点**：
  - 乙巳为覆灯火，临官之火
  - 巳为水绝地故水不克
  - 得水济反而纯粹
  - 得二三火助亦佳
  - 纯阳巽发、光辉充实
  - 春冬向吉、夏秋向凶

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_237]` `[trigger: 乙巳火性质]` `[factor_trigger: yisi_official_position_fire AND pure_yang_xun_manifesting_radiance_full AND spring_winter_auspicious_summer_autumn_inauspicious]` `[role: 主干]` 乙巳临官之火，水不能克，盖水绝于巳，得水济之，则为纯粹，若得二三火助之亦佳。五行要论云：乙巳火含纯阳巽发之气，光辉充实，春冬向吉，夏秋向凶。 → 《三命通会》卷一#乙巳火性质

- **详细解说**：
  此条详论乙巳（覆灯火）的性质。乙巳是临官的火（巳为火临官），水不能克（因巳为水绝地），得水济之反而纯粹（水火既济），得二三火助也好。五行要论强调乙巳火含纯阳巽发之气，光辉充实，春冬向吉（火需温暖）、夏秋向凶（火太旺）。这是论述临官火的特殊性与水火既济原理。

- **校勘与字词辨析（双语）**：
  - **中文**："临官"为十二长生之一，主旺盛。"水绝于巳"，巳为水绝地。"纯阳巽发"，巽为东南，火从东南而发。"向吉"指趋向吉利。
  - **English**: "Official-position" is one of Twelve Longevity stages, indicating prosperity. "Water extinct at Si" means Si is water's extinction position. "Pure-yang Xun-manifesting" means fire manifests from southeast (Xun). "Toward-auspicious" means trending toward auspiciousness."""
    normalized_text_zh: str = """"""
    subject: str = "乙巳覆灯火：临官之火纯阳巽发"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_乙巳覆灯火_临官之火纯阳巽发_001_L1",
    )
    version: str = "1.0.0"
