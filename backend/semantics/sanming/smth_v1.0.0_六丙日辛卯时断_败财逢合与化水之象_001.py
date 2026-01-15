"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157479
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
    semantic_id="smth_v1.0.0_六丙日辛卯时断_败财逢合与化水之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日辛卯时断败财逢合与化水之象(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日辛卯时断。

  六丙日生时辛卯，旺木双妻为人巧；不旺化水死乡中，色欲随身多爱好。丙日辛卯时，败财逢合，丙日卯上沐浴，见辛合神。若身甚旺不得化者，只是...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日辛卯时断。

  六丙日生时辛卯，旺木双妻为人巧；不旺化水死乡中，色欲随身多爱好。丙日辛卯时，败财逢合，丙日卯上沐浴，见辛合神。若身甚旺不得化者，只是为人无礼而贪色欲，却好如身弱化水，卯上水死，秀而不实，为人惯巧虚诈。惟丙午、丙寅、春月生，身旺不化者，文贵显秀。

  丙子日辛卯时，子卯相刑，伤妻害子。年月同，主魁名，近侍之贵。寅、午、丑、戌、天干地支俱合者大贵。

  丙寅日辛卯时，无祖自立，有肢体疾。寅卯未子月，贵。余月平，岁运同。

  丙辰日辛卯时，生寅戌月，天月二德，高。巳月，行北方运，贵。酉丑亦贵。亥卯未，大贵。

  丙午日辛卯时，年月中得癸水官星去刃则吉。子月，伤克妻子，寅酉，性格刚强，不受击触，三四品贵。午戌，行东南运；卯月，行西北运，俱贵。

  丙申日辛卯时滞，主聪明好酒色，身旺不化者贵。春吉。冬，行北运，富贵双全。巳丑年月，行东运，二品，午未三品。

  丙戌日辛卯时，伤妻害子，身旺不化者贵。春，聪明好酒色。冬，行西运，富贵。夏风宪。

  丙辛化水不相当，有助身强大吉昌；四柱若逢冲克破，劳心劳力过时光。丙日时逢辛卯，贪财坏印难成。财官运步显名声，身弱性情不定。父母六亲难靠，挺身改祖方成。雁行各自望前程，有破如常之命。

- 分字分词释义：

  - **败财逢合**：丙火在卯为沐浴（败地），见辛金偏财来合。
  - **丙辛化水**：丙火与辛金合化为水，若化成则改变命局性质。
  - **贪色欲**：沐浴主桃花，丙辛合又主情感，故有贪色之象。
  - **秀而不实**：表面聪明秀丽，但缺乏实际成就。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，辛卯时」：

  - 丙火在卯为沐浴之地，见辛金偏财来合，形成「败财逢合」之象；
  - 若身旺不化，则只是贪色欲、无礼节；若身弱化水，卯上水死，则秀而不实；
  - 唯有丙午、丙寅日或春月生，身旺不化者，方能文贵显秀。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Xin-Mao Hour":

  - Bing Fire at Mao is at bathing (decline) position, meeting Xin Metal (Indirect Wealth) in combination, forming "declining wealth meets combination."
  - If body is strong without transformation, the person merely indulges in desires and lacks propriety; if body is weak and transforms to water, with water dead at Mao, the result is "elegant but unsubstantial."
  - Only Bing-Wu, Bing-Yin days or spring births with strong body not transforming can achieve literary nobility and refinement.

- 核心要点：

  - 本格以「败财逢合」为核心，结构复杂。
  - 化与不化是关键：身旺不化可贵，身弱化水则虚。
  - 需防贪色欲、性情不定等问题。

- 详细解说：

  1. **败财逢合的特点**  
     - 卯为丙火沐浴，主桃花与情感；  
     - 辛金偏财来合，财与情感交织。

  2. **化水的利弊**  
     - 丙辛合化为水，若化成则命局性质改变；  
     - 卯上水死，化水者秀而不实，虚巧不实在。

  3. **身旺不化的优势**  
     - 若身旺不化，可用辛金为财；  
     - 形成「贪财」但有实力承担的结构，可显贵。

- 校勘与字词辨析：

  - 「旺木双妻」指情感关系复杂，可能有多段婚姻。
  - 「挺身改祖方成」指需要自立门户才能成就。
  - **English**：
    - Must establish own household to achieve success.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_109]` `[trigger: 败财逢合]` `[factor_trigger: baicai_fenghe AND shuangqi_weiren]` `[role: 主干]` 六丙日生时辛卯，旺木双妻为人巧。 → 《三命通会》卷八#六丙日辛卯时
  - `[ns_smth_08_110]` `[trigger: 丙辛化水]` `[factor_trigger: bingxin_huashui AND sixiang_zhong]` `[role: 主干依赖]` 不旺化水死乡中，色欲随身多爱好。 → 《三命通会》卷八#六丙日辛卯时
  - `[ns_smth_08_111]` `[trigger: 身旺不化]` `[factor_trigger: shenwang_buhua AND wengui_xianxiu]` `[role: 条件分支]` 惟丙午、丙寅、春月生，身旺不化者，文贵显秀。 → 《三命通会》卷八#六丙日辛卯时
  - `[ns_smth_08_112]` `[trigger: 改祖方成]` `[factor_trigger: gaizu_fangcheng AND yanxing_geji]` `[role: 总结]` 雁行各自望前程，挺身改祖方成。 → 《三命通会》卷八#六丙日辛卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日辛卯时断：败财逢合与化水之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_factor_171', 'bazi_semantic', 'bazi_state_bing_xin_water', 'bazi_semantic', 'bazi_state_factor_347', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_factor_50', 'bazi_semantic', 'source_ref', 'rel_smth_08_082', 'baicai_fenghe', 'rel_smth_08_083', 'bingxin_huashui', 'rel_smth_08_084', 'shenwang_buhua', 'evi_smth_08_082', 'baicai_fenghe', 'rule_baicai', 'evi_smth_08_083', 'bingxin_huashui', 'rule_huashui', 'evi_smth_08_084', 'xiu_er_bushi', 'rule_bushi', 'map_smth_08_055', 'map_smth_08_056']
    
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
        l1_anchor="smth_v1.0.0_六丙日辛卯时断_败财逢合与化水之象_001_L1",
    )
    version: str = "1.0.0"
