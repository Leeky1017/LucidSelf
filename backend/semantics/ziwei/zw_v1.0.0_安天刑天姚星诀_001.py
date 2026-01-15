"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654192
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
    semantic_id="zw_v1.0.0_安天刑天姚星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安天刑天姚星诀(SemanticEntry):
    """
    **主题**：论本生月安天刑天姚。

#### 原文（断句）：

天刑星从酉上起，正月顺至本生月安之；天姚从丑上起，正月顺至本生月安之。

#### 分字分词释义：

- **天刑**：杂曜之一，主刑...
    """
    
    original_text: str = """**主题**：论本生月安天刑天姚。

#### 原文（断句）：

天刑星从酉上起，正月顺至本生月安之；天姚从丑上起，正月顺至本生月安之。

#### 分字分词释义：

- **天刑**：杂曜之一，主刑罚、官司、法律纠纷。
- **酉上起**：以酉宫为起点。
- **正月顺**：从正月开始顺时针方向数。
- **本生月安之**：数到命主出生月份的宫位安放此星。
- **天姚**：杂曜之一，主桃花、人缘、情欲魅力。
- **丑上起**：以丑宫为起点。

#### 安星规则：

- **天刑**：正月起酉宫，顺数至生月
- **天姚**：正月起丑宫，顺数至生月

#### 规范化释义（primary_lang_explained）：

天刑与天姚是一对相对而行的杂曜：前者偏向刑罚、是非与制度压力，后者偏向情欲、桃花与社交魅惑。二星都以本生月为锚点——从酉宫起数安天刑，从丑宫起数安天姚——像是在出生月份周围标出一处“法律红线”与一处“情欲磁场”，提醒命主在哪些宫位最容易在官非与情感之间起波澜。

实务上，天刑落入命宫、官禄宫等位置，常见为规则意识强、对公平敏感，也可能卷入官司诉讼或制度性压力；天姚落入夫妻、福德等宫，则多主魅力、人缘、情欲议题被放大。若二星同宫或相互呼应，则“因色惹是非”的概率显著上升，需要在享受魅力与追求公平之间拿捏分寸。安星歌诀只是给出位置算法，真正的吉凶仍需结合整盘星曜与行运强弱来判断。

#### 完整对等诠释（secondary_lang_full·17天刑天姚）：

Tianxing and Tianyao move as a paired set of minor stars: one leans toward law, punishment and institutional pressure, the other toward attraction, romance and social allure. Both are anchored purely by the birth month—Tianxing is counted forward from You to the native’s month, while Tianyao is counted forward from Chou—so that the month of birth marks where a personal “legal boundary” and a “seductive field” are inscribed into the chart. The houses they land in show where the life story repeatedly toggles between discipline and desire.

In practice, Tianxing in the Life or Career palaces often appears in charts of people who feel watched by rules: they may work within legal systems, handle disputes, or simply carry a strong sense of justice while being more exposed to lawsuits and formal complaints. Tianyao in the Spouse or Fortune palaces highlights charm, sensuality and entangling relationships. When the two stars fall together or tightly interact, the risk of trouble arising from romance, scandal or boundary-crossing behaviour increases sharply. The placement rule itself is simple counting, but reading it well means asking whether law clarifies desire, or whether desire keeps dragging someone across the legal and ethical line.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 天刑 | Tianxing | 酉宫起生月主刑罚官非 | From You by birth month punishment | star_tianxing | existing |
| 天姚 | Tianyao | 丑宫起生月主桃花魅力 | From Chou by birth month romance | star_tianyao | existing |
| 刑姚同宫 | Penalty-Peach Conjunction | 天刑天姚同宫因色犯刑 | Tianxing-Tianyao join legal romance | pattern_xingyaotonggong | new_candidate |
| 生月锚点 | Birth-Month Anchor | 以本生月为安星基准 | Using birth month as anchor | principle_shengyuemaodian | existing |

#### 详细解说：

天刑与天姚是紫微斗数杂曜系统中性质相反的一对星曜，天刑主刑罚法律，天姚主桃花魅力，二者都依据生月定位。

**算法原理**：
- 天刑从酉宫起正月，顺时针数到生月安放
- 天姚从丑宫起正月，顺时针数到生月安放
- 二星同为论生月的杂曜，但起点与象征意义完全不同

**天刑与天姚的象征意义**：
- **天刑**：主刑罚、官司、法律纠纷、制度压力。入命主人对规则敏感，可能从事法律相关工作，也可能卷入官司。
- **天姚**：主桃花、人缘、魅力、情欲。入命主人有吸引力，异性缘好，但也可能因情惹祸。

**"刑姚同宫"的特殊含义**：
当天刑与天姚同宫时，形成"因色犯刑"的格局，警示因感情、桃花事件而引发官司、是非的风险。

**现代应用**：
天刑可延伸为法律风险、合规问题、规则意识；天姚可延伸为个人魅力、人际吸引、情感丰富度。

#### 校勘与字词辨析（bilingual）：

- **"天刑"**：刑罚之星，与法律、规则、惩罚相关。英文："Tianxing, Penalty Star"。
- **"天姚"**：桃花之星，与魅力、情欲、人缘相关。英文："Tianyao, Peach-Flower Star"。
- **"酉/丑"**：二星的起始宫位，酉为西方金位，丑为东北土位。英文："You (west metal) and Chou (northeast earth) as starting palaces"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："天刑酉上正月起，天姚丑上正月临，刑主官司姚主色，二星同宫祸非轻。"此诀概括了天刑天姚的定位方法与基本象征。
- **因色犯刑**：古人云"天姚逢天刑，多因色惹是非"，警示桃花与法律纠纷的关联。
- **现代应用**：天刑在现代可用于评估法律风险、合规意识；天姚可用于评估个人魅力指数、情感丰富度。二者同宫时需特别注意职场情感关系的边界。"""
    normalized_text_zh: str = """"""
    subject: str = "安天刑天姚星诀"
    factor_refs: list = ['source_ref', 'rel_xingyao_001', 'principle_shengyuemaodian', 'rel_xingyao_002', 'principle_shengyuemaodian', 'rel_xingyao_003', 'star_tianxing', 'evi_xingyao_001', 'star_tianxing', 'rule_tianxing_dingwei', 'evi_xingyao_002', 'star_tianyao', 'rule_tianyao_dingwei', 'concept_penalty_star', 'concept_peach_star']
    
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
        l1_anchor="zw_v1.0.0_安天刑天姚星诀_001_L1",
    )
    version: str = "1.0.0"
