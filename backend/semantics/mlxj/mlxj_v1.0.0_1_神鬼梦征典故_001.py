"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.810784
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
    semantic_id="mlxj_v1.0.0_1_神鬼梦征典故_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1神鬼梦征典故(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 北魏 | 魏主 | 老公拜立道左（晋侍中嵇绍） | 吊祭后安宁 |
|...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 北魏 | 魏主 | 老公拜立道左（晋侍中嵇绍） | 吊祭后安宁 |
| 唐 | 江陵力昌 | 蛇被诉阎摩天子 | 写经救厄 |
| 唐 | 杨氏 | 神人复鼎 | 生肃宗 |
| 唐 | 开元帝 | 九天使者 | 庐山建宫 |
| 唐 | 玄宗 | 凌波池龙女 | 作凌波曲 |
| 唐 | 玄宗 | 终南进士锺馗 | 痁疾顿瘳 |
| 唐 | 玄宗 | 竹山神 | 紫箨山名 |
| 宋 | 滑世昌 | 城隍神告大灾 | 阖门获救 |

#### 锺馗典故（详）

唐帝因痁疾作，昼梦一小鬼盗太真绣香囊及上玉笛。上怒欲呼武士，俄见一大鬼顶破帽、衣蓝袍、系角带、靸朝靴，迳捉小鬼先刳其目然后擘而啖之。

大鬼自称：臣终南进士锺馗也，因武德中应举不捷，羞归故里，触殿阶而死，蒙赐绿袍以葬，感恩发誓除天下虚耗妖孽。

言讫而寤，痁疾顿瘳。诏画工吴道子如梦图之。"""
    normalized_text_zh: str = """"""
    subject: str = "1 神鬼梦征典故"
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
        l1_anchor="mlxj_v1.0.0_1_神鬼梦征典故_001_L1",
    )
    version: str = "1.0.0"
