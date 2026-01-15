"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101274
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
    semantic_id="smth_v1.0.0_乙禄卯_001",
    book_id="sanming",
    engine_id="bazi"
)
class 乙禄卯(SemanticEntry):
    """
    - **原文（source_text）**：
  乙禄卯。见乙卯，谓之喜神旺禄，主吉。丁卯为截路空亡，主凶。己卯，进神禄；辛卯，破禄，又为交神，半吉半凶。癸卯带太乙，死禄，虽贵终贫。

- **分字分...
    """
    
    original_text: str = """- **原文（source_text）**：
  乙禄卯。见乙卯，谓之喜神旺禄，主吉。丁卯为截路空亡，主凶。己卯，进神禄；辛卯，破禄，又为交神，半吉半凶。癸卯带太乙，死禄，虽贵终贫。

- **分字分词释义**：
  - **喜神旺禄**：用神得禄且无冲破，为最理想的禄象。
  - **进神禄**：有向上、向前之象，多主进益与升迁机会。
  - **交神**：两种力量交织，既有助亦有损，形成复杂局面。
  - **死禄**：禄位与用神相冲，表面有贵，终局羸弱。

- **规范化释义（primary_lang_explained）**：
  乙木禄在卯。若见乙卯同宫，为「喜神旺禄」，乙木得自身禄位，且不受破坏，多主顺遂与吉祥。若丁卯，则为截路空亡，有路断之象，多主波折与损失。己卯称「进神禄」，土来承木，象征有现实平台托举，多主有进步、晋升契机。辛卯为「破禄」，金克木，且为交神，说明有外部力量搅入，吉凶参半。癸卯带太乙号为「死禄」，虽有贵象，但禄位终被耗泄，多见贵而不富、后劲不足的情形。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood has its Lu in Mao. When Mao holds Yi itself, this is the "Joy-Spirit Prosperous Lu": the useful spirit sits on its own Lu without being harmed, and the pattern usually gives smooth progress and good fortune.
  Ding-Mao is classified as "Cut-Path Void"; the road is interrupted and losses and setbacks are common, so it is judged as inauspicious. Ji-Mao is called the "Advancing-Spirit Lu", where Earth supports Wood and stands for a concrete platform or institution that lifts the person upward, often bringing promotion or advancement.
  Xin-Mao is "Broken Lu" and at the same time a "Crossing-Spirit" configuration: outside forces cut into and entangle the Lu, so the result is half favourable, half difficult. Gui-Mao is said to carry the Taiyi spirit and forms a "Dead Lu": there are signs of rank and distinction, but the Lu is gradually drained, so one often becomes noble in status yet struggles to sustain long-term material security.
- **核心要点**：
  - 乙禄卯重在「细腻成长与环境承托」，破禄多由金水过重而来，提示环境过度干预。
  - 「死禄」的关键词是「前贵后困」，在系统里可作为职业生命周期中晚期风险的标记。
  - 拟合现代场景时，可把乙禄卯的各种变化映射到「成长路径 + 外部干预 + 终局可持续性」三个参数上。

- **详细解说**：
  1) 首先确认日主为乙木，再查看卯支分布：是否为日坐卯、或年、月、时支见卯，标记「坐禄/见禄」；
  2) 根据卯上所透天干（乙、丁、己、辛、癸）分类为喜神旺禄、截路空亡、进神禄、破禄、死禄，在模型中编码为不同子类型；
  3) 将「喜神旺禄、进神禄」与「成长环境稳定、平台支持良好」关联，将「截路空亡、破禄、死禄」与「路径被打断、外界干预过多、前高后低」等模式关联；
  4) 在职业与发展曲线预测中，使用这些标签调整不同阶段的成功概率，尤其对死禄结构，在中后期给予额外的风险预警与策略建议。

- 反例与边界：
  - 不宜一见「死禄」就断终身贫困或必有大祸，更合理的解释是：早期顺利、后期维持难度加大，需要更重视持续性与收缩策略；
  - 不可将「破禄」理解为「一切贵气作废」，若整体格局清纯、用神得力，仍可以在局部波折中获得不错的发展；
  - 工程上若只把乙禄卯当作单一「好/坏」标签，会掩盖其对于阶段性风险与结构性干预的精细提示；
  - 反向误区是完全忽略这些禄型差异，只以学历、职位等表面变量建模，从而失去对中长期风险的前瞻视角。

- 小例（示意）：
  - 某乙日命，日坐卯，月支又为己卯，系统可标记为「坐禄 + 进神禄」，在职业路径上倾向「在稳定平台上逐级上升」的模式，并提示中年阶段有较好的晋升窗口；
  - 另一乙日命，年柱癸卯为死禄，早年行木火运、晚年行金水运，系统则在中后期提示「贵而不富、攻坚期后的守成压力增大」，建议提前进行资产与身份的多元布局。"""
    normalized_text_zh: str = """"""
    subject: str = "乙禄卯"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_yi_mao', 'bazi_semantic', 'bazi_state_marker_3', 'bazi_semantic', 'bazi_state_marker_4', 'bazi_semantic', 'bazi_state_marker_5', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_乙禄卯_001_L1",
    )
    version: str = "1.0.0"
