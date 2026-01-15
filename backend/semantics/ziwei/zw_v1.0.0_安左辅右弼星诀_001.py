"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654075
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
    semantic_id="zw_v1.0.0_安左辅右弼星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安左辅右弼星诀(SemanticEntry):
    """
    **主题**：论本生月安左辅右弼。

#### 原文（断句）：

左辅正月起于辰，顺逢生月是贵方。右弼正月宫寻戌，逆至生月便调停。

#### 分字分词释义：

- **左辅**：六吉星之一，主正面辅...
    """
    
    original_text: str = """**主题**：论本生月安左辅右弼。

#### 原文（断句）：

左辅正月起于辰，顺逢生月是贵方。右弼正月宫寻戌，逆至生月便调停。

#### 分字分词释义：

- **左辅**：六吉星之一，主正面辅佐、阳贵助力。
- **正月起于辰**：以正月为起点，从辰宫开始计算。
- **顺逢生月**：顺时针数到命主出生的月份。
- **贵方**：贵人所在的方位。
- **右弼**：六吉星之一，主侧面协调、阴贵助力。
- **宫寻戌**：从戌宫开始计算。
- **逆至生月**：逆时针数到命主出生的月份。
- **调停**：协调安排，指右弼的安放位置确定。

#### 规范化释义（primary_lang_explained）：

左辅正月起于辰顺逢生月是贵方。右弼正月宫寻戌逆至生月便调停。

#### 安星规则：

**左辅**：
- 正月起点：辰宫
- 方向：顺时针
- 正月辰、二月巳、三月午...

**右弼**：
- 正月起点：戌宫
- 方向：逆时针
- 正月戌、二月酉、三月申...

#### 完整对等诠释（secondary_lang_full·7左辅右弼）：

The Zuofu–Youbi placement rule assigns an assisting pair of stars according to the birth month. Zuofu is found by treating the Chen palace as the seat of the first lunar month and counting clockwise to the native’s month; Youbi is found by treating the Xu palace as that same first‑month seat and counting counter‑clockwise. The two stars thus stand on opposite sides of the birth‑month axis, echoing the opposition between Chen and Xu and creating a balanced frame of support.

In symbolism, Zuofu represents bright, front‑stage help from superiors and allies—obvious recommendations, visible protection and people who stand beside the native. Youbi represents quieter, back‑stage help—those who coordinate, mediate and smooth over difficulties out of sight. As part of the six auspicious stars they describe how assistance enters the life: whether it is direct or indirect, loud or discreet. When they flank Ziwei or converge on the Life Palace, charts often show repeated experiences of “ruler and ministers celebrating together”, where the native is drawn close to power and receives substantial backing at key moments.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 左辅 | Zuofu | 主正面辅佐的昼贵星 | Daylight-nobility frontal assistance | star_zuofu | existing |
| 右弼 | Youbi | 主侧面协调的夜贵星 | Night-nobility lateral coordination | star_youbi | existing |
| 辅弼夹紫微 | Assistants Flanking Ziwei | 左右辅夹紫微君臣庆会格 | Monarch-ministers celebration | combo_fubijiaziwei | existing |
| 贵人相助 | Noble-Person Support | 贵人辅佐扶持之力 | Assistance from noble persons | concept_guirenxiangzhu | new_candidate |

#### 详细解说：

左辅右弼是六吉星中专主贵人辅佐的一对星曜。它们依据生月安放，体现了月份对命盘人际助力层面的影响。

**算法特点**：
- 左辅与右弼的起点分别在辰宫与戌宫，恰好形成对冲关系
- 左辅顺行、右弼逆行，使得两星总是以生月为轴呈现对称分布
- 这种对称结构象征"阳贵明助"（左辅）与"阴贵暗助"（右弼）的互补

**左辅与右弼的区别**：
- **左辅**：主阳贵、昼贵，代表正面直接的帮助，如上司提拔、贵人推荐、明确的支持与背书
- **右弼**：主阴贵、夜贵，代表侧面间接的协助，如幕后协调、暗中相助、不露痕迹的支持

**重要格局**：
- **辅弼夹紫微**：左辅右弼分别在紫微前后宫位，形成"君臣庆会"格局，主得贵人鼎力相助
- **辅弼入命**：左辅或右弼入命宫，主一生多得贵人相助
- **辅弼同宫**：二星同宫（极少见），主贵人缘极佳

#### 校勘与字词辨析（bilingual）：

- **"贵方"**：贵人所在的方位，引申为有利的位置。英文："direction of noble assistance"。
- **"调停"**：此处非调解争端之意，而是"安排妥当"的意思。英文："properly arranged" 或 "settled in position"。
- **"辰戌对冲"**：辰宫与戌宫相对，形成180度关系。英文："Chen-Xu opposition, 180-degree axis"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："左辅辰宫顺行详，右弼戌上逆路长，一主明助一暗助，命逢辅弼贵人帮。"此口诀帮助学习者记忆辅弼的安放规则与主象区别。
- **君臣庆会**：辅弼夹紫微的格局被称为"君臣庆会"，象征帝王得良臣辅佐，在现代可理解为核心人物得到得力团队的支持。
- **现代应用**：现代解读中，左辅可延伸为直接上司的提拔、明确的推荐信、公开的背书；右弼可延伸为幕后协调、内部关系疏通、不动声色的人脉支持。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j3_043]` `[trigger: 辅弼定位算法]` `[factor_trigger: algo_fubidingwei]` `[role: 主干]` 辅弼定位算法为根据生月安放左辅右弼的算法。 → 《安左辅右弼星诀》
- `[ns_zwds_j3_044]` `[trigger: 左辅顺行]` `[factor_trigger: algo_zuofushunxing]` `[role: 主干]` 左辅顺行为从辰宫起正月顺数至生月的算法。 → 《安左辅右弼星诀》
- `[ns_zwds_j3_045]` `[trigger: 右弼逆行]` `[factor_trigger: algo_youbinixing]` `[role: 主干]` 右弼逆行为从戌宫起正月逆数至生月的算法。 → 《安左辅右弼星诀》
- `[ns_zwds_j3_046]` `[trigger: 君臣庆会格]` `[factor_trigger: combo_fubijiaziwei]` `[role: 条件分支]` 君臣庆会格为辅弼夹紫微的极贵格局。 → 《安左辅右弼星诀》"辅弼夹紫微"
- `[ns_zwds_j3_047]` `[trigger: 辅弼同宫]` `[factor_trigger: combo_fubi_tonggong]` `[role: 条件分支]` 辅弼同宫为左辅右弼同在一宫的配置，主贵人缘极佳。 → 《安左辅右弼星诀》
- `[ns_zwds_j3_048]` `[trigger: 明助暗助]` `[factor_trigger: trait_mingzhu_anzhu]` `[role: 主干]` 明助暗助为左辅主明助、右弼主暗助的区别。 → 《安左辅右弼星诀》"一主明助一暗助""""
    normalized_text_zh: str = """"""
    subject: str = "安左辅右弼星诀"
    factor_refs: list = ['source_ref', 'rel_fubi_001', 'algo_fubidingwei', 'rel_fubi_002', 'algo_fubidingwei', 'rel_fubi_003', 'star_zuofu', 'evi_fubi_001', 'star_zuofu', 'rule_zuofu_dingwei', 'evi_fubi_002', 'star_youbi', 'rule_youbi_dingwei', 'concept_assistant_star', 'concept_daylight_noble', 'concept_night_noble']
    
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
        l1_anchor="zw_v1.0.0_安左辅右弼星诀_001_L1",
    )
    version: str = "1.0.0"
