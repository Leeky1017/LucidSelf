"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850595
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
    semantic_id="mlxj_v1.0.0_条目七_敬肆有端_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目七敬肆有端(SemanticEntry):
    """
    ### 原文（source_text）

敬肆有端，祸兮福倚，福兮祸伏。天道无常，惟人自召，故梦瑞而德益修者福必臻；梦瑞而纵恣者，福转为祸矣。梦妖而骄益甚者祸必成；梦妖而戒惧者，祸转为福矣。故梦之妖瑞...
    """
    
    original_text: str = """### 原文（source_text）

敬肆有端，祸兮福倚，福兮祸伏。天道无常，惟人自召，故梦瑞而德益修者福必臻；梦瑞而纵恣者，福转为祸矣。梦妖而骄益甚者祸必成；梦妖而戒惧者，祸转为福矣。故梦之妖瑞，视乎其人之德不德，召感几微，转移呼吸，不可不慎，岂执经而论哉？

### 规范化释义（primary_lang_explained）

占梦的第七条核心原则是「敬肆有端」——梦后的敬畏或放纵态度决定最终结果。

祸福相依：福中可能隐藏祸，祸中可能包含福。天道并无恒常，全在人之所召。因此：梦见祥瑞而更加修德者，福必来临；梦见祥瑞而纵恣放肆者，福会转为祸。梦见妖异而更加骄傲者，祸必成真；梦见妖异而戒惧谨慎者，祸会转为福。

所以梦之妖瑞，关键在于其人是否有德。感召的机微、转移的瞬息，不可不慎，岂能死守经文来论断？

### 核心要点

- 敬肆有端是占梦第七核心原则
- 祸兮福倚，福兮祸伏
- 梦瑞+修德 → 福必臻
- 梦瑞+纵恣 → 福转祸
- 梦妖+骄甚 → 祸必成
- 梦妖+戒惧 → 祸转福
- 召感几微，转移呼吸，不可执经而论

### 叙事素材（narrative_snippets）

- `[ns_mlxj_020]` `[trigger: 梦后态度]` `[factor_trigger: post_dream_attitude]` `[role: 转化机制]` 梦瑞而德益修者福必臻；梦瑞而纵恣者，福转为祸矣。 → 《梦林玄解·卷之首》#敬肆有端"""
    normalized_text_zh: str = """"""
    subject: str = "条目七：敬肆有端"
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
        l1_anchor="mlxj_v1.0.0_条目七_敬肆有端_001_L1",
    )
    version: str = "1.0.0"
