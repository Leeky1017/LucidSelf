"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436529
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
    semantic_id="smth_v1.0.0_安静守分格与夫妇齐稳_001",
    book_id="sanming",
    engine_id="bazi"
)
class 安静守分格与夫妇齐稳(SemanticEntry):
    """
    - 原文（source_text）：

  安静守分。

  安静守分，乃夫星有气，日干自旺，相停无克，不值刑冲，财食得所者是也。如一命：癸巳、庚申、乙卯、丁亥。乙坐卯，专禄自旺，又得时支亥字合局，是...
    """
    
    original_text: str = """- 原文（source_text）：

  安静守分。

  安静守分，乃夫星有气，日干自旺，相停无克，不值刑冲，财食得所者是也。如一命：癸巳、庚申、乙卯、丁亥。乙坐卯，专禄自旺，又得时支亥字合局，是本身旺也。以庚金为夫，七月庚禄得申，又得年支巳火为金长生之地，是夫星旺也。亥中壬水，夫之食神天厨，故主夫食天禄。此乃自己、夫星两不相伤，各乘旺气，无混乱相侵，夫妇偕和，安静守分格也。

- 分字分词释义：

  - **安静守分**：安于本位，各守其分，不越界、不争权，关系中少波折。
  - **夫星有气，日干自旺，相停无克**：命主与夫星皆得其气势，彼此力量相当而不相互克伐。
  - **不值刑冲，财食得所**：四柱少见刑冲破害，财星、食神各得其所，为家道提供稳定资源与生活品质。
  - **夫之食神天厨**：夫星之食神得地，有“天禄”之象，指饮食、物质供养稳定丰足。

- **规范化释义（primary_lang_explained）**：

  本节所言“安静守分格”，相对于前几格的偏激，强调的是一种**平稳、中和的婚姻结构**：

  - 命主自身与夫星皆得旺气，力量不失衡；
  - 四柱少有刑冲，财食得所，日常生活有稳定的物质基础；
  - 夫妇双方相互不伤，各守本分，能够长期维持和谐共处。

- **完整对等诠释（secondary_lang_full）**：

  This pattern describes a partnership in which both the Day Master and the spouse star stand on solid ground and do not attack each other. The chart shows few clashes or punishments, while Wealth and Food are well placed, so that daily life has a stable material base. Rather than dramatic rise and fall, the emphasis is on a steady rhythm of shared work, care and responsibility, where each person keeps to their role without withdrawing or over‑controlling.

  Compared with the more extreme structures in the surrounding sections, "Quietly Keeping One's Place" is less about dazzling success and more about long‑term reliability. For a modern reader, it points to relationships where safety, predictability and mutual support are valued as blessings in their own right. It encourages noticing the quiet strength of an ordinary, well‑run household in which both partners can breathe and stay.

- 核心要点：

  - 夫星与命主同旺而不相克，是安静守分格的骨架。
  - 财星、食神位置适当，使家庭在物质与日常生活层面有保障。
  - 少刑冲、少极端象，关系模式趋向温和稳定。

- 详细解说：

  1. **“安静”与“守分”的双重含义**  
     - 安静：关系中少大起大落与激烈冲突；  
     - 守分：各自承担相应责任，不轻易越界或逃避。

  2. **资源与责任的平衡**  
     - 夫星旺、食神得地，往往象征伴侣能在经济、生活照料上承担相应责任；  
     - 命主自身亦自旺，有能力在情感与事务上支撑家庭运作。

  3. **现代视角下的“好命”**  
     - 与其追求极端的“贵、显、奇”，不如把这种平稳、互相支持的结构视为一种可贵的福分；  
     - 对今人而言，“安静守分”更接近于在长期亲密关系中的安全感与共识感。

- 校勘与字词辨析：

  - 原文中“夫食天禄”等说法，本稿理解为物质与生活条件相对优渥，不作封爵层面的想象。
  - “安静守分格”在本稿中用来指代一种结构与关系模式，而非评价个人性格好坏。
  - **English**：
    - Expressive format; not evaluating personal character.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_053]` `[trigger: 安静守分定义]` `[factor_trigger: anjing_shoufen_ge]` `[role: 主干]` 安静守分。 → 《三命通会》卷七#安静守分
  - `[ns_smth_07_054]` `[trigger: 夫身同旺]` `[factor_trigger: fuxing_youqi AND rigan_ziwang]` `[role: 主干依赖]` 乃夫星有气，日干自旺，相停无克，不值刑冲，财食得所者是也。 → 《三命通会》卷七#安静守分
  - `[ns_smth_07_055]` `[trigger: 两不相伤]` `[factor_trigger: liang_bu_xiangshang AND wuhunluan]` `[role: 条件分支]` 此乃自己、夫星两不相伤，各乘旺气，无混乱相侵。 → 《三命通会》卷七#安静守分
  - `[ns_smth_07_056]` `[trigger: 夫妇偕和]` `[factor_trigger: fufu_xiehe]` `[role: 总结]` 夫妇偕和，安静守分格也。 → 《三命通会》卷七#安静守分"""
    normalized_text_zh: str = """"""
    subject: str = "安静守分格与夫妇齐稳"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_99', 'bazi_semantic', 'bazi_state_relation_5', 'bazi_semantic', 'bazi_state_factor_354', 'bazi_semantic', 'source_ref', 'rel_smth_07_037', 'fuxing_mingzhu_duibi', 'rel_smth_07_038', 'guanxi_bodong', 'rel_smth_07_039', 'wuzhi_wending', 'evi_smth_07_037', 'fuxing_mingzhu_duibi', 'rule_anjing', 'evi_smth_07_038', 'guanxi_bodong', 'rule_wuxingchong', 'evi_smth_07_039', 'wuzhi_wending', 'rule_xiehe', 'map_smth_07_025', 'map_smth_07_026']
    
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
        l1_anchor="smth_v1.0.0_安静守分格与夫妇齐稳_001_L1",
    )
    version: str = "1.0.0"
