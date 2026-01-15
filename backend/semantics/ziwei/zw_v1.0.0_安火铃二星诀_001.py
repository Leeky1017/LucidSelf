"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654134
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
    semantic_id="zw_v1.0.0_安火铃二星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安火铃二星诀(SemanticEntry):
    """
    **主题**：论生年支安火星铃星。

#### 原文（断句）：

寅午戌人丑卯方，申子辰人寅戌场，巳酉丑人卯戌位，亥卯未人酉戌房。

#### 分字分词释义：

- **寅午戌人**：生年地支为寅、午...
    """
    
    original_text: str = """**主题**：论生年支安火星铃星。

#### 原文（断句）：

寅午戌人丑卯方，申子辰人寅戌场，巳酉丑人卯戌位，亥卯未人酉戌房。

#### 分字分词释义：

- **寅午戌人**：生年地支为寅、午、戌的人，属于火局三合。
- **丑卯方**：火星在卯宫，铃星在丑宫。
- **申子辰人**：生年地支为申、子、辰的人，属于水局三合。
- **寅戌场**：火星在寅宫，铃星在戌宫。
- **巳酉丑人**：生年地支为巳、酉、丑的人，属于金局三合。
- **卯戌位**：火星在卯宫，铃星在戌宫。
- **亥卯未人**：生年地支为亥、卯、未的人，属于木局三合。
- **酉戌房**：火星在酉宫，铃星在戌宫。

#### 安星规则：

| 生年支 | 火星 | 铃星 |
|--------|------|------|
| 寅午戌 | 卯 | 丑 |
| 申子辰 | 寅 | 戌 |
| 巳酉丑 | 卯 | 戌 |
| 亥卯未 | 酉 | 戌 |

#### 规范化释义（primary_lang_explained）：

寅午戌人丑卯方申子辰人寅戌场巳酉丑人卯戌位亥卯未人酉戌房。

#### 完整对等诠释（secondary_lang_full·12火铃）：

The Huoxing–Lingxing rule derives a fiery malefic pair from the birth‑year branch. Using the same four triad groups as Tianma, it assigns a fixed Fire Star and Bell Star to each: Yin–Wu–Xu years place Huoxing in Mao and Lingxing in Chou; Shen–Zi–Chen years place Huoxing in Yin and Lingxing in Xu; Si–You–Chou years again use Mao and Xu; Hai–Mao–Wei years place Huoxing in You and Lingxing in Xu. The two stars thus trace a patterned circuit through the zodiac, always tied back to the native’s year branch and to the idea of volatile fire.

Huoxing expresses the sudden, explosive side of fire—impulsiveness, flare‑ups, accidents and inflammatory crises—while Lingxing expresses smouldering, hidden heat that eats away through worry, resentment or chronic strain. When they flank the Life Palace or important houses, they create a “fire‑malefic” configuration that raises the emotional temperature of events: conflicts become sharper, reactions quicker and tolerance lower. Combined with certain main stars such as Tanlang they can also indicate bold risk‑taking that brings dramatic gains, but only when the rest of the chart supports such volatility; otherwise they warn of burns, arguments and situations that run too hot to handle.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 火星 | Huoxing | 主暴烈急躁的火煞星 | Fire-malefic violence impulsiveness | star_huoxing | existing |
| 铃星 | Lingxing | 主阴火暗耗的闷煞星 | Smoldering-malefic covert consumption | star_lingxing | existing |
| 火煞格局 | Fire-Malefic Pattern | 火铃形成的火性煞格 | Fire-nature malefic formation | pattern_huoshageju | new_candidate |
| 贪火相逢 | Tanlang-Fire Convergence | 贪狼遇火铃的突发财格 | Sudden-prosperity Tanlang-fire | combo_tanhuoxiangfeng | existing |
| 突发横财 | Windfall Wealth | 突然意外的财富 | Sudden unexpected wealth | concept_tufahengcai | new_candidate |

#### 详细解说：

火星与铃星是紫微斗数六煞星中的两颗火性煞星，依据生年地支的三合局来定位。它们代表急躁、暴烈、冲动等火性能量。

**算法原理**：
- 十二地支分为四组三合局，每组对应固定的火星、铃星位置
- 火星与铃星的定位独立于禄存，直接依据年支
- 铃星多数落在戌宫（四组中有三组），体现戌宫为火库的象征

**火星与铃星的性质区别**：
- **火星**：急煞，主暴烈、急躁、冲动、爆发性事件。性质外显，如明火般炽烈。
- **铃星**：闷煞，主阴火、暗耗、焦虑、慢性消耗。性质内敛，如闷烧般持续。

**重要格局**：
- **火铃夹命**：火星、铃星分别在命宫前后，主性格急躁、多灾多难
- **贪火相逢**：贪狼与火星或铃星同宫，主突发横财，是横发格局
- **火铃入庙**：在庙旺地可转化为威武、果断、行动力

**现代应用**：
火星可延伸为急性事件、爆发冲突、激烈竞争；铃星可延伸为焦虑、压力、慢性消耗。

#### 校勘与字词辨析（bilingual）：

- **"火星"**：又称"荧惑"，五行属火，主急躁暴烈。英文："Huoxing, Mars star, governing impulsiveness"。
- **"铃星"**：又称"孤辰"，五行属火但性阴，主阴火暗耗。英文："Lingxing, Bell star, governing covert fire consumption"。
- **"方/场/位/房"**：均为"位置"之意，押韵用词。英文："all mean 'position', used for rhyming"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："寅午戌人火居卯，申子辰人火在寅，巳酉丑人火卯位，亥卯未人火酉临。"此为火星单独的记忆口诀。
- **贪火横发**：古人云"贪狼遇火铃，主横发之财"，形容贪狼与火铃同宫时突然发迹的特点。
- **现代应用**：火铃在现代可理解为压力、急躁情绪、突发事件。贪火格局可延伸为投机成功、意外之财、冒险获利等。"""
    normalized_text_zh: str = """"""
    subject: str = "安火铃二星诀"
    factor_refs: list = ['source_ref', 'rel_huoling_001', 'algo_huolingdingwei', 'rel_huoling_002', 'algo_huolingdingwei', 'rel_huoling_003', 'star_huoxing', 'evi_huoling_001', 'star_huoxing', 'rule_huoling_yinwuxu', 'evi_huoling_002', 'star_lingxing', 'rule_huoling_shenzichen', 'concept_fire_malefic', 'concept_smolder_malefic']
    
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
        l1_anchor="zw_v1.0.0_安火铃二星诀_001_L1",
    )
    version: str = "1.0.0"
