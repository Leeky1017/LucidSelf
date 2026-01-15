"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272584
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
    semantic_id="pit_v1.0.0_neptune_in_the_fourth_house__海_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheFourthHouse海(SemanticEntry):
    """
    **Source Text** (Lines 16746-16769):
> Domestic and personal life will undergo strange and subtle ch...
    """
    
    original_text: str = """**Source Text** (Lines 16746-16769):
> Domestic and personal life will undergo strange and subtle changes, reflecting psychological changes within. May become attracted to spiritual and occult subjects from your own experiences. If haven't had much home life, may create in your mind ideal of what home should be—work hard to make it reality, but if too ideal, difficult for anything real to live up to. Another side: home life may become source of confusion because someone working against your best interests. May feel demoralized and less confident without any actual problems. These feelings sign of tremendous inner changes. Communications with parents may become difficult, or parent may have difficulties affecting your sense of security. Sometimes coincides with illness/hospitalization of parent.

**English Paraphrase**: Domestic life undergoes subtle changes reflecting inner psychology. May attract to occult. May create ideal home in mind—hard for reality to match. Home may be confusing—someone working against you. May feel demoralized. Parent communications difficult or parent may have difficulties.

**Complete Chinese Interpretation**: 家庭生活经历微妙变化反映内在心理。可能被神秘学吸引。可能在脑中创造理想家庭——现实难以匹配。家可能令人困惑——有人在对付你。可能感到士气低落。与父母沟通困难或父母可能有困难。

**Narrative Snippets**:
- `[ns_pit_ne004]` `[trigger: neptune_transit_house_4]` `[factor_trigger: astro_transit_neptune AND astro_house_4]` `[role: 主干]` Domestic life changes subtly. May idealize home. Confusion possible. Inner changes. Parent issues. → PIT Ch12 Neptune-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Fourth House (海王星过境第四宫)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_neptune_in_the_fourth_house__海_001_L1",
    )
    version: str = "1.0.0"
