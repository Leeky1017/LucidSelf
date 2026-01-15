"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699725
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
    semantic_id="zw_v1.0.0_范丹贫命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 范丹贫命(SemanticEntry):
    """
    - 分字分词释义：

  - **生来贫贱**：命局自出生即显贫困之象，财福根基薄弱。
  - **劫空临财福**：劫空落在财帛与福德宫，主资源与福报被抽空。
  - **禄马落空地**：禄星与马星落...
    """
    
    original_text: str = """- 分字分词释义：

  - **生来贫贱**：命局自出生即显贫困之象，财福根基薄弱。
  - **劫空临财福**：劫空落在财帛与福德宫，主资源与福报被抽空。
  - **禄马落空地**：禄星与马星落于空亡或势弱之地，主难以稳固收益与行动力。
  - **中年限入美景**：中年行运入吉地，暂得发达名扬。
  - **禄倒马倒**：在关键限运中禄马失位或受克，主支撑系统崩塾。
  - **忌太岁相冲**：忌星随太岁而冲命，主该年严重冲击。
  - **阳男土五局**：范丹贫命盘的五行局数，土五局主厚重贫困。

- **原文（source_text）**：  
  范丹贫命。阳男土五局。生来贫贱，劫空临财福之乡，禄马落于空地，中年限入美景，方得发达名杨。七十五岁，大限入于天空，小限七十七同入此地，禄倒马倒，忌太岁相冲，故亡。

- **规范化释义（primary_lang_explained）**：  
  范丹贫命为阳男土五局，「生来贫贱」源于劫空同临财帛与福德之乡，禄马又落于空地，象征财禄与行动力难以着落，早年多为「有心无力」，根基薄弱。  
  但中年限入美景，说明行运暂入吉地，方得发达名扬，生活与地位有所改善。七十五岁，大限入天空之地，小限七十七岁同入此处，「禄倒马倒」指原本支撑财富与行动的关键星曜在此阶段俱失其力，再加忌星随太岁而冲，是「天空 + 禄马倒 + 忌太岁相冲」的晚年重凶组合。于是命主于此阶段死亡，呈现「早贫、中年略达、终因结构性虚空与冲击而亡」的命运。

- **完整对等诠释（secondary_lang_full）**：  
  Fan Dan’s "poor" chart is that of a Yang Earth native in the Fifth Configuration. From birth he is marked by poverty: Jie and Kong occupy the sectors of wealth and blessings, while Lu and Ma fall into void positions. This indicates that income, opportunity and mobility are difficult to anchor—ambition exists, but the base is weak.  
  In midlife the periods move into "beautiful scenery," a metaphor for favourable sectors, and he finally attains some success and reputation. Yet at seventy‑five the major period enters Tian Kong, and at seventy‑seven the minor period also returns there; "Lu falls, Ma falls" signals the collapse of the very factors supporting wealth and movement. With Ji‑type stars following Tai Sui to冲 the configuration, the late‑life combination of emptiness, fallen Lu/Ma and冲 transits leads to death. The example depicts a life of early deprivation, modest midlife improvement and structurally fragile late years.

- **核心要点**：  
  1. 劫空临财福、禄马落空地，使命主早年生来贫贱、根基薄弱。  
  2. 中年限入美景方得发达名扬，但整体结构偏虚，难以长久。  
  3. 七十五岁后大限小限双入天空之地，禄倒马倒并逢忌太岁相冲，最终寿终。"""
    normalized_text_zh: str = """"""
    subject: str = "范丹贫命"
    factor_refs: list = ['quality_shenglai_pingjian', 'malefic_jiekong_caif', 'malefic_luma_luokong', 'timing_zhongnian_meijing', 'malefic_ludao_madao', 'timing_ji_taisui_chong']
    
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
        l1_anchor="zw_v1.0.0_范丹贫命_001_L1",
    )
    version: str = "1.0.0"
