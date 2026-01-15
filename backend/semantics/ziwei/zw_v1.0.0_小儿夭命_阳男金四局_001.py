"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699983
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
    semantic_id="zw_v1.0.0_小儿夭命_阳男金四局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 小儿夭命阳男金四局(SemanticEntry):
    """
    - 分字分词释义：

  - **本宫守命垣星本宜易养**：命宫主星不陷，原本是易养格局。
  - **羊夹陀夹空夹劫**：擎羊陀罗空亡地劫四面夹制命宫。
  - **若非夭即主下贱**：若不早夭也会...
    """
    
    original_text: str = """- 分字分词释义：

  - **本宫守命垣星本宜易养**：命宫主星不陷，原本是易养格局。
  - **羊夹陀夹空夹劫**：擎羊陀罗空亡地劫四面夹制命宫。
  - **若非夭即主下贱**：若不早夭也会沉为社会底层。
  - **虽紫禄何力**：即便有紫微或禄星也无力救助。
  - **夭于九岁**：九岁时因多重夹煎夭亡。
  - **阳男金四局**：小儿夭命盘的五行局数，金四局主刚断受困。

- **原文（source_text）**：  
  小儿夭命。阳男金四局。此看本宫守命垣星，本宜易养，但爽羊夹陀夹空夹劫，若非夭，即主下贱，虽紫禄何力，故夭于九岁而亡。

- **规范化释义（primary_lang_explained）**：  
  小儿夭命为阳男金四局，「本宫守命垣星，本宜易养」，说明从命宫主星来看，原本是容易养育的格局，主星并无明显落陷。然而「但爽羊夹陀夹空夹劫」，命宫被多重凶星夹制：擎羊、陀罗、空亡、地劫等四面包夹，形成极端险恶的「多重夹煞」结构。原文直言「若非夭，即主下贱」，意指在这种凶夹之下，即便不早夭，也会沦为社会底层。「虽紫禄何力」，说明即便有紫微或禄星等吉星，也无力扭转夹煞的败局，最终「夭于九岁而亡」。

- **完整对等诠释（secondary_lang_full）**：  
  This "Infant Death" chart for a Yang Metal native originally shows a principal star in the Life palace that "should be easy to raise." However, the palace is squeezed by Yang Blade, Tuo Luo, Kong and Jie from all sides—a severe multi‑layered malefic encirclement. The text bluntly states that under such pressure, "if not dead young, then destined for lowliness." Even Zi Wei or Lu cannot overcome such a cage. The child dies at nine.

- **核心要点**：  
  1. 本宫主星本宜易养，但被多重凶煞夹制，格局逆转。  
  2. 羊夹、陀夹、空夹、劫夹，形成极端「四面凶夹」结构。  
  3. 即便紫禄同在也无力救助，命主九岁夭亡。"""
    normalized_text_zh: str = """"""
    subject: str = "小儿夭命（阳男金四局）"
    factor_refs: list = ['quality_bengong_yiyang', 'malefic_yangtuo_kongjie_jia', 'quality_ruofei_yao_xiajian', 'quality_sui_zilu_heli', 'result_yao_yu_jiusui', 'principle_jiasha_xiongyu_luoxian']
    
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
        l1_anchor="zw_v1.0.0_小儿夭命_阳男金四局_001_L1",
    )
    version: str = "1.0.0"
