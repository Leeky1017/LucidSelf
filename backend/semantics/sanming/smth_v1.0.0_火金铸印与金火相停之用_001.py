"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412890
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
    semantic_id="smth_v1.0.0_火金铸印与金火相停之用_001",
    book_id="sanming",
    engine_id="bazi"
)
class 火金铸印与金火相停之用(SemanticEntry):
    """
    - **原文（source_text）**：

  赋云：金非火不能成器，火非金无以显诸用，金火相停，有铸印之象，忌丑字为损模。赋云：乘轩衣冕，金火何多。又云：金鬼无偏，此之谓也。

- 分字分词释义...
    """
    
    original_text: str = """- **原文（source_text）**：

  赋云：金非火不能成器，火非金无以显诸用，金火相停，有铸印之象，忌丑字为损模。赋云：乘轩衣冕，金火何多。又云：金鬼无偏，此之谓也。

- 分字分词释义：

  - **金非火不能成器**：金属若不经火炼，则难成锋刃与器物，象征刚劲之性需经历锻炼方能有用。
  - **火非金无以显诸用**：火若无金可炼，则多成空焰，难见实际成果，象征热情需有具体载体方能落实。
  - **金火相停**：金与火力量相当、彼此制约而不相毁，形成一种互相成就而不相伤的平衡状态。
  - **有铸印之象**：如同以金火合铸官印，象征权柄、名分与正式身份的确立。
  - **忌丑字为损模**：丑中藏癸辛己，土湿金寒，既损火力，又损金之利，仿佛铸印之模具受损，不利成器。
  - **金鬼无偏**：指金煞得用而不偏邪，既能成权，又不至于为祸，强调金火平衡之重要。

- **规范化释义（primary_lang_explained）**：

  火金铸印格，以“金火相停、相生相成”为核心意象。原文指出：金若无火难成器，火若无金难显用，说明刚劲之才若不经历锻炼，便难成可用之器；而热烈之火若无合适的载体，则终归虚耗。只有当金与火彼此均衡，既不火过金焦，又不金重灭火，才形成“金火铸印”的上乘格局，象征权柄在身、名分明确。

  这一格局在现实中常表现为：一方面具备坚决果断的执行力（金），另一方面又有热诚投入与表现欲（火）；二者适度结合时，易在需要制度、权力与执行的领域获得认可，如行政管理、军警系统、企业管理层等。若丑土过重，或火、金一方偏枯，则如铸印之模受损，要么刚烈而不为用，要么热情而难成器。

- 核心要点：

  - 强调**金火平衡**：火为锻炼之力，金为成器之材，两者相停方有“铸印”之象。
  - 忌丑土过重等破局之物，防止火力受损、金性钝化。
  - 合宜时，多主权柄在手、名分明确，宜从事需要“令出必行”的岗位。

- 详细解说：

  若从五行关系看，火克金，本为相克之象；但在火金铸印格中，这种克制被重新诠释为“锻炼”：火使金软化可塑，金因火而成器——这是“以克为用”的典型。关键在于火不能过烈，以免金被烧毁；金也不能太弱，否则承受不起锻炼。

  实务判断时，可以从以下几方面观察：

  1. 金是否有根、有气，能承受火之锻炼；
  2. 火是否适度而不至于焚金成灰；
  3. 是否有土、水介入调和，避免火金两败俱伤。若能形成“金火相停”的格局，多见其人既有原则，又能担当，一生重要关口常靠“硬仗”成名；若失衡，则容易因刚猛太过、好胜心重，而在事业或健康上付出代价。

- **校勘与字词辨析（双语）**：

  - “金非火不能成器，火非金无以显诸用”两句，本稿统一理解为“以克为炼”的象意，而非一般的相克凶论。
  - “忌丑字为损模”一句，本稿在白话中以“损坏铸印之模”比喻格局被湿土阻塞，不再详分丑土内部支藏。
  - “金鬼无偏”一语，本稿视为对“金煞得用而不偏凶”的评价，强调需注意煞气是否被火与全局所制。
  - **English**：
    - Whether the qi is controlled by fire and the overall configuration noted.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_209]` `[trigger: 火金铸印]` `[factor_trigger: huojin_zhuyin AND jinhuo_xiangting]` `[role: 主干]` 金非火不能成器，火非金无以显诸用。 → 《三命通会》卷六#火金铸印
  - `[ns_smth_06_210]` `[trigger: 铸印之象]` `[factor_trigger: jinhuo_xiangting AND zhuyin_guiqi]` `[role: 主干依赖]` 金火相停，有铸印之象。 → 《三命通会》卷六#火金铸印
  - `[ns_smth_06_211]` `[trigger: 忌丑损模]` `[factor_trigger: ji_chouzi AND sunmo_poju]` `[role: 条件分支]` 忌丑字为损模。 → 《三命通会》卷六#火金铸印
  - `[ns_smth_06_212]` `[trigger: 乘轩衣冕]` `[factor_trigger: jinhuo_heduo AND chengxuan_yimian]` `[role: 总结]` 乘轩衣冕，金火何多。 → 《三命通会》卷六#火金铸印"""
    normalized_text_zh: str = """"""
    subject: str = "火金铸印与金火相停之用"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_fire_metal_marker', 'bazi_semantic', 'bazi_structure_metal_fire_config', 'bazi_semantic', 'bazi_state_degree_36', 'bazi_semantic', 'bazi_state_factor_35', 'bazi_semantic', 'bazi_condition_chou', 'bazi_semantic', 'bazi_condition_metal_fire', 'bazi_semantic', 'source_ref', 'rel_smth_06_184', 'huojinzhuyin_presence', 'rel_smth_06_185', 'chengqi_chengdu', 'rel_smth_06_186', 'chouzi_sunmo_risk', 'evi_smth_06_184', 'huojinzhuyin_presence', 'rule_zhuyin', 'evi_smth_06_185', 'zhuyin_guiqi', 'rule_chengxuan', 'evi_smth_06_186', 'chouzi_sunmo_risk', 'rule_sunmo', 'map_smth_06_123', 'map_smth_06_124']
    
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
        l1_anchor="smth_v1.0.0_火金铸印与金火相停之用_001_L1",
    )
    version: str = "1.0.0"
