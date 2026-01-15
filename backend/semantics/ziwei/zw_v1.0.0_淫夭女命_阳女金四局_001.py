"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.700016
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
    semantic_id="zw_v1.0.0_淫夭女命_阳女金四局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 淫夭女命阳女金四局(SemanticEntry):
    """
    - 分字分词释义：

  - **虽有左右加会**：有辅彼左右星加会，本应有助力。
  - **羊陀夹空夹劫**：擎羊陀罗天空地劫四面夹制命宫。
  - **若非夰即主下贱**：若不早夰也会沉为社会底...
    """
    
    original_text: str = """- 分字分词释义：

  - **虽有左右加会**：有辅彼左右星加会，本应有助力。
  - **羊陀夹空夹劫**：擎羊陀罗天空地劫四面夹制命宫。
  - **若非夰即主下贱**：若不早夰也会沉为社会底层。
  - **虽紫禄何力**：即便有紫微或禄星也无力救助。
  - **夰于九岁**：九岁时因多重夹煎夰亡。
  - **阳女金四局**：淫夰女命盘的五行局数，金四局主刚断受困。

- **原文（source_text）**：  
  淫夰女命。阳女金四局。此命虽有左右加会，但羊陀夹空夹劫，若非夰，即主下贱，虽紫禄何力，故夰于九岁而亡。

- **规范化释义（primary_lang_explained）**：  
  此淫夭女命为阳女金四局，「虽有左右加会」说明有辅弼星的支持，「但羊陀夹空夹劫」，命宫被擎羊、陀罗、天空、地劫等多重凶星夹制。「若非夭，即主下贱」，在这种配置下，命主若不早夭，也会沦为社会底层。「虽紫禄何力」，即便有紫微或禄星，也无力扭转夹煞败局。最终「故夭于九岁而亡」。

- **完整对等诠释（secondary_lang_full）**：  
  This chart is that of a Yang Metal female. Although Zuo‑You provide support, Yang‑Tuo and Kong‑Jie form a multi‑layered clamp around Life. "If not dead young, then destined for lowliness." Even Zi Wei or Lu cannot overcome. The child dies at nine.

- **核心要点**：  
  1. 左右加会但被羊陀空劫多重夹制。  
  2. 若非夭即下贱，紫禄无力救助。  
  3. 九岁夭亡。"""
    normalized_text_zh: str = """"""
    subject: str = "淫夭女命（阳女金四局）"
    factor_refs: list = ['pattern_zuoyou_jiahui', 'malefic_yangtuo_kongjie_jia', 'quality_ruofei_yao_xiajian', 'quality_sui_zilu_heli', 'result_yao_yu_jiusui']
    
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
        l1_anchor="zw_v1.0.0_淫夭女命_阳女金四局_001_L1",
    )
    version: str = "1.0.0"
