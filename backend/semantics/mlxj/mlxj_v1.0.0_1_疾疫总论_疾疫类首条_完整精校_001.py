"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.853779
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
    semantic_id="mlxj_v1.0.0_1_疾疫总论_疾疫类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1疾疫总论疾疫类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

凡梦身躯，上关国政，下系宗支，为政苛虐，黔黎受病；为政懈弛，边强受病；不能齐其家而居处病危。此为人之大病也。贪污暴虐，而国家之病发，内有贼盗，外有夷虏，非良...
    """
    
    original_text: str = """#### 原文（source_text）

凡梦身躯，上关国政，下系宗支，为政苛虐，黔黎受病；为政懈弛，边强受病；不能齐其家而居处病危。此为人之大病也。贪污暴虐，而国家之病发，内有贼盗，外有夷虏，非良将不能平。风寒暑湿，而脉胳之病发，蛊瘵痨瘵、疫痢、廱疽，非良药不能治。是故医比将才，药比兵卒。身发寒热者，病之初起也。梦中见之，为祸乱之征，在一家，为家事不宁也。

#### 规范化释义（primary_lang_explained）

凡梦见身躯疾病，上关国家政治，下系宗族支派。为政苛虐，则百姓受病；为政懈弛，则边疆受病；不能齐家，则居处病危。这是人的大病。

贪污暴虐，则国家之病发作，内有贼盗，外有夷虏，非良将不能平定。风寒暑湿，则脉络之病发作，蛊疾痨瘵、疫痢、痈疽，非良药不能治疗。所以医生比作将才，药物比作兵卒。

身发寒热者，是病之初起。梦中见之，是祸乱之征；在一家而言，是家事不宁之象。

#### 完整对等诠释（secondary_lang_full）

Dreams of bodily illness relate above to state affairs and below to family lineage. Harsh governance causes the people to suffer; lax governance causes borders to suffer; inability to regulate the household causes domestic crisis. These are humanity's great ailments.

Corruption and tyranny cause national illness—internal bandits, external barbarians—only good generals can pacify. Wind, cold, heat, and dampness cause meridian illness—parasites, consumption, epidemics, abscesses—only good medicine can cure. Thus physicians are like generals, medicines like soldiers.

Fever and chills signify illness beginning. Seeing this in dreams portends chaos and disorder; for a household, it signifies domestic unrest.

#### 核心要点

- 身躯梦象=国政+宗支（上下对应）
- 政治隐喻：苛虐→民病，懈弛→边病，不齐家→居病
- 医将对比：医=将，药=兵
- 寒热=病初起=祸乱之征

#### 疾疫梦象与层次对应

| 层次 | 疾病表现 | 对应问题 |
|------|---------|---------|
| 国家 | 贪污暴虐 | 内贼外虏 |
| 地方 | 懈弛政治 | 边疆不宁 |
| 家族 | 不能齐家 | 居处病危 |
| 个人 | 风寒暑湿 | 脉络疾病 |

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v11_001]` `[trigger: 政事梦象]` `[factor_trigger: dream_shenqu AND zhengzhi_cengci AND yijiang AND bingbing]` `[role: 政事类]` 身躯对应政治层次，医将如药兵。 → 《梦林玄解·卷十一》#政事
- `[ns_mlxj_v11_002]` `[trigger: 恩求祝祭]` `[factor_trigger: dream_enqiu AND enmeng_baoen AND yinde_jisha AND caifu_xinwang]` `[role: 恩求类]` 恩求报恩、阴德积善、财富心旺等梦象。 → 《梦林玄解·卷十一》#恩求祝祭
- `[ns_mlxj_v11_003]` `[trigger: 火盗杀斗]` `[factor_trigger: dream_huodao AND dream_chugou AND sha_youxue AND huo_yanyan AND dream_ji AND dream_qinshubing]` `[role: 灾凶类]` 火盗出狱杀有血等凶梦。 → 《梦林玄解·卷十一》#火盗杀斗"""
    normalized_text_zh: str = """"""
    subject: str = "1 疾疫总论（疾疫类首条·完整精校）"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_疾疫总论_疾疫类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
