"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412848
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
    semantic_id="smth_v1.0.0_稼穑与四季土之生养_001",
    book_id="sanming",
    engine_id="bazi"
)
class 稼穑与四季土之生养(SemanticEntry):
    """
    - **原文（source_text）**：

  赋云：戊己忻逢四季，乃为稼穑之名。是戊己生逢季月，喜见木为官，止得一木为妙，木多则土虚，主虚诈为破家不仁之人。辰未土聚之地，见巳午火即贵，亦不宜多，...
    """
    
    original_text: str = """- **原文（source_text）**：

  赋云：戊己忻逢四季，乃为稼穑之名。是戊己生逢季月，喜见木为官，止得一木为妙，木多则土虚，主虚诈为破家不仁之人。辰未土聚之地，见巳午火即贵，亦不宜多，多则土燥，不能滋生万物。丑戌之土，内怀金气，不宜重见，恐存煞气，不生万物，又不宜见金泄气，不贵。秋土不成器为死土，因土内含金，冬土不成器为泥土，因土内含水，故土只四季也。诗曰：戊己日生宜四季，多防丑戌坏金气，生来见木或逢荧，个中消息真荣贵。又：戊己生逢四月中，戊辰丑未要全逢，喜行财地嫌官煞，运到东方定有凶。

- 分字分词释义：

  - **稼穑**：原指播种与收获，引申为土能生养万物之功。
  - **戊己忻逢四季**：戊己土日若生于辰戌丑未等四季之月，土得其时，最能发挥生养功能。
  - **喜见木为官，止得一木为妙**：以木为官星，一木点睛，可成“木得其养”；木多则反损土气，变成虚诈、破家之象。
  - **辰未土聚之地，见巳午火即贵**：辰、未为土聚之所，若再得巳午火温养，则土能生发万物，易呈贵气。
  - **丑戌之土内怀金气，不宜重见**：丑、戌之土含金，重见则煞气偏重，难以生养万物。
  - **秋土为死土，冬土为泥土**：秋令土内含金，偏于收敛，不宜再负生养之任；冬令土内含水，偏于泥湿，亦难成器，故古人说“土只四季也”。

- **规范化释义（primary_lang_explained）**：

  稼穑格，主要讨论戊己土日在四季土月中的表现。戊己土本主承载与生养，当其生逢辰戌丑未等季月之时，就像农田正处于适宜耕作的季节：土气居中而稳，既能承受，又能孕育。如果再有一位木官星得其滋养，则如良田上植一棵好树，既成观，又成材。

  但原文亦多处设限：木多则土虚，象征过多的理想与要求反而掏空基础；辰未土聚之地见巳午火则贵，意味适量火气温暖土壤，有利作物生长；丑戌之土内怀金气，过多则煞重，既不利于生养，也不利于贵气的呈现。秋冬之土分别因内含金、水而偏向“死土”“泥土”，若仍以“稼穑”之土论之，则往往力不从心。

- 核心要点：

  - 以**戊己日 + 四季土月**为基础，强调土之“生养万物”之功。
  - 喜一木为官，以“木得其养”成贵；忌木多反虚土，或金气太重致煞。
  - 火宜温土而不宜过烈，秋冬之土若再负重任，多半难成器。

- 详细解说：

  可以把稼穑格理解为对“土之德”的细致分层：

  1. **时令之别**：同为戊己土，春夏多偏向生长与扩张，四季土则偏向成熟与收成，秋冬土则偏向收敛或泥滞；
  2. **方位之别**：辰未之土宜得火暖，丑戌之土却要防金气过重；
  3. **用神之别**：以木为官星，一则代表制度规范，一则代表成长方向；过多之木反而变成对土的掏空。

  在现实人生中，稼穑格往往对应那些擅长“打基础、做长期工程”的人：重视稳健、讲求循序渐进；若命局火木得宜，则有能力把基础土壤培育成高产良田；若煞气过重或木多土虚，则易见急功近利、虚张声势而难以善终的故事。

- **校勘与字词辨析（双语）**：

  - 原文“戊己忻逢四季，乃为稼穑之名”一句，本稿将“稼穑”概括为“土之生养职能”，并在白话中以“良田耕作”的比喻呈现。
  - “秋土不成器为死土”“冬土不成器为泥土”两句，本稿理解为对秋冬土功能有限的警示，并不作绝对否定土之价值。
  - 诗句中“多防丑戌坏金气”“喜行财地嫌官煞”等语，本稿分别归纳为“防金煞过重”“行财地而慎防官煞”的两类行运提示。
  - **English**：
    - Two categories of fortune-cycle guidance regarding official and seven-kill noted.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_193]` `[trigger: 稼穑定义]` `[factor_trigger: jiase_presence AND wuji_siji]` `[role: 主干]` 戊己忻逢四季，乃为稼穑之名。 → 《三命通会》卷六#稼穑
  - `[ns_smth_06_194]` `[trigger: 一木为官]` `[factor_trigger: xi_yimu AND muguan_weimiao]` `[role: 主干依赖]` 喜见木为官，止得一木为妙。 → 《三命通会》卷六#稼穑
  - `[ns_smth_06_195]` `[trigger: 木多土虚]` `[factor_trigger: mu_duo AND tu_xu]` `[role: 条件分支]` 木多则土虚，主虚诈为破家不仁之人。 → 《三命通会》卷六#稼穑
  - `[ns_smth_06_196]` `[trigger: 秋冬不成器]` `[factor_trigger: qiutu_situ AND dongtu_nitu]` `[role: 总结]` 秋土不成器为死土，冬土不成器为泥土，故土只四季也。 → 《三命通会》卷六#稼穑"""
    normalized_text_zh: str = """"""
    subject: str = "稼穑与四季土之生养"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_48', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_wood_2', 'bazi_semantic', 'bazi_state_earth_degree', 'bazi_semantic', 'bazi_condition_metal_6', 'bazi_semantic', 'bazi_condition_factor_211', 'bazi_semantic', 'source_ref', 'rel_smth_06_172', 'jiase_ge_presence', 'rel_smth_06_173', 'muguan_shiliangdu', 'rel_smth_06_174', 'jinsha_guozhong_risk', 'evi_smth_06_172', 'jiase_ge_presence', 'rule_jiase', 'evi_smth_06_173', 'muguan_shiliangdu', 'rule_yimu', 'evi_smth_06_174', 'tuqi_shengyang', 'rule_situ', 'map_smth_06_115', 'map_smth_06_116']
    
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
        l1_anchor="smth_v1.0.0_稼穑与四季土之生养_001_L1",
    )
    version: str = "1.0.0"
