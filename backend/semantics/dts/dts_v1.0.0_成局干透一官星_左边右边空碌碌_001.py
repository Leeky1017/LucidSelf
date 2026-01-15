"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997354
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
    semantic_id="dts_v1.0.0_成局干透一官星_左边右边空碌碌_001",
    book_id="dts",
    engine_id="bazi"
)
class 成局干透一官星左边右边空碌碌(SemanticEntry):
    """
    - **原文（source_text）**：
  成局干透一官星，左边右边空碌碌。

- 分字分词释义：
  - 成局：三合局已成（如亥卯未木局）。
  - 干透：天干透出。
  - 一官星：一位官星...
    """
    
    original_text: str = """- **原文（source_text）**：
  成局干透一官星，左边右边空碌碌。

- 分字分词释义：
  - 成局：三合局已成（如亥卯未木局）。
  - 干透：天干透出。
  - 一官星：一位官星（如庚辛为甲乙之官）。
  - 左边右边：命局左右两侧的地支。
  - 空碌碌：忙碌而无成、有劳无功。

- 规范化释义（primary_lang_explained）：
  三合局已成，又有官星干透，本可成就官贵；若左右再杂以同类方气，牵扯主线之力，则多主名利空忙，格局难以落实。

- **核心要点**：
  - 成局见官本是好势，但若左右再杂同类方气，则主线被分流；
  - 同一五行不可又成局又成方，局方相混，多成“空碌碌”；
  - 警示勿在已成格局上不断叠加同类枝节，反致主业难成。

- 详细解说：
  本条承接前文“方不可混以局”，转而指出“局不可混以方”：当亥卯未等三合局已成、庚辛官星干透时，原本是清楚的官局主线；若又在左右见寅辰等同类方气，局之力量被分拆为数股，既顾此又顾彼，终致名利多空。命理解读中，这类命往往工作繁忙、事务众多，却难以在单一主线累积成就。

- 校勘与字词辨析：
  - “空碌碌”：并非完全无官无局，而是有势难成，有忙无功之象。

 - 原注（原文注解）：
 　　如甲乙日遇亥卯未全，而又干透庚辛一官星，又见右寅，左辰，则名利无成，局不可混以方也，甲乙日单遇庚辛，则亦无成.
 
- **规范化释义（primary_lang_explained）**：
  局已成而干再透官星，且两旁杂以方气冲错，往往名利两空.
- **次语种完整诠释（secondary_lang_full）**:  
  A formed trinity assembly with an Officer star clearly revealed on the stems ought, in principle, to bring rank and achievement. But if, to the left and right of this main structure, additional directional qi of the same element keeps pulling, the officer line is constantly distracted. Energy that should flow into one clear channel is split between several similar side tracks, so the native is busy, engaged, and apparently well positioned, yet finds it hard to settle concrete results. This is the image of working hard with structure and opportunity in place, but having official fortune and reputation remain thin. The verse therefore cautions against mixing a finished Ju with more of the same Fang on both sides: keep the main structure clean if you want its promise to materialise."""
    normalized_text_zh: str = """"""
    subject: str = "成局干透一官星，左边右边空碌碌。"
    factor_refs: list = ['chengju', 'guanxing_tougan', 'zuoyou_fangqi', 'konglulu', 'juhunfang', 'fenliu_haosan']
    
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
        l1_anchor="dts_v1.0.0_成局干透一官星_左边右边空碌碌_001_L1",
    )
    version: str = "1.0.0"
