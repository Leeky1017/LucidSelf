"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.806610
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
    semantic_id="mlxj_v1.0.0_1_马牛羊猪犬类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1马牛羊猪犬类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 战国 | 吴王夫差 | 两黑犬嗥 | 阴匿之兆 |
| 东晋 | 李回...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 战国 | 吴王夫差 | 两黑犬嗥 | 阴匿之兆 |
| 东晋 | 李回 | 乘白马入梨山 | 立祠 |
| 东晋 | 谢安 | 乘桓温舆 | 代位后薨 |
| 东晋 | 牵腾 | 断马足 | 马足自断 |
| 梁 | 宣武王 | 乘马飞半天而坠 | 赤龙腾虚 |
| 梁 | 朱耽 | 犬羊御座 | 侯景登殿 |
| 西汉 | 高祖 | 逐羊拔角尾 | 去角尾为王 |
| 三国 | 云长 | 猪啮足 | 为吴人所袭 |
| 三国 | 蒋琬 | 牛头在门 | 位至公 |
| 三国 | 曹操 | 三马同槽 | 司马氏当国 |
| 东晋 | 王敦 | 白犬啮之 | 死 |
| 唐 | 某人 | 妾为猪伤 | 擒诸姓贼 |
| 宋 | 徐元杰 | 二黑犬 | 默字有黑犬 |
| 宋 | 宋太祖孙 | 拥一羊 | 生伯琮为孝宗 |
| 宋 | 阮登炳 | 独角青牛 | 代毛自知状元 |
| 明 | 徐宗 | 大猪 | 己亥生擢御史 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 马牛羊猪犬类"
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
        l1_anchor="mlxj_v1.0.0_1_马牛羊猪犬类_001_L1",
    )
    version: str = "1.0.0"
