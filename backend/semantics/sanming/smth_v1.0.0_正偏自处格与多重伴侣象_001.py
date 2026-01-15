"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436565
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
    semantic_id="smth_v1.0.0_正偏自处格与多重伴侣象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 正偏自处格与多重伴侣象(SemanticEntry):
    """
    - 原文（source_text）：

  正偏自处。

  夫正偏自处者何也？乃夫妇相合，复遇比肩分争。如一位夫星，有两位妻星相合，谓之争合。若本身自旺，彼身值衰，四柱不冲，则我正而彼偏矣。盖我生旺...
    """
    
    original_text: str = """- 原文（source_text）：

  正偏自处。

  夫正偏自处者何也？乃夫妇相合，复遇比肩分争。如一位夫星，有两位妻星相合，谓之争合。若本身自旺，彼身值衰，四柱不冲，则我正而彼偏矣。盖我生旺有气，则夫从我为正；我身衰而别位旺，则夫从别位，我反为偏，谓之彼旺争去我夫，我只得为偏。或自旺太过，柱无夫星者亦为偏；或官煞混杂，或伤官太重，亦为偏，更淫滥。如一命：壬子、丙午、辛酉、辛卯，辛用丙为夫星，我坐酉支，专禄自旺，虽时引辛卯之金，彼却无力，故我为正而彼为偏，此为二女争夫，正偏自处。又：癸未、壬戌、癸巳、壬子，癸用土为夫，癸巳水弱；壬子水旺，弱不能胜旺，被壬水争去戊土为正夫，乃彼胜我衰，我只得为偏。但壬水重而太泛，又带桃花，不能自处，余仿此推。

- 分字分词释义：

  - **正偏自处**：正妻与偏房之象并存，各自占有一部分夫星，古人以“正”“偏”名之。
  - **争合**：一位夫星与多位妻星相合，象征多重伴侣象之间的竞争。
  - **我正彼偏 / 彼旺争夫**：以我身旺衰与对方旺衰来判定哪一方在关系中占主位。
  - **官煞混杂、伤官太重，更淫滥**：夫星混乱或伤官过盛时，关系结构更为复杂。

- **规范化释义（primary_lang_explained）**：

  “正偏自处格”描述的是一种**存在多重伴侣象、关系位置有主有次**的结构：

  - 当我身旺而夫星更多与我一边相合时，我为正位，对方为偏位；
  - 当我身衰而另一方更旺时，则夫星被对方“争去”，我反为偏位；
  - 若官煞混杂、伤官太重，则关系更易演化为多角纠结。

- **完整对等诠释（secondary_lang_full）**：

  This pattern describes a situation in which more than one partner image appears in the chart, and the roles of "primary" and "secondary" are shaped by relative strength rather than moral labels. When the Day Master is strong and the spouse star leans more clearly toward the native's side, the native tends to occupy the central position in the partnership story, while other contenders remain on the margins. When another line is stronger, the spouse star may be "pulled away", leaving the native in a supporting or sidelined role.

  In modern terms, this can correspond to triangles or overlapping relationship fields: ex‑partners, current partners, family expectations and outside attractions all competing for attention. The chart does not command anyone to be a "proper" wife or a "lesser" partner; instead, it maps how energy, loyalty and resources tend to be distributed. For a contemporary reader, the teaching is to be clear about boundaries, self‑respect and choice: to recognise when one is being treated as secondary, and to decide consciously whether to stay, renegotiate, or leave.

- 核心要点：

  - 正偏之分，重在说明多重伴侣象中的重心，而非对人格作绝对评价。
  - 比肩、合冲、身旺衰等，共同决定“谁为主轴、谁为支线”。
  - 官煞混杂与伤官过重，会加剧关系的复杂度与不稳定性。

- 详细解说：

  1. **多重伴侣象的来源**  
     - 比肩、劫财与多位妻星同合一夫星，是“二女争夫”的象数学写；  
     - 在现实中，可以对应为前任、现任、家庭与外部关系之间的重叠与竞争。

  2. **身旺衰与位置感**  
     - 身旺者更容易在关系中占主导与主位，身衰者则易处于从属或边缘位置；  
     - 命局提示的，是关系中“资源与注意力如何分配”的结构，而非道德裁决。

  3. **现代转译**  
     - 与其执著于“正室 / 偏房”这样的旧称号，不如关注自己在关系中的边界、自尊与选择权；  
     - 当命局显出多重伴侣象时，越需要对承诺、沟通与诚实有更高要求，以避免伤害自己与他人.

- 校勘与字词辨析：

  - “二女争夫”“正偏”一类用语，本稿保留其结构意义，但在白话中以“主次位置与资源分配”来说明，不再沿用原有道德色彩.
  - 文中“壬水重而太泛，又带桃花，不能自处”，本稿理解为情感边界模糊、情绪容易泛滥，而非单纯的品行评价.
  - **English**：
    - Spirit-star (shensha) terms demystified; fortune cycle descriptions treated as developmental tendencies.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_065]` `[trigger: 正偏自处定义]` `[factor_trigger: zhengpian_zichu_ge]` `[role: 主干]` 正偏自处。 → 《三命通会》卷七#正偏自处
  - `[ns_smth_07_066]` `[trigger: 争合分位]` `[factor_trigger: fufu_xianghe AND bijian_fenzheng]` `[role: 主干依赖]` 夫妇相合，复遇比肩分争。如一位夫星，有两位妻星相合，谓之争合。 → 《三命通会》卷七#正偏自处
  - `[ns_smth_07_067]` `[trigger: 我正彼偏]` `[factor_trigger: wo_ziwang_bi_shuai]` `[role: 条件分支]` 若本身自旺，彼身值衰，四柱不冲，则我正而彼偏矣。 → 《三命通会》卷七#正偏自处
  - `[ns_smth_07_068]` `[trigger: 二女争夫]` `[factor_trigger: ernv_zhengfu]` `[role: 总结]` 此为二女争夫，正偏自处。 → 《三命通会》卷七#正偏自处"""
    normalized_text_zh: str = """"""
    subject: str = "正偏自处格与多重伴侣象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_relation', 'bazi_semantic', 'bazi_structure_factor_103', 'bazi_semantic', 'bazi_state_boundary', 'bazi_semantic', 'bazi_factor_14', 'bazi_semantic', 'source_ref', 'rel_smth_07_046', 'guanxi_zhuzhu', 'rel_smth_07_047', 'qinggan_bianjie', 'rel_smth_07_048', 'ziyuan_fenpei', 'evi_smth_07_046', 'guanxi_zhuzhu', 'rule_zhengpian', 'evi_smth_07_047', 'qinggan_bianjie', 'rule_wangqi', 'evi_smth_07_048', 'ziyuan_fenpei', 'rule_pianwei', 'map_smth_07_031', 'map_smth_07_032']
    
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
        l1_anchor="smth_v1.0.0_正偏自处格与多重伴侣象_001_L1",
    )
    version: str = "1.0.0"
