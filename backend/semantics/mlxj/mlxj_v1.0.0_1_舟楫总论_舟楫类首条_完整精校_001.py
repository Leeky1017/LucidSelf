"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.799553
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
    semantic_id="mlxj_v1.0.0_1_舟楫总论_舟楫类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1舟楫总论舟楫类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

船舟船者，载万物，济百川，安行千里。车骑所不通，得舟以通；危倾顷刻，羽翼不能济，得楫以济。维鬼神之德，解风波之险，下涉沧溟，上达天衢，预兆于寤寐，避凶趋吉，...
    """
    
    original_text: str = """#### 原文（source_text）

船舟船者，载万物，济百川，安行千里。车骑所不通，得舟以通；危倾顷刻，羽翼不能济，得楫以济。维鬼神之德，解风波之险，下涉沧溟，上达天衢，预兆于寤寐，避凶趋吉，不可不察也。

#### 规范化释义（primary_lang_explained）

船舟，载万物，济百川，安行千里。车骑所不通之处，得舟以通达；危急倾覆之时，羽翼不能救济，得楫以渡济。这是维系鬼神之德，解除风波之险的器物。下可涉沧溟大海，上可达天衢仙路，预兆于寤寐之间，避凶趋吉，不可不详察。

#### 完整对等诠释（secondary_lang_full）

Boats and ships carry all things, cross all rivers, travel safely a thousand miles. Where carriages cannot pass, boats provide passage; in moments of peril when wings cannot save, oars provide rescue. They maintain the virtue of gods and ghosts, dispelling dangers of wind and waves. Below they traverse the vast seas, above they reach the heavenly roads. Omens appearing in dreams allow one to avoid misfortune and pursue good fortune—this must be carefully examined.

#### 核心要点

- 舟船=载万物济百川=交通工具之首
- 通达功能：车骑不通→舟通，危急→楫济
- 神圣属性：维鬼神之德，解风波之险
- 上下通达：下涉沧溟，上达天衢
- 占断功能：预兆寤寐，避凶趋吉"""
    normalized_text_zh: str = """"""
    subject: str = "1 舟楫总论（舟楫类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_舟楫总论_舟楫类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
