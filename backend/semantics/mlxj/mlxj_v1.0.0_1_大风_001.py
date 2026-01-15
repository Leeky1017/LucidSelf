"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831713
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
    semantic_id="mlxj_v1.0.0_1_大风_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1大风(SemanticEntry):
    """
    #### 原文（source_text）

忽起大风，大吉。申天之命，上行下承，在卦为巽，国有号令，主凡事有扫荡邪秽，吹嘘惠泽之象。风者，养物成功。四时有八风：立春条风至，地暖；春分明庶风至，万物产；...
    """
    
    original_text: str = """#### 原文（source_text）

忽起大风，大吉。申天之命，上行下承，在卦为巽，国有号令，主凡事有扫荡邪秽，吹嘘惠泽之象。风者，养物成功。四时有八风：立春条风至，地暖；春分明庶风至，万物产；立夏清明风至，物形；夏至景风至，棘造实；立秋凉风至，黍禾乾；秋分阊阖风至，生荠麦；立冬不周风至，蛰虫匿；冬至广莫风至，万物伏。所谓风者，萌也，萌于庶物之间也。

#### 规范化释义（primary_lang_explained）

梦见忽然刮起大风，大吉。这是申明天命、上行下效的象征，对应《易经》巽卦。主国家有号令颁布，凡事有扫荡邪恶污秽、吹拂惠泽恩德的象征。

风是养育万物使之成功的力量。一年四时有八种风：立春条风至则地暖；春分明庶风至则万物生产；立夏清明风至则物形成；夏至景风至则棘生实；立秋凉风至则黍禾干燥；秋分阊阖风至则荠麦生；立冬不周风至则蛰虫隐匿；冬至广莫风至则万物蛰伏。所谓风者，萌动之意，萌发于万物之间。

#### 完整对等诠释（secondary_lang_full）

Dreaming of a sudden great wind is greatly auspicious. This symbolizes the proclamation of Heaven's mandate, with superiors giving orders and subordinates receiving them—corresponding to the Xun (Wind) hexagram in the I Ching. It indicates national decrees and represents sweeping away evil impurities while spreading beneficial influence.

Wind nurtures all things to fruition. The four seasons have eight winds: at Spring's Beginning, the Tiao wind arrives and earth warms; at Spring Equinox, the Mingzhu wind arrives and all things are born; at Summer's Beginning, the Qingming wind arrives and forms take shape; at Summer Solstice, the Jing wind arrives and thorny plants bear fruit; at Autumn's Beginning, the cool wind arrives and millet dries; at Autumn Equinox, the Changhe wind arrives and shepherd's purse and wheat grow; at Winter's Beginning, the Buzhou wind arrives and hibernating insects hide; at Winter Solstice, the Guangmo wind arrives and all things rest. Wind means "sprouting"—it sprouts among all things.

#### 核心要点

- **梦象**：忽起大风
- **吉凶**：大吉
- **卦象**：巽卦
- **主应**：国有号令、扫荡邪秽、吹嘘惠泽
- **八风理论**：立春条风、春分明庶风、立夏清明风、夏至景风、立秋凉风、秋分阊阖风、立冬不周风、冬至广莫风

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v2_001]` `[trigger: 大风]` `[factor_trigger: dream_dafeng AND yijing_xun]` `[role: 吉象]` 忽起大风，大吉。申天之命，在卦为巽，主扫荡邪秽，吹嘘惠泽。 → 《梦林玄解·卷二》#大风
- `[ns_mlxj_v2_002]` `[trigger: 八风]` `[factor_trigger: bafeng AND dream_bafeng_theory AND sishi]` `[role: 理论基础]` 四时有八风：立春条风、春分明庶风...风者，萌也，萌于庶物之间也。 → 《梦林玄解·卷二》#大风
- `[ns_mlxj_v2_003]` `[trigger: 风云诸兆]` `[factor_trigger: fengyun AND tianming AND jieling]` `[role: 天象体系]` 风云雷雨霜雪等天象梦兆，应时令节气。 → 《梦林玄解·卷二》#风云
- `[ns_mlxj_v2_004]` `[trigger: 雷雨梦象]` `[factor_trigger: lei AND yu AND tianling AND tianze]` `[role: 雷雨类]` 雷者令也天之号令，雨者恩泽也天之润泽。 → 《梦林玄解·卷二》#雷雨
- `[ns_mlxj_v2_005]` `[trigger: 霜雪梦象]` `[factor_trigger: xue AND lu AND enze AND gongming]` `[role: 霜雪类]` 雪主功名，露主恩泽。 → 《梦林玄解·卷二》#霜雪
- `[ns_mlxj_v2_006]` `[trigger: 雾虹梦象]` `[factor_trigger: wu AND hongni AND hunmeng AND yinyang_jiaojie]` `[role: 雾虹类]` 雾主昏蒙，虹主阴阳交接。 → 《梦林玄解·卷二》#雾虹
- `[ns_mlxj_v2_007]` `[trigger: 冰火梦象]` `[factor_trigger: bing_jie AND caiyuan AND xiaosan AND huo_qi AND jiji]` `[role: 冰火类]` 冰主财源消散，火主气急之象。 → 《梦林玄解·卷二》#冰火"""
    normalized_text_zh: str = """"""
    subject: str = "1 大风"
    factor_refs: list = []
    
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
        l1_anchor="mlxj_v1.0.0_1_大风_001_L1",
    )
    version: str = "1.0.0"
