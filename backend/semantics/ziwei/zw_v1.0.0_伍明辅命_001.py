"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699148
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
    semantic_id="zw_v1.0.0_伍明辅命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 伍明辅命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄生逢**：生年即逢化权化禄，主先天福德。
  - **左右昌曲加会**：左辅右彼文昌文曲同会命宫，主辅佐文才。
  - **七杀守命**：七杀星坐守命宫，主壮年峙...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄生逢**：生年即逢化权化禄，主先天福德。
  - **左右昌曲加会**：左辅右彼文昌文曲同会命宫，主辅佐文才。
  - **七杀守命**：七杀星坐守命宫，主壮年峙嵬。
  - **擎羊天空**：早年犯擎羊天空，三十六后方遂志。
  - **天伤陀罗**：大限遇天伤陀罗，主凶险。
  - **酉生人忌**：酉年生人于巳宫有特定禁忌。
  - **小限重逢**：小限再遇凶星，主命亡。

- **原文（source_text）**：  
  伍明辅命。阴男水二局。权禄生逢左右昌曲加会，七杀守命，壮年峥嵘，为战国明辅，升五岁，有犯擎羊、天空，直在卅六后方遂志。六十二，大很入巳，天伤陀罗酉人忌，小限重逢，故死。

- **规范化释义（primary_lang_explained）**：  
  伍明辅命属阴男水二局，权禄生逢、左右昌曲加会、七杀守命，主壮年峥嵘。早年犯擎羊天空，三十六后方遂志。六十二岁大限入巳，天伤陀罗加会，酉生人有忌，小限重逢凶星而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Wu Mingfu's Yin male Water Second chart has Authority‑Salary at birth, Left‑Right Chang‑Qu converge, Seven Killings guards Life—outstanding in prime years. Early affliction by Yang Blade and Void; success after 36. At 62 major enters Si with Wound and Tuo; You natives face taboos. Minor re‑encounters malefics, causing death.

- **核心要点**：  
  1. 权禄左右昌曲加会、七杀守命，主壮年峥嵘。  
  2. 早年犯擎羊天空，三十六后方遂志。  
  3. 大限天伤陀罗、酉生忌、小限重逢，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **壮年峥嵘**："权禄生逢左右昌曲加会，七杀守命，壮年峥嵘"，伍明辅命主中年显达、战功卓著。
  - **三十六后遂志**："升五岁，有犯擎羊、天空，直在卅六后方遂志"，早年多阻，三十六后方能一展所长。
  - **晚年凶限**："六十二，大限入巳，天伤陀罗酉人忌，小限重逢，故死"，晚年天伤陀罗与生年忌限、小限重逢凶星叠加为命亡时点。
  - **现代应用**：此类命例可用于提醒：事业高峰之后，仍需为晚年限运预留退路与健康缓冲，而非一路冲到极限。"""
    normalized_text_zh: str = """"""
    subject: str = "伍明辅命"
    factor_refs: list = ['pattern_quanlu', 'star_qisha', 'pattern_xiaoxianchongfeng', 'source_ref', 'rel_wumingfu_001', 'pattern_quanlu', 'rel_wumingfu_002', 'taboo_youshengji', 'rel_wumingfu_003', 'pattern_xiaoxianchongfeng', 'evi_wumingfu_001', 'pattern_xiaoxianchongfeng', 'rule_yousheng_tianshang', 'concept_seven_killings', 'concept_minor_reencounter']
    
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
        l1_anchor="zw_v1.0.0_伍明辅命_001_L1",
    )
    version: str = "1.0.0"
