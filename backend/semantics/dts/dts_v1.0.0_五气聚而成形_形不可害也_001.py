"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997299
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
    semantic_id="dts_v1.0.0_五气聚而成形_形不可害也_001",
    book_id="dts",
    engine_id="bazi"
)
class 五气聚而成形形不可害也(SemanticEntry):
    """
    - **原文（source_text）**：
  五气聚而成形，形不可害也。

- 原注（原文注解）：
  　　如木必得水以生之，火以行之，土以培之，金以成之，五者聚而成形或过或缺则害，馀仿此。

-...
    """
    
    original_text: str = """- **原文（source_text）**：
  五气聚而成形，形不可害也。

- 原注（原文注解）：
  　　如木必得水以生之，火以行之，土以培之，金以成之，五者聚而成形或过或缺则害，馀仿此。

- 分字分词释义：
  - 五气聚：五行之气聚合配全.
  - 成形：由象进而成“形”（实体之用）。
  - 不可害：不宜以偏克破其全.

- **规范化释义（primary_lang_explained）**：
  五行之气协调配合，方能成“形”。一旦成形，虽可调剂，不可任意破害；若过或缺，则为害.


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 五气聚 | Five Qi Gathering | 五行之气聚合配全 | Convergence of all five elemental forces | wuqiju | new_candidate |
| 成形 | Form Completion | 由象进阶为实体之用 | Evolution from pattern to functional entity | chengxing | new_candidate |
| 不可害 | Cannot Be Harmed | 不可被任意破坏 | Integrity must be preserved from harm | bukehai | new_candidate |
| 过或缺 | Excess or Deficiency | 五行配比失衡 | Imbalance in elemental proportions | guohuoque | new_candidate |
| 整体平衡 | Holistic Balance | 五行系统的动态平衡 | Dynamic equilibrium of the five-element system | zhengtipingheng | new_candidate |

- **次语种完整诠释（secondary_lang_full）**:
  When the five elemental qi gather and cooperate, they do not just form a pattern but a usable "shape"—a complete structure that can bear real work and long-term development. Wood needs Water to give it life, Fire to move it, Earth to root it, and Metal to refine and finish it; only when these roles are all present in right proportion does the shape truly stand. Once such a shape is established, it should be adjusted with care, not smashed: correcting mild excess or deficiency is acceptable, but violent disruption that breaks the overall balance will cause the function of the whole system to collapse."""
    normalized_text_zh: str = """"""
    subject: str = "五气聚而成形，形不可害也。"
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
        l1_anchor="dts_v1.0.0_五气聚而成形_形不可害也_001_L1",
    )
    version: str = "1.0.0"
