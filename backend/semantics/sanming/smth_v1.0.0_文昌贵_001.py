"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101479
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
    semantic_id="smth_v1.0.0_文昌贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 文昌贵(SemanticEntry):
    """
    - **原文（source_text）**：
  有文昌贵：甲乙蛇口乙猪头，丙狗丁龙戊向猴；己午庚寅辛未贵，六壬卯位癸逢牛。

- **分字分词释义**：
  - **文昌贵**：偏主文章、科名与才学...
    """
    
    original_text: str = """- **原文（source_text）**：
  有文昌贵：甲乙蛇口乙猪头，丙狗丁龙戊向猴；己午庚寅辛未贵，六壬卯位癸逢牛。

- **分字分词释义**：
  - **文昌贵**：偏主文章、科名与才学之贵。
  - **歌诀配干支**：以口诀方式列出不同日主所对应的文昌贵位置。

- **规范化释义（primary_lang_explained）**：
  文昌贵是一类以文章与才学为主的贵神，原文以歌诀列举甲乙、丙丁戊己庚辛壬癸等日主，各自对应的贵位干支组合。此类组合若得之，并配合原局清气，多主读书有成、文章见长、科名有望。

- **完整对等诠释（secondary_lang_full）**：
  Wenchang Noble is a spirit of scholarship and letters that signals affinity with study, writing and examinations rather than brute power or wealth.
  The mnemonic verse assigns different Wenchang positions to different day stems, and when these positions are strong and well integrated they often correspond to good learning environments and a taste for reading or composition.
  It should therefore be used as a weight on education and literary output dimensions and not as a direct shortcut to social class.
- **核心要点**：
  - 文昌贵应与整体格局、用神与清浊程度一并考察，不能单凭口诀即许以高科。
  - 在系统中，可将文昌贵视为「学习与文书能力」的加权因子，用于解释命主在知识与表达方面的优势。
 
- **详细解说**：
  1) 按照日主与歌诀，对每一命局标注文昌贵所在的干支位置（年、月、日、时中），形成 `wenchang_positions`；
   2) 结合学堂、词馆、印绶等结构，计算「学习投入」「知识掌握」与「文书输出」相关的综合评分，将文昌贵主要作用于这些维度，而非直接映射为考试成绩；
   3) 在现实数据中，将文昌特征与教育年限、阅读习惯、写作频率等变量做相关性分析，以校准文昌因子的权重；
   4) 在解释层，把文昌贵更多描述为「学习与文书的天赋倾向与兴趣点」，并强调仍需后天努力与环境配合。

 - 反例与边界：
   - 不宜因命盘有文昌贵就断定必然「高考状元」「科名显赫」，现代教育与考试体系远比古代复杂，命盘仅提供潜质与倾向；
   - 若文昌落在忌神之地、被重煞刑冲或落空亡，其正向作用应显著折减，甚至可能表现为「想太多、动手太少」的倾向；
   - 工程上若把文昌贵直接当作高收入或高社会阶层的强预测因子，容易造成偏见，应通过实际样本验证其效应大小；
   - 反向误区是完全舍弃文昌特征，使模型无法刻画「学习型」「文书型」人格与发展路径的差异。

 - 小例（示意）：
   - 某命局文昌落在日支学堂附近，又与印星、食神形成良性结构，现实中表现为「自学能力强、善于通过笔头总结」，系统可在解释中强调其适合研究、写作、咨询等需要大量文书与知识整合的工作；
  - 另一命局虽有文昌，却落在忌神宫位且被煞星冲破，现实中读书兴趣不稳定、多有中断，系统则将文昌视为潜在兴趣点，而不据此作过度乐观的学历预测。"""
    normalized_text_zh: str = """"""
    subject: str = "文昌贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_53', 'bazi_semantic', 'bazi_state_marker_15', 'bazi_semantic', 'bazi_function_factor_5', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_文昌贵_001_L1",
    )
    version: str = "1.0.0"
