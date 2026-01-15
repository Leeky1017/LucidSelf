"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654392
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
    semantic_id="zw_v1.0.0_五局大限起例_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 五局大限起例(SemanticEntry):
    """
    - 分字分词释义：

  - **五局**：金木水火土五种命局分类。
  - **金四局**：金局起限四岁。
  - **木三局**：木局起限三岁。
  - **水二局**：水局起限二岁。
  - *...
    """
    
    original_text: str = """- 分字分词释义：

  - **五局**：金木水火土五种命局分类。
  - **金四局**：金局起限四岁。
  - **木三局**：木局起限三岁。
  - **水二局**：水局起限二岁。
  - **火六局**：火局起限六岁。
  - **土五局**：土局起限五岁。
  - **起限年数**：第一个大限开始的年龄。
  - **顺逆规则**：大限宫位前进或后退的规律。

#### 金四局：
紫微金宫四岁花。初一寻猪初二龙，顺进三步逆退一。

#### 木三局：
生逢木宫三岁游。初一起龙初二牛，逆进二宫安二日。

#### 水二局：
坎水宫中二岁行。初一起丑初二寅，顺行一宫安二日。

#### 火六局：
离火宫中六岁奇。初二骑马初四龙，进二退二各一日。

#### 土五局：
戊土五岁居其中。初一午上二亥宫，逆行二宫安一日。

#### 完整对等诠释（secondary_lang_full·43五局大限）：

  The Five-Bureau Major Limit system determines at what age the first ten-year period begins and how the limit palaces progress. Metal-Four Bureau (Jin Si Ju) starts the first limit at age four; Wood-Three Bureau (Mu San Ju) at age three; Water-Two Bureau (Shui Er Ju) at age two; Fire-Six Bureau (Huo Liu Ju) at age six; Earth-Five Bureau (Tu Wu Ju) at age five. Each bureau also specifies a starting palace and a forward or backward stepping pattern based on the birth day within the lunar month. For example, Metal Bureau natives born on the first day start from Hai palace, second day from Chen, then advance three steps forward and retreat one. This layered algorithm ensures that natives of different bureau types have distinct limit trajectories even if their natal charts share similar star placements."""
    normalized_text_zh: str = """"""
    subject: str = "五局大限起例"
    factor_refs: list = ['structure_wuju', 'bureau_jinsi', 'algo_qixian_nian', 'algo_shunni_rule']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_五局大限起例_001_L1",
    )
    version: str = "1.0.0"
