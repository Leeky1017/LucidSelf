"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339312
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
    semantic_id="smth_v1.0.0_六己日乙丑时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日乙丑时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时乙丑，煞星透出坐金神。身强无破要通月，早运名高近侍臣。
  己日乙丑时，专煞，乙木皆多，克己土。丑是金库，金神入庙，己土食神。若身旺，通月气，主富贵...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时乙丑，煞星透出坐金神。身强无破要通月，早运名高近侍臣。
  己日乙丑时，专煞，乙木皆多，克己土。丑是金库，金神入庙，己土食神。若身旺，通月气，主富贵。若身衰，夭折。

- 分字分词释义：
  - **专煞**：乙木为己土七煞（偏官），乙丑时乙木透干，丑中亦藏癸水生乙，煞气专一。
  - **金神入庙**：丑为金库（巳酉丑合金），乙丑为金神（一说乙丑、己巳、癸酉为金神），此处指丑为金之库地，金能制煞。
  - **食神**：丑中藏辛金，为己土食神，能制乙木七煞。

- **规范化释义（primary_lang_explained）**：
  六己日出生于乙丑时，乙木七煞透出。丑为金库，内藏辛金食神，能制七煞。若日主己土身强，且通月气（得令），七煞有制化为权，早年便可名高，有望成为近侍之臣（高官）。若身衰无气，七煞攻身，则恐夭折。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Yi-Chou Hour":

  - Yi Wood Seven-Killing reveals at Chou; Chou is Metal treasury containing Xin Metal Eating God that controls killing.
  - If Ji Earth Day Master is strong passing monthly qi, Seven-Killing becomes authority—early fame and high position as imperial attendant.
  - If body is weak without support, Seven-Killing attacks self—risk of early death.
  - Key: Eating God in treasury secretly controls killing; strong body transforms killing into authority.

- 核心要点：
  - **时上七煞格**：乙木为煞，坐丑湿土，煞有根。
  - **食神制煞**：丑中辛金食神暗藏，制乙木七煞。
  - **身旺为贵**：七煞格最重身旺，身强方能任煞、制煞。

- 详细解说：
  己日乙丑时，七煞透干。古语云“时上一位贵”，指时上偏官（七煞）若一位清纯且有制，主大贵。丑土既是煞之余气（水木余气），又是金库（食神库）。食神在库中暗制七煞，格局有情。关键在于日主强弱：身旺者，以煞为权，主武职或权贵；身弱者，煞重身轻，不仅无贵，反遭灾咎、短寿。

- 校勘与字词辨析：
  - **“金神”**：命理学中乙丑为金神之一（金神格）。此处原文“丑是金库，金神入庙”，意指丑土作为金库，增强了金（食神）的力量，能够制煞。
  - **English**：
    - Annual fortune (大运) terminology explained; timing indicators treated as influence periods rather than fixed events.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_005]` `[trigger: 煞星透出]` `[factor_trigger: shaxing_touchu AND zuo_jinshen]` `[role: 主干]` 六己日生时乙丑，煞星透出坐金神。 → 《三命通会》卷九#六己日乙丑时
  - `[ns_smth_09_006]` `[trigger: 身强通月]` `[factor_trigger: shenqiang_tongyue AND mingao_jinshi]` `[role: 主干依赖]` 身强无破要通月，早运名高近侍臣。 → 《三命通会》卷九#六己日乙丑时
  - `[ns_smth_09_007]` `[trigger: 食神制煞]` `[factor_trigger: shishen_zhisha AND fugui]` `[role: 条件分支]` 丑是金库，金神入庙，己土食神。若身旺，通月气，主富贵。 → 《三命通会》卷九#六己日乙丑时
  - `[ns_smth_09_008]` `[trigger: 身衰夷折]` `[factor_trigger: shenshuai_yaozhe AND xiong]` `[role: 总结]` 若身衰，夷折。 → 《三命通会》卷九#六己日乙丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日乙丑时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_factor_254', 'bazi_semantic', 'bazi_relation_shishen_5', 'bazi_semantic', 'bazi_state_metal_2', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_factor_111', 'bazi_semantic', 'source_ref', 'rel_smth_09_004', 'zhuansha', 'rel_smth_09_005', 'shishen_zhisha', 'rel_smth_09_006', 'shenwang_tongyueqi', 'evi_smth_09_004', 'zhuansha', 'rule_zhuansha1', 'evi_smth_09_005', 'shishen_zhisha', 'rule_shishen_zhisha1', 'evi_smth_09_006', 'shenwang_tongyueqi', 'rule_shenwang_tongyueqi1', 'map_smth_09_003', 'map_smth_09_004']
    
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
        l1_anchor="smth_v1.0.0_六己日乙丑时_001_L1",
    )
    version: str = "1.0.0"
