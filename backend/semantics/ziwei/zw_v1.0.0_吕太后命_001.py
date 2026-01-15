"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699991
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
    semantic_id="zw_v1.0.0_吕太后命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 吕太后命(SemanticEntry):
    """
    - 分字分词释义：

  - **双禄守垣**：双禄星守护命垣，主极高财权。
  - **紫府左右昌曲加会**：紫微天府与左右昌曲同会，主尊贵与文采。
  - **吕后专权二重天禄**：经典格局，主女...
    """
    
    original_text: str = """- 分字分词释义：

  - **双禄守垣**：双禄星守护命垣，主极高财权。
  - **紫府左右昌曲加会**：紫微天府与左右昌曲同会，主尊贵与文采。
  - **吕后专权二重天禄**：经典格局，主女性专权掌政。
  - **七杀夫宫克夫**：七杀居夫妻宫，主克害丈夫。
  - **火铃羊陀洴夹命垣**：火铃羊陀等凶星夹制命垣，主淫欲。
  - **大限夹地小限羊陀凑合**：晚年大小限同遇凶星，主寿终。
  - **阳女火六局**：吕太后命盘的五行局数，火六局主明亮专权。

- **原文（source_text）**：  
  吕太后命。阳女火六局。双禄守垣，紫府左右，昌曲加会，经云：吕后专权，二重天禄，七杀夫宫克夫。火铃羊陀洴夹命垣，亦主淫欲。大限夹地，小限羊陀凑合是凶，故寿终焉。

- **规范化释义（primary_lang_explained）**：  
  吕太后命为阳女火六局，「双禄守垣，紫府左右，昌曲加会」，构成极高等级的女命权贵格局。「经云：吕后专权，二重天禄」，暗示此类命局可以取得如吕后般的专权地位。然而「七杀夫宫克夫」，七杀落入夫妻宫，对配偶形成克制。「火铃羊陀洴夹命垣，亦主淫欲」，火铃与羊陀夹命，带来强烈欲望。应期：「大限夹地，小限羊陀凑合是凶」，最终「寿终焉」。

- **完整对等诠释（secondary_lang_full）**：  
  Empress Lü's chart is that of a Yang Fire female. Double Lu guards the Life palace; Zi Wei and Tian Fu join Zuo‑You; Chang and Qu also converge. The classic notes: "Lü Hou wielded absolute power—double Heavenly Lu." Yet Qi Sha in the Spouse palace harms the husband. Fire‑Bell and Yang‑Tuo form a clamp around Life, signaling strong desires. When the major period reached a "clamped" position and the minor period aligned with Yang‑Tuo, her life ended.

- **核心要点**：  
  1. 双禄紫府左右昌曲加会，是吕后专权型的女命极贵格局。  
  2. 七杀夫宫克夫，火铃羊陀夹命主淫欲。  
  3. 大限夹地、小限羊陀凑合，最终寿终。"""
    normalized_text_zh: str = """"""
    subject: str = "吕太后命"
    factor_refs: list = ['pattern_shuanglu_shouyuan', 'pattern_zifu_zuoyou_changqu', 'pattern_lvhou_zhuanquan', 'malefic_qisha_fugong', 'malefic_huoling_yangtuo_jiaming', 'timing_daxian_jiadi_xiaoxian']
    
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
        l1_anchor="zw_v1.0.0_吕太后命_001_L1",
    )
    version: str = "1.0.0"
