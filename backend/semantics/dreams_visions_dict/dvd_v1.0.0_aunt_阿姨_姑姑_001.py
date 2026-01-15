"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439790
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
    semantic_id="dvd_v1.0.0_aunt_阿姨_姑姑_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Aunt阿姨姑姑(SemanticEntry):
    """
    ### Source Text

**Dreams**: Consider the main qualities of your aunt. When she comes to mind, what ...
    """
    
    original_text: str = """### Source Text

**Dreams**: Consider the main qualities of your aunt. When she comes to mind, what is the first thing that comes to you? This will give you an indication of what she represents. The circumstances surrounding your dream will tell you what is going on in your life right now.

**Visions - Positive**: If you see your aunt in vision, the Lord could be telling you to pray for her. If you function in intercession ministry, the Lord is bringing her to mind for prayer.

**Visions - Negative**: Often the Lord will show someone in vision to bring healing to a specific event or break spiritual ties. If seeking God regarding a curse or blockage and He brings your aunt to mind, you may have received something from her that was not of Him. Lord could also be exposing a generational curse—consider her life and what He is exposing.

**See also**: Uncle, Ancestor

### English Paraphrase

Aunt = represents her main qualities (first thing that comes to mind). Circumstances in dream reveal what's going on in your life. **Positive vision**: Lord calling you to pray for her (intercession). **Negative vision**: Exposing something received from her that wasn't of God, or generational curse. Consider her life—what is Lord exposing? May need to break spiritual ties.

### Chinese Interpretation（完整对等诠释）

阿姨/姑姑 = 代表她的主要特质（脑海中首先浮现的）。梦中情境揭示你生活中正在发生什么。**正面异象**：主呼召你为她代祷（代祷事工）。**负面异象**：揭露从她那里接受的不属神的东西，或世代咒诅。考虑她的生命——主在揭露什么？可能需要断开属灵连结。

### Narrative Snippets

- `[ns_dav_a066]` `[trigger: 梦阿姨]` `[factor_trigger: dream_symbol_aunt]` `[role: 主干]` Aunt = her main qualities—first thing that comes to mind. Circumstances reveal your life situation. → Dreams Dictionary #Aunt
- `[ns_dav_a067]` `[trigger: 阿姨正面]` `[factor_trigger: dream_symbol_aunt AND aunt_relation]` `[role: 条件分支]` Aunt in vision = Lord calling to pray for her, intercession ministry. → Dreams Dictionary #Aunt
- `[ns_dav_a068]` `[trigger: 阿姨负面]` `[factor_trigger: dream_symbol_aunt AND aunt_relation]` `[role: 条件分支]` Aunt in negative vision = exposing something received from her, generational curse, break ties. → Dreams Dictionary #Aunt"""
    normalized_text_zh: str = """"""
    subject: str = "Aunt 阿姨/姑姑"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_aunt_阿姨_姑姑_001_L1",
    )
    version: str = "1.0.0"
