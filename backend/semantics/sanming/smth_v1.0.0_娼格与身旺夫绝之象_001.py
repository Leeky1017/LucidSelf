"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436469
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
    semantic_id="smth_v1.0.0_娼格与身旺夫绝之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 娼格与身旺夫绝之象(SemanticEntry):
    """
    - 原文（source_text）：

  娼者妓也。乃身旺夫绝，官衰食盛，或柱中不见官煞，或有而伤官伤尽，或官煞混乱而食神盛旺，此必娼妓之命，否则，为师尼婢妾，克夫淫奔。如丁亥、庚戌、戊辰、庚申，戊...
    """
    
    original_text: str = """- 原文（source_text）：

  娼者妓也。乃身旺夫绝，官衰食盛，或柱中不见官煞，或有而伤官伤尽，或官煞混乱而食神盛旺，此必娼妓之命，否则，为师尼婢妾，克夫淫奔。如丁亥、庚戌、戊辰、庚申，戊以甲为夫，九月失时无气，又被庚克绝，时引入申以庚为食，建禄在申。戊辰魁罡，生申太旺，亥中壬财亦旺，谓之身旺逢生，贪食贪财，夫绝而为秀丽娼也。

- 分字分词释义：

  - **身旺夫绝，官衰食盛**：日主极旺而夫星受损，官星衰微，食神反而强盛，象征自我意志与欲望远强于对伴侣关系的维系。
  - **不见官煞 / 伤官伤尽**：柱中完全不见官煞，或虽有官星却被伤官克尽，皆主夫象难立。
  - **官煞混乱而食神盛旺**：夫星混乱、难以稳定，而个人欲求与享乐倾向强烈。
  - **身旺逢生，贪食贪财，夫绝**：身旺又逢生扶，食神与财星助长个人追求，使夫星难以维系。

- **规范化释义（primary_lang_explained）**：

  “娼格”描述的是一种**自我与欲望极强，而伴侣星极弱甚至中断的结构**：

  - 命主自身力量与欲求旺盛，人生重心更多放在自我实现、享受与物质上；
  - 夫星要么根本不立，要么立而反复受克，婚姻关系稳定性差；
  - 原例中戊土魁罡、庚金建禄、壬财旺，皆加强了“身旺逢生、贪食贪财”的格局，因此古书以“秀丽娼”之语形容其艳丽而多波折。

- 核心要点：

  - 身旺而夫星绝或极衰，是娼格的结构基点。
  - 食神、财星过盛，欲望与享受的动力盖过对稳定婚姻的坚持。
  - 现实中对应的是情感不易定型、关系模式频繁变动的一类命局。

- 详细解说：

  1. **自我力量与他者关系**  
     - 身旺配合魁罡、建禄等强势星曜，往往带来鲜明个性与主导欲；  
     - 若夫星又弱，容易在关系中“以自我为中心”，难以长期妥协与共建。

  2. **食神与享乐倾向**  
     - 食神盛多主享乐、表达、饮食与感官之欲，在女命中若与财星合流，则易追求物质与情感上的丰盛体验；  
     - 若缺乏责任感与边界意识，便可能演化为古书所批评的“娼妓”象.

  3. **现代重释**  
     - 对今人而言，更可将“娼格”视为对情感自由与强烈自我意识的一种描述；  
     - 关键不在于道德贴标签，而在于如何在尊重自我欲求的同时，兼顾安全、尊严与对他人的责任.

- **完整对等诠释（secondary_lang_full）**：

  The "Courtesan" pattern, in its original language, uses harsh labels to describe a structure where self-power and desire grow far stronger than the spouse star. The essence, however, is not morality but imbalance: the Day Master stands exceedingly strong, repeatedly nourished by further support, while the Officer that symbolises the partner is weak, cut off, or entirely absent. At the same time, Food God and Wealth are flourishing, channeling energy into enjoyment, expression, and personal gain rather than into sustaining a stable partnership.

  In the example, Wu Earth is born in the ninth lunar month, already off-season and further suppressed by Geng Metal, which is at its Lu in Shen. Wu sits on Chen with the powerful marker of Kui Gang, and is once more strengthened by the presence of strong Wealth in Hai. Geng in Shen acts as Food for Wu, giving drive toward sensuality, taste, and experience. Under such conditions the spouse star represented by Jia fails to stand, while the native's own will and appetites are repeatedly fueled. The old text calls this "a beautiful courtesan" to capture the combination of allure, charisma, and relationship instability.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_033]` `[trigger: 娼格定义]` `[factor_trigger: chang_ge_ji]` `[role: 主干]` 娼者妓也。 → 《三命通会》卷七#娼格
  - `[ns_smth_07_034]` `[trigger: 身旺夫绝]` `[factor_trigger: shen_wang_fu_jue AND guan_shuai_shi_sheng]` `[role: 主干依赖]` 乃身旺夫绝，官衰食盛。 → 《三命通会》卷七#娼格
  - `[ns_smth_07_035]` `[trigger: 伤官伤尽]` `[factor_trigger: bu_jian_guansha OR shangguan_shangjin]` `[role: 条件分支]` 或柱中不见官煞，或有而伤官伤尽，或官煞混乱而食神盛旺。 → 《三命通会》卷七#娼格
  - `[ns_smth_07_036]` `[trigger: 秀丽娼]` `[factor_trigger: tan_shi_tan_cai]` `[role: 总结]` 身旺逢生，贪食贪财，夫绝而为秀丽娼也。 → 《三命通会》卷七#娼格"""
    normalized_text_zh: str = """"""
    subject: str = "娼格与身旺夫绝之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_97', 'bazi_semantic', 'bazi_state_factor_352', 'bazi_semantic', 'bazi_state_relation_4', 'bazi_semantic', 'bazi_factor_10', 'bazi_semantic', 'source_ref', 'rel_smth_07_022', 'shenwang_fujue', 'rel_smth_07_023', 'ziwo_qudong', 'rel_smth_07_024', 'ziwo_daoxiang', 'evi_smth_07_022', 'shenwang_fujue', 'rule_changge', 'evi_smth_07_023', 'ziwo_qudong', 'rule_tanshi', 'evi_smth_07_024', 'ziwo_daoxiang', 'rule_shenwang', 'map_smth_07_015', 'map_smth_07_016']
    
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
        l1_anchor="smth_v1.0.0_娼格与身旺夫绝之象_001_L1",
    )
    version: str = "1.0.0"
