"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436455
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
    semantic_id="smth_v1.0.0_滥格与多夫多财之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 滥格与多夫多财之象(SemanticEntry):
    """
    - 原文（source_text）：

  滥者婪也。谓柱中明有夫多，暗者财旺，干支又多带煞，必因酒色，私暗得财。此等之命，或为奴婢，或克夫再嫁。如庚寅、丙戌、庚申、丁亥，庚申八专自旺，丙火为夫，寅戌...
    """
    
    original_text: str = """- 原文（source_text）：

  滥者婪也。谓柱中明有夫多，暗者财旺，干支又多带煞，必因酒色，私暗得财。此等之命，或为奴婢，或克夫再嫁。如庚寅、丙戌、庚申、丁亥，庚申八专自旺，丙火为夫，寅戌会局时干，又丁爱重火情，庚申金暗克寅亥木为财，亥中壬水为食生财，其人虽美貌有福，不免滥而得财。

- 分字分词释义：

  - **滥者婪也**：滥，本义过度泛滥，引申为贪婪、不加节制。
  - **明有夫多，暗者财旺**：天干上可见多位夫星，地支或藏财星旺盛，象征情感与财务对象皆多。
  - **干支多带煞**：命局中刑冲、七煞等较多，关系动力中带有风险与冲突。
  - **因酒色，私暗得财**：以古语形容通过情感、人际或隐性渠道获取资源。

- **规范化释义（primary_lang_explained）**：

  “滥格”强调的是**多夫星、多财星且多煞**：

  - 明处可见多位夫星，暗处又有财星旺盛，表示情感、合作与金钱往来都偏向多线并行；
  - 干支多带煞气，使得这些关系往往伴随强烈欲望与风险，易因情财纠葛而起波折；
  - 原例中庚金自旺、丙丁火情重，壬水生财，故古人以“滥而得财”形容其以情财相纠的模式。

- 核心要点：

  - 多夫星、多财星，再叠加煞气，是滥格的结构核心。
  - 容易通过关系网络获取资源，同时也易陷入情财难分的局面。
  - 对应的不是必然的“品行问题”，而是情感与利益纠缠过密的生活结构。

- 详细解说：

  1. **多夫星与情感模式**  
     - 多夫星并非一定意味着现实中多次婚姻，更可看作对伴侣类型期待多元、容易卷入复杂关系；  
     - 若缺乏明确边界与自我照顾，易在不同关系间摇摆。

  2. **财旺与资源流向**  
     - 财星旺而多，与“私暗得财”的古语相对应，象征通过关系、社交、合作项目获得收益；  
     - 若缺乏制度化的管理，易导致不透明、不稳定的收入结构。

  3. **煞气与风险**  
     - 七煞、刑冲等神煞增多，往往意味着决策冲动、冒进与反复；  
     - 在实际生活中，表现为在感情与金钱上都较容易“上头”，事后才感受后果。

  对现代人来说，“滥格”可以提醒我们：在情感与资源获取方式上保持适度与清晰边界，避免因过度贪多而耗损自我与他人。

- **完整对等诠释（secondary_lang_full）**：

  The "Overflowing" pattern highlights a chart where both relationship and money lines are numerous and heavily charged. On the visible level, there are multiple spouse stars appearing on the Heavenly Stems; beneath the surface, hidden Wealth stars are abundant in the Branches. At the same time, many of these indicators carry Sha or clash relationships, so that desire, competition, and risk are woven into how affection and resources move.

  In the example, Geng Metal sits in its own Lu at Shen, indicating strong self and strong capacity to act. Bing Fire as a spouse star is reinforced by the Yin–Xu Fire combination, while Ding Fire further intensifies emotional and sensual drives. Geng Metal covertly controls Yin Wood and Hai Wood as Wealth, with Ren Water in Hai feeding this Wealth. The result is a structure where there is no lack of attraction, opportunities, and financial channels, but much of it flows through personal ties, favours, or ambiguous arrangements rather than through transparent, institutionalised paths. Hence the classical phrase "to gain wealth through excess".

  For today's reader, this pattern describes a strong tendency to pursue both relationship intensity and material gain through complex networks. When handled without clear boundaries or accountability, it can lead to burnout, scandals, or legal/ethical trouble. When handled with awareness, it can instead be channelled into socially responsible networking, partnership-based business, or creative industries where emotional intelligence and contact-building are real assets.

- 校勘与字词辨析：

  - 原文“庚申，八专自旺”一句，本稿按意作“庚申八专自旺”，理解为庚金自坐申禄而极旺。
  - “滥者婪也”“因酒色，私暗得财”等词，属于强烈价值判断色彩的古语，本稿在解说中均改以“情财关系交织、资源获取渠道不透明”的结构语言表达。
  - **English**：
    - Structural language expressing "path not transparent."

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_029]` `[trigger: 滥格定义]` `[factor_trigger: lan_ge_lan]` `[role: 主干]` 滥者婪也。 → 《三命通会》卷七#滥格
  - `[ns_smth_07_030]` `[trigger: 多夫多财]` `[factor_trigger: ming_you_fu_duo AND an_zhe_cai_wang]` `[role: 主干依赖]` 谓柱中明有夫多，暗者财旺，干支又多带煞。 → 《三命通会》卷七#滥格
  - `[ns_smth_07_031]` `[trigger: 酒色得财]` `[factor_trigger: yin_jiuse_sian_decai]` `[role: 条件分支]` 必因酒色，私暗得财。 → 《三命通会》卷七#滥格
  - `[ns_smth_07_032]` `[trigger: 滥而得财]` `[factor_trigger: lan_er_decai]` `[role: 总结]` 其人虽美貌有福，不免滥而得财。 → 《三命通会》卷七#滥格"""
    normalized_text_zh: str = """"""
    subject: str = "滥格与多夫多财之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_96', 'bazi_semantic', 'bazi_structure_strength', 'bazi_semantic', 'bazi_state_index', 'bazi_semantic', 'bazi_factor_9', 'bazi_semantic', 'source_ref', 'rel_smth_07_019', 'fuxing_shuliang', 'rel_smth_07_020', 'qingcai_jiuchan', 'rel_smth_07_021', 'guodu_fengxian', 'evi_smth_07_019', 'fuxing_shuliang', 'rule_lange', 'evi_smth_07_020', 'qingcai_jiuchan', 'rule_jiuse', 'evi_smth_07_021', 'guodu_fengxian', 'rule_decai', 'map_smth_07_013', 'map_smth_07_014']
    
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
        l1_anchor="smth_v1.0.0_滥格与多夫多财之象_001_L1",
    )
    version: str = "1.0.0"
