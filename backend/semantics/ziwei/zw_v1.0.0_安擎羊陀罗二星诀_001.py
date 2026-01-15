"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654122
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
    semantic_id="zw_v1.0.0_安擎羊陀罗二星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安擎羊陀罗二星诀(SemanticEntry):
    """
    **主题**：禄前擎羊禄后陀罗。

#### 原文（断句）：

禄前擎羊后陀罗，夹限逢凶祸患多。岁限逢之多不利，人生遇此莫蹉跴。

#### 分字分词释义：

- **禄前擎羊**：擎羊位于禄存的前一...
    """
    
    original_text: str = """**主题**：禄前擎羊禄后陀罗。

#### 原文（断句）：

禄前擎羊后陀罗，夹限逢凶祸患多。岁限逢之多不利，人生遇此莫蹉跴。

#### 分字分词释义：

- **禄前擎羊**：擎羊位于禄存的前一个宫位（顺时针方向）。
- **后陀罗**：陀罗位于禄存的后一个宫位（逆时针方向）。
- **夹限逢凶**：当大限或流年被擎羊、陀罗夹制时，容易遇到凶险。
- **祸患多**：灾祸较多，运势不顺。
- **岁限**：流年与大限。
- **蹉跎**：虚度光阴，耽误时机。

#### 规范化释义（primary_lang_explained）：

禄前擎羊后陀罗夹限逢凶祸患多。岁限逢之多不利人生遇此莫蹉跴。

#### 安星规则：

- **擎羊**：禄存前一位（顺时针）
- **陀罗**：禄存后一位（逆时针）

#### 示例：
- 甲生人禄在寅：擎羊在卯，陀罗在丑
- 癸生人禄在子：擎羊在丑，陀罗在亥

#### 完整对等诠释（secondary_lang_full·11擎羊陀罗）：

The Qingyang–Tuoluo rule sets a malefic pair on either side of Lucun. The core instruction is “sheep before, Tuoluo after”: Qingyang is placed one house ahead of Lucun in the clockwise direction, while Tuoluo is placed one house behind it in the counter‑clockwise direction. For example, if a Jia year gives Lucun in Yin, then Qingyang goes to Mao and Tuoluo to Chou; if a Gui year gives Lucun in Zi, Qingyang moves to Chou and Tuoluo to Hai. Whatever Lucun’s position, the two stars always flank it tightly.

Qingyang acts as a hard, cutting influence associated with aggression, accidents, sharp breaks and painful confrontations; Tuoluo acts as a soft but dragging influence linked to delay, entanglement and slow depletion. Together they form the “malefics flanking salary” pattern that tests how one handles pressure around resources and initiatives. When they close in around the Life Palace or key time‑periods, the native may feel surrounded by crises or heavy obligations, especially if other killing stars join them. If well dignified or controlled by benefics, however, the same energy can be channelled into decisive action, surgery, competition or disciplined struggle rather than uncontrolled damage.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 擎羊 | Qingyang | 主刑伤暴戴的刚煞星 | Hard-malefic punishment violence | star_qingyang | existing |
| 陀罗 | Tuoluo | 主阴滞拖延的柔煞星 | Soft-malefic stagnation delay | star_tuoluo | existing |
| 禄前羊禄后陀 | Sheep-Before Tuoluo-After | 擎羊陀罗的定位法则 | Positioning rule Qingyang-Tuoluo | principle_luqianyanghoutuo | existing |
| 夹禄煞星 | Flanking-Salary Malefics | 夹禄存的两颗煞星 | Two malefics flanking Lucun | pattern_jialushaxing | new_candidate |
| 入庙有制 | Temple-With-Control | 煞星入庙受制可化险 | Malefics under control | condition_rumiaoyouzhi | new_candidate |

#### 详细解说：

擎羊与陀罗是紫微斗数六煞星中的两颗，它们的位置完全依据禄存来确定。擎羊在禄存的顺时针方向前一宫，陀罗在禄存的逆时针方向后一宫，形成"夹禄"的格局。

**算法原理**：
- 擎羊与陀罗的位置由禄存决定，先定禄存，后定羊陀
- "禄前羊、禄后陀"是固定规则，不因其他因素改变
- 羊陀与禄存总是相邻，形成"禄被煞夹"的结构

**擎羊与陀罗的性质区别**：
- **擎羊**：刚煞，主刑伤、暴戾、急躁、意外伤害、手术刀光。性质刚烈，来得快去得也快。
- **陀罗**：柔煞，主阴滞、拖延、纠缠、暗耗、慢性问题。性质阴柔，来得慢但持续时间长。

**重要格局**：
- **羊陀夹命**：擎羊、陀罗分别在命宫前后，主一生多阻碍
- **羊陀夹忌**：擎羊、陀罗夹制化忌星，凶上加凶
- **羊陀入庙**：在庙旺地且有吉星制化，可以化险为夷

**现代应用**：
擎羊可延伸为手术、竞争、冲突、果断行动；陀罗可延伸为拖延、缠绕、慢性病、持久战。

#### 校勘与字词辨析（bilingual）：

- **"擎羊"**：又称"羊刃"，是刚烈的煞星。英文："Qingyang, also known as Sheep Blade"。
- **"陀罗"**：意为"缠绕"，是阴柔的煞星。英文："Tuoluo, meaning entanglement"。
- **"蹉跎"**：原文作"蹉跴"，应为"蹉跎"之异体，指虚度时光。英文："to waste time, to miss opportunities"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："禄前擎羊后陀罗，二煞夹禄福消磨，若逢限运行此处，祸患临门奈若何。"此诀警示羊陀夹制的凶险。
- **刚柔对比**：古人以"刀刃"比喻擎羊的锋利，以"绳索"比喻陀罗的缠绕，二者性质截然不同但都是阻碍力量。
- **现代应用**：擎羊在现代可理解为急性问题、手术、竞争冲突；陀罗可理解为慢性病、法律纠纷、人事纠葛等需要时间化解的问题。"""
    normalized_text_zh: str = """"""
    subject: str = "安擎羊陀罗二星诀"
    factor_refs: list = ['source_ref', 'rel_yangtuo_001', 'star_lucun', 'rel_yangtuo_002', 'star_lucun', 'rel_yangtuo_003', 'star_qingyang', 'evi_yangtuo_001', 'star_qingyang', 'rule_qingyang_dingwei', 'evi_yangtuo_002', 'star_tuoluo', 'rule_yangtuo_jiaxian', 'concept_hard_malefic', 'concept_soft_malefic']
    
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
        l1_anchor="zw_v1.0.0_安擎羊陀罗二星诀_001_L1",
    )
    version: str = "1.0.0"
