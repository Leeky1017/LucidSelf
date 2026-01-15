"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997445
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
    semantic_id="dts_v1.0.0_何谓冲_001",
    book_id="dts",
    engine_id="bazi"
)
class 何谓冲(SemanticEntry):
    """
    - **原文（source_text）**：
  何谓冲。

- **核心要点**：
  - 运岁地支相冲为“冲”，看哪一方党援与干头更强；
  - 喜神一方得势，多为“冲去忌神”；
  - 忌神一方...
    """
    
    original_text: str = """- **原文（source_text）**：
  何谓冲。

- **核心要点**：
  - 运岁地支相冲为“冲”，看哪一方党援与干头更强；
  - 喜神一方得势，多为“冲去忌神”；
  - 忌神一方得势，多为“冲坏用神或格局”。

- 详细解说：
  本条从“党援多少”“干头助谁”两个角度细化冲局的判断。子午等六冲若只是表面相冲、双方皆弱，则多为虚冲；若一方得令通根且站在用神阵营，则冲多表现为替命局“打开一条路”，把不利之神冲掉；反之，若强方为忌神，则冲往往直指用神或整体结构。

- 校勘与字词辨析：
  - “运冲岁/岁冲运”：仅指运支与岁支构成六冲，不含其他刑害。

- 原注（原文注解）：
  　　如子运午年，谓之运冲岁，日主喜子，则要助子，又得年干乃制午之神更妙，若午之党多，或干头遇丙戊甲者必凶。  
  　　如午运子年，谓之岁冲运，日干喜午而子之党多，干头又助子，必凶。  
  　　日干喜子，而午之党少，干头亦不助午，必吉。若午重子轻，则岁不降，亦无咎（其势已成，岁力不能为祸）。

- **规范化释义（primary_lang_explained）**：
  运岁相冲，仍以“喜忌+党援+干头助谁”判吉凶。喜神一方若有党援且得干头助制彼方，多吉；反之则凶。若强弱悬殊，弱方难以致祸，虽不降亦无咎。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 冲 | Clash (Chong) | 岁运地支相冲 | Earthly branch clash between Yun and Sui | dizhi_chong | existing |
| 运冲岁 | Yun Clashes Sui | 运支冲岁支 | Decade branch clashes annual branch | yun_chong_sui | new_candidate |
| 岁冲运 | Sui Clashes Yun | 岁支冲运支 | Annual branch clashes decade branch | sui_chong_yun | new_candidate |
| 党援 | Party Support | 同类之助 | Support from same kind/roots | dang_yuan | new_candidate |
| 干头助 | Heaven Stem Backing | 天干盖头之助 | Support from covering heaven stem | gantou_zhu | new_candidate |
| 强弱悬殊 | Huge Disparity | 力量差距过大 | Power difference too large | qiangruo_xuanshu | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Chong (Clash) between Yun and Sui (e.g. Zi-Wu clash)运岁相冲 context-dependent: 运冲岁 Yun-clashes-Sui or 岁冲运 Sui-clashes-Yun determined by 喜忌 favors/disfavors, 党援 party-support, and 干头 heaven-stem-backing. If 喜神 favored-god has support and heaven-stem help, it wins (lucky); if 忌神 disfavored-god has support, it wins (unlucky). When 强弱悬殊 disparity-is-huge (e.g. strong Wu vs weak Zi), the weak cannot cause chaos (no disaster)."""
    normalized_text_zh: str = """"""
    subject: str = "何谓冲"
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
        l1_anchor="dts_v1.0.0_何谓冲_001_L1",
    )
    version: str = "1.0.0"
