"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997558
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
    semantic_id="dts_v1.0.0_一清到底有清神_管取平生富贵真_澄浊求清清得去_时来寒谷也生_001",
    book_id="dts",
    engine_id="bazi"
)
class 一清到底有清神管取平生富贵真澄浊求清清得去时来寒谷也生(SemanticEntry):
    """
    - **原文（source_text）**：
  一清到底有清神，管取平生富贵真。澄浊求清清得去，时来寒谷也生春。

- 原注（原文注解）：
  　　清者，不必一气成局之谓也，如正官之格，身旺有财，身...
    """
    
    original_text: str = """- **原文（source_text）**：
  一清到底有清神，管取平生富贵真。澄浊求清清得去，时来寒谷也生春。

- 原注（原文注解）：
  　　清者，不必一气成局之谓也，如正官之格，身旺有财，身弱有印，并无伤官七煞，纵有比肩，食神，财煞，印绶，杂之，皆循序得所，有安顿，或作闲神，不来破局，乃为之清，又要有精神，有气势，不枯不弱方佳。浊非五行并出之谓也；如正官格，身弱煞食杂之，不能伤我之官，反与官星不和，印绶杂之，不能扶我之身，反与财星相伐，俱为浊局，或得一神有力，或行运得所，扫其浊气，皆为澄浊求清，亦富贵之命。

- **规范化释义（primary_lang_explained）**：
  “清”重在次序得所、用神得位、闲神不乱；不必拘泥“一气成局”。“浊”在杂乱相伐、用忌相冲。行运得所，亦可“澄浊求清”。

- 分字分词释义：
  - 一清：全局调序得当、喜用不受侵凌之清。
  - 清神：为我所用之神且居位得势者。
  - 管取：可把握、可断定。
  - 富贵真：富与贵皆有真凭实据，非虚花。
  - 澄浊：去杂、去伐、解冲、安顿喜用。
  - 求清：以行运或局内改度而还其清。
  - 时来：岁运到位。
  - 寒谷生春：由枯槁转为发生之喻。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 清浊 | Clear-Turbid (Qing-Zhuo) | 气之清浊 | Clarity and turbidity of Qi | qingzhuo | existing |
| 清神 | Clear Spirit (Qing-Shen) | 局中清气 | Clear Qi in the chart | qingshen | new_candidate |
| 澄浊求清 | Purify Turbidity | 去浊留清 | Remove turbidity keep clarity | chengzhuo_qiuqing | new_candidate |
| 寒谷生春 | Spring in Cold Valley | 绝处逢生 | Life in hopeless place | hangu_shengchun | new_candidate |
| 富贵真 | True Nobility | 真实富贵 | Genuine wealth and status | fugui_zhen | new_candidate |
| 循序得所 | Orderly Sequence | 有序相生 | Orderly mutual generation | xunxu_desuo | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Qing-Zhuo (Clear-Turbid) theory: "Clear" (Qing) means orderly sequence, not just one element. "Clear Spirit" (Qing-Shen) must be vigorous. "Turbid" (Zhuo) means chaotic conflict. "Purifying Turbidity" (Cheng-Zhuo Qiu-Qing) via Luck Cycles can also bring nobility. Even a "Cold Valley" can sprout Spring if the time comes."""
    normalized_text_zh: str = """"""
    subject: str = "一清到底有清神，管取平生富贵真，澄浊求清清得去，时来寒谷也生春。"
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
        l1_anchor="dts_v1.0.0_一清到底有清神_管取平生富贵真_澄浊求清清得去_时来寒谷也生_001_L1",
    )
    version: str = "1.0.0"
