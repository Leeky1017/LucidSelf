"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264429
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
    semantic_id="smth_v1.0.0_支元六合的阴阳结构与律吕根基_001",
    book_id="sanming",
    engine_id="bazi"
)
class 支元六合的阴阳结构与律吕根基(SemanticEntry):
    """
    - **原文（source_text）**：  
  论支元六合夫合者，和也，乃阴阳相和，其气自合。子寅、辰、午申戌六者为阳，丑卯巳、未酉亥六者为阴，是以一阴一阳，和而谓之合。子合丑，寅合亥，却不子合...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论支元六合夫合者，和也，乃阴阳相和，其气自合。子寅、辰、午申戌六者为阳，丑卯巳、未酉亥六者为阴，是以一阴一阳，和而谓之合。子合丑，寅合亥，却不子合亥，寅合丑。夫何故？造物中虽是阴阳为合，气数中要占阳气为尊。子为一阳，丑伪二阳一二成三数，寅为三阳，亥是六。阴，三六成九数。卯为四阳，戌是五阴，四五得九数；辰为五阳，酉为四阴，五四得九数；巳为六阳，申为三阴，六三得九数；午为一阴，未为二阳，一二得三数。子丑午、未各得三者，三生万物，余皆得九者，乃阳数极也。尝问论甲乙者，如何子与丑合？皆莫知其故。因徧览群书，以观大运，乃知壬亥之间，日月十二辰交会之所……十一月建子，是时星纪在壬亥之间，星纪丑，故子与丑合。得日月会同之数，则其相合之用，如日月弥漫六合矣。人命逢六合，造化岂不美哉！

- **规范化释义（primary_lang_explained）**：  
  本段系统说明地支六合的阴阳结构与数理根源。作者先把十二支分成六阳、六阴，两两配成“一阴一阳”之合：子配丑，寅配亥，卯配戌，辰配酉，巳配申，午配未。关键不在“方位接近”而在“阳数为尊”：如子为一阳，丑为二阳，一二相加成三，三为生数；寅为三阳，亥为六阴，三六成九，九为阳之极数。其他诸对亦皆如此，要么得三，要么得九，体现“阳数主合”的原则。此外，作者引入历法与律吕系统：以壬亥为日月交会之所，推十二月建位与二十八宿在壬亥间的对应，来解释为何子丑、寅亥、卯戌、辰酉、巳申、午未各得六合。周礼中以黄钟子、大吕丑、太簇寅、应钟亥等配合祭祀乐章，也是借律吕相合来召天地之和气。综合而言，六合既是阴阳配对的结构，又是时间与空间节律在地支上的投影。"""
    normalized_text_zh: str = """"""
    subject: str = "支元六合的阴阳结构与律吕根基"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_支元六合的阴阳结构与律吕根基_001_L1",
    )
    version: str = "1.0.0"
