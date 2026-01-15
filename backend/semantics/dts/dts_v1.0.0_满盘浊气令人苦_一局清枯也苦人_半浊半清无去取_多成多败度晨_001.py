"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997566
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
    semantic_id="dts_v1.0.0_满盘浊气令人苦_一局清枯也苦人_半浊半清无去取_多成多败度晨_001",
    book_id="dts",
    engine_id="bazi"
)
class 满盘浊气令人苦一局清枯也苦人半浊半清无去取多成多败度晨(SemanticEntry):
    """
    - **原文（source_text）**：
  满盘浊气令人苦，一局清枯也苦人。半浊半清无去取，多成多败度晨昏。

- 原注（原文注解）：
  　　柱中寻他清气不出，行运又不能去其浊气，必是贫贱。若...
    """
    
    original_text: str = """- **原文（source_text）**：
  满盘浊气令人苦，一局清枯也苦人。半浊半清无去取，多成多败度晨昏。

- 原注（原文注解）：
  　　柱中寻他清气不出，行运又不能去其浊气，必是贫贱。若清而枯，弱而无气，行运又不遇生地，亦清苦之人。至于浊气又难去，清气又不真，行运又不遇清气，又不脱浊气，此则成败不一。

- **规范化释义（primary_lang_explained）**：
  清要有气、有承；清而枯亦苦。半清半浊、运助无门者，成败起伏。

- 分字分词释义：
  - 满盘浊气：处处互伐、无序相冲。
  - 清枯：清而无生机、无承续之路。
  - 半浊半清：两套气脉并存、难定主从。
  - 无去取：取舍无门、路径不显。
  - 多成多败：阶段性起伏、难稳常态。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 满盘浊气 | Full Turbidity | 处处混杂 | Chaos everywhere | manpan_zhuoqi | new_candidate |
| 清枯 | Clear but Withered (Qing-Ku) | 清而无气 | Clear but lifeless | qing_ku | new_candidate |
| 半浊半清 | Half Turbid Half Clear | 清浊混杂 | Mixed clarity and turbidity | ban_zhuo_ban_qing | new_candidate |
| 无去取 | No Decision | 难以取舍 | Hard to choose | wu_ququ | new_candidate |
| 多成多败 | Mixed Success/Failure | 起伏不定 | Ups and downs | duo_cheng_duo_bai | new_candidate |
| 苦人 | Suffering Person | 劳苦之人 | Person in hardship | ku_ren | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Qing-Zhuo Subtypes: "Full Turbidity" (Man-Pan Zhuo) causes suffering. "Clear but Withered" (Qing-Ku) also causes suffering. "Half Clear Half Turbid" (Ban-Zhuo Ban-Qing) leads to mixed success and failure (Duo-Cheng Duo-Bai). The key is whether the Luck Cycle supports the Clear or removes the Turbid."""
    normalized_text_zh: str = """"""
    subject: str = "满盘浊气令人苦，一局清枯也苦人，半浊半清无去取，多成多败度晨昏。"
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
        l1_anchor="dts_v1.0.0_满盘浊气令人苦_一局清枯也苦人_半浊半清无去取_多成多败度晨_001_L1",
    )
    version: str = "1.0.0"
