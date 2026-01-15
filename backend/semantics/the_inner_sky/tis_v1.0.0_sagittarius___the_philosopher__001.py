"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.113463
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
    semantic_id="tis_v1.0.0_sagittarius___the_philosopher__001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class SagittariusThePhilosopher(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Mutable Fire | Explorato...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Mutable Fire | Exploratory flame | Element |
| Quest for Meaning | Purpose-seeking | Core drive |
| Faith | Life has coherence | Foundation |
| Vision | Big-picture | Strength |

**Source Text**: "The Archer (Centaur). Sagittarius has come to discover meaning—not just information but larger patterns, philosophical frameworks, truth giving life purpose. The endpoint is wisdom: understanding, context, meaning beyond facts."

**English Paraphrase**: **Sagittarius** = **Mutable Fire** embodying **expansion, wisdom-seeking, and teaching**. Archetype: adventurer-philosopher aiming arrow at stars, combining animal vitality with human consciousness.

**Core**: Expansion (travel/study/explore), teaching (share discovered truth), faith (life has meaning), optimism (things will work out), vision (see possibilities). **Shadow**: Dogmatism (arrogant certainty), restlessness (perpetual tourist), recklessness (risks without consequences). **Challenge**: Truth is journey not destination; remain student while teaching.

**Chinese**: 射手座=变动火象体现扩展、求智和教学。核心：扩展、教学、信念、乐观、视野。阴影：教条、不安、鲁莽。挑战：真理是旅程非目的地；教学时保持学生。

**East**: 射手↔丁火阴柔/伤官智慧 (yin fire wisdom)

#### Narrative Snippets

- `[ns_innersky_sagittarius_001]` `[trigger: sign_sagittarius]` `[factor_trigger: sign_sagittarius AND element_fire]` `[role: 主干]` The Archer (Centaur). Sagittarius has come to discover meaning—not just information but larger patterns, philosophical frameworks, truth giving life purpose. → The Inner Sky Ch.4 #Sagittarius
- `[ns_innersky_sagittarius_002]` `[trigger: sign_sagittarius AND astro_strength]` `[factor_trigger: astro_sign_sagittarius]` `[role: 主干依赖]` The endpoint is wisdom: understanding, context, meaning beyond facts. Expansion, teaching, faith, optimism, vision seeing possibilities. → The Inner Sky Ch.4 #Sagittarius
- `[ns_innersky_sagittarius_003]` `[trigger: sign_sagittarius AND astro_shadow]` `[factor_trigger: astro_sign_sagittarius AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: dogmatism (arrogant certainty that one's beliefs are absolute), restlessness (perpetual tourist), recklessness (risks without considering consequences). → The Inner Sky Ch.4 #Sagittarius
- `[ns_innersky_sagittarius_004]` `[trigger: sign_sagittarius AND astro_challenge]` `[factor_trigger: astro_sign_sagittarius]` `[role: 总结]` Truth is journey not destination; remain student while teaching. The challenge is to hold strong convictions with humility. → The Inner Sky Ch.4 #Sagittarius"""
    normalized_text_zh: str = """"""
    subject: str = "Sagittarius - The Philosopher (Mutable Fire)"
    factor_refs: list = ['new_candidate', 'sign_sagittarius', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_sagittarius___the_philosopher__001_L1",
    )
    version: str = "1.0.0"
