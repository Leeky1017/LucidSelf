"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997668
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
    semantic_id="dts_v1.0.0_臣不可过也_贵乎损下益上_001",
    book_id="dts",
    engine_id="bazi"
)
class 臣不可过也贵乎损下益上(SemanticEntry):
    """
    - **原文（source_text）**：
  臣不可过也，贵乎损下益上。

- 原注（原文注解）：
  　　日主为臣，官星为君。如甲乙日主，满盘是木，内有一二点金，是臣盛而君衰，要土金势盛，方能助...
    """
    
    original_text: str = """- **原文（source_text）**：
  臣不可过也，贵乎损下益上。

- 原注（原文注解）：
  　　日主为臣，官星为君。如甲乙日主，满盘是木，内有一二点金，是臣盛而君衰，要土金势盛，方能助其君……（略）。

- **规范化释义（primary_lang_explained）**：
  臣盛君衰，需“损下益上”，回流资源与权力，使君位恢复纲纪。

- 分字分词释义：
  - 臣：财/佐辅/体系之下位。
  - 不可过：不可喧宾夺主。
  - 损下益上：回流资源，以安上位（官/纲）。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 臣不可过 | Subject Cannot Be Excessive | 臣不欺君 | Subject must not surpass Ruler | chenbukeguo | new_candidate |
| 损下益上 | Damage Lower Benefit Upper | 损臣益君 | Transfer resources to Ruler | sunxia_yishang | new_candidate |
| 喧宾夺主 | Guest Usurps Host | 臣强君弱 | Subject overpowers Ruler | xuanbin_duozhu | new_candidate |
| 势盛 | Power Flourishing | 气势旺盛 | Strong momentum | shisheng | new_candidate |
| 纲纪 | Discipline/Order | 君臣纲纪 | Hierarchy and order | gangji | new_candidate |
| 助君 | Assist Ruler | 扶助君位 | Support the Ruler position | zhujun | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Jun-Chen (Ruler-Subject) theory: The Subject (Wealth/Official) cannot be excessive (Bu-Ke-Guo). Value lies in "Damaging the Lower to Benefit the Upper" (Sun-Xia Yi-Shang). When Subject is strong and Ruler weak, use Earth and Metal to support the Ruler and constrain the Subject."""
    normalized_text_zh: str = """"""
    subject: str = "臣不可过也，贵乎损下益上。"
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
        l1_anchor="dts_v1.0.0_臣不可过也_贵乎损下益上_001_L1",
    )
    version: str = "1.0.0"
