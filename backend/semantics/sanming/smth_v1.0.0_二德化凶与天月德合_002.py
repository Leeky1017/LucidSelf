"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101463
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
    semantic_id="smth_v1.0.0_二德化凶与天月德合_002",
    book_id="sanming",
    engine_id="bazi"
)
class 二德化凶与天月德合(SemanticEntry):
    """
    - **分字分词释义**：
  - **月空、月厌、月煞**：与月份相关的一组时日忌神，用以补充对当月气机偏枯或不利的描述。
  - **天赦日、天喜神、旌德煞、旌钺煞、三公煞**：一系列与赦罪、喜庆...
    """
    
    original_text: str = """- **分字分词释义**：
  - **月空、月厌、月煞**：与月份相关的一组时日忌神，用以补充对当月气机偏枯或不利的描述。
  - **天赦日、天喜神、旌德煞、旌钺煞、三公煞**：一系列与赦罪、喜庆、功名、诛戮相关的时日神煞。

- **规范化释义（primary_lang_explained）**：
  在讲明天德、月德之后，原文顺带列出一批与月令相关的辅助神煞：月空、月厌、月煞提示当月中某些干支组合代表气机空虚、压抑或不利；天赦日则是四时专气所聚之日，可视作「系统性宽宥节点」，若命造在此日又逢德星与吉时，多主灾祸得以赦免；天喜神带来喜庆气氛；旌德、旌钺、三公煞则与功名、刑戮高度相关：得其正用者主勋业显赫，错用或被克者则多有刑戮之忧。

- **核心要点**：
  - 德星体系不仅包括天德、月德，还与一系列月令与时日神煞联动，共同刻画「此时此刻」的福凶基调。
  - 在工程上，这些可以统一抽象为「时间特征层」：不同月日组合为整体风险与机遇曲线带来微调，德星则是其中最强的正向因子之一。

- **详细解说**：
  1) 在时间特征模块中，为每一个年月日组合标注月空、月厌、月煞、天赦日、天喜、旌德、旌钺、三公煞等标签，并与天德、月德信息统一存储；
  2) 在事件预测任务中，将这些标签作为「时间调制因子」参与风险与机遇曲线的建模，例如在天赦日与德星同见时下调惩罚类事件概率；
  3) 对于旌德、旌钺、三公煞等强烈功名/刑戮象，结合命主行业与现实行为数据，区分「正向显赫」与「高危诛戮」的不同路径；
  4) 在解释层中，尽量使用现代语言描述这些时日神煞的作用，如「处于监管高压周期」「处于宽宥窗口」，避免直接使用古代刑罚字样对用户造成心理负担。

- 反例与边界：
  - 不宜将任何带三公煞或旌钺煞的命局都解读为「大贵」或「必遭重刑」，应回到实际职业、行为模式与外部环境综合判断；
  - 若缺乏精确的出生时间与历法换算，强行细分日时神煞可能引入噪音，应有降级策略（仅使用月度层级或只启用德星而暂不启用细小煞）；
  - 工程上若把所有时日神煞一股脑加入模型而不做特征选择，会导致维度爆炸与解释困难，需要通过重要性分析筛选关键因子；
  - 反向误区是完全忽略时间特征，只看静盘，使系统对「特定时间窗口的宽宥或高压」缺乏表达能力。

- 小例（示意）：
  - 某命局逢天德月德并临之月，又值天赦日，现实中在那一阶段虽有违规风险却最终得到从轻处理，系统可用「德星 + 天赦提供宽宥窗口」来解释事件走向；
  - 另一命局在三公煞叠加的年份发生产业政策强监管与团队清洗，命主身居关键岗位，系统在事前就应提高该时间段的风险提示等级，并在解释中说明这是「制度高压与个人位置叠加」的结果。"""
    normalized_text_zh: str = """"""
    subject: str = "二德化凶与天月德合"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_52', 'bazi_semantic', 'bazi_state_factor_127', 'bazi_semantic', 'bazi_state_factor_128', 'bazi_semantic', 'bazi_state_factor_129', 'bazi_semantic', 'bazi_state_factor_130', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_二德化凶与天月德合_002_L1",
    )
    version: str = "1.0.0"
