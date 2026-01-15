"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228166
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
    semantic_id="smth_v1.0.0_大林木与杨柳木_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大林木与杨柳木(SemanticEntry):
    """
    - **原文（source_text）**：
  戊辰己巳，则气不成量，物已及时，枝叶茂盛，郁然成林，取其木之盛也，故曰大林木。壬午癸未，木至午而死，至未而墓，故杨柳盛夏叶凋，枝干微弱，取其性之柔也，...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊辰己巳，则气不成量，物已及时，枝叶茂盛，郁然成林，取其木之盛也，故曰大林木。壬午癸未，木至午而死，至未而墓，故杨柳盛夏叶凋，枝干微弱，取其性之柔也，故曰杨柳木。

- **分字分词释义**：
  - **气不成量**：气达到无法测量的程度。
  - **物已及时**：植物已经到了适当的时候。
  - **郁然成林**：茂密地成为树林。
  - **木至午而死**：木到午位而死绝。
  - **木至未而墓**：木到未位而入墓。
  - **盛夏叶凋**：盛夏时叶子凋零。
  - **枝干微弱**：枝干柔弱。
  - **取其性之柔**：取其性质的柔软。

- **规范化释义（primary_lang_explained）**：
  戊辰己巳，气达到无法测量的程度，植物已经到了适当的时候，枝叶茂盛，茂密地成为树林，取其木最茂盛的状态，所以叫大林木。壬午癸未，木到午位而死绝，到未位而入墓，所以杨柳树在盛夏时叶子凋零，枝干柔弱，取其性质的柔软，所以叫杨柳木。

- **完整对等诠释（secondary_lang_full）**：
  Wuchen-Jisi: qi immeasurable, plants already timely, branches and leaves luxuriant, densely forming forest, taking Wood's flourishing state, thus called Great-Forest Wood. Renwu-Guiwei: Wood reaching Wu dies, reaching Wei enters tomb, thus Willow in midsummer withers leaves, branches and trunk feeble, taking their nature's softness, thus called Willow Wood.

- **核心要点**：
  - 戊辰己巳：大林木（枝叶茂盛，郁然成林）
  - 壬午癸未：杨柳木（午死未墓，枝干柔弱）
  - 大林木为木的盛极
  - 杨柳木为木的衰弱

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_180]` `[trigger: 大林木与杨柳木]` `[factor_trigger: great_forest_wood AND willow_wood AND nayin_wood_flourish_decline]` `[role: 主干]` 戊辰己巳，枝叶茂盛，郁然成林，取其木之盛也，故曰大林木。壬午癸未，木至午而死，至未而墓，枝干微弱，取其性之柔也，故曰杨柳木。 → 《三命通会》卷一#大林木与杨柳木

- **详细解说**：
  此条续解木纳音。戊辰己巳为"大林木"：辰巳属春夏之交，木气最盛，枝叶繁茂，郁郁葱葱成为大森林，这是木的极盛状态。壬午癸未为"杨柳木"：午为火旺之地，未为土旺之地，木到午死到未墓（五行十二长生），就像杨柳在盛夏反而叶落，枝干柔弱下垂，取其柔软之性。从桑柘木（盘曲）→松柏木（坚韧）→大林木（极盛）→杨柳木（柔弱），木经历了从初生、坚强、繁盛到衰弱的过程。大林木命格较强，杨柳木命格柔弱但有韧性。

- **校勘与字词辨析（双语）**：
  - **中文**："气不成量"指气盛到无法衡量。"郁然成林"形容树木茂密。"木至午而死"，午属火，木生火为泄，故木死于午。杨柳树枝条柔软下垂，夏季易枯。
  - **English**: "Qi immeasurable" means qi so abundant it cannot be measured. "Densely forming forest" describes luxuriant trees. "Wood dies at Wu"—Wu is Fire, Wood generates Fire (draining), thus Wood dies at Wu. Willow branches soft and drooping, easily withering in summer."""
    normalized_text_zh: str = """"""
    subject: str = "大林木与杨柳木"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_大林木与杨柳木_001_L1",
    )
    version: str = "1.0.0"
