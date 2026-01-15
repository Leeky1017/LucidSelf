"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439658
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
    semantic_id="dvd_v1.0.0_ancestor_祖先_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ancestor祖先(SemanticEntry):
    """
    ### Source Text

**Dreams - Positive**: If the ancestor you dream of is someone you knew personally ...
    """
    
    original_text: str = """### Source Text

**Dreams - Positive**: If the ancestor you dream of is someone you knew personally and had a good influence in your life, then they would represent something positive concerning yourself. Example: A man dreamed of his grandmother (now deceased) telling him to go out and face his fears. In reality she brought him to the Lord and was a good influence. In his dream, she represented the Holy Spirit, leading him to victory.

**Dreams - Negative**: If you dream of deceased ancestors whom you knew 'visiting' you in your dreams, there is likely some demonic bondage you are still under. The Word is very clear on communicating with the dead—many still receive 'spirits' who come in the name of their long-lost dead ones.

If you dream of ancestors you had never met, they could represent things of the past you are still holding on to and need to let go of. Perhaps sin or bad experiences in your past that you cannot let go. Ancestors could also speak of generational traditions and morals that control you.

**Visions - Positive**: (Not specifically mentioned)

**Visions - Negative**: (Not specifically mentioned)

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Ancestor | Deceased family member | Past influence, positive or negative |
| Good-influence ancestor | Positive past relationship | May represent Holy Spirit |
| Visiting spirits | Deceased appearing in dreams | Possible demonic bondage |

### English Paraphrase

Ancestor dreams depend on your actual relationship with them. **Positive**: If you knew the ancestor personally and they were a good influence, they may represent something positive—even the Holy Spirit guiding you (like the grandmother example leading to face fears). **Negative**: Deceased ancestors "visiting" you suggests demonic bondage—the Bible forbids communicating with the dead. Ancestors you never met represent things from the past you're holding onto: sins, hurts, guilt. May also represent generational traditions/morals still controlling you—need to move on in Christ.

### Chinese Interpretation（完整对等诠释）

祖先梦境取决于你与他们的实际关系。**正面**：如果你亲自认识这位祖先且他们有好的影响，可能代表正面的事——甚至是圣灵引导你（如祖母的例子带领面对恐惧）。**负面**：已故祖先「来访」暗示魔鬼捆绑——圣经禁止与死人交流。从未见过的祖先代表你仍紧抓的过去：罪、伤害、内疚。也可能代表仍控制你的世代传统/道德——需要在基督里前进。

### Core Points

- 祖先梦 = 取决于实际关系
- 正面影响的祖先 → 可能代表圣灵引导
- 已故祖先「来访」→ 可能是魔鬼捆绑
- 从未见过的祖先 → 过去的事物/罪/伤害
- 世代传统/道德的控制
- 需要在基督里放下、前进

### Narrative Snippets

- `[ns_dav_a023]` `[trigger: 梦祖先]` `[factor_trigger: dream_symbol_ancestor]` `[role: 主干]` Ancestor dreams depend on your actual relationship with them—positive influence or demonic bondage. → Dreams Dictionary #Ancestor
- `[ns_dav_a024]` `[trigger: 好影响祖先]` `[factor_trigger: dream_symbol_ancestor AND actual_relationship]` `[role: 条件分支]` Good-influence ancestor may represent Holy Spirit guiding you to victory. → Dreams Dictionary #Ancestor
- `[ns_dav_a025]` `[trigger: 来访祖先]` `[factor_trigger: dream_symbol_ancestor AND actual_relationship AND bondage_state]` `[role: 条件分支]` Deceased ancestors "visiting" = likely demonic bondage, Bible forbids communicating with dead. → Dreams Dictionary #Ancestor
- `[ns_dav_a026]` `[trigger: 陌生祖先]` `[factor_trigger: dream_symbol_ancestor AND dream_unknown]` `[role: 条件分支]` Unknown ancestors = past things you're holding onto—sins, hurts, generational patterns. → Dreams Dictionary #Ancestor"""
    normalized_text_zh: str = """"""
    subject: str = "Ancestor 祖先"
    factor_refs: list = ['dream_symbol_ancestor', 'spirit_visiting', 'pattern_generational']
    
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_ancestor_祖先_001_L1",
    )
    version: str = "1.0.0"
