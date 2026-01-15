"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.798180
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
    semantic_id="mlxj_v1.0.0_1_饮天河之水_泉茗类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1饮天河之水泉茗类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

饮天河之水，大吉。天一生水，为五行之首，而万物所自始。天河之水，为百川之源，而众流所自出，梦饮此水者，主大贵之兆。居官沐天恩，居家受天福，武将得天机，文士食...
    """
    
    original_text: str = """#### 原文（source_text）

饮天河之水，大吉。天一生水，为五行之首，而万物所自始。天河之水，为百川之源，而众流所自出，梦饮此水者，主大贵之兆。居官沐天恩，居家受天福，武将得天机，文士食天禄，有疾遇天医，生男必天玉。

#### 规范化释义（primary_lang_explained）

梦饮天河之水，大吉。天一生水，是五行之首，万物所自始。天河之水是百川之源，众流所自出。

梦饮此水者，主大贵之兆：
- 居官者：沐天恩
- 居家者：受天福
- 武将：得天机
- 文士：食天禄
- 有疾者：遇天医
- 生男：必天玉

#### 完整对等诠释（secondary_lang_full）

Dreaming of drinking water from the Heavenly River (Milky Way) is greatly auspicious. Heaven first created water as the foremost of the Five Elements, from which all things originate. The Heavenly River is the source of all streams.

Dreaming of drinking this water signifies great nobility:
- Officials: bathed in heavenly grace
- Homemakers: receiving heavenly blessings
- Military generals: obtaining heavenly strategy
- Scholars: enjoying heavenly salary
- The ill: meeting heavenly physicians
- Sons born: destined for heavenly excellence

#### 核心要点

- 天河水=百川之源=万物所始
- 天一生水=五行之首
- 大贵之兆=各类天恩
- 身份分化：官/家/武/文/病/子

#### 典故

侯弘实冲龄梦入河饮水：有虹自河贯口，僧相之曰"霓龙也，官必显荣"，后从兴圣太子收蜀。

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v17_001]` `[trigger: 饮食梦象]` `[factor_trigger: dream_yintianhe AND dream_dagui AND dream_gaosheng AND dream_gao]` `[role: 饮食类]` 饮天河主大贵高升。 → 《梦林玄解·卷十七》#饮食
- `[ns_mlxj_v17_002]` `[trigger: 肴馔梦象]` `[factor_trigger: dream_jiuwei AND dream_yaozuan AND dream_jielie AND dream_yangtou]` `[role: 肴馔类]` 酒味佳肴、筵席戒烈、仰头饮等梦象。 → 《梦林玄解·卷十七》#肴馔
- `[ns_mlxj_v17_003]` `[trigger: 蔬果梦象]` `[factor_trigger: dream_caimi AND dream_caomu]` `[role: 蔬果类]` 菜苗草木等蔬果梦象。 → 《梦林玄解·卷十七》#蔬果"""
    normalized_text_zh: str = """"""
    subject: str = "1 饮天河之水（泉茗类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_饮天河之水_泉茗类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
