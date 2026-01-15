"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.152310
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
    semantic_id="ca_v1.0.0_children__5th_house_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class Children5thHouse(SemanticEntry):
    """
    #### Source Text
(Lilly Book III, pp. 602-605): "Of Children. Jupiter or Venus in 5th, or Lord of 5t...
    """
    
    original_text: str = """#### Source Text
(Lilly Book III, pp. 602-605): "Of Children. Jupiter or Venus in 5th, or Lord of 5th well-dignified = children. Saturn or Mars afflicting 5th = few or none. Fruitful signs on 5th cusp = many children."

#### English Paraphrase (Primary Language)

**Children indicators**:
- **Lord of 5th**: Dignified = children; debilitated = difficulty
- **Planets in 5th**: Jupiter/Venus = fruitful; Saturn/Mars = barren
- **Fruitful signs** on 5th cusp: Cancer, Scorpio, Pisces = many
- **Barren signs** on 5th cusp: Gemini, Leo, Virgo = few

**Number of children**: Count planets in 5th, aspects to L5, fruitfulness of signs involved.

**Gender**: Masculine planets/signs = male; feminine = female.

#### Complete Chinese Interpretation (Secondary Language)

**子女指标**：第5宫主尊贵=有子女，失势=困难；第5宫内行星：木星/金星=多产，土星/火星=少子；第5宫尖**多产星座**（巨蟹、天蝎、双鱼）=多；**贫瘠星座**（双子、狮子、处女）=少。**子女数量**：计算第5宫内行星、L5相位、相关星座多产性。**性别**：阳性行星/星座=男；阴性=女。

**Narrative Snippets**:
- `[ns_lilly_child_001]` `[trigger: children]` `[factor_trigger: astro_fertility]` `[role: 主干]` Lord of 5th dignified with benefics in 5th = children; malefics = few or difficulty. → CA III #Children
- `[ns_lilly_child_002]` `[trigger: fruitful]` `[factor_trigger: astro_child_number]` `[role: 条件分支]` Fruitful signs (Cancer, Scorpio, Pisces) on 5th cusp indicate many children. → CA III #Children
- `[ns_lilly_child_003]` `[trigger: lord_5th]` `[factor_trigger: astro_lord_5th_dignity]` `[role: 主干依赖]` Lord of 5th dignified with benefics = children; with malefics = difficulty. → English Paraphrase
- `[ns_lilly_child_004]` `[trigger: fruitful_sign]` `[factor_trigger: astro_fruitful_sign_5th]` `[role: 条件分支]` Fruitful signs on 5th (Cancer/Scorpio/Pisces) vs barren (Gemini/Leo/Virgo). → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Children (5th House)"
    factor_refs: list = ['lord_5th', 'fruitful_sign', 'barren_sign']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_children__5th_house_001_L1",
    )
    version: str = "1.0.0"
