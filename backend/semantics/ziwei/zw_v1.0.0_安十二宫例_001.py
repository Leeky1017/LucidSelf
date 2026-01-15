"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654019
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
    semantic_id="zw_v1.0.0_安十二宫例_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安十二宫例(SemanticEntry):
    """
    **主题**：十二宫的排列顺序与逆数规则。

#### 原文（断句）：

男女俱从逆转，切记莫顺去。一命宫，二兄弟，三妻妾，四子女，五财帛，六疾厄，七迁移，八奴仆，九官禄，十田宅，十一福德，十二父母。...
    """
    
    original_text: str = """**主题**：十二宫的排列顺序与逆数规则。

#### 原文（断句）：

男女俱从逆转，切记莫顺去。一命宫，二兄弟，三妻妾，四子女，五财帛，六疾厄，七迁移，八奴仆，九官禄，十田宅，十一福德，十二父母。

#### 分字分词释义：

- **俱从逆转**：都按照逆时针方向排列。
- **切记莫顺去**：特别强调不能顺时针排列，这是容易犯错的地方。
- **命宫**：第一宫，代表自我本质与一生命运主线。
- **兄弟宫**：第二宫，代表兄弟姐妹缘分与手足关系。
- **妻妾宫**：第三宫，代表婚姻配偶与情感关系。
- **子女宫**：第四宫，代表子嗣传承与亲子关系。
- **财帛宫**：第五宫，代表钱财收入与理财能力。
- **疾厄宫**：第六宫，代表健康状况与疾病倾向。
- **迁移宫**：第七宫，代表外出发展与人际环境。
- **奴仆宫**：第八宫，代表下属助力与交友关系。
- **官禄宫**：第九宫，代表事业发展与社会地位。
- **田宅宫**：第十宫，代表不动产与家业根基。
- **福德宫**：第十一宫，代表精神享受与内心福气。
- **父母宫**：第十二宫，代表父母缘分与相貌遗传。

#### 规范化释义（primary_lang_explained）：

男女俱从逆转切记莫顺去。一命寫二兄弟三妻妾四子女五财帛六疾厄七迁移八奴仆九官禄十田宅十一福德十二父母。

#### 核心要点：

- **逆数排列**：十二宫从命宫开始逆时针排列
- **宫位顺序**：命→兄弟→夫妻→子女→财帛→疾厄→迁移→奴仆→官禄→田宅→福德→父母

#### 十二宫列表：

1. 命宫（命）
2. 兄弟宫（兄弟姊妹）
3. 夫妻宫（妻妾、配偶）
4. 子女宫（儿女）
5. 财帛宫（钱财）
6. 疾厄宫（疾病）
7. 迁移宫（外出）
8. 奴仆宫（交友、下属）
9. 官禄宫（事业）
10. 田宅宫（不动产）
11. 福德宫（精神享受）
12. 父母宫（相貌、长辈）

#### 完整对等诠释（secondary_lang_full·2安十二宫例）：

Twelve-Palace Arrangement describes how Ziwei Doushu maps the whole of life into twelve stable sectors. Starting from the Life Palace, all other palaces are laid out counter-clockwise in a fixed sequence: Siblings, Spouse, Children, Wealth, Illness, Travel, Servants, Career, Property, Fortune, and Parents. The verse insists that both male and female charts must follow this reverse order, never clockwise, so that once the Life Palace is known, every other house is determined purely by relative position.

In practice, this layout becomes a topological skeleton for interpretation. Each palace anchors a field of experience—identity, family ties, marriage, descendants, resources, health, movement, helpers and subordinates, vocation, real estate, inner happiness, and ancestry. Because the order never changes, shifting the Life or Body Palace simply rotates which concrete zodiacal house carries which life topic. Reading three-directions and four-cardinal relationships among palaces therefore presupposes complete fluency with this basic counter-clockwise loop.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 十二宫 | Twelve-Palace Scheme | 命盘中对应十二个人生领域的宫位系统 | Palace system twelve life domains | structure_shiergong | existing |
| 逆数排列 | Counter-Clockwise Order | 以命宫为起点逆时针依次排列诸宫 | Counter-clockwise from Life Palace | algo_nishupaiilie | new_candidate |
| 三方四正 | Three-Directions Four-Cardinals | 宫位间对宫与三合六合呼应结构 | Angular trine framework | structure_sanfangsizheng | existing |
| 命宫起点 | Life-Palace Anchor | 以命宫为起点决定其他宫位顺序 | Life Palace as anchor | principle_minggongqidian | new_candidate |

#### 详细解说：

十二宫是紫微斗数的空间框架，将人生划分为十二个领域。这一划分体系源于天干地支与十二地支的对应关系，是中国传统命理学的核心结构。

**逆时针排列的原理**：
紫微斗数采用逆时针排列十二宫，这与天体运行的视觉规律相关（从北方观测天空，星辰呈逆时针方向移动）。原文特别强调"切记莫顺去"，是因为顺时针排列是初学者常犯的错误。

**十二宫的象征意义**：
1. **命宫**：核心自我，一生命运主线
2. **兄弟宫**：手足缘分，平辈关系
3. **夫妻宫**：婚姻情感，合作对象
4. **子女宫**：子嗣传承，创造能力
5. **财帛宫**：钱财收入，理财能力
6. **疾厄宫**：健康状况，身心平衡
7. **迁移宫**：外出发展，人际环境
8. **奴仆宫**：助力支持，团队合作
9. **官禄宫**：事业发展，社会地位
10. **田宅宫**：不动产，家业根基
11. **福德宫**：精神享受，内心福气
12. **父母宫**：原生家庭，相貌遗传

**宫位间的关系**：
- **对宫**：相隔六宫，呈180度对冲关系
- **三方**：相隔四宫，呈120度三合关系
- **四正**：命宫、官禄宫、财帛宫、迁移宫构成的核心关系网

#### 校勘与字词辨析（bilingual）：

- **"俱从逆转"**：所有命盘都采用逆时针排列。英文："all charts follow counter-clockwise arrangement"。
- **"妻妾"**：古代指正妻与妾室，现代统称配偶或伴侣。英文："spouse or partner"。
- **"奴仆"**：古代指仆从，现代理解为下属、助手或合作者。英文："subordinates, assistants or collaborators"。
- **"迁移"**：不仅指地理移动，也包括社会流动与环境变化。英文："travel, relocation and environmental shifts"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："十二宫位定乾坤，逆行排列记分明，命为首位父母尾，六亲人事此中分。"此口诀帮助学习者记忆十二宫的排列顺序。
- **易学溯源**：十二宫与十二地支对应，源于《周易》的时空观念与干支历法体系，是中国传统命理学的基础结构。
- **现代应用**：现代排盘软件自动生成十二宫位，但理解其排列规律对于手工验盘、理解宫位关系仍有重要价值。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j3_011]` `[trigger: 十二宫结构]` `[factor_trigger: structure_shiergong]` `[role: 主干]` 十二宫结构为紫微斗数命盘的基本空间框架。 → 《安十二宫例》
- `[ns_zwds_j3_012]` `[trigger: 逆序排列]` `[factor_trigger: algo_nishupaiilie]` `[role: 主干]` 逆序排列为十二宫逆时针排列的算法。 → 《安十二宫例》"逆行排列"
- `[ns_zwds_j3_013]` `[trigger: 三方四正]` `[factor_trigger: structure_sanfangsizheng]` `[role: 主干]` 三方四正为命宫与对宫、三合宫的结构关系。 → 《安十二宫例》
- `[ns_zwds_j3_014]` `[trigger: 对宫关系]` `[factor_trigger: relation_duigong]` `[role: 主干]` 对宫关系为相隔六宫的180度对冲关系。 → 《安十二宫例》
- `[ns_zwds_j3_015]` `[trigger: 三合关系]` `[factor_trigger: relation_sanhe]` `[role: 主干]` 三合关系为相隔四宫的120度相生关系。 → 《安十二宫例》
- `[ns_zwds_j3_016]` `[trigger: 六合关系]` `[factor_trigger: relation_liuhe]` `[role: 主干]` 六合关系为相邻宫位的相合关系。 → 《安十二宫例》
- `[ns_zwds_j3_017]` `[trigger: 兄弟宫定义]` `[factor_trigger: palace_xiongdi]` `[role: 主干]` 兄弟宫为命宫逆数第一宫，主兄弟姐妹。 → 《安十二宫例》
- `[ns_zwds_j3_018]` `[trigger: 夫妻宫定义]` `[factor_trigger: palace_fuqi]` `[role: 主干]` 夫妻宫为命宫逆数第二宫，主配偶婚姻。 → 《安十二宫例》
- `[ns_zwds_j3_019]` `[trigger: 子女宫定义]` `[factor_trigger: palace_zinv]` `[role: 主干]` 子女宫为命宫逆数第三宫，主子女后代。 → 《安十二宫例》
- `[ns_zwds_j3_020]` `[trigger: 财帛宫定义]` `[factor_trigger: palace_caibo]` `[role: 主干]` 财帛宫为命宫逆数第四宫，主财运收入。 → 《安十二宫例》
- `[ns_zwds_j3_021]` `[trigger: 疾厄宫定义]` `[factor_trigger: palace_jie]` `[role: 主干]` 疾厄宫为命宫逆数第五宫，主健康疾病。 → 《安十二宫例》
- `[ns_zwds_j3_022]` `[trigger: 迁移宫定义]` `[factor_trigger: palace_qianyi]` `[role: 主干]` 迁移宫为命宫对宫，主外出社交。 → 《安十二宫例》
- `[ns_zwds_j3_023]` `[trigger: 奴仆宫定义]` `[factor_trigger: palace_nupu]` `[role: 主干]` 奴仆宫为迁移宫逆数第一宫，主下属朋友。 → 《安十二宫例》
- `[ns_zwds_j3_024]` `[trigger: 官禄宫定义]` `[factor_trigger: palace_guanlu]` `[role: 主干]` 官禄宫为迁移宫逆数第二宫，主事业地位。 → 《安十二宫例》
- `[ns_zwds_j3_025]` `[trigger: 田宅宫定义]` `[factor_trigger: palace_tianzhai]` `[role: 主干]` 田宅宫为迁移宫逆数第三宫，主房产家庭。 → 《安十二宫例》
- `[ns_zwds_j3_026]` `[trigger: 福德宫定义]` `[factor_trigger: palace_fude]` `[role: 主干]` 福德宫为迁移宫逆数第四宫，主精神享受。 → 《安十二宫例》
- `[ns_zwds_j3_027]` `[trigger: 父母宫定义]` `[factor_trigger: palace_fumu]` `[role: 主干]` 父母宫为迁移宫逆数第五宫，主原生家庭。 → 《安十二宫例》"""
    normalized_text_zh: str = """"""
    subject: str = "安十二宫例"
    factor_refs: list = ['source_ref', 'rel_12gong_001', 'palace_ming', 'rel_12gong_002', 'algo_nishupaiilie', 'rel_12gong_003', 'structure_sanfangsizheng', 'evi_12gong_001', 'algo_nishupaiilie', 'rule_nishu_pailie', 'evi_12gong_002', 'structure_shiergong', 'rule_12gong_tixi', 'concept_12palace', 'concept_angular']
    
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
        l1_anchor="zw_v1.0.0_安十二宫例_001_L1",
    )
    version: str = "1.0.0"
