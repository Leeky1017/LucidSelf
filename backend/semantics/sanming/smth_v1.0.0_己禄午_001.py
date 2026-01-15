"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101313
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
    semantic_id="smth_v1.0.0_己禄午_001",
    book_id="sanming",
    engine_id="bazi"
)
class 己禄午(SemanticEntry):
    """
    - **原文（source_text）**：
  己禄午。见庚午，截路空亡。壬午，死鬼禄，俱凶。甲午，进神合禄，显达之象。丙午，喜神禄。戊午，伏神羊刃禄，凶。

- **规范化释义（primary_l...
    """
    
    original_text: str = """- **原文（source_text）**：
  己禄午。见庚午，截路空亡。壬午，死鬼禄，俱凶。甲午，进神合禄，显达之象。丙午，喜神禄。戊午，伏神羊刃禄，凶。

- **规范化释义（primary_lang_explained）**：
  己土禄在午。庚午为截路空亡，金克土又有路断之象，凶。壬午为「死鬼禄」，水克土且为鬼禄，多凶。甲午为「进神合禄」，木土相合有显达之象，吉。丙午为「喜神禄」，火生土而禄位得生，吉。戊午为「伏神羊刃禄」，刃性伏藏于禄中，凶。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth has its Lu in Wu. Geng-Wu is another instance of "Cut-Path Void": Metal overcomes Earth and again gives the image of a broken road, so it is considered harmful.
  Ren-Wu forms the "Dead-Ghost Lu", where Water overcomes Earth and ghostly themes are emphasised, and it is generally treated as very inauspicious. Jia-Wu is the "Advancing-Spirit Merge-Lu"; Wood combining with Earth suggests union and promotion, and so it symbolises conspicuous achievement.
  Bing-Wu is the "Joy-Spirit Lu": Fire generates Earth and the Lu gains fresh vitality, making this a genuinely auspicious form. Wu-Wu is the "Hidden-Spirit Yangren Lu", where the blade-like Yangren quality is buried within the Lu position; its power is volatile and easily turns destructive, so it tends toward misfortune.
- **核心要点**：
  - 己禄午与丁禄午类似，均寄禄于午火之地，偏重土承火势与木土合化。
  - 「进神合禄」为己禄午中最佳结构，木土相合有显达之象；「死鬼禄」则为最凶，水克土且为鬼禄。
  - 工程建模时可将「合禄/鬼禄」作为对立标签，用于识别「平台支持vs外部克制」的极端情况。

- **详细解说**：
  1) 确认日主为己土，定位午支，并识别其上天干庚、壬、甲、丙、戊；
  2) 将庚午、壬午、甲午、丙午、戊午分别视为截路空亡、死鬼禄、进神合禄、喜神禄、伏神羊刃禄，并在系统中拆解为「合化度」「克制强度」「刃风险」等子维度；
  3) 对甲午进神合禄和丙午喜神禄结构，提高在显达、得生上的成功概率；对庚午、壬午、戊午三类，则同步提高阻断、克制、刃风险权重；
  4) 在行运分析中，当午支或相关火土局被再度触发时，结合木火、金水的配置，判断是进入「合化显达」阶段，还是「鬼禄克制」阶段。

- 反例与边界：
  - 不宜将「死鬼禄」一律判为必死必败，应看整体格局是否有化解与转化；
  - 不能把「进神合禄」浪漫化为「必然显达」，仍需考虑整体格局与用神配合；
  - 工程上若不区分合禄与鬼禄，只统一标记为「有禄」，会淹没关键差异；
  - 反向误区是过度追求名目，忽略实际质地与可持续性。

- 小例（示意）：
  - 某己日命，甲午进神合禄且有火土相生，系统可评估其在稳定平台上有显达机会，并在建议中强调「借助平台 + 木土合化」；
  - 另一己日命，壬午死鬼禄且水势过重，行运再逢金水旺地，系统则在职业与健康层面同时发出预警：需警惕克制过度，适合寻找调候与化解之道。"""
    normalized_text_zh: str = """"""
    subject: str = "己禄午"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_ji_wu', 'bazi_semantic', 'bazi_state_marker_10', 'bazi_semantic', 'bazi_state_marker_11', 'bazi_semantic', 'bazi_state_marker_12', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_己禄午_001_L1",
    )
    version: str = "1.0.0"
