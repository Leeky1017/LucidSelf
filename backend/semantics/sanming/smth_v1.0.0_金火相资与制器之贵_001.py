"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458299
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
    semantic_id="smth_v1.0.0_金火相资与制器之贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 金火相资与制器之贵(SemanticEntry):
    """
    - **原文（source_text）**：
  经云：金无火制，器难成。如乙巳、辛巳、庚午、辛巳，庚坐午，入火乡官贵之地。喜生四月，逢生天干二辛相比，地支巳午纯火，金生火旺，两各有气，故贵。又云：金...
    """
    
    original_text: str = """- **原文（source_text）**：
  经云：金无火制，器难成。如乙巳、辛巳、庚午、辛巳，庚坐午，入火乡官贵之地。喜生四月，逢生天干二辛相比，地支巳午纯火，金生火旺，两各有气，故贵。又云：金鬼无偏，以金须要火，而金相当，如两火两金，各居生旺，尤妙。

- 分字分词释义：
  - **金无火制，器难成**：金属若无火锻炼，难以铸成器物，比喻金气之人需经火之锻炼、磨砺方成大器。
  - **庚坐午，入火乡官贵之地**：庚金日主坐午火，午为火旺之乡，庚金在此一方面受制，一方面亦借火势显其光辉，多主官贵。
  - **两各有气**：金、火两者各自得地有气，既不偏枯，也不互相毁伤，为相成之象。
  - **金鬼无偏**：金为杀伐之神，"金鬼"指金之煞气；"无偏"意为不过分偏激，有火制炼则不至滥杀。
  - **两火两金，各居生旺**：金火数量与力量大致相当，且各在生旺之地，构成均衡而有力的结构。

- **规范化释义（primary_lang_explained）**：
  本节说明金日主与火之间相成的贵格。金若无火，则如未锻之矿石，难以成器；若金遇旺火，则可被炼成利器，同时也因火光而显其锋芒。以乙巳、辛巳、庚午、辛巳一造为例：庚金坐午火，入火旺之乡；又见辛金在天干比肩相助，地支巳午纯火，形成两火两金，各在生旺之地。金得火炼而不熔，火得金助而不虚，故能成就高贵之官职。

- **完整对等诠释（secondary_lang_full）**：
  The saying 'metal without fire to refine it cannot become a vessel' teaches that metal nature on its own is like unworked ore: hard but crude. When metal day-masters sit in strong fire, the flames temper them into useful tools and also light them up so their sharpness is seen. In the example with Yi-Si, Xin-Si, Geng-Wu and Xin-Si, Geng metal sits on Wu fire, entering a fiery land fit for noble office; above it, two Xin metals on the stems stand as peers, while below, Si and Wu form a pure fire field. Metal feeds the fire and fire in turn brings out the brilliance of metal; each has its own qi and neither is starved.
  The text further notes that the 'metal demon' is not biased or excessive when there is proper fire to discipline it, and that a layout with two fires and two metals each in prosperous positions is especially excellent. This is the essence of the Metal–Fire Mutual-Formation pattern: both metal and fire are strong, neither destroys the other, and together they symbolise positions of harsh judgment, reputation and heavy responsibility, such as military, judicial or supervisory roles where punishment and propriety must work hand in hand.


- 核心要点：
  - 金火相成格，重在**金火两旺而不相毁**，彼此制衡、相互成就。
  - 金象征决断、权威与刑罚，火象征光明、名声与热情，两者得当，多主带刑名、声望且权责重大的职位。
  - 忌一方过旺：火太甚则金熔为渣，主性急多灾；金太重则火光被遏，主刚愎伤人。

- 详细解说：
  在命理象义中，金火之配常出现在武职、司法、军警等领域：金为刑，火为礼；刑礼相资，方能既有威严又不失正当。本节所举命局中，庚金坐午火且再得辛金比肩，显示其本身刚劲而不折；巳午纯火又为之提供热度与舞台，使其锋芒得以展现。由于金火各在生旺之地，形成"两火两金"的均衡结构，故不致走向偏激，而能转化为贵格。
  
  实务中，如见金日主临火乡、再得同类金助与火局成势，而全局又无过重之水来熄火、无过重之土来埋金，多主以武职、司法、监察等需要严明与热度并行的岗位而贵显。若行运再助火金之旺而不失衡，则为发迹之期；若行运一味增火或增金，而缺少调剂，则需防官灾刑戮。

- 校勘与字词辨析：
  - 原文"金鬼无偏"一句，古本多作"金鬼须火"之类，今据文意与上下文"金须要火"相参，取其强调金煞需火炼而后可用之旨。
  - "两火两金，各居生旺"点明此格之要诀：数量相当、位置得宜，而非单纯金多或火多即可称为"金火相成"。
  - **English**：
    - Metal with abundant Fire can be called "Metal-Fire mutual completion."

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_044]` `[trigger: 金火制器]` `[factor_trigger: jinhuo_xiangcheng_presence]` `[role: 主干]` 金无火制，器难成。 → 《三命通会》卷五#金火相成
  - `[ns_smth_05_045]` `[trigger: 两火两金]` `[factor_trigger: liang_huo_liang_jin AND ge_ju_sheng_wang]` `[role: 主干依赖]` 两火两金，各居生旺，尤妙。 → 《三命通会》卷五#金火相成
  - `[ns_smth_05_046]` `[trigger: 锻炼成器]` `[factor_trigger: jin_de_huo_lian AND huo_de_jin_zhu]` `[role: 条件分支]` 金得火炼而不熔，火得金助而不虚，故能成就高贵之官职。 → 《三命通会》卷五#金火相成
  - `[ns_smth_05_047]` `[trigger: 刑礼相资]` `[factor_trigger: xing_li_xiangzi AND wei_yan_zheng_dang]` `[role: 总结]` 金为刑，火为礼；刑礼相资，方能既有威严又不失正当。 → 《三命通会》卷五#金火相成"""
    normalized_text_zh: str = """"""
    subject: str = "金火相资与制器之贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'jinhuo_xiangcheng_presence', 'bazi_semantic', 'jinhuo_shuliang_config', 'bazi_semantic', 'jinhuo_pingheng_score', 'bazi_semantic', 'duanlian_chengqi_score', 'bazi_semantic', 'xingli_xiangzi', 'bazi_semantic', 'guowang_shiheng_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_034', 'jinhuo_xiangcheng_presence', 'rel_smth_05_035', 'duanlian_chengqi_score', 'rel_smth_05_036', 'guowang_shiheng_risk', 'evi_smth_05_034', 'duanlian_chengqi_score', 'rule_jinhuo_cheng', 'evi_smth_05_035', 'jinhuo_shuliang_config', 'rule_junheng', 'evi_smth_05_036', 'jinhuo_pingheng_score', 'rule_youqi', 'map_smth_05_023', 'map_smth_05_024']
    
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
        l1_anchor="smth_v1.0.0_金火相资与制器之贵_001_L1",
    )
    version: str = "1.0.0"
