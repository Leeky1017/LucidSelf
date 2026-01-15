"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808923
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
    semantic_id="mlxj_v1.0.0_2_列子梦论_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2列子梦论(SemanticEntry):
    """
    #### 原文（source_text）

梦有六候：一曰正梦，二曰噩梦，三曰思梦，四曰寤梦，五曰喜梦，六曰惧梦。此六者，神所交也。

故阴气壮则梦涉大水而恐惧，阳气壮则梦涉大火而燔灼。阴阳俱壮，则梦...
    """
    
    original_text: str = """#### 原文（source_text）

梦有六候：一曰正梦，二曰噩梦，三曰思梦，四曰寤梦，五曰喜梦，六曰惧梦。此六者，神所交也。

故阴气壮则梦涉大水而恐惧，阳气壮则梦涉大火而燔灼。阴阳俱壮，则梦生杀，甚饱则梦与，甚饥则梦取。是以虚浮为疾者则梦扬，以沉实为疾者则梦溺。藉带而寝则梦蛇，飞鸟衔发则梦飞。将阴梦火，将疾梦食，梦饮酒者忧，梦歌舞者哭。

神遇为梦，形接为事，故昼想夜梦。神形所遇，故神凝者，想梦自消。信觉不语，信梦不达，物化之往来者也。古之真人，其觉日忘，其寝不梦。欲辨觉梦，惟黄帝与孔丘。今无黄帝、孔丘，孰辨之哉？

#### 规范化释义（primary_lang_explained）

《列子》梦论：梦有六候（正、噩、思、寤、喜、惧），此六者神所交也。

阴阳与梦：
- 阴气壮 → 梦涉大水而恐惧
- 阳气壮 → 梦涉大火而燔灼
- 阴阳俱壮 → 梦生杀
- 甚饱 → 梦与
- 甚饥 → 梦取

因梦理论：
- 虚浮为疾 → 梦扬
- 沉实为疾 → 梦溺
- 藉带而寝 → 梦蛇
- 飞鸟衔发 → 梦飞

神形论：神遇为梦，形接为事，故昼想夜梦。神凝者，想梦自消。古之真人，其觉日忘，其寝不梦。欲辨觉梦，惟黄帝与孔丘。"""
    normalized_text_zh: str = """"""
    subject: str = "2 列子梦论"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_2_列子梦论_001_L1",
    )
    version: str = "1.0.0"
