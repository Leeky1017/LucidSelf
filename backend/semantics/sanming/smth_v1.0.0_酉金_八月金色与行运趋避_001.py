"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042521
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
    semantic_id="smth_v1.0.0_酉金_八月金色与行运趋避_001",
    book_id="sanming",
    engine_id="bazi"
)
class 酉金八月金色与行运趋避(SemanticEntry):
    """
    - **原文（source_text）**：
  酉建八月金色，白水流清。若遇日时火多，运更愁东去；若遇日时水旺，运亦怕南行。柱见水泥，应为有用，运行西北，岂是无情？然逢己丑三合，亦能坚锐，岂可以阴金...
    """
    
    original_text: str = """- **原文（source_text）**：
  酉建八月金色，白水流清。若遇日时火多，运更愁东去；若遇日时水旺，运亦怕南行。柱见水泥，应为有用，运行西北，岂是无情？然逢己丑三合，亦能坚锐，岂可以阴金为温柔珠玉而泥论哉？

- **分字分词释义**：
  - **金色、白水流清**：秋金肃杀而水清凉，喻气象高洁。
  - **愁东去、怕南行**：金遇东方木、南方火之运，多成克战之象。
  - **水泥有用**：水土相杂为泥，可成就金之用处。

- **规范化释义（primary_lang_explained）**：
  酉为八月之金，色白而水清，有清肃之象。若日时火多，再行东方木或南方火之运，则金火交战，易生破耗；若日时水旺，再往南方火地，也多不利。柱中若见「水泥」之象（即水土相杂），未必是坏事，反能为金提供锻炼与立足之所；运行西北金水之地，也未必薄情无义。逢己丑三合金局，更能使酉金坚锐。作者提醒：不可一概将阴金视作温柔珠玉，而忽略其坚硬刚利的一面。

- **完整对等诠释（secondary_lang_full）**：
  You governs the eighth month, when Metal is pure and the waters run clear, giving a scene of cool clarity. As Yin Metal, it is often imagined as temple bells or fine instruments that require both structure and resonance. When the stems and branches are already heavy with Fire and the fortune cycles again move east or south, clashes between Metal and Wood–Fire bring repeated consumption and damage; when Water is abundant and cycles still go south, boiling and corrosion likewise harm the blade. The text notes that mixtures of Water and Earth—the so‑called “mud” structures—are not necessarily bad: in many charts they provide the matrix in which You Metal is set, supporting, polishing, and grounding it rather than simply dirtying it. Running toward the north‑west Metal–Water regions can, in such cases, strengthen standards, law, and precision rather than indicate coldness or ruthlessness. Combined with Ji Chou to form a strong Metal bureau, You becomes tougher and more incisive, showing that Yin Metal, though often stereotyped as gentle, can also be extremely sharp; the real question is whether its environment turns discipline into healthy standards or into endless conflict."""
    normalized_text_zh: str = """"""
    subject: str = "酉金：八月金色与行运趋避"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_you_presence', 'bazi_calculator', 'si_you_chou_combo', 'bazi_calculator', 'mao_you_chong', 'bazi_calculator', 'seasonal_phase', 'autumn', 'metal_fire_wood_balance', 'bazi_calculator', 'earth_platform_role', 'bazi_semantic', 'geng_xin_yun_flag', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_072', 'dizhi_you_presence', 'rel_smth_02_073', 'mao_you_chong', 'rel_smth_02_074', 'earth_platform_role', 'evi_smth_02_068', 'si_you_chou_combo', 'rule_si_you_chou_metal', 'evi_smth_02_069', 'earth_platform_role', 'rule_mud_support_you', 'evi_smth_02_070', 'metal_fire_wood_balance', 'rule_you_fear_east_south', 'map_smth_02_049', 'map_smth_02_050']
    
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
        l1_anchor="smth_v1.0.0_酉金_八月金色与行运趋避_001_L1",
    )
    version: str = "1.0.0"
