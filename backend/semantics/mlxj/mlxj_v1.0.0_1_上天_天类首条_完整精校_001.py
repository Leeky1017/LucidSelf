"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.783912
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
    semantic_id="mlxj_v1.0.0_1_上天_天类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1上天天类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

上天。虞帝尧受封于唐，为诸侯，尝梦上天，故二十而登帝位。

#### 规范化释义（primary_lang_explained）

帝尧受封于唐为诸侯，曾梦...
    """
    
    original_text: str = """#### 原文（source_text）

上天。虞帝尧受封于唐，为诸侯，尝梦上天，故二十而登帝位。

#### 规范化释义（primary_lang_explained）

帝尧受封于唐为诸侯，曾梦上天。故二十岁即登帝位。

梦上天→登帝位

#### 完整对等诠释（secondary_lang_full）

Emperor Yao was enfeoffed at Tang as a feudal lord. He once dreamed of ascending to heaven, and thus ascended to the imperial throne at age twenty.

Dream of ascending heaven → Imperial enthronement

#### 核心要点

- 梦上天=登帝位之征
- 典故：虞帝尧

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v30_001]` `[trigger: 天象梦征]` `[factor_trigger: dream_dengdiwei AND dream_tianlei AND dream_leiyu AND dream_long AND dream_zhongkui]` `[role: 天象类]` 登帝位、天雷、雷雨、龙、钟馗等天象梦征。 → 《梦林玄解·卷三十》#天象
- `[ns_mlxj_v30_002]` `[trigger: 典故梦征]` `[factor_trigger: lishi_zhuran AND lishi_tanggaozu AND lishi_weiyan AND lishi_xuanzong AND zi_jiao]` `[role: 典故]` 朱然、唐高祖、魏延、玄宗等历史典故及子骄。 → 《梦林玄解·卷三十》#典故
- `[ns_mlxj_v30_003]` `[trigger: 梦象分类]` `[factor_trigger: dream_denglou AND dream_chengche AND dream_chengzhou AND dream_kaixing AND dream_daojian AND dream_yifu AND dream_fenglin AND dream_huxiongluu]` `[role: 综合类]` 登楼、乘车、乘舟、开星、刀剑、衣服、风林、狐熊鹿等梦象。 → 《梦林玄解·卷三十》#梦象
- `[ns_mlxj_v30_004]` `[trigger: 身体梦征]` `[factor_trigger: dream_toushengjiao AND dream_shensizhuichuang AND xueshi_tongxiao]` `[role: 身体类]` 头生角、身死坠床、血食通霄等身体梦征。 → 《梦林玄解·卷三十》#身体"""
    normalized_text_zh: str = """"""
    subject: str = "1 上天（天类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_上天_天类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
