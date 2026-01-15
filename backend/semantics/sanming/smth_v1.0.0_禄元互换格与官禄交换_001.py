"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412465
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
    semantic_id="smth_v1.0.0_禄元互换格与官禄交换_001",
    book_id="sanming",
    engine_id="bazi"
)
class 禄元互换格与官禄交换(SemanticEntry):
    """
    - **原文（source_text）**：

  此格止有四日：戊申、丁酉、丙子、庚子。戊申日见乙卯时，戊取卯中乙木为官，乙取申中庚金为官，互换成其贵禄，柱中喜壬癸为财，生助乙木官星，运临官旺乡，便...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格止有四日：戊申、丁酉、丙子、庚子。戊申日见乙卯时，戊取卯中乙木为官，乙取申中庚金为官，互换成其贵禄，柱中喜壬癸为财，生助乙木官星，运临官旺乡，便是贵命，忌见甲煞、辛伤、寅酉冲。丁酉见壬寅，丙子见癸巳，庚子见丁亥，喜忌与前同推。如一命：癸亥、壬戌、丙子、癸巳，互换禄旺，各临官贵，无刑冲破害，故贵。又：己未、辛未、丙子、癸巳，合格，大贵。古法论禄元互换，如戊午见丁巳之例，是取临官之禄。

- 分字分词释义：

  - **禄元互换**：指日主与对方（多为他干）互取对方所在支中的禄或官，形成一种“官禄互为对方根基”的结构。
  - **此格止有四日：戊申、丁酉、丙子、庚子**：限定四个日柱为本格基础日。
  - **戊取卯中乙木为官，乙取申中庚金为官**：举戊申日见乙卯的典型结构：戊以乙为官，而乙又以庚为官，二者互成官根。
  - **柱中喜壬癸为财，生助乙木官星**：借壬癸之水生乙木，使互换而来的官星更加有力。
  - **丁酉见壬寅、丙子见癸巳、庚子见丁亥**：分别为其他三日的对应“互换”组合，喜忌大体类同。
  - **古法论禄元互换，如戊午见丁巳之例，是取临官之禄**：说明此格可类推至“临官之禄”的互用，只是本段着重于四日之原型。

- **规范化释义（primary_lang_explained）**：

  禄元互换格，是一种“官禄彼此交换、互为根基”的格局。以戊申日见乙卯为例：戊土以卯中乙木为官，而乙木又以申中庚金为官，因此戊与乙之间，形成了一个“你以我为官、我以你为官”的环扣结构；再加上壬癸为财生助乙木官星，等于在互换之后，又为对方的官位提供了源源不绝的养分。

  原文指出，此格只取戊申、丁酉、丙子、庚子四日为正宗，分别配以乙卯、壬寅、癸巳、丁亥为互换之枢纽，余者类推而不列。命中若能成此格，又在岁运中行到官旺之地，并且不遭刑冲破害，则多主贵命；若反见甲煞、辛伤，或寅酉等冲击枢纽之支，则官禄之根被破，互换之局难以稳固，贵气便大打折扣。

- 核心要点：

  - 本格强调**日主与他干之间官禄互为根基**，构成一种“互相成就”的官禄结构。
  - 仅以戊申、丁酉、丙子、庚子四日为原型，各有对应的互换支干组合。
  - 需要财星（壬癸等）来生扶对方官星，使互换后的官禄不致空虚。
  - 怕刑冲破害及煞伤关键支干，一旦枢纽被冲断，则格局难以成立或难以久保。

- 详细解说：

  从命理结构上看，禄元互换格有两个显著特点：

  1. **关系性强**：不同于单一日主自取禄官的格局，此格的贵处在于“我以彼为官、彼以我为官”，更强调人与人、干与干之间的互动与互赖；
  2. **依赖枢纽稳定**：若支干之间的互换支点（如乙卯、壬寅、癸巳、丁亥）被刑冲破害，则“互为根基”的关系自然难以维持，官禄亦随之摇动。

  实务判断时，应重点考察三方面：

  - 一看互换链是否完整：日主与对方是否真正互取官禄；
  - 二看财星生扶是否得力：有无壬癸等财星来生对方之官，使互换的官禄有源可依；
  - 三看岁运是否维护或破坏枢纽：行官旺生扶之运，则官禄互换之象得以发挥；行刑冲煞重之运，则容易在权位、身份上发生较大波折。

- **校勘与字词辨析（双语）**：

  - 原文“戊取卯中乙木为官，乙取申中庚金为官，互换成其贵禄”一句，本稿在白话中展开为“官禄环扣”的结构，以便理解互换之意。
  - 文末“古法论禄元互换，如戊午见丁巳之例，是取临官之禄”一语，本稿理解为：可将“互换”思路推广至其他临官禄位，但本节只以四日为主干示例。
  - 若干命例（如癸亥、壬戌、丙子、癸巳等），本稿只在白话中概括其“互换禄旺、官贵并临”的共性，不逐一推演局势。
  - **English**：
    - The sentence "Wu takes Mao's Yi wood as official, Yi takes Shen's Geng metal as official, mutually exchanging to form noble salary" is expanded in vernacular as "official-salary interlocking" structure for understanding.
    - The example charts are summarized for their "mutual exchange of official-salary, complementary stem-branch positions" commonality without individual case analysis.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_085]` `[trigger: 禄元互换定义]` `[factor_trigger: luyuan_huhuan_presence]` `[role: 主干]` 此格止有四日：戊申、丁酉、丙子、庚子。 → 《三命通会》卷六#禄元互换
  - `[ns_smth_06_086]` `[trigger: 官禄环扣]` `[factor_trigger: wu_qu_yi_wei_guan AND yi_qu_geng_wei_guan]` `[role: 主干依赖]` 戊取卯中乙木为官，乙取申中庚金为官，互换成其贵禄。 → 《三命通会》卷六#禄元互换
  - `[ns_smth_06_087]` `[trigger: 喜财忌煞]` `[factor_trigger: xi_ren_gui_cai OR ji_jia_sha_xin_shang]` `[role: 条件分支]` 柱中喜壬癸为财，生助乙木官星，运临官旺乡，便是贵命，忌见甲煞、辛伤、寅酉冲。 → 《三命通会》卷六#禄元互换
  - `[ns_smth_06_088]` `[trigger: 无刑冲故贵]` `[factor_trigger: wu_xing_chong_po_hai]` `[role: 总结]` 互换禄旺，各临官贵，无刑冲破害，故贵。 → 《三命通会》卷六#禄元互换"""
    normalized_text_zh: str = """"""
    subject: str = "禄元互换格与官禄交换"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_21', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_factor_14', 'bazi_semantic', 'bazi_state_degree_4', 'bazi_semantic', 'bazi_condition_jia_xin', 'bazi_semantic', 'bazi_condition_yin_you', 'bazi_semantic', 'source_ref', 'rel_smth_06_064', 'luyuan_huhuan_presence', 'rel_smth_06_065', 'huhuan_lian_wanzheng', 'rel_smth_06_066', 'jiasha_xinshang_risk', 'evi_smth_06_064', 'luyuan_huhuan_presence', 'rule_huhuan', 'evi_smth_06_065', 'huhuan_lian_wanzheng', 'rule_huqu', 'evi_smth_06_066', 'jiasha_xinshang_risk', 'rule_shashang', 'map_smth_06_043', 'map_smth_06_044']
    
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
        l1_anchor="smth_v1.0.0_禄元互换格与官禄交换_001_L1",
    )
    version: str = "1.0.0"
