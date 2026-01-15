"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699965
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
    semantic_id="zw_v1.0.0_孤夭之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 孤夭之命(SemanticEntry):
    """
    - 分字分词释义：

  - **贪狼廉贞俱陷**：贪狼廉贞二星同时落陷，主星严重受损。
  - **又逢化忌**：主星再遭化忌，雪上加霜。
  - **天魁坐长生亦无用**：虽有贵人坐长生位，但无力...
    """
    
    original_text: str = """- 分字分词释义：

  - **贪狼廉贞俱陷**：贪狼廉贞二星同时落陷，主星严重受损。
  - **又逢化忌**：主星再遭化忌，雪上加霜。
  - **天魁坐长生亦无用**：虽有贵人坐长生位，但无力救助。
  - **羊铃会合**：擎羊与铃星同时出现并会合于关键宫位。
  - **小限入绝地太岁在地网**：小限入绝地且太岁在地网，多重凶象叠加。
  - **狂邪之疾**：精神或神经系统方面的疾病。
  - **阳男木三局**：孤夭命盘的五行局数，木三局主生发受阻。

- **原文（source_text）**：  
  孤夭之命。阳男木三局。此命贪狼、廉贞二星俱陷，又逢化忌，虽有天魁贵人坐长生，亦无用也。三方四正俱见羊铃会合，廿九岁小限入于绝地，太岁又在地网，故得狂邪之疾而亡。

- **规范化释义（primary_lang_explained）**：  
  孤夭之命为阳男木三局，「贪狼、廉贞二星俱陷，又逢化忌」，说明两颗主星同时落陷并遭化忌，形成极为虚弱的命局核心。虽然「有天魁贵人坐长生」，看似有贵人相助且长生位置不差，但因主星过度受损，「亦无用也」，贵人之力无法扭转败局。更严重的是「三方四正俱见羊铃会合」，三方四正全被擎羊、铃星等凶星包围。原文点明应期：「廿九岁小限入于绝地，太岁又在地网」，二十九岁时多重凶象叠加，最终「得狂邪之疾而亡」。

- **完整对等诠释（secondary_lang_full）**：  
  This "Lonely and Short‑Lived" chart for a Yang Wood native has both Tan Lang and Lian Zhen fallen and afflicted by taboo transformation. Even Tian Kui the noble patron sitting at the Long Life position cannot rescue the situation—the core is too damaged. The tri‑palaces and four‑directional aspects are all besieged by Yang Blade and Ling Xing. At twenty‑nine, the minor period enters a wasteland sector while Tai Sui falls into the Earth Net. Under this convergence, the native succumbs to "kuang xie zhi ji"—a disease of madness.

- **核心要点**：  
  1. 贪狼廉贞俱陷并化忌，主星严重受损，命局核心虚弱。  
  2. 天魁坐长生但无力救助，贵人被主星的败局抵消。  
  3. 羊铃会合于三方四正，廿九岁小限入绝地且太岁在地网，终因狂邪之疾夭亡。"""
    normalized_text_zh: str = """"""
    subject: str = "孤夭之命"
    factor_refs: list = ['malefic_tanlian_juxian', 'malefic_you_feng_huaji', 'quality_tiankui_wuyong', 'malefic_yangling_hehe', 'timing_xiaoxian_juedi_taisui_diwang', 'affliction_kuangxie_zhiji']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_孤夭之命_001_L1",
    )
    version: str = "1.0.0"
