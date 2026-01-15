"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699205
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
    semantic_id="zw_v1.0.0_张子房命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 张子房命(SemanticEntry):
    """
    - 分字分词释义：

  - **双禄朝守**：禄存与化禄同时拱守命宫，主极富贵。
  - **紫府同宫**：紫微天府同在一宫，主极贵。
  - **左右昌曲加会**：左辅右彼文昌文曲同会命宫，主筹画...
    """
    
    original_text: str = """- 分字分词释义：

  - **双禄朝守**：禄存与化禄同时拱守命宫，主极富贵。
  - **紫府同宫**：紫微天府同在一宫，主极贵。
  - **左右昌曲加会**：左辅右彼文昌文曲同会命宫，主筹画天下。
  - **限落夹地**：晚年限运落入夹地，预示困境。
  - **衰死之地**：十二长生中的衰死位，主气绝。
  - **天伤天空天使**：多重凶星齐聚于衰死位，主寿终。
  - **阳男火六局**：张子房命盘的五行局数，火六局主热情谋略。

- **原文（source_text）**：  
  张子房命。阳男火六局。此是双禄朝守，左右昌曲加会，又兼紫府同宫，作极富贵之命，直湏限落夹地，故以命亡。七十六，大小二限在天伤、天空、天使，衰死之地，是以难逃。

- **规范化释义（primary_lang_explained）**：  
  张子房命属阳男火六局，双禄朝守、左右昌曲加会、紫府同宫，主极富贵。然限落夹地，七十六岁大小二限在天伤、天空、天使、衰死之地，诸凶叠加而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Zhang Zifang's Yang male Fire Sixth chart has Double Salary guarding, Left‑Right Chang‑Qu converge, Ziwei‑Tianfu same palace—extreme wealth and honour. Period falls into flanked territory. At 76 both periods at Celestial Wound, Void, Envoy, Decay‑Death positions. Inescapable malefics cause death.

- **核心要点**：  
  1. 双禄朝守、左右昌曲、紫府同宫，主极富贵。  
  2. 限落夹地，晚年凶险。  
  3. 大小限在天伤天空天使衰死之地，为寿终应期。

- **叙事素材（narrative_snippets）**：
  - **双禄紫府**："此是双禄朝守，左右昌曲加会，又兼紫府同宫，作极富贵之命"，张子房命主极富贵、筹画天下。
  - **限落夹地**："直湏限落夹地，故以命亡"，晚年限运落入夹地，预示身心被困于局势漩涡。
  - **衰死之地**："七十六，大小二限在天伤、天空、天使，衰死之地，是以难逃"，天伤天空天使齐聚衰死位，为自然寿终的收束节点。
  - **现代应用**：智谋型权臣在高龄阶段遇到天伤天空衰死组合之年，应主动淡出权力中心，专注养生与家园，顺势而退。"""
    normalized_text_zh: str = """"""
    subject: str = "张子房命"
    factor_refs: list = ['pattern_zifutonggong', 'pos_shuaisi', 'pattern_xianlaojiadi', 'source_ref', 'rel_zhangzifang_001', 'pattern_shuangluzifu', 'rel_zhangzifang_002', 'pattern_xianlaojiadi', 'rel_zhangzifang_003', 'pos_shuaisi', 'evi_zhangzifang_001', 'pos_shuaisi', 'rule_shuaisi_tianshang', 'concept_zifu_same', 'concept_decay_death']
    
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
        l1_anchor="zw_v1.0.0_张子房命_001_L1",
    )
    version: str = "1.0.0"
