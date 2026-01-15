"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.402080
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
    semantic_id="dvd_v1.0.0_dress_衣服_形象_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Dress衣服形象(SemanticEntry):
    """
    ### Source Text

> **Dress**: Your image to the world representing who you are and your position.
> ...
    """
    
    original_text: str = """### Source Text

> **Dress**: Your image to the world representing who you are and your position.
> A bride wore a dress that was white and without spot—a union and being pure. A purple dress with rich fabric represents wealth. To receive a blue dress is a picture of being given a ministry. To receive new clothes means the Lord is about to bring change.
> Zechariah 3:3 "Now Joshua was clothed with filthy garments, and stood before the angel."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Dress | 衣服 | 形象和地位 |
| Image | 形象 | 你向世界呈现的 |
| Position | 地位 | 你的站立 |
| New clothes | 新衣服 | 改变和更新 |

### English Paraphrase

A dress represents your image to the world—who you are and your position. A white bridal dress speaks of purity and union. Purple represents wealth. Blue dress represents ministry. Receiving new clothes means the Lord is bringing change. Torn or moth-eaten dress speaks of flesh and worldliness.

### Chinese Interpretation

衣服代表你向世界呈现的形象——你是谁和你的地位。白色新娘礼服象征纯洁和联合。紫色代表财富。蓝色衣服代表事工。接受新衣服意味着主正在带来改变。破烂或被虫蛀的衣服象征肉体和世俗。

### Core Points

1. **正负皆可**: 衣服状态决定含义
2. **形象象征**: 代表你向世界呈现的
3. **颜色含义**: 不同颜色有不同含义
4. **更新记号**: 新衣服代表改变

### Narrative Snippets

- `[ns_dav_d026]` `[trigger: dress_new]` `[factor_trigger: dream_dress AND dream_new]` `[role: 主干]` Receiving new clothes means the Lord is about to bring a change in your life and position. → 接受新衣服意味着主即将在你的生命和地位中带来改变。
- `[ns_dav_d027]` `[trigger: dress_torn]` `[factor_trigger: dream_dress AND dream_torn]` `[role: 警告]` A dress that is moth-eaten and torn speaks of the stain of flesh and involvement in the world. → 被虫蛀和破烂的衣服象征肉体的污渍和参与世界。"""
    normalized_text_zh: str = """"""
    subject: str = "Dress 衣服/形象"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_dress_衣服_形象_001_L1",
    )
    version: str = "1.0.0"
