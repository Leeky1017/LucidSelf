"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.845107
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
    semantic_id="mlxj_v1.0.0_1_修德为禳梦至言_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1修德为禳梦至言(SemanticEntry):
    """
    #### 原文（source_text）

尚子平曰：魂之所丽，气为通也；气之所循，躬为召也。若夫异梦来感，无辨妖祥，时栗惧省修，以德迎之，斯足逢吉。

故曰：天子梦恶则修道，诸侯梦恶则修政，大夫、士...
    """
    
    original_text: str = """#### 原文（source_text）

尚子平曰：魂之所丽，气为通也；气之所循，躬为召也。若夫异梦来感，无辨妖祥，时栗惧省修，以德迎之，斯足逢吉。

故曰：天子梦恶则修道，诸侯梦恶则修政，大夫、士梦恶则修身。又曰：恶梦不胜善行也。

说苑云：妖孽者，天之所以警天子、诸侯也；恶梦者，所以警士大夫也。故妖孽不胜善政，恶梦不胜善行。

#### 规范化释义（primary_lang_explained）

尚子平说：魂所附丽之处，气为其通道；气所循行之处，自身为其召感。若有异梦来感，无法分辨是妖是祥，应当恐惧反省修身，以德行迎接它，便足以逢吉。

因此说：天子梦恶则修道，诸侯梦恶则修政，大夫士梦恶则修身。又说：恶梦胜不过善行。

《说苑》云：妖孽是上天用来警告天子诸侯的；恶梦是用来警告士大夫的。所以妖孽胜不过善政，恶梦胜不过善行。

#### 核心要点

- **修德禳梦原则**：以德迎之，斯足逢吉
- **层级对应**：
  - 天子梦恶 → 修道
  - 诸侯梦恶 → 修政
  - 大夫士梦恶 → 修身
- **核心论断**：恶梦不胜善行

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v27_002]` `[trigger: 修德禳梦]` `[factor_trigger: dream_response]` `[role: 核心原则]` 天子梦恶则修道，诸侯梦恶则修政，大夫士梦恶则修身。恶梦不胜善行。 → 《梦林玄解·卷二十七》#感梦修省说"""
    normalized_text_zh: str = """"""
    subject: str = "1 修德为禳梦至言"
    factor_refs: list = ['xiude_rangmeng']
    
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
        l1_anchor="mlxj_v1.0.0_1_修德为禳梦至言_001_L1",
    )
    version: str = "1.0.0"
