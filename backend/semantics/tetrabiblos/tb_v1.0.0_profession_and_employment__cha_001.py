"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169535
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
    semantic_id="tb_v1.0.0_profession_and_employment__cha_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ProfessionAndEmploymentCha(SemanticEntry):
    """
    **Source Text** (Lines 7400-7550):
> The lord of action or profession is to be ascertained from the ...
    """
    
    original_text: str = """**Source Text** (Lines 7400-7550):
> The lord of action or profession is to be ascertained from the planet which may be in familiarity with the place of the mid-heaven, and with the place of the lord of that place, and with the Moon and the part of Fortune... Mercury makes scribes, astronomers, geometricians, accountants, teachers... Venus makes musicians, players, painters, perfumers... Mars makes soldiers, hunters, founders, carpenters, physicians, surgeons.

**English Paraphrase (Primary Language)**:
**Profession** is determined by the planet ruling:
- **Mid-heaven** (MC)
- **Moon's position**
- **Part of Fortune**

**Planetary professions**:

| Planet | Professions |
|--------|-------------|
| Saturn | Agriculture, navigation, building, mining, undertaking |
| Jupiter | Government, law, priesthood, banking, philosophy |
| Mars | Military, surgery, smithing, hunting, athletics |
| Venus | Music, art, perfumery, jewelry, prostitution |
| Mercury | Writing, teaching, astronomy, commerce, interpretation |
| Sun | Kingship, leadership, public offices |
| Moon | Navigation, midwifery, embassy, trade in liquids |

**Multiple planets** = multiple professions or trades combining their natures.
**Benefic configuration** = honorable profession; **Malefic** = dishonorable.

**Complete Chinese Interpretation (Secondary Language)**:
**职业**由主宰以下位置的行星决定：
- **中天**（MC）
- **月亮位置**
- **福点**

**行星职业**：

| 行星 | 职业 |
|------|------|
| 土星 | 农业、航海、建筑、采矿、殡葬 |
| 木星 | 政府、法律、祭司、银行、哲学 |
| 火星 | 军事、外科、冶炼、狩猎、竞技 |
| 金星 | 音乐、艺术、香水、珠宝、娼妓 |
| 水星 | 写作、教学、天文、商业、翻译 |
| 太阳 | 王权、领导、公职 |
| 月亮 | 航海、助产、使节、液体贸易 |

**多行星** = 多职业或结合其性质的行业。
**吉星配置** = 尊贵职业；**凶星** = 卑贱职业。

**Core Points**:
- MC ruler = primary profession indicator
- Each planet governs specific trades
- Multiple ruling planets = multiple or combined professions
- Benefic aspects = honorable work; Malefic = dishonorable
- Moon adds navigation and public dealings

**Narrative Snippets**:
- `[ns_tetra_iv005]` `[trigger: profession]` `[factor_trigger: astro_planet_ruler_mc]` `[role: 主干]` Profession is determined by the planet ruling the mid-heaven—each planet governs specific trades. → Source Text IV.3
- `[ns_tetra_iv006]` `[trigger: mercury_professions]` `[factor_trigger: astro_planet_mercury AND astro_house_10]` `[role: 条件分支]` Mercury ruling MC: scribes, astronomers, accountants, teachers, interpreters. → Source Text IV.3
- `[ns_tetra_iv_pt]` `[trigger: profession_type]` `[factor_trigger: profession_type]` `[role: 效果]` Profession type determined by MC ruler: Saturn=agriculture/building, Jupiter=law/religion, Mars=military/surgery, Venus=art/music, Mercury=writing/commerce. → Source Text IV.3"""
    normalized_text_zh: str = """"""
    subject: str = "Profession and Employment (Chapter III)"
    factor_refs: list = ['lord_of_action', 'new_candidate']
    
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
        l1_anchor="tb_v1.0.0_profession_and_employment__cha_001_L1",
    )
    version: str = "1.0.0"
