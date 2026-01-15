"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066745
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
    semantic_id="smth_v1.0.0_2_崇奇宝贵与神煞加临_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2崇奇宝贵与神煞加临(SemanticEntry):
    """
    - 原文（source_text）：
  崇为宝也，奇为贵也。将星扶德，天乙加临。本主休囚，行藏汨没。
  至若勾陈得位，不亏小信以成仁；真武当权，知是大才而分瑞。
  不仁不义，庚辛与甲乙交差；或是...
    """
    
    original_text: str = """- 原文（source_text）：
  崇为宝也，奇为贵也。将星扶德，天乙加临。本主休囚，行藏汨没。
  至若勾陈得位，不亏小信以成仁；真武当权，知是大才而分瑞。
  不仁不义，庚辛与甲乙交差；或是或非，壬癸与丙丁相畏。
  故有先贤谦己处俗，求仙崇释；则离宫修定，归道乃水府求玄。
  是知五行通道，取用多门。理于贤人，乱于不肖；成于妙用，败于不能。

- 分字分词释义：
  - **崇**：高尚、尊贵（年为尊）。
  - **奇**：三奇（乙丙丁、甲戊庚、壬癸辛）。
  - **将星**：月将，或三合将星。
  - **德**：天月二德。
  - **本主休囚**：本（年）主（日）处于死绝休囚之地。
  - **勾陈得位**：勾陈属土（戊己），得位指生于四季月或旺地，主信。
  - **真武当权**：真武属水（壬癸），当权指生于冬月，主智。
  - **交差**：金克木（庚辛克甲乙），仁义相损。
  - **相畏**：水克火（壬癸克丙丁），是非多端。

- **规范化释义（primary_lang_explained）**：
  崇高者为宝，奇特者为贵。若有将星扶持德神，天乙贵人加临，主大贵。但若本命（年）和日主（日）处于休囚之地，即使有神煞，也难免淹没不显。
  土（勾陈）得位，主信实仁厚；水（真武）当权，主才智祥瑞。
  金木相战（庚辛与甲乙交差），主不仁不义；水火相克（壬癸与丙丁相畏），主是非不断。
  所以古之先贤，有的谦己处俗，求仙礼佛。修定于离宫（心火），求玄于水府（肾水），皆是五行通道的妙用。
  五行之道，取用多门。贤人能理顺，不肖者致乱。成于妙用，败于无能。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Veneration-Wonder Precious-Noble and Spirit-Killings Adding-Approaching" from the Xiao-Xi Rhapsody:

  - Veneration为treasure, Wonder为noble. General-Star supports Virtue, Heavenly-Yi加临.
  - Root-Master rest-imprison, conduct-藏沉没.
  - Hook-Spread得位, not亏small信成仁; True-Warrior当权, know大才分瑞.
  - Not仁not义, Geng-Xin与Jia-Yi交差; or是or非, Ren-Gui与Bing-Ding相畏.
  - Key: Spirit-Killings need Five Elements prosperous support; Metal-Wood war indicates injustice; Water-Fire conflict indicates disputes.

- 核心要点：
  - **神煞与五行**：神煞虽好，需五行生旺。
  - **水土得地**：主信主智。
  - **金木水火相战**：主性格缺陷或是非。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_025]` `[trigger: 崇奇贵宝]` `[factor_trigger: chongqi_guibao AND jianxing_fude AND tianyi_jialing]` `[role: 主干]` 崇为宝也，奇为贵也。将星扶德，天乙加临。 → 《三命通会》卷十一#崇奇宝贵与神煞加临
  - `[ns_smth_11_026]` `[trigger: 本主休囚]` `[factor_trigger: benzhu_xiuqiu AND xingcang_mimo]` `[role: 主干依赖]` 本主休囚，行藏汨没。 → 《三命通会》卷十一#崇奇宝贵与神煞加临
  - `[ns_smth_11_027]` `[trigger: 勾陈真武]` `[factor_trigger: gouchen_dewei AND zhenwu_dangquan]` `[role: 条件分支]` 勾陈得位，不亏小信以成仁；真武当权，知是大才而分瑞。 → 《三命通会》卷十一#崇奇宝贵与神煞加临
  - `[ns_smth_11_028]` `[trigger: 金木交差]` `[factor_trigger: jinmu_jiaocha AND shuihuo_xiangwei]` `[role: 条件分支]` 不仁不义，庚辛与甲乙交差；或是或非，壬癸与丙丁相畏。 → 《三命通会》卷十一#崇奇宝贵与神煞加临
  - `[ns_smth_11_029]` `[trigger: 五行通道]` `[factor_trigger: wuxing_tongdao AND quyong_duomen]` `[role: 总结]` 是知五行通道，取用多门。理于贤人，乱于不肖；成于妙用，败于不能。 → 《三命通会》卷十一#崇奇宝贵与神煞加临"""
    normalized_text_zh: str = """"""
    subject: str = "2 崇奇宝贵与神煞加临"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_16', 'bazi_semantic', 'bazi_state_factor_61', 'bazi_semantic', 'bazi_state_factor_62', 'bazi_semantic', 'bazi_state_factor_63', 'bazi_semantic', 'bazi_relation_metal_wood', 'bazi_semantic', 'bazi_relation_water_fire', 'bazi_semantic', 'source_ref', 'rel_smth_11_025', 'wuxing_ciming', 'rel_smth_11_026', 'jinmu_jiaocha', 'rel_smth_11_027', 'shuihuo_xiangwei', 'evi_smth_11_025', 'zhenwu_dangquan', 'rule_zhenwu_dangquan1', 'evi_smth_11_026', 'jinmu_jiaocha', 'rule_jinmu_jiaocha1', 'evi_smth_11_027', 'shuihuo_xiangwei', 'rule_shuihuo_xiangwei1', 'map_smth_11_017', 'map_smth_11_018']
    
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
        l1_anchor="smth_v1.0.0_2_崇奇宝贵与神煞加临_001_L1",
    )
    version: str = "1.0.0"
