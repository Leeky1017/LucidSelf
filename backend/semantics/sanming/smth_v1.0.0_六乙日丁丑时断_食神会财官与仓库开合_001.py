"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157336
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
    semantic_id="smth_v1.0.0_六乙日丁丑时断_食神会财官与仓库开合_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日丁丑时断食神会财官与仓库开合(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日丁丑时断。

  （以下六乙日所忌月分与上同，时亦并论。）六乙日生时丁丑，食神相助遇财官；月通金气化为福，不是寻常下贱看。乙日丁丑时，食会财官。丁为食...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日丁丑时断。

  （以下六乙日所忌月分与上同，时亦并论。）六乙日生时丁丑，食神相助遇财官；月通金气化为福，不是寻常下贱看。乙日丁丑时，食会财官。丁为食，庚为官，己为财，丑中有辛金合局，己土得位，如有倚托者，贵。通金气月化者，富厚尊重；不通月气，平常。

  乙丑日丁丑时，秋生，有权。主带疾；夏吉，冬平；春旺，贵寿。

  乙卯日丁丑时，亥月，身旺见辛偏官，柱有丁制，风宪武职。

  乙巳日丁丑时生，亥卯未寅月，贵。通金气月，有倚托者，福重。

  乙未日丁丑时，辰戌丑未月，富。春寿长，秋名利，夏贫下，冬平常。申年月，武职三品。

  乙酉日丁丑时，若通木气，有倚托者，显贵。申丑年月亦好，寅亥尤佳。

  乙亥日丁丑时，亥月，性急有操持，妻贤子孝，官至六七品。午月长生，年月透官印，大贵。

  仓库时开乙见丁，食神坐库禄财亲。无匙不作朝中客，也是清闲有福人。乙日时逢丁丑，寿星发达无疑。身居磨蝎莫嫌迟，库内钱财积聚。年时月合发达，空刑妻子难为。双亲雁侣有盈亏，运至牢藏金柜。

- 分字分词释义：

  - **食会财官**：食神与财星、官星同见，象征有生产力、财力与职位三者的联动.
  - **仓库时开**：丑为库地，比喻财富或资源的积聚之所，被「开启」则能动用.
  - **无匙不作朝中客**：无合化、无生扶时，仓库难开，难登高位，仅为清闲之命.

- 规范化释义（primary_lang_explained）：

  本节论「六乙日，丁丑时」：

  - 丑为财库，丁火为食神生财，庚官、己财俱在其中，若月令通金气、有倚托，则财官并济，多主富厚、尊荣；
  - 若不通月气，则只是普通衣禄之人，但也不至于极端困厄；
  - 各日支配合不同月令，可见或文武并贵、或富而有疾、或清贵不权等多种情形.

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Ding-Chou Hour":

  - Chou serves as the wealth treasury; Ding Fire as Food God generates wealth; Geng Official and Ji Wealth are both contained within. When monthly pillar channels Metal energy with proper support, Wealth-Official combine for abundant prosperity and honor.
  - When not connected to monthly energy, this remains an ordinary livelihood, though not extremely troubled.
  - Different day branches with various monthly pillars show combinations of civil-military nobility, wealth with illness, or pure nobility without authority.

- 核心要点：

  - 结构以**食神生财、财生官、库地聚气**为主轴，条件好时容易「厚积薄发」；
  - 但若缺乏「匙」——即合化、印绶等开库之物，则易成有库无门、潜能难启；
  - 对亲缘与婚姻，有「空刑妻子难为」的提醒，强调责任与照顾的重要性.

- 详细解说：

  1. **库地的现代理解**  
     - 「库」可视作资源池、资产池，例如专业能力、资产、社会资本；  
     - 若只积不流，容易形成内耗；适度投资与使用，反而能形成良性循环.

  2. **文武双轨的可能**  
     - 原文中有「风宪武职」「武职三品」等说法，提示此格既能文、亦能武；  
     - 现代可对应管理岗位、技术+管理复合角色等.

  3. **家庭与寿夭提示**  
     - 多处提到带疾、刑妻、双亲盈亏，提醒此格在照顾家人、平衡健康方面要更用心；  
     - 日常可通过作息、运动与情绪管理，主动弱化这些风险.

- 校勘与字词辨析：

  - 「仓库时开」在本稿中比喻为资源渠道被打通，不作额外神煞系统.
  - 关于各品级、职位的描写，统一保留其等级感，用以呈现高低差异，而不机械类比现代职级.
  - **English**：
    - Life stage predictions explained as probability indicators; metaphorical descriptions of fortune and misfortune contextualized; technical shensha terms demystified.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_053]` `[trigger: 食神会财官]` `[factor_trigger: shishen_hui_caiguan AND yu_caiguan]` `[role: 主干]` 六乙日生时丁丑，食神相助遇财官。 → 《三命通会》卷八#六乙日丁丑时
  - `[ns_smth_08_054]` `[trigger: 通金气化福]` `[factor_trigger: tong_jinqi AND hua_wei_fu]` `[role: 主干依赖]` 月通金气化为福，不是寻常下贱看。 → 《三命通会》卷八#六乙日丁丑时
  - `[ns_smth_08_055]` `[trigger: 仓库时开]` `[factor_trigger: cangku_shi_kai AND lu_cai_qin]` `[role: 条件分支]` 仓库时开乙见丁，食神坐库禄财亲。 → 《三命通会》卷八#六乙日丁丑时
  - `[ns_smth_08_056]` `[trigger: 牢藏金柜]` `[factor_trigger: laocang_jingui AND yunzhi_fada]` `[role: 总结]` 运至牢藏金柜。 → 《三命通会》卷八#六乙日丁丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日丁丑时断：食神会财官与仓库开合"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_factor_151', 'bazi_semantic', 'bazi_relation_factor_71', 'bazi_semantic', 'bazi_state_factor_152', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_metal_1', 'bazi_semantic', 'source_ref', 'rel_smth_08_040', 'shihui_caiguan', 'rel_smth_08_041', 'cangku_kaihe', 'rel_smth_08_042', 'tongjinqi_yue', 'evi_smth_08_040', 'shihui_caiguan', 'rule_shihui', 'evi_smth_08_041', 'cangku_kaihe', 'rule_cangku', 'evi_smth_08_042', 'tongjinqi_yue', 'rule_tongjin', 'map_smth_08_027', 'map_smth_08_028']
    
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
        l1_anchor="smth_v1.0.0_六乙日丁丑时断_食神会财官与仓库开合_001_L1",
    )
    version: str = "1.0.0"
