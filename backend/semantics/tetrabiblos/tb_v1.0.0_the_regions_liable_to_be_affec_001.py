"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162789
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
    semantic_id="tb_v1.0.0_the_regions_liable_to_be_affec_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheRegionsLiableToBeAffec(SemanticEntry):
    """
    **Source Text**:
> The countries thus liable to be affected by the eclipse are those which are in fa...
    """
    
    original_text: str = """**Source Text**:
> The countries thus liable to be affected by the eclipse are those which are in familiarity with the sign in which the eclipse takes place... by means of houses, exaltations, triplicities, or terms of the planets which rule those countries.

**English Paraphrase (Primary Language)**:
Regions affected by an eclipse are determined by their **zodiacal familiarity**:
- Countries ruled by the sign of the eclipse
- Countries ruled by planets dignified in that sign (domicile, exaltation, triplicity, terms)
- Countries whose ruling planet configurates the eclipse

The closer the familiarity, the more direct and intense the effect.

**Complete Chinese Interpretation (Secondary Language)**:
受日食影响的地区由其**黄道亲和性**决定：被日食星座主宰的国家、被该星座中有尊贵的行星主宰的国家、主宰行星与日食配置的国家。

**Core Points**:
- Affected regions = those with zodiacal familiarity to eclipse sign
- Familiarity through domicile, exaltation, triplicity, or terms
- Closer familiarity = stronger effect

**Narrative Snippets**:
- `[ns_tetra_ii006]` `[trigger: eclipse_regions]` `[factor_trigger: astro_eclipse_affected_region]` `[role: 条件分支]` Regions affected by eclipse are those in familiarity with the eclipse sign through dignities. → Source Text II.6
- `[ns_tetra_ii_zf]` `[trigger: zodiacal_familiarity]` `[factor_trigger: zodiacal_familiarity]` `[role: 条件分支]` Zodiacal familiarity connects regions to eclipse through dignities: domicile, exaltation, triplicity, or terms rulership. → Source Text II.6
- `[ns_tetra_ii_er]` `[trigger: eclipse_region]` `[factor_trigger: eclipse_region]` `[role: 效果]` Eclipse region is determined by zodiacal familiarity—the closer the dignity connection, the more intense the effect. → Source Text II.6"""
    normalized_text_zh: str = """"""
    subject: str = "The Regions Liable to be Affected (Chapter VI)"
    factor_refs: list = ['zodiacal_familiarity']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_the_regions_liable_to_be_affec_001_L1",
    )
    version: str = "1.0.0"
