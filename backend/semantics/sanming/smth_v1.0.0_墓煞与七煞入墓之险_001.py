"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412932
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
    semantic_id="smth_v1.0.0_墓煞与七煞入墓之险_001",
    book_id="sanming",
    engine_id="bazi"
)
class 墓煞与七煞入墓之险(SemanticEntry):
    """
    - **原文（source_text）**：

  古歌曰：墓中逢鬼要知之，夹煞持丘骨肉离，犯此凶星无救助，生来福寿少年亏。如甲日见庚戌、庚辰，乙日见辛丑、辛未，丙日见壬辰、壬戌，丁日见癸丑、癸未，戊...
    """
    
    original_text: str = """- **原文（source_text）**：

  古歌曰：墓中逢鬼要知之，夹煞持丘骨肉离，犯此凶星无救助，生来福寿少年亏。如甲日见庚戌、庚辰，乙日见辛丑、辛未，丙日见壬辰、壬戌，丁日见癸丑、癸未，戊日见甲辰、甲戌，己日见乙丑、乙未，庚日见丙辰、丙戌，辛日见丁丑、丁未，壬日见戊辰、戊戌，癸日见己丑、己未，此谓七煞入墓。《珞??录子》云：夹煞持丘，亲姻哭送。如己巳、戊辰、癸丑、丙辰，癸日见戊为官，己为煞，戊己并在辰上，又为癸水库，多主早发早夭。或曰：煞非止七煞，乃羊刃、亡、劫，与日时或日月夹藏墓中，皆凶。

- 分字分词释义：

  - **墓中逢鬼**：墓为库地，鬼指煞星，指煞星落于墓库之中，象征凶气深藏而难觉。
  - **夹煞持丘**：煞星在墓库两侧夹持，如同坟丘被凶气环绕，比单一煞更为险峻。
  - **七煞入墓**：以十干配十支之例，列举各日主遇特定地支时，七煞落于墓库之象。
  - **福寿少年亏**：指早年福寿多有损失，易见病损、灾祸或亲缘不全。
  - **煞非止七煞**：提醒羊刃、亡神、劫煞等若与日时或日月夹藏于墓中，同样为重凶之象。

- **规范化释义（primary_lang_explained）**：

  墓煞格，专论七煞等凶星落于墓库之地、且形成夹煞之象时的危险性。原文以“墓中逢鬼要知之，夹煞持丘骨肉离”警示：当煞星被墓库包裹或夹持时，凶性往往不在表面，而是潜伏于生命深处，一旦遇到岁运引发，容易出现骨肉分离、病灾意外等难以挽回的事件。

  列举的十日干配十地支之例，说明每一日主都有特定的“墓煞位置”；若命局中恰逢其位，再加上岁运引动，则风险加剧。经典又进一步指出，羊刃、亡神、劫煞等若夹藏于墓库中，同样可视作墓煞的一种变体，凶性更重。

- 核心要点：

  - 墓煞不在于“煞多”而在于“煞入墓、夹持成局”，主凶象潜伏而不易察觉。
  - 关键在岁运引动：原局虽险，若岁运不触发，则多为隐患；一旦引动，则应提防重大转折。
  - 实务中宜结合全局：若有印绶、生气、吉神化解，则可减轻其凶性；若全局本弱而煞重，则需加倍谨慎。

- 详细解说：

  墓煞的难处在于“藏而不显”：与明显的冲、刑不同，墓中煞多在命主感受中体现为压抑、郁结、反覆经历类似的考验，而在关键节点上爆发为实质事件（如病灾、亲缘破损、事业大挫等）。因此，判断墓煞不能只看某一条口诀，而应结合：

  1. 日主强弱与用神所系：若用神恰被墓煞所困，则凶性更大；
  2. 岁运是否冲开墓库或合动煞气；
  3. 命局中是否有印绶、比劫等力量来分解或承受冲击。若整体格局高、吉神有力，则墓煞未必致命，反而可能只表现为“在艰难中成事”的历练。

- **校勘与字词辨析（双语）**：

  - “夹煞持丘，亲姻哭送”之语，本稿在白话中仅以“骨肉分离、亲缘受损”的象意表述，不做具体事件的硬性预言。
  - 文中“煞非止七煞”一段，本稿视为对传统“只看七煞”的纠偏，强调诸煞夹藏皆需综合考量。
  - 原文命例如“己巳、戊辰、癸丑、丙辰”等，本稿不逐案拆解，仅以“早发早夭之象”点出风险类型。
  - **English**：
    - Risk type of "premature death imagery" identified.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_217]` `[trigger: 墓煚定义]` `[factor_trigger: musha_presence AND qisha_rumu]` `[role: 主干]` 墓中逢鬼要知之，夹煚持丘骨肉离。 → 《三命通会》卷六#墓煚
  - `[ns_smth_06_218]` `[trigger: 七煚入墓]` `[factor_trigger: qisha_rumu AND fushou_shaonian_kui]` `[role: 主干依赖]` 此谓七煚入墓，多主早发早夭。 → 《三命通会》卷六#墓煚
  - `[ns_smth_06_219]` `[trigger: 夹煚持丘]` `[factor_trigger: jiasha_chiqiu AND qinyin_kusong]` `[role: 条件分支]` 夹煚持丘，亲姻哭送。 → 《三命通会》卷六#墓煚
  - `[ns_smth_06_220]` `[trigger: 诸煚皆凶]` `[factor_trigger: sha_fei_zhiqisha AND jiecang_jiexiong]` `[role: 总结]` 煚非止七煚，乃羊刃、亡、劫，与日时或日月夹藏墓中，皆凶。 → 《三命通会》卷六#墓煚"""
    normalized_text_zh: str = """"""
    subject: str = "墓煞与七煞入墓之险"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_49', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_38', 'bazi_semantic', 'bazi_state_degree_39', 'bazi_semantic', 'bazi_condition_factor_217', 'bazi_semantic', 'bazi_condition_li', 'bazi_semantic', 'source_ref', 'rel_smth_06_190', 'musha_ge_presence', 'rel_smth_06_191', 'rumu_chengdu', 'rel_smth_06_192', 'zaoyao_risk', 'evi_smth_06_190', 'musha_ge_presence', 'rule_musha', 'evi_smth_06_191', 'xiongxian_chengdu', 'rule_jiasha', 'evi_smth_06_192', 'zaoyao_risk', 'rule_shaonian', 'map_smth_06_127', 'map_smth_06_128']
    
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
        l1_anchor="smth_v1.0.0_墓煞与七煞入墓之险_001_L1",
    )
    version: str = "1.0.0"
