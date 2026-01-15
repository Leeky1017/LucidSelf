"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042508
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
    semantic_id="smth_v1.0.0_申金_长生之地与火炼水淬_001",
    book_id="sanming",
    engine_id="bazi"
)
class 申金长生之地与火炼水淬(SemanticEntry):
    """
    - **原文（source_text）**：
  申宫水土长生之地，入巳、午则逢火炼，遂成剑戟，见子、辰则逢水淬，益得光锋；使木多无火，金终能胜，若土重堆埋，金却有凶。盖申乃顽钝之金，与温柔珠玉不同故...
    """
    
    original_text: str = """- **原文（source_text）**：
  申宫水土长生之地，入巳、午则逢火炼，遂成剑戟，见子、辰则逢水淬，益得光锋；使木多无火，金终能胜，若土重堆埋，金却有凶。盖申乃顽钝之金，与温柔珠玉不同故也。

- **分字分词释义**：
  - **水土长生之地**：申为壬水长生之所，又含土气，可育水金。
  - **火炼、水淬**：巳午之火炼金成器，子辰之水洗金增光。
  - **顽钝之金**：申金偏刚猛粗重，与酉中柔金不同。

- **规范化释义（primary_lang_explained）**：
  申地是壬水长生、金气渐盛之处，并含有一定土气。入巳午火乡，如炉中火炼，可使申金成为剑戟之器；见子辰水乡，则似以水淬火炼之后的金，锋芒更显。若木多而无火，金终能战胜木；若土重堆埋，则金被压制，反成凶象。作者特别指出申为顽钝之金，与酉中精细珠玉不同，需要火水适度锻炼与淬洗，方能成器。

- **完整对等诠释（secondary_lang_full）**：
  Shen is described as the place where Ren Water is born and Metal qi begins to take shape, mixed with a measure of Earth. Entering the fiery territories of Si and Wu is likened to being thrown into a furnace: here the coarse ore of Shen Metal can be smelted into swords and halberds. Meeting Zi or Chen brings the water‑tempering that follows forging, washing away impurities and sharpening the edge. If Wood is numerous yet no Fire is present, the text says Metal will eventually prevail, because its latent strength is great; but when heavy Earth piles over Shen, the Metal is buried and turns from potential tool into a source of misfortune. The author emphasises that Shen represents tough, stubborn Metal rather than the refined jewellery associated with You, and must be correctly treated with cycles of heating and quenching. In destiny analysis this pattern speaks to the making of execution power and hard discipline: it can produce a capable, resilient enforcer when Fire and Water are balanced, or a brutal, dulled instrument when buried under rigid structures or left untempered."""
    normalized_text_zh: str = """"""
    subject: str = "申金：长生之地与火炼水淬"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_shen_presence', 'bazi_calculator', 'shen_zi_chen_combo', 'bazi_calculator', 'si_you_chou_combo', 'bazi_calculator', 'seasonal_phase', 'autumn', 'metal_fire_water_earth_balance', 'bazi_calculator', 'water_role_on_metal', 'bazi_semantic', 'geng_xin_yun_flag', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_069', 'dizhi_shen_presence', 'rel_smth_02_070', 'dizhi_si_presence', 'rel_smth_02_071', 'water_role_on_metal', 'evi_smth_02_065', 'dizhi_si_presence', 'rule_fire_forge_shen', 'evi_smth_02_066', 'shen_zi_chen_combo', 'rule_water_temper_shen', 'evi_smth_02_067', 'metal_fire_water_earth_balance', 'rule_earth_bury_shen', 'map_smth_02_047', 'map_smth_02_048']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_申金_长生之地与火炼水淬_001_L1",
    )
    version: str = "1.0.0"
