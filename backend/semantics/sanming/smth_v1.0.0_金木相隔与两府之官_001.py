"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458275
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
    semantic_id="smth_v1.0.0_金木相隔与两府之官_001",
    book_id="sanming",
    engine_id="bazi"
)
class 金木相隔与两府之官(SemanticEntry):
    """
    - **原文（source_text）**：
  经云：木若逢金间隔，作两府之官。木无金，终不成器。如杨博尚书：己巳、庚午、乙卯、庚辰。乙坐卯自旺，生于午，得两庚间隔，成器，故贵极品。

- 分字分词...
    """
    
    original_text: str = """- **原文（source_text）**：
  经云：木若逢金间隔，作两府之官。木无金，终不成器。如杨博尚书：己巳、庚午、乙卯、庚辰。乙坐卯自旺，生于午，得两庚间隔，成器，故贵极品。

- 分字分词释义：
  - **金木间隔**：木日主或木局两旁有金星夹辅，如乙卯日两边见庚金，为"金木相隔"之象。
  - **两府之官**：两府本指中书、门下或文武两府，泛指朝廷中枢要职，此处用以形容官位之高。
  - **木无金，终不成器**：取木工制器之喻，木若无金斧斤之裁削，终难成器；喻木性之人需经金官之砥砺方成大器。
  - **得两庚间隔**：命局中两处庚金分别坐落于木日主两侧，既能制约木气，又不至于折伤，成"相隔而不相害"之妙局。

- **规范化释义（primary_lang_explained）**：
  本节说的是木日主两旁为金所夹的格局。经云"木若逢金间隔，作两府之官"，意思是木性日主若两边有金星夹辅，好比木材既有锐利金工具裁制，又不至于被砍折，可被雕琢成器，因此多主居中枢之高位。"木无金，终不成器"则从反面说明：若木气孤旺而无金来裁制，虽有生机，却难成栋梁。
  
  杨博尚书一命己巳、庚午、乙卯、庚辰，即乙卯日主，日支卯木自旺，生于午火之月，又得两庚金分别在月干、时干间隔木气，既有火生木，又有金斧斤砥砺木性，故能成器而贵至极品。

- **完整对等诠释（secondary_lang_full）**：
  The text says that when wood meets metal in an 'interval' configuration it can make a person into an official of the two ministries, while wood without metal can never truly become a vessel. This image comes from carpentry: raw wood must be cut and shaped by metal tools before it can become a useful structure. In the example of Minister Yang Bo, with Ji-Si, Geng-Wu, Yi-Mao and Geng-Chen, Yi wood sits on Mao and is self-prosperous, born in the fiery month of Wu, and flanked on both sides by Geng metal. The two Geng stems restrain and refine the strong wood without breaking it, so the person is carved and tempered into talent and rises to the very highest rank.


- 核心要点：
  - 金木间隔格，重在**木旺而不骄，得金裁制成器**，象征在严格制度与权力约束下成就之才。
  - 金须得位得势而不过度：金过重则伤木，金太轻则不能成器，贵在制约与生扶的平衡。
  - 此格多主文武兼资、刚中有柔之官职，适宜在制度森严的机构中居要职。

- 详细解说：
  在五行象义中，木主生长、伸展与仁，金主肃杀、裁决与义。金木相隔一格，实乃以金之严肃、决断来砥砺木之伸展，使其由散漫而成栋梁。若无金之裁制，木气纵横易流于浮华；若金重木弱，则又成压抑、折损之象。故本节特别提出"木无金，终不成器"，强调金之存在并非为伤害木，而是令其成器。
  
  以例命而论，乙卯日主得午火生扶，又得两庚夹辅，形成火生木、金裁木之局。庚金既制卯木之过旺，又因位置得当而不至于克折日主，故名"间隔"而非"冲克"。这一结构在现实中常表现为：命主性格有原则、有棱角，历经制度与上级严格要求而愈发成熟，终能在两府类的中枢机关中担重任。

- 校勘与字词辨析：
  - **"两府"**：历代所指略有变化，多为中书、门下或文武两府等中央最高级机构，今可泛指国家权力中枢。
  - **"成器"**：本义指木材被雕刻为器物，引申为人成为可堪大用之才。
  - **English**：
    - Extended to mean becoming talent worthy of great responsibility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_036]` `[trigger: 金木间隔]` `[factor_trigger: jinmu_jiange_presence]` `[role: 主干]` 木若逢金间隔，作两府之官。 → 《三命通会》卷五#金木间隔
  - `[ns_smth_05_037]` `[trigger: 成器之理]` `[factor_trigger: mu_wu_jin AND zhong_bu_cheng_qi]` `[role: 主干依赖]` 木无金，终不成器。 → 《三命通会》卷五#金木间隔
  - `[ns_smth_05_038]` `[trigger: 两庚间隔]` `[factor_trigger: liang_geng_jiange AND mu_ri_wang]` `[role: 条件分支]` 乙坐卯自旺，生于午，得两庚间隔，成器，故贵极品。 → 《三命通会》卷五#金木间隔
  - `[ns_smth_05_039]` `[trigger: 砥砺成才]` `[factor_trigger: jin_zhi_mu_qi AND pingheng_peizhi]` `[role: 总结]` 以金之严肃、决断来砥砺木之伸展，使其由散漫而成栋梁。 → 《三命通会》卷五#金木间隔"""
    normalized_text_zh: str = """"""
    subject: str = "金木相隔与两府之官"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'jinmu_jiange_presence', 'bazi_semantic', 'jiange_config', 'bazi_semantic', 'jinmu_pingheng_score', 'bazi_semantic', 'chengqi_score', 'bazi_semantic', 'zhiheng_tiaohe', 'bazi_semantic', 'zhongshu_yaozhi', 'bazi_semantic', 'source_ref', 'rel_smth_05_028', 'jinmu_jiange_presence', 'rel_smth_05_029', 'chengqi_score', 'rel_smth_05_030', 'zhongshu_yaozhi', 'evi_smth_05_028', 'jiange_config', 'rule_jiange', 'evi_smth_05_029', 'chengqi_score', 'rule_chengqi', 'evi_smth_05_030', 'zhongshu_yaozhi', 'rule_jigui', 'map_smth_05_019', 'map_smth_05_020']
    
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
        l1_anchor="smth_v1.0.0_金木相隔与两府之官_001_L1",
    )
    version: str = "1.0.0"
