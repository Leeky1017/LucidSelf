"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227832
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
    semantic_id="smth_v1.0.0_五行强弱与相制_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行强弱与相制(SemanticEntry):
    """
    - **原文（source_text）**：
  强可攻弱，土得木而达；实可胜虚，水得土而绝；阴可消阳，火得水而灭；烈可敌刚，金得火而缺；坚可制柔，木得金而伐。故五者流行而更转，顺则相生，逆则相克，如...
    """
    
    original_text: str = """- **原文（source_text）**：
  强可攻弱，土得木而达；实可胜虚，水得土而绝；阴可消阳，火得水而灭；烈可敌刚，金得火而缺；坚可制柔，木得金而伐。故五者流行而更转，顺则相生，逆则相克，如是则各各为用，以成其道而己。

- **分字分词释义**：
  - **强可攻弱**：强者可攻击弱者。
  - **土得木而达**：土得木克制，反而通达（木疏土）。
  - **实可胜虚**：充实可战胜虚弱。
  - **水得土而绝**：水被土克制而断绝。
  - **烈可敌刚**：炽烈可对抗刚强。
  - **流行而更转**：流动运行而交替转换。

- **规范化释义（primary_lang_explained）**：
  强者可以攻击弱者，土得木克制反而通达；充实可以战胜虚弱，水被土克制就断绝；阴可以消解阳，火遇水就熄灭；炽烈可以对抗刚强，金遇火就熔化；坚硬可以制约柔软，木被金砍伐。所以五行流动运行、交替转换，顺应则相生，违逆则相克，如此则各自发挥作用，完成自己的规律。

- **完整对等诠释（secondary_lang_full）**：
  The Five Elements exhibit strength-weakness dynamics: the strong attacks the weak—Earth gains openness through Wood (Wood loosens Earth); the solid defeats the empty—Water ceases when meeting Earth; yin dissolves yang—Fire extinguishes when meeting Water; the fierce opposes the rigid—Metal melts when meeting Fire; the hard controls the soft—Wood is cut when meeting Metal. The Five flow and alternate, generating when in accord and restricting when in opposition, each fulfilling its function to complete its way. This depicts the Elements' dynamic interactions and power relationships, enabling balance through strength-weakness contrast rather than absolute domination. This establishes the Elements' relative power in destiny analysis.

- **核心要点**：
  - 五行之间有强弱、实虚、阴阳、烈刚、坚柔的对比
  - 每种对比都有特定的相制关系
  - 五行流行更转，顺则相生，逆则相克
  - 各自发挥作用，完成自然规律

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_135]` `[trigger: 五行强弱相制]` `[factor_trigger: strength_weakness AND flow_transform]` `[role: 主干]` 强可攻弱，土得木而达；实可胜虚，水得土而绝。故五者流行而更转，顺则相生，逆则相克，如是则各各为用，以成其道而己。 → 《三命通会》卷一#五行强弱与相制

- **详细解说**：
  此条深入阐释五行相克中的力量对比。"土得木而达"看似矛盾，实则木能疏松土壤使之通达；"水得土而绝"是土克水的常理；"火得水而灭"是水克火；"金得火而缺"是火克金；"木得金而伐"是金克木。这五个例子展示了五行相克的具体表现。重点在于"强弱"、"实虚"等力量对比——相克并非绝对，而是取决于双方力量对比。原文强调，五行流动转换，顺应则相生，违逆则相克，各自发挥作用，共同完成天道规律。

- **校勘与字词辨析（双语）**：
  - **中文**："达"在此指通达疏松，非"到达"。"缺"指熔化损缺，非"缺少"。
  - **English**："达" (open/loosen) here means to become porous and permeable, not "to arrive"; "缺" (melt/diminish) means to be melted and damaged, not merely "to lack"."""
    normalized_text_zh: str = """"""
    subject: str = "五行强弱与相制"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_五行强弱与相制_001_L1",
    )
    version: str = "1.0.0"
