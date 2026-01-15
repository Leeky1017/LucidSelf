"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789205
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
    semantic_id="mlxj_v1.0.0_2_五神所属事物_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2五神所属事物(SemanticEntry):
    """
    #### 原文摘要

**肝属之事**（不尽类推）：斗殴刳杀、争讼、拷讯、杖责、怒气、骂詈、叱咤、伏坐、立负、抱谒、访迎、送殡、殓冠、笄种、植栉、发酗、酒击、毬跳、越御、车雕、塑担、荷织、作畋、猎决、...
    """
    
    original_text: str = """#### 原文摘要

**肝属之事**（不尽类推）：斗殴刳杀、争讼、拷讯、杖责、怒气、骂詈、叱咤、伏坐、立负、抱谒、访迎、送殡、殓冠、笄种、植栉、发酗、酒击、毬跳、越御、车雕、塑担、荷织、作畋、猎决、断谋、虑观、看呼、吸动、摇颤、掉旋、转飘、扬虚、浮行、空登、高涉、险执、持擒、捉擎、举提、挈搬移。

**心属之事**：捕捉、火烧、跪屈、飞盟、誓恐、畏宴、会嫁、娶考、试疾、病庆、贺喜、欢聚、吟诵、迁移、惊仕、宦狂、绘画、升擢、算数、炊爨、抚掌、洗涤、声韵、音响。

**脾属之事**：歌舞、匠作、笑饮、食祭、享身、重葬、埋取、予交、易耕、作大便、缝补、祝佛、事跳、跃医、治陶、冶扶、觇牧、养。

**肺属之事**：战斗、杀戮、呼召、言语、啑咳、哭泣、生死、飞扬、奔驰、悲涕、大叫、冶铸、借贷、咒咀、吹弹、忧思、分析、戏演、卜筮、镌刻、搬运、声哑、唾啐、吊奠、歌舞。

**肾属之事**：拜揖、行步、坠堕、盗发、溺水、涉水、分别、沐浴、溲便、姤孕、洒扫、盥洗、游玩、寝卧、汗湿、磨碾、淘汰、临钓、服役、染采、驾舟。

#### 语义提取

五神所属事物表提供了梦中出现的各类行为、动作与五脏五神的对应关系，是占梦时判断梦象归属的重要依据。"""
    normalized_text_zh: str = """"""
    subject: str = "2 五神所属事物"
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
        l1_anchor="mlxj_v1.0.0_2_五神所属事物_001_L1",
    )
    version: str = "1.0.0"
