"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699603
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
    semantic_id="zw_v1.0.0_李嗣源命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 李嗣源命(SemanticEntry):
    """
    - 分字分词释义：

  - **七杀朝斗**：七杀星朝向斗位，主武职、权威与高危性。
  - **紫府朝垣**：紫微与天府朝向官垣，主尊贵与统摄能力。
  - **左右拱照**：左辅右彼拱照命宫，主...
    """
    
    original_text: str = """- 分字分词释义：

  - **七杀朝斗**：七杀星朝向斗位，主武职、权威与高危性。
  - **紫府朝垣**：紫微与天府朝向官垣，主尊贵与统摄能力。
  - **左右拱照**：左辅右彼拱照命宫，主贵人扶持与富贵终身。
  - **大限到夹地**：大限行至被地劫或地网夹困之地。
  - **遇流羊**：流年逢羊刃星，主刚烈冲撞与意外危险。
  - **太岁逢陀亥**：太岁与陀罗同会于亥位，主难以回避的冲击与破坏。
  - **阴男土五局**：李嗣源命盘的五行局数，土五局主厚重武功。

- **原文（source_text）**：  
  李嗣源命。阴男土五局。七杀朝斗，一生爵禄荣昌，紫府朝垣，左右拱照，终身富贵。大十七岁，大限到夹地，遇流羊，太岁逢陀亥，生人有忌，故凶。

- **规范化释义（primary_lang_explained）**：  
  李嗣源命为阴男土五局，「七杀朝斗」为强势武职格局，一生爵禄荣昌，再加紫微、天府朝垣，左右辅弼拱照，是「七杀朝斗 + 紫府朝垣 + 左右拱照」的权贵命结构，终身富贵不缺。此类格局多主有武功军权、位高而威重。  
  然而，原文指出于「大十七岁」即大约晚年关键阶段，大限行至「夹地」，可理解为地劫或地网夹困之处，又遇流年羊刃，太岁逢陀罗亥位，为该生所忌，形成「夹地 + 流羊 + 太岁陀亥」的多重凶象。一方面象征权势所依之结构被夹击、受制，另一方面代表身体与气数在高压环境中难以支撑，最终以凶终。此命例呈现「武功权贵，在地网与羊刃、陀罗叠加之运中折损」的命局形态。

- **完整对等诠释（secondary_lang_full）**：  
  Li Siyuan’s chart is that of a Yin Earth native in the Fifth Configuration. "Seven Killing facing the Dipper" denotes a powerful martial configuration, promising rank and honours; with Zi Wei and Tian Fu "facing the court," and Left and Right Assistants flanking, the pattern becomes one of sustained wealth and authority. Such a structure suits a military ruler or commander whose status is both high and solid.  
  Yet around a key later period—"the great seventeen"—the major period enters a "clamped earth" region, suggestive of Di‑type nets and constraints. At the same time flowing Yang Blade appears, and the Annual Tai Sui meets Tuo Luo at Hai, an especially inauspicious position for the native. This combination of earth nets, Blade and Tuo Luo indicates that the power base and bodily resilience are simultaneously under siege, leading to a destructive outcome. The case portrays a martial ruler whose great power is eventually broken when heavy, constricting and cutting influences converge. 

- **核心要点**：  
  1. 七杀朝斗配合紫府朝垣与左右拱照，是典型武功权贵命。  
  2. 晚年大限行夹地，又遇流羊与太岁陀亥，形成结构受制与身命受冲的高危组合。  
  3. 命例体现「权贵在重凶限运中折损」的武职命轨迹。

- **叙事素材（narrative_snippets）**：
  - **七杀朝斗**："七杀朝斗，一生爵禄荣昌"，李嗣源命主以七杀武贵之格起家，爵禄荣昌。
  - **紫府左右**："紫府朝垣，左右拱照，终身富贵"，紫府朝垣并得左右辅弼，构成稳固的武勋权贵格局。
  - **夹地流羊**："大十七岁，大限到夹地，遇流羊，太岁逢陀亥，生人有忌，故凶"，夹地配流羊与陀罗，为晚年权力基础与身体同时承压的凶象。
  - **现代应用**：对拥有实权、长期镇守一线的军警或安全类职业者，在明显「地网 + 羊刃 + 陀罗」组合年份，应主动简化战线与卸下部分职责，避免在体系重组或前线高危任务中透支性命。"""
    normalized_text_zh: str = """"""
    subject: str = "李嗣源命"
    factor_refs: list = ['pattern_qisha_chaodou', 'pattern_zifu_chaoyuan', 'pattern_zuoyou_gongzhao', 'timing_daxian_jiadi', 'timing_liuyang', 'timing_taisui_tuohai']
    
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
        l1_anchor="zw_v1.0.0_李嗣源命_001_L1",
    )
    version: str = "1.0.0"
