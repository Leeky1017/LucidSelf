"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850571
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
    semantic_id="mlxj_v1.0.0_条目四_贵贱有别_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目四贵贱有别(SemanticEntry):
    """
    ### 原文（source_text）

贵贱有别，帝王有帝王之梦，臣宰有臣宰之梦，圣贤有圣贤之梦，常人有常人之梦，以至工贾商农、舆台厮仆，则有工贾、商农、舆台厮仆之梦。穷通荣辱，成败亏盈，各缘其人而...
    """
    
    original_text: str = """### 原文（source_text）

贵贱有别，帝王有帝王之梦，臣宰有臣宰之梦，圣贤有圣贤之梦，常人有常人之梦，以至工贾商农、舆台厮仆，则有工贾、商农、舆台厮仆之梦。穷通荣辱，成败亏盈，各缘其人而为推测，不得以至卑至贱者，乃妄以尊贵之象加之耳。

### 规范化释义（primary_lang_explained）

占梦的第四条核心原则是「贵贱有别」——必须根据做梦者的社会身份地位来推断梦境。帝王有帝王层级的梦，臣宰有臣宰层级的梦，圣贤有圣贤层级的梦，常人有常人层级的梦。乃至工匠、商贾、农夫、车夫、仆役，都各有其身份对应的梦境解读方式。

一个人的穷困通达、荣耀屈辱、成功失败、亏损盈余，都要根据其人的实际身份地位来推测，不能将卑微低贱之人的梦，妄自用尊贵高显的象征去解读。

### 完整对等诠释（secondary_lang_full）

The fourth principle is "Distinction by Social Status" — dream interpretation must consider the dreamer's social position. Emperors dream emperor-level dreams, ministers dream minister-level dreams, sages dream sage-level dreams, and commoners dream commoner-level dreams. Craftsmen, merchants, farmers, drivers, and servants each have dreams appropriate to their stations.

One's poverty or prosperity, honor or disgrace, success or failure, loss or gain must be interpreted according to their actual social position. One must never interpret a lowly person's dream using symbols meant for the noble and exalted.

### 核心要点

- 梦境解读必须因人而异，考虑社会身份
- 帝王、臣宰、圣贤、常人各有其梦的层级
- 工贾商农舆台厮仆各有其对应的梦象解读
- 不可将卑者之梦妄用尊贵之象解释
- 穷通荣辱皆缘其人而推测

### 叙事素材（narrative_snippets）

- `[ns_mlxj_014]` `[trigger: 身份判断]` `[factor_trigger: dreamer_status]` `[role: 核心原则]` 帝王有帝王之梦，臣宰有臣宰之梦，圣贤有圣贤之梦，常人有常人之梦。 → 《梦林玄解·卷之首》#贵贱有别
- `[ns_mlxj_015]` `[trigger: 身份限制]` `[factor_trigger: dreamer_status]` `[role: 禁忌]` 不得以至卑至贱者，乃妄以尊贵之象加之耳。 → 《梦林玄解·卷之首》#贵贱有别"""
    normalized_text_zh: str = """"""
    subject: str = "条目四：贵贱有别"
    factor_refs: list = ['dreamer_status']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_条目四_贵贱有别_001_L1",
    )
    version: str = "1.0.0"
