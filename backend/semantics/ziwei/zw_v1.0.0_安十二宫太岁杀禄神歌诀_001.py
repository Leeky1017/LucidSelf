"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654182
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
    semantic_id="zw_v1.0.0_安十二宫太岁杀禄神歌诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安十二宫太岁杀禄神歌诀(SemanticEntry):
    """
    **主题**：流年十二神煞（博士十二神）。

#### 原文（断句）：

博士力士青龙续，小耗将军及奏书。蜚廉喜神病符录，大耗伏兵至官府。

#### 分字分词释义：

- **博士**：十二神煞之首...
    """
    
    original_text: str = """**主题**：流年十二神煞（博士十二神）。

#### 原文（断句）：

博士力士青龙续，小耗将军及奏书。蜚廉喜神病符录，大耗伏兵至官府。

#### 分字分词释义：

- **博士**：十二神煞之首，主聪明、学习、进修。
- **力士**：主权力、力量、行动力。
- **青龙**：主喜气、贵人、吉祥之事。
- **小耗**：主小破财、小损失。
- **将军**：主威武、争斗、行动。
- **奏书**：主文书、合同、官方文件。
- **蜚廉**：主孤独、奔波、变动。
- **喜神**：主喜庆、好事、吉利。
- **病符**：主疾病、健康问题。
- **大耗**：主大破财、重大损失。
- **伏兵**：主暗害、小人、潜在危险。
- **官府**：主官讼、法律纠纷、与官方打交道。

#### 十二神煞顺序：

1. 博士（聪明）
2. 力士（权力）
3. 青龙（喜气）
4. 小耗（破财）
5. 将军（威武）
6. 奏书（文书）
7. 蜚廉（孤独）
8. 喜神（喜庆）
9. 病符（疾病）
10. 大耗（大破财）
11. 伏兵（暗害）
12. 官府（官讼）

#### 安星规则：

- 阳男阴女：从禄存顺数
- 阴男阳女：从禄存逆数

#### 规范化释义（primary_lang_explained）：

太岁十二神是一组沿着十二宫循环运行的流年辅神，从“博士”到“官府”构成一个从学习成长、取得权势，到喜庆、破财、疾病、官非的完整年运光谱。排盘时以禄存宫为起点，按命主性别阴阳决定顺逆行，将十二个神煞依次落入各宫，形成当年“聪明用力、喜事破耗、文书是非”等不同主题的流年焦点。

在传统实务中，博士、青龙、喜神多被视为吉神，适合读书进修、求职考试、办喜事；小耗、大耗、病符、官府则偏凶，提示破财、疾病与官非压力；力士、将军、奏书、蜚廉、伏兵居于中间，视全盘吉凶与所落宫位而定。太岁十二神并不单独决定吉凶，而是给出当年在哪些宫位“事多”，哪些议题需要多用心经营的指示。

#### 完整对等诠释（secondary_lang_full·16太岁杀禄神）：

The Twelve Annual Auxiliaries form a circulating belt of minor spirits that colour each year’s themes rather than rewriting the whole chart. Starting from the Lu Cun palace as the anchor, the sequence Doctor, Strongman, Azure Dragon, Minor Loss, General, Petition, Feilian, Joy Spirit, Sickness Talisman, Major Loss, Ambush, and Official Bureau is distributed around the twelve houses by counting either forward or backward according to the native’s gender polarity. Wherever they fall, they highlight where attention, activity and disruption are likely to cluster in that year.

In practice, Doctor, Azure Dragon and Joy Spirit function as supportive markers for study, exams, applications and celebrations. Minor Loss, Major Loss, Sickness Talisman and Official Bureau point to leakages of money, health burdens and legal or bureaucratic entanglements. Strongman, General, Petition, Feilian and Ambush sit in between, becoming helpful or troublesome depending on the natal house and other stars they mix with. Annual Auxiliaries therefore act like a secondary weather map laid over the natal chart, showing which life areas will feel more intelligent, pressured, joyful, depleted or embattled without overturning the base structure of fate.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 太岁十二神煞 | Twelve Annual Auxiliaries | 以禄存为起点流年辅神 | Yearly auxiliaries from Lu Cun | system_taishui12shensha | existing |
| 禄存 | Lu Cun | 年运安星算法的基准星 | Anchor star for annual placements | star_lucun | existing |
| 吉神 | Auspicious Auxiliaries | 博士青龙喜神主吉庆 | Doctor Azure-Dragon Joy-Spirit | group_jishen | new_candidate |
| 凶煞 | Malefic Auxiliaries | 小耗大耗病符官府主凶 | Minor-Major-Loss Sickness Official | group_xiongsha | new_candidate |
| 阴阳顺逆安星 | Yin-Yang Directed Placement | 依性别阴阳决定顺逆 | Forward/backward by gender polarity | algo_yinyangshuninianxing | existing |

#### 详细解说：

太岁十二神煞是紫微斗数流年推断的重要辅助工具，它们以禄存为基准点，依据命主的阴阳属性决定顺逆方向，将十二种不同性质的神煞分布到十二宫中。

**算法原理**：
- 阳年生男、阴年生女（阳男阴女）：从禄存宫顺时针排布
- 阴年生男、阳年生女（阴男阳女）：从禄存宫逆时针排布
- 十二神煞按固定顺序依次安放

**十二神煞的吉凶分类**：
- **吉神**：博士（学习进修）、青龙（贵人喜气）、喜神（喜庆吉利）
- **凶煞**：小耗（小破财）、大耗（大损失）、病符（疾病）、官府（官讼）
- **中性**：力士、将军、奏书、蜚廉、伏兵（视配合而定）

**实际应用**：
太岁十二神煞主要用于流年推断，看某一年中哪些宫位会比较"热闹"。博士入命主学业进修，青龙入财主财运亨通，病符入疾厄需注意健康，官府入迁移需小心法律纠纷等。

#### 校勘与字词辨析（bilingual）：

- **"博士"**：此处非学位名称，而是流年神煞名，主聪明智慧。英文："Doctor auxiliary, indicating intelligence and learning"。
- **"蜚廉"**：又作"飞廉"，主孤独奔波。英文："Feilian, governing loneliness and restless movement"。
- **"官府"**：此处指与官方机构打交道，包括官讼、税务、法律等。英文："Official Bureau, indicating dealings with authorities"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："博士力士青龙续，小耗将军及奏书，蜚廉喜神病符录，大耗伏兵至官府。"此为十二神煞的完整记忆口诀。
- **吉凶分用**：古人云"博士青龙喜神至，诸事顺遂多吉利；小耗大耗病符临，破财疾病须防避。"
- **现代应用**：太岁十二神煞在现代可用于规划一年中的重点事项。博士临宫适合进修考试，喜神临宫适合办喜事，病符临宫需注意健康检查等。"""
    normalized_text_zh: str = """"""
    subject: str = "安十二宫太岁杀禄神歌诀"
    factor_refs: list = ['source_ref', 'rel_taishui_001', 'star_lucun', 'rel_taishui_002', 'algo_yinyangshuninianxing', 'rel_taishui_003', 'group_jishen', 'evi_taishui_001', 'system_taishui12shensha', 'rule_taishui_sequence', 'evi_taishui_002', 'algo_yinyangshuninianxing', 'rule_taishui_yinyang', 'concept_annual_auxiliary', 'concept_fortune_indicator']
    
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
        l1_anchor="zw_v1.0.0_安十二宫太岁杀禄神歌诀_001_L1",
    )
    version: str = "1.0.0"
