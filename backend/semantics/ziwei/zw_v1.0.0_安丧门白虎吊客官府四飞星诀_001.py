"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654273
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
    semantic_id="zw_v1.0.0_安丧门白虎吊客官府四飞星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安丧门白虎吊客官府四飞星诀(SemanticEntry):
    """
    **主题**：流年凶煞，论流年太岁安四飞星。

#### 原文（断句）：

流年太岁前二位是丧门，后二位是吊客，丧门对照安白虎，吊客对照安官府。

#### 分字分词释义：

- **丧门**：流年凶...
    """
    
    original_text: str = """**主题**：流年凶煞，论流年太岁安四飞星。

#### 原文（断句）：

流年太岁前二位是丧门，后二位是吊客，丧门对照安白虎，吊客对照安官府。

#### 分字分词释义：

- **丧门**：流年凶煞之一，主丧事、哭丧、孝服。
- **白虎**：流年凶煞之一，主血光、伤害、手术。
- **吊客**：流年凶煞之一，主凶祸、吊唁、意外。
- **官府**：流年凶煞之一，主官讼、法律纠纷。
- **流年太岁**：当年的太岁所在宫位。
- **前二位**：太岁宫顺数两位。
- **后二位**：太岁宫逆数两位。
- **对照**：相隔六位的对宫。

#### 安星规则：

以流年太岁宫位为基准：
- **丧门**：太岁前二位（顺数两位）
- **吊客**：太岁后二位（逆数两位）
- **白虎**：丧门对宫
- **官府**：吊客对宫

#### 示例（子年）：
- 太岁在子
- 丧门在寅（前二）
- 吊客在戌（后二）
- 白虎在申（寅对宫）
- 官府在辰（戌对宫）

#### 规范化释义（primary_lang_explained）：

丧门、白虎、吊客、官府被合称为“四飞星”，围绕流年太岁前后二位与对宫成对飞布，是专门标记丧事、血光、凶祸与官讼压力的一组流年凶煞。歌诀“太岁前二为丧门，后二为吊客，对宫安白虎、官府”说明了算法：先以当年太岁所在宫为中心，前后各推两位定出“丧门、吊客”，再取其对宫作为“白虎、官府”，形成一个四点围绕太岁的夹击结构。

在实际断事中，四飞星本身并不保证一定有丧事或官司，而是指出“今年这些宫位格外容易沾上凶事的味道”：落入父母、田宅等宫，可能指代家中长辈、房产与家庭环境承受丧事或官非压力；落入命宫、疾厄宫，则强调自身血光、手术、意外伤害或卷入法律纠纷的风险。若又与天哭天虚、丧门本命星、重煞同会，其凶象会被成倍放大，需要在相应领域提前做好预防与风险管理。

#### 完整对等诠释（secondary_lang_full·25四飞星）：

Sangmen, Baihu, Diaoke and Guanfu are grouped as the Four Flying Stars, a travelling set of malefics that orbit the annual Tai Sui in a cross-shaped pattern. The rule is straightforward: from the year’s Tai Sui palace, count two houses forward to locate Sangmen and two houses backward for Diaoke; their opposite houses then host Baihu and Guanfu. The result is a four-point frame around the year ruler, indicating where themes of mourning, injury, misfortune and legal entanglement are more easily triggered.

In delineation, the Four Flying Stars act less like inevitable disaster and more like stress indicators. When they occupy parental, property or domestic houses, they suggest that elders, home life or land issues may intersect with funerals, accidents or courtroom matters in that year. When they fall into the Life or Health palaces, they underline vulnerability to bloodshed, surgery, violent events or disputes with authorities. Only when these placements resonate with the natal chart—such as repeating the same houses or joining heavier malefics—do they move from “heightened risk” into likely manifestation, at which point cautious planning and safety awareness become especially important.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 丧门 | Sangmen (Mourning Gate) | 以太岁前二宫安置，主丧事、哭丧与孝服应期 | Star two houses ahead of Tai Sui, linked to funerals, mourning and periods of bereavement | star_sangmen | existing |
| 白虎 | Baihu (White Tiger) | 对应丧门之对宫，主血光、伤害与手术之灾 | Opposite Sangmen, associated with bloodshed, injuries and operations | star_baihu | existing |
| 吊客 | Diaoke (Condolence Visitor) | 以太岁后二宫安置，主凶祸、吊唁与意外之事 | Star two houses behind Tai Sui, symbolising misfortune, condolence visits and disruptive events | star_diaoke | existing |
| 官府 | Guanfu (Judicial Office) | 对应吊客之对宫，主官讼、公权力介入与法律压力 | Opposite Diaoke, indicating lawsuits, legal proceedings and pressure from official institutions | star_guanfu | existing |

#### 详细解说：

丧门、白虎、吊客、官府合称"四飞星"，是紫微斗数流年推断中最重要的凶煞组合，它们围绕流年太岁形成四点夹击结构。

**算法原理**：
- 以当年太岁所在宫位为中心
- 丧门在太岁顺数两位（前二）
- 吊客在太岁逆数两位（后二）
- 白虎为丧门的对宫
- 官府为吊客的对宫

**四飞星的象征意义**：
- **丧门**：主丧事、丧亲、孝服、送终
- **白虎**：主血光、伤害、手术、意外受伤
- **吊客**：主凶祸、吊唁、意外灾难
- **官府**：主官讼、法律纠纷、与公权力打交道

**重要应用**：
- 四飞星入命限：当年需特别注意相关领域的风险
- 丧门白虎入父母疾厄：需注意家人健康与安全
- 吊客官府入迁移官禄：需注意出行安全与法律问题

**现代应用**：
四飞星可用于评估流年的风险点。入相关宫位时，需要在该领域做好预防与风险管理。

#### 校勘与字词辨析（bilingual）：

- **"丧门"**：丧事之门，主丧亲孝服。英文："Sangmen, Mourning Gate, indicating funerals and bereavement"。
- **"白虎"**：白色猛虎，主血光伤害。英文："Baihu, White Tiger, indicating bloodshed and injuries"。
- **"吊客"**：吊唁之客，主凶祸意外。英文："Diaoke, Condolence Visitor, indicating misfortune"。
- **"官府"**：官方机构，主官讼法律。英文："Guanfu, Judicial Office, indicating lawsuits"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："太岁前二丧门临，后二吊客凶祸侵，对宫白虎主血光，官府官讼是非频。"此诀概括了四飞星的定位与象征。
- **四点夹击**：古人云"四飞星围太岁，凶事难逃避"，形容四飞星对流年的凶煞作用。
- **现代应用**：四飞星在现代可用于年度风险评估。入相关宫位时，建议做好保险、体检、法律咨询等预防措施。"""
    normalized_text_zh: str = """"""
    subject: str = "安丧门白虎吊客官府四飞星诀"
    factor_refs: list = ['source_ref', 'rel_sifeixing_001', 'system_liuniantaisui', 'rel_sifeixing_002', 'star_sangmen', 'rel_sifeixing_003', 'system_liuniantaisui', 'rel_sifeixing_004', 'star_diaoke', 'evi_sifeixing_001', 'star_sangmen', 'rule_sangmen_dingwei', 'evi_sifeixing_002', 'star_diaoke', 'rule_diaoke_dingwei', 'concept_mourning_malefic', 'concept_legal_malefic']
    
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
        l1_anchor="zw_v1.0.0_安丧门白虎吊客官府四飞星诀_001_L1",
    )
    version: str = "1.0.0"
