"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755651
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
    semantic_id="zw_v1.0.0_论格星数高下_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论格星数高下(SemanticEntry):
    """
    - 分字分词释义：

  - **星格**：星曜阴阳、庙旺、吉凶配合的等级。
  - **数格**：阴阳相半、数理相生的等级。
  - **阴阳相半**：阴星与阳星数量平衡。
  - **数不相生**...
    """
    
    original_text: str = """- 分字分词释义：

  - **星格**：星曜阴阳、庙旺、吉凶配合的等级。
  - **数格**：阴阳相半、数理相生的等级。
  - **阴阳相半**：阴星与阳星数量平衡。
  - **数不相生**：数理五行不成生扶关系。
  - **三方四正**：命宫与三合宫位及对宫的结构。
  - **九等**：星格与数格交叉形成的九个等级。
  - **富比陶朱**：极富的象征，比拟巨商陶朱公。
  - **异路前程**：非科举正途的仕途荣誉。
  - **寿享遐龄**：长寿之命。
  - **六畜之命**：极端贫贱的最低等命格。

- 原文（断句）：

  紫府与数相合何如？紫微南北斗中天帝王，天府乃南斗主。又有阴阳相半者。若阴阳不相半，又数不相生，为下格；阴阳纯一为中格。又三方四正皆吉星，为上格；吉凶相半守照，为中格；纯是恶杀，为下格，凶徒论。凡星得上格而数得上格，为第一；人臣星得上格而数得中格，为第二，位至三公；星得上格而数得下格，为第三，位至六卿，皆为上格。上寿之人，星得中格而数得上格，为第四，位至监司；星中数中，为第五，位至县令；星中数下，为第六，异路前程、贵题，皆为中等享福之人也。又星得下格而数得上格，为第七，衣禄丰足，富比陶朱，子孙蕃盛，寿享遐龄；以星虽凶，而又入格合局故也耳。若虚名虚利，星下数中，为第八，衣食无亏；星下数下，为第九，辛苦奔波，贫穷夭折。上中下三等，依理而断也，则上可以知祖宗之源流，下可以知子孙之昌盛。

- 规范化释义（primary_lang_explained）：

  本条将星曜格局与数理阴阳配合交叉，划分出九个高低不同的等级。先以星曜本身的庙旺与吉凶定为上、中、下三格，再以阴阳是否相半、数理是否相生分出上、中、下三等数格，二者相乘成为九档。星上格配数上格，是第一等至高贵格；星上格配数中、数下，为第二、第三等，仍属三公、六卿一类的上贵之流。星中格配上、中、下数格，则成第四、第五、第六等，多主监司、县令或异路贵题等中等享福之命。

  星下格若兼得上数，仍可成第七等，虽星性凶烈，却因格局得以成就而富比陶朱、寿长子多；星下数中，为第八等，只剩虚名虚利，衣食不缺而已；星下数下，则为第九等，下下之局，多见辛苦奔波、贫穷夭折。由此可见，命局的祖宗根基与子孙昌盛，既取决于星曜本身的格局高下，也受制于背后数理阴阳的相生相克。

- 完整对等诠释（secondary_lang_full）：

  This passage links star patterns with numerical patterns and grades both on
  three levels. Star grade looks at the dignity and quality of the main
  stars—whether they are strong or weak, benefic or malefic, balanced in
  yin and yang. Number grade looks at whether the underlying yin–yang counts
  and stem–branch sequences support or frustrate the configuration. Crossing
  upper, middle and lower star grades with upper, middle and lower number
  grades produces nine tiers, from charts fit for the highest offices down
  to lives marked by toil, poverty and early death. Each tier corresponds to
  a different combination of rank, wealth and longevity.

  The text pays special attention to mixed cases. When the stars are of only
  middling or even low grade but the numbers are strong and the chart still
  forms a proper configuration, a person may still enjoy great wealth, long
  life and many descendants—"wealth to rival Tao Zhu". When both stars and
  numbers are weak, on the other hand, the most one can expect is modest
  security, or at worst hardship and shortened life. In practice this scheme
  asks the practitioner to judge star strength and numerical support
  together, rather than being dazzled by famous configurations. It becomes a
  matrix for reading how far ancestral merit can carry a chart upward and how
  far its blessings or burdens may flow on to later generations.

- 核心要点：

  1. 星与数双重分级：先将星格（星之阴阳、庙旺、吉凶）与数格（阴阳相半、数理相生）各分上中下，再交叉成九等.
  2. 上三等（第一～第三等）：星上格为前提，数上/中/下依次对应帝王近臣、三公、六卿等级的贵格.
  3. 中三等（第四～第六等）：星中格为主，配以上中下数格，对应监司、县令和异路贵题等中等享福之命.
  4. 下三等（第七～第九等）：星下格配以上中下数格，高者虽星凶却因入格合局而富比陶朱，低者则虚名虚利，乃至辛苦奔波、贫穷夭折.
  5. 评价重点：不可只看星或只看数，须同时观「星之格局」与「数之配合」方能准确分层.

- 叙事素材（narrative_snippets）：

  - **九等分级**："星数各分上中下，交叉成九等"，建立星格与数格的双重评估体系。
  - **上三等**："星上格配数上中下，对应帝王近臣、三公、六卿"，最高三等贵格。
  - **中三等**："星中格为主，对应监司、县令、异路贵题"，中等享福之命。
  - **下三等**："星下格高者富比陶朱，低者贫穷夭折"，下格仍有分化。
  - **富比陶朱**："星虽凶却因入格合局而富"，星凶但数强仍可富贵。
  - **现代应用**：本条建立"星×数"的九宫格评估矩阵，可作为命盘分层的参考框架。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j5_021]` `[trigger: 九等分级]` `[factor_trigger: level_jiudeng]` `[role: 主干]` 九等分级为星格与数格交叉形成的九等评估体系。 → 《卷五》"星数各分上中下"
  - `[ns_zwds_j5_022]` `[trigger: 星格评估]` `[factor_trigger: xingge_pinggu]` `[role: 主干]` 星格评估为星曜品质位置阴阳配置的评估。 → 《卷五》
  - `[ns_zwds_j5_023]` `[trigger: 数格评估]` `[factor_trigger: shuge_pinggu]` `[role: 主干]` 数格评估为阴阳数理相生配合的评估。 → 《卷五》
  - `[ns_zwds_j5_024]` `[trigger: 帝王近臣]` `[factor_trigger: result_diwangjinchen]` `[role: 结果]` 帝王近臣为第一等极贵的命格结果。 → 《卷五》"帝王近臣"
  - `[ns_zwds_j5_025]` `[trigger: 三公六卿]` `[factor_trigger: result_sangongliuqing]` `[role: 结果]` 三公六卿为第二三等贵格的命格结果。 → 《卷五》"三公、六卿"
  - `[ns_zwds_j5_026]` `[trigger: 监司县令]` `[factor_trigger: result_jiansi_xianling]` `[role: 结果]` 监司县令为中等享福的命格结果。 → 《卷五》"监司、县令"
  - `[ns_zwds_j5_027]` `[trigger: 富比陶朱]` `[factor_trigger: result_fubi_taozhu]` `[role: 结果]` 富比陶朱为虽星凶但因入格合局而大富的结果。 → 《卷五》"富比陶朱"
  - `[ns_zwds_j5_028]` `[trigger: 贫穷夭折]` `[factor_trigger: result_pinqiong_yaozhe]` `[role: 结果]` 贫穷夭折为下格最凶的命格结果。 → 《卷五》"贫穷夭折"
  - `[ns_zwds_j5_029]` `[trigger: 质量评估]` `[factor_trigger: quality_ruofei_yao_xiajian]` `[role: 条件分支]` 质量评估为命格品质高下的判断。 → 《卷五》
  - `[ns_zwds_j5_030]` `[trigger: 自禄合力]` `[factor_trigger: quality_sui_zilu_heli]` `[role: 条件分支]` 自禄合力为禄星得力的配置判断。 → 《卷五》"""
    normalized_text_zh: str = """"""
    subject: str = "论格星数高下"
    factor_refs: list = ['level_xingge', 'level_shuge', 'level_jiudeng', 'pattern_fubitaozhu', 'pattern_yiluqiancheng', 'source_ref', 'rel_xingshu_001', 'level_xingge', 'rel_xingshu_002', 'level_jiudeng', 'rel_xingshu_003', 'pattern_fubitaozhu', 'evi_xingshu_001', 'level_xingge', 'rule_xingshu_diyi', 'evi_xingshu_002', 'level_jiudeng', 'rule_xingshu_diqi', 'concept_star_grade', 'concept_number_grade']
    
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
        l1_anchor="zw_v1.0.0_论格星数高下_001_L1",
    )
    version: str = "1.0.0"
