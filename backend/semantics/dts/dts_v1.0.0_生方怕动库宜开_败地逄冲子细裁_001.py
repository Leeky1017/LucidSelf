"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997192
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
    semantic_id="dts_v1.0.0_生方怕动库宜开_败地逄冲子细裁_001",
    book_id="dts",
    engine_id="bazi"
)
class 生方怕动库宜开败地逄冲子细裁(SemanticEntry):
    """
    - **原文（source_text）**：
  生方怕动，库宜开，败地逄冲，子细裁.

- 原注（原文注解）：
  　　寅申巳亥，四生也；忌冲动。辰戌丑未，四库也；宜冲开.子午卯酉，四败也，有逄合而...
    """
    
    original_text: str = """- **原文（source_text）**：
  生方怕动，库宜开，败地逄冲，子细裁.

- 原注（原文注解）：
  　　寅申巳亥，四生也；忌冲动。辰戌丑未，四库也；宜冲开.子午卯酉，四败也，有逄合而喜冲者，不若生地之必不可冲也；有逄冲而喜合者，不若库地之必不可闭也，宜详细裁之.

- 分字分词释义：
  - 生方（地）：四生地（寅申巳亥），生发之位.
  - 怕动：不喜被冲动，否则根气动摇.
  - 库：四库地（辰戌丑未），为藏蓄之地.
  - 宜开：喜冲开以发用（合开库）.
  - 败地：四败地（子午卯酉）.
  - 逄冲/逄合：遇冲、遇合（“逄”通“逢”）.
  - 子细裁：细致裁量，不可一概而论.

- **规范化释义（primary_lang_explained）**：
  生地重在护根，忌被冲扰；库地重在开阖，宜得冲开以发藏；败地有时喜冲、有时喜合，需按具体组合细致裁量。

- **次语种完整诠释（secondary_lang_full）**:  
  Birth positions (Yin, Shen, Si, Hai) primarily protect roots and dislike being disturbed; storage vaults (Chen, Xu, Chou, Wei) need to be opened at the right time to release what is stored; defeat locations (Zi, Wu, Mao, You) sit at a more fragile stage and may benefit from either clashes or combinations depending on the broader structure. In practice you must judge case by case instead of applying one rigid rule to all three types.

- **核心要点**：
  - 生方护根：四生地重在护根，忌被冲动摇根气
  - 库地宜开：四库地宜得冲开，方能发用
  - 败地权衡：四败地或喜冲或喜合，须按局细察
  - 取用策略：先分清生库败，再定护根、开库或权衡之法

- **详细解说**：
  生方指寅申巳亥等长生之地，根气初发，最怕被冲折根基；库地指辰戌丑未等墓库之位，本为藏蓄之所，宜在合适的时机被冲开或合开，方能把所藏之物发用；败地指子午卯酉等旺极而败之位，有时需要冲开，有时反而喜合以收敛，不能一概而论。实际断局时，必须先辨清某支是生方、库地还是败地，再结合用神路径与岁运结构，分别考虑是护根、开库，还是在败地上做精细权衡。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_061]` `[trigger: 地支落生方逢冲]` `[factor_trigger: dizhi_birth_storage_defeat_type==四生 AND root_stability_index==被冲动摇]` `[role: 主干]` 生方怕动，长生之地被冲，多主根气动摇，不宜轻言其吉。 → 《滴天髓·地支论》#生方库败
  - `[ns_dts_062]` `[trigger: 地支落库地被冲开]` `[factor_trigger: dizhi_birth_storage_defeat_type==四库 AND vault_opening_state==全开|部分开]` `[role: 主干依赖]` 库地逢冲或合而开，多主积蓄之物发用，为库宜开之象。 → 《滴天髓·地支论》#生方库败
  - `[ns_dts_063]` `[trigger: 地支在败地逢冲合]` `[factor_trigger: dizhi_birth_storage_defeat_type==四败 AND defeat_adjudication==高]` `[role: 条件分支]` 败地逢冲或逢合，或损或利，全凭局中制化与用神，须子细裁量。 → 《滴天髓·地支论》#生方库败
  - `[ns_dts_137]` `[trigger: 库不开则藏不出]` `[factor_trigger: vault_opening_state==闭 AND dizhi_birth_storage_defeat_type==四库]` `[role: 例外处理]` 库地若无冲合引动，内蓄之物难以发用，多主潜力未开。 → 《滴天髓·地支论》#生方库败
  - `[ns_dts_138]` `[trigger: 生库败三分判]` `[factor_trigger: clash_effect_mode IN {护根, 开库, 个案权衡}]` `[role: 总结]` 断冲之吉凶，先辨生库败，再定护根、开库或权衡之法。 → 《滴天髓·地支论》#生方库败"""
    normalized_text_zh: str = """"""
    subject: str = "生方怕动库宜开，败地逄冲子细裁."
    factor_refs: list = ['shengfang', 'kudi', 'baidi', 'padong', 'kuyikai', 'zixicai', 'dizhi_birth_position', 'dizhi_storage_vault', 'dizhi_defeat_position', 'hugen_strategy', 'kaichu_strategy', 'quanheng_strategy']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_生方怕动库宜开_败地逄冲子细裁_001_L1",
    )
    version: str = "1.0.0"
