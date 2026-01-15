"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850611
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
    semantic_id="mlxj_v1.0.0_条目九_梦寄_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目九梦寄(SemanticEntry):
    """
    ### 原文（source_text）

梦寄凡见梦而互相征应，如他人之梦忽见诸我，己身之梦反见于人。故臣有忠良，主得之梦；子有贤贵，亲得之梦；夫有怅木，妻得之梦；人有穷达，友得之梦。或共寝而梦各异，...
    """
    
    original_text: str = """### 原文（source_text）

梦寄凡见梦而互相征应，如他人之梦忽见诸我，己身之梦反见于人。故臣有忠良，主得之梦；子有贤贵，亲得之梦；夫有怅木，妻得之梦；人有穷达，友得之梦。或共寝而梦各异，或隔绝而梦寔同。逮至久不相见，素不相识，远不相及之人，本无缘感，突如托梦，甚有神灵昭现，英魂咛诫。凡此之梦，皆宜精详细究，得之意象之先，乃可推其奥渺也。

### 规范化释义（primary_lang_explained）

占梦的第九条核心原则是「梦寄」——梦境可以寄托于他人而互相征应。

有时他人的梦会显现于我，有时我的梦会反映于他人。因此：臣子有忠良之质，君主可能先得其梦；儿子有贤贵之相，父母可能先得其梦；丈夫有志向，妻子可能先得其梦；某人有穷达之变，朋友可能先得其梦。

有时同床共寝却梦各不同，有时相隔万里却梦完全相同。甚至久不相见、素不相识、远不相及之人，本无缘分感应，却突然托梦，更有神灵昭示、英魂告诫的情况。

凡此梦寄之梦，都应当精详细究，在意象之先领会其意，才能推究其深奥微妙。

### 核心要点

- 梦寄是占梦第九核心原则
- 梦可以寄托于他人，互相征应
- 臣忠则主得梦，子贤则亲得梦
- 共寝可异梦，隔绝可同梦
- 无缘之人亦可托梦
- 神灵英魂可通过梦显现

### 叙事素材（narrative_snippets）

- `[ns_mlxj_023]` `[trigger: 梦寄现象]` `[factor_trigger: dream_transfer]` `[role: 特殊类型]` 他人之梦忽见诸我，己身之梦反见于人。 → 《梦林玄解·卷之首》#梦寄
- `[ns_mlxj_024]` `[trigger: 托梦]` `[factor_trigger: spirit_dream]` `[role: 特殊类型]` 本无缘感，突如托梦，甚有神灵昭现，英魂咛诫。 → 《梦林玄解·卷之首》#梦寄"""
    normalized_text_zh: str = """"""
    subject: str = "条目九：梦寄"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_条目九_梦寄_001_L1",
    )
    version: str = "1.0.0"
