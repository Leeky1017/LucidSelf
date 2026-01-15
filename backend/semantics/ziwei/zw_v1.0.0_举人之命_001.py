"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699916
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
    semantic_id="zw_v1.0.0_举人之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 举人之命(SemanticEntry):
    """
    - 分字分词释义：

  - **君臣庆会**：帝星与臣辅星同会的高格结构，主大贵。
  - **左右同宫**：左辅右彼同居一宫，主贵人辅佐有力。
  - **夹昌夹曲**：文昌文曲分列两侧夹住命宫，...
    """
    
    original_text: str = """- 分字分词释义：

  - **君臣庆会**：帝星与臣辅星同会的高格结构，主大贵。
  - **左右同宫**：左辅右彼同居一宫，主贵人辅佐有力。
  - **夹昌夹曲**：文昌文曲分列两侧夹住命宫，主文采与科名。
  - **火星同垣**：火星与主星同宫，带来烈性与波动。
  - **空劫迭守**：地空地劫重叠守护命局，削弱根基。
  - **流昌居卯照身限**：流年文昌居于卯位照到身宫或流年限运，触发入仕。
  - **阳男火六局**：举人命盘的五行局数，火六局主明亮科名。

- **原文（source_text）**：  
  举人之命。阳男火六局。君臣庆会，左右同宫，夹昌夹曲之格，当为大贵。但干火星同垣，空劫迭守，故限交科禄。辛酉年世二中不得连登，至癸未年，流昌居卯，照身限出仕矣。

- **规范化释义（primary_lang_explained）**：  
  举人之命为阳男火六局，「君臣庆会，左右同宫，夹昌夹曲之格」，构成君主星与臣辅星同聚的高格结构，配合左右辅弼同宫，再有文昌文曲夹命，本来「当为大贵」。然而「但干火星同垣，空劫迭守」，火星同垣带来烈性与波动，空劫迭守则削弱了根基，「故限交科禄」——在考运与科禄之事上多有曲折。原文详述应期：「辛酉年世二中不得连登，至癸未年，流昌居卯，照身限出仕矣」，说明辛酉年时虽入围却未能连续登科，到癸未年时流年文昌居于卯位照身命限，才终于入仕。此命例展示「高格受阻，终以特定流年配合而成」的举人命路径。

- **完整对等诠释（secondary_lang_full）**：  
  This "Juren" (provincial graduate) chart for a Yang Fire native in the Sixth Configuration features a classic "Emperor‑Minister Meeting" pattern: Zuo and You share the same palace, and Chang‑Qu form a clamp. This should indicate high nobility. Yet Fire Star sharing the palace plus Kong‑Jie repeatedly guarding the key zones create volatility and drain. Exam success becomes entangled—"crossing at Ke and Lu," meaning exam luck is delayed. In the Xinyou year, the native passed but did not rise consecutively; only in Guiwei, when Flowing Wen Chang reached Mao and aligned with Body‑period, did the native finally obtain office.

- **核心要点**：  
  1. 君臣庆会配左右夹昌夹曲，本是大贵格局。  
  2. 火星同垣、空劫迭守压制了科禄顺畅度，导致考运曲折。  
  3. 癸未年流昌照身限，终于入仕，呈现「流年配合而成」的举人命路径。"""
    normalized_text_zh: str = """"""
    subject: str = "举人之命"
    factor_refs: list = ['pattern_junchen_qinghui', 'pattern_zuoyou_tonggong', 'pattern_jia_changqu', 'malefic_huoxing_tongyuan', 'malefic_kongjie_dieshou', 'timing_liuchang_juemao']
    
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
        l1_anchor="zw_v1.0.0_举人之命_001_L1",
    )
    version: str = "1.0.0"
