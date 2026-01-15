"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101501
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
    semantic_id="smth_v1.0.0_学堂词馆本义与取位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 学堂词馆本义与取位(SemanticEntry):
    """
    - **原文（source_text）**：
  论学堂词馆。夫学堂者，如人读书之在学堂；词馆者，如今官翰林谓之词馆，取其学业精专、文章出类。长生乃学堂之正位，如金命见辛巳，金长生在巳，辛巳纳音又属金...
    """
    
    original_text: str = """- **原文（source_text）**：
  论学堂词馆。夫学堂者，如人读书之在学堂；词馆者，如今官翰林谓之词馆，取其学业精专、文章出类。长生乃学堂之正位，如金命见辛巳，金长生在巳，辛巳纳音又属金是也。临官乃词馆正位，如金命壬申，金临官在申，壬申纳音又属金是也，余以类推。

- **分字分词释义**：
  - **学堂**：对应长生之位，重在学习起步与基础打底。
  - **词馆**：对应临官之位，重在文章成熟与进入仕途或专业体系。

- **规范化释义（primary_lang_explained）**：
  本节先将学堂比作读书之处，将词馆比作翰林等高阶文职所在之馆。以金命为例，辛巳长生为学堂，壬申临官为词馆，纳音又俱属金，象征从入学、研习到文章成名、入仕的全过程。其他五行可类推，各有其长生、临官对应的学堂与词馆之地。

- **完整对等诠释（secondary_lang_full）**：
  The Study Hall marks the Longevity position of a given element and symbolises the place where learning is begun and foundations are laid, while the Literary Hall marks the Arrival at Office position, where knowledge matures and enters public or professional life.
  Using the Metal examples, the text shows how seeing both positions with matching Nayin points to a full path from schooling to institutional role.
  Other elements can be treated in the same pattern and in modelling these halls are best read as indicators of how smoothly learning can be started and later turned into recognised competence.
- **核心要点**：
  - 学堂词馆格重点刻画一个人在「学习—成才—入仕」链条上的潜力与节点，不可脱离整体命局孤立判断。
  - 在工程化分析中，应根据学堂所在宫位的气势、是否空亡、是否与官星、禄马、贵人等同见，给出一个「学业与文章转换力」评分，而不能只看有无学堂标签。
 
- **详细解说**：
  1) 在五行与长生、临官体系中，为每一命局标注学堂与词馆所在的位置，形成 `xuetang_flag`、`ciguan_flag` 及其落宫信息；
   2) 结合命主的日主、用神与行运，评估学堂、词馆是否为用神或中性之神，并据此计算「学习起步质量」与「文章/专业成熟度」评分；
   3) 与现实数据中的受教育年限、学历层级、专业与职位匹配度等变量对照，用以标定学堂词馆特征在现代环境下的实际效应；
   4) 在解释层，将学堂词馆更多用于说明「学习路径的顺畅度与上升通道」，而非直接许诺科第与官职。

 - 反例与边界：
   - 不宜因命盘有学堂、词馆便断定必读完高等学府或必入仕途，现代社会存在多样化职业路径；
   - 若学堂落空亡或被严重刑冲，其「读书」一面可能表现为反复中断或学习效率低下，不能只按吉格论；
   - 工程上若将学堂词馆特征直接映射为「社会阶层」指标，容易引入阶层偏见，应通过多任务建模分离「学习能力」与「资源获取」；
   - 反向误区是完全忽略学堂词馆，使模型无法表达「学习能力强但资源一般」与「资源好但学习意愿弱」的差异。

 - 小例（示意）：
   - 某命局学堂与词馆皆在用神宫位，行运不破，现实中从中学到研究生一路顺利，专业与职业高度匹配，系统可用「学堂词馆链路顺畅」解释其教育路径平稳；
  - 另一命局学堂有而词馆落空亡，现实表现为早期学习基础不错但在升学或职业转轨时多有卡顿，系统则在解释中提示「需要在中后段规划上投入更多精力」。"""
    normalized_text_zh: str = """"""
    subject: str = "学堂词馆本义与取位"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_56', 'bazi_semantic', 'bazi_structure_factor_57', 'bazi_semantic', 'bazi_state_factor_134', 'bazi_semantic', 'bazi_function_factor_8', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_学堂词馆本义与取位_001_L1",
    )
    version: str = "1.0.0"
