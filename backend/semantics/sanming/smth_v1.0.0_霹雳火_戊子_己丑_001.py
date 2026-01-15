"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227773
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
    semantic_id="smth_v1.0.0_霹雳火_戊子_己丑_001",
    book_id="sanming",
    engine_id="bazi"
)
class 霹雳火戊子己丑(SemanticEntry):
    """
    - **原文（source_text）**：
  戊子己丑何以取象霹雳火？盖气在一阳，形居水位，水中之火，非神龙则无，故曰霹雳火。

- 分字分词释义：
  - **霹雳火**：雷霆之火，骤然而发，来...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊子己丑何以取象霹雳火？盖气在一阳，形居水位，水中之火，非神龙则无，故曰霹雳火。

- 分字分词释义：
  - **霹雳火**：雷霆之火，骤然而发，来去迅疾。
  - **水中之火**：在水位之中爆发的火，反差强烈。

- **规范化释义（primary_lang_explained）**：
  戊子、己丑之火，如雷霆霹雳：本居水位，却忽然一阳发动，光声大作。象征突发事件、剧烈转折与“极端条件下的点火”。

- **完整对等诠释（secondary_lang_full）**：

  Wuzi and Jichou are likened to "Thunderbolt Fire". Fire is here lodged in Water positions: a single point of Yang suddenly ignites in a watery setting, producing a flash of light and a crack of sound. The image is one of shocks, lightning strikes and turning points—brief in duration yet intense in impact. In charts, this Nayin often marks events or phases where change comes abruptly, under extreme or highly compressed conditions. Whether such thunderbolts become breakthroughs or disasters depends on the surrounding Earth and Metal: with solid structures and safeguards they can trigger necessary reform; without them they easily manifest as accidents, crises or blows that the system cannot absorb."""
    normalized_text_zh: str = """"""
    subject: str = "霹雳火（戊子、己丑）"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_霹雳火_戊子_己丑_001_L1",
    )
    version: str = "1.0.0"
