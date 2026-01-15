"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654377
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
    semantic_id="zw_v1.0.0_论星辰生克制化_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论星辰生克制化(SemanticEntry):
    """
    - 分字分词释义：

  - **生克制化**：五行相生相克的作用机制。
  - **星宫五行**：星曜与宫位的五行属性关系。
  - **廉贞属火**：廉贞星五行属火。
  - **寅宫木乡**：寅...
    """
    
    original_text: str = """- 分字分词释义：

  - **生克制化**：五行相生相克的作用机制。
  - **星宫五行**：星曜与宫位的五行属性关系。
  - **廉贞属火**：廉贞星五行属火。
  - **寅宫木乡**：寅宫五行属木。
  - **木生火**：木能生火，星曜得生。
  - **受制**：星曜五行被宫位五行所克。
  - **金入火乡**：金星落火地，被火克金。

星曜全要明生克制化之机，次看落于何宫。如廉贞属火在寅宫乃木乡能生廉贞之火。若武曲金星与廉贞同度，则武曲为财而无用也。

**五行受制**：
- 金入火乡
- 火入水乡
- 水入土乡
- 土入金乡

#### 完整对等诠释（secondary_lang_full·41生克制化）：

  The Five-Phase interaction between stars and palaces forms a foundational layer of interpretation. A star's element interacts with the element of the palace it occupies. For example, Lianzhen (Fire) in Yin palace (Wood territory) receives support, as Wood feeds Fire. But if Wuqu (Metal) shares the same palace, Metal is melted by Fire, weakening Wuqu's wealth-generating capacity. The text lists four classic "controlled" scenarios: Metal entering Fire territory, Fire entering Water territory, Water entering Earth territory, and Earth entering Metal territory. In each case the star's native element is restrained or drained by the palace element. Understanding these interactions helps refine judgments about whether a star can fully express its potential or is structurally hampered."""
    normalized_text_zh: str = """"""
    subject: str = "论星辰生克制化"
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
        l1_anchor="zw_v1.0.0_论星辰生克制化_001_L1",
    )
    version: str = "1.0.0"
