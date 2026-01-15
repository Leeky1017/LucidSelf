"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654283
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
    semantic_id="zw_v1.0.0_安斗君诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安斗君诀(SemanticEntry):
    """
    **主题**：月将星（流月定位），用于流年流月推算。

#### 原文（断句）：

年太岁宫起正月，逆至本生月，又从本生月起子，顺数至本生时安斗君。

#### 分字分词释义：

- **斗君**：月...
    """
    
    original_text: str = """**主题**：月将星（流月定位），用于流年流月推算。

#### 原文（断句）：

年太岁宫起正月，逆至本生月，又从本生月起子，顺数至本生时安斗君。

#### 分字分词释义：

- **斗君**：月将星，流月定位的起点。
- **年太岁宫**：当年太岁所在的宫位。
- **起正月**：将该宫视为正月起点。
- **逆至本生月**：逆时针数到命主出生月份。
- **从本生月起子**：以生月宫位为子时起点。
- **顺数至本生时**：顺时针数到命主出生时辰。
- **安斗君**：在该宫位安放斗君。

#### 安星规则：

**步骤1**：从流年太岁宫起正月，逆数至生月  
**步骤2**：从生月宫起子时，顺数至生时，该宫为斗君

#### 作用：
- 斗君为流月起点
- 从斗君顺数十二宫为流月位置

#### 规范化释义（primary_lang_explained）：

斗君是用来定位流月起点的月将星，它把“这一年”的时间进一步切分成十二个流月节奏。安星法先以流年太岁宫为正月，从太岁宫逆数到本生月，找到“年与月交汇”的位置；再从该宫起子时，顺数到本生时，所得之宫即为斗君所在。由斗君起算十二宫，便得到当年正月到腊月各月的流月落宫，好比在星盘上画出一年中能量在十二宫之间依次巡行的路线图。

在实务上，斗君本身并不带强烈吉凶，而是作为时间游标，将全年运势细化到每个月与每个宫位：当流月斗君走到财帛宫，财务议题自然更活跃；走到官禄宫，事业、职务与工作压力更显著；走到疾厄、父母等宫，则提示那几个月在健康与家人层面需要特别留心。配合大限、小限与各类流年安星，可以构成一套“年—月—宫位”的多层时序框架，让占验者更清楚哪段时间在哪个生活领域最容易起波澜。

#### 完整对等诠释（secondary_lang_full·26斗君）：

Doujun functions as the monthly pointer star that refines the annual picture into a twelve-step rhythm. Its placement procedure is twofold: first, treat the year’s Tai Sui palace as the seat of the first lunar month and count backward to the native’s birth month; second, from that month’s palace start at Zi hour and count forward to the birth hour. The house reached by this second count is Doujun, the anchor from which the twelve monthly positions for the year are traced in order.

Interpreters use Doujun less as a source of independent meaning and more as a moving marker that slides the year’s emphasis around the chart. Months in which Doujun occupies the Wealth palace highlight income, expenses and financial decisions; when it travels through the Career palace, work, status and public responsibility come to the foreground; in the Health or Parents palaces, bodily condition and family matters demand extra attention. Combined with major-period rulers and other annual stars, Doujun helps build a layered calendar of when and where life is busiest, turning the static natal map into a living cycle of shifting focus.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 斗君 | Doujun | 太岁生月生时综合定位流月起点 | Tai Sui month hour monthly pivot | star_doujun | existing |
| 先逆后顺算法 | Reverse-Then-Forward | 太岁逆至生月再顺至生时 | Backward month forward hour | algo_xiannihoushunn | new_candidate |
| 流月巡行 | Monthly Circuit | 斗君起算十二宫映射月序 | Doujun forward twelve monthly | concept_liuyuexunxing | new_candidate |
| 年月同参 | Year-Month Composite | 流年大限斗君叠加判断 | Annual period monthly combined | principle_nianyuetongcan | new_candidate |

#### 详细解说：

斗君是紫微斗数流月推断的核心工具，它将全年运势细化到每个月份，是"年—月—宫位"多层时序框架的关键节点。

**算法原理**：
- **第一步**：从流年太岁宫起正月，逆时针数到命主出生月份
- **第二步**：从第一步得到的宫位起子时，顺时针数到命主出生时辰
- 最终到达的宫位即为斗君所在

**斗君的功能意义**：
- 斗君本身不带强烈吉凶，而是时间游标
- 从斗君顺数十二宫，即为当年正月到腊月的流月位置
- 可将全年运势精细化到每个月的每个宫位

**流月推算应用**：
- 流月走财帛宫：该月财务议题活跃
- 流月走官禄宫：该月事业压力明显
- 流月走疾厄宫：该月需注意健康问题

**现代应用**：
斗君可用于月度规划与时机选择。结合大限、流年等信息，可以精确判断某个月在哪个领域最需要关注。

#### 校勘与字词辨析（bilingual）：

- **"斗君"**：北斗之君，主流月定位。英文："Doujun, Monthly Pivot Star, governing monthly positions"。
- **"先逆后顺"**：斗君定位的独特算法——先逆后顺。英文："reverse-then-forward method"。
- **"流月巡行"**：从斗君起算的月度宫位循环。英文："monthly circuit of houses"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："太岁起正逆生月，生月起子顺生时，斗君既定流月推，十二宫位月运知。"此诀概括了斗君的定位方法与流月推算。
- **年月同参**：古人云"斗君定位，流月可推，年月同参，吉凶可知"，强调斗君在时序推断中的重要性。
- **现代应用**：斗君在现代可用于月度运势规划。通过流月走宫分析，可以提前规划每月的重点事项与注意领域。"""
    normalized_text_zh: str = """"""
    subject: str = "安斗君诀"
    factor_refs: list = ['source_ref', 'rel_doujun_001', 'system_liuniantaisui', 'rel_doujun_002', 'principle_shengyuemaodian', 'rel_doujun_003', 'star_doujun', 'evi_doujun_001', 'star_doujun', 'rule_doujun_step1', 'evi_doujun_002', 'star_doujun', 'rule_doujun_step2', 'concept_monthly_pivot']
    
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
        l1_anchor="zw_v1.0.0_安斗君诀_001_L1",
    )
    version: str = "1.0.0"
