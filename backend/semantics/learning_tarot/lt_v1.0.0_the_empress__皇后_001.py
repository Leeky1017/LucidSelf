"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.007992
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
    semantic_id="lt_v1.0.0_the_empress__皇后_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheEmpress皇后(SemanticEntry):
    """
    **Source Text** (Lines 3655-3715):
> **Keywords**: Mothering • Abundance • Senses • Nature
>
> **Act...
    """
    
    original_text: str = """**Source Text** (Lines 3655-3715):
> **Keywords**: Mothering • Abundance • Senses • Nature
>
> **Actions**:
> - **Mothering**: giving birth, nourishing life, nurturing and caring for others, cherishing the world, expressing tenderness, working with children
> - **Experiencing the Senses**: giving and receiving pleasure, focusing on the body, appreciating beauty, feeling vibrantly healthy, being earthy, doing physical activity
> - **Welcoming Abundance**: enjoying extravagance, receiving lavish reward, luxuriating in plenty, having more than enough, feeling rich
> - **Responding to Nature**: relating to plants and animals, embracing the natural, feeling connected to the Earth, going outdoors, harmonizing with natural rhythms
>
> **Description**: The Empress and the High Priestess are the two halves of the female archetype in the major arcana. The Empress represents the fertile, life-giving Mother who reigns over the bounty of nature and the rhythms of the Earth. From her comes all the pleasures and joys of the senses and the abundance of new life in all its forms.

**Key Term Analysis**:
- **The Empress (3)**: `fertile, life-giving Mother` / `bounty of nature` / `rhythms of Earth`
- **Mothering**: `giving birth` / `nourishing life` / `nurturing and caring`
- **Abundance**: `extravagance` / `lavish reward` / `having more than enough`
- **Senses**: `pleasure` / `beauty` / `vibrantly healthy` / `earthy`
- **Nature**: `plants and animals` / `connected to Earth` / `natural rhythms`

**English Paraphrase (Primary Language)**:
**The Empress (Card 3)** represents "the fertile, life-giving Mother who reigns over the bounty of nature." She is the second half of the feminine archetype (High Priestess being the first):
- **High Priestess**: mysterious unknown, inner world, spiritual feminine
- **Empress**: fertile creativity, outer world, physical feminine

**Four domains**:
1. **Mothering**: Birth, nurturing, tenderness—creating and sustaining life
2. **Abundance**: Lavish reward, plenty, richness—"the cornucopia of delights"
3. **Senses**: Physical pleasure, beauty, health—embodied experience
4. **Nature**: Earth connection, natural rhythms, plants and animals

**Reading implication**: "The Empress can refer to any aspect of Motherhood... She can also represent lavish abundance of all kinds... with the understanding that riches go with a generous and open spirit."

**Complete Chinese Interpretation (Secondary Language)**:
**皇后（第3号牌）**代表"统治自然恩赐和大地节律的多产、赋予生命的母亲"。她是女性原型的第二面（女祭司是第一面）：
- **女祭司**：神秘的未知、内在世界、灵性女性
- **皇后**：丰饶的创造力、外在世界、肉体女性

**四个领域**：
1. **母性**：生育、滋养、温柔——创造和维持生命
2. **丰盛**：慷慨回报、富足、丰裕——"愉悦的聚宝盆"
3. **感官**：身体愉悦、美丽、健康——具身体验
4. **自然**：与大地连接、自然节律、植物和动物

**解读含义**："皇后可以指母性的任何方面……她也可以代表各种慷慨的丰盛……并理解财富伴随着慷慨开放的精神。"

**Core Points**:
- Card 3 = fertile Mother, bounty of nature, Earth rhythms
- Second feminine archetype (vs High Priestess = first)
- Mothering: birth, nurturing, creating/sustaining life
- Abundance: lavish reward, plenty, generous spirit
- Senses: physical pleasure, beauty, embodied health
- Nature: Earth connection, plants/animals, natural cycles

**Narrative Snippets**:
- `[ns_ltt_030]` `[trigger: empress_card]` `[factor_trigger: tarot_empress AND nurturing]` `[role: 主干]` The Empress represents the fertile, life-giving Mother who reigns over the bounty of nature and the rhythms of the Earth. → L3700-3702
- `[ns_ltt_031]` `[trigger: empress_feminine]` `[factor_trigger: tarot_empress AND tarot_tarot_high_priestess]` `[role: 主干依赖]` The Empress and the High Priestess are the two halves of the female archetype—High Priestess is mysterious unknown, Empress is fertile creativity. → L3698-3700
- `[ns_ltt_032]` `[trigger: empress_abundance]` `[factor_trigger: tarot_empress AND tarot_abundance AND abundance]` `[role: 总结]` The Empress represents lavish abundance—riches that go with a generous and open spirit. → L3712-3715"""
    normalized_text_zh: str = """"""
    subject: str = "The Empress (皇后)"
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_the_empress__皇后_001_L1",
    )
    version: str = "1.0.0"
