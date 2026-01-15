"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042454
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
    semantic_id="smth_v1.0.0_卯木_仲春繁华与刑冲之机_001",
    book_id="sanming",
    engine_id="bazi"
)
class 卯木仲春繁华与刑冲之机(SemanticEntry):
    """
    - **原文（source_text）**：
  卯木仲春，气禀繁华，唱用金水，不可太过。若干头庚辛叠见，地支不可见申酉，恐有破伐之害；地支亥子重逢，干头不可见癸壬，主有漂流之伤。见酉则冲，木必落叶，...
    """
    
    original_text: str = """- **原文（source_text）**：
  卯木仲春，气禀繁华，唱用金水，不可太过。若干头庚辛叠见，地支不可见申酉，恐有破伐之害；地支亥子重逢，干头不可见癸壬，主有漂流之伤。见酉则冲，木必落叶，见亥未则合，木必成林。若时日归于金重，大运更向西行，患不禁也。

- **分字分词释义**：
  - **气禀繁华**：仲春万物盛长，枝叶繁茂之象。
  - **唱用金水，不可太过**：金以裁木，水以润木，然二者过重皆伤木。
  - **见酉则冲，见亥未则合**：冲则落叶，合则成林，喻木之盛衰。

- **规范化释义（primary_lang_explained）**：
  卯为仲春之木，枝叶繁华，本宜金来修整、水平滋润，但金水皆不可太过。若天干庚辛叠见，再逢申酉之地，便成重金砍伐，木难久存；若地支亥子重逢而天干癸壬又多，则水泛木浮，木根不固。见酉冲卯，如秋风落木；见亥未合，则如山林成片。若日时金重、大运又向西行，则金气过盛，卯木所受之克难以承受。

- **完整对等诠释（secondary_lang_full）**：
  Mao represents mid‑spring, when branches and leaves are at their lush peak. At this stage Wood welcomes both Metal and Water: Metal to prune and shape, Water to moisten and feed. Yet if Geng and Xin crowd the stems while Shen or You repeat in the Branches, pruning turns into heavy logging and the grove cannot endure; if Hai and Zi recur below while Gui and Ren dominate above, water becomes excessive, roots lose their grip, and "floating wood" appears. Mao meeting You is likened to an autumn wind that strips leaves, whereas combinations with Hai or Wei evoke whole hillsides turning into continuous forest. When the day and hour already carry much Metal and the fortune cycles again move toward the western Metal regions, the cutting force becomes more than Mao can bear. In practice this section reminds us that expansion and refinement must be balanced: Mao Wood thrives when structure and nourishment are present in measured amounts, and declines when so‑called "improvement" or resource inflow becomes an attack on its basic vitality."""
    normalized_text_zh: str = """"""
    subject: str = "卯木：仲春繁华与刑冲之机"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_mao_presence', 'bazi_calculator', 'hai_mao_wei_combo', 'bazi_calculator', 'mao_you_chong', 'bazi_calculator', 'seasonal_phase', 'spring', 'wood_metal_water_balance', 'bazi_calculator', 'jia_yi_spring_window', 'bazi_calculator', 'geng_xin_yun_flag', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_054', 'dizhi_mao_presence', 'rel_smth_02_055', 'dizhi_mao_presence', 'rel_smth_02_056', 'wood_metal_water_balance', 'evi_smth_02_050', 'hai_mao_wei_combo', 'rule_hai_mao_wei_wood', 'evi_smth_02_051', 'mao_you_chong', 'rule_mao_you_clash', 'evi_smth_02_052', 'geng_xin_yun_flag', 'rule_mao_metal_overload', 'map_smth_02_037', 'map_smth_02_038']
    
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
        l1_anchor="smth_v1.0.0_卯木_仲春繁华与刑冲之机_001_L1",
    )
    version: str = "1.0.0"
