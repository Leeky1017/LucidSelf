"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227687
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
    semantic_id="smth_v1.0.0_松柏木_庚寅_辛卯_001",
    book_id="sanming",
    engine_id="bazi"
)
class 松柏木庚寅辛卯(SemanticEntry):
    """
    - **原文（source_text）**：
  庚寅辛卯则气已乘阳，得栽培之势，其为状也；奈居金下，凡金与霜素坚，木居下得其旺，岁寒后凋，取其性之坚也，故曰松柏木。

- 分字分词释义：
  - *...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚寅辛卯则气已乘阳，得栽培之势，其为状也；奈居金下，凡金与霜素坚，木居下得其旺，岁寒后凋，取其性之坚也，故曰松柏木。

- 分字分词释义：
  - **气已乘阳，得栽培之势**：阳气已经乘势上升，又得后天培植之力。
  - **居金下而岁寒后凋**：根居金下，历经风霜而后凋落，表其坚贞不屈之性。

- **规范化释义（primary_lang_explained）**：
  庚寅、辛卯之木，如松柏一般：得阳气扶持，又有栽培之力相助，即便处于金气之下、历经风霜，仍能到岁寒方才凋零，象征坚忍挺立、耐寒耐压。

- **完整对等诠释（secondary_lang_full）**：

  Geng Yin and Xin Mao are likened to "Pine and Cypress". Their Wood rides rising Yang and receives careful cultivation, yet stands beneath Metal and endures wind and frost until the coldest part of the year before shedding leaves. The emphasis is on toughness and staying power: the ability to remain upright and green through hardship, to hold responsibility over long stretches of time. In destiny analysis this Nayin signals a temperament suited to guarding, maintaining and persevering rather than to rapid expansion—pillar trees more than fast‑growing vines. Its gift is resilience; its danger is rigidity. When there is enough Fire, Water and flexibility elsewhere in the chart, Pine‑Cypress Wood becomes loyal endurance and moral backbone; when those moderating factors are lacking, the same quality can turn into stubbornness, refusal to adapt and carrying burdens alone for too long."""
    normalized_text_zh: str = """"""
    subject: str = "松柏木（庚寅、辛卯）"
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
        l1_anchor="smth_v1.0.0_松柏木_庚寅_辛卯_001_L1",
    )
    version: str = "1.0.0"
