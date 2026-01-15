"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436480
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
    semantic_id="smth_v1.0.0_淫格与夫星明暗交集之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 淫格与夫星明暗交集之象(SemanticEntry):
    """
    - 原文（source_text）：

  淫者沃也。乃本身得地，夫星明暗交集。谓日干自旺，柱中皆官煞是也。在干者为明，在支者为暗。四柱太过，如一丁见三壬及辰子多之例，谓之交集，于人无所不纳也。如戊辰...
    """
    
    original_text: str = """- 原文（source_text）：

  淫者沃也。乃本身得地，夫星明暗交集。谓日干自旺，柱中皆官煞是也。在干者为明，在支者为暗。四柱太过，如一丁见三壬及辰子多之例，谓之交集，于人无所不纳也。如戊辰、壬辰、壬戌、癸亥，壬辰、癸亥本自得地，明有戊土为正夫，暗有辰戌为偏夫。又庚戌、戊子、乙酉、甲申，乙以庚为明夫，而身坐酉支，时又引申为暗夫，运行西方金旺之地。二命俱夫星明暗交集，淫不可言。

- 分字分词释义：

  - **淫者沃也**：以“沃”喻水灌太过，言其情感与欲求的泛滥，而非单指性行为本身.
  - **本身得地**：日主自旺得地，有足够主动权与行动力.
  - **夫星明暗交集**：天干上有夫星（明夫），地支中又藏夫星（暗夫），且数量偏多，关系线索复杂.
  - **于人无所不纳**：古语夸张其广泛应对、多方接纳之象，带有明显批评意味.

- **规范化释义（primary_lang_explained）**：

  “淫格”并非单指行为放纵，而是指一种**夫星过多、明暗交错而自身又极旺**的结构：

  - 命主自身力量充足，主观能动强；
  - 命局中夫星遍布干支，既有公开的伴侣象，也有隐性的情感牵连；
  - 当行运再激活这些夫星时，容易在人际与情感上形成“多方纠缠”的局面.

- 核心要点：

  - 夫星明暗交集，是淫格的关键结构特征.
  - 身旺得地，使命主在这些关系中通常处于主动方.
  - 过多的伴侣象意味着情感焦点难以集中，关系边界易模糊.

- 详细解说：

  1. **明夫与暗夫**  
     - 明夫：天干上透出的官煞，象征公开承认或社会可见的伴侣关系；  
     - 暗夫：地支中所藏的官煞，象征隐性的情感牵连、旧情或不易公开之关系；  
     - 当二者数量过多、彼此交错时，命主在情感生活中的牵扯面自然扩大.

  2. **身旺与“沃”之比喻**  
     - “沃”强调灌注过多，隐喻感情投入、注意力与欲求的泛滥；  
     - 日主得地身旺，意味着命主有能力主动展开并维系多重关系，这既是能力，也是风险.

  3. **现代应用上的转化**  
     - 与其将“淫格”理解为道德谴责，不如视作对“关系过多、边界不清”的结构警示；  
     - 当命局呈现大量夫星时，更需要有意识地澄清承诺、避免暧昧与交叉伤害.

 - 校勘与字词辨析：

  - “淫不可言”并非鼓励隐瞒，而是古书以夸张语气强调结构之极端，本稿在白话中仅保留其“关系纠缠严重”的含义.
  - “沃”字在此用为比喻，指水势过溢，本稿据此将“淫”理解为能量泛滥而非单一性行为标签.
  - **English**：
    - Spirit-star (shensha) terms demystified; fortune cycle descriptions treated as developmental tendencies.


- **完整对等诠释（secondary_lang_full）**：

  The "Overflowing Desire" pattern focuses on a configuration where the Day Master stands on solid ground and spouse stars crowd around from both the visible and hidden layers. Official and Killing stars appear openly on the stems and are also concealed in the branches, forming a web of potential partner indications. With such abundance of spouse qi, the native is naturally drawn into multiple relational channels, whether or not each one becomes a formal partnership.

  In the examples, the Day Master has strong roots and favourable positions, while one set of spouse stars shows up as "bright" partners on the stems and another set as "dark" partners in the branches. When later luck cycles hit the directions where these stars gather – such as the western Metal phases – the entire spouse network can be activated at once. The ancient phrase that she "accepts all without refusal" is not a literal prescription, but an attempt to capture the breadth and fluidity of her relational field.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_037]` `[trigger: 淫格定义]` `[factor_trigger: yin_ge_wo]` `[role: 主干]` 淫者沃也。 → 《三命通会》卷七#淫格
  - `[ns_smth_07_038]` `[trigger: 夫星明暗]` `[factor_trigger: ben_shen_dedi AND fuxing_mingan_jiaoii]` `[role: 主干依赖]` 乃本身得地，夫星明暗交集。 → 《三命通会》卷七#淫格
  - `[ns_smth_07_039]` `[trigger: 明暗之分]` `[factor_trigger: zai_gan_wei_ming AND zai_zhi_wei_an]` `[role: 条件分支]` 在干者为明，在支者为暗。四柱太过，谓之交集，于人无所不纳也。 → 《三命通会》卷七#淫格
  - `[ns_smth_07_040]` `[trigger: 淫不可言]` `[factor_trigger: yin_buke_yan]` `[role: 总结]` 二命俱夫星明暗交集，淫不可言。 → 《三命通会》卷七#淫格"""
    normalized_text_zh: str = """"""
    subject: str = "淫格与夫星明暗交集之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_98', 'bazi_semantic', 'bazi_structure_interaction', 'bazi_semantic', 'bazi_state_relation_boundary', 'bazi_semantic', 'bazi_water', 'bazi_semantic', 'source_ref', 'rel_smth_07_025', 'mingan_fuxing', 'rel_smth_07_026', 'fuxing_hudong', 'rel_smth_07_027', 'duochong_banlu', 'evi_smth_07_025', 'mingan_fuxing', 'rule_yinge', 'evi_smth_07_026', 'fuxing_hudong', 'rule_taiguo', 'evi_smth_07_027', 'duochong_banlu', 'rule_duochong', 'map_smth_07_017', 'map_smth_07_018']
    
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
        l1_anchor="smth_v1.0.0_淫格与夫星明暗交集之象_001_L1",
    )
    version: str = "1.0.0"
