"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654299
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
    semantic_id="zw_v1.0.0_安飞天三杀诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安飞天三杀诀(SemanticEntry):
    """
    - 分字分词释义：

  - **飞天三杀**：流年凶煞星群，按三合局对冲飞入。
  - **奏书**：三杀之一，主文书诉讼是非。
  - **将军**：三杀之一，主官非刑讼。
  - **直符**：...
    """
    
    original_text: str = """- 分字分词释义：

  - **飞天三杀**：流年凶煞星群，按三合局对冲飞入。
  - **奏书**：三杀之一，主文书诉讼是非。
  - **将军**：三杀之一，主官非刑讼。
  - **直符**：三杀之一，主灾祸意外。
  - **三合冲**：寅午戌、申子辰、亥卯未、巳酉丑四组三合局互相对冲。
  - **飞入**：凶煞星按规律落入特定宫位。

**主题**：流年三杀（奏书、将军、直符）。

#### 安星规则（三合冲）：

- 寅午戌年：飞入亥卯未宫
- 申子辰年：飞入巳酉丑宫
- 亥卯未年：飞入申子辰宫
- 巳酉丑年：飞入寅午戌宫

#### 完整对等诠释（secondary_lang_full·28飞天三杀）：

  The Flying Three Killers (Feitian Sansha) comprise Zoushu, Jiangjun, and Zhifu—three roving malefic stars whose annual placement follows the logic of Sanhe (three-harmony) opposition. In years belonging to the Yin-Wu-Xu frame, the killers fly into Hai-Mao-Wei palaces; in Shen-Zi-Chen years, they occupy Si-You-Chou; in Hai-Mao-Wei years, they land in Shen-Zi-Chen; and in Si-You-Chou years, they descend on Yin-Wu-Xu. When the Life Palace, Body Palace, or Fortune Palace falls within the sector invaded by the Three Killers for a given year, the native should exercise extra caution regarding litigation, accidents, and unexpected reversals. Benefic stars or strong principal stars in the same zone can mitigate the threat, but the killers remain a warning flag that deserves respect during annual forecasting."""
    normalized_text_zh: str = """"""
    subject: str = "安飞天三杀诀"
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_安飞天三杀诀_001_L1",
    )
    version: str = "1.0.0"
