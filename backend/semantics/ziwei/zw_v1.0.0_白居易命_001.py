"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699660
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
    semantic_id="zw_v1.0.0_白居易命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 白居易命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄拱照**：权星与禄星同拱命宫，主功名、权位与俸禄并臻。
  - **左右夹垣**：左辅右彼夹拱命垣，主贵人护持。
  - **日月同宫**：太阳太阴同宫，主光明与...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄拱照**：权星与禄星同拱命宫，主功名、权位与俸禄并臻。
  - **左右夹垣**：左辅右彼夹拱命垣，主贵人护持。
  - **日月同宫**：太阳太阴同宫，主光明与阴柔兼备。
  - **昌曲守身**：文昌文曲守护命身，主文名与才学出众。
  - **命带忌星**：命垣自带忌星，预示寿命难以极长。
  - **陀罗天空之卿**：大限行至陀罗与天空同会之地，主突发打击与虚耗。
  - **擎羊亥**：小限行擎羊亥位，为命主所忌，主刚烈冲撞。
  - **阴男木三局**：白居易命盘的五行局数，木三局主文才清贵。

- **原文（source_text）**：  
  白居易命。阴男木三局。权禄拱照，左右夹垣，日月同宫，昌曲守身，富贵之命。命带忌星，寿难长永。大限到佗罗天空之卿，小限行擎羊亥，生人有忌，故死子五十二岁。

- **规范化释义（primary_lang_explained）**：  
  白居易命为阴男木三局，命局中权星与禄星拱照，左右夹垣，日月同宫，再加文昌、文曲守身，是「权禄拱照 + 左右夹垣 + 日月同宫 + 昌曲守身」的综合文贵格局，一生富贵，文名与权位并著。  
  但命垣自带忌星，预示寿命难以极长，晚年容易因忌星所引发之病变或波折而折损。原文又言：大限行至佗罗与天空同会之地，小限行擎羊亥位，为命主所忌，是「陀罗 + 天空 + 擎羊」三重凶曜同来；其中陀罗与擎羊主突发打击与硬碰，天空主虚耗与根基不稳，合而为极高危的五十二岁重凶年份，故于此年死亡。命例借白居易之名，呈现「文权双美、却因忌星与三重凶曜折寿」的形态。

- **完整对等诠释（secondary_lang_full）**：  
  Bai Juyi’s chart is that of a Yin Wood native in the Third Configuration. Power and Lu stars shine on the Life, Left and Right Assistants flank the palace, the Sun and Moon share a sector, and Wen Chang and Wen Qu attend the self. This combination—"Quan‑Lu illuminating, Zuo‑You flanking, Sun‑Moon together, Chang‑Qu guarding"—depicts a literary nobleman whose fortunes and influence are substantial.  
  Yet the Life also contains Ji‑type stars, signalling that longevity may be limited. Later in life the major period reaches a region where Tuo Luo and Tian Kong meet, while the minor period passes through the Hai position of Qing Yang, sharply inauspicious for the native. Tuo Luo and Qing Yang are associated with sudden blows and confrontations; Tian Kong with emptiness and structural instability. Together they define age fifty‑two as a year of compounded danger, and the text records death at that time. The case portrays a figure of great literary and political standing whose life is shortened by a convergence of natal Ji influence and triple malefic transits.

- **核心要点**：  
  1. 权禄拱照、左右夹垣、日月同宫、昌曲守身，为典型文权双美之贵格。  
  2. 命垣带忌星，使寿命难以极长。大限陀罗天空、小限擎羊亥成三重重凶。  
  3. 命例呈现「文名权位兼具却在五十二岁折寿」的才子权臣格局。

- **叙事素材（narrative_snippets）**：  
  - **文权双美**："权禄拱照，左右夹垣，日月同宫，昌曲守身，富贵之命"，白居易命主既有文名又握实权，为典型文权双美。  
  - **命带忌星**："命带忌星，寿难长永"，说明在完美格局之下，寿数本身存在隐形上限。  
  - **三重凶曜**："大限到佗罗天空之卿，小限行擎羊亥，生人有忌，故死子五十二岁"，陀罗、天空与擎羊亥三重凶曜叠加，为五十二岁折寿的关键结构。  
  - **现代应用**：对现实中既有高声望又身居要职的文人官员或知识分子来说，当个人命局本身带忌星，又遇多重凶曜叠加年份，宜主动从台前退到幕后，减少高危公开活动与过劳，以免在事业高峰被「系统性透支」提前收场。"""
    normalized_text_zh: str = """"""
    subject: str = "白居易命"
    factor_refs: list = ['pattern_quanlu_gongzhao', 'pattern_zuoyou_jiayuan', 'pattern_riyue_tonggong', 'pattern_changqu_shoushen', 'malefic_tuoluo_tiankong', 'malefic_qingyang_hai']
    
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
        l1_anchor="zw_v1.0.0_白居易命_001_L1",
    )
    version: str = "1.0.0"
