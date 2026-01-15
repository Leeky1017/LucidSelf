"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.413011
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
    semantic_id="smth_v1.0.0_朱雀乘风与火势既济_001",
    book_id="sanming",
    engine_id="bazi"
)
class 朱雀乘风与火势既济(SemanticEntry):
    """
    - **原文（source_text）**：

  丙丁火属南方，谓之朱雀乘风，亦持势之义也。丙丁喜居金水之乡，身旺有托富贵。如丙子、丁亥，水火既济，又合胎元受气之贵，官旺财旺为上。丙丁有申子辰水局，...
    """
    
    original_text: str = """- **原文（source_text）**：

  丙丁火属南方，谓之朱雀乘风，亦持势之义也。丙丁喜居金水之乡，身旺有托富贵。如丙子、丁亥，水火既济，又合胎元受气之贵，官旺财旺为上。丙丁有申子辰水局，亦为既济。赋云：火旺得水，以成既济之功，须水火相停，不致偏枯方是。丙申、丙辰、丁酉、丁丑，得身有托，生气相扶，财官旺相，俱吉。有以丁未日时名朱雀折足，大不利六畜，亡散死伤，或患疮疾，有甲乙则有子孙。诗曰：朱雀乘风是丙丁，如逢金水便峥嵘，申子辰乡多贵达，逢时多殿玉阶行。

- 分字分词释义：

  - **丙丁火属南方，谓之朱雀**：以丙丁火喻南方朱雀之象，主光明、礼乐、文采、声名。
  - **乘风，亦持势之义**：火得风助而势旺，象征名声传播、影响扩散，与白虎“持势”相类而偏向文名一侧。
  - **丙丁喜居金水之乡**：火日若身旺而又居金水之地，一则火得金水调剂，不至燥烈；二则官财并得，利于名利双收。
  - **丙子、丁亥水火既济**：子、亥为水，丙丁为火，水火既济而不相害，且兼“胎元受气之贵”。
  - **申子辰水局亦为既济**：丙丁日若会成申子辰水局，在火旺有根的前提下，同样可成水火调匀之局。
  - **丁未日时名朱雀折足**：指丁未日时的一种偏凶象，原文主不利六畜、易有散亡伤病等事。

- **规范化释义（primary_lang_explained）**：

  朱雀乘风格，是以丙丁火日配合金水之乡、水火既济而“乘风持势”为核心的一类格局。丙丁火主光明与礼乐，象征人的表达、表现与外显的才情；当其日支或局中又有金水之地承托，尤其是丙子、丁亥一类“水火既济”的组合时，就好像朱雀得风而飞翔：一方面火得水济，不至燥烈自焚；另一方面水得火暖，化为蒸腾的气势，推动名利之成。

  原文强调：火旺得水，方成既济之功；若火有根而水相停，则官星、财星俱得其所，丙申、丙辰、丁酉、丁丑等日柱，只要“身有托、生气相扶”，财官旺相皆可视为吉象。但若如丁未日时之“朱雀折足”，则象征势头被折，一方面不利六畜家业，另一方面也提示命主需谨防疮疾、损伤等现实问题。

- 核心要点：

  - 以**丙丁火日 + 金水承托**为基础，关键在于火旺而不燥、得水而不熄。
  - 丙子、丁亥等“水火既济”日柱，为本格中最典型的贵象；申子辰水局亦可成局。
  - 财官旺相而身有托，则名利双收；若势旺而无托，或火、水失衡，则“乘风”易成“折足”。
  - 行运中宜再得金水调和，不宜火土过盛，以免火气过烈而伤身破局。

- 详细解说：

  若与白虎持势相比，朱雀乘风更偏重“声名与文彩”的一面：白虎主刚猛执权，朱雀则主表达、礼乐与对外影响力。丙丁火若单纯局限于火土之地，固然力量充沛，却容易局促于一隅；当其与金水之乡发生良性互动时，火的光明与水的流动结合起来，更容易体现在学业成绩、科举功名、仕途荣誉或公众声望等方面。

  实务判断中，要特别注意几点：

  1. 火是否真旺有根，而非虚火浮焰；
  2. 水是否能济火，而非泛滥成灾或被火尽数蒸干；
  3. 金是否作为官星、或借金生水，而不是单纯克木却无用；
  4. 行运是否延续“水火既济”的格局，抑或将其打破。原文以“朱雀折足”示警，提醒此格若行运不当或行为失度，很容易在看似高飞之时遭遇突然而至的折损。

- **校勘与字词辨析（双语）**：

  - 原文“丙丁火属南方，谓之朱雀乘风，亦持势之义也”一句，本稿在释义中将“乘风”解释为“火势得势而传播影响”，与白虎之“持势”并列。
  - “火旺得水，以成既济之功，须水火相停，不致偏枯方是”一语，本稿在白话中以“火旺而不燥、水济而不灭”的双重平衡来呈现。
  - 对“丁未日时名朱雀折足”的理解，本稿仅保留其“不利六畜、易有伤疾”的象征意义，不将其绝对化为定命断语。
  - **English**：
    - Not absolutized into fatalistic pronouncement.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_249]` `[trigger: 朱雀乘风]` `[factor_trigger: zhuque_chengfeng AND bingding_nanfang]` `[role: 主干]` 丙丁火属南方，谓之朱雀乘风，亦持势之义也。 → 《三命通会》卷六#朱雀乘风
  - `[ns_smth_06_250]` `[trigger: 水火既济]` `[factor_trigger: shuihuo_jiji AND taiyuan_shouqi]` `[role: 主干依赖]` 丙子、丁亥，水火既济，又合胎元受气之贵。 → 《三命通会》卷六#朱雀乘风
  - `[ns_smth_06_251]` `[trigger: 火旺得水]` `[factor_trigger: huowang_deshui AND jiji_zhigong]` `[role: 条件分支]` 火旺得水，以成既济之功，须水火相停。 → 《三命通会》卷六#朱雀乘风
  - `[ns_smth_06_252]` `[trigger: 多贵达]` `[factor_trigger: shenzichen_guida AND dianyu_jie_xing]` `[role: 总结]` 申子辰乡多贵达，逢时多殿玉阶行。 → 《三命通会》卷六#朱雀乘风"""
    normalized_text_zh: str = """"""
    subject: str = "朱雀乘风与火势既济"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_87', 'bazi_semantic', 'bazi_state_water_fire', 'bazi_semantic', 'bazi_state_factor_350', 'bazi_semantic', 'source_ref', 'rel_smth_06_214', 'zhuquechengfeng_presence', 'rel_smth_06_215', 'shuihuo_jiji', 'rel_smth_06_216', 'zhuque_zhezu', 'evi_smth_06_214', 'zhuquechengfeng_presence', 'rule_zhuque', 'evi_smth_06_215', 'shuihuo_jiji', 'rule_jiji', 'evi_smth_06_216', 'zhuque_zhezu', 'rule_zhezu', 'map_smth_06_143', 'map_smth_06_144']
    
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
        l1_anchor="smth_v1.0.0_朱雀乘风与火势既济_001_L1",
    )
    version: str = "1.0.0"
