"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.819266
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
    semantic_id="mlxj_v1.0.0_1_太任_后妃类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1太任后妃类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

太任大吉。帝王梦之，主生明圣之子。贤人梦之，必育天挺之英。女人梦之，兆亦如是。惟常人与杂役见梦，反为不祥，或主以女匹人，则亦吉利之兆也。

#### 分字分...
    """
    
    original_text: str = """#### 原文（source_text）

太任大吉。帝王梦之，主生明圣之子。贤人梦之，必育天挺之英。女人梦之，兆亦如是。惟常人与杂役见梦，反为不祥，或主以女匹人，则亦吉利之兆也。

#### 分字分词释义

- **太任**：周文王之母 / 胎教之祖 / 贤母典范
- **明圣之子**：聪明圣德之子嗣 / 如文王武王
- **天挺之英**：天生英杰 / 非凡之才
- **以女匹人**：将女儿许配他人 / 嫁女得佳婿

#### 规范化释义（primary_lang_explained）

梦见太任，大吉。帝王梦此，主生明圣之子。贤人梦此，必育天挺之英。女人梦此，兆亦如是。唯常人与杂役见梦，反为不祥；或主以女匹人，则亦吉利之兆。

太任是周文王之母，史载其「目不视恶色，耳不听淫声，口不出傲言」，为胎教之祖。梦见太任，主生育贤德子嗣。

#### 完整对等诠释（secondary_lang_full）

Dreaming of Tai Ren (mother of King Wen of Zhou) is greatly auspicious. If an emperor dreams this, it portends giving birth to a wise and sage son. If a virtuous person dreams this, they will surely raise an extraordinary talent. If a woman dreams this, the omen is likewise. However, for common people and servants, such a dream is inauspicious—unless it signifies marrying off a daughter to a worthy family, which is then auspicious.

#### 核心要点

- 太任=周文王之母=胎教之祖=贤母典范
- **身份分化**：帝王/贤人→大吉生贵子，常人→不祥或嫁女
- 主生育：明圣之子、天挺之英
- 女人梦之亦主得贤德子嗣

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v5_001]` `[trigger: 梦太任]` `[factor_trigger: dream_jian_tairen AND dream_tairen]` `[role: 主干]` 太任大吉。帝王梦之，主生明圣之子；贤人梦之，必育天挺之英。 → 《梦林玄解·卷五》#太任
- `[ns_mlxj_v5_002]` `[trigger: 人物梦象]` `[factor_trigger: dream_xianfo AND dream_jiexiao AND jiexiao_diangu AND dream_shengzi]` `[role: 人物类]` 梦见仙佛、节孝、生子等人物梦象。 → 《梦林玄解·卷五》#人物
- `[ns_mlxj_v5_003]` `[trigger: 后妃梦象]` `[factor_trigger: dream_houfei AND houfei_dexing AND dream_yinben AND chongbi_nanguo]` `[role: 后妃类]` 梦后妃得行、淫奔、宠妾等后妃类梦象。 → 《梦林玄解·卷五》#后妃"""
    normalized_text_zh: str = """"""
    subject: str = "1 太任（后妃类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_太任_后妃类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
