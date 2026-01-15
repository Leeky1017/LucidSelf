"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042587
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
    semantic_id="smth_v1.0.0_戊土为霞_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊土为霞(SemanticEntry):
    """
    - **原文（source_text）**：
  戊土为霞。土无专气，依火而生；霞无定体，借日以现。知丙火之为日，则知戊土之为霞矣。是霞者，日之余也，日尽而霞将灭没；火熄则土无生意，故谓之霞也。如戊土...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊土为霞。土无专气，依火而生；霞无定体，借日以现。知丙火之为日，则知戊土之为霞矣。是霞者，日之余也，日尽而霞将灭没；火熄则土无生意，故谓之霞也。如戊土日主爱四柱带水，则为上格，霞水相辉而成文彩也；更喜年月干见癸，癸则为雨，雨后霞现而睹文明也。

- **分字分词释义**：
  - **依火而生**：戊土须得丙火照映，方显霞彩。
  - **日之余、霞将灭没**：喻戊土之美在于余晖，非正午烈照。
  - **霞水相辉**：水映霞光，色彩更显缤纷。

- **规范化释义（primary_lang_explained）**：
  戊土被喻为晚霞：本身并无光彩，需借丙日余晖而显色。日近西山之时，霞光满天，如火映土而成彩。这说明戊土的美多在「余势」里，在正午烈火之时反不宜。戊日命人若四柱多水，有「霞水相辉」之象；又见癸雨，则如雨后晚霞，更显文明绚烂。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth is pictured as evening cloud‑glow: earth that has no light of its own but shows colour when touched by the fading rays of the sun. When Bing Fire is high in the sky, Wu looks plain and even parched; as the sun moves toward the western hills, its surplus light is scattered through cloud and vapour so that the whole horizon fills with soft reds and golds. The value of Wu here lies in receiving and displaying the residual force of Fire, not in competing with it at noon. For a Wu‑day chart, plentiful Water in the pillars answers this image of “mist and glow shining on one another”, adding depth and richness to the scene; visible Gui, likened to rain, gives the classic picture of clear air after rain with fresh, cultured colours in the sky. In reading a life, this passage points to Wu Earth types who come into their own in consolidation and aftermath phases—styling, presenting, giving form to what has already been accomplished—rather than in raw, blazing beginnings, and whose refinement depends on a good balance of Fire, Water, and earthbound stability."""
    normalized_text_zh: str = """"""
    subject: str = "戊土为霞"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_戊土为霞_001_L1",
    )
    version: str = "1.0.0"
