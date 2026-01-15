"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264131
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
    semantic_id="smth_v1.0.0_岁运刑冲与神煞_001",
    book_id="sanming",
    engine_id="bazi"
)
class 岁运刑冲与神煞(SemanticEntry):
    """
    - 原文（source_text）：
  大凡行好运，日干伤流年岁君，干头祸轻；行不好运，日干伤岁君，干头祸重。若已发过，则死。
  辰戌丑未各有三分余气。如行午运至未，有三分火气；行子至丑，有三分水...
    """
    
    original_text: str = """- 原文（source_text）：
  大凡行好运，日干伤流年岁君，干头祸轻；行不好运，日干伤岁君，干头祸重。若已发过，则死。
  辰戌丑未各有三分余气。如行午运至未，有三分火气；行子至丑，有三分水气之例，不可全作土论。
  凡阳刃格，岁运最怕冲合太岁。干合日时干者，为晦气煞；日时干支与流年干支同，为转趾煞，如庚申日见庚申或庚寅太岁之类，轻则远迁，重则毁屋破财。

- 分字分词释义：
  - **日干伤岁君**：日干克流年天干（如甲日克戊年）。
  - **三分余气**：四季土各藏余气（未藏火、丑藏水等），行运交接时需注意余气延续。
  - **晦气煞**：流年干合日干或时干（合住日主或时干）。
  - **转趾煞**：流年干支与日柱或时柱相同（伏吟）或相冲（反吟）。

- **规范化释义（primary_lang_explained）**：
  行好运时，若日干克流年太岁，祸患较轻；行坏运时，日干克太岁，祸患较重。若在坏运中已经发迹过，恐有死灾。
  辰戌丑未四季土，各有上个季节的三分余气。如午运交入未运，未中尚有三分火气；子运交入丑运，丑中尚有三分水气。不可全当作土来看待。
  阳刃格最怕岁运冲合太岁。流年天干合日干或时干，叫晦气煞（主晦气、阻滞）。日柱或时柱干支与流年干支相同（伏吟）或相冲，叫转趾煞（主迁移、变动）。如庚申日遇到庚申流年（伏吟）或庚寅流年（冲），轻则远迁，重则破财毁屋。

- 核心要点：
  - **犯太岁**：日犯岁君，视运吉凶。
  - **四季余气**：土运需看余气。
  - **伏吟反吟**：转趾煞主变动。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_009]` `[trigger: 日干伤岁君]` `[factor_trigger: rigan_shang_suijun AND haoyun_huoqing]` `[role: 主干]` 大凡行好运，日干伤流年岁君，干头祸轻；行不好运，祸重。 → 《三命通会》卷十#岁运刑冲与神煞
  - `[ns_smth_10_010]` `[trigger: 三分余气]` `[factor_trigger: sanfen_yuqi AND siji_tu]` `[role: 主干依赖]` 辰戌丑未各有三分余气，不可全作土论。 → 《三命通会》卷十#岁运刑冲与神煞
  - `[ns_smth_10_011]` `[trigger: 晦气煞]` `[factor_trigger: huiqi_sha AND ganhe_rishi]` `[role: 条件分支]` 干合日时干者，为晦气煞。 → 《三命通会》卷十#岁运刑冲与神煞
  - `[ns_smth_10_012]` `[trigger: 转趾煞]` `[factor_trigger: zhuanzhi_sha AND fuyin_fanyin]` `[role: 总结]` 日时干支与流年干支同，为转趾煞，轻则远迁，重则毁屋破财。 → 《三命通会》卷十#岁运刑冲与神煞"""
    normalized_text_zh: str = """"""
    subject: str = "岁运刑冲与神煞"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_relation_factor_101', 'bazi_semantic', 'bazi_state_factor_221', 'bazi_semantic', 'bazi_state_factor_222', 'bazi_semantic', 'bazi_condition_factor_84', 'bazi_semantic', 'bazi_condition_factor_85', 'bazi_semantic', 'source_ref', 'rel_smth_10_007', 'yunshi_tiaozhi', 'rel_smth_10_008', 'zhuanzhi_sha', 'rel_smth_10_009', 'yuqi', 'evi_smth_10_007', 'yunshi_tiaozhi', 'rule_yunshi_tiaozhi1', 'evi_smth_10_008', 'zhuanzhi_sha', 'rule_zhuanzhi_sha1', 'evi_smth_10_009', 'yuqi', 'rule_yuqi1', 'map_smth_10_005', 'map_smth_10_006']
    
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
        l1_anchor="smth_v1.0.0_岁运刑冲与神煞_001_L1",
    )
    version: str = "1.0.0"
