"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789198
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
    semantic_id="mlxj_v1.0.0_1_五神配八卦_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1五神配八卦(SemanticEntry):
    """
    #### 原文（source_text）

肝属木，旺于春，在卦为震巽，实则梦恚怒忿争，虚则梦林木枯槁，平和则梦台阁壮丽。

心属火，旺于夏，在卦为离，实则梦大火燔灼、疮疽疼痛，虚则梦烟销焰灭，平和则...
    """
    
    original_text: str = """#### 原文（source_text）

肝属木，旺于春，在卦为震巽，实则梦恚怒忿争，虚则梦林木枯槁，平和则梦台阁壮丽。

心属火，旺于夏，在卦为离，实则梦大火燔灼、疮疽疼痛，虚则梦烟销焰灭，平和则梦丽日融和、烛光辉燿。

肺属金，旺于秋，在卦为乾、兑，实则梦戈矛闪烁，虚则梦照鉴无光，平和则梦金珠炫彩。

肾属水，旺于冬，在卦为坎，实则梦洪涛汹涌，虚则梦水涸冰坚，平和则梦游行水际、烟雨霏微。

脾属土，旺于四季月及长夏，在卦为坤、艮，实则梦高陵大阜，虚则梦土坼山崩，平和则梦花堤柳陌、坦道平沙。

占以太过不及为凶，顺适为吉也。

#### 规范化释义（primary_lang_explained）

五脏与八卦、四时、梦象的对应关系：

| 脏 | 五行 | 旺季 | 卦象 | 实证梦象 | 虚证梦象 | 平和梦象 |
|---|------|------|------|---------|---------|---------|
| 肝 | 木 | 春 | 震、巽 | 恚怒忿争 | 林木枯槁 | 台阁壮丽 |
| 心 | 火 | 夏 | 离 | 大火燔灼、疮疽疼痛 | 烟销焰灭 | 丽日融和、烛光辉燿 |
| 肺 | 金 | 秋 | 乾、兑 | 戈矛闪烁 | 照鉴无光 | 金珠炫彩 |
| 肾 | 水 | 冬 | 坎 | 洪涛汹涌 | 水涸冰坚 | 游行水际、烟雨霏微 |
| 脾 | 土 | 四季月/长夏 | 坤、艮 | 高陵大阜 | 土坼山崩 | 花堤柳陌、坦道平沙 |

太过不及为凶，顺适为吉。"""
    normalized_text_zh: str = """"""
    subject: str = "1 五神配八卦"
    factor_refs: list = ['wuzang_gua']
    
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
        l1_anchor="mlxj_v1.0.0_1_五神配八卦_001_L1",
    )
    version: str = "1.0.0"
