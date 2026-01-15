"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412498
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
    semantic_id="smth_v1.0.0_倒冲禄与禄马反向飞出_001",
    book_id="sanming",
    engine_id="bazi"
)
class 倒冲禄与禄马反向飞出(SemanticEntry):
    """
    - **原文（source_text）**：

  倒冲禄：伤官月建，内有倒冲禄马格，喜忌与飞天同，惟时不论。此格止有二日：丙午、丁巳，夏日纯阳。丙以癸水为官，要柱中午多有力，冲出子中癸水，则丙日得官...
    """
    
    original_text: str = """- **原文（source_text）**：

  倒冲禄：伤官月建，内有倒冲禄马格，喜忌与飞天同，惟时不论。此格止有二日：丙午、丁巳，夏日纯阳。丙以癸水为官，要柱中午多有力，冲出子中癸水，则丙日得官星；丁以壬水为官，要柱中巳多有力，冲出亥中壬水，则丁日得官星。更得丑寅或申辰卯未，但有一字合住禄马为妙，多则不中。丙午日怕未，丁巳日怕申辰等字羁绊，则巳午贪合，不能冲子亥中之禄；柱有亥壬子癸为煞官显露，则减分数，岁运同。古歌云：丙日无官局午多，倒冲禄马癸官和，不逢未字来羁绊，癸子俱无福嵯峨。又：倒冲贵气不同伦，丙午飞冲子禄神，癸水克来是贵禄，刑伤填实是常人。又：倒冲禄马贵非常，丙日多逢午位良，七煞不逢并惹绊，白衣平步入朝堂。又：丁日蛇多是倒冲，官星飞起出干宫，柱不见亥壬字，辰不留蛇福贵隆。又：丁日冲官巳要强，亥为壬禄贵人乡，柱中不见辰壬癸，岁运相扶福禄昌。

- 分字分词释义：

  - **倒冲禄马格**：与飞天禄马相对，以日支本身为禄马之根，通过对宫之冲“倒着”把官禄从子、亥中冲出。
  - **伤官月建，喜忌与飞天同**：同样是在表面凶月中起贵，忌官星显露与过多羁绊。
  - **丙午、丁巳二日**：仅限两个日柱，且宜夏季纯阳之时，方显“倒冲”之力。
  - **午多有力冲子、巳多有力冲亥**：分别以午冲子、巳冲亥，引出子中癸水官星、亥中壬水官星。
  - **怕未、申辰等羁绊**：未合午、申辰合巳，都会使冲力被合住，禄马难以飞出。

- **规范化释义（primary_lang_explained）**：

  倒冲禄，与飞天禄马同属“冲出伏禄”的体系，只是路径相反：

  - 飞天禄马多以子、亥为冲神，去冲午、巳之禄；
  - 倒冲禄则以午、巳为冲神，去冲子、亥中所藏的官禄。

  丙午日以癸水为官；丁巳日以壬水为官。若命局在夏季火旺之时，午或巳多而有力，便可把子、亥中的癸、壬官星从伏藏状态冲出，使原本“无官”的日主得以骤然遇官。若同时有一支丑、寅、申、辰、卯、未等与禄马成合，又不至于过多，则既能收住官禄，又不妨冲力，格局尤高。

- 核心要点：

  - 倒冲禄与飞天禄马同理，皆属**冲出伏禄、以凶制凶成贵**之格。
  - 仅限丙午、丁巳二日，且以夏季火旺、午巳有力为前提。
  - 忌未、申辰等支过度合住午、巳，使之“贪合忘冲”；忌亥壬子癸等官煞显露。

- 详细解说：

  从结构上看，倒冲禄体现的是“以我之旺势，倒去冲出对宫之官”：

  1. 丙、丁在夏令自旺，午巳为其根基，气势集中；
  2. 子、亥中所藏癸、壬，本是官煞伏处，若不经冲击则难以为用；
  3. 当午、巳有力而无过度合绊时，便能“飞冲”子、亥，将癸、壬官气引出，化凶月为贵格。

  实际占用时，需要细看：

  - 原局身是否真旺，是否能承受飞出的官煞；
  - 冲出官星之后，是否另有财、印相配，以成稳固之官格；
  - 岁运是否帮助午巳有力，而非再度以合、刑、害削弱冲势。若条件不足，倒冲之象往往只剩“动荡与是非”，难成真正之贵。

- **校勘与字词辨析（双语）**：

  - “倒冲”一语，本稿理解为“由日支向对宫冲出禄马”，与飞天禄马“由对宫冲日支之禄”方向相反。
  - 古歌中“癸官和”“贵非常”等语，皆指官星被成功冲出、且不受破坏时的高格象意，本稿不做官阶细分。
  - 关于“丁未日时名朱雀折足”等说法，本节只取与倒冲禄相关之部分，其余关于火日格局的内容在前文“朱雀乘风”中另行展开。
  - **English**：
    - Cross-references to "Vermillion Bird Riding Wind" content are expanded separately in that earlier section.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_097]` `[trigger: 倒冲禄定义]` `[factor_trigger: daochong_lu_presence]` `[role: 主干]` 倒冲禄：伤官月建，内有倒冲禄马格，喜忌与飞天同，惟时不论。 → 《三命通会》卷六#倒冲禄
  - `[ns_smth_06_098]` `[trigger: 二日限定]` `[factor_trigger: daochong_erri]` `[role: 主干依赖]` 此格止有二日：丙午、丁巳，夏日纯阳。 → 《三命通会》卷六#倒冲禄
  - `[ns_smth_06_099]` `[trigger: 忌羁绊贪合]` `[factor_trigger: ji_jiban_tanhe]` `[role: 条件分支]` 丙午日怕未，丁巳日怕申辰等字羁绊，则巳午贪合，不能冲子亥中之禄。 → 《三命通会》卷六#倒冲禄
  - `[ns_smth_06_100]` `[trigger: 贵非常]` `[factor_trigger: gui_fei_chang]` `[role: 总结]` 倒冲禄马贵非常，丙日多逢午位良。 → 《三命通会》卷六#倒冲禄"""
    normalized_text_zh: str = """"""
    subject: str = "倒冲禄与禄马反向飞出"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_24', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_wu_si_degree', 'bazi_semantic', 'bazi_state_degree_7', 'bazi_semantic', 'bazi_condition_factor_163', 'bazi_semantic', 'bazi_condition_factor_164', 'bazi_semantic', 'source_ref', 'rel_smth_06_073', 'daochong_lu_presence', 'rel_smth_06_074', 'wusi_chongli_guanxing', 'rel_smth_06_075', 'guansha_xianlu_risk', 'evi_smth_06_073', 'daochong_lu_presence', 'rule_daochong', 'evi_smth_06_074', 'hezhu_luma_chengdu', 'rule_hezhu_dc', 'evi_smth_06_075', 'jiban_tanhe_risk', 'rule_tanhe', 'map_smth_06_049', 'map_smth_06_050']
    
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
        l1_anchor="smth_v1.0.0_倒冲禄与禄马反向飞出_001_L1",
    )
    version: str = "1.0.0"
