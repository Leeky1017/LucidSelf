"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523839
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
    semantic_id="zpzq_v1.0.0_刑者三刑也_冲者六冲也_会者三会也_合者六合也_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 刑者三刑也冲者六冲也会者三会也合者六合也(SemanticEntry):
    """
    - **原文（source_text）**：
  刑者，三刑也，子卯、巳申、丑戌未之类是也。冲者，六冲也，子午、卯酉之类是也。会者，三会也，申子辰之类是也。合者，六合也，子与丑合之类是也。此皆以地支宫...
    """
    
    original_text: str = """- **原文（source_text）**：
  刑者，三刑也，子卯、巳申、丑戌未之类是也。冲者，六冲也，子午、卯酉之类是也。会者，三会也，申子辰之类是也。合者，六合也，子与丑合之类是也。此皆以地支宫分而言，系对冲之意也。三方为会，朋友之意也；并对为合，比邻之意也。至于三刑取庳，姑且阙疑，虽不知其所以然，于命理亦无害也.

- 原注（原文注解）：
  　　本段给出四种基本地支关系的定义：
  - 三刑：子卯、巳申、丑戌未等互相刑害之支；
  - 六冲：子午、卯酉等正对冲击之支；
  - 三会：申子辰等同类会局，成水木火金土等局势；
  - 六合：子丑、丑子等一对一的合支关系.
  并说明：
  - 三会像朋友相聚，三方合力；
  - 六合像比邻相合，两支成对；
  - 至于三刑取法，未必人人明白其细因，但对命理大局影响有限，可暂且搁置疑问.

- 分字分词释义：
  - 宫分：地支所在的方位与宫位，如子午卯酉四正、寅申巳亥四生等.
  - 对冲之意：六合、六冲皆以前后相对的宫位而言.
  - 三方为会：三支成方局，如申子辰合水等.
  - 并对为合：两支相邻或相对成一对，如子丑、寅亥等.
  - 三刑取庳（原文作“取庳/取庑”等异写）：指三刑的具体取法在古人间亦存疑，作者不作深究.

- **规范化释义（primary_lang_explained）**：
 - 作者先把"刑、冲、会、合"四种地支关系的基本含义交代清楚.所谓"三刑"，就是子卯、巳申、丑戌未等互相刑害的关系；"六冲"是像子午、卯酉这样一正对的冲击关系；"三会"是像申子辰这样三支同类会聚，形成某一大局（如水局、木局等）；"六合"则是子与丑这类一对一的合支.这里特别强调，这些概念都是从地支的"宫位与方位"来理解的：三会好比"朋友聚会、三方同心"，六合好比"邻里合力、两支相亲".至于三刑的来由与取法，古人本身也有不同说法，作者建议暂存疑而不必强求其"所以然"，因为即便不弄清每一条细节，也不影响整体命理判断.

- **完整对等诠释（secondary_lang_full）**：  
  This paragraph simply defines four basic kinds of relationship among the Earthly Branches. "Three punishments" refers to the three sets of branches that tend to injure one another, such as the pairings usually written as Zi with Mao, Si with Shen, and Chou with Xu and Wei. "Six clashes" are the six diametrically opposed pairs such as Zi–Wu and Mao–You. "Three meetings" are the three triplicities like Shen–Zi–Chen, where three branches of the same elemental family come together to form a large‑scale Water, Wood, Fire, Metal or Earth configuration. "Six combinations" are the six one‑to‑one pairings such as Zi with Chou, which bind two branches into a unit.

  All of these patterns are grounded in the branch palaces and directions: the way signs stand opposite one another or join to form a quadrant of the compass, rather than any arbitrary numerology. As for the exact rules behind the three punishments, the author treats them with reserve: even if we do not fully understand why they were formulated in a particular way, this does not prevent us from reading charts effectively, so there is no need to be obsessed with tracing every last theoretical origin.

- 详细解说：
  - 刑冲会合的本质都在“地支方位与宫分”之中，不在单个字面之上.
  - 会局、六合是“聚力与合力”的概念；刑、冲是“冲突与紧张”的概念，两者在用神分析中常互相制衡.
  - 对三刑不必过度执着其来由，只要掌握其“易生暗伤与内在紧张”的特点即可.

- 核心要点：
  - 刑、冲不利为主；会、合多作“解法”与“助力”看，但不必一概视为吉.
  - 会合都是以地支为基准的结构，分析时要看全局支位间的方局关系.

- 应用推演：
  1) 先画出命局地支的分布，标出有无三刑、六冲、三合三会、六合等；
  2) 分清哪些是对日主或用神的直接刑冲，哪些只是支中次要冲突；
  3) 预先记住会合多用于“解冲解刑”，为后文细节分析打底.

- 反例与边界：
  - 把一切刑冲都视为必然大凶，不看是否有会合解救；
  - 把一切会合都视为必然大吉，不看其是否会“因解反得刑冲”.

- 小例（示意）：
  - 命局有子、卯、卯三支，初看二卯不刑一子；若再遇戌，会合一卯，剩余子卯反成独立刑局，此时要提高对有关六亲的注意.

- 校勘与字词辨析：
  - “子卯巳申子类是也”一作“子卯、巳申、丑戌未之类是也”，本精校按照通行三刑（子卯、丑戌未、寅巳申）之说整理，并在此说明.

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_260]` `[trigger: 命理要义]` `[factor_trigger: benjie_hexin_mingli AND lunshu_yaodian]` `[role: 主干]` 本节核心命理论述。 → 《子平真诠》#第52节
  - `[ns_zpzy_261]` `[trigger: 实践要领]` `[factor_trigger: duanming_shijian AND yaoling_zonghe]` `[role: 主干]` 断命实践要领。 → 《子平真诠》#上卷
  - `[ns_zpzy_262]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_263]` `[trigger: 用神有力]` `[factor_trigger: yongshen_youli=true AND result=fugui_keqi]` `[role: 主干]` 用神有力，富贵可期。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "刑者三刑也，冲者六冲也，会者三会也，合者六合也"
    factor_refs: list = ['sanxing', 'liuchong', 'sanhui', 'liuhe', 'engine_id', 'dizhi_relation_type', 'bazi_rule_engine', 'chengju_zhishu', 'bazi_rule_engine', 'xingchong_luodian', 'bazi_rule_engine', 'huihe_jiechong', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_069', 'sanxing', 'rel_zpzq_070', 'liuchong', 'rel_zpzq_071', 'sanhui', 'evi_zpzq_069', 'sanxing', 'rule_sanxing_def', 'evi_zpzq_070', 'liuchong', 'rule_liuchong_def', 'evi_zpzq_071', 'sanhui', 'rule_sanhui_def', 'concept_conflict', 'concept_alliance']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_刑者三刑也_冲者六冲也_会者三会也_合者六合也_001_L1",
    )
    version: str = "1.0.0"
