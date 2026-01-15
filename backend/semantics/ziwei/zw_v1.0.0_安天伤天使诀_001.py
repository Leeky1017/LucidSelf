"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654170
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
    semantic_id="zw_v1.0.0_安天伤天使诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安天伤天使诀(SemanticEntry):
    """
    **主题**：命前六位天伤，命后六位天使。

#### 原文（断句）：

命前六位是天伤，命后六位天使当。天伤安在奴仆宫，天使安在疾厄宫。身与岁限夹在伤使中间，谓之奴夹地，更加恶曜，多凶。

####...
    """
    
    original_text: str = """**主题**：命前六位天伤，命后六位天使。

#### 原文（断句）：

命前六位是天伤，命后六位天使当。天伤安在奴仆宫，天使安在疾厄宫。身与岁限夹在伤使中间，谓之奴夹地，更加恶曜，多凶。

#### 分字分词释义：

- **命前六位**：从命宫开始顺时针数第六个宫位。
- **天伤**：杂曜之一，固定在奴仆宫，主下属、助手方面的困扰。
- **命后六位**：从命宫开始逆时针数第六个宫位。
- **天使**：杂曜之一，固定在疾厄宫，主疾病、健康方面的困扰。
- **奴夹地**：身宫或行运被天伤、天使夹制的凶险格局。
- **恶曜**：凶星、煞星的统称。

#### 安星规则：

- **天伤**：命宫顺数第六位（奴仆宫）
- **天使**：命宫逆数第六位（疾厄宫）
- **奴夹地**：身或岁限在伤使之间，加恶曜主凶

#### 规范化释义（primary_lang_explained）：

 天伤、天使皆以命宫为中心来安放：从命宫顺数六位为奴仆宫，即天伤所在；从命宫逆数六位为疾厄宫，即天使所在。当身宫或岁限行运落在这两宫之间，再加上凶曜同会时，便形成所谓"奴夹地"——上有病厄压力、下有奴仆纠缠，人处两难之中。

#### 完整对等诠释（secondary_lang_full·15天伤天使）：

 The Tianshang–Tianshi rule treats the Life Palace as a pivot. Counting six houses clockwise from the Life Palace locates Tianshang in the Servants Palace; counting six houses counter-clockwise locates Tianshi in the Illness Palace. When the Body Palace or major-period positions fall between these two, especially together with additional malefics, the pattern called "slave-encirclement" arises: the native is squeezed between problematic subordinates on one side and health burdens on the other.

 In practice, Tianshang marks trouble from helpers, employees or those in a lower position who may create damage or betrayal, while Tianshi marks chronic vulnerability through illness or caretaking obligations. Charts where life periods repeatedly pass through the zone between them often describe people who work hard to hold everything together while feeling surrounded by demands they cannot easily refuse.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 天伤 | Tianshang | 命前六位奴仆宫主奴仆之灾 | Servants Palace troubles subordinates | star_tianshang | new_candidate |
| 天使 | Tianshi | 命后六位疾厄宫主疾病负担 | Illness Palace bodily burdens | star_tianshi | new_candidate |
| 奴夹地 | Servant-Encirclement | 身或岁限在伤使间加恶曜 | Body/period trapped between with malefics | pattern_nujiadi | new_candidate |

#### 详细解说：

天伤与天使是紫微斗数杂曜系统中的两颗星，它们的位置完全由命宫决定，分别固定在奴仆宫和疾厄宫。

**算法原理**：
- 天伤固定在命宫顺数第六位，即奴仆宫
- 天使固定在命宫逆数第六位，即疾厄宫
- 由于十二宫的固定结构，天伤与天使的位置是确定的

**天伤与天使的象征意义**：
- **天伤**：在奴仆宫，象征下属、助手、合作者带来的困扰，如员工背叛、朋友欺骗、合伙人纠纷
- **天使**：在疾厄宫，象征疾病、健康问题、身心负担，如慢性病、心理压力、照顾他人的责任

**"奴夹地"格局**：
当身宫或大限流年行运落在天伤与天使之间（即迁移宫附近），又加上其他凶星同会时，便形成"奴夹地"的凶格。命主会感到两面受压：一边是人际关系的困扰，一边是健康问题的侵袭，处境艰难。

**现代应用**：
天伤可理解为职场人际关系问题、下属管理困难、朋友圈麻烦；天使可理解为健康亚红灯、家人照顾压力、心理健康问题。

#### 校勘与字词辨析（bilingual）：

- **"命前六位"**：从命宫顺时针数第六宫。英文："sixth house counting clockwise from Life Palace"。
- **"奴夹地"**：被奴仆宫与疾厄宫夹制的格局。英文："encirclement by Servants and Illness palaces"。
- **"恶曜"**：凶星、煞星的通称。英文："malefic stars"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："命前六位天伤临，命后六位天使寻，若逢身限行此地，奴欺主兮病缠身。"此诀描述天伤天使的定位及"奴夹地"的凶险。
- **固定宫位**：天伤天使与其他杂曜不同，其位置完全由十二宫的固定结构决定，不随年月日时变化。
- **现代应用**：天伤天使在现代可用于评估人际压力与健康风险的交叉点。大限或流年经过相关宫位时，需特别注意职场关系与身体保养的平衡。"""
    normalized_text_zh: str = """"""
    subject: str = "安天伤天使诀"
    factor_refs: list = ['source_ref', 'rel_shangshi_001', 'palace_ming', 'rel_shangshi_002', 'palace_ming', 'rel_shangshi_003', 'star_tianshang', 'evi_shangshi_001', 'star_tianshang', 'rule_tianshang_dingwei', 'evi_shangshi_002', 'star_tianshi', 'rule_tianshi_dingwei', 'concept_subordinate_trouble', 'concept_health_burden']
    
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
        l1_anchor="zw_v1.0.0_安天伤天使诀_001_L1",
    )
    version: str = "1.0.0"
