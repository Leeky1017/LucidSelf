"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793447
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
    semantic_id="mlxj_v1.0.0_6_天象诸兆_综合条目_001",
    book_id="mlxj",
    engine_id="dream"
)
class 6天象诸兆综合条目(SemanticEntry):
    """
    #### 原文摘要

- 梦天高亮：阳明显达之象，事事亨吉
- 梦天昏黑：意多郁抑，主事不明
- 梦天崩裂：凡百忧虞，上危中决，主有大丧、大败
- 梦天低近身：主被宠承恩
- 梦天作悲鸣：主凶丧大故，...
    """
    
    original_text: str = """#### 原文摘要

- 梦天高亮：阳明显达之象，事事亨吉
- 梦天昏黑：意多郁抑，主事不明
- 梦天崩裂：凡百忧虞，上危中决，主有大丧、大败
- 梦天低近身：主被宠承恩
- 梦天作悲鸣：主凶丧大故，四境兵荒
- 梦投天河中：不利济涉之象
- 梦天色将晓：年华方盛
- 梦天晚无光：主晚景凄凉，家道中替
- 天青色：吉，功名遂，家业丰
- 天色红黄：福禄永昌
- 天色黑白：不为佳兆
- 天上霞光灿烂照身：大吉，宠光荐至，灾病全除
- 天开眼：大吉，富贵异常，福寿骈臻
- 天张口舌：大不祥，争讼不宜
- 以舌餂天：大吉，非至德之圣人不可妄言
- 捧天：大吉，匡扶社稷之兆
- 背负天：身当重任之象

#### 语义提取表

| 梦象 | 吉凶 | 主应 | factor_id |
|------|------|------|-----------|
| 天高亮 | 吉 | 阳明显达 | dream_tian_gaoliang |
| 天昏黑 | 凶 | 事不明 | dream_tian_hunhei |
| 天崩裂 | 大凶 | 大丧大败 | dream_tian_benglie |
| 天低近身 | 吉 | 被宠承恩 | dream_tian_dijinshen |
| 天悲鸣 | 凶 | 凶丧兵荒 | dream_tian_beiming |
| 天青色 | 吉 | 功名家业 | dream_tian_qingse |
| 天开眼 | 大吉 | 富贵福寿 | dream_tian_kaiyan |
| 捧天 | 大吉 | 匡扶社稷 | dream_pengtian |
| 背负天 | 吉 | 身当重任 | dream_beifutian |"""
    normalized_text_zh: str = """"""
    subject: str = "6 天象诸兆（综合条目）"
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
        l1_anchor="mlxj_v1.0.0_6_天象诸兆_综合条目_001_L1",
    )
    version: str = "1.0.0"
