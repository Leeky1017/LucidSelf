"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192607
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
    semantic_id="tb_v1.0.0_quality_of_the_mind__chapter_x_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class QualityOfTheMindChapterX(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Quality of mind | Mental/psychological nature | Inner character |
| Mercury | Rational faculty | Intellectual capacity |
| Moon | Soul/emotional nature | Psychological temperament |

#### Source Text

"In investigating the quality of the mind, the situation of Mercury and of the Moon is to be considered: whether they be in angles or succedent houses, in masculine or feminine signs, in oriental or occidental positions; also whether they be configured with benefics or malefics."

#### English Paraphrase (Primary Language)

For analyzing **mental qualities**, Ptolemy assigns joint rulership to **Mercury** (rational mind) and **Moon** (emotional/soul nature). The analysis considers:

- **Angular position**: In angles (strong) or succedent (moderate)
- **Sign gender**: Masculine (assertive mind) or feminine (receptive mind)
- **Orientation**: Oriental (before Sun, more independent) or occidental (after Sun, more reflective)
- **Aspects**: Configured with benefics (sound mind) or malefics (troubled mind)

**Dual significator principle**: Mercury alone shows intellectual capacity; the Moon shows emotional temperament. Together they reveal the complete mental constitution.

#### Complete Chinese Interpretation (Secondary Language)

分析**心智品质**时，托勒密将共同主管权赋予**水星**（理性心智）和**月亮**（情感/灵魂本质）。分析考虑：

- **角宫位置**：在角宫（强）或续宫（中等）
- **星座性别**：阳性（自信心智）或阴性（接受性心智）
- **方位**：东方（太阳前，更独立）或西方（太阳后，更反思）
- **相位**：与吉星有相位（健全心智）或与凶星（困扰心智）

**双重指示星原则**：单独水星显示智力能力；月亮显示情感气质。两者一起揭示完整的心理构成。

#### Core Points

- **Dual significators**: Mercury (reason) + Moon (emotion)
- **Angular strength**: Position in houses matters
- **Sign qualities**: Gender affects expression
- **Aspectual influence**: Benefics/malefics modify

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's Mercury-Moon combination for mind differs from later traditions that emphasized Mercury alone. This dual approach captures both rational and emotional intelligence.
- **中文**: 托勒密的水星-月亮心智组合不同于后来仅强调水星的传统。这种双重方法同时捕捉理性和情感智力。

**Narrative Snippets**:
- `[ns_ptolemy_iii_007]` `[trigger: mind_quality]` `[factor_trigger: astro_mind AND astro_mercury_moon]` `[role: 主干]` The quality of mind is determined by Mercury (reason) and Moon (soul), their positions, signs, and aspects. → Source Text
- `[ns_ptolemy_iii_008]` `[trigger: dual_significator]` `[factor_trigger: astro_mercury AND astro_moon]` `[role: 主干依赖]` Mercury shows intellectual capacity while Moon shows emotional temperament—together revealing complete mental constitution. → English Paraphrase
- `[ns_tetra_iii_mr]` `[trigger: mercury_reason]` `[factor_trigger: mercury_reason]` `[role: 条件分支]` Mercury as reason significator: shows intellectual capacity, logical ability, communication skills, and rational nature. → Ptolemy III
- `[ns_tetra_iii_ms]` `[trigger: moon_soul]` `[factor_trigger: moon_soul]` `[role: 条件分支]` Moon as soul significator: shows emotional temperament, instinctual responses, and psychic receptivity. → Ptolemy III
- `[ns_tetra_iii_bm]` `[trigger: benefic_malefic]` `[factor_trigger: benefic_malefic]` `[role: 条件分支]` Benefic/malefic aspects modify mind quality: Jupiter/Venus enhance, Saturn/Mars disturb mental constitution. → Ptolemy III
- `[ns_tetra_iii_mq]` `[trigger: mind_quality]` `[factor_trigger: mind_quality]` `[role: 效果]` Mind quality is the resultant mental constitution from Mercury-Moon positions modified by benefic/malefic aspects. → Ptolemy III
- `[ns_tetra_iii_mmm]` `[trigger: mercury_moon_mind]` `[factor_trigger: mercury_moon_mind]` `[role: 主干]` Mercury-Moon mind complex: dual significators jointly ruling mental faculties—reason (Mercury) and soul (Moon). → Ptolemy III"""
    normalized_text_zh: str = """"""
    subject: str = "Quality of the Mind (Chapter XVIII)"
    factor_refs: list = ['mind_quality', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tb_v1.0.0_quality_of_the_mind__chapter_x_001_L1",
    )
    version: str = "1.0.0"
