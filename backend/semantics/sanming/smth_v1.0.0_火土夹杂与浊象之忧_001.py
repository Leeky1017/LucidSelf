"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412918
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
    semantic_id="smth_v1.0.0_火土夹杂与浊象之忧_001",
    book_id="sanming",
    engine_id="bazi"
)
class 火土夹杂与浊象之忧(SemanticEntry):
    """
    - **原文（source_text）**：

  火见土则暗，土宿火则晦，故火自火，土自土，两不相掩为妙，若火土夹杂，主愚浊。经云：“火虚土聚成何用，定是尘埃碌碌人”是也。如：戊申、己未、丙午、乙未...
    """
    
    original_text: str = """- **原文（source_text）**：

  火见土则暗，土宿火则晦，故火自火，土自土，两不相掩为妙，若火土夹杂，主愚浊。经云：“火虚土聚成何用，定是尘埃碌碌人”是也。如：戊申、己未、丙午、乙未；庚戌、乙丑、丙辰、戊戌；戊戌、丁巳、己未、丙寅。三命皆火土夹杂，平常。

- 分字分词释义：

  - **火见土则暗，土宿火则晦**：火被厚土遮蔽则光明不彰，土被火气郁积则变得燥浊不清。
  - **火自火，土自土，两不相掩为妙**：火与土若各守其位、互不遮掩，则火可明、土可厚，各展其用。
  - **火土夹杂**：火土杂糅、互相牵扯，既使火光难明，又使土性不清，形成愚钝浑浊之象。
  - **尘埃碌碌人**：形容忙碌劳碌而难见高远之志，易陷于琐碎事务与世俗奔波。

- **规范化释义（primary_lang_explained）**：

  火土夹杂格，并非一类值得追求的格局，而是一种“光明被遮、厚土成浊”的状态。原文指出：火本主光明与热力，土本主厚重与承载；若火过多入土，土则燥而浑浊；若土过重压火，火则暗而不明。两者彼此牵扯不清时，往往表现为思维不够通透、眼界不够开阔，容易陷入日常琐事与现实压力中，难以见高远之成就。

  所列三造，多为火土互缠之例：既非极凶，亦难言大贵，故原文评为“平常”。这并非贬抑人生价值，而是强调此类结构若无其他格局提升，多主一生忙碌平凡，少有显赫之名。

- 核心要点：

  - 火土各守其位时可成佳局，过度夹杂则多浊少清。
  - 此象偏于“劳而不显”，除非有其他格局提携，否则难以论为上乘贵格。
  - 实务中宜慎用火、土为用神，更多依赖金水木等其他五行来疏导。

- 详细解说：

  从心理与人生体验看，火土夹杂者常呈现：热情有余而方向模糊，责任心重却易陷入琐事。火代表意愿与表达，土代表现实与责任；当火被土遮蔽时，人容易“心有不甘而无从施展”；当土被火炙烤时，人又容易“责任过重而心性烦躁”。

  若命局中另有清金、活水或生发之木介入，便有机会打破浊局：

  1. 金可砍伐燥木、斩断纠缠，使火土各归其位；
  2. 水可润土济火，使情绪柔和、思路清明；
  3. 木可引导火势向上生长，而非在土中郁积。若全局皆火土而少见他行，则多应“平常劳碌的人生图景”，宜在修身与见识上下功夫，减轻格局所带来的局限。

- **校勘与字词辨析（双语）**：

  - “火见土则暗，土宿火则晦”一句，本稿以“光明被遮蔽、土变燥浊”解释，不作抽象玄论。
  - “尘埃碌碌人”一语，本稿理解为命局偏向繁忙劳碌、难成大贵，而非否定人格或道德。
  - 所列三造命例，本稿不逐一拆解，仅以“火土偏重、清气不足”的共性概括。
  - **English**：
    - Common pattern of "insufficient clear qi" summarized.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_213]` `[trigger: 火土夹杂]` `[factor_trigger: huotu_jiaza AND yuzhu_zhi_xiang]` `[role: 主干]` 火见土则暗，土宿火则晦，故火自火，土自土，两不相掩为妙。 → 《三命通会》卷六#火土夹杂
  - `[ns_smth_06_214]` `[trigger: 浊象之忧]` `[factor_trigger: huotu_hun AND yuzhu]` `[role: 主干依赖]` 若火土夹杂，主愚浊。 → 《三命通会》卷六#火土夹杂
  - `[ns_smth_06_215]` `[trigger: 火虚土聚]` `[factor_trigger: huoxu_tuju AND wuyong]` `[role: 条件分支]` 火虚土聚成何用，定是尘埃碌碌人。 → 《三命通会》卷六#火土夹杂
  - `[ns_smth_06_216]` `[trigger: 平常之造]` `[factor_trigger: huotu_zahe AND pingchang]` `[role: 总结]` 三命皆火土夹杂，平常。 → 《三命通会》卷六#火土夹杂"""
    normalized_text_zh: str = """"""
    subject: str = "火土夹杂与浊象之忧"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_fire_earth_marker', 'bazi_semantic', 'bazi_structure_fire_earth_config', 'bazi_semantic', 'bazi_state_degree_37', 'bazi_semantic', 'bazi_state_factor_36', 'bazi_semantic', 'bazi_condition_fire_earth_5', 'bazi_semantic', 'bazi_condition_factor_216', 'bazi_semantic', 'source_ref', 'rel_smth_06_187', 'huotujiaza_presence', 'rel_smth_06_188', 'zhuoxiang_chengdu', 'rel_smth_06_189', 'huoan_tuhui_risk', 'evi_smth_06_187', 'huotujiaza_presence', 'rule_huotujiaza', 'evi_smth_06_188', 'zhuoxiang_chengdu', 'rule_wuyong', 'evi_smth_06_189', 'pingyong_lulu_risk', 'rule_lulu', 'map_smth_06_125', 'map_smth_06_126']
    
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
        l1_anchor="smth_v1.0.0_火土夹杂与浊象之忧_001_L1",
    )
    version: str = "1.0.0"
