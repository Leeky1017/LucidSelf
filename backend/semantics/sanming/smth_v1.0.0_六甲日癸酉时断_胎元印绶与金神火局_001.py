"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157289
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
    semantic_id="smth_v1.0.0_六甲日癸酉时断_胎元印绶与金神火局_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六甲日癸酉时断胎元印绶与金神火局(SemanticEntry):
    """
    - 原文（source_text）：

  六甲日癸酉时断.

  六甲日生时癸酉，暗官明印未希奇；柱中有火无刑破，元命胎生贵可知.甲日癸酉时，胎生元命，甲木酉上受胎，为甲生气；明癸为印，暗辛为官，有...
    """
    
    original_text: str = """- 原文（source_text）：

  六甲日癸酉时断.

  六甲日生时癸酉，暗官明印未希奇；柱中有火无刑破，元命胎生贵可知.甲日癸酉时，胎生元命，甲木酉上受胎，为甲生气；明癸为印，暗辛为官，有巳土破印，不贵.酉为金神，若柱有寅戌，通火气者，德性纯厚而贵；无火见水，凶暴残疾.

  甲子日癸酉时，春生木旺；酉月官纯，贵.若混之以煞，或煞多，柱中全无火气，凶.

  甲寅日癸酉时，春生寿；夏反复；秋性不定，多凶；冬平常.丑未月贵.

  甲辰日癸酉时，子戌年月，有财有官，贵.

  甲午日癸酉时，主孤.生寅午戌月，行东北方郎官.

  甲申日癸酉时，平常.通火气月，行南运，富贵.申酉年月，多夭.有水化金毒，只作官印论，不作金神，亦吉，但主退早.

  甲戌日癸酉时，子戌年月，文章显贵；子午月，不贵即富.

  甲日交通癸酉时，金神火局两相宜；运行南地无刑破，富贵荣华事事奇.甲日时逢癸酉，为人富贵双全.三奇发福屡升迁，上下相和贵显.君子寒门将相，常人置立田园.无伤无破是英贤，此命定居台宪.

- 分字分词释义：

  - **胎生元命**：指日主在该支处犹如胎元之地，有未成形而具潜力之意.
  - **金神**：酉为金神之一，若火不济则刚烈伤人，得火则刚中有柔.
  - **化金毒**：指水气过盛，把金性发挥到极端，易显冷酷或伤害性.

- 规范化释义（primary_lang_explained）：

  本节论「六甲日，癸酉时」：

  - 甲木在酉受胎，癸水为印、辛金为官，若得火土调和，则身官印配合良好，多主文章、德行与地位兼具；
  - 火气不济而水金过盛时，则金神偏激，易生凶暴、残疾等风险；
  - 依不同甲日，看有的是官纯而贵，有的是孤而仕途通达，有的则主富而退早.

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Jia Days with Gui-You Hour":

  - Jia Wood receives embryonic qi at You; Gui Water serves as Seal while hidden Xin Metal serves as Official. With Fire and Earth harmonization, Day Master, Official, and Seal coordinate well, typically indicating combined literary achievement, virtuous character, and status.
  - When Fire energy is insufficient and Water-Metal dominates, the Golden Spirit becomes extreme, risking violence or disability.
  - Depending on different Jia days, some show pure Official and nobility, others show solitude yet successful official career, still others show wealth but early retirement.

- 核心要点：

  - 结构核心在于**金神与印绶如何调和**：火足则贵，水重则险；
  - 此格的上限很高，可以从寒门而至将相之位，也可以是稳健的田产之家；
  - 是否「无刑破」与行运方向（南地火运）是关键变量.

- 详细解说：

  1. **胎元视角**  
     - 「胎生元命」提示此时格具备「潜能多、成形晚」的特点；  
     - 早年不必强求立刻定型，逐步累积能力与人脉反而更合结构.

  2. **金神与人格特质**  
     - 金神得火，不仅象征权位，也象征原则与担当；  
     - 若火弱水强，则可能表现为过度冷静、刚硬乃至对他人造成伤害的决策风格.

  3. **现代建议**  
     - 适合走制度化、可长期累积信誉的路径，如公职、专业服务等；  
     - 建议在权力与效率之外，刻意培养共情与柔软度，以避免「化金为毒」.

- 校勘与字词辨析：

  - 「金神火局两相宜」在本稿中理解为五行力量的配合度，而非额外神煞系统.
  - 「凶暴残疾」等说法，统一视作风险程度的夸张表达，并非字面预言.
  - **English**：
    - Life stage predictions explained as probability indicators; metaphorical descriptions of fortune and misfortune contextualized; technical shensha terms demystified.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_037]` `[trigger: 暗官明印]` `[factor_trigger: anguan_mingyin AND wei_xiqi]` `[role: 主干]` 六甲日生时癸酉，暗官明印未希奇。 → 《三命通会》卷八#六甲日癸酉时
  - `[ns_smth_08_038]` `[trigger: 胎生元命]` `[factor_trigger: taisheng_yuanming AND jia_shengqi]` `[role: 主干依赖]` 甲木酉上受胎，为甲生气；明癸为印，暗辛为官。 → 《三命通会》卷八#六甲日癸酉时
  - `[ns_smth_08_039]` `[trigger: 金神火局]` `[factor_trigger: jinshen_huoju AND dexing_chunhou]` `[role: 条件分支]` 酉为金神，若柱有寅戌，通火气者，德性纯厚而贵；无火见水，凶暴残疾。 → 《三命通会》卷八#六甲日癸酉时
  - `[ns_smth_08_040]` `[trigger: 台宪英贤]` `[factor_trigger: taixian_yingxian AND wu_shang_wupo]` `[role: 总结]` 无伤无破是英贤，此命定居台宪。 → 《三命通会》卷八#六甲日癸酉时"""
    normalized_text_zh: str = """"""
    subject: str = "六甲日癸酉时断：胎元印绶与金神火局"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_jia', 'bazi_semantic', 'bazi_state_factor_273', 'bazi_semantic', 'bazi_state_factor_342', 'bazi_semantic', 'bazi_state_metal_1', 'bazi_semantic', 'hour_branch_you', 'bazi_semantic', 'bazi_condition_fire_earth', 'bazi_semantic', 'source_ref', 'rel_smth_08_028', 'taisheng_yuanming', 'rel_smth_08_029', 'jinshen_ge', 'rel_smth_08_030', 'huotu_tiaohe', 'evi_smth_08_028', 'taisheng_yuanming', 'rule_taisheng', 'evi_smth_08_029', 'jinshen_ge', 'rule_jinshen_you', 'evi_smth_08_030', 'huotu_tiaohe', 'rule_huozu', 'map_smth_08_019', 'map_smth_08_020']
    
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
        l1_anchor="smth_v1.0.0_六甲日癸酉时断_胎元印绶与金神火局_001_L1",
    )
    version: str = "1.0.0"
