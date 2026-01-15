"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169559
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
    semantic_id="tb_v1.0.0_marriage__chapter_v_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class MarriageChapterV(SemanticEntry):
    """
    **Source Text** (Lines 7560-7605):
> In the case of men, the Moon and Venus are to be observed; for ...
    """
    
    original_text: str = """**Source Text** (Lines 7560-7605):
> In the case of men, the Moon and Venus are to be observed; for if they be in mutual configuration, or counterchanging places, the native will be connected with one wife only, provided they be also in fixed signs. If in bicorporeal or tropical signs, he will have several wives. If Saturn be in configuration, the marriage will be with elderly women; if Jupiter, with women of rank or wealth; if Mars, with bold or violent women.

**English Paraphrase (Primary Language)**:
**Marriage** indicators differ by sex:

**For men** (observe Moon and Venus):
- Moon-Venus in mutual configuration = harmonious marriage
- Fixed signs = one wife
- Bicorporeal/tropical signs = multiple marriages
- Saturn aspecting = elderly wife
- Jupiter aspecting = wealthy/noble wife
- Mars aspecting = bold/violent wife

**For women** (observe Sun and Mars):
- Sun-Mars harmonious = good husband
- Fixed signs = one husband
- Bicorporeal = multiple husbands
- Saturn aspecting = elderly husband
- Jupiter aspecting = dignified husband
- Venus aspecting = handsome husband

**Sexual morality** also judged from Venus-Mars configurations.

**Complete Chinese Interpretation (Secondary Language)**:
**婚姻**指标因性别而异：

**对于男性**（观察月亮和金星）：
- 月-金相互配置 = 和谐婚姻
- 固定星座 = 一妻
- 双体/回归星座 = 多婚
- 土星相位 = 年长妻子
- 木星相位 = 富贵妻子
- 火星相位 = 大胆/暴力妻子

**对于女性**（观察太阳和火星）：
- 日-火和谐 = 好丈夫
- 固定星座 = 一夫
- 双体 = 多夫
- 土星相位 = 年长丈夫
- 木星相位 = 尊贵丈夫
- 金星相位 = 英俊丈夫

**Core Points**:
- Men: Moon-Venus = marriage significators
- Women: Sun-Mars = marriage significators
- Fixed signs = one spouse; Bicorporeal = multiple
- Aspecting planets modify spouse's character
- Venus-Mars configurations = sexual morality

**Narrative Snippets**:
- `[ns_tetra_iv007]` `[trigger: marriage_men]` `[factor_trigger: astro_moon_venus]` `[role: 主干]` For men, marriage is judged from Moon and Venus—their configuration shows marital harmony. → Source Text IV.5
- `[ns_tetra_iv008]` `[trigger: marriage_women]` `[factor_trigger: astro_sun_mars]` `[role: 条件分支]` For women, marriage is judged from Sun and Mars—their configuration shows husband's character. → Source Text IV.5
- `[ns_tetra_iv018]` `[trigger: marriage_number]` `[factor_trigger: astro_sign_fixed AND astro_sign_bicorporeal]` `[role: 条件分支]` Fixed signs = one spouse; bicorporeal or tropical signs = multiple marriages. → Number
- `[ns_tetra_iv019]` `[trigger: spouse_character]` `[factor_trigger: astro_saturn AND astro_jupiter AND astro_mars]` `[role: 条件分支]` Saturn aspect = elderly spouse; Jupiter = wealthy/noble; Mars = bold/violent. → Character
- `[ns_tetra_iv_sf]` `[trigger: spouse_female]` `[factor_trigger: spouse_female]` `[role: 效果]` Wife characteristics (for male natives) judged from Moon and Venus: their sign, aspects, and planetary configurations describe her nature. → Source Text IV.5
- `[ns_tetra_iv_sm2]` `[trigger: spouse_male]` `[factor_trigger: spouse_male]` `[role: 效果]` Husband characteristics (for female natives) judged from Sun and Mars: their sign, aspects, and planetary configurations describe his nature. → Source Text IV.5"""
    normalized_text_zh: str = """"""
    subject: str = "Marriage (Chapter V)"
    factor_refs: list = ['marriage_sig', 'new_candidate']
    
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
        l1_anchor="tb_v1.0.0_marriage__chapter_v_001_L1",
    )
    version: str = "1.0.0"
