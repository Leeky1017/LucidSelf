"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458228
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
    semantic_id="smth_v1.0.0_时柱官星与晚年之贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 时柱官星与晚年之贵(SemanticEntry):
    """
    - **原文（source_text）**：
  如甲日酉辛时，乙日申庚时例。时上官星与月亦同，但力轻微，发福多在晚年，或生贤子，要有印助。古歌云：正官有用不须多，多则伤身少则和，日旺再逢生印绶，定须...
    """
    
    original_text: str = """- **原文（source_text）**：
  如甲日酉辛时，乙日申庚时例。时上官星与月亦同，但力轻微，发福多在晚年，或生贤子，要有印助。古歌云：正官有用不须多，多则伤身少则和，日旺再逢生印绶，定须平步擢高科。

- 分字分词释义：
  - **时上官星**：指官星落在时柱，如甲日辛酉时、乙日庚申时，象征晚年境遇与子息情况中的官贵之象。
  - **与月亦同**：取官原则与月令正官相似，仍以清纯、得令、有印扶身为佳，只是力量较月令为轻。
  - **发福多在晚年**：时柱主晚年、子息与后运，故时上正官多主中晚年功名、退休前后之荣遇。
  - **生贤子**：时干支亦主子女，时上官星清正，多主子女贤良、有科名或仕途发展。
  - **正官有用不须多，多则伤身少则和**：强调官星宜一位清纯，过多则克身太重，反损日主。

- **规范化释义（primary_lang_explained）**：
  本节论的是时柱上出现正官星的情形。与月令正官一样，时上正官仍以官星清纯、有印生扶为贵，但因时柱主晚年和子息，其力道比月令为轻，多数在中晚年才显现福分，或者体现在子女成就上。若日主旺、再得印绶生扶，时上这一位官星即可成为晚年功名、平步高科的重要着力点；若官星多见混杂，或无印以生身，则反可能导致身轻官重，晚年反受牵累。

- **完整对等诠释（secondary_lang_full）**：
  Here the text turns to cases like a Jia day with Xin-You hour or a Yi day with Geng-Shen hour, where the proper official sits on the hour pillar. The principles for judging purity, support from Seal and the matching of body and official are the same as for the month-official, but the strength is lighter and its effects show more in later life and in the fortunes of one’s children. When the day-master is robust and there is Seal to nourish it, a single clean proper official on the hour pillar can become the focus for late-life advancement and examination success, or for children who achieve distinction.
  The old verse that says "a useful proper official need not be many; too many hurt the body, few keep harmony; if a strong day again meets generating Seals, one is bound to rise smoothly through the ranks" underlines two points: that proper official should appear as one clear star rather than in crowded company, and that its promises are only realised when the self and its supporting Seals are strong enough to bear the responsibilities that come in the later stages of life.

- 核心要点：
  - 时上正官主要反映**中晚年与子女层面的官贵**，而非少年、壮年之发达。
  - 取用原则与月令正官相同：官星宜一位清纯、有印扶身，忌伤官七煞混杂。
  - 日主需有一定根气与印绶支撑，方能在晚年真正承受官星所代表的责任与荣誉。

- 详细解说：
  在四柱结构中，年柱为根、月柱为苗、日柱为身、时柱为果。岁德正官着重出身之根芽，月令正官着重壮年格局，而时上正官则偏向人生后程的结果与子孙表现。古歌所谓"日旺再逢生印绶，定须平步擢高科"，可以理解为：当日主已具相当实力，再加以印绶支持，于时柱上再得一位清纯正官，则多主中晚年科名晋升顺畅，或子女科甲及第，为家庭带来后续的荣光。
  
  然而，时上正官由于本身力量较月令为弱，若全局仅此一位官星，而日主又偏弱无印，则易形成"尾重头轻"的局面——责任压力集中于人生后程，身心却已不足以承担，反致晚景劳碌。因此，在实际判命时，应将时上正官与月令、年柱结构一并衡量，既不可因见官而妄言贵命，亦不可忽视其在晚年与子息方面的加分作用。

- 校勘与字词辨析：
  - **"如甲日酉辛时，乙日申庚时例"**：以甲日辛酉时、乙日庚申时为代表，余干可类推其他日干坐时上官星之情形。
  - **"多则伤身少则和"**：与前文正官总论中"官星止许一位"之旨相合，再次强调正官格清纯为上，不宜多见。
  - **English**：
    - Direct-Official pattern favors purity; multiple officials undesirable.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_021]` `[trigger: 时上官星]` `[factor_trigger: shi_shang_zhengguan_presence]` `[role: 主干]` 时上官星与月亦同，但力轻微，发福多在晚年，或生贤子。 → 《三命通会》卷五#时上正官
  - `[ns_smth_05_022]` `[trigger: 官星纯一]` `[factor_trigger: guanxing_purity AND body_official_balance]` `[role: 主干依赖]` 正官有用不须多，多则伤身少则和。 → 《三命通会》卷五#时上正官
  - `[ns_smth_05_023]` `[trigger: 晚年高科]` `[factor_trigger: day_master_strong AND yin_support AND shi_zhu_guanxing]` `[role: 总结]` 日旺再逢生印绶，定须平步擢高科。 → 《三命通会》卷五#时上正官"""
    normalized_text_zh: str = """"""
    subject: str = "时柱官星与晚年之贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'shishang_zhengguan_presence', 'bazi_semantic', 'shishang_guanxing_config', 'bazi_semantic', 'wannian_fufu_score', 'bazi_semantic', 'zinv_xianliang_score', 'bazi_semantic', 'rizhu_yin_fuchi', 'bazi_semantic', 'houcheng_yali_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_016', 'shishang_zhengguan_presence', 'rel_smth_05_017', 'wannian_fufu_score', 'rel_smth_05_018', 'houcheng_yali_risk', 'evi_smth_05_016', 'wannian_fufu_score', 'rule_wannian', 'evi_smth_05_017', 'zinv_xianliang_score', 'rule_xianzi', 'evi_smth_05_018', 'rizhu_yin_fuchi', 'rule_yinfuchi', 'map_smth_05_011', 'map_smth_05_012']
    
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
        l1_anchor="smth_v1.0.0_时柱官星与晚年之贵_001_L1",
    )
    version: str = "1.0.0"
