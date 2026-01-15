"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997795
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
    semantic_id="dts_v1.0.0_分藩司牧财官和_清奇纯粹局全多_001",
    book_id="dts",
    engine_id="bazi"
)
class 分藩司牧财官和清奇纯粹局全多(SemanticEntry):
    """
    - **原文（source_text）**：
  分藩司牧财官和，清奇纯粹局全多。

- 分字分词释义：
  - 分藩：分封的藩属、地方大员。
  - 司牧：掌管政务、牧民一方。
  - 财官和：财星...
    """
    
    original_text: str = """- **原文（source_text）**：
  分藩司牧财官和，清奇纯粹局全多。

- 分字分词释义：
  - 分藩：分封的藩属、地方大员。
  - 司牧：掌管政务、牧民一方。
  - 财官和：财星与官星和谐配合。
  - 清奇纯粹：格局清雅纯正。
  - 局全多：局势完整、配置齐全。

- 规范化释义（primary_lang_explained）：
  此条主“分藩司牧”之任：适合治理一方、掌管财官之职。命局中财官和洽、清奇纯粹而局势完整者，多主封疆大吏、地方重臣之类，能在区域层面统筹资源与行政。

- **核心要点**：
  - 财官和洽、不相战，兼具资源与权力；
  - 局清而全，有足够承载面，适合地方长官；
  - 地位虽不及台阁中枢，却能“一方之主”。

- 详细解说：
  “分藩司牧”比台阁稍下一等，但仍属高位：一方面需要财星成局以供养体系，另一方面要有官星坐镇以行使权力。若财官相和、杂气不多，则既能善理钱谷，又能稳住行政秩序，是典型的地方长官配置。若财官相拗、局中混浊，则容易沦为奔波琐碎之职，而非清奇之任。

- 校勘与字词辨析：
  - “分藩司牧”：统指分封诸侯、地方巡抚、郡守太守等类型的地方主官。

- **次语种完整诠释（secondary_lang_full）**:
  Provincial-governor分藩 local-administrator司牧 wealth-official-harmonious财官和: clear-extraordinary清奇 pure-complete纯粹 pattern-full局全多—regional地方 high-official高官 needs财官 wealth-official和谐 harmonious清奇 clear-extraordinary."""
    normalized_text_zh: str = """"""
    subject: str = "分藩司牧财官和，清奇纯粹局全多。"
    factor_refs: list = ['fenfan_regional_role', 'simu_local_admin_role', 'wealth_official_harmony', 'extraordinary_level', 'purity_level']
    
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
        l1_anchor="dts_v1.0.0_分藩司牧财官和_清奇纯粹局全多_001_L1",
    )
    version: str = "1.0.0"
