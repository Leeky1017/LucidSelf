"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439781
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
    semantic_id="dvd_v1.0.0_authorities_权柄人物_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Authorities权柄人物(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: Those people who are senior to you and have authority over y...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: Those people who are senior to you and have authority over you—parents, boss, pastor, or any figure set over you in administrative or spiritual position.

**Dreams - Positive**: Dreaming of authority positively = your leadership being accepted, growing in that area. May mean attaining to that level of authority. Worldly authorities could speak of archetypes and mindsets controlling your thinking.

**Dreams - Negative**: In bondage to authority = under oppression or attack. Being controlled by influences not of God, brought under domination against the Word. May also indicate you are trying to dominate others.

**Visions - Positive** (Rom 13:1): "There is no authority except from God." Highest authority = the Lord. Often depicted as umbrella in spirit—holes in umbrella or not standing under it = authority not covering correctly, under attack.

**Visions - Negative**: To rebel against authority God placed you under = rebelling against Lord Himself.

**See also**: Father

### English Paraphrase

Authorities = those with leadership over you (parents, boss, pastor). **Positive**: Authority dream = leadership accepted, growing, attaining authority level. **Negative**: Bondage to authority = oppression, attack, ungodly control. Or YOU trying to dominate others. Visions: Umbrella = covering of authority—holes or outside umbrella = not properly covered, under attack. All authority from God (Rom 13:1); rebelling against God-placed authority = rebelling against God.

### Chinese Interpretation（完整对等诠释）

权柄人物 = 那些对你有领导权的人（父母、老板、牧师）。**正面**：权柄梦 = 领导被接受，在该领域成长，达到权柄层级。**负面**：被权柄捆绑 = 压迫、攻击、不属神的控制。或者你试图控制他人。异象：雨伞 = 权柄的遮盖——伞有洞或站在伞外 = 没有正确遮盖，正受攻击。所有权柄来自神（罗13:1）；悖逆神所设立的权柄 = 悖逆神自己。

### Narrative Snippets

- `[ns_dav_a063]` `[trigger: 梦权柄]` `[factor_trigger: dream_symbol_authorities]` `[role: 主干]` Authorities = leadership figures—positive = growth, negative = oppression or dominating others. → Dreams Dictionary #Authorities
- `[ns_dav_a064]` `[trigger: 权柄正面]` `[factor_trigger: dream_symbol_authorities AND authority_relation]` `[role: 条件分支]` Authority accepted = leadership growing, attaining that level of authority. → Dreams Dictionary #Authorities
- `[ns_dav_a065]` `[trigger: 雨伞异象]` `[factor_trigger: dream_symbol_authorities AND authority_relation]` `[role: 条件分支]` Umbrella = authority covering—holes or outside = not properly covered, under attack. → Dreams Dictionary #Authorities"""
    normalized_text_zh: str = """"""
    subject: str = "Authorities 权柄人物"
    factor_refs: list = []
    
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
        l1_anchor="dvd_v1.0.0_authorities_权柄人物_001_L1",
    )
    version: str = "1.0.0"
