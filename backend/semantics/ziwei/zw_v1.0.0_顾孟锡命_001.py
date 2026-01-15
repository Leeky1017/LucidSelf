"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699588
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
    semantic_id="zw_v1.0.0_顾孟锡命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 顾孟锡命(SemanticEntry):
    """
    - 分字分词释义：

  - **巨日同宫**：巨门与太阳同宫，主聪敏与声名兼具。
  - **双禄守恒**：两颗禄星守于命垣或三方，主俸禄丰厚与财源稳定。
  - **左右供照**：左辅右彼同宫供照...
    """
    
    original_text: str = """- 分字分词释义：

  - **巨日同宫**：巨门与太阳同宫，主聪敏与声名兼具。
  - **双禄守恒**：两颗禄星守于命垣或三方，主俸禄丰厚与财源稳定。
  - **左右供照**：左辅右彼同宫供照命宫，主贵人护持与富贵享用。
  - **申人有忌**：生于申支者于特定限运逢凶，较他支更易显凶。
  - **火星之位**：火星所在宫位，主突然、火爆式的灾祸或事故。
  - **见凶即死**：逢凶曜之运即刻引发致命事件，几无缓冲。
  - **阳男水二局**：顾孟锡命盘的五行局数，水二局主智慧享乐。

- **原文（source_text）**：  
  顾孟钖命。阳男水二局。巨日同宫，双禄守恒，左右供照，为富贵宜矣。柰申人大小二限行于火星之位，见凶也，即死。子五十三岁。

- **规范化释义（primary_lang_explained）**：  
  顾孟钖命为阳男水二局，巨门与太阳同宫，双禄守于命垣，左右辅弼同宫供照，是「巨日同宫 + 双禄守命 + 左右同拱」之极厚富贵格局，一生适宜富贵享用。  
  但对申人而言，大小二限行至火星所在之位，火星为猛烈突发之凶曜，申人逢之尤为不利。原文言「见凶也，即死」，表明在此运程中，一旦触发火星之凶性，结合原有结构的聚能效应，极易在短时间内出现致命事件，于五十三岁骤亡。此命例呈现「富贵厚实而折于火星重击」的命局图像。

- **完整对等诠释（secondary_lang_full）**：  
  Gu Mengxi’s chart is that of a Yang Water native in the Second Configuration. Ju Men and the Sun share a palace, two Lu stars "guard" the Life sector, and Left and Right Assistants attend—"Ju and Sun in one place, double Lu guarding, Zuo‑You serving." This describes a very solid pattern for wealth and comfort: ample resources, support and recognition throughout life.  
  However, for natives of Shen, when both major and minor periods pass through the sector of Huo Xing, the star of sudden fire and violence, the danger is acute. The text summarises this as "seeing misfortune and immediately dying" at age fifty‑three. The implication is that the concentrated power of the natal configuration, when struck by a sharp malefic transit, can translate into a swift, catastrophic event—illness, accident or violence. The case shows a person eminently suited to wealth and enjoyment whose life nonetheless ends abruptly under a harsh Mars‑type influence.

- **核心要点**：  
  1. 巨日同宫、双禄守命、左右供照，是极厚的富贵与享乐格局。  
  2. 申人大小二限行至火星之位，火星凶性被放大，形成极高风险。  
  3. 五十三岁遭遇火星主导之限运而骤亡，是「富贵而难免横祸」命例。

- **叙事素材（narrative_snippets）**：
  - **巨日双禄**："巨日同宫，双禄守恒，左右供照，为富贵宜矣"，顾孟锡命主一生适宜享受丰厚的物质与名位。
  - **火星为忌**："柰申人大小二限行于火星之位，见凶也，即死"，申年生人在大小限同行火星之位时，火曜凶性被推至极致。
  - **五十三岁横祸**：原文点明"子五十三岁"，说明其在五十三岁因火星主导限运而骤然身故。
  - **现代应用**：对生活安逸、资源雄厚的人而言，在形成「火星+生年忌限」的年份，尤其要警惕高危出行、酒驾、极限运动与急性心脑血管风险，避免在最舒适的阶段被一场突变打断人生进程。"""
    normalized_text_zh: str = """"""
    subject: str = "顾孟锡命"
    factor_refs: list = ['pattern_juri_tonggong', 'pattern_shuanglu_shouheng', 'pattern_zuoyou_gongzhao', 'condition_shenren_youji', 'malefic_huoxing_wei', 'result_jianxiong_jisi']
    
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
        l1_anchor="zw_v1.0.0_顾孟锡命_001_L1",
    )
    version: str = "1.0.0"
