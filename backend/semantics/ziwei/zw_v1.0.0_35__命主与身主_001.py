"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654334
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
    semantic_id="zw_v1.0.0_35__命主与身主_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 35命主与身主(SemanticEntry):
    """
    - 分字分词释义：

  - **命主**：由命宫地支决定的主星，主先天命运框架。
  - **身主**：由生年地支决定的主星，主后天修为倾向。
  - **子宫贪狼**：命宫在子宫者，命主为贪狼星。...
    """
    
    original_text: str = """- 分字分词释义：

  - **命主**：由命宫地支决定的主星，主先天命运框架。
  - **身主**：由生年地支决定的主星，主后天修为倾向。
  - **子宫贪狼**：命宫在子宫者，命主为贪狼星。
  - **子午火铃**：生于子年或午年者，身主为火铃星。
  - **先天**：与生俱来的禀赋与潜质。
  - **后天**：通过努力与环境培养的特质。

#### 命主（论命宫所在支）：

- 子宫：贪狼
- 丑亥：巨门
- 寅戌：禄存
- 卯酉：文曲
- 辰申：廉贞
- 巳未：武曲
- 午宫：破军

#### 身主（论生年支）：

- 子午：火铃
- 丑未：天相
- 寅申：天梁
- 卯酉：天同
- 辰戌：文昌
- 巳亥：天机

#### 完整对等诠释（secondary_lang_full·34-35命主身主）：

  The Dual Ruler system assigns two personal governor stars to every chart. Mingzhu (Life Ruler) is determined by the earthly branch of the Life Palace: Zi gives Tanlang; Chou and Hai give Jumen; Yin and Xu give Lucun; Mao and You give Wenqu; Chen and Shen give Lianzhen; Si and Wei give Wuqu; Wu gives Pojun. Shenzhu (Body Ruler) is determined by the birth-year branch: Zi-Wu give Huoxing or Lingxing; Chou-Wei give Tianxiang; Yin-Shen give Tianliang; Mao-You give Tiantong; Chen-Xu give Wenchang; Si-Hai give Tianji. The Life Ruler governs innate destiny framework and potential, while the Body Ruler governs acquired cultivation and behavioral tendencies. When the Life Ruler is strong and well-placed, native potential is robust; when the Body Ruler is dignified, the native tends to grow into their better possibilities through effort and circumstance."""
    normalized_text_zh: str = """"""
    subject: str = "35. 命主与身主"
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
        l1_anchor="zw_v1.0.0_35__命主与身主_001_L1",
    )
    version: str = "1.0.0"
