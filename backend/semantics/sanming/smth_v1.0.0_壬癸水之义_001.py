"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227956
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
    semantic_id="smth_v1.0.0_壬癸水之义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬癸水之义(SemanticEntry):
    """
    - **原文（source_text）**：
  壬癸其位，水行冬之令。壬之言任也。壬乃阳生之位，壬而为胎，万物怀妊于壬，与子同意。癸者，揆也。天令至此，万物闭藏，怀妊于其下，揆然萌芽，此天之道也，以...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬癸其位，水行冬之令。壬之言任也。壬乃阳生之位，壬而为胎，万物怀妊于壬，与子同意。癸者，揆也。天令至此，万物闭藏，怀妊于其下，揆然萌芽，此天之道也，以为日各焉。故经曰：天有十日，日六竟而周甲者，此也。

- **分字分词释义**：
  - **壬之言任**：壬就是"任"的意思。
  - **阳生之位**：阳气萌生的位置。
  - **壬而为胎**：壬为胎孕之位。
  - **怀妊**：怀孕。
  - **与子同意**：与地支子相同意义。
  - **揆**：度量、萌芽。
  - **天令至此**：天时到此。
  - **揆然萌芽**：揆度而萌芽。
  - **日六竟而周甲**：六旬循环而周遍天干。

- **规范化释义（primary_lang_explained）**：
  壬癸的位置属水，主管冬季的时令。壬就是"任"，即怀孕之意。壬是阳气萌生的位置，壬为胎孕之位，万物怀孕于壬，与地支子的意义相同。癸就是"揆"，即度量、萌芽之意。天时到了此时，万物闭藏，在下面怀孕，揆度而萌芽，这是天道。用来作为日期。所以经书说：天有十日，六旬循环而周遍天干，就是这个道理。

- **完整对等诠释（secondary_lang_full）**：
  Ren and Gui occupy the Water position, commanding Winter's decree. Ren means "conceiving" or "bearing." Ren is the position where yang qi begins to germinate; Ren serves as the womb—myriad things are conceived in Ren, sharing the same meaning as the Earthly Branch Zi. Gui means "measuring" or "sprouting." When Heaven's decree reaches this point, myriad things are sealed and stored, conceiving below and sprouting through measurement—this is Heaven's Way, serving as the daily markers. Therefore the classics state: "Heaven has Ten Days; after six cycles they complete the Stems"—this is the principle.

- **核心要点**：
  - 壬癸属水，主冬季
  - 壬水：阳生之位，为胎孕，与子同意
  - 癸水：揆度萌芽，万物闭藏
  - 壬为"任"（怀孕），癸为"揆"（度量萌芽）
  - 天有十日，六竟周甲

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_153]` `[trigger: 壬癸水之义]` `[factor_trigger: ren_water AND gui_water AND element_water]` `[role: 主干]` 壬癸其位，水行冬之令。壬之言任也，壬乃阳生之位，万物怀妊于壬，与子同意。癸者，揆也，天令至此，万物闭藏，揆然萌芽。 → 《三命通会》卷一#壬癸水之义

- **详细解说**：
  此条详解壬癸水之义并总结十干之用。壬水为阳水，冬初之时一阳始生，万物在此位置开始孕育，如同胎儿在母体中怀孕，与地支子（一阳初生）意义相同。癸水为阴水，万物完全闭藏于地下，在隐蔽处揆度（度量、筹划）萌芽的时机。"壬，任也"指承担孕育之任；"癸，揆也"指揆度未来生机。这是天道循环的终点也是起点。最后引经书说明十天干作为日期标记，六个甲子（60天）循环往复，周而复始。这体现了壬癸水从孕育（壬）到揆度（癸）的两个阶段，完成五行循环回到起点。

- **校勘与字词辨析（双语）**：
  - **中文**："任"通"妊"，怀孕之意。"揆"有度量、揆度之意。"日六竟"指六旬（60天）。"周甲"指周遍天干。
  - **English**: "任" (ren) means "conceiving/bearing"; "揆" (kui) means "measuring/calculating"; "六竟" refers to six cycles (60 days); "周甲" means completing the Stems cycle."""
    normalized_text_zh: str = """"""
    subject: str = "壬癸水之义"
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
        l1_anchor="smth_v1.0.0_壬癸水之义_001_L1",
    )
    version: str = "1.0.0"
