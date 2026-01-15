"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558948
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
    semantic_id="yhzp_v1.0.0_论印绶_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论印绶(SemanticEntry):
    """
    - **原文（source_text）**：印绶者，生我之神也；乃母也，乃祖业父母田产房屋之类，有庇护我之义也。如逢官运最吉，见财运则凶。喜官杀、忌财、喜食神，忌伤官。印绶无伤，贵享福禄；印绶多者，为...
    """
    
    original_text: str = """- **原文（source_text）**：印绶者，生我之神也；乃母也，乃祖业父母田产房屋之类，有庇护我之义也。如逢官运最吉，见财运则凶。喜官杀、忌财、喜食神，忌伤官。印绶无伤，贵享福禄；印绶多者，为母所蔽，平生少子。印绶一位者主得母力、恩荫祖考、父母慈爱；印绶破者克母。

- **分字分词释义**：
  - **印绶**：生我之神且阴阳相异者，如甲木见癸水，癸水为甲木之印绶（正印）。
  - **生我之神**：五行相生关系中，能够生扶日主的五行。
  - **乃母也**：印绶代表母亲，为六亲之一。
  - **祖业父母田产房屋**：印绶象征的现实事物——祖传家业、房产田地。
  - **庇护我之义**：印绶的核心功能——保护、滋养日主。
  - **官运最吉**：官杀生印，印生身，形成官印相生的贵格。
  - **财运则凶**：财克印，破坏印绶的保护功能。
  - **为母所蔽**：印绶过多，母亲过度保护反而阻碍发展。
  - **平生少子**：印绶克食伤（子女星），故印多少子。

- **规范化释义（primary_lang_explained）**：印绶是生我之神，代表母亲、学历、庇护。印绶喜官杀（官杀生印）、喜食神（食神不伤印），忌财星（财克印）、忌伤官（伤官泄身又克印）。印绶宜一位，多则母蔽少子；印绶无伤享福禄，印绶破克母。

- **完整对等诠释（secondary_lang_full）**：Seal is what-generates-me deity, representing mother, education, protection. Seal favors Officer/Killing (Officer/Killing generates Seal), favors Eating God (Eating God doesn't harm Seal); taboos Wealth Star (Wealth controls Seal), taboos Injuring Officer (Injuring Officer drains Self and controls Seal). Seal ideally singular—multiple brings mother's obstruction with few children; unbroken Seal enjoys blessings, broken Seal harms mother.

- **核心要点**：
  - 印绶是生我之神，代表母亲、学历、庇护
  - 印绶喜官杀（官杀生印），逢官运最吉
  - 印绶忌财星（财克印），见财运则凶
  - 印绶宜一位，多则为母所蔽、平生少子
  - 印绶无伤贵享福禄，印绶破则克母

- **详细解说**：  
  本条论述印绶（正印）的性质与喜忌。印绶是生我之神且阴阳相异者（如甲木见癸水），其六亲代表是"母也"，其象征是"祖业父母田产房屋之类"，其核心功能是"有庇护我之义"——滋养、保护日主。印绶的喜忌十分明确：喜官杀（官杀生印，印生身，形成官印相生的贵格），喜食神（食神不伤印）；忌财星（财克印，破坏庇护功能），忌伤官（伤官泄身又克印）。特别强调印绶的数量问题："印绶一位者主得母力、恩荫祖考、父母慈爱"——一位最吉；"印绶多者，为母所蔽，平生少子"——印绶过多则母亲过度保护反碍发展，且印克食伤（子女星）故少子。"印绶破者克母"警示财破印的严重后果。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_089]` `[trigger: 印绶定义]` `[factor_trigger: yinshou_def AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干]` 印绶者，生我之神也。 → 《渊海子平·论印绶》
  - `[ns_yhzp_090]` `[trigger: 印绶代表]` `[factor_trigger: shishen_yinshou AND liuqin_mu AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干依赖]` 乃母也，乃祖业父母田产房屋之类。 → 《渊海子平·论印绶》
  - `[ns_yhzp_091]` `[trigger: 印绶功能]` `[factor_trigger: shishen_yinshou AND bihu_function AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干依赖]` 有庇护我之义也。 → 《渊海子平·论印绶》
  - `[ns_yhzp_092]` `[trigger: 印绶喜官]` `[factor_trigger: shishen_yinshou AND shishen_guanxing AND dayun_guan AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 如逢官运最吉。 → 《渊海子平·论印绶》
  - `[ns_yhzp_093]` `[trigger: 印绶忌财]` `[factor_trigger: shishen_yinshou AND shishen_caixin AND xiongxiang AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 例外处理]` 见财运则凶。 → 《渊海子平·论印绶》
  - `[ns_yhzp_094]` `[trigger: 印绶喜忌]` `[factor_trigger: shishen_yinshou AND xiji_config AND caiyin AND caiyin_qing_guansha_zu AND changyin AND seal_pattern]` `[role: 条件分支]` 喜官杀、忌财、喜食神，忌伤官。 → 《渊海子平·论印绶》
  - `[ns_yhzp_095]` `[trigger: 印绶无伤]` `[factor_trigger: shishen_yinshou AND wushang AND guixiang AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 印绶无伤，贵享福禄。 → 《渊海子平·论印绶》
  - `[ns_yhzp_096]` `[trigger: 印绶过多]` `[factor_trigger: shishen_yinshou AND guoduo AND shaozu AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 例外处理]` 印绶多者，为母所蔽，平生少子。 → 《渊海子平·论印绶》
  - `[ns_yhzp_097]` `[trigger: 印绶一位]` `[factor_trigger: shishen_yinshou AND yiwei AND mu_li AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 印绶一位者主得母力、恩荫祖考、父母慈爱。 → 《渊海子平·论印绶》
  - `[ns_yhzp_098]` `[trigger: 印绶破]` `[factor_trigger: shishen_yinshou AND po AND ke_mu AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 总结]` 印绶破者克母。 → 《渊海子平·论印绶》"""
    normalized_text_zh: str = """"""
    subject: str = "论印绶"
    factor_refs: list = ['direct_seal', 'wealth_breaking_seal']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论印绶_001_L1",
    )
    version: str = "1.0.0"
