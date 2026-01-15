"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.819323
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
    semantic_id="mlxj_v1.0.0_1_释迦佛_仙佛类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1释迦佛仙佛类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

释迦佛大吉。此佛祖也，兆之，则明心见性，可悟上乘，为佛弟子，智慧日增，西土生莲也。

#### 规范化释义（primary_lang_explained）
...
    """
    
    original_text: str = """#### 原文（source_text）

释迦佛大吉。此佛祖也，兆之，则明心见性，可悟上乘，为佛弟子，智慧日增，西土生莲也。

#### 规范化释义（primary_lang_explained）

梦见释迦佛，大吉。释迦是佛祖，梦见此兆，则主明心见性，可悟上乘佛法，为佛弟子，智慧日增，来世可生西方莲土。

#### 完整对等诠释（secondary_lang_full）

Dreaming of Shakyamuni Buddha is greatly auspicious. He is the founder of Buddhism. Such a dream portends enlightening one's mind and seeing one's true nature, comprehending the supreme vehicle of dharma, becoming a disciple of Buddha with daily increasing wisdom, and being reborn in the Western Pure Land of lotus.

#### 核心要点

- 释迦佛=佛祖=最高佛教象征
- 主明心见性——开悟之兆
- 主智慧日增——修行进境
- 主西土生莲——来世善果

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v5_002]` `[trigger: 梦释迦佛]` `[factor_trigger: dream_jian_shijiafo]` `[role: 主干]` 释迦佛大吉。此佛祖也，兆之，则明心见性，可悟上乘。 → 《梦林玄解·卷五》#释迦佛"""
    normalized_text_zh: str = """"""
    subject: str = "1 释迦佛（仙佛类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_释迦佛_仙佛类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
