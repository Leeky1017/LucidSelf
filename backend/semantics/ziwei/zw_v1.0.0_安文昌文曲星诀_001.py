"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654061
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
    semantic_id="zw_v1.0.0_安文昌文曲星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安文昌文曲星诀(SemanticEntry):
    """
    **主题**：论本生时安文昌文曲。

#### 原文（断句）：

子时戌上起文昌，逆到生时是贵乡。文曲数从辰上起，顺数至生时安之。

#### 分字分词释义：

- **子时戌上起**：以子时为起点，...
    """
    
    original_text: str = """**主题**：论本生时安文昌文曲。

#### 原文（断句）：

子时戌上起文昌，逆到生时是贵乡。文曲数从辰上起，顺数至生时安之。

#### 分字分词释义：

- **子时戌上起**：以子时为起点，从戌宫开始计算。
- **逆到生时**：逆时针数到命主出生的时辰。
- **贵乡**：贵人之地，指文昌所在宫位为有利位置。
- **文曲数从辰上起**：文曲从辰宫开始，以子时为起点。
- **顺数**：顺时针方向数。
- **安之**：安放在该宫位。

#### 规范化释义（primary_lang_explained）：

子时戌上起文昌逆到生时是贵乡。文曲数从辰上起顺数至生时安之。

#### 安星规则：

**文昌**：
- 子时起点：戌宫
- 方向：逆时针
- 子时戌、丑时酉、寅时申...

**文曲**：
- 子时起点：辰宫
- 方向：顺时针
- 子时辰、丑时巳、寅时午...

#### 完整对等诠释（secondary_lang_full·6文昌文曲）：

The Wenchang–Wenqu placement rule fixes a paired set of literary stars from the birth hour. Wenchang is obtained by treating the Xu palace as the seat of Zi hour and counting counter‑clockwise to the native’s hour; Wenqu is obtained by treating the Chen palace as the Zi‑hour seat and counting clockwise to that same hour. One star therefore approaches from behind and the other from ahead, so that they always face one another around the time anchor and trace out a symmetrical corridor of learning and expression.

Together they form the literary branch of the six auspicious stars. Wenchang emphasises formal study, exams, written work and success in official channels of knowledge, while Wenqu leans toward artistry, technical refinement and aesthetic communication. When either or both occupy the Life, Fortune or Career palaces, education, writing, languages or design often become central to the life story. Strong support from benefics can coincide with academic honours or recognised expertise; heavy affliction, by contrast, may point to pressure, blocked qualifications or talent that struggles to find the right setting.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 文昌 | Wenchang | 主正途科甲的文星 | Literary star orthodox examination | star_wenchang | existing |
| 文曲 | Wenqu | 主偏才艺术的文星 | Literary star artistic talents | star_wenqu | existing |
| 六吉星 | Six Auspicious Stars | 昌曲辅弼魁钺六颜吉星 | Six benefic stars set | structure_liujixing | existing |
| 贵乡 | Noble Territory | 文昌所在为贵人之位 | Wenchang noble-person location | concept_guixiang | new_candidate |

#### 详细解说：

文昌文曲是紫微斗数六吉星中专主文才与学业的两颗星曜。它们的安放完全依据生时，体现了时辰对命盘文学素养层面的影响。

**算法特点**：
- 文昌与文曲的起点分别在戌宫与辰宫，恰好形成对冲关系
- 文昌逆行、文曲顺行，使得两星总是以生时为轴呈现对称分布
- 这种对称结构象征"正统文教"（文昌）与"偏才艺术"（文曲）的互补

**文昌与文曲的区别**：
- **文昌**：主正途科名，代表正规教育、考试能力、学术资格、官方认可的知识体系
- **文曲**：主偏才艺术，代表才艺技能、审美能力、艺术表达、非正统的专业技术

**现代应用**：
- 文昌入命宫或官禄宫：适合学术研究、教育工作、公务考试
- 文曲入命宫或官禄宫：适合艺术创作、设计工作、技术专业
- 昌曲同宫或夹宫：文采斐然，才华横溢

#### 校勘与字词辨析（bilingual）：

- **"贵乡"**：指文昌所在位置为贵人提携之地。英文："territory of noble assistance"。
- **"逆到"/"顺数"**：分别指逆时针与顺时针计算方向。英文："counter-clockwise counting" / "clockwise counting"。
- **"戌上起"/"辰上起"**：分别以戌宫和辰宫为子时的起点位置。英文："starting from Xu palace" / "starting from Chen palace"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："文昌戌上逆行详，文曲辰宫顺路长，一主科名一主艺，命逢昌曲贵难量。"此口诀帮助学习者记忆昌曲的安放规则与主象区别。
- **文教象征**：文昌与文曲象征古代"文教之邦"的理想：文昌代表科举正途，文曲代表琴棋书画，两者共同构成完整的文化修养。
- **现代应用**：现代解读中，文昌可延伸为正规学历、职业资格证书、公务员考试等；文曲可延伸为设计、音乐、编程、技术专长等非传统路径的才能。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j3_037]` `[trigger: 文昌定位算法]` `[factor_trigger: algo_wenchangdingwei]` `[role: 主干]` 文昌定位算法为从戌宫起子时逆数至生时的安星算法。 → 《安文昌文曲例》
- `[ns_zwds_j3_038]` `[trigger: 文曲定位算法]` `[factor_trigger: algo_wenqudingwei]` `[role: 主干]` 文曲定位算法为从辰宫起子时顺数至生时的安星算法。 → 《安文昌文曲例》
- `[ns_zwds_j3_039]` `[trigger: 六吉星体系]` `[factor_trigger: structure_liujixing]` `[role: 主干]` 六吉星体系为文昌文曲左辅右弼天魁天钺六颗吉星。 → 《安文昌文曲例》
- `[ns_zwds_j3_040]` `[trigger: 科名才艺]` `[factor_trigger: trait_keming_caiyi]` `[role: 主干]` 科名才艺为文昌主科名、文曲主才艺的区别。 → 《安文昌文曲例》
- `[ns_zwds_j3_041]` `[trigger: 昌曲同宫]` `[factor_trigger: combo_changqu_tonggong]` `[role: 条件分支]` 昌曲同宫为文昌文曲同在一宫的配置，主才华横溢。 → 《安文昌文曲例》
- `[ns_zwds_j3_042]` `[trigger: 昌曲夹宫]` `[factor_trigger: combo_changqu_jiagong]` `[role: 条件分支]` 昌曲夹宫为文昌文曲夹命宫的配置，主贵不可言。 → 《安文昌文曲例》"""
    normalized_text_zh: str = """"""
    subject: str = "安文昌文曲星诀"
    factor_refs: list = ['source_ref', 'rel_changqu_001', 'algo_wenxingdingwei', 'rel_changqu_002', 'algo_wenxingdingwei', 'rel_changqu_003', 'star_wenchang', 'evi_changqu_001', 'star_wenchang', 'rule_wenchang_dingwei', 'evi_changqu_002', 'star_wenqu', 'rule_wenqu_dingwei', 'concept_literary_star', 'concept_orthodox_talent', 'concept_artistic_talent']
    
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
        l1_anchor="zw_v1.0.0_安文昌文曲星诀_001_L1",
    )
    version: str = "1.0.0"
