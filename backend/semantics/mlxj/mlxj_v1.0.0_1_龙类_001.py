"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.806561
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
    semantic_id="mlxj_v1.0.0_1_龙类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1龙类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 三皇 | 帝 | 玄龟衔符 | 伐蚩尤 |
| 西汉 | 薄姬 | 苍...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 三皇 | 帝 | 玄龟衔符 | 伐蚩尤 |
| 西汉 | 薄姬 | 苍龙据腹 | 生代王（文帝） |
| 西汉 | 杨雄 | 口吐白凤 | 作甘泉赋 |
| 西晋 | 李太后 | 两龙枕膝 | 生武帝 |
| 西晋 | 郭瑀 | 乘青龙至屋 | 知将死 |
| 宋 | 刘穆之 | 二白龙夹舫 | 佐命元勋 |
| 齐 | 孙奉伯 | 捉龙脚 | 道成即位 |
| 齐 | 萧赜 | 龙据屋 | 即位 |
| 齐 | 娄太后 | 四梦龙祥 | 生四帝 |
| 隋 | 炀帝 | 龙出身中 | 生时验 |
| 唐 | 王积薪 | 青龙吐棋经 | 艺乃精 |
| 唐 | 刘暠 | 金龙绕身 | 登九五 |
| 宋 | 刘赞 | 吞金龟 | 文思进/吐龟卒 |
| 宋 | 文天祥 | 龙降 | 生祥 |
| 宋 | 陈麟母 | 麟入室 | 生陈麟 |
| 明 | 高皇 | 二龙绕斗 | 燕邸胜 |
| 明 | 秦𫟄 | 骑龙项 | 累官显贵 |
| 明 | 计礼 | 龙头一枚 | 中解元 |

#### 四梦龙祥典故（详）

齐娄太后：
- 孕文襄：梦一断龙
- 孕文宣：梦大龙首尾属天地，张口动目势状惊人
- 孕孝昭：梦蠕龙于地
- 孕武成：梦龙浴于海"""
    normalized_text_zh: str = """"""
    subject: str = "1 龙类"
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
        l1_anchor="mlxj_v1.0.0_1_龙类_001_L1",
    )
    version: str = "1.0.0"
