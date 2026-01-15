"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412993
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
    semantic_id="smth_v1.0.0_勾陈得位与土居中权衡_001",
    book_id="sanming",
    engine_id="bazi"
)
class 勾陈得位与土居中权衡(SemanticEntry):
    """
    - **原文（source_text）**：

  戊己土属中央，谓之勾陈当位，即当权之义。如戊寅、戊辰、戊子、戊申、乙卯、己亥、己未，皆坐下财官印，若身旺，官得时者贵，财得时者富，不见伤官劫财为妙，...
    """
    
    original_text: str = """- **原文（source_text）**：

  戊己土属中央，谓之勾陈当位，即当权之义。如戊寅、戊辰、戊子、戊申、乙卯、己亥、己未，皆坐下财官印，若身旺，官得时者贵，财得时者富，不见伤官劫财为妙，忌冲刑，煞旺生灾，岁运同。诗曰：戊己勾陈在旺乡，寅卯之宫号最强，若是更临辰卯未，亥子相逢大吉昌。又：日干戊己坐财官，号曰勾陈得位看，知有大财分瑞气，命中值此列朝班。

- 分字分词释义：

  - **戊己土属中央，谓之勾陈**：以戊己土喻中央勾陈之象，主守成、镇压与秩序维护。
  - **当位 / 当权**：土居中得位，掌管诸方，具有调和四方、承载百物之权。
  - **戊寅、戊辰、戊子、戊申、乙卯、己亥、己未**：列出勾陈得位的典型日柱，皆坐下有财官印三类之气。
  - **官得时者贵，财得时者富**：官星当令、得时则以贵显为主；财星得时、旺相则以富厚为主。
  - **不见伤官劫财为妙**：忌再见伤官、劫财来克制官星、分夺财星，以免破坏“居中而稳”的格局。
  - **忌冲刑，煞旺生灾**：土虽能承载，但过度的冲刑与煞气会撼动根基，易致灾祸。

- **规范化释义（primary_lang_explained）**：

  勾陈得位格，是以戊己土日坐财官印之地、且居中当权为核心的一类格局。戊己土象征居中之势：能载万物、能承压力、能调和四方。当日支又坐在寅、辰、子、申、卯、亥、未等财官印旺盛之地时，就好像勾陈位居中央，既能联通各方资源，又能承接权力与责任。

  原文指出：身旺而官得时者，多主贵显；身旺而财得时者，多主富足。若在这样的结构之上，又能避免伤官、劫财的过多干扰，则格局稳定而厚实，有利于“列朝班、分瑞气”。反之，若四柱冲刑太重、煞气过旺，则相当于在中央大地上挖坑、掀土，容易引发权位不稳、家业动摇等问题。

- 核心要点：

  - 以**戊己土日坐财官印之地**为本，强调土之居中、承载与调和功能。
  - 官得时者多贵，财得时者多富，关键在于“身旺能任其财官”。
  - 忌伤官、劫财与重煞冲刑破局，宜行有利于土之稳定与财官之和的运程。

- 详细解说：

  在四象体系中，勾陈与青龙、白虎、朱雀、玄武并列而偏重“中宫守成”的一端。若把青龙、白虎、朱雀、玄武看作四方之将，那么勾陈更类似“中军大帐”：不一定亲自冲锋，却决定全局节奏与资源配置。

  因此，勾陈得位格在现实中往往表现为：

  - 担当协调中枢、后勤枢纽、制度建设等职务的人物；
  - 善于整合资源、稳住局面，而非单点爆发型的先锋；
  - 发福多在中晚年，随着“土之沉淀”而渐厚，不一定少年显达。

- **校勘与字词辨析（双语）**：

  - 原文标题处“勾陈当位”与后文“勾陈得位”互见，本稿采用“勾陈得位”为节标题，以“得位”统摄“当位 / 当权”之意。
  - 日柱列表中“戊寅、戊辰、戊子、戊申、乙卯、己亥、己未”，本稿不作增减，仅在释义中说明其“皆坐下财官印”。
  - “号曰勾陈得位看，知有大财分瑞气，命中值此列朝班”一句，本稿在白话与核心要点中概括为“富贵并重、居中当班”，未逐句分译。
  - **English**：
    - Not translated sentence by sentence; key meaning preserved.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_241]` `[trigger: 勾陈得位]` `[factor_trigger: gouchen_dewei AND wuji_zhongyang]` `[role: 主干]` 戊己土属中央，谓之勾陈当位，即当权之义。 → 《三命通会》卷六#勾陈得位
  - `[ns_smth_06_242]` `[trigger: 坐下财官印]` `[factor_trigger: zuoxia_caiguanyin AND shenwang_guanfu]` `[role: 主干依赖]` 皆坐下财官印，若身旺，官得时者贵，财得时者富。 → 《三命通会》卷六#勾陈得位
  - `[ns_smth_06_243]` `[trigger: 忌伤官劫财]` `[factor_trigger: bujan_shangguan_jiecai AND wei_miao]` `[role: 条件分支]` 不见伤官劫财为妙。 → 《三命通会》卷六#勾陈得位
  - `[ns_smth_06_244]` `[trigger: 大财理气]` `[factor_trigger: dacai_fenruiqi AND lieban_chaoban]` `[role: 总结]` 知有大财分瑞气，命中值此列朝班。 → 《三命通会》卷六#勾陈得位"""
    normalized_text_zh: str = """"""
    subject: str = "勾陈得位与土居中权衡"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_85', 'bazi_semantic', 'bazi_condition_earth_4', 'bazi_semantic', 'bazi_state_earth_metal', 'bazi_semantic', 'source_ref', 'rel_smth_06_208', 'gouchendewei_presence', 'rel_smth_06_209', 'tujuzhong_quanheng', 'rel_smth_06_210', 'tuzhong_maijin', 'evi_smth_06_208', 'gouchendewei_presence', 'rule_gouchen', 'evi_smth_06_209', 'tuqi_dangling', 'rule_dangling', 'evi_smth_06_210', 'tuzhong_maijin', 'rule_maijin', 'map_smth_06_139', 'map_smth_06_140']
    
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
        l1_anchor="smth_v1.0.0_勾陈得位与土居中权衡_001_L1",
    )
    version: str = "1.0.0"
