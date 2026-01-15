"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.825985
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
    semantic_id="mlxj_v1.0.0_1_山行_山水类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1山行山水类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

山行大吉。履高山，居高位，亨通尊贵之象也。在易为艮止而不动，动极归静，梦此者握大权获大利，享大福富贵佳祥。山亦地属，贵显之征。天下名山五千三百七十，名地六万...
    """
    
    original_text: str = """#### 原文（source_text）

山行大吉。履高山，居高位，亨通尊贵之象也。在易为艮止而不动，动极归静，梦此者握大权获大利，享大福富贵佳祥。山亦地属，贵显之征。天下名山五千三百七十，名地六万四千五十六里。

#### 分字分词释义

- **山**：高山 / 艮卦所主 / 止、静、高、贵
- **行**：行走、攀登 / 进取、上升 / 主动进取
- **艮**：易经第52卦 / 山卦 / 止、静、背
- **止而不动**：艮卦之德 / 该止则止 / 动静有时
- **动极归静**：阳极生阴 / 动后归静 / 休息收藏

#### 规范化释义（primary_lang_explained）

梦见山中行走，大吉。攀登高山，居于高位，是亨通尊贵的象征。对应《易经》艮卦，止而不动，动极归静。做此梦者，主握大权、获大利、享大福，富贵佳祥。

山也属于地，是贵显的征兆。天下名山五千三百七十座，名地六万四千五十六里。

#### 完整对等诠释（secondary_lang_full）

Dreaming of walking in the mountains is greatly auspicious. Climbing high mountains and occupying elevated positions symbolizes prosperity and nobility. It corresponds to the Gen (Mountain) hexagram in the I Ching, representing stillness and cessation—when movement reaches its extreme, it returns to stillness. The dreamer will grasp great power, obtain great profit, and enjoy great fortune and noble prosperity.

Mountains also belong to the earth element and signify eminence and distinction. There are 5,370 famous mountains under heaven, and 64,056 li of notable terrain.

#### 核心要点

- 山行为山水类梦象核心吉兆
- 对应艮卦，止而不动，动极归静
- 山=高位/权力/贵显
- 主握大权——权力象征
- 主获大利——财富增益
- 主享大福——福禄绑绵

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v3_004]` `[trigger: 梦山行]` `[factor_trigger: dream_shan_xing AND yijing_gen AND dream_shan_beng AND dream_cheng_deng AND dream_cheng_hui AND dream_qiao_xin AND dream_qiao_huai]` `[role: 主干]` 山行大吉。履高山，居高位，亨通尊贵之象也。 → 《梦林玄解·卷三》#山行
- `[ns_mlxj_v3_005]` `[trigger: 梦山行]` `[factor_trigger: dream_shan_xing]` `[role: 主干依赖]` 在易为艮止而不动，动极归静，梦此者握大权获大利。 → 《梦林玄解·卷三》#山行"""
    normalized_text_zh: str = """"""
    subject: str = "1 山行（山水类首条·完整精校）"
    factor_refs: list = ['dream_shan_xing', 'yijing_gen']
    
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
        l1_anchor="mlxj_v1.0.0_1_山行_山水类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
